import pandas as pd
import os

def extract_all_oregon_files(start_year=2021, end_year=2022):
    target_files = [
        'accident', 'person', 'pbtype', 'nmcrash',
        'nmprior', 'nmimpair', 'nmdistract', 'safetyeq',
        'weather', 'crashrf', 'vehicle'
    ]

    # Saving directly into your 'raw' folder to match the Mac setup
    out_dir = 'Oregon_Cleaned_FARS'
    os.makedirs(out_dir, exist_ok=True)

    for year in range(start_year, end_year + 1):
        folder_name = f'FARS{year}NationalCSV'
        
        if not os.path.exists(folder_name):
            print(f"Directory {folder_name} not found.")
            continue
            
        print(f"\n--- Extracting Oregon Data for {year} ---")
        actual_files_in_dir = os.listdir(folder_name)
        
        for target in target_files:
            matched_file = next((f for f in actual_files_in_dir if f.lower() == f"{target}.csv".lower()), None)
            
            if matched_file:
                file_path = os.path.join(folder_name, matched_file)
                # Load the file
                df = pd.read_csv(file_path, low_memory=False, encoding='latin1')
                
                # --- THE FIX: Strip invisible characters from column names ---
                df.columns = df.columns.str.replace(r'[^A-Za-z0-9_]', '', regex=True).str.upper()
                
                if 'STATE' in df.columns:
                    df_or = df[df['STATE'] == 41]
                    out_name = f'oregon_{target}_{year}.csv'
                    out_path = os.path.join(out_dir, out_name)
                    
                    df_or.to_csv(out_path, index=False)
                    print(f"  Saved {out_name} ({len(df_or)} rows)")
            else:
                print(f"  WARNING: '{target}.csv' not found in {year} raw folder.")

if __name__ == "__main__":
    extract_all_oregon_files(2015, 2024)