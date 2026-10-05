---
id: dash.sales-and-customer-service.customers
type: dashboard
status: specification
function: Sales and Customer Service
area: Customers
audience_roles: [Executive, Data analytics]
---

# Sales and Customer Service / Customers

A specification, not a claim that a live dashboard exists.

## Questions

- Are the customers measures on the right side of their targets or inside their corridors?
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

- `kpi.sales-and-customer-service.accounts-with-health-score` Accounts with health score (kpi). Communication `bullet-graph`. Analysis `histogram`.
- `kpi.sales-and-customer-service.at-risk-accounts-contacted` At risk accounts contacted (kpi). Communication `bullet-graph`. Analysis `histogram`.
- `kpi.sales-and-customer-service.customer-interviews` Customer interviews (kpi). Communication `line-chart`. Analysis `bar-chart`.
- `kpi.sales-and-customer-service.customer-satisfaction-score` Customer satisfaction score (kpi). Communication `bullet-graph`. Analysis `histogram`.
- `kpi.sales-and-customer-service.net-promoter-score` Net promoter score (kpi). Communication `big-number`. Analysis `diverging-stacked-bar`.
- `kpi.sales-and-customer-service.weekly-active-users` Weekly active users (kpi). Communication `bullet-graph`. Analysis `histogram`.
