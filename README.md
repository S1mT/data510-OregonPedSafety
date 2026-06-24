# Fatal Pedestrian and Cyclist Crash Risk Factors in Oregon (2015-2024)

A data science project using NHTSA FARS data to identify environmental, roadway, and demographic factors associated with fatal pedestrian and cyclist crashes across Oregon.

## Quick reference

| Field | Value |
|-------|-------|
| Owner team | Simon Thompson, Rohan Srinivasa Babu |
| Owner Product Lead | Simon Thompson |
| Peer Stakeholder POs | Amaya Supancich-McCord, Aiyana Brown, Seira Ramchandani |
| Studio Session | 2 |
| GitHub repo | https://github.com/S1mT/data510-SalemPedSafety |
| GitHub Projects board | https://github.com/S1mT/data510-SalemPedSafety/projects?query=is%3Aopen |
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

- `data/README.md`
- `data/processed/OregonFARSMaster.csv`

The project uses Oregon-specific records extracted from the National Highway Traffic Safety Administration (NHTSA) Fatality Analysis Reporting System (FARS) for years 2015–2024.

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

**Iteration ending:** <date>
**Milestone tag in focus:** `M3-poster-draft`

**Completed PBIs**
- ...

**Stakeholder response log**
- ...

**Plan for next iteration**
- ...

**Risks and impediments**
- ...

## Week 9

**Iteration ending:** <date>
**Milestone tag in focus:** `M3-poster-draft`

**Completed PBIs**
- ...

**Stakeholder response log**
- ...

**Plan for next iteration**
- ...

**Risks and impediments**
- ...

## Week 10 -- Poster rough-draft milestone (M3)

**Iteration ending:** <date>
**Milestone tag in focus:** `M3-poster-draft`

**Completed PBIs**
- ...

**Stakeholder response log**
- ...

**Plan for next iteration**
- ...

**Risks and impediments**
- ...

**Retrospective (milestone boundary)**
- What worked: ...
- What did not: ...
- One change for next iteration: ...

## Week 11

**Iteration ending:** <date>
**Milestone tag in focus:** `M4-writeup-draft`

**Completed PBIs**
- ...

**Stakeholder response log**
- ...

**Plan for next iteration**
- ...

**Risks and impediments**
- ...

## Week 12 -- Write-up rough-draft milestone (M4)

**Iteration ending:** <date>
**Milestone tag in focus:** `M4-writeup-draft`

**Completed PBIs**
- ...

**Stakeholder response log**
- ...

**Plan for next iteration**
- ...

**Risks and impediments**
- ...

**Retrospective (milestone boundary)**
- What worked: ...
- What did not: ...
- One change for next iteration: ...

## Week 13

**Iteration ending:** <date>
**Milestone tag in focus:** `M5-final`

**Completed PBIs**
- ...

**Stakeholder response log**
- ...

**Plan for next iteration**
- ...

**Risks and impediments**
- ...

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
