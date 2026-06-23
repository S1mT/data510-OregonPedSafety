## Raw Data Provenance
The analysis relies on raw data originating from the National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS) from 2015 to 2024. 

- Raw Data Download Source: https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/FARS/
- FARS Analytical User’s Manual: https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/813794 

Due to the relational structure of the FARS database and the massive size of the national files, the raw data is not committed to this repository. The raw extraction process relies on the following annual national tables stored locally in `data/raw/`:
* `accident.csv` (Crash-level environmental and temporal factors)
* `person.csv` (Demographics and non-motorist identifiers)
* `pbtype.csv` (Pedestrian/Bicyclist positioning relative to infrastructure)
* `vehicle.csv` (Infrastructure features governing the striking vehicle)
* `weather.csv` (Supplemental multi-condition weather reporting)

## Dataset registry

### Dataset 1: Oregon FARS Master Dataset (2015-2024)

- **Source:** National Highway Traffic Safety Administration (NHTSA) FARS FTP.
- **License:** Public Domain (U.S. Government Open Data).
- **Date pulled:** 2026-06-22
- **Approximate size:** 1,049 rows, 25 columns
- **Owner on this project:** Simon Thompson
- **Where it lives in this repo:** `data/processed/OregonFARSMaster.csv`
- **Ethics / consent notes:** Publicly available fatal crash data. Anonymized by NHTSA; contains no Personally Identifiable Information (PII) or Protected Health Information (PHI). Victim identification relies strictly on randomized `ST_CASE` and `PER_NO` indexing.
- **How to fetch (for a teammate cloning fresh):** 1. Download the raw national CSV zip folders for 2015-2024 from the NHTSA FARS data portal. 
  2. Run `clean.py` to extract and parse the Oregon-specific records (stripping invisible BOM characters) into `data/raw/`.
  3. Execute `MasterFull.py` to merge the relational tables and compile this final processed dataset.
