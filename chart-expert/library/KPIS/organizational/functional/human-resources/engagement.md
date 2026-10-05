# Human Resources / Engagement

Context: organizational. Group: functional. KPIs: 2.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Employee pulse score

- id: `kpi.human-resources.employee-pulse-score`
- kind: kpi
- unit: number
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: survey
- dashboard: `dash.human-resources.engagement`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Mean response on the stated pulse scale. Placed under Human Resources / Engagement.

Questions: Is Employee pulse score on the desired side of its target for this period?

Inputs:

- `metric.mean-pulse-response` (mean pulse response)

Placements:

- organizational / functional / Human Resources / Engagement (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Town hall held

- id: `kpi.human-resources.town-hall-held`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.engagement`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Count of town halls held. A task count; the outcome is the pulse or retention that follows. Placed under Human Resources / Engagement.

Questions: Is Town hall held on the desired side of its target for this period?

Inputs:

- `metric.town-halls-held` (town halls held)

Placements:

- organizational / functional / Human Resources / Engagement (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.
