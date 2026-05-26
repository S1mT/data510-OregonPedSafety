# Studio Charter: <project name>

> Filled in live during the **Studio Charter** session in week 3. Every section below is committed in the same commit at the end of that class block. See [Studio Charter (single-session inception)](https://courses.lpcordova.phd/data510/project-framework/charter-inception.html) for the script and time-boxes.

**Owner team:** Simon Thompson & Rohan Srinivasa Babu
**Owner Product Lead:** Simon Thompson
**Peer Stakeholder POs:** Amaya Supancich-McCord, Aiyana Brown, Seira Ramchandani
**Instructor / Sponsor:** Lucas Cordova (`LucasCordova` on GitHub)
**GitHub repo:** <link to this repo>
**GitHub Projects board:** <link>
**Discord category:** `#<project>-*`
**Studio Session:** 2
**Studio formed:** 5/25/26

## Vision

Salem becomes a city where planners and engineers can pinpoint the roads and intersections that put pedestrians at greatest risk — and direct safety investments there before the next crash, not after.

## Mission

The team will build a spatial risk model of pedestrian incidents in the Salem area using ODOT crash records and public infrastructure data and identify the factors most associated with high-severity outcomes.

## Context

- **Users / affected parties:**
  Pedestrians – most exposed to severe crashes and least buffered by car infrastructure
  Oregon DOT's Transportation Safety Division – funds and publishes the crash data; may act on statewide pattern findings
  Salem city planners / council – primary users of risk-area findings; can act on infrastructure recommendations

- **Data sources (proposed):** ODOT, City of Salem, Salem Keizer Area Transportation Study (SKATS)

- **Constraints:**
  Compute: Standard laptop-tier compute; dataset size (county-level crash records) is well within local capacity
  Access: All proposed sources are public or publicly requestable; no data-sharing agreement required
  Skills: Team has prior traffic accident project experience; pedestrian/cyclist-specific modeling and spatial analysis (GeoPandas, QGIS) may require some ramp-up

- **Ethics risks:** Underreporting bias: Police-reported crash data systematically undercounts minor pedestrian and cyclist incidents, skewing models toward severe events; findings must be explicitly scoped to reported crashes and not generalized as total risk
Fairness / deployment risk: A hotspot model that under-represents low-income or minority corridors (due to underreporting or lower baseline traffic counts) could inadvertently direct resources away from the most vulnerable communities

## Success criteria by milestone

- **M1, proposal (W4):** <measurable criterion>
- **M2, data summary (W7):** <measurable criterion>
- **M3, poster rough draft (W10):** <measurable criterion>
- **M4, write-up rough draft (W12):** <measurable criterion>
- **M5, final write-up and poster (W14):** <measurable criterion>

## Working agreements (internal to owner team)

- **Sync rhythm:** <e.g., one async standup per weekday in `#<project>-standup`>
- **Code review:** <who reviews what, by when>
- **Decision rule:** <how the team decides when it disagrees>

## Working agreements (triad with peer POs)

- **Studio Brief due:** By 5 pm the day before class (Sunday), committed to `studio/briefs/W<NN>-<peer>.md` and linked in `#<project>-studio` on Google Chat. If the owner team needs the peer POs to read or review something specific *before* the Studio Session (a data preview, model results, a draft figure), file the Brief earlier so the peer POs actually have time to do that homework. Otherwise the default is "before the Studio Session starts."
- **Studio Critique due:** By 11:59pm the following Wednesday if the peer PO needs extra time to draft a thoughtful write-up.
- **Priority conflict resolution:** owner team integrates briefs in good faith; the instructor arbitrates (as Process Expert) if peer POs and owner team disagree.

## Response SLAs (Service Level Agreements)

A **Service Level Agreement** is a written promise the triad makes about *how fast* each side responds when a specific signal arrives. Every row must have an answer before this Charter is committed. See [Response SLAs](https://courses.lpcordova.phd/data510/project-framework/charter-inception.html#response-slas-service-level-agreements) for the full definition.

| When this signal arrives... | Who responds | By when |
|-----------------------------|--------------|---------|
| Peer PO files a **Studio Brief** (commits to `studio/briefs/...`, links in `#<project>-studio`) | Owner team | <e.g., acknowledge in `#<project>-studio` within 24 hours, with a first-pass adopt / defer / decline call for each item> |
| Peer PO files a **Studio Critique** | Owner team | <e.g., respond in `#<project>-studio` within 24 hours and capture follow-up items into the backlog> |
| Owner team posts an **Iteration Review** in `README.md` | Both peer POs | <e.g., read before filing the next Brief and Critique> |
| Owner team flags a **blocker** in `#<project>-blockers` | Instructor, plus any tagged peer PO | <e.g., responds by the next Studio Session at the latest; faster if online> |
| Anyone asks a clarifying question in `#<project>-general` | Whoever is tagged (default: owner team) | <e.g., reply within 48 hours, even if the reply is "we will look at this next iteration"> |

## Definition of Ready (PBI)

A PBI is ready to be pulled out of `Backlog` and moved into `Create` when it has:

- A one-sentence hypothesis or user story.
- A named **Create**, **Observe**, **Analyze** triple.
- A milestone tag (`M1-proposal`, `M2-data-summary`, `M3-poster-draft`, `M4-writeup-draft`, `M5-final`, `infra`, `ethics`).
- A T-shirt size estimate (S, M, L, XL).
- WIP slack on the board: `Create + Observe + Analyze` is below the team's WIP cap (owners + 1).

## Definition of Done (PBI)

A PBI is done, and may be moved from `Analyze` into `Done`, when:

- The Create artifact is in the repo or linked from the issue.
- The Observe results are recorded somewhere referenceable (notebook output, processed dataset, draft results section).
- The Analyze writeup names a next step (continue, pivot, kill, or decompose into new PBIs).
- A peer PO has either signed off in `#<project>-studio` or filed a Studio Critique covering it.
- The card is linked under *Completed PBIs* in the next Iteration Review in `README.md`.

## Context map

> Optional. Replace this block with a Mermaid `flowchart LR` showing how users, data, constraints, and ethics risks flow into the owner team and out to the capstone outcome. See the [`charter-inception.qmd` template](https://courses.lpcordova.phd/data510/project-framework/charter-inception.html) for a starting Mermaid diagram.

## Stakeholder alignment memo (one-page summary)

### Why we exist
<two sentences from Vision and Mission>

### What we will deliver to peer POs every week
- An Iteration Review in this `README.md` by <day / time>
- A summary of which Studio Brief items we adopted, deferred, or declined and why

### What we need from peer POs every week
- A Studio Brief by <day / time> next class (next iteration's requirements, questions, risks)
- A Studio Critique by <day / time> next class (assessment of last week's delivery)

### How to reach us
- Discord category: `#<project>-general` (day-to-day), `#<project>-studio` (Briefs and Critiques), `#<project>-blockers` (impediments)
- GitHub repo: <link>
- GitHub Projects board: <link>
