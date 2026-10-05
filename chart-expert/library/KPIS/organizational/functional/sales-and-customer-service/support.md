# Sales and Customer Service / Support

Context: organizational. Group: functional. KPIs: 2.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### First response time

- id: `kpi.sales-and-customer-service.first-response-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.support`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Elapsed time from ticket open to first response. State the percentile, not only the mean. Placed under Sales and Customer Service / Support.

Questions: Is First response time on the desired side of its target for this period?

Inputs:

- `metric.elapsed-time-to-first-response` (elapsed time to first response)

Placements:

- organizational / functional / Sales and Customer Service / Support (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Resolution time

- id: `kpi.sales-and-customer-service.resolution-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.support`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Elapsed time from open to resolution. Placed under Sales and Customer Service / Support.

Questions: Is Resolution time on the desired side of its target for this period?

Inputs:

- `metric.elapsed-time-to-resolution` (elapsed time to resolution)

Placements:

- organizational / functional / Sales and Customer Service / Support (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.
