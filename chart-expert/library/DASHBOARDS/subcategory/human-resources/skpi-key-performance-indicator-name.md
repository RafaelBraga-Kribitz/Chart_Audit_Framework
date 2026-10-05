---
id: dash.human-resources.skpi-key-performance-indicator-name
type: dashboard
status: placeholder
category: Human Resources
subcategory: sKPI # Key Performance Indicator name
context: organizational
audiences: [Executive, Data Analytics, HR]
---

# Human Resources / sKPI # Key Performance Indicator name

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in sKPI # Key Performance Indicator name on the right side of their targets?
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

- `kpi.human-resources.overtime-hours-per-employee` Overtime hours per employee. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.sickness-absence-days-per-full-time-equivalent-fte-employee` Sickness absence days per full time equivalent (FTE) employee. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.long-time-due-to-accidents-per-100-000-hours-worked` Long time due to accidents per 100,000 hours worked. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.accidental-or-pay-100-000-hours-worked` Accidental or Pay 100,000 hours worked. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.harassment-and-discrimination-complaints-received` Harassment and discrimination complaints received. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.paid-time-off` Paid time off. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.misradiation-luring-bullying-or-retaliation-campaign-received` Misradiation, luring, bullying or retaliation campaign received. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.total-accidents` Total accidents. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.health-and-safety-prevention-costs` Health and safety prevention costs. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.hours-lost-due-to-absenteeism` Hours lost due to absenteeism. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.lost-time-due-to-strike-action` Lost time due to strike action. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.employees-with-working-home-agreements` Employees with working home agreements. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.job-sharing-agreements` Job sharing agreements. Communication `bullet-graph`. Analysis `diverging-bar`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).
