---
id: dash.sales-and-customer-service.retention
type: dashboard
status: specification
function: Sales and Customer Service
area: Retention
audience_roles: [Executive, Data analytics]
---

# Sales and Customer Service / Retention

A specification, not a claim that a live dashboard exists.

## Questions

- Are the retention measures on the right side of their targets or inside their corridors?
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

- `kpi.sales-and-customer-service.customer-churn-rate` Customer churn rate (kri). Communication `line-chart`. Analysis `survival-curve`.
- `kpi.sales-and-customer-service.customer-retention` Customer retention (kpi). Communication `bullet-graph`. Analysis `survival-curve`.
