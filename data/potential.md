# Oregon Active Transportation Fatality Infrastructure & Equity Analysis (2015–2024)

## Overview
This repository contains the data engineering pipeline and final analytical datasets for analyzing pedestrian and cyclist fatalities in Oregon over a 10-year period. 

Aligning with Vision Zero and the Safe System Approach, this project strips away subjective behavioral factors (e.g., "distraction" or "darting into traffic") to focus exclusively on the built environment and physical infrastructure where fatal incidents occur. Furthermore, it incorporates a spatial equity analysis, mapping crash sites to U.S. Census Bureau tracts to identify demographic and socioeconomic disparities in fatal crash exposure.

The resulting master datasets are optimized for exploratory data analysis (EDA) and machine learning applications.

## Methodology
The pipeline extracts, coalesces, and enriches data using two primary sources:
1. **National Highway Traffic Safety Administration (NHTSA):** Fatality Analysis Reporting System (FARS).
2. **U.S. Census Bureau:** American Community Survey (ACS) 5-Year Estimates.

**Data Engineering Highlights:**
* **Standardization:** Resolves structural database changes implemented by NHTSA in 2020, bridging legacy formats with modern 1-to-many tables.
* **Spatial Integration:** Executes a Point-in-Polygon spatial join (WGS84 to NAD83 projection alignment) to map exact crash coordinates to Oregon's 2020 Census Tracts.
* **Equity Lenses:** Calculates precise exposure risk metrics (e.g., Zero-Vehicle Households, Transit Commuting dependency) while securely handling Census Bureau data suppression flags.

---

## ⚙️ Reproducibility: How to Run the Pipeline

To reproduce the data engineering pipeline from scratch, follow these exact steps. **Note:** The raw national files contain millions of rows and are git-ignored to prevent repository bloat.

### Step 1: Secure the Raw FARS Data
1. Ensure the directory `data/raw/` exists in your local repository.
2. Download the raw national CSV zip folders for 2015-2024 from the NHTSA FARS FTP data portal.
3. Extract these folders directly into `data/raw/`. 
   *(Expected structure: `data/raw/FARS2015NationalCSV/`, `data/raw/FARS2016NationalCSV/`, etc.)*

### Step 2: Build the Infrastructure Matrix
Run the local engineering script. This extracts the Oregon-specific records, strips formatting anomalies (e.g., invisible BOM characters), and performs the relational merges between the victim, the striking vehicle, and the crash environment.
```bash
python initial.py