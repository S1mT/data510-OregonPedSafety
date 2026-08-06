# Backlog: Oregon Pedestrian and Cyclist Safety

This file is the **human-readable mirror** of the [GitHub Projects (v2) Iterative Development board](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) for this repo. Every row here should also exist as a GitHub issue, be added to the board, tagged with a milestone label, and sized.

## Conventions

- Each item has: id, title, hypothesis or user story, **Create / Observe / Analyze** triple, milestone tag, size, and status.
- Items are ordered primarily by project sequence. Remaining open items should be prioritized on the GitHub Projects board.
- Milestone tags: `M1-proposal`, `M2-data-summary`, `M3-poster-draft`, `M4-writeup-draft`, `M5-final`, `infra`, `ethics`.
- Sizes: S, M, L, XL.
- Status values:
  - `Done` – Definition of Done has been met.
  - `Create` – The planned artifact is being produced.
  - `Observe` – Outputs are being inspected or validated.
  - `Analyze` – Results are being interpreted or documented.
  - `Backlog` – Ready or awaiting prioritization.
  - `Deferred` – Valid work intentionally postponed.
  - `Superseded` – Replaced by a more specific PBI.
  - `Discontinued` – Investigated but intentionally stopped after feasibility review.
- The board has five active workflow columns: `Backlog` → `Create` → `Observe` → `Analyze` → `Done`.
- `Superseded`, `Deferred`, and `Discontinued` are historical outcomes recorded in this file and may be represented through labels or closed issues on GitHub.
- WIP cap: `Create + Observe + Analyze` ≤ `owners + 1` at any time.
- Definition of Ready and Definition of Done live in [`CHARTER.md`](CHARTER.md).

## Change Log

### August 2026 backlog reconciliation

- Added explicit status fields while preserving all historical PBIs.
- Marked PBI-007 as superseded by the more specific implementation in PBI-012.
- Marked PBI-008 and PBI-015 as discontinued after determining that the fatality-only dataset does not support a sufficiently defensible supervised predictive target.
- Retained PBI-014 in the Analyze phase because significance testing was completed, but final test details and interpretation still need to be consolidated.
- Decomposed the original XL finalization item, PBI-018, into smaller M4 and M5 PBIs.
- Added PBIs for feedback integration, model-feasibility documentation, final figures, final write-up completion, and reproducibility validation.

## Items

### PBI-001

- **Title:** Acquire and Process Oregon FARS Data
- **Hypothesis:** The FARS database contains sufficient pedestrian and cyclist fatality records to support statewide crash-risk analysis.
- **Create:** Develop the extraction pipeline and isolate Oregon-specific records from the national FARS datasets.
- **Observe:** Verify yearly row counts, state filtering accuracy, and successful extraction of required tables.
- **Analyze:** Determine whether Oregon has sufficient crash volume and variable coverage for project feasibility.
- **Tag:** `M1-proposal`
- **Size:** M
- **Status:** Done
- **Outcome:** Oregon records from 2015–2024 were successfully extracted from the national FARS tables and used to construct the project datasets.
- **GitHub issue:** <link once filed>

### PBI-002

- **Title:** Define Research Questions and Stakeholder Scope
- **Hypothesis:** A clearly defined research question aligned with stakeholder needs will guide dataset selection and analysis priorities.
- **Create:** Draft project proposal and charter research questions.
- **Observe:** Collect peer stakeholder and instructor feedback.
- **Analyze:** Refine the scope from local crash analysis toward statewide Oregon fatality analysis.
- **Tag:** `M1-proposal`
- **Size:** S
- **Status:** Done
- **Outcome:** The project scope shifted from Salem-focused analysis to statewide Oregon analysis and was formalized in the approved proposal.
- **GitHub issue:** <link once filed>

### PBI-003

- **Title:** Build Analysis-Ready Master Dataset
- **Hypothesis:** Relational FARS tables can be merged into a single analytical dataset without losing critical information.
- **Create:** Develop the initial processing pipeline and construct `FARSinfrastructure.csv`.
- **Observe:** Validate joins, row counts, duplicate records, and variable availability.
- **Analyze:** Confirm the resulting dataset contains roadway, environmental, temporal, victim, and spatial variables needed for analysis.
- **Tag:** `M2-data-summary`
- **Size:** L
- **Status:** Done
- **Outcome:** A row-per-victim infrastructure dataset was created from the Accident, Person, PBType, Vehicle, and Weather tables.
- **GitHub issue:** ...

### PBI-004

