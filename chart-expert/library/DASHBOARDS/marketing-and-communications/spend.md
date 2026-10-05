---
id: dash.marketing-and-communications.spend
type: dashboard
status: specification
function: Marketing and Communications
area: Spend
audience_roles: [Marketing lead, Marketing analytics]
---

# Marketing and Communications / Spend

A specification, not a claim that a live dashboard exists.

## Questions

- Are the spend measures on the right side of their targets or inside their corridors?
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

- `kpi.marketing-and-communications.marketing-spend-to-gross-profit` Marketing spend to gross profit (kpi). Communication `bullet-graph`. Analysis `histogram`.
