import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import requests
import numpy as np

def run_enrichment():
    # Insert your university API key here
    CENSUS_API_KEY = "e58f8758e782b6351da7f3c36b5a3b6d8145328d"
    INPUT_FILE = 'data/processed/FARSinfrastructure.csv'
    OUTPUT_FILE = 'data/processed/FARSmaster.csv'

    print("PHASE 1: Spatial Join (Point-in-Polygon)")
    
    df = pd.read_csv(INPUT_FILE)
    
    # Filter out FARS 'ghost' coordinates (99.9999, 88.8888)
    valid_coords = df[(df['LATITUDE'] < 50) & (df['LATITUDE'] > 40) & 
                      (df['LONGITUD'] < -110) & (df['LONGITUD'] > -130)].copy()

    # Convert Pandas to Spatial GeoDataFrame (WGS84 projection)
    geometry = [Point(xy) for xy in zip(valid_coords.LONGITUD, valid_coords.LATITUDE)]
    fars_gdf = gpd.GeoDataFrame(valid_coords, crs="EPSG:4326", geometry=geometry)

    print("Downloading Oregon Census Tract shapefiles...")
    tracts_url = "https://www2.census.gov/geo/tiger/TIGER2020/TRACT/tl_2020_41_tract.zip"
    tracts_gdf = gpd.read_file(tracts_url)

    # Align CRSs and execute the spatial join
    fars_gdf = fars_gdf.to_crs(tracts_gdf.crs)
    joined_gdf = gpd.sjoin(fars_gdf, tracts_gdf, how="inner", predicate="within")

    cols_to_keep = list(df.columns) + ['GEOID', 'NAMELSAD'] 
    spatial_df = pd.DataFrame(joined_gdf[cols_to_keep])

    print("PHASE 2: Census API Demographic Enrichment")

    # Base Demographics + Equity Variables
    variables = (
        "NAME,"
        "B19013_001E,"              # Median Income
        "B03002_001E,B03002_003E,B03002_004E,B03002_012E," # Race/Ethnicity
        "B08301_001E,B08301_010E,B08301_019E" # Total Commuters, Transit, Walk
    )
    
    url = f"https://api.census.gov/data/2022/acs/acs5?get={variables}&for=tract:*&in=state:41&key={CENSUS_API_KEY}"

    print("Pulling ACS 5-Year Estimates for Oregon...")
    response = requests.get(url)
    data = response.json()
    acs_df = pd.DataFrame(data[1:], columns=data[0])

    acs_df = acs_df.rename(columns={
        # Demographic Variables
        'B19013_001E': 'MEDIAN_INCOME',
        'B03002_001E': 'TOTAL_POPULATION',
        'B03002_003E': 'POP_WHITE',
        'B03002_004E': 'POP_BLACK',
        'B03002_012E': 'POP_HISPANIC',
        'B08301_001E': 'TOTAL_COMMUTERS',
        'B08301_010E': 'COMMUTE_TRANSIT',
        'B08301_019E': 'COMMUTE_WALK',
    })

    # Convert all demographic strings to numeric
    numeric_cols = [
        'MEDIAN_INCOME', 'TOTAL_POPULATION', 'POP_WHITE', 'POP_BLACK', 'POP_HISPANIC',
        'TOTAL_COMMUTERS', 'COMMUTE_TRANSIT', 'COMMUTE_WALK'
    ]
    for col in numeric_cols:
        acs_df[col] = pd.to_numeric(acs_df[col], errors='coerce')

    # Clean Census Suppression Codes (Convert massive negatives to NaN across all numeric columns)
    for col in numeric_cols:
        acs_df[col] = acs_df[col].apply(lambda x: np.nan if x < 0 else x)


    # CALCULATING EQUITY PERCENTAGES (Safely handling 0 denominators)

    # Race & Ethnicity
    acs_df['PCT_WHITE'] = np.where(acs_df['TOTAL_POPULATION'] > 0, (acs_df['POP_WHITE'] / acs_df['TOTAL_POPULATION']) * 100, np.nan)
    acs_df['PCT_BLACK'] = np.where(acs_df['TOTAL_POPULATION'] > 0, (acs_df['POP_BLACK'] / acs_df['TOTAL_POPULATION']) * 100, np.nan)
    acs_df['PCT_HISPANIC'] = np.where(acs_df['TOTAL_POPULATION'] > 0, (acs_df['POP_HISPANIC'] / acs_df['TOTAL_POPULATION']) * 100, np.nan)

    # Exposure Risk: Percentage of workers who commute via Transit OR Walking
    acs_df['PCT_TRANSIT_WALK_COMMUTE'] = np.where(acs_df['TOTAL_COMMUTERS'] > 0, ((acs_df['COMMUTE_TRANSIT'] + acs_df['COMMUTE_WALK']) / acs_df['TOTAL_COMMUTERS']) * 100, np.nan)
    
    # Standardize 11-digit GEOID to match shapefile
    acs_df['GEOID'] = acs_df['state'] + acs_df['county'] + acs_df['tract']
    
    # Select final columns to merge
    acs_subset = acs_df[[
        'GEOID', 'MEDIAN_INCOME', 'TOTAL_POPULATION', 
        'PCT_WHITE', 'PCT_BLACK', 'PCT_HISPANIC',
        'PCT_TRANSIT_WALK_COMMUTE'
    ]]

    # Final Relational Merge
    spatial_df['GEOID'] = spatial_df['GEOID'].astype(str)
    final_equity_df = pd.merge(spatial_df, acs_subset, on='GEOID', how='inner')

    final_equity_df.to_csv(OUTPUT_FILE, index=False)
    print(f"\nSUCCESS! Fully integrated spatial/demographic dataset saved to '{OUTPUT_FILE}'")

if __name__ == "__main__":
    run_enrichment()