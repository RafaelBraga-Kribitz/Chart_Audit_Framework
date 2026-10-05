---
id: dash.sales-and-customer-service.expansion
type: dashboard
status: specification
function: Sales and Customer Service
area: Expansion
audience_roles: [Executive, Data analytics]
---

# Sales and Customer Service / Expansion

A specification, not a claim that a live dashboard exists.

## Questions

- Are the expansion measures on the right side of their targets or inside their corridors?
- Which input moved, and is that a signal or a tail?

## Zones (communication)

| Zone | What goes here |
|---|---|
| Score | `big-number` or `bullet-graph` against target for the lead KPI |
| Trend | `line-chart` of that KPI |
| Breakdown | Sorted `bar-chart` of the entities |
| Variance | `waterfall-chart` or `diverging-bar` against plan |
| Detail | `data-table` of the rows a person can act on |

## KPIs

- `kpi.sales-and-customer-service.expansion-revenue` Expansion revenue (kpi). Communication `line-chart`. Analysis `bar-chart`.
- `kpi.sales-and-customer-service.upsell-rate` Upsell rate (kpi). Communication `bullet-graph`. Analysis `histogram`.