- **Title:** Profile Dataset Quality
- **Hypothesis:** Data quality issues can be identified and documented before analysis begins.
- **Create:** Generate descriptive statistics and quality checks.
- **Observe:** Review duplicates, missingness, victim distributions, age distributions, and geographic coverage.
- **Analyze:** Document limitations and determine which variables require caution during analysis.
- **Tag:** `M2-data-summary`
- **Size:** M
- **Status:** Done
- **Outcome:** Dataset profiling documented zero duplicate rows, victim and geographic distributions, and substantial reporting gaps in variables including traffic controls and speed limits.
- **GitHub issue:** ...

### PBI-005

- **Title:** Produce Data Summary Deliverable
- **Hypothesis:** Comprehensive documentation will allow the dataset and pipeline to be understood and reproduced independently.
- **Create:** Write the M2 Data Summary and supporting data documentation.
- **Observe:** Verify inventory, schema, reproducibility instructions, ethics documentation, and freeze statement.
- **Analyze:** Confirm ingestion is complete and dataset scope is frozen.
- **Tag:** `M2-data-summary`
- **Size:** S
- **Status:** Done
- **Outcome:** The M2 Data Summary documented the two-stage pipeline, schema, quality findings, reproducibility workflow, ethics considerations, and final data freeze.
- **GitHub issue:** ...

### PBI-006

- **Title:** Generate Exploratory Visualizations
- **Hypothesis:** Visual exploration will reveal meaningful crash patterns and support communication of findings.
- **Create:** Build charts, maps, and summary figures.
- **Observe:** Examine temporal, geographic, roadway, infrastructure, and demographic patterns.
- **Analyze:** Identify the strongest and most defensible findings for the poster and write-up.
- **Tag:** `M3-poster-draft`
- **Size:** M
- **Status:** Done
- **Outcome:** Exploratory visualizations were produced and the most relevant figures were selected for the poster narrative.
- **GitHub issue:** ...

### PBI-007

- **Title:** Identify Crash Hotspots and Spatial Clusters
- **Hypothesis:** Fatal pedestrian and cyclist crashes are geographically concentrated in identifiable areas.
- **Create:** Produce hotspot maps and spatial analyses.
- **Observe:** Measure clustering and corridor-level patterns.
- **Analyze:** Determine whether specific locations show elevated fatal-crash concentration.
- **Tag:** `M3-poster-draft`
- **Size:** L
- **Status:** Superseded
- **Change note:** This broad planning item was replaced by the more specific implementation described in PBI-012.
- **GitHub issue:** ...

### PBI-008

- **Title:** Develop Predictive Modeling Workflow
- **Hypothesis:** Environmental, roadway, and demographic variables can explain meaningful variation in fatal crash characteristics.
- **Create:** Investigate potential statistical and machine-learning outcomes and preprocessing requirements.
- **Observe:** Evaluate whether the available dataset contains a defensible target, comparison group, and sufficient class variation.
- **Analyze:** Determine whether predictive modeling would answer the research question more meaningfully than descriptive, spatial, and inferential analysis.
- **Tag:** `M3-poster-draft`
- **Size:** L
- **Status:** Discontinued
- **Outcome:** The team determined that a general fatal-crash prediction model was not defensible because the dataset contains only fatal cases and lacks an appropriate non-fatal or non-crash comparison group. Spatial, descriptive, infrastructure, and statistical analyses were prioritized instead.
- **GitHub issue:** ...

### PBI-009

- **Title:** Enrich Crash Records with Census Tract Demographics
- **Hypothesis:** Adding tract-level socioeconomic and commuting characteristics will support a more meaningful transportation-equity analysis.
- **Create:** Develop `enrich.py` to spatially join crash coordinates to Oregon census tracts and merge ACS 5-year estimates into `FARSmaster.csv`.
- **Observe:** Verify coordinate filtering, tract assignment, GEOID joins, demographic coverage, and final row and column counts.
- **Analyze:** Confirm that income, race/ethnicity, and transit/walking commute variables are sufficiently complete for descriptive and statistical analysis.
- **Tag:** `M2-data-summary`
- **Size:** L
- **Status:** Done
- **Outcome:** The infrastructure dataset was spatially joined to Census tracts and enriched with ACS income, population, race/ethnicity, and commuting measures.
- **GitHub issue:** ...

### PBI-010

- **Title:** Establish the M3 Analysis and Communication Plan
- **Hypothesis:** Mapping each research question to specific spatial, statistical, and communication outputs will keep the poster and write-up coherent.
- **Create:** Define the M3 workflow for EDA, density mapping, hotspot analysis, geographic comparisons, hypothesis testing, predictive-model feasibility, and equity analysis.
- **Observe:** Compare the proposed analyses against the M3 poster rubric and available variables in `FARSmaster.csv`.
- **Analyze:** Prioritize analyses that directly support the research questions and defer or discontinue methods that cannot be justified by the data.
- **Tag:** `M3-poster-draft`
- **Size:** S
- **Status:** Done
- **Outcome:** The M3 plan was refined around spatial clustering, infrastructure profiling, descriptive comparisons, and statistical testing.
- **GitHub issue:** ...

