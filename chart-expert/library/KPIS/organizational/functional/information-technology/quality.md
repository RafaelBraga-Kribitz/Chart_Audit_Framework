# Information Technology / Quality

Context: organizational. Group: functional. KPIs: 2.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Critical defects

- id: `kpi.information-technology.critical-defects`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.quality`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Critical defects found after the release, on the stated severity rule. Placed under Information Technology / Quality.

Questions: Is Critical defects on the desired side of its target for this period?

Inputs:

- `metric.critical-defects-found-after-release` (critical defects found after release)

Placements:

- organizational / functional / Information Technology / Quality (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Regressions

- id: `kpi.information-technology.regressions`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.quality`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Behaviors that worked before the release and failed after it. Placed under Information Technology / Quality.

Questions: Is Regressions on the desired side of its target for this period?

Inputs:

- `metric.regressions-found-after-release` (regressions found after release)

Placements:

- organizational / functional / Information Technology / Quality (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.
