---
id: dash.management.discovery
type: dashboard
status: specification
function: Management
area: Discovery
audience_roles: [Executive, Researcher]
---

# Management / Discovery

A specification, not a claim that a live dashboard exists.

## Questions

- Are the discovery measures on the right side of their targets or inside their corridors?
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

- `kpi.management.usability-score` Usability score (kpi). Communication `bullet-graph`. Analysis `bar-chart`.
