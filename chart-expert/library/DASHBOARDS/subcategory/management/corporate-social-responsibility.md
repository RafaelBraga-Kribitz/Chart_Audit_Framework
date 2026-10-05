---
id: dash.management.corporate-social-responsibility
type: dashboard
status: placeholder
category: Management
subcategory: Corporate Social Responsibility
context: organizational
audiences: [Executive, Data Analytics]
---

# Management / Corporate Social Responsibility

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Corporate Social Responsibility on the right side of their targets?
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

- `kpi.management.funds-raised-per-employee` Funds raised per employee. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.management.investment-in-the-community` Investment in the community. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.hours-volunteered-by-employees` Hours volunteered by employees. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.partnerships-with-non-profit-organizations-non-governmental-organization` Partnerships with non-profit organizations / non-governmental organizations. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.community-satisfaction-index` Community satisfaction index. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.local-residents-in-tool-workforce` Local residents in tool workforce. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.sponsorship-projects` Sponsorship projects. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.students-recruited-for-holiday-work` Students recruited for holiday work. Communication `bar-chart`. Analysis `bar-chart`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).
