---
id: dash.finance.profitability
type: dashboard
status: placeholder
category: Finance
subcategory: Profitability
context: organizational
audiences: [Executive, Data Analytics]
---

# Finance / Profitability

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Profitability on the right side of their targets?
- Which input moved, and is that a signal or a tail?

## Audiences and surfaces

- Communication (executive, client, HR business partner): dashboard or report. Use each KPI's communication chart.
- Analysis (data scientist, researcher, R&D, marketing analytics, development): notebook or pandas/matplotlib plot. Use each KPI's analysis chart. Do not paste that figure onto the executive page unchanged.

## Zones (communication)

| Zone | What goes here |
|---|---|
| Score | Big number or bullet versus target for the OMTM of this subcategory |
| Trend | Line of that KPI |
| Breakdown | Sorted bar of the entities |
| Variance | Waterfall or diverging bar versus plan |
| Detail | Data table of the rows a person can act on |

## KPIs

- `kpi.finance.revenue-per-employee` Revenue per employee. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.finance.net-revenue-minus-cac` Net revenue minus CAC. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.finance.ltv-to-cac-ratio` LTV to CAC ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.finance.net-profit` Net profit. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.finance.monthly-recurring-profit` Monthly recurring profit. Communication `line-chart`. Analysis `bar-chart`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).
