# Sales and Customer Service / Expansion

Context: organizational. Group: functional. KPIs: 2.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Upsell rate

- id: `kpi.sales-and-customer-service.upsell-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.expansion`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Share of customers who expanded. Placed under Sales and Customer Service / Expansion.

Questions: Is Upsell rate on the desired side of its target for this period?

Inputs:

- `metric.customers-who-bought-more` (customers who bought more)
- `metric.customers-eligible` (customers eligible)

Placements:

- organizational / functional / Sales and Customer Service / Expansion (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Expansion revenue

- id: `kpi.sales-and-customer-service.expansion-revenue`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.expansion`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Revenue from existing customers buying more. Placed under Sales and Customer Service / Expansion.

Questions: Is Expansion revenue on the desired side of its target for this period?

Inputs:

- `metric.revenue-from-upsell-and-cross-sell` (revenue from upsell and cross-sell)

Placements:

- organizational / functional / Sales and Customer Service / Expansion (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.
