---
id: dash.planning.general
type: dashboard
status: placeholder
category: Planning
subcategory: General
context: personal
audiences: [Executive, Data Analytics]
---

# Planning / General

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

- `kpi.planning.ebit-earnings-before-interest-and-taxes` § EBIT (Earnings Before Interest and Taxes). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.planning.operating-expenses` § Operating expenses. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.planning.cost-of-goods-sold-cogs` § Cost of goods sold (COGS). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.planning.asset-turnover` § Asset turnover. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.planning.earnings-per-share-eps` § Earnings per share (EPS). Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.planning.budget-variance` § Budget variance. Communication `waterfall-chart`. Analysis `bar-chart`.
- `kpi.planning.price-to-sales-ratio` § Price to sales ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.planning.perry-ratio` Perry ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.planning.current-ratio` Current ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.planning.working-capital-turnover` Working capital turnover. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.planning.earnings-before-interest-taxes-depreciation-amortization-and-restructuri` § Earnings before interest, taxes, depreciation, amortization, and restructuring or net costs (EBITDAR). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.planning.net-debt` § Net debt. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.planning.net-income-after-taxes-niat` § Net income after taxes (NIAT). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.planning.shareholders-equity` § Shareholders' equity. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.planning.tangible-book-value-per-share-tbvp5` Tangible book value per share (TBVP5). Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.planning.earnings-before-interest-taxes-depreciation-and-amortization-ebitia` § Earnings before interest, taxes, depreciation and amortization (EBITIA). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.planning.breakdown-point-bep` Breakdown point (BEP). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.planning.fixed-assets-per-pte-full-time-equivalent` § Fixed assets per PTE (full Time Equivalent). Communication `horizontal-bar-chart`. Analysis `bar-chart`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).
