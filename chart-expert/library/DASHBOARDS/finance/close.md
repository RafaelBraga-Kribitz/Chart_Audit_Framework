---
id: dash.finance.close
type: dashboard
status: specification
function: Finance
area: Close
audience_roles: [Executive, Data analytics]
---

# Finance / Close

A specification, not a claim that a live dashboard exists.

## Questions

- Are the close measures on the right side of their targets or inside their corridors?
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

- `kpi.finance.days-to-close` Days to close (kpi). Communication `line-chart`. Analysis `histogram`.
