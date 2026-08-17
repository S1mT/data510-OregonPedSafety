# Fatal Pedestrian and Cyclist Crash Risk Factors in Oregon (2015-2024)

A data science project using NHTSA FARS data to identify environmental, roadway, and demographic factors associated with fatal pedestrian and cyclist crashes across Oregon.

## Quick reference

| Field | Value |
|-------|-------|
| Portfolio Site | https://s1mt.github.io/data510-OregonPedSafety/index.html |
| Owner team | Simon Thompson, Rohan Srinivasa Babu |
| Owner Product Lead | Simon Thompson |
| Peer Stakeholder POs | Amaya Supancich-McCord, Aiyana Brown, Seira Ramchandani |
| Studio Session | 2 |
| GitHub repo | https://github.com/S1mT/data510-OregonPedSafety |
| GitHub Projects board | https://github.com/S1mT/data510-OregonPedSafety/projects?query=is%3Aopen |
| Discord category | `#<project>-19` |
| Instructor / Sponsor | Lucas Cordova (`LucasCordova` on GitHub) |

## What this repo contains

| Path | Purpose |
|------|---------|
| [`CHARTER.md`](CHARTER.md) | Studio Charter: vision, mission, context, success criteria, working agreements, SLAs, DoR / DoD. Committed at the end of the week 3 Studio Charter session. |
| [`BACKLOG.md`](BACKLOG.md) | Human-readable mirror of the GitHub Projects board. |
| [`studio/briefs/`](studio/briefs/) | Weekly Studio Briefs from peer POs (`W<NN>-<peer>.md`). |
| [`studio/critiques/`](studio/critiques/) | Weekly Studio Critiques from peer POs (`W<NN>-<peer>.md`). |
| [`src/`](src/) | Working code (scripts, modules). |
| [`notebooks/`](notebooks/) | Exploratory and reporting notebooks. |
| [`data/`](data/) | Project data. Raw inputs are `.gitignored` by default; see `data/README.md`. |
| [`deliverables/`](deliverables/) | Milestone deliverables: proposal, data summary, poster, write-up. |

## Data Documentation

Project data documentation is available in:

- [`data/README.md`](data/README.md)
- `data/processed/FARSinfrastructure.csv`
- `data/processed/FARSmaster.csv`

The project uses Oregon-specific records extracted from the National Highway Traffic Safety Administration's Fatality Analysis Reporting System for 2015–2024.

The final analysis-ready dataset is produced through a two-stage pipeline:

1. `initial.py` extracts Oregon records from the annual national FARS tables and combines victim, crash, weather, roadway, traffic-control, and striking-vehicle information into `FARSinfrastructure.csv`.
2. `enrich.py` assigns crash coordinates to Oregon Census tracts and appends American Community Survey income, demographic, population, and transit/walking commute variables to produce `FARSmaster.csv`.

The data scope was frozen at the M2 milestone. No additional data ingestion is planned before final submission.

## How this project runs (DS3 in one paragraph)

