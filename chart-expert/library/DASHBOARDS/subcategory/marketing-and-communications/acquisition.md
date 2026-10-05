---
id: dash.marketing-and-communications.acquisition
type: dashboard
status: placeholder
category: Marketing and Communications
subcategory: Acquisition
context: organizational
audiences: [Executive, Data Analytics, Marketing Analytics]
---

# Marketing and Communications / Acquisition

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Acquisition on the right side of their targets?
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

- `kpi.marketing-and-communications.wins-by-lead-source` Wins by lead source. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.marketing-and-communications.click-through-rate` Click through rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.marketing-and-communications.marketing-qualified-leads` Marketing qualified leads. Communication `bar-chart`. Analysis `bar-chart`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).
