---
id: dash.management.forecasts-and-valuation
type: dashboard
status: placeholder
category: Management
subcategory: Forecasts & Valuation
context: organizational
audiences: [Executive, Data Analytics]
---

# Management / Forecasts & Valuation

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Forecasts & Valuation on the right side of their targets?
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

- `kpi.planning.earnings-per-share-eps` § Earnings per share (EPS). Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.management.price-to-earnings-ratio` Price-to-earnings ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.economic-value-added-eva` Economic value added (EVA). Communication `bar-chart`. Analysis `bar-chart`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).
