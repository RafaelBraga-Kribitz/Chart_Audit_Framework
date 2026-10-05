# Healthcare / Hospitals

Context: organizational. Group: industries. KPIs: 60.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Hospital bed capacity

- id: `kpi.healthcare.hospital-bed-capacity`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Hospital bed capacity measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Hospital bed capacity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hospital bed capacity on the desired side of its target for this period?

Inputs:

- `metric.hospital-bed-capacity` (Hospital bed capacity)

Placements:

- organizational / industries / Healthcare / Hospitals (sK40, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hospital bed occupancy rate

- id: `kpi.healthcare.hospital-bed-occupancy-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Hospital bed occupancy rate measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is numerator of Hospital bed occupancy rate, B is base of Hospital bed occupancy rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hospital bed occupancy rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-hospital-bed-occupancy-rate` (numerator of Hospital bed occupancy rate)
- `metric.base-of-hospital-bed-occupancy-rate` (base of Hospital bed occupancy rate)

Placements:

- organizational / industries / Healthcare / Hospitals (sK41, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unplanned readmission rate

- id: `kpi.healthcare.unplanned-readmission-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Unplanned readmission rate measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is numerator of Unplanned readmission rate, B is base of Unplanned readmission rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unplanned readmission rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-unplanned-readmission-rate` (numerator of Unplanned readmission rate)
- `metric.base-of-unplanned-readmission-rate` (base of Unplanned readmission rate)

Placements:

- organizational / industries / Healthcare / Hospitals (sK42, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Outpatient surgeries

- id: `kpi.healthcare.outpatient-surgeries`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Outpatient surgeries measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Outpatient surgeries, B is whole named by Outpatient surgeries. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Outpatient surgeries on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-outpatient-surgeries` (part named by Outpatient surgeries)
- `metric.whole-named-by-outpatient-surgeries` (whole named by Outpatient surgeries)

Placements:

- organizational / industries / Healthcare / Hospitals (sK50, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Length of stay variance

- id: `kpi.healthcare.length-of-stay-variance`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Length of stay variance measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is Length, B is stay variance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Length of stay variance on the desired side of its target for this period?

Inputs:

- `metric.length` (Length)
- `metric.stay-variance` (stay variance)

Placements:

- organizational / industries / Healthcare / Hospitals (sK307, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cases classified as May Not Require Hospitalization (NMN1)

- id: `kpi.healthcare.cases-classified-as-may-not-require-hospitalization-nmn1`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Cases classified as May Not Require Hospitalization (NMN1) measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Cases classified as May Not Require Hospitalization (NMN1), B is whole named by Cases classified as May Not Require Hospitalization (NMN1). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cases classified as May Not Require Hospitalization (NMN1) on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-cases-classified-as-may-not-require-hospitalization-nmn1` (part named by Cases classified as May Not Require Hospitalization (NMN1))
- `metric.whole-named-by-cases-classified-as-may-not-require-hospitalization-nmn1` (whole named by Cases classified as May Not Require Hospitalization (NMN1))

Placements:

- organizational / industries / Healthcare / Hospitals (sK308, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Alternative level of care days (ALC)

- id: `kpi.healthcare.alternative-level-of-care-days-alc`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Alternative level of care days (ALC) measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is Alternative level, B is care days (ALC). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Alternative level of care days (ALC) on the desired side of its target for this period?

Inputs:

- `metric.alternative-level` (Alternative level)
- `metric.care-days-alc` (care days (ALC))

Placements:

- organizational / industries / Healthcare / Hospitals (sK311, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Medication error rate

- id: `kpi.healthcare.medication-error-rate`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Medication error rate measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is numerator of Medication error rate, B is base of Medication error rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Medication error rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-medication-error-rate` (numerator of Medication error rate)
- `metric.base-of-medication-error-rate` (base of Medication error rate)

Placements:

- organizational / industries / Healthcare / Hospitals (sK311, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Surgical site infection rate

- id: `kpi.healthcare.surgical-site-infection-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Surgical site infection rate measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is numerator of Surgical site infection rate, B is base of Surgical site infection rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Surgical site infection rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-surgical-site-infection-rate` (numerator of Surgical site infection rate)
- `metric.base-of-surgical-site-infection-rate` (base of Surgical site infection rate)

Placements:

- organizational / industries / Healthcare / Hospitals (sK312, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Inpatient mortality

- id: `kpi.healthcare.inpatient-mortality`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Inpatient mortality measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Inpatient mortality, B is whole named by Inpatient mortality. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Inpatient mortality on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-inpatient-mortality` (part named by Inpatient mortality)
- `metric.whole-named-by-inpatient-mortality` (whole named by Inpatient mortality)

Placements:

- organizational / industries / Healthcare / Hospitals (sK322, page_0111)
- organizational / industries / Healthcare / Organizational > Industries (sK15614, page_0114)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Peri-operative mortality

- id: `kpi.healthcare.peri-operative-mortality`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Peri-operative mortality measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Peri-operative mortality, B is whole named by Peri-operative mortality. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Peri-operative mortality on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-peri-operative-mortality` (part named by Peri-operative mortality)
- `metric.whole-named-by-peri-operative-mortality` (whole named by Peri-operative mortality)

Placements:

- organizational / industries / Healthcare / Hospitals (sK323, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hospital-acquired infections

- id: `kpi.healthcare.hospital-acquired-infections`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Hospital-acquired infections measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Hospital-acquired infections, B is whole named by Hospital-acquired infections. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hospital-acquired infections on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-hospital-acquired-infections` (part named by Hospital-acquired infections)
- `metric.whole-named-by-hospital-acquired-infections` (whole named by Hospital-acquired infections)

Placements:

- organizational / industries / Healthcare / Hospitals (sK324, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Outpatient revenue

- id: `kpi.healthcare.outpatient-revenue`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Outpatient revenue measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Outpatient revenue, B is whole named by Outpatient revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Outpatient revenue on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-outpatient-revenue` (part named by Outpatient revenue)
- `metric.whole-named-by-outpatient-revenue` (whole named by Outpatient revenue)

Placements:

- organizational / industries / Healthcare / Hospitals (sK2877, page_0111)
- organizational / industries / Healthcare / Organizational » Industries (sK21138, page_0122)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hospital operating profit per bed

- id: `kpi.healthcare.hospital-operating-profit-per-bed`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Hospital operating profit per bed measures that result inside Healthcare, subcategory Hospitals. The unit is currency. The formula is A / B, where A is Hospital operating profit, B is bed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hospital operating profit per bed on the desired side of its target for this period?

Inputs:

- `metric.hospital-operating-profit` (Hospital operating profit)
- `metric.bed` (bed)

Placements:

- organizational / industries / Healthcare / Hospitals (sK2884, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue per physician

- id: `kpi.healthcare.revenue-per-physician`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Revenue per physician measures that result inside Healthcare, subcategory Hospitals. The unit is currency. The formula is A / B, where A is Revenue, B is physician. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue per physician on the desired side of its target for this period?

Inputs:

- `metric.revenue` (Revenue)
- `metric.physician` (physician)

Placements:

- organizational / industries / Healthcare / Hospitals (sK2897, page_0111)
- organizational / industries / Healthcare / Organizational » Industries (sK1976, page_0117)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### ER admissions by clinical condition

- id: `kpi.healthcare.er-admissions-by-clinical-condition`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

ER admissions by clinical condition measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by ER admissions by clinical condition, B is whole named by ER admissions by clinical condition. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is ER admissions by clinical condition on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-er-admissions-by-clinical-condition` (part named by ER admissions by clinical condition)
- `metric.whole-named-by-er-admissions-by-clinical-condition` (whole named by ER admissions by clinical condition)

Placements:

- organizational / industries / Healthcare / Hospitals (sK3159, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Retreatment ratio

- id: `kpi.healthcare.retreatment-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Retreatment ratio measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is numerator of Retreatment ratio, B is base of Retreatment ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Retreatment ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-retreatment-ratio` (numerator of Retreatment ratio)
- `metric.base-of-retreatment-ratio` (base of Retreatment ratio)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4186, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Medical residents employed after residency

- id: `kpi.healthcare.medical-residents-employed-after-residency`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Medical residents employed after residency measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Medical residents employed after residency, B is whole named by Medical residents employed after residency. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Medical residents employed after residency on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-medical-residents-employed-after-residency` (part named by Medical residents employed after residency)
- `metric.whole-named-by-medical-residents-employed-after-residency` (whole named by Medical residents employed after residency)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4192, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Operating time on bypass

- id: `kpi.healthcare.operating-time-on-bypass`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Operating time on bypass measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Operating time on bypass. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Operating time on bypass on the desired side of its target for this period?

Inputs:

- `metric.operating-time-on-bypass` (Operating time on bypass)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4201, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Patient falls that result in a fracture

- id: `kpi.healthcare.patient-falls-that-result-in-a-fracture`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Patient falls that result in a fracture measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Patient falls that result in a fracture, B is whole named by Patient falls that result in a fracture. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Patient falls that result in a fracture on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-patient-falls-that-result-in-a-fracture` (part named by Patient falls that result in a fracture)
- `metric.whole-named-by-patient-falls-that-result-in-a-fracture` (whole named by Patient falls that result in a fracture)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4202, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Daily census

- id: `kpi.healthcare.daily-census`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Daily census measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Daily census. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Daily census on the desired side of its target for this period?

Inputs:

- `metric.daily-census` (Daily census)

Placements:

- organizational / industries / Healthcare / Hospitals (sK5207, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Length of stay (LOS)

- id: `kpi.healthcare.length-of-stay-los`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Length of stay (LOS) measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Length of stay (LOS). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Length of stay (LOS) on the desired side of its target for this period?

Inputs:

- `metric.length-of-stay-los` (Length of stay (LOS))

Placements:

- organizational / industries / Healthcare / Hospitals (sK4212, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Throughput per bed

- id: `kpi.healthcare.throughput-per-bed`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Throughput per bed measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A / B, where A is Throughput, B is bed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Throughput per bed on the desired side of its target for this period?

Inputs:

- `metric.throughput` (Throughput)
- `metric.bed` (bed)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4215, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Available hospital bed

- id: `kpi.healthcare.available-hospital-bed`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Available hospital bed measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Available hospital bed, B is whole named by Available hospital bed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Available hospital bed on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-available-hospital-bed` (part named by Available hospital bed)
- `metric.whole-named-by-available-hospital-bed` (whole named by Available hospital bed)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4216, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Patient visits resulting in transfer

- id: `kpi.healthcare.patient-visits-resulting-in-transfer`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Patient visits resulting in transfer measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Patient visits resulting in transfer, B is whole named by Patient visits resulting in transfer. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Patient visits resulting in transfer on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-patient-visits-resulting-in-transfer` (part named by Patient visits resulting in transfer)
- `metric.whole-named-by-patient-visits-resulting-in-transfer` (whole named by Patient visits resulting in transfer)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4218, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Emergency department visits resulting in hospital stay

- id: `kpi.healthcare.emergency-department-visits-resulting-in-hospital-stay`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Emergency department visits resulting in hospital stay measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Emergency department visits resulting in hospital stay, B is whole named by Emergency department visits resulting in hospital stay. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Emergency department visits resulting in hospital stay on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-emergency-department-visits-resulting-in-hospital-stay` (part named by Emergency department visits resulting in hospital stay)
- `metric.whole-named-by-emergency-department-visits-resulting-in-hospital-stay` (whole named by Emergency department visits resulting in hospital stay)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4219, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time that hospital beds are occupied

- id: `kpi.healthcare.time-that-hospital-beds-are-occupied`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Time that hospital beds are occupied measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Time that hospital beds are occupied, B is whole named by Time that hospital beds are occupied. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time that hospital beds are occupied on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-time-that-hospital-beds-are-occupied` (part named by Time that hospital beds are occupied)
- `metric.whole-named-by-time-that-hospital-beds-are-occupied` (whole named by Time that hospital beds are occupied)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4220, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Adverse events prevalence

- id: `kpi.healthcare.adverse-events-prevalence`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Adverse events prevalence measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Adverse events prevalence. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Adverse events prevalence on the desired side of its target for this period?

Inputs:

- `metric.adverse-events-prevalence` (Adverse events prevalence)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4221, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Medical ancillary services

- id: `kpi.healthcare.medical-ancillary-services`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Medical ancillary services measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Medical ancillary services. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Medical ancillary services on the desired side of its target for this period?

Inputs:

- `metric.medical-ancillary-services` (Medical ancillary services)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4224, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Casted-up physician

- id: `kpi.healthcare.casted-up-physician`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Casted-up physician measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Casted-up physician. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Casted-up physician on the desired side of its target for this period?

Inputs:

- `metric.casted-up-physician` (Casted-up physician)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4226, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Surgical performed

- id: `kpi.healthcare.surgical-performed`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Surgical performed measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Surgical performed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Surgical performed on the desired side of its target for this period?

Inputs:

- `metric.surgical-performed` (Surgical performed)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4229, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Discharges

- id: `kpi.healthcare.discharges`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Discharges measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Discharges. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Discharges on the desired side of its target for this period?

Inputs:

- `metric.discharges` (Discharges)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4230, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Nurse per physician

- id: `kpi.healthcare.nurse-per-physician`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Nurse per physician measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A / B, where A is Nurse, B is physician. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Nurse per physician on the desired side of its target for this period?

Inputs:

- `metric.nurse` (Nurse)
- `metric.physician` (physician)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4232, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Full Time Equivalent per occupied bed

- id: `kpi.healthcare.full-time-equivalent-per-occupied-bed`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Full Time Equivalent per occupied bed measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A / B, where A is Full Time Equivalent, B is occupied bed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Full Time Equivalent per occupied bed on the desired side of its target for this period?

Inputs:

- `metric.full-time-equivalent` (Full Time Equivalent)
- `metric.occupied-bed` (occupied bed)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4233, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Medical residency positions opened

- id: `kpi.healthcare.medical-residency-positions-opened`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Medical residency positions opened measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Medical residency positions opened. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Medical residency positions opened on the desired side of its target for this period?

Inputs:

- `metric.medical-residency-positions-opened` (Medical residency positions opened)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4236, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Medical records with work

- id: `kpi.healthcare.medical-records-with-work`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Medical records with work measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Medical records with work. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Medical records with work on the desired side of its target for this period?

Inputs:

- `metric.medical-records-with-work` (Medical records with work)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4240, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Patients on the waiting list for admission to long-term care

- id: `kpi.healthcare.patients-on-the-waiting-list-for-admission-to-long-term-care`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Patients on the waiting list for admission to long-term care measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Patients on the waiting list for admission to long-term care. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Patients on the waiting list for admission to long-term care on the desired side of its target for this period?

Inputs:

- `metric.patients-on-the-waiting-list-for-admission-to-long-term-care` (Patients on the waiting list for admission to long-term care)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4241, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue per patient per day

- id: `kpi.healthcare.revenue-per-patient-per-day`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Revenue per patient per day measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A / B, where A is Revenue, B is patient per day. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue per patient per day on the desired side of its target for this period?

Inputs:

- `metric.revenue` (Revenue)
- `metric.patient-per-day` (patient per day)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4242, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Medical support staff cost per Full Time Equivalent physician

- id: `kpi.healthcare.medical-support-staff-cost-per-full-time-equivalent-physician`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Medical support staff cost per Full Time Equivalent physician measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A / B, where A is Medical support staff cost, B is Full Time Equivalent physician. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Medical support staff cost per Full Time Equivalent physician on the desired side of its target for this period?

Inputs:

- `metric.medical-support-staff-cost` (Medical support staff cost)
- `metric.full-time-equivalent-physician` (Full Time Equivalent physician)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4243, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Compliance before patient contact

- id: `kpi.healthcare.compliance-before-patient-contact`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Compliance before patient contact measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Compliance before patient contact, B is whole named by Compliance before patient contact. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Compliance before patient contact on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-compliance-before-patient-contact` (part named by Compliance before patient contact)
- `metric.whole-named-by-compliance-before-patient-contact` (whole named by Compliance before patient contact)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4245, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Post discharge complications

- id: `kpi.healthcare.post-discharge-complications`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Post discharge complications measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Post discharge complications. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Post discharge complications on the desired side of its target for this period?

Inputs:

- `metric.post-discharge-complications` (Post discharge complications)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4250, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Reappresentings of critical diseases

- id: `kpi.healthcare.reappresentings-of-critical-diseases`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Reappresentings of critical diseases measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is Reappresentings, B is critical diseases. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Reappresentings of critical diseases on the desired side of its target for this period?

Inputs:

- `metric.reappresentings` (Reappresentings)
- `metric.critical-diseases` (critical diseases)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4251, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cases where a foreign body was left in during procedure

- id: `kpi.healthcare.cases-where-a-foreign-body-was-left-in-during-procedure`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Cases where a foreign body was left in during procedure measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Cases where a foreign body was left in during procedure. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cases where a foreign body was left in during procedure on the desired side of its target for this period?

Inputs:

- `metric.cases-where-a-foreign-body-was-left-in-during-procedure` (Cases where a foreign body was left in during procedure)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4252, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Post operating hematoma

- id: `kpi.healthcare.post-operating-hematoma`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Post operating hematoma measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Post operating hematoma, B is whole named by Post operating hematoma. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Post operating hematoma on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-post-operating-hematoma` (part named by Post operating hematoma)
- `metric.whole-named-by-post-operating-hematoma` (whole named by Post operating hematoma)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4255, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Anesthesia cases

- id: `kpi.healthcare.anesthesia-cases`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Anesthesia cases measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Anesthesia cases. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Anesthesia cases on the desired side of its target for this period?

Inputs:

- `metric.anesthesia-cases` (Anesthesia cases)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4256, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Waiting time for planned surgical care

- id: `kpi.healthcare.waiting-time-for-planned-surgical-care`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Waiting time for planned surgical care measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Waiting time for planned surgical care. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Waiting time for planned surgical care on the desired side of its target for this period?

Inputs:

- `metric.waiting-time-for-planned-surgical-care` (Waiting time for planned surgical care)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4257, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Deaths within a month of a bypass surgery

- id: `kpi.healthcare.deaths-within-a-month-of-a-bypass-surgery`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Deaths within a month of a bypass surgery measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is Deaths within a month, B is a bypass surgery. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Deaths within a month of a bypass surgery on the desired side of its target for this period?

Inputs:

- `metric.deaths-within-a-month` (Deaths within a month)
- `metric.a-bypass-surgery` (a bypass surgery)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4259, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Postoperatively sepsis incidence

- id: `kpi.healthcare.postoperatively-sepsis-incidence`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Postoperatively sepsis incidence measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Postoperatively sepsis incidence, B is whole named by Postoperatively sepsis incidence. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Postoperatively sepsis incidence on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-postoperatively-sepsis-incidence` (part named by Postoperatively sepsis incidence)
- `metric.whole-named-by-postoperatively-sepsis-incidence` (whole named by Postoperatively sepsis incidence)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4260, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Rehospital hospitalization with a month of discharge

- id: `kpi.healthcare.rehospital-hospitalization-with-a-month-of-discharge`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Rehospital hospitalization with a month of discharge measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is Rehospital hospitalization with a month, B is discharge. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Rehospital hospitalization with a month of discharge on the desired side of its target for this period?

Inputs:

- `metric.rehospital-hospitalization-with-a-month` (Rehospital hospitalization with a month)
- `metric.discharge` (discharge)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4261, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Readmission from configuration or infection

- id: `kpi.healthcare.readmission-from-configuration-or-infection`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Readmission from configuration or infection measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is Readmission, B is configuration or infection. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Readmission from configuration or infection on the desired side of its target for this period?

Inputs:

- `metric.readmission` (Readmission)
- `metric.configuration-or-infection` (configuration or infection)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4262, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Risk-adjusted mortality

- id: `kpi.healthcare.risk-adjusted-mortality`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Risk-adjusted mortality measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Risk-adjusted mortality, B is whole named by Risk-adjusted mortality. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Risk-adjusted mortality on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-risk-adjusted-mortality` (part named by Risk-adjusted mortality)
- `metric.whole-named-by-risk-adjusted-mortality` (whole named by Risk-adjusted mortality)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4263, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Surgical infection prevention procedures

- id: `kpi.healthcare.surgical-infection-prevention-procedures`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Surgical infection prevention procedures measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Surgical infection prevention procedures. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Surgical infection prevention procedures on the desired side of its target for this period?

Inputs:

- `metric.surgical-infection-prevention-procedures` (Surgical infection prevention procedures)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4264, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cycle time to discharge patients

- id: `kpi.healthcare.cycle-time-to-discharge-patients`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Cycle time to discharge patients measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Cycle time to discharge patients. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cycle time to discharge patients on the desired side of its target for this period?

Inputs:

- `metric.cycle-time-to-discharge-patients` (Cycle time to discharge patients)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4266, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Delayed inpatient discharges

- id: `kpi.healthcare.delayed-inpatient-discharges`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Delayed inpatient discharges measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Delayed inpatient discharges, B is whole named by Delayed inpatient discharges. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Delayed inpatient discharges on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-delayed-inpatient-discharges` (part named by Delayed inpatient discharges)
- `metric.whole-named-by-delayed-inpatient-discharges` (whole named by Delayed inpatient discharges)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4268, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Heart failure patients discharged home with written instructions

- id: `kpi.healthcare.heart-failure-patients-discharged-home-with-written-instructions`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Heart failure patients discharged home with written instructions measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Heart failure patients discharged home with written instructions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Heart failure patients discharged home with written instructions on the desired side of its target for this period?

Inputs:

- `metric.heart-failure-patients-discharged-home-with-written-instructions` (Heart failure patients discharged home with written instructions)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4269, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Inpatients waiting longer than the standard

- id: `kpi.healthcare.inpatients-waiting-longer-than-the-standard`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Inpatients waiting longer than the standard measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A, where A is Inpatients waiting longer than the standard. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Inpatients waiting longer than the standard on the desired side of its target for this period?

Inputs:

- `metric.inpatients-waiting-longer-than-the-standard` (Inpatients waiting longer than the standard)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4271, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Patients leaving against medical advice

- id: `kpi.healthcare.patients-leaving-against-medical-advice`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Patients leaving against medical advice measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Patients leaving against medical advice, B is whole named by Patients leaving against medical advice. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Patients leaving against medical advice on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-patients-leaving-against-medical-advice` (part named by Patients leaving against medical advice)
- `metric.whole-named-by-patients-leaving-against-medical-advice` (whole named by Patients leaving against medical advice)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4272, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Patients waiting more than x hours

- id: `kpi.healthcare.patients-waiting-more-than-x-hours`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Patients waiting more than x hours measures that result inside Healthcare, subcategory Hospitals. The unit is percent. The formula is (A / B) * 100, where A is part named by Patients waiting more than x hours, B is whole named by Patients waiting more than x hours. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Patients waiting more than x hours on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-patients-waiting-more-than-x-hours` (part named by Patients waiting more than x hours)
- `metric.whole-named-by-patients-waiting-more-than-x-hours` (whole named by Patients waiting more than x hours)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4273, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New patients per physician

- id: `kpi.healthcare.new-patients-per-physician`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

New patients per physician measures that result inside Healthcare, subcategory Hospitals. The unit is count. The formula is A / B, where A is New patients, B is physician. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New patients per physician on the desired side of its target for this period?

Inputs:

- `metric.new-patients` (New patients)
- `metric.physician` (physician)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4274, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost per discharge

- id: `kpi.healthcare.cost-per-discharge`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hospitals`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Cost per discharge measures that result inside Healthcare, subcategory Hospitals. The unit is currency. The formula is A / B, where A is Cost, B is discharge. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost per discharge on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.discharge` (discharge)

Placements:

- organizational / industries / Healthcare / Hospitals (sK4275, page_0111)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
