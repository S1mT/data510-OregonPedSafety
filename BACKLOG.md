# Backlog: Oregon Pedestrian and Cyclist Safety

This file is the **human-readable mirror** of the [GitHub Projects (v2) Iterative Development board](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) for this repo. Every row here is also a GitHub issue, added to the board, tagged with a milestone label, and sized.

## Conventions

- Each item has: id, title, hypothesis or user story, **Create / Observe / Analyze** triple, milestone tag, size.
- Items are ordered top to bottom by **priority**.
- Milestone tags: `M1-proposal`, `M2-data-summary`, `M3-poster-draft`, `M4-writeup-draft`, `M5-final`, `infra`, `ethics`.
- Sizes: S, M, L, XL.
- The board has five columns: `Backlog` → `Create` → `Observe` → `Analyze` → `Done`. Each column is the *phase of work happening on a single PBI right now*, not a work type. See the [Iterative Development board explainer](https://courses.lpcordova.phd/data510/project-framework/#github-projects-board-per-project-iterative-development-board) for what each column means and when to advance a card.
- WIP cap: `Create + Observe + Analyze` ≤ `owners + 1` at any time.
- Definition of Ready and Definition of Done live in [`CHARTER.md`](CHARTER.md).

## Items

### PBI-001

- **Title:** Acquire and Process Oregon FARS Data
- **Hypothesis:** The FARS database contains sufficient pedestrian and cyclist fatality records to support statewide crash-risk analysis.
- **Create:** Develop `clean.py` and extract Oregon-specific records from the national FARS datasets.
- **Observe:** Verify yearly row counts, state filtering accuracy, and successful extraction of required tables.
- **Analyze:** Determine whether Oregon has sufficient crash volume and variable coverage for project feasibility.
- **Tag:** `M1-proposal`
- **Size:** M
- **GitHub issue:** <link once filed>

### PBI-002

- **Title:** Define Research Questions and Stakeholder Scope
- **Hypothesis:** A clearly defined research question aligned with stakeholder needs will guide dataset selection and analysis priorities.
- **Create:** Draft project proposal and charter research questions.
- **Observe:** Collect peer stakeholder and instructor feedback.
- **Analyze:** Refine the scope from local crash analysis toward statewide Oregon fatality analysis.
- **Tag:** `M1-proposal`
- **Size:** S
- **GitHub issue:** <link once filed>

### PBI-003

- **Title:** Build Analysis-Ready Master Dataset
- **Hypothesis:** Relational FARS tables can be merged into a single analytical dataset without losing critical information.
- **Create:** Develop `MasterFull.py` and construct `OregonFARSMaster.csv`.
- **Observe:** Validate joins, row counts, and variable availability.
- **Analyze:** Confirm the resulting dataset contains roadway, environmental, demographic, and spatial variables needed for modeling.
- **Tag:** `M2-data-summary`
- **Size:** L
- **GitHub issue:** ...

### PBI-004

- **Title:** Profile Dataset Quality
- **Hypothesis:** Data quality issues can be identified and documented before modeling begins.
- **Create:** Generate descriptive statistics and quality checks.
- **Observe:** Review duplicates, missingness, victim distributions, age distributions, and geographic coverage.
- **Analyze:** Document limitations and determine which variables require caution during modeling.
- **Tag:** `M2-data-summary`
- **Size:** M
- **GitHub issue:** ...

### PBI-005

- **Title:** Produce Data Summary Deliverable
- **Hypothesis:** Comprehensive documentation will allow reproduction of the dataset independently.
- **Create:** Write M2 Data Summary and data documentation.
- **Observe:** Verify inventory, schema, reproducibility instructions, and ethics documentation.
- **Analyze:** Confirm ingestion is complete and dataset scope is frozen.
- **Tag:** `M2-data-summary`
- **Size:** S
- **GitHub issue:** ...

### PBI-006

- **Title:** Generate Exploratory Visualizations
- **Hypothesis:** Visual exploration will reveal meaningful crash patterns and support communication of findings.
- **Create:** Build charts, maps, and summary figures.
- **Observe:** Examine temporal, geographic, and demographic patterns.
- **Analyze:** Identify candidate findings for the poster and writeup.
- **Tag:** `M3-poster-draft`
- **Size:** M
- **GitHub issue:** ...

### PBI-007

- **Title:** Identify Crash Hotspots and Spatial Clusters
- **Hypothesis:** Fatal pedestrian and cyclist crashes are geographically concentrated in identifiable areas.
- **Create:** Produce hotspot maps and spatial analyses.
- **Observe:** Measure clustering and corridor-level patterns.
- **Analyze:** Determine whether specific locations show elevated crash risk.
- **Tag:** `M3-poster-draft`
- **Size:** L
- **GitHub issue:** ...

### PBI-008

- **Title:** Develop Predictive Modeling Workflow
- **Hypothesis:** Environmental, roadway, and demographic variables can explain meaningful variation in fatal crash characteristics.
- **Create:** Build statistical and machine-learning models.
- **Observe:** Evaluate model performance and feature importance.
- **Analyze:** Identify the factors most strongly associated with fatal crashes.
- **Tag:** `M3-poster-draft`
- **Size:** L
- **GitHub issue:** ...

### PBI-009

- **Title:** Enrich Crash Records with Census Tract Demographics
- **Hypothesis:** Adding tract-level socioeconomic and commuting characteristics will support a more meaningful transportation-equity analysis.
- **Create:** Develop `enrich.py` to spatially join crash coordinates to Oregon census tracts and merge ACS 5-year estimates into `FARSmaster.csv`.
- **Observe:** Verify coordinate filtering, tract assignment, GEOID joins, demographic coverage, and final row/column counts.
- **Analyze:** Confirm that income, race/ethnicity, and transit/walking commute variables are sufficiently complete for descriptive and statistical analysis.
- **Tag:** `M2-data-summary`
- **Size:** L
- **GitHub issue:** ...

### PBI-010

- **Title:** Establish the M3 Analysis and Communication Plan
- **Hypothesis:** Mapping each research question to specific spatial, statistical, and machine-learning outputs will keep the poster and write-up coherent.
- **Create:** Define the M3 workflow for EDA, density mapping, hotspot analysis, geographic comparisons, hypothesis testing, predictive modeling, and equity analysis.
- **Observe:** Compare the proposed analyses against the M3 poster rubric and available variables in `FARSmaster.csv`.
- **Analyze:** Prioritize analyses that directly support the research questions and defer methods that cannot be justified by the data.
- **Tag:** `M3-poster-draft`
- **Size:** S
- **GitHub issue:** ...

### PBI-011

- **Title:** Draft the Capstone Write-Up Structure and Methods
- **Hypothesis:** Drafting the full narrative before final results are available will make it easier to transfer concise content into the poster.
- **Create:** Populate `writeup.qmd` with the introduction, data, engineering, planned methods, ethics, limitations, and reproducibility sections while preserving existing project metadata and research questions.
- **Observe:** Check the draft against the M3 poster and M4 write-up requirements and identify explicit placeholders for results and figures.
- **Analyze:** Determine which portions can be reused directly in the poster and which require further evidence before finalization.
- **Tag:** `M4-writeup-draft`
- **Size:** M
- **GitHub issue:** ...

### PBI-012

- **Title:** Produce Statewide Crash Density and Hotspot Maps
- **Hypothesis:** Fatal pedestrian and cyclist crashes form visible statewide concentrations and statistically meaningful local clusters.
- **Create:** Generate a KDE or hexbin density map and run DBSCAN or HDBSCAN on valid crash coordinates.
- **Observe:** Compare cluster counts, noise points, geographic concentration, and sensitivity to clustering parameters.
- **Analyze:** Identify defensible hotspot areas or corridors and document that clusters reflect fatal-crash concentration rather than exposure-adjusted risk.
- **Tag:** `M3-poster-draft`
- **Size:** L
- **GitHub issue:** ...

### PBI-013

- **Title:** Compare Fatal Crashes Across Oregon Geographies
- **Hypothesis:** Fatal pedestrian and cyclist crashes are unevenly distributed across counties, cities, and urban/rural settings.
- **Create:** Produce county, city, and urban/rural summaries with normalized comparisons where suitable denominators are available.
- **Observe:** Rank geographic areas by crash and victim counts and inspect whether results are driven by population concentration or a small number of events.
- **Analyze:** Select the most interpretable geographic comparison for the poster and explain the limitations of raw-count comparisons.
- **Tag:** `M3-poster-draft`
- **Size:** M
- **GitHub issue:** ...

### PBI-014

- **Title:** Test Associations Between Crash Characteristics
- **Hypothesis:** Selected roadway, environmental, temporal, and demographic variables are statistically associated with meaningful crash-group differences.
- **Create:** Define appropriate categorical outcomes or group comparisons and run chi-square tests with effect-size measures and assumption checks.
- **Observe:** Review expected cell counts, p-values, effect sizes, and multiple-comparison concerns.
- **Analyze:** Retain only tests that are substantively meaningful and avoid treating statistical association as causation.
- **Tag:** `M3-poster-draft`
- **Size:** M
- **GitHub issue:** ...

### PBI-015

- **Title:** Rank Crash Factors with an Interpretable Machine-Learning Model
- **Hypothesis:** A Random Forest model can rank roadway, environmental, temporal, and demographic variables associated with a clearly defined crash outcome.
- **Create:** Build a preprocessing and Random Forest workflow with a documented target, baseline, train/test or cross-validation strategy, and class-imbalance handling if needed.
- **Observe:** Evaluate predictive performance, permutation or model-based feature importance, and stability across validation folds.
- **Analyze:** Report the strongest predictors cautiously, distinguish prediction from causation, and compare findings with descriptive and statistical results.
- **Tag:** `M3-poster-draft`
- **Size:** L
- **GitHub issue:** ...

### PBI-016

- **Title:** Evaluate Transportation Equity Patterns
- **Hypothesis:** Fatal crash concentrations differ across census tracts with different income, demographic, and transit/walking commute characteristics.
- **Create:** Summarize crash records across tract-level socioeconomic groups and fit an appropriate statistical model or comparison framework.
- **Observe:** Examine concentration patterns by income and demographic measures while checking sparsity, collinearity, and tract-level aggregation limits.
- **Analyze:** Determine whether the evidence supports an equity-related finding and clearly state the absence of pedestrian, cyclist, and vehicle exposure measures.
- **Tag:** `M4-writeup-draft`
- **Size:** L
- **GitHub issue:** ...

### PBI-017

- **Title:** Assemble the M3 Poster Rough Draft
- **Hypothesis:** A complete conference-style draft with honest preliminary findings will enable useful peer critique before final analysis is complete.
- **Create:** Build the poster with labeled sections for the question, stakeholders, data pipeline, ethics, methods, preliminary results, limitations, conclusions, reproducibility, and references.
- **Observe:** Check readability, figure captions, claim-evidence alignment, repository links, and rubric coverage.
- **Analyze:** Record peer and instructor feedback and convert required revisions into M4 and M5 backlog items.
- **Tag:** `M3-poster-draft`
- **Size:** L
- **GitHub issue:** ...

### PBI-018

- **Title:** Finalize Results, Recommendations, and Reproducibility
- **Hypothesis:** Integrating spatial, statistical, machine-learning, and equity findings will support a defensible final report and actionable transportation-safety recommendations.
- **Create:** Finalize figures, tables, model documentation, recommendations, references, and reproducibility instructions for the write-up and poster.
- **Observe:** Verify that every claim is traceable to an analysis artifact and that all final deliverables render successfully from the repository.
- **Analyze:** Reconcile conflicting findings, state limitations, and produce two or three recommendations supported by the available evidence.
- **Tag:** `M5-final`
- **Size:** XL
- **GitHub issue:** ...
