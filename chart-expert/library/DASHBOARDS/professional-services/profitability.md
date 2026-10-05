---
id: dash.professional-services.profitability
type: dashboard
status: specification
function: Professional Services
area: Profitability
audience_roles: [Executive, Client, Data analytics]
---

# Professional Services / Profitability

A specification, not a claim that a live dashboard exists.

## Questions

- Are the profitability measures on the right side of their targets or inside their corridors?
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

- `kpi.professional-services.gross-profit-per-head` Gross profit per head (kpi). Communication `line-chart`. Analysis `bar-chart`.
- `kpi.professional-services.team-cost-to-gross-profit` Team cost to gross profit (kpi). Communication `bullet-graph`. Analysis `histogram`.