### PBI-011

- **Title:** Draft the Capstone Write-Up Structure and Methods
- **Hypothesis:** Drafting the full narrative before final results are available will make it easier to transfer concise content into the poster.
- **Create:** Populate `writeup.qmd` with the introduction, data, engineering, planned methods, ethics, limitations, and reproducibility sections while preserving existing project metadata and research questions.
- **Observe:** Check the draft against the M3 poster and M4 write-up requirements and identify explicit placeholders for results and figures.
- **Analyze:** Determine which portions can be reused directly in the poster and which require further evidence before finalization.
- **Tag:** `M4-writeup-draft`
- **Size:** M
- **Status:** Done
- **Outcome:** The write-up structure and major narrative sections were drafted and subsequently used to develop and revise poster content.
- **GitHub issue:** ...

### PBI-012

- **Title:** Produce Statewide Crash Density and Hotspot Maps
- **Hypothesis:** Fatal pedestrian and cyclist crashes form visible statewide concentrations and meaningful local spatial clusters.
- **Create:** Generate density visualizations and conduct spatial clustering on valid crash coordinates.
- **Observe:** Compare cluster membership, noise points, geographic concentration, and sensitivity to methodological choices.
- **Analyze:** Identify defensible hotspot areas or corridors and document that clusters represent fatal-crash concentration rather than exposure-adjusted risk.
- **Tag:** `M3-poster-draft`
- **Size:** L
- **Status:** Done
- **Outcome:** The spatial hotspot implementation replaced the broader PBI-007 and produced the clustering results and visual material used in the project narrative.
- **GitHub issue:** ...

### PBI-013

- **Title:** Compare Fatal Crashes Across Oregon Geographies
- **Hypothesis:** Fatal pedestrian and cyclist crashes are unevenly distributed across counties, cities, and urban/rural settings.
- **Create:** Produce geographic summaries using available county, city, regional, or urban/rural classifications.
- **Observe:** Rank geographic areas by crash and victim counts and inspect whether results are driven by population concentration or a small number of events.
- **Analyze:** Select the most interpretable geographic comparison and explain the limitations of raw-count comparisons.
- **Tag:** `M3-poster-draft`
- **Size:** M
- **Status:** Analyze
- **Current note:** Geographic patterns have been examined, but the final comparison and wording should be reconciled with the poster and write-up before this PBI is closed.
- **GitHub issue:** ...

### PBI-014

- **Title:** Test Associations Between Crash Characteristics
- **Hypothesis:** Selected roadway, environmental, temporal, and demographic variables are statistically associated with meaningful crash-group differences.
- **Create:** Define appropriate categorical group comparisons and conduct significance tests with relevant assumption checks and effect-size measures where available.
- **Observe:** Review test statistics, p-values, expected cell counts, effect sizes, and multiple-comparison concerns.
- **Analyze:** Retain only substantively meaningful findings and avoid interpreting statistical association as evidence of causation.
- **Tag:** `M3-poster-draft`
- **Size:** M
- **Status:** Analyze
- **Current note:** Significance tests have been completed. The exact variables, statistical results, and final interpretations are being consolidated into the shared project artifacts.
- **GitHub issue:** ...

### PBI-015

- **Title:** Rank Crash Factors with an Interpretable Machine-Learning Model
- **Hypothesis:** A Random Forest model can rank roadway, environmental, temporal, and demographic variables associated with a clearly defined crash outcome.
- **Create:** Investigate potential targets, baselines, validation strategies, and preprocessing requirements.
- **Observe:** Assess whether a meaningful target and comparison framework exist in the fatality-only data.
- **Analyze:** Decide whether model performance and feature importance would provide a valid answer to the research question.
- **Tag:** `M3-poster-draft`
- **Size:** L
- **Status:** Discontinued
- **Outcome:** No sufficiently defensible prediction target was identified. A model distinguishing fatal crashes from non-fatal crashes or non-crash locations would require data not present in the frozen project scope.
- **GitHub issue:** ...

### PBI-016

- **Title:** Evaluate Transportation Equity Patterns
- **Hypothesis:** Fatal crash concentrations differ across census tracts with different income, demographic, and transit/walking commute characteristics.
- **Create:** Summarize crash records across tract-level socioeconomic groups and apply an appropriate statistical comparison framework.
- **Observe:** Examine patterns by income, race/ethnicity, and transit/walking commute measures while checking sparsity, collinearity, and tract-level aggregation limits.
- **Analyze:** Determine whether the evidence supports an equity-related finding and clearly state the absence of pedestrian, cyclist, vehicle, and roadway exposure measures.
- **Tag:** `M4-writeup-draft`
- **Size:** L
- **Status:** Analyze
- **Current note:** Demographic and socioeconomic variables have been incorporated into the analysis. Final statistical details and equity interpretations must be reconciled with the significance-testing results before closure.
- **GitHub issue:** ...

