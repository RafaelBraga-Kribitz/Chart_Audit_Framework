# Human Resources / Service Delivery

Context: organizational. Group: functional. KPIs: 29.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### HR department cost per FTE

- id: `kpi.human-resources.hr-department-cost-per-fte`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

HR department cost per FTE measures that result inside Human Resources, subcategory Service Delivery. The unit is currency. The formula is A / B, where A is HR department cost, B is FTE. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is HR department cost per FTE on the desired side of its target for this period?

Inputs:

- `metric.hr-department-cost` (HR department cost)
- `metric.fte` (FTE)

Placements:

- organizational / functional / Human Resources / Service Delivery (k83, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### FTEs per HR department FTE

- id: `kpi.human-resources.ftes-per-hr-department-fte`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

FTEs per HR department FTE measures that result inside Human Resources, subcategory Service Delivery. The unit is count. The formula is A / B, where A is FTEs, B is HR department FTE. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is FTEs per HR department FTE on the desired side of its target for this period?

Inputs:

- `metric.ftes` (FTEs)
- `metric.hr-department-fte` (HR department FTE)

Placements:

- organizational / functional / Human Resources / Service Delivery (k844, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### HR outsource rate

- id: `kpi.human-resources.hr-outsource-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

HR outsource rate measures that result inside Human Resources, subcategory Service Delivery. The unit is percent. The formula is (A / B) * 100, where A is numerator of HR outsource rate, B is base of HR outsource rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is HR outsource rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-hr-outsource-rate` (numerator of HR outsource rate)
- `metric.base-of-hr-outsource-rate` (base of HR outsource rate)

Placements:

- organizational / functional / Human Resources / Service Delivery (k45, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Absent days per employee during peak operational periods

- id: `kpi.human-resources.absent-days-per-employee-during-peak-operational-periods`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Absent days per employee during peak operational periods measures that result inside Human Resources, subcategory Service Delivery. The unit is count. The formula is A / B, where A is Absent days, B is employee during peak operational periods. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Absent days per employee during peak operational periods on the desired side of its target for this period?

Inputs:

- `metric.absent-days` (Absent days)
- `metric.employee-during-peak-operational-periods` (employee during peak operational periods)

Placements:

- organizational / functional / Human Resources / Service Delivery (k8752, page_0024)
- organizational / industries / Healthcare / Hotel/Accommodation (sB752, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees who interact with customers

- id: `kpi.human-resources.employees-who-interact-with-customers`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employees who interact with customers measures that result inside Human Resources, subcategory Service Delivery. The unit is percent. The formula is (A / B) * 100, where A is part named by Employees who interact with customers, B is whole named by Employees who interact with customers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees who interact with customers on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-employees-who-interact-with-customers` (part named by Employees who interact with customers)
- `metric.whole-named-by-employees-who-interact-with-customers` (whole named by Employees who interact with customers)

Placements:

- organizational / functional / Human Resources / Service Delivery (k1800, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### HR outsourcing cost

- id: `kpi.human-resources.hr-outsourcing-cost`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

HR outsourcing cost measures that result inside Human Resources, subcategory Service Delivery. The unit is percent. The formula is (A / B) * 100, where A is part named by HR outsourcing cost, B is whole named by HR outsourcing cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is HR outsourcing cost on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-hr-outsourcing-cost` (part named by HR outsourcing cost)
- `metric.whole-named-by-hr-outsourcing-cost` (whole named by HR outsourcing cost)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82021, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Availability of Human Resources IT system

- id: `kpi.human-resources.availability-of-human-resources-it-system`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Availability of Human Resources IT system measures that result inside Human Resources, subcategory Service Delivery. The unit is percent. The formula is (A / B) * 100, where A is Availability, B is Human Resources IT system. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Availability of Human Resources IT system on the desired side of its target for this period?

Inputs:

- `metric.availability` (Availability)
- `metric.human-resources-it-system` (Human Resources IT system)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82033, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### HR or capital staffing ratio

- id: `kpi.human-resources.hr-or-capital-staffing-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

HR or capital staffing ratio measures that result inside Human Resources, subcategory Service Delivery. The unit is count. The formula is A, where A is HR or capital staffing ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is HR or capital staffing ratio on the desired side of its target for this period?

Inputs:

- `metric.hr-or-capital-staffing-ratio` (HR or capital staffing ratio)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82027, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Satisfaction of employees with HR services

- id: `kpi.human-resources.satisfaction-of-employees-with-hr-services`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: survey
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Satisfaction of employees with HR services measures that result inside Human Resources, subcategory Service Delivery. The unit is count. The formula is A, where A is Satisfaction of employees with HR services. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Satisfaction of employees with HR services on the desired side of its target for this period?

Inputs:

- `metric.satisfaction-of-employees-with-hr-services` (Satisfaction of employees with HR services)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82038, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### HR mobility ratio

- id: `kpi.human-resources.hr-mobility-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

HR mobility ratio measures that result inside Human Resources, subcategory Service Delivery. The unit is percent. The formula is (A / B) * 100, where A is numerator of HR mobility ratio, B is base of HR mobility ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is HR mobility ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-hr-mobility-ratio` (numerator of HR mobility ratio)
- `metric.base-of-hr-mobility-ratio` (base of HR mobility ratio)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82039, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### HR related pick ratio

- id: `kpi.human-resources.hr-related-pick-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

HR related pick ratio measures that result inside Human Resources, subcategory Service Delivery. The unit is count. The formula is A, where A is HR related pick ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is HR related pick ratio on the desired side of its target for this period?

Inputs:

- `metric.hr-related-pick-ratio` (HR related pick ratio)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82040, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Human resources staffing breakdown

- id: `kpi.human-resources.human-resources-staffing-breakdown`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Human resources staffing breakdown measures that result inside Human Resources, subcategory Service Delivery. The unit is percent. The formula is (A / B) * 100, where A is part named by Human resources staffing breakdown, B is whole named by Human resources staffing breakdown. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Human resources staffing breakdown on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-human-resources-staffing-breakdown` (part named by Human resources staffing breakdown)
- `metric.whole-named-by-human-resources-staffing-breakdown` (whole named by Human resources staffing breakdown)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82041, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### HR staffing coverage ratio

- id: `kpi.human-resources.hr-staffing-coverage-ratio`
- kind: kpi
- unit: count
- direction: corridor
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

HR staffing coverage ratio measures that result inside Human Resources, subcategory Service Delivery. The unit is count. The formula is A, where A is HR staffing coverage ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is HR staffing coverage ratio on the desired side of its target for this period?

Inputs:

- `metric.hr-staffing-coverage-ratio` (HR staffing coverage ratio)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82042, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### HR staffing ratio distribution by function

- id: `kpi.human-resources.hr-staffing-ratio-distribution-by-function`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `histogram` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

HR staffing ratio distribution by function measures that result inside Human Resources, subcategory Service Delivery. The unit is percent. The formula is (A / B) * 100, where A is numerator of HR staffing ratio distribution by function, B is base of HR staffing ratio distribution by function. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is HR staffing ratio distribution by function on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-hr-staffing-ratio-distribution-by-function` (numerator of HR staffing ratio distribution by function)
- `metric.base-of-hr-staffing-ratio-distribution-by-function` (base of HR staffing ratio distribution by function)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82043, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### HR expense distribution by type

- id: `kpi.human-resources.hr-expense-distribution-by-type`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `histogram` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

HR expense distribution by type measures that result inside Human Resources, subcategory Service Delivery. The unit is percent. The formula is (A / B) * 100, where A is part named by HR expense distribution by type, B is whole named by HR expense distribution by type. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is HR expense distribution by type on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-hr-expense-distribution-by-type` (part named by HR expense distribution by type)
- `metric.whole-named-by-hr-expense-distribution-by-type` (whole named by HR expense distribution by type)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82044, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### HR operating expense rate

- id: `kpi.human-resources.hr-operating-expense-rate`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

HR operating expense rate measures that result inside Human Resources, subcategory Service Delivery. The unit is percent. The formula is (A / B) * 100, where A is numerator of HR operating expense rate, B is base of HR operating expense rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is HR operating expense rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-hr-operating-expense-rate` (numerator of HR operating expense rate)
- `metric.base-of-hr-operating-expense-rate` (base of HR operating expense rate)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82045, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### HR revenue adequacy rate

- id: `kpi.human-resources.hr-revenue-adequacy-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

HR revenue adequacy rate measures that result inside Human Resources, subcategory Service Delivery. The unit is percent. The formula is (A / B) * 100, where A is numerator of HR revenue adequacy rate, B is base of HR revenue adequacy rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is HR revenue adequacy rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-hr-revenue-adequacy-rate` (numerator of HR revenue adequacy rate)
- `metric.base-of-hr-revenue-adequacy-rate` (base of HR revenue adequacy rate)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82047, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### HR revenue per HR full Time Equivalent (FTE)

- id: `kpi.human-resources.hr-revenue-per-hr-full-time-equivalent-fte`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

HR revenue per HR full Time Equivalent (FTE) measures that result inside Human Resources, subcategory Service Delivery. The unit is percent. The formula is A / B, where A is HR revenue, B is HR full Time Equivalent (FTE). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is HR revenue per HR full Time Equivalent (FTE) on the desired side of its target for this period?

Inputs:

- `metric.hr-revenue` (HR revenue)
- `metric.hr-full-time-equivalent-fte` (HR full Time Equivalent (FTE))

Placements:

- organizational / functional / Human Resources / Service Delivery (k82048, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Human Resources Information Technology (HRIT) investment rate

- id: `kpi.human-resources.human-resources-information-technology-hrit-investment-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Human Resources Information Technology (HRIT) investment rate measures that result inside Human Resources, subcategory Service Delivery. The unit is percent. The formula is (A / B) * 100, where A is numerator of Human Resources Information Technology (HRIT) investment rate, B is base of Human Resources Information Technology (HRIT) investment rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Human Resources Information Technology (HRIT) investment rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-human-resources-information-technology-hrit-investment-rate` (numerator of Human Resources Information Technology (HRIT) investment rate)
- `metric.base-of-human-resources-information-technology-hrit-investment-rate` (base of Human Resources Information Technology (HRIT) investment rate)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82049, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Human Resources IT (HRIT) system average days to date

- id: `kpi.human-resources.human-resources-it-hrit-system-average-days-to-date`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: average
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Human Resources IT (HRIT) system average days to date measures that result inside Human Resources, subcategory Service Delivery. The unit is count. The formula is A / B, where A is sum underlying Human Resources IT (HRIT) system average days to date, B is count of observations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Human Resources IT (HRIT) system average days to date on the desired side of its target for this period?

Inputs:

- `metric.sum-underlying-human-resources-it-hrit-system-average-days-to-date` (sum underlying Human Resources IT (HRIT) system average days to date)
- `metric.count-of-observations` (count of observations)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82050, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Human Resources IT (HRIT) system transaction error rate

- id: `kpi.human-resources.human-resources-it-hrit-system-transaction-error-rate`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Human Resources IT (HRIT) system transaction error rate measures that result inside Human Resources, subcategory Service Delivery. The unit is percent. The formula is (A / B) * 100, where A is numerator of Human Resources IT (HRIT) system transaction error rate, B is base of Human Resources IT (HRIT) system transaction error rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Human Resources IT (HRIT) system transaction error rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-human-resources-it-hrit-system-transaction-error-rate` (numerator of Human Resources IT (HRIT) system transaction error rate)
- `metric.base-of-human-resources-it-hrit-system-transaction-error-rate` (base of Human Resources IT (HRIT) system transaction error rate)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82051, page_0024)
- organizational / functional / Human Resources / Service Delivery (k82052, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Overpayment value

- id: `kpi.human-resources.overpayment-value`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Overpayment value measures that result inside Human Resources, subcategory Service Delivery. The unit is currency. The formula is A, where A is Overpayment value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Overpayment value on the desired side of its target for this period?

Inputs:

- `metric.overpayment-value` (Overpayment value)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82053, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Direct deposit participation rate

- id: `kpi.human-resources.direct-deposit-participation-rate`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Direct deposit participation rate measures that result inside Human Resources, subcategory Service Delivery. The unit is currency. The formula is A, where A is Direct deposit participation rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Direct deposit participation rate on the desired side of its target for this period?

Inputs:

- `metric.direct-deposit-participation-rate` (Direct deposit participation rate)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82054, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Overpayment rate

- id: `kpi.human-resources.overpayment-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Overpayment rate measures that result inside Human Resources, subcategory Service Delivery. The unit is percent. The formula is (A / B) * 100, where A is numerator of Overpayment rate, B is base of Overpayment rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Overpayment rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-overpayment-rate` (numerator of Overpayment rate)
- `metric.base-of-overpayment-rate` (base of Overpayment rate)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82055, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Payroll error rate

- id: `kpi.human-resources.payroll-error-rate`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Payroll error rate measures that result inside Human Resources, subcategory Service Delivery. The unit is percent. The formula is (A / B) * 100, where A is numerator of Payroll error rate, B is base of Payroll error rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Payroll error rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-payroll-error-rate` (numerator of Payroll error rate)
- `metric.base-of-payroll-error-rate` (base of Payroll error rate)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82056, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Payroll expense per employee

- id: `kpi.human-resources.payroll-expense-per-employee`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Payroll expense per employee measures that result inside Human Resources, subcategory Service Delivery. The unit is currency. The formula is A / B, where A is Payroll expense, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Payroll expense per employee on the desired side of its target for this period?

Inputs:

- `metric.payroll-expense` (Payroll expense)
- `metric.employee` (employee)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82057, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time sheets incorrectly filled

- id: `kpi.human-resources.time-sheets-incorrectly-filled`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Time sheets incorrectly filled measures that result inside Human Resources, subcategory Service Delivery. The unit is percent. The formula is (A / B) * 100, where A is part named by Time sheets incorrectly filled, B is whole named by Time sheets incorrectly filled. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time sheets incorrectly filled on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-time-sheets-incorrectly-filled` (part named by Time sheets incorrectly filled)
- `metric.whole-named-by-time-sheets-incorrectly-filled` (whole named by Time sheets incorrectly filled)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82059, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Human Capital related savings recommendations submitted and approved

- id: `kpi.human-resources.human-capital-related-savings-recommendations-submitted-and-approved`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Human Capital related savings recommendations submitted and approved measures that result inside Human Resources, subcategory Service Delivery. The unit is count. The formula is A, where A is Human Capital related savings recommendations submitted and approved. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Human Capital related savings recommendations submitted and approved on the desired side of its target for this period?

Inputs:

- `metric.human-capital-related-savings-recommendations-submitted-and-approved` (Human Capital related savings recommendations submitted and approved)

Placements:

- organizational / functional / Human Resources / Service Delivery (k82060, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### HR deficiencies

- id: `kpi.human-resources.hr-deficiencies`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

HR deficiencies measures that result inside Human Resources, subcategory Service Delivery. The unit is count. The formula is A, where A is HR deficiencies. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is HR deficiencies on the desired side of its target for this period?

Inputs:

- `metric.hr-deficiencies` (HR deficiencies)

Placements:

- organizational / functional / Human Resources / Service Delivery (k81493, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
