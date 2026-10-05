---
id: dash.management.profitability
type: dashboard
status: placeholder
category: Management
subcategory: Profitability
context: organizational
audiences: [Executive, Data Analytics]
---

# Management / Profitability

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

- `kpi.accounting.gross-profit-margin` Gross profit margin. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.planning.asset-turnover` § Asset turnover. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.sbit-farnings-before-interest-and-taxes` SBIT (Farnings Before Interest and Taxes). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.return-on-equity-roe` Return on equity (ROE). Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.return-on-asset` Return on asset. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.return-on-security-investment-rosii` Return on security investment (ROSII). Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.return-on-total-assets-rota` Return on total assets (ROTA). Communication `bullet-graph`. Analysis `diverging-bar`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).
