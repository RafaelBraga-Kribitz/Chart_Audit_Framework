---
id: dash.human-resources.hiring
type: dashboard
status: placeholder
category: Human Resources
subcategory: Hiring
context: organizational
audiences: [Executive, Data Analytics, HR]
---

# Human Resources / Hiring

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Hiring on the right side of their targets?
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

- `kpi.human-resources.account-executives-hired` Account executives hired. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.sales-development-hires` Sales development hires. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.interview-to-offer-ratio` Interview to offer ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.sdrs-trained` SDRs trained. Communication `bar-chart`. Analysis `bar-chart`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).
