---
id: dash.sales-and-customer-service.pipeline
type: dashboard
status: specification
function: Sales and Customer Service
area: Pipeline
audience_roles: [Executive, Data analytics]
---

# Sales and Customer Service / Pipeline

A specification, not a claim that a live dashboard exists.

## Questions

- Are the pipeline measures on the right side of their targets or inside their corridors?
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

- `kpi.sales-and-customer-service.average-deal-size` Average deal size (kpi). Communication `line-chart`. Analysis `bar-chart`.
- `kpi.sales-and-customer-service.closed-won-rate` Closed won rate (kpi). Communication `bullet-graph`. Analysis `histogram`.
- `kpi.sales-and-customer-service.coaching-sessions` Coaching sessions (kpi). Communication `line-chart`. Analysis `bar-chart`.
- `kpi.sales-and-customer-service.new-accounts` New accounts (kpi). Communication `line-chart`. Analysis `bar-chart`.
- `kpi.sales-and-customer-service.pipeline-coverage` Pipeline coverage (kpi). Communication `bullet-graph`. Analysis `histogram`.
- `kpi.sales-and-customer-service.pipeline-created` Pipeline created (kpi). Communication `line-chart`. Analysis `bar-chart`.
- `kpi.sales-and-customer-service.product-demos` Product demos (kpi). Communication `line-chart`. Analysis `bar-chart`.
- `kpi.sales-and-customer-service.sales-qualified-leads` Sales qualified leads (kpi). Communication `line-chart`. Analysis `bar-chart`.
