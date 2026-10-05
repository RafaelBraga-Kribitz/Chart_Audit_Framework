---
id: dash.online-presence.conversion
type: dashboard
status: specification
function: Online Presence
area: Conversion
audience_roles: [Marketing lead, Marketing analytics]
---

# Online Presence / Conversion

A specification, not a claim that a live dashboard exists.

## Questions

- Are the conversion measures on the right side of their targets or inside their corridors?
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

- `kpi.online-presence.ecommerce-conversion-rate` Ecommerce conversion rate (kpi). Communication `bullet-graph`. Analysis `histogram`.
- `kpi.online-presence.landing-page-conversion-rate` Landing page conversion rate (kpi). Communication `bullet-graph`. Analysis `histogram`.
- `kpi.online-presence.pages-meeting-speed-budget` Pages meeting speed budget (kpi). Communication `line-chart`. Analysis `bar-chart`.