This project is run as a **DS3 studio**: the owner team is paired with two or three **peer Stakeholder POs** drawn from adjacent capstone projects. Every week the peer POs file a **Studio Brief** for the next iteration and a **Studio Critique** of the last iteration. The owner team commits an **Iteration Review** here in `README.md` before each class. See the [Studio Session weekly ritual](https://courses.lpcordova.phd/data510/project-framework/weekly-ritual.html) for the cadence and [Studio Charter](https://courses.lpcordova.phd/data510/project-framework/charter-inception.html) for the inception session.

---

# Iteration Reviews

One subsection per class week. The owner team commits the new section **before each class** so peer POs can read it before filing the next Brief and Critique. Use the template at the bottom of this file for any extra weeks you add.

## Week 4 -- Proposal milestone (M1)

**Iteration ending:** June 2026  
**Milestone tag in focus:** `M1-proposal`

**Completed PBIs**
- PBI-001 Acquire and Process Oregon FARS Data (feasibility validation)

**In-flight (carrying across the boundary)**
- Finalize project proposal
- Evaluate project scope and stakeholder priorities

**Stakeholder response log**
- Feedback provided was to confirm dataset availability and acquisition plan, document data pipeline and preprocessing approach, and begin formal ethics and bias mitigation planning.

**Plan for next iteration**
- Complete proposal submission (`M1-proposal`)
- Confirm final data source selection (`M2-data-summary`)
- Begin ingestion planning (`M2-data-summary`)

**Risks and impediments**
- Dataset availability and quality had not yet been validated.
- Scope depended on identifying a sufficiently rich public dataset.

## Week 5

**Iteration ending:** June 2026  
**Milestone tag in focus:** `M1-proposal` / `M2-data-summary`

**Completed PBIs**
- PBI-002 Define Research Questions and Stakeholder Scope
- Submitted project proposal
- Confirmed FARS as primary data source
- Established statewide Oregon project scope

**In-flight (carrying across the boundary)**
- PBI-003 Build Analysis-Ready Master Dataset

**Stakeholder response log**
- n/a

**Plan for next iteration**
- Develop Oregon extraction workflow (`M2-data-summary`)
- Validate source tables and schema (`M2-data-summary`)
- Begin dataset integration pipeline (`M2-data-summary`)

**Risks and impediments**
- FARS data is highly relational and requires multiple table joins.
- Some desired variables may not be consistently available across years.

## Week 6

**Iteration ending:** June 2026  
**Milestone tag in focus:** `M2-data-summary`

**Completed PBIs**
- Developed Oregon extraction workflow (`clean.py`)
- Generated Oregon-specific source tables from national FARS files

**In-flight (carrying across the boundary)**
- PBI-003 Build Analysis-Ready Master Dataset
- PBI-004 Profile Dataset Quality

**Stakeholder response log**
- n/a

**Plan for next iteration**
- Complete dataset integration workflow (`M2-data-summary`)
- Conduct data profiling and validation (`M2-data-summary`)
- Finalize M2 deliverable (`M2-data-summary`)

**Risks and impediments**
- Several roadway variables contain substantial "Not Reported" values.
- Join validation was required before analysis could begin.

## Week 7 -- Data summary milestone (M2)

**Iteration ending:** June 2026  
**Milestone tag in focus:** `M2-data-summary`

**Completed PBIs**
- PBI-003 Build Analysis-Ready Master Dataset
- PBI-004 Profile Dataset Quality
- PBI-005 Produce Data Summary Deliverable

**Stakeholder response log**
- n/a

**Plan for next iteration**
- PBI-006 Generate exploratory visualizations (`M3-poster-draft`)
- PBI-007 Identify crash hotspots and spatial patterns (`M3-poster-draft`)
- PBI-008 Develop predictive modeling workflow (`M3-poster-draft`)

**Risks and impediments**
- FARS includes only fatal crashes and therefore cannot represent total pedestrian or cyclist risk.
- Traffic exposure measures are unavailable, limiting causal interpretation.
- Some roadway variables contain substantial "Not Reported" values.

**Retrospective (milestone boundary)**
- What worked: The ETL pipeline successfully produced a reproducible statewide dataset. Documentation and schema design improved project transparency.
- What did not: The original Salem-focused scope proved too restrictive. Several planned variables were unavailable or inconsistently reported.
- One change for next iteration: Begin visualization and modeling work earlier so more time is available for interpretation and communication of results.

## Week 8

**Iteration ending:** July 5, 2026  
**Milestone tag in focus:** `M3-poster-draft`

**Completed PBIs**
- PBI-009 Enrich Crash Records with Census Tract Demographics
- Completed the two-stage processing workflow using `initial.py` and `enrich.py`
- Produced the final `FARSmaster.csv` dataset with census tract, income, demographic, and transit/walking commute variables
- Confirmed the statewide analysis scope and finalized the M2 data freeze

**In-flight (carrying across the boundary)**
- PBI-006 Generate Exploratory Visualizations
- PBI-010 Establish the M3 Analysis and Communication Plan

**Stakeholder response log**
- No additional formal Studio Brief or Studio Critique feedback was recorded for this iteration.

**Plan for next iteration**
- Complete core exploratory summaries and visualizations (`M3-poster-draft`)
- Finalize the spatial, statistical, machine-learning, and equity analysis plan (`M3-poster-draft`)
- Begin drafting the full write-up structure so content can be condensed into the poster (`M4-writeup-draft`)

**Risks and impediments**
- The final dataset contains only fatal crashes, so analyses cannot estimate the probability that an arbitrary crash becomes fatal.
- Several roadway variables have substantial `Not Reported` values.
- Census attributes are measured at the tract level and should not be interpreted as individual victim characteristics.

## Week 9

**Iteration ending:** July 12, 2026  
**Milestone tag in focus:** `M3-poster-draft`

**Completed PBIs**
- PBI-010 Establish the M3 Analysis and Communication Plan
- PBI-011 Draft the Capstone Write-Up Structure and Methods
- Defined the planned analysis sequence: EDA, density mapping, DBSCAN/HDBSCAN hotspots, geographic comparisons, chi-square testing, Random Forest modeling, and transportation-equity analysis
- Drafted the non-results portions of `writeup.qmd`, including the data pipeline, planned methods, ethics, limitations, and reproducibility narrative

**In-flight (carrying across the boundary)**
- PBI-006 Generate Exploratory Visualizations
- PBI-007 Identify Crash Hotspots and Spatial Clusters
- PBI-008 Develop Predictive Modeling Workflow
- PBI-017 Assemble the M3 Poster Rough Draft

**Stakeholder response log**
- No additional formal Studio Brief or Studio Critique feedback was recorded for this iteration.

**Plan for next iteration**
- Complete and select at least three poster-ready figures (`M3-poster-draft`)
- Produce statewide density and hotspot maps (`M3-poster-draft`)
- Complete preliminary statistical and Random Forest results (`M3-poster-draft`)
- Assemble and submit the complete M3 poster rough draft (`M3-poster-draft`)

**Risks and impediments**
- A defensible predictive target must be defined because every observation in FARS is already part of a fatal crash.
- Cluster and geographic results may identify concentrations but cannot establish exposure-adjusted risk without pedestrian, cyclist, traffic, or population denominators.
- The poster deadline requires prioritizing a small number of well-supported findings over a large number of incomplete analyses.

## Week 10 -- Poster rough-draft milestone (M3)

**Iteration ending:** July 19, 2026  
**Milestone due:** July 12, 2026  
**Milestone tag in focus:** `M3-poster-draft` / `M4-writeup-draft`

**Completed PBIs**
- PBI-006 Generate Exploratory Visualizations
- PBI-012 Produce Statewide Crash Density and Hotspot Maps
- PBI-017 Assemble the M3 Poster Rough Draft
- Submitted the complete M3 poster rough draft by July 12, 2026
- Produced poster-ready spatial, infrastructure, temporal, and demographic visualizations
- Implemented the specific statewide clustering workflow described in PBI-012, superseding the broader PBI-007

**In-flight (carrying across the boundary)**
- PBI-013 Compare Fatal Crashes Across Oregon Geographies
- PBI-014 Test Associations Between Crash Characteristics
- PBI-016 Evaluate Transportation Equity Patterns
- Revisions to `writeup.qmd` based on completed analyses and poster development

**Scope decisions**
- PBI-008 and PBI-015 were discontinued after predictive-model feasibility review.
- The frozen dataset contains only fatal pedestrian and cyclist cases and does not include nonfatal crashes, non-crash locations, or another defensible comparison group.
- The team therefore prioritized spatial clustering, descriptive profiling, geographic comparisons, and inferential statistical testing rather than forcing a supervised predictive model that would not directly answer the research questions.

**Stakeholder response log**
- The poster rough draft was prepared for milestone-boundary critique.
- Feedback collection and formal revision decisions continued during Weeks 11 and 12.

**Plan for next iteration**
- Complete statistical significance testing and consolidate results (`M3-poster-draft` / `M4-writeup-draft`)
- Complete transportation-equity interpretation (`M4-writeup-draft`)
- Expand the write-up Results and Discussion sections (`M4-writeup-draft`)
- Revise the poster layout and narrative based on stakeholder feedback

**Risks and impediments**
- Spatial clusters represent concentrations of fatal crashes, not exposure-adjusted crash risk.
- The project lacks pedestrian counts, cyclist counts, vehicle-volume measures, and nonfatal crash records.
- Census tract characteristics describe areas surrounding crashes and cannot be attributed to individual victims.
- Traffic-control and speed-limit fields contain substantial reporting gaps.

**Retrospective (milestone boundary)**
- What worked: The team produced a complete poster narrative with real analysis progress, several developed visualizations, and a reproducible data pipeline. Beginning the longer write-up before finalizing the poster made it easier to condense the project into a visual format.
- What did not: The original machine-learning plan did not fit the structure of a fatality-only dataset. The poster also contained too much supporting text relative to the space given to figures and key findings.
- One change for next iteration: Center the remaining work on the strongest spatial, infrastructure, demographic, and statistical findings rather than attempting to include every originally proposed method.

## Week 11

**Iteration ending:** July 26, 2026  
**Milestone tag in focus:** `M4-writeup-draft`

**Completed PBIs**
- Advanced PBI-013 Compare Fatal Crashes Across Oregon Geographies
- Advanced PBI-014 Test Associations Between Crash Characteristics
- Advanced PBI-016 Evaluate Transportation Equity Patterns
- Completed the main spatial, infrastructure, demographic, and statistical analyses used in the poster and write-up
- Revised `writeup.qmd` to reflect the analyses that were actually completed
- Replaced the planned predictive-model narrative with a methodological explanation of why a supervised model was not appropriate for the frozen dataset
- Continued refining poster figures, captions, and narrative structure

**In-flight (carrying across the boundary)**
- Consolidation of exact significance-test results and interpretations
- Expansion of the write-up Results, Discussion, Limitations, and Conclusion sections
- Final poster layout revisions
- PBI-020 Document Predictive-Model Feasibility Decision

**Stakeholder response log**
- Informal poster review emphasized reducing text, increasing the prominence of visualizations, and making the relationship between each figure and the research questions more explicit.
- These recommendations were adopted in the next poster revision cycle.

**Plan for next iteration**
- Complete and submit the M4 write-up rough draft by August 2 (`M4-writeup-draft`)
- Integrate significance-test findings into the Results section
- Strengthen the connection between the research questions, visualizations, and discussion
- Convert the text-heavy data pipeline description into a compact visual diagram
- Prepare the final poster revision for printing

**Risks and impediments**
- Statistical outputs were divided across team members and still needed to be consolidated into one shared narrative.
- The write-up needed to distinguish clearly between statistical significance, practical importance, and causal interpretation.
- Poster space remained limited, requiring the team to prioritize only the most defensible findings.

## Week 12 -- Write-up rough-draft milestone (M4)

**Iteration ending:** August 2, 2026  
**Milestone tag in focus:** `M4-writeup-draft` / `M5-final`

**Completed PBIs**
- Submitted the M4 write-up rough draft on August 2, 2026
- Completed the major write-up sections, including the introduction, data and engineering, methods, results, ethics, discussion, limitations, conclusion, and reproducibility narrative
- Updated the write-up to reflect completed spatial clustering, infrastructure profiling, demographic analysis, geographic comparisons, and significance testing
- Documented the limitations of the fatality-only dataset and the methodological reasoning for not forcing a predictive model
- Revised the poster abstract, data pipeline, discussion, limitations and future work, and conclusion
- Consolidated spatial clustering and infrastructure profiling into a clearer analytical narrative
- Developed a compact vertical pipeline diagram suitable for the limited poster space

**In-flight (carrying across the boundary)**
- Final poster revisions and print preparation
- Final reconciliation of significance-test details provided by the team
- PBI-020 Document Predictive-Model Feasibility Decision
- PBI-022 Complete the Final Capstone Write-Up
- PBI-023 Validate Final Write-Up Reproducibility and Repository Hygiene

**Stakeholder response log**
- **Amaya:** Praised the clear narrative, developed analysis, visualizations, and helpful figure captions. Recommended giving visualizations and key findings more prominence, reducing supporting text, converting the pipeline into a diagram, and connecting each visualization group explicitly to a research question.
  - **Adopted:** Reduced text, increased emphasis on figures, created a pipeline diagram, strengthened figure-to-question connections, and sharpened the main takeaway.
- **Aiyana:** Identified the analysis as mostly complete and praised the project presentation. Recommended making more room for visualizations, adding short descriptive takeaways, condensing paragraphs, and briefly addressing all analytical methods considered.
  - **Adopted:** Condensed poster prose, added concise takeaway text, improved spacing, and included the rationale for methods used and omitted.
- **Seira:** Described the poster as one of the most complete drafts reviewed and praised its professional visualizations and detailed methods and validation section. Recommended using space more efficiently, converting the pipeline to a visual, grouping related figures, and stating a memorable result in the discussion.
  - **Adopted:** Reorganized related visualizations, revised the central layout, created a visual pipeline, and strengthened the discussion and conclusion around the poster's main takeaway.
- No critique recommendations were declined. Detailed statistical material that could not fit legibly on the poster was deferred to the final write-up.

**Plan for next iteration**
- Apply the stakeholder critiques to the final poster layout (`M5-final`)
- Finalize figures, captions, section balance, and the pipeline diagram
- Submit the poster for printing
- Continue expanding the M4 rough draft into the final written report
- Verify all statistical claims against the final shared outputs

**Risks and impediments**
- Final significance-test values and effect-size interpretations still needed to be reconciled with the shared analysis files.
- Reducing poster text created a risk of removing methodological context that should instead be retained in the final write-up.
- Findings remain observational and should not be presented as evidence that a particular roadway or demographic characteristic caused fatal crashes.

**Retrospective (milestone boundary)**
- What worked: Writing the detailed report before finalizing the poster made it easier to identify the strongest findings and create a coherent project narrative. The poster had a clear structure, professional visualizations, and substantial analysis progress by the M4 boundary.
- What did not: The first poster versions were too text-heavy, and the original modeling plan did not fully account for the lack of a comparison outcome in the fatality-only data.
- One change for next iteration: Treat the final write-up as the complete technical record and let the poster communicate only the most important methods, findings, limitations, and recommendations.

## Week 13

**Iteration ending:** August 9, 2026  
**Milestone tag in focus:** `M5-final`

**Completed PBIs**
- PBI-019 Incorporate Poster and Write-Up Feedback
- PBI-021 Finalize Poster Figures and Captions
- Completed the final poster layout and narrative revisions
- Increased the prominence of the results and visualizations
- Condensed supporting text throughout the poster
- Grouped visualizations according to the research questions and analytical themes
- Replaced the text-heavy pipeline section with a compact visual diagram
- Tightened the abstract, discussion, limitations and future work, and conclusion
- Submitted the final poster for printing on August 3, 2026

**In-flight (carrying across the boundary)**
- PBI-013 final geographic interpretation for the write-up
- PBI-014 consolidation of significance-test details
- PBI-016 final equity interpretation
- PBI-020 Document Predictive-Model Feasibility Decision
- PBI-022 Complete the Final Capstone Write-Up
- PBI-023 Validate Final Write-Up Reproducibility and Repository Hygiene

**Stakeholder response log**
- All three Week 12 critiques were reviewed and incorporated into the final poster.
- Adopted changes included increasing figure prominence, reducing text, creating a visual pipeline, grouping related findings, adding clearer takeaways, and aligning the discussion more explicitly with the research questions.
- Detailed statistical explanations and methodological context were intentionally moved to the final write-up rather than forced into the poster.

**Plan for next iteration**
- Complete the final report Results section using verified statistical outputs
- Finalize the Discussion, Limitations, Future Work, Conclusion, and Recommendations sections
- Include the predictive-model feasibility explanation
- Verify references, figure numbering, captions, repository paths, and reproducibility instructions
- Render and review the final write-up before submission

**Risks and impediments**
- The final report depends on receiving and verifying the exact significance-test outputs maintained by the other team member.
- Claims must remain consistent with the already printed poster while allowing the report to provide greater nuance.
- Reproducibility documentation must remove or secure any API credentials and clearly state required manual setup.

## Week 14 -- Final write-up and poster (M5)

**Iteration ending:** <date>
**Milestone tag in focus:** `M5-final`

**Completed PBIs**
- ...

**Stakeholder response log**
- ...

**Final retrospective**
- What worked: ...
- What did not: ...
- What we would change if we ran this project again: ...

---

## Iteration Review template (copy for any extra week)

```markdown
## Week <NN>

**Iteration ending:** <date>
**Milestone tag in focus:** <M1-proposal | M2-data-summary | M3-poster-draft | M4-writeup-draft | M5-final | infra | ethics>

**Completed PBIs**
- ...

**In-flight (carrying across the boundary)**
- ...

**Stakeholder response log**
- Studio Brief from <peer PO>: adopted = ..., deferred = ..., declined (with reason) = ...

**Plan for next iteration**
- Top PBIs (with milestone tags): ...

**Risks and impediments**
- ...
```
