## Overview
This repository contains the data engineering pipeline and final analytical datasets for analyzing pedestrian and cyclist fatalities in Oregon over a 10-year period. 

Aligning with Vision Zero and the Safe System Approach, this project strips away subjective behavioral factors (e.g., "distraction" or "darting into traffic") to focus exclusively on the built environment and physical infrastructure where fatal incidents occur. Furthermore, it incorporates a spatial equity analysis, mapping crash sites to U.S. Census Bureau tracts to identify demographic and socioeconomic disparities in fatal crash exposure.


## Methodology
The pipeline extracts, coalesces, and enriches data using two distinct engineering approaches for its primary sources:
1. **National Highway Traffic Safety Administration (NHTSA):** Local extraction and merging of raw Fatality Analysis Reporting System (FARS) CSVs.
    - FARS Analytical User’s Manual: https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/813794 
2. **U.S. Census Bureau API:** Programmatic querying of the American Community Survey (ACS) 5-Year Estimates, directly integrating demographic data without relying on static dataset downloads. 
    - ACS Census API: https://www.census.gov/data/developers/data-sets/acs-5year.2022.html#list-tab-1806015614


## Reproducibility

To reproduce the data engineering pipeline from scratch, follow these exact steps. **Note:** The raw national files contain millions of rows and are git-ignored to prevent repository bloat.

### Step 1: Secure the Raw FARS Data
1. Ensure the directory `data/raw/` exists in your local repository.
2. Download the raw national CSV zip folders for 2015-2024 from the NHTSA FARS FTP data portal.
    - Raw Data Download Source: https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/FARS/
3. Extract these folders directly into `data/raw/`. 
   *(Expected structure: `data/raw/FARS2015NationalCSV/`, `data/raw/FARS2016NationalCSV/`, etc.)*

### Step 2: Run initial.py script
Run the local python script initial.py. This extracts the Oregon-specific records, strips formatting anomalies, and performs the relational merges between the victim, the striking vehicle, and the crash environment.

This will create `data/processed/FARSinfrastructure.csv`

### Step 3: Run enrich.py script
1. Ensure active census key is present on *line 9: CENSUS_API_KEY = "YOUR_API_KEY_HERE"*, if not replace  with active API key.
2. Run the local python script enrich.py.

This will create `data/processed/FARSmaster.csv`

## Dataset registry

### Dataset 1: FARS Infrastructure 

- **Source:** National Highway Traffic Safety Administration (NHTSA) FARS FTP.
- **License:** Public Domain (U.S. Government Open Data).
- **Date pulled:** 2026-06-22
- **Approximate size:** 1,049 rows, 30 columns, ~250 KB
- **Owner on this project:** Simon Thompson
- **Where it lives in this repo:** `data/processed/FARSinfrastructure.csv`
- **Ethics / consent notes:** Publicly available fatal crash data. Anonymized by NHTSA; contains no Personally Identifiable Information (PII) or Protected Health Information (PHI). Victim identification relies strictly on randomized `ST_CASE` and `PER_NO` indexing.
- **How to fetch (for a teammate cloning fresh):** 1. Download the raw national CSV zip folders for 2015-2024 from the NHTSA FARS data portal into `data/raw/`. 2. Run `python initial.py` to extract and merge the matrix.

### Dataset 2: Spatial Equity Master

- **Source:** U.S. Census Bureau American Community Survey (ACS) 5-Year Estimates (2022) via API, intersected with NHTSA FARS infrastructure data.
- **License:** Public Domain (U.S. Government Open Data).
- **Date pulled:** 2026-06-24
- **Approximate size:** 1,049 rows, 38 columns, ~350 KB
- **Owner on this project:** Simon Thompson
- **Where it lives in this repo:** `data/processed/FARSmaster.csv`
- **Ethics / consent notes:** Combines anonymized crash locations with aggregated, public-domain demographic data. The pipeline actively handles and blanks out Census privacy suppression codes (e.g., `-666666666`) to respect household anonymity in low-population tracts.
- **How to fetch (for a teammate cloning fresh):** 1. Ensure `FARSinfrastructure.csv` has been generated. 2. Insert a valid U.S. Census API key into line 9 of `enrich.py`. 3. Run `python enrich.py`.

## Data Architecture & Relational Merges

The raw FARS database is highly relational. A single fatal incident requires data to be stitched together from multiple independent tables. To flatten this into the analytical `FARSMaster.csv` matrix, the Python pipeline executes a precise sequence of SQL-style joins, followed by a spatial point-in-polygon mapping.

### Primary and Foreign Keys
NHTSA and the U.S. Census Bureau use hierarchical indexing systems to link records:
* `ST_CASE`: The unique identifier for the crash event itself.
* `VEH_NO`: The identifier for a specific vehicle within that crash.
* `PER_NO`: The identifier for a specific person within that vehicle (or a specific non-motorist).
* `GEOID`: The 11-digit U.S. Census Tract identifier appended to a crash via spatial mapping.

### The Merge Sequence
The pipeline builds the dataset horizontally, starting with the individual victim and appending environmental, infrastructural, and socioeconomic context outwards:

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

**5. Spatial Integration (Point-in-Polygon Join)**
* **Inputs:** `[Infrastructure Matrix]` + `Oregon Census Tract Shapefiles (TIGER/Line)`
* **Keys:** Coordinate Geometry (`LATITUDE`, `LONGITUD`) → Spatial Polygon
* **Logic:** Converts the FARS WGS84 GPS coordinates into spatial points and overlays them onto NAD83 Census Tract polygons. This appends the standard 11-digit `GEOID` to every fatal crash, serving as the bridge between physical crash sites and neighborhood demographics.

**6. Demographic & Equity Enrichment (Inner Join)**
* **Tables:** `[Spatially Mapped Crash Base]` + `U.S. Census ACS 5-Year Estimates`
* **Keys:** `['GEOID']`
* **Logic:** Pings the U.S. Census API to retrieve tract-level socioeconomic and vulnerability data (Median Income, Race/Ethnicity, Transit Dependency) for every unique `GEOID`. This final merge connects the physical crash environment to systemic equity metrics, resolving the final `FARSMaster.csv` dataset.
