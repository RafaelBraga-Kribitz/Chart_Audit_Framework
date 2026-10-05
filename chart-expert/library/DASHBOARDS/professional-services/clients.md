---
id: dash.professional-services.clients
type: dashboard
status: specification
function: Professional Services
area: Clients
audience_roles: [Executive, Client, Data analytics]
---

# Professional Services / Clients

A specification, not a claim that a live dashboard exists.

## Questions

- Are the clients measures on the right side of their targets or inside their corridors?
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

- `kpi.professional-services.client-breakeven` Client breakeven (kpi). Communication `line-chart`. Analysis `histogram`.
- `kpi.professional-services.client-roi` Client ROI (kpi). Communication `bullet-graph`. Analysis `histogram`.
