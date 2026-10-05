# Sales and Customer Service / Revenue

Context: organizational. Group: functional. KPIs: 1.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Revenue

- id: `kpi.sales-and-customer-service.revenue`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.revenue`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Revenue recognized in the period on the stated basis. Placed under Sales and Customer Service / Revenue.

Questions: Is Revenue on the desired side of its target for this period?

Inputs:

- `metric.recognized-revenue` (recognized revenue)

Placements:

- organizational / functional / Sales and Customer Service / Revenue (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.
