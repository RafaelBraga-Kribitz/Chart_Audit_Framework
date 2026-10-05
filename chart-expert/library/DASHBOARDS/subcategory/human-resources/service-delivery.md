---
id: dash.human-resources.service-delivery
type: dashboard
status: placeholder
category: Human Resources
subcategory: Service Delivery
context: organizational
audiences: [Executive, Data Analytics, HR]
---

# Human Resources / Service Delivery

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Service Delivery on the right side of their targets?
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

- `kpi.human-resources.hr-department-cost-per-fte` HR department cost per FTE. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.ftes-per-hr-department-fte` FTEs per HR department FTE. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.hr-outsource-rate` HR outsource rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.absent-days-per-employee-during-peak-operational-periods` Absent days per employee during peak operational periods. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.employees-who-interact-with-customers` Employees who interact with customers. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.hr-outsourcing-cost` HR outsourcing cost. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.availability-of-human-resources-it-system` Availability of Human Resources IT system. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.hr-or-capital-staffing-ratio` HR or capital staffing ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.satisfaction-of-employees-with-hr-services` Satisfaction of employees with HR services. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.hr-mobility-ratio` HR mobility ratio. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.hr-related-pick-ratio` HR related pick ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.human-resources-staffing-breakdown` Human resources staffing breakdown. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.hr-staffing-coverage-ratio` HR staffing coverage ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.hr-staffing-ratio-distribution-by-function` HR staffing ratio distribution by function. Communication `bullet-graph`. Analysis `histogram`.
- `kpi.human-resources.hr-expense-distribution-by-type` HR expense distribution by type. Communication `bullet-graph`. Analysis `histogram`.
- `kpi.human-resources.hr-operating-expense-rate` HR operating expense rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.hr-revenue-adequacy-rate` HR revenue adequacy rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.hr-revenue-per-hr-full-time-equivalent-fte` HR revenue per HR full Time Equivalent (FTE). Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.human-resources-information-technology-hrit-investment-rate` Human Resources Information Technology (HRIT) investment rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.human-resources-it-hrit-system-average-days-to-date` Human Resources IT (HRIT) system average days to date. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.human-resources-it-hrit-system-transaction-error-rate` Human Resources IT (HRIT) system transaction error rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.overpayment-value` Overpayment value. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.direct-deposit-participation-rate` Direct deposit participation rate. Communication `bullet-graph`. Analysis `bar-chart`.
- `kpi.human-resources.overpayment-rate` Overpayment rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.payroll-error-rate` Payroll error rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.payroll-expense-per-employee` Payroll expense per employee. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.time-sheets-incorrectly-filled` Time sheets incorrectly filled. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.human-resources.human-capital-related-savings-recommendations-submitted-and-approved` Human Capital related savings recommendations submitted and approved. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.human-resources.hr-deficiencies` HR deficiencies. Communication `bar-chart`. Analysis `bar-chart`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).
