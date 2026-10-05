---
id: dash.finance.cash-management
type: dashboard
status: specification
function: Finance
area: Cash Management
audience_roles: [Executive, Data analytics]
---

# Finance / Cash Management

A specification, not a claim that a live dashboard exists.

## Questions

- Are the cash management measures on the right side of their targets or inside their corridors?
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

- `kpi.finance.accounts-receivable-aging` Accounts receivable aging (kri). Communication `stacked-bar-chart`. Analysis `histogram`.
- `kpi.finance.days-sales-outstanding` Days sales outstanding (kpi). Communication `line-chart`. Analysis `histogram`.
- `kpi.finance.operating-cash-flow` Operating cash flow (kpi). Communication `line-chart`. Analysis `bar-chart`.
