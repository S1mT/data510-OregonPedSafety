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
