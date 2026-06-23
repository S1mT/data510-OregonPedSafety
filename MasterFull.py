import pandas as pd
import os

def build_multi_year_datasets(input_dir, output_dir, start_year=2015, end_year=2024):
    os.makedirs(output_dir, exist_ok=True)

    person_keys = ['STATE', 'STATENAME', 'ST_CASE', 'VEH_NO', 'PER_NO']
    crash_keys = ['STATE', 'STATENAME', 'ST_CASE']

    def collapse_data(df, keys):
        if df.empty:
            return df
        return df.groupby(keys, as_index=False).agg(lambda x: ' | '.join(x.dropna().astype(str).unique()))

    def load_optional_file(filepath, keys):
        if os.path.exists(filepath):
            return pd.read_csv(filepath, low_memory=False)
        else:
            return pd.DataFrame(columns=keys)

    all_years_data = []

    for year in range(start_year, end_year + 1):
        print(f"Processing Year: {year}...")

        acc_path = f'{input_dir}/oregon_accident_{year}.csv'
        per_path = f'{input_dir}/oregon_person_{year}.csv'
        pb_path  = f'{input_dir}/oregon_pbtype_{year}.csv'
        veh_path = f'{input_dir}/oregon_vehicle_{year}.csv'

        if not all(os.path.exists(p) for p in [acc_path, per_path, pb_path, veh_path]):
            print(f"  -> Skipping {year}: Missing core files.")
            continue

        acc = pd.read_csv(acc_path, low_memory=False)
        per = pd.read_csv(per_path, low_memory=False)
        pb = pd.read_csv(pb_path, low_memory=False)
        veh = pd.read_csv(veh_path, low_memory=False)

        # We only need the weather file now for our infrastructure list
        weather = load_optional_file(f'{input_dir}/oregon_weather_{year}.csv', crash_keys)

        # Prevent basic redundant _x and _y columns from accident/person overlap
        redundant_cols = ['YEAR', 'MONTHNAME', 'DAY_WEEKNAME', 'HOURNAME', 'RUR_URBNAME', 'FUNC_SYSNAME']
        per = per.drop(columns=[col for col in redundant_cols if col in per.columns])

        # --- Explicit Vehicle/Infrastructure Extraction ---
        # Grabbing both the numeric codes and the text names as requested
        veh_target_cols = [
            'ST_CASE', 'VEH_NO', 
            'VSPD_LIMNAME',   # Posted Speed Limit Text
            'VTRAFCONNAME',   # Traffic Control Device Text
            'VTRAFWAYNAME'    # Trafficway Flow Text
        ]
        
        veh_cols_to_keep = [col for col in veh_target_cols if col in veh.columns]
        veh_subset = veh[veh_cols_to_keep]
        
        veh_cols_to_keep = [col for col in veh_target_cols if col in veh.columns]
        veh_subset = veh[veh_cols_to_keep]

        # Collapse 1-to-many
        weather_grp = collapse_data(weather, crash_keys)

        # Clean Joins (Stripped out all behavioral/crash factor files)
        df = pd.merge(per, pb, on=person_keys, how='inner')
        df = pd.merge(df, acc, on=crash_keys, how='left')
        df = pd.merge(df, weather_grp, on=crash_keys, how='left')
        df = pd.merge(df, veh_subset, left_on=['ST_CASE', 'STR_VEH'], right_on=['ST_CASE', 'VEH_NO'], how='left')

        # =========================================================
        # --- THE BRIDGE: Historical Data Extraction ---
        # =========================================================
        
        # 1. Standardize Weather
        if 'WEATHERNAME_y' in df.columns:
            df['WEATHER_FINAL'] = df['WEATHERNAME_y'].fillna(df.get('WEATHERNAME_x', df.get('WEATHERNAME')))
        elif 'WEATHERNAME' in df.columns:
            df['WEATHER_FINAL'] = df['WEATHERNAME']
        else:
            df['WEATHER_FINAL'] = 'Unknown'

        # --- TRIM TO EXACT REQUESTED WHITELIST ---
        core_whitelist = [
            'ST_CASE', 'PER_NO', 'AGE', 'SEXNAME', 'PBPTYPENAME',  
            'YEAR', 'MONTHNAME', 'DAY_WEEKNAME', 'HOURNAME', 
            'LGT_CONDNAME', 'WEATHER_FINAL',
            'RUR_URBNAME', 'FUNC_SYSNAME', 'TYP_INTNAME', 'REL_ROADNAME', 'WRK_ZONENAME', 
            'LATITUDE', 'LONGITUD',
            'PEDLOCNAME', 'BIKELOCNAME', 'PEDPOSNAME', 'BIKEPOSNAME', 'PEDDIRNAME', 'BIKEDIRNAME'
        ]
        
        # Append the explicit vehicle/infrastructure columns we extracted earlier
        final_whitelist = core_whitelist + [col for col in veh_cols_to_keep if col not in ['ST_CASE', 'VEH_NO']]
        available_columns = [col for col in final_whitelist if col in df.columns]
        
        df_final = df[available_columns].copy()
        
        # Strip the "_FINAL" tags so WEATHER_FINAL becomes WEATHER
        df_final.columns = df_final.columns.str.replace('_FINAL', '', regex=False)
        
        all_years_data.append(df_final)

    print("\n" + "="*40)
    print("Concatenating all years into unified master dataset...")
    
    master_df = pd.concat(all_years_data, ignore_index=True)
    
    # Final ML Polish: Fill any remaining stray NaNs 
    master_df = master_df.fillna('None / Unknown')
    
    output_name = f'{output_dir}/OregonFARSMaster.csv'
    master_df.to_csv(output_name, index=False)
    
    print(f"SUCCESS! Master dataset saved as '{output_name}'")
    print(f"Total Dataset Shape: {master_df.shape[0]} total victims | {master_df.shape[1]} variables")
    print("="*40 + "\n")

if __name__ == "__main__":
    INPUT_FOLDER = 'raw'
    OUTPUT_FOLDER = 'processed'
    build_multi_year_datasets(INPUT_FOLDER, OUTPUT_FOLDER, 2015, 2024)