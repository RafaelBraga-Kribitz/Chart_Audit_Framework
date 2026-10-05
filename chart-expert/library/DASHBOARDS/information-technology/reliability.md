---
id: dash.information-technology.reliability
type: dashboard
status: specification
function: Information Technology
area: Reliability
audience_roles: [Development, Data analytics]
---

# Information Technology / Reliability

A specification, not a claim that a live dashboard exists.

## Questions

- Are the reliability measures on the right side of their targets or inside their corridors?
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

- `kpi.information-technology.restore-tests-passed` Restore tests passed (kpi). Communication `line-chart`. Analysis `bar-chart`.
- `kpi.information-technology.unplanned-downtime` Unplanned downtime (kri). Communication `run-chart`. Analysis `histogram`.
