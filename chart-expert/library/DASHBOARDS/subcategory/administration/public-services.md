---
id: dash.administration.public-services
type: dashboard
status: placeholder
category: Administration
subcategory: Public Services
context: organizational
audiences: [Executive, Data Analytics]
---

# Administration / Public Services

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Public Services on the right side of their targets?
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

- `kpi.administration.crowd-over-travel-market` crowd over travel market. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.administration.building-rehabilitation-projects` Building rehabilitation projects. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.administration.pedants-crossing-with-facilities-for-people-living-with-disabilities` Pedants crossing with facilities for people living with disabilities. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.administration.frequency-of-public-transport-services` Frequency of public transport services. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.administration.on-time-performance-for-public-transport-services` On-time performance for public transport services. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.administration.government-basic-services-available-online` Government basic services available online. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.administration.maturity-of-online-public-service-delivery` Maturity of online public service delivery. Communication `bullet-graph`. Analysis `diverging-bar`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).
