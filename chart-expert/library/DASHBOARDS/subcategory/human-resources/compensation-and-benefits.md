---
id: dash.human-resources.compensation-and-benefits
type: dashboard
status: placeholder
category: Human Resources
subcategory: Compensation and Benefits
context: organizational
audiences: [Executive, Data Analytics, HR]
---

# Human Resources / Compensation and Benefits

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Compensation and Benefits on the right side of their targets?
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

- `kpi.human-resources.compensation-per-employee` Compensation per employee. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.compensation-revenue-rate` Compensation revenue rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.entry-level-wage-to-local-minimum-wage` Entry level wage to local minimum wage. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.means-payout` Means payout. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.actual-or-potential-bonus-paid` Actual or potential bonus paid. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.compensation-and-benefits-cost-to-annual-sales-turnover` Compensation and benefits cost to annual sales turnover. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.wage-rate` Wage rate. Communication `bullet-graph`. Analysis `bar-chart`.
- `kpi.human-resources.social-insurance-cost-per-employee` Social insurance cost per employee. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.medical-insurance-cost-per-employee` Medical insurance cost per employee. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.hourly-compensation-per-employee` Hourly compensation per employee. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.income-per-employee-by-position` Income per employee by position. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.workforce-on-individual-employment-contracts` Workforce on individual employment contracts. Communication `bullet-graph`. Analysis `diverging-bar`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).
