---
id: dash.finance.general
type: dashboard
status: placeholder
category: Finance
subcategory: General
context: organizational
audiences: [Executive, Data Analytics]
---

# Finance / General

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in General on the right side of their targets?
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

- `kpi.finance.revenue-generated-from-the-sale-of-local-community-surplus-goods` Revenue generated from the sale of local community surplus goods. Communication `bullet-graph`. Analysis `bar-chart`.
- `kpi.finance.family-homes-market-value-from-sales-price` Family homes market value from sales price. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.finance.time-to-record-a-property-interest-from-transfer-date` Time to record a property interest from transfer date. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.finance.increases-in-tax-liability-as-a-result-of-audits` Increases in tax liability as a result of audits. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.finance.time-to-issue-a-property-tax-refund` Time to issue a property tax refund. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.finance.managed-expenditure-mre` Managed expenditure (MRE). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.finance.national-public-spending-expenditure-on-services` National public spending expenditure on services. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.finance.tax-collected-on-time` Tax collected on time. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.finance.days-sales-outstanding` Days Sales Outstanding. Communication `bullet-graph`. Analysis `waterfall-chart`.
- `kpi.finance.cost-per-acquisition` Cost Per Acquisition. Communication `bullet-graph`. Analysis `waterfall-chart`.
- `kpi.finance.monthly-recurring-revenue` Monthly Recurring Revenue. Communication `bullet-graph`. Analysis `waterfall-chart`.
- `kpi.finance.customer-churn-rate` Customer Churn Rate. Communication `bullet-graph`. Analysis `waterfall-chart`.
- `kpi.finance.utilization-rate` Utilization Rate. Communication `bullet-graph`. Analysis `waterfall-chart`.
- `kpi.finance.labour-efficiency-ratio` Labour Efficiency Ratio. Communication `bullet-graph`. Analysis `waterfall-chart`.
- `kpi.finance.labor-efficiency-ratio` Labor Efficiency Ratio. Communication `bullet-graph`. Analysis `waterfall-chart`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).
