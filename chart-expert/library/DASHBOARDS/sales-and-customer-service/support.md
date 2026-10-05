---
id: dash.sales-and-customer-service.support
type: dashboard
status: specification
function: Sales and Customer Service
area: Support
audience_roles: [Executive, Data analytics]
---

# Sales and Customer Service / Support

A specification, not a claim that a live dashboard exists.

## Questions

- Are the support measures on the right side of their targets or inside their corridors?
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

- `kpi.sales-and-customer-service.first-response-time` First response time (kpi). Communication `line-chart`. Analysis `histogram`.
- `kpi.sales-and-customer-service.resolution-time` Resolution time (kpi). Communication `line-chart`. Analysis `histogram`.
- `kpi.sales-and-customer-service.tickets-resolved-within-24-hours` Tickets resolved within 24 hours (kpi). Communication `bullet-graph`. Analysis `histogram`.
