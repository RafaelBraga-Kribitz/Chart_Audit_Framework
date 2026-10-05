---
id: dash.human-resources.hiring
type: dashboard
status: specification
function: Human Resources
area: Hiring
audience_roles: [HR business partner, Data analytics]
---

# Human Resources / Hiring

A specification, not a claim that a live dashboard exists.

## Questions

- Are the hiring measures on the right side of their targets or inside their corridors?
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

- `kpi.human-resources.account-executives-hired` Account executives hired (kpi). Communication `line-chart`. Analysis `bar-chart`.
- `kpi.human-resources.interview-to-offer-ratio` Interview to offer ratio (kpi). Communication `bullet-graph`. Analysis `histogram`.
- `kpi.human-resources.sales-development-hires` Sales development hires (kpi). Communication `line-chart`. Analysis `bar-chart`.
- `kpi.human-resources.sdrs-trained` SDRs trained (kpi). Communication `line-chart`. Analysis `bar-chart`.
