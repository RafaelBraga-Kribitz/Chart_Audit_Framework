---
id: dash.human-resources.engagement
type: dashboard
status: specification
function: Human Resources
area: Engagement
audience_roles: [HR business partner, Data analytics]
---

# Human Resources / Engagement

A specification, not a claim that a live dashboard exists.

## Questions

- Are the engagement measures on the right side of their targets or inside their corridors?
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

- `kpi.human-resources.employee-pulse-score` Employee pulse score (kpi). Communication `bullet-graph`. Analysis `bar-chart`.
- `kpi.human-resources.town-hall-held` Town hall held (kpi). Communication `line-chart`. Analysis `bar-chart`.
