# Human Resources / Hiring

Context: organizational. Group: functional. KPIs: 4.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Account executives hired

- id: `kpi.human-resources.account-executives-hired`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.hiring`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Account executives who started in the period. Placed under Human Resources / Hiring.

Questions: Is Account executives hired on the desired side of its target for this period?

Inputs:

- `metric.account-executives-who-started` (account executives who started)

Placements:

- organizational / functional / Human Resources / Hiring (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Sales development hires

- id: `kpi.human-resources.sales-development-hires`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.hiring`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Sales development hires who started. Placed under Human Resources / Hiring.

Questions: Is Sales development hires on the desired side of its target for this period?

Inputs:

- `metric.sales-development-representatives-who-started` (sales development representatives who started)

Placements:

- organizational / functional / Human Resources / Hiring (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Interview to offer ratio

- id: `kpi.human-resources.interview-to-offer-ratio`
- kind: kpi
- unit: number
- direction: corridor
- timing: leading
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.hiring`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Interviews divided by offers. A corridor: too low and too high both mean the process is off. Placed under Human Resources / Hiring.

Questions: Is Interview to offer ratio on the desired side of its target for this period?

Inputs:

- `metric.interviews` (interviews)
- `metric.offers` (offers)

Placements:

- organizational / functional / Human Resources / Hiring (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### SDRs trained

- id: `kpi.human-resources.sdrs-trained`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.hiring`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

SDRs who finished the named training. Placed under Human Resources / Hiring.

Questions: Is SDRs trained on the desired side of its target for this period?

Inputs:

- `metric.sales-development-representatives-who-finished-training` (sales development representatives who finished training)

Placements:

- organizational / functional / Human Resources / Hiring (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.
