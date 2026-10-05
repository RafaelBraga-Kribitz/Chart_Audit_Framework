---
id: dash.portfolio-and-project-management.delivery
type: dashboard
status: specification
function: Portfolio and Project Management
area: Delivery
audience_roles: [Executive, Client, Data analytics]
---

# Portfolio and Project Management / Delivery

A specification, not a claim that a live dashboard exists.

## Questions

- Are the delivery measures on the right side of their targets or inside their corridors?
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

- `kpi.portfolio-and-project-management.billed-versus-expected` Billed versus expected (kpi). Communication `bullet-graph`. Analysis `scatter-plot`.
- `kpi.portfolio-and-project-management.estimated-versus-actual-project-cost` Estimated versus actual project cost (kpi). Communication `bullet-graph`. Analysis `scatter-plot`.
- `kpi.portfolio-and-project-management.estimated-versus-actual-project-time` Estimated versus actual project time (kpi). Communication `bullet-graph`. Analysis `scatter-plot`.
- `kpi.portfolio-and-project-management.lead-time-per-project` Lead time per project (kpi). Communication `line-chart`. Analysis `histogram`.
- `kpi.portfolio-and-project-management.project-contribution-margin` Project contribution margin (kpi). Communication `bullet-graph`. Analysis `waterfall-chart`.
