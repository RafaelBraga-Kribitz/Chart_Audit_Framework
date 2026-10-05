---
id: dash.finance.profitability
type: dashboard
status: specification
function: Finance
area: Profitability
audience_roles: [Executive, Data analytics]
---

# Finance / Profitability

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

- `kpi.finance.gross-profit-margin` Gross profit margin (kpi). Communication `bullet-graph`. Analysis `histogram`.
- `kpi.finance.ltv-to-cac-ratio` LTV to CAC ratio (kpi). Communication `bullet-graph`. Analysis `histogram`.
- `kpi.finance.monthly-recurring-profit` Monthly recurring profit (kpi). Communication `line-chart`. Analysis `bar-chart`.
- `kpi.finance.net-profit` Net profit (kpi). Communication `line-chart`. Analysis `bar-chart`.
- `kpi.finance.net-revenue-minus-cac` Net revenue minus CAC (kpi). Communication `line-chart`. Analysis `bar-chart`.
- `kpi.finance.profit-margin` Profit margin (kpi). Communication `bullet-graph`. Analysis `histogram`.
- `kpi.finance.revenue-per-employee` Revenue per employee (kpi). Communication `line-chart`. Analysis `bar-chart`.
