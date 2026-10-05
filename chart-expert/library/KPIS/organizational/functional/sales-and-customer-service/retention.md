# Sales and Customer Service / Retention

Context: organizational. Group: functional. KPIs: 1.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Customer retention

- id: `kpi.sales-and-customer-service.customer-retention`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.retention`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Share of starting customers still active at the end of the period. Placed under Sales and Customer Service / Retention.

Questions: Is Customer retention on the desired side of its target for this period?

Inputs:

- `metric.customers-retained` (customers retained)
- `metric.customers-at-the-start-of-the-period` (customers at the start of the period)

Placements:

- organizational / functional / Sales and Customer Service / Retention (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.
