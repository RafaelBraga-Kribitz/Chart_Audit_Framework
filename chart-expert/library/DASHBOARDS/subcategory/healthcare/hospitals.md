---
id: dash.healthcare.hospitals
type: dashboard
status: placeholder
category: Healthcare
subcategory: Hospitals
context: organizational
audiences: [Executive, Data Analytics, Researcher, R&D]
---

# Healthcare / Hospitals

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Hospitals on the right side of their targets?
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

- `kpi.healthcare.hospital-bed-capacity` Hospital bed capacity. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.hospital-bed-occupancy-rate` Hospital bed occupancy rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.unplanned-readmission-rate` Unplanned readmission rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.outpatient-surgeries` Outpatient surgeries. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.length-of-stay-variance` Length of stay variance. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.cases-classified-as-may-not-require-hospitalization-nmn1` Cases classified as May Not Require Hospitalization (NMN1). Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.alternative-level-of-care-days-alc` Alternative level of care days (ALC). Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.medication-error-rate` Medication error rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.surgical-site-infection-rate` Surgical site infection rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.inpatient-mortality` Inpatient mortality. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.peri-operative-mortality` Peri-operative mortality. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.hospital-acquired-infections` Hospital-acquired infections. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.outpatient-revenue` Outpatient revenue. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.hospital-operating-profit-per-bed` Hospital operating profit per bed. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.revenue-per-physician` Revenue per physician. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.er-admissions-by-clinical-condition` ER admissions by clinical condition. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.retreatment-ratio` Retreatment ratio. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.medical-residents-employed-after-residency` Medical residents employed after residency. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.operating-time-on-bypass` Operating time on bypass. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.patient-falls-that-result-in-a-fracture` Patient falls that result in a fracture. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.daily-census` Daily census. Communication `line-chart`. Analysis `bar-chart`.
- `kpi.healthcare.length-of-stay-los` Length of stay (LOS). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.throughput-per-bed` Throughput per bed. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.available-hospital-bed` Available hospital bed. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.patient-visits-resulting-in-transfer` Patient visits resulting in transfer. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.emergency-department-visits-resulting-in-hospital-stay` Emergency department visits resulting in hospital stay. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.time-that-hospital-beds-are-occupied` Time that hospital beds are occupied. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.healthcare.adverse-events-prevalence` Adverse events prevalence. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.medical-ancillary-services` Medical ancillary services. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.casted-up-physician` Casted-up physician. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.surgical-performed` Surgical performed. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.discharges` Discharges. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.nurse-per-physician` Nurse per physician. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.full-time-equivalent-per-occupied-bed` Full Time Equivalent per occupied bed. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.medical-residency-positions-opened` Medical residency positions opened. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.medical-records-with-work` Medical records with work. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.patients-on-the-waiting-list-for-admission-to-long-term-care` Patients on the waiting list for admission to long-term care. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.revenue-per-patient-per-day` Revenue per patient per day. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.medical-support-staff-cost-per-full-time-equivalent-physician` Medical support staff cost per Full Time Equivalent physician. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.compliance-before-patient-contact` Compliance before patient contact. Communication `bullet-graph`. Analysis `diverging-bar`.
- ... 20 more in the subcategory KPI page.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).
