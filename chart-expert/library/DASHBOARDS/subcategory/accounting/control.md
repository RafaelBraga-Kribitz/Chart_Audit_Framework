---
id: dash.accounting.control
type: dashboard
status: placeholder
category: Accounting
subcategory: Control
context: organizational
audiences: [Executive, Data Analytics]
---

# Accounting / Control

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Control on the right side of their targets?
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

- `kpi.accounting.bill-and-proposal-costs` Bill and proposal costs. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.financial-reports-submitted-as-correct-and-on-time` Financial reports submitted as correct and on time. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.non-compliance-statements-evolved` Non-compliance statements evolved. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.time-allocated-to-central-financial-data` Time allocated to central financial data. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.time-allocated-to-decision-support` Time allocated to decision support. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.time-allocated-to-financial-management-activities` Time allocated to financial management activities. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.accuracy-financial-reports` Accuracy financial reports. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.economic-value-added-per-employee` Economic value added per employee. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.revenue-leakage-from-total-revenue` Revenue leakage from total revenue. Communication `bullet-graph`. Analysis `diverging-bar`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).