### PBI-017

- **Title:** Assemble the M3 Poster Rough Draft
- **Hypothesis:** A complete conference-style draft with honest preliminary findings will enable useful peer critique before final analysis is complete.
- **Create:** Build the poster with labeled sections for the question, stakeholders, data pipeline, ethics, methods, preliminary results, limitations, conclusions, reproducibility, and references.
- **Observe:** Check readability, figure captions, claim-evidence alignment, repository links, and rubric coverage.
- **Analyze:** Record peer and instructor feedback and convert required revisions into M4 and M5 backlog items.
- **Tag:** `M3-poster-draft`
- **Size:** L
- **Status:** Done
- **Outcome:** The M3 poster rough draft was assembled and submitted. Its content and layout have since undergone additional revision.
- **GitHub issue:** ...

### PBI-018

- **Title:** Finalize Results, Recommendations, and Reproducibility
- **Hypothesis:** Integrating spatial, statistical, machine-learning, and equity findings will support a defensible final report and actionable transportation-safety recommendations.
- **Create:** Finalize figures, tables, model documentation, recommendations, references, and reproducibility instructions for the write-up and poster.
- **Observe:** Verify that every claim is traceable to an analysis artifact and that all final deliverables render successfully from the repository.
- **Analyze:** Reconcile conflicting findings, state limitations, and produce two or three recommendations supported by the available evidence.
- **Tag:** `M5-final`
- **Size:** XL
- **Status:** Superseded
- **Change note:** This item was too broad to manage as one PBI and was decomposed into smaller tasks. Poster work is complete; the remaining scope is limited to the final write-up, predictive-model feasibility documentation, and final reproducibility checks.
- **GitHub issue:** ...

### PBI-019

- **Title:** Incorporate Poster and Write-Up Feedback
- **Hypothesis:** Systematically resolving peer and instructor feedback will improve the accuracy, clarity, and coherence of the final deliverables.
- **Create:** Consolidate feedback from the poster draft, studio reviews, and write-up review into a revision log.
- **Observe:** Classify each item as adopted, deferred, declined, or already resolved.
- **Analyze:** Update the poster and write-up and document the reasoning behind major scope or interpretation decisions.
- **Tag:** `M4-writeup-draft`
- **Size:** M
- **Status:** Done
- **Outcome:** Poster-related feedback was incorporated before the final poster was submitted for printing. Remaining revisions now apply only to the final write-up.
- **GitHub issue:** ...

### PBI-020

- **Title:** Document Predictive-Model Feasibility Decision
- **Hypothesis:** Explicitly documenting why predictive modeling was not used will demonstrate that the decision was methodologically grounded rather than an incomplete project task.
- **Create:** Write a concise feasibility assessment describing the candidate outcomes considered, available data structure, missing comparison data, and alternative methods selected.
- **Observe:** Verify that the reasoning aligns with the frozen dataset, research questions, poster claims, and course expectations.
- **Analyze:** Explain why spatial, descriptive, and inferential methods provide a more defensible answer within the current project scope.
- **Tag:** `M4-writeup-draft`
- **Size:** S
- **Status:** Backlog
- **GitHub issue:** ...

### PBI-021

- **Title:** Finalize Poster Figures and Captions
- **Hypothesis:** Print-ready figures with precise captions and legible labels will make the final poster easier to interpret and defend.
- **Create:** Regenerate selected maps, charts, and statistical summaries at final resolution and dimensions.
- **Observe:** Check axes, legends, sample sizes, geographic labels, captions, and consistency with the underlying analysis.
- **Analyze:** Remove redundant figures and ensure each retained visualization supports a specific claim or research question.
- **Tag:** `M5-final`
- **Size:** M
- **Status:** Done
- **Outcome:** Final poster figures, captions, and layout were completed, and the poster was submitted for printing.
- **GitHub issue:** ...

### PBI-022

- **Title:** Complete the Final Capstone Write-Up
- **Hypothesis:** Expanding the rough draft with final results, interpretation, and evidence will produce a coherent and defensible final report.
- **Create:** Complete the Results, Discussion, Limitations, Future Work, Conclusion, Recommendations, and References sections.
- **Observe:** Check alignment among the research questions, methods, figures, statistical results, and conclusions.
- **Analyze:** Reconcile spatial, infrastructure, demographic, and statistical findings and clearly distinguish supported conclusions from speculation.
- **Tag:** `M5-final`
- **Size:** L
- **Status:** Create
- **Current note:** This is the primary remaining project task.
- **GitHub issue:** ...
