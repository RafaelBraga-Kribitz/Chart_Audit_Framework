---
id: dash.marketing-and-communications.acquisition
type: dashboard
status: specification
function: Marketing and Communications
area: Acquisition
audience_roles: [Marketing lead, Marketing analytics]
---

# Marketing and Communications / Acquisition

A specification, not a claim that a live dashboard exists.

## Questions

- Are the acquisition measures on the right side of their targets or inside their corridors?
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

- `kpi.marketing-and-communications.click-through-rate` Click through rate (kpi). Communication `bullet-graph`. Analysis `histogram`.
- `kpi.marketing-and-communications.cost-per-lead` Cost per lead (kpi). Communication `line-chart`. Analysis `bar-chart`.
- `kpi.marketing-and-communications.customer-acquisition-cost` Customer acquisition cost (kpi). Communication `line-chart`. Analysis `bar-chart`.
- `kpi.marketing-and-communications.marketing-qualified-leads` Marketing qualified leads (kpi). Communication `line-chart`. Analysis `bar-chart`.
- `kpi.marketing-and-communications.wins-by-lead-source` Wins by lead source (kpi). Communication `horizontal-bar-chart`. Analysis `bar-chart`.
