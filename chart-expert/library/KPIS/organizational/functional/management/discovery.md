# Management / Discovery

Context: organizational. Group: functional. KPIs: 1.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Usability score

- id: `kpi.management.usability-score`
- kind: kpi
- unit: number
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: survey
- dashboard: `dash.management.discovery`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Mean score on the stated usability scale for the prototype or release. Placed under Management / Discovery.

Questions: Is Usability score on the desired side of its target for this period?

Inputs:

- `metric.mean-usability-score` (mean usability score)

Placements:

- organizational / functional / Management / Discovery (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.
