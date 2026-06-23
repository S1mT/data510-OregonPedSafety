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

## Data Architecture & Relational Merges

The raw FARS database is highly relational. A single fatal incident requires data to be stitched together from multiple independent tables. To flatten this into the analytical `OregonFARSMaster.csv` matrix, the Python pipeline executes a precise sequence of SQL-style joins.

### Primary and Foreign Keys
NHTSA uses a hierarchical indexing system to link records across the database:
* `ST_CASE`: The unique identifier for the crash event itself.
* `VEH_NO`: The identifier for a specific vehicle within that crash.
* `PER_NO`: The identifier for a specific person within that vehicle (or a specific non-motorist).

### The Merge Sequence
The pipeline builds the dataset horizontally, starting with the individual victim and appending environmental context outwards:

**1. The Victim Base (Inner Join)**
* **Tables:** `person.csv` + `pbtype.csv`
* **Keys:** `['STATE', 'STATENAME', 'ST_CASE', 'VEH_NO', 'PER_NO']`
* **Logic:** This inner join creates the foundational row. It ensures that every non-motorist demographic profile is securely locked to their exact spatial positioning (e.g., Bike Lane, Crosswalk) at the time of the crash.

**2. The Crash Environment (Left Join)**
* **Tables:** `[Victim Base]` + `accident.csv`
* **Keys:** `['STATE', 'STATENAME', 'ST_CASE']`
* **Logic:** Appends the overarching spatial and temporal context of the crash (Lighting Conditions, Rural/Urban Classification, Latitude/Longitude) to the victim's row.

**3. Multi-Condition Weather (Left Join with Aggregation)**
* **Tables:** `[Victim Base]` + `weather.csv`
* **Keys:** `['STATE', 'STATENAME', 'ST_CASE']`
* **Logic:** Because a single crash can have multiple weather conditions (e.g., Rain *and* Fog), the pipeline first groups the 1-to-many `weather.csv` table. It collapses multiple conditions into a single pipe-separated string (`Rain | Fog`) per `ST_CASE` before executing the left join.

**4. The Infrastructure & Striking Vehicle (Left Join)**
* **Tables:** `[Victim Base]` + `vehicle.csv`
* **Keys:** Left `['ST_CASE', 'STR_VEH']` → Right `['ST_CASE', 'VEH_NO']`
* **Logic:** This is the critical infrastructure join. A pedestrian's native `VEH_NO` is 0. To find the infrastructure parameters (Speed Limit, Traffic Controls) relevant to the crash, the pipeline maps the pedestrian's `STR_VEH` (Striking Vehicle Number) to the `vehicle.csv`'s `VEH_NO`. This securely retrieves the infrastructure variables governing the exact vehicle that struck the pedestrian.
