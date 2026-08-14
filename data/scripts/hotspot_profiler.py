import pandas as pd
import numpy as np

def calculate_radius_meters(lat_center, lon_center, lats, lons):
    """Calculates the max Haversine distance from the center to the furthest incident."""
    r = 6371000 # Radius of Earth in meters
    phi1, phi2 = np.radians(lat_center), np.radians(lats)
    delta_phi = np.radians(lats - lat_center)
    delta_lambda = np.radians(lons - lon_center)
    
    a = np.sin(delta_phi / 2.0) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2.0) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distances = r * c
    
    return np.max(distances) + 20

# 1. Load the clustered spatial data
df = pd.read_csv('data/processed/FARSclusters.csv')

# 2. Filter out the noise (-1 are crashes that didn't form a cluster)
df_clusters = df[df['SPATIAL_CLUSTER'] != -1]

# 3. Identify ALL hotspots with >1 UNIQUE INCIDENT
cluster_stats = df_clusters.groupby('SPATIAL_CLUSTER').agg(
    Total_Fatalities=('ST_CASE', 'count'),
    Unique_Incidents=('ST_CASE', 'nunique')
).reset_index()

cluster_stats = cluster_stats.sort_values(by=['Unique_Incidents', 'Total_Fatalities'], ascending=[False, False])

# Grab every cluster ID that had more than 1 unique incident
systemic_clusters = cluster_stats[cluster_stats['Unique_Incidents'] > 1]
target_ids = systemic_clusters['SPATIAL_CLUSTER'].tolist()

# --- Extract and save the individual incidents for mapping ---
systemic_incidents = df[df['SPATIAL_CLUSTER'].isin(target_ids)].copy()
incidents_path = 'data/processed/systemic_hotspots_incidents.csv'
systemic_incidents.to_csv(incidents_path, index=False)

# 4. Expanded Infrastructure Features
features_to_compare = [
    'RUR_URBNAME',      # Rural vs Urban
    'FUNC_SYSNAME',     # Road Type
    'VTRAFWAYNAME',     # Road Division (Barrier, Painted, Two-Way)
    'VSPD_LIMNAME',     # Posted Speed Limit
    'TYP_INTNAME',      # Intersection Type
    'VTRAFCONNAME',     # Traffic Controls
    'LGT_CONDNAME',     # Lighting Conditions
    'WEATHER',          # Weather Conditions
    'PEDPOSNAME'        # Where the pedestrian was
]

profiles = []

print(f"=== EXTRACTING {len(target_ids)} SYSTEMIC HOTSPOTS ===\n")

for cluster_id in target_ids:
    cluster_data = df[df['SPATIAL_CLUSTER'] == cluster_id]
    total_fatalities = len(cluster_data)
    unique_incidents = cluster_data['ST_CASE'].nunique()
    
    # Extract the timeline of the crashes
    years_active = sorted(cluster_data['YEAR'].unique().tolist())
    years_str = ", ".join(map(str, years_active))
    
    avg_lat = cluster_data['LATITUDE'].mean()
    avg_lon = cluster_data['LONGITUD'].mean()
    radius_m = calculate_radius_meters(avg_lat, avg_lon, cluster_data['LATITUDE'], cluster_data['LONGITUD'])
    
    # Clean ages (ignore 998, 999 FARS unknown codes)
    valid_ages = cluster_data[cluster_data['AGE'] < 120]['AGE']
    median_age = valid_ages.median() if not valid_ages.empty else "Unknown"
    
    profile = {
        'Cluster_ID': cluster_id,
        'Unique_Incidents': unique_incidents,
        'Total_Fatalities': total_fatalities,
        'Years_Active': years_str,
        'Centroid_Latitude': round(avg_lat, 5),
        'Centroid_Longitude': round(avg_lon, 5),
        'Radius_Meters': round(radius_m, 1),
        'Median_Age': median_age
    }
    
    for feature in features_to_compare:
        profile[f'Dominant_{feature}'] = cluster_data[feature].mode()[0]
        
    profiles.append(profile)

profile_df = pd.DataFrame(profiles)
profile_path = 'data/processed/systemic_hotspots_profile.csv'
profile_df.to_csv(profile_path, index=False)

print(f"SUCCESS: Extracted {len(systemic_incidents)} incidents across {len(target_ids)} clusters.")
print(f"Saved incidents to: {incidents_path}")
print(f"Saved profiles to: {profile_path}")

# --- POOLED SYSTEMIC ANALYSIS ---
print("\n=== SYSTEMIC DNA OF REPEAT-FATALITY LOCATIONS ===")
pooled_data = df[df['SPATIAL_CLUSTER'].isin(target_ids)]

key_features = features_to_compare

for feature in key_features:
    counts = pooled_data[feature].value_counts(normalize=True) * 100
    print(f"-- {feature.replace('NAME', '')} --")
    for trait, pct in counts.head(2).items():
        print(f"   {round(pct, 1)}% : {trait}")
    print("")

# --- NEW: OVERALL STATEWIDE BASELINE ---
print("\n=== OVERALL STATEWIDE BASELINE (ALL FATALITIES) ===")
print(f"Analysis of all {len(df)} fatal incidents in the dataset.\n")

for feature in key_features:
    # Use the entire original 'df' instead of 'pooled_data'
    counts = df[feature].value_counts(normalize=True) * 100
    print(f"-- {feature.replace('NAME', '')} --")
    for trait, pct in counts.head(2).items():
        print(f"   {round(pct, 1)}% : {trait}")
    print("")