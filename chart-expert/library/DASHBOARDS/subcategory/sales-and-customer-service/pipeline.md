---
id: dash.sales-and-customer-service.pipeline
type: dashboard
status: placeholder
category: Sales and Customer Service
subcategory: Pipeline
context: organizational
audiences: [Executive, Data Analytics]
---

# Sales and Customer Service / Pipeline

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Pipeline on the right side of their targets?
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

- `kpi.sales-and-customer-service.closed-won-rate` Closed won rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.sales-and-customer-service.average-deal-size` Average deal size. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.sales-and-customer-service.pipeline-created` Pipeline created. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.sales-and-customer-service.product-demos` Product demos. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.sales-and-customer-service.coaching-sessions` Coaching sessions. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.sales-and-customer-service.new-accounts` New accounts. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.sales-and-customer-service.sales-qualified-leads` Sales qualified leads. Communication `bar-chart`. Analysis `bar-chart`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).
