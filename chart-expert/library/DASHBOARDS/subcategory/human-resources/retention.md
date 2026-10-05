---
id: dash.human-resources.retention
type: dashboard
status: placeholder
category: Human Resources
subcategory: Retention
context: organizational
audiences: [Executive, Data Analytics, HR]
---

# Human Resources / Retention

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Retention on the right side of their targets?
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

- `kpi.management.hours-volunteered-by-employees` Hours volunteered by employees. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.new-hire-failure` New hire failure. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.turnover-cost` Turnover cost. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.time-to-promotion` Time to promotion. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.employee-empowerment-index` Employee empowerment index. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.employee-termination-value` Employee termination value. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.voluntary-termination-cost` Voluntary termination cost. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.termination-value-per-full-time-equivalent-fte` Termination value per full time equivalent (FTE). Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.new-employees-turning-over-cost-rate` New employees turning over cost rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.employee-commitment-index` Employee commitment index. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.employee-engagement-index` Employee engagement index. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.employee-retention-index` Employee retention index. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.staffing-rate-less-than-1-year-tenure` Staffing rate less than 1 year tenure. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.voluntary-termination-rate` Voluntary termination rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.termination-by-performance-rating` Termination by performance rating. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.employment-termination-reason-breakdown` Employment termination reason breakdown. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.new-hire-turnover` New hire turnover. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.employee-perceptions-of-external-job-opportunities-index` Employee perceptions of external job opportunities index. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.early-retirements` Early retirements. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.employees-taking-ill-health-retirement` Employees taking ill health retirement. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.length-of-service-of-senior-level-staff` Length of service of senior level staff. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.unplanned-personnel-losses` Unplanned personnel losses. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.job-subhandlement-cost` Job subhandlement cost. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.unavoidable-officer-terminations` Unavoidable officer terminations. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.employee-satisfaction` Employee satisfaction. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.management-lost` Management lost. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.workers-retaining-employment-after-relocation` Workers retaining employment after relocation. Communication `bar-chart`. Analysis `bar-chart`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).
