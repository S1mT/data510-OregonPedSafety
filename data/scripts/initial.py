import pandas as pd
import os

def run_pipeline():
    START_YEAR = 2015
    END_YEAR = 2024
    RAW_DIR = 'data/raw'
    INTERIM_DIR = 'data/interim'
    PROCESSED_DIR = 'data/processed'

    os.makedirs(INTERIM_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    target_files = ['accident', 'person', 'pbtype', 'vehicle', 'weather']

    print("PHASE 1: Extracting Oregon Records & Cleaning BOMs")
    
    for year in range(START_YEAR, END_YEAR + 1):
        # Look for the standard NHTSA folder structure inside data/raw/
        folder_path = os.path.join(RAW_DIR, f'FARS{year}NationalCSV')
        
        if not os.path.exists(folder_path):
            print(f"  -> Skipping {year}: Directory {folder_path} not found.")
            continue
            
        actual_files_in_dir = os.listdir(folder_path)
        
        for target in target_files:
            matched_file = next((f for f in actual_files_in_dir if f.lower() == f"{target}.csv".lower()), None)
            
            if matched_file:
                file_path = os.path.join(folder_path, matched_file)
                df = pd.read_csv(file_path, low_memory=False, encoding='latin1')
                
                # Strip invisible characters (BOMs) from column names
                df.columns = df.columns.str.replace(r'[^A-Za-z0-9_]', '', regex=True).str.upper()
                
                if 'STATE' in df.columns:
                    df_or = df[df['STATE'] == 41]
                    out_name = f'oregon_{target}_{year}.csv'
                    df_or.to_csv(os.path.join(INTERIM_DIR, out_name), index=False)
            else:
                print(f"  WARNING: '{target}.csv' not found in {year} raw folder.")

    print("PHASE 2: Building the Infrastructure Master Matrix")

    person_keys = ['STATE', 'STATENAME', 'ST_CASE', 'VEH_NO', 'PER_NO']
    crash_keys = ['STATE', 'STATENAME', 'ST_CASE']

    def collapse_data(df, keys):
        if df.empty: return df
        return df.groupby(keys, as_index=False).agg(lambda x: ' | '.join(x.dropna().astype(str).unique()))

    def load_interim(target, year, keys):
        path = os.path.join(INTERIM_DIR, f'oregon_{target}_{year}.csv')
        return pd.read_csv(path, low_memory=False) if os.path.exists(path) else pd.DataFrame(columns=keys)

    all_years_data = []

    for year in range(START_YEAR, END_YEAR + 1):
        acc_path = os.path.join(INTERIM_DIR, f'oregon_accident_{year}.csv')
        if not os.path.exists(acc_path):
            continue
            
        print(f"Joining relational tables for {year}...")
        
        acc = pd.read_csv(acc_path, low_memory=False)
        per = load_interim('person', year, person_keys)
        pb = load_interim('pbtype', year, person_keys)
        veh = load_interim('vehicle', year, crash_keys)
        weather = load_interim('weather', year, crash_keys)

        # Drop redundant basic columns from person to avoid _x/_y collisions
        redundant_cols = ['YEAR', 'MONTHNAME', 'DAY_WEEKNAME', 'HOURNAME', 'RUR_URBNAME', 'FUNC_SYSNAME']
        per = per.drop(columns=[col for col in redundant_cols if col in per.columns])

        # Explicit Infrastructure Extraction
        veh_target_cols = [
            'ST_CASE', 'VEH_NO', 
            'VSPD_LIM', 'VSPD_LIMNAME',   
            'VTRAFCON', 'VTRAFCONNAME',   
            'VTRAFWAY', 'VTRAFWAYNAME'    
        ]
        veh_cols_to_keep = [col for col in veh_target_cols if col in veh.columns]
        veh_subset = veh[veh_cols_to_keep]

        weather_grp = collapse_data(weather, crash_keys)

        # Merge Sequence
        df = pd.merge(per, pb, on=person_keys, how='inner')
        df = pd.merge(df, acc, on=crash_keys, how='left')
        df = pd.merge(df, weather_grp, on=crash_keys, how='left')
        df = pd.merge(df, veh_subset, left_on=['ST_CASE', 'STR_VEH'], right_on=['ST_CASE', 'VEH_NO'], how='left')

        # Standardize Weather
        if 'WEATHERNAME_y' in df.columns:
            df['WEATHER_FINAL'] = df['WEATHERNAME_y'].fillna(df.get('WEATHERNAME_x', df.get('WEATHERNAME')))
        elif 'WEATHERNAME' in df.columns:
            df['WEATHER_FINAL'] = df['WEATHERNAME']
        else:
            df['WEATHER_FINAL'] = 'Unknown'

        # Final Vision Zero Whitelist
        core_whitelist = [
            'ST_CASE', 'PER_NO', 'AGE', 'SEXNAME', 'PBPTYPENAME',  
            'YEAR', 'MONTHNAME', 'DAY_WEEKNAME', 'HOURNAME', 
            'LGT_CONDNAME', 'WEATHER_FINAL',
            'RUR_URBNAME', 'FUNC_SYSNAME', 'TYP_INTNAME', 'REL_ROADNAME', 'WRK_ZONENAME', 
            'LATITUDE', 'LONGITUD',
            'PEDLOCNAME', 'BIKELOCNAME', 'PEDPOSNAME', 'BIKEPOSNAME', 'PEDDIRNAME', 'BIKEDIRNAME'
        ]
        
        final_whitelist = core_whitelist + [col for col in veh_cols_to_keep if col not in ['ST_CASE', 'VEH_NO']]
        available_columns = [col for col in final_whitelist if col in df.columns]
        
        df_final = df[available_columns].copy()
        df_final.columns = df_final.columns.str.replace('_FINAL', '', regex=False)
        all_years_data.append(df_final)

    master_df = pd.concat(all_years_data, ignore_index=True)
    master_df = master_df.fillna('None / Unknown')
    
    output_name = os.path.join(PROCESSED_DIR, 'FARSinfrastructure.csv')
    master_df.to_csv(output_name, index=False)
    
    print(f"\nSUCCESS! Master dataset saved to '{output_name}'")
    print(f"Total Dimensions: {master_df.shape[0]} victims | {master_df.shape[1]} variables")

if __name__ == "__main__":
    run_pipeline()