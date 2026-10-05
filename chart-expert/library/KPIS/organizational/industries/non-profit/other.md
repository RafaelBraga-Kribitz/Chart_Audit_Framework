# Non-profit / Other

Context: organizational. Group: industries. KPIs: 40.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Net account receivable days

- id: `kpi.planning.net-account-receivable-days`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Net account receivable days measures that result inside Planning, subcategory Organizational » Functional Areas. The unit is count. The formula is A, where A is Net account receivable days. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Net account receivable days on the desired side of its target for this period?

Inputs:

- `metric.net-account-receivable-days` (Net account receivable days)

Placements:

- organizational / functional / Planning / Organizational » Functional Areas (sK6164, page_0011)
- organizational / industries / Non-profit / Other (xK6164, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Payroll tax paid by the employer

- id: `kpi.management.payroll-tax-paid-by-the-employer`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Payroll tax paid by the employer measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Payroll tax paid by the employer. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Payroll tax paid by the employer on the desired side of its target for this period?

Inputs:

- `metric.payroll-tax-paid-by-the-employer` (Payroll tax paid by the employer)

Placements:

- organizational / functional / Management / Financial stability (x3945, page_0017)
- organizational / industries / Non-profit / Other (xK5945, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Expense of temporary staffing to labor cost

- id: `kpi.human-resources.expense-of-temporary-staffing-to-labor-cost`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.organizational-functional-areas`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Expense of temporary staffing to labor cost measures that result inside Human Resources, subcategory Organizational » Functional Areas. The unit is percent. The formula is (A / B) * 100, where A is Expense, B is temporary staffing to labor cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Expense of temporary staffing to labor cost on the desired side of its target for this period?

Inputs:

- `metric.expense` (Expense)
- `metric.temporary-staffing-to-labor-cost` (temporary staffing to labor cost)

Placements:

- organizational / functional / Human Resources / Organizational » Functional Areas (KPI940, page_0022)
- organizational / industries / Non-profit / Other (xK6440, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Staff attendance rate

- id: `kpi.human-resources.staff-attendance-rate`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Staff attendance rate measures that result inside Human Resources, subcategory Organizational » Functional Areas. The unit is count. The formula is A, where A is Staff attendance rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Staff attendance rate on the desired side of its target for this period?

Inputs:

- `metric.staff-attendance-rate` (Staff attendance rate)

Placements:

- organizational / functional / Human Resources / Organizational » Functional Areas (sK22456, page_0023)
- organizational / industries / Non-profit / Other (xK22456, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hours of training per FTE

- id: `kpi.human-resources.hours-of-training-per-fte`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Hours of training per FTE measures that result inside Human Resources, subcategory Organizational > Functional Areas. The unit is count. The formula is A / B, where A is Hours of training, B is FTE. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hours of training per FTE on the desired side of its target for this period?

Inputs:

- `metric.hours-of-training` (Hours of training)
- `metric.fte` (FTE)

Placements:

- organizational / functional / Human Resources / Organizational > Functional Areas (sK22472, page_0026)
- organizational / industries / Non-profit / Other (xK22472, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Ratio of production staff to administrative and supervisory staff

- id: `kpi.human-resources.ratio-of-production-staff-to-administrative-and-supervisory-staff`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.workforce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Ratio of production staff to administrative and supervisory staff measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Ratio of production staff to administrative and supervisory staff. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Ratio of production staff to administrative and supervisory staff on the desired side of its target for this period?

Inputs:

- `metric.ratio-of-production-staff-to-administrative-and-supervisory-staff` (Ratio of production staff to administrative and supervisory staff)

Placements:

- organizational / functional / Human Resources / Workforce (sK14270, page_0026)
- organizational / industries / Non-profit / Other (xK2470, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees by union code

- id: `kpi.human-resources.employees-by-union-code`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.workforce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employees by union code measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Employees by union code. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees by union code on the desired side of its target for this period?

Inputs:

- `metric.employees-by-union-code` (Employees by union code)

Placements:

- organizational / functional / Human Resources / Workforce (sK22234, page_0026)
- organizational / industries / Non-profit / Other (xK22523, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Work hours lost to accidents

- id: `kpi.human-resources.work-hours-lost-to-accidents`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Work hours lost to accidents measures that result inside Human Resources, subcategory Organizational > Functional Areas. The unit is count. The formula is A, where A is Work hours lost to accidents. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Work hours lost to accidents on the desired side of its target for this period?

Inputs:

- `metric.work-hours-lost-to-accidents` (Work hours lost to accidents)

Placements:

- organizational / functional / Human Resources / Organizational > Functional Areas (sK22471, page_0027)
- organizational / industries / Non-profit / Other (xK22471, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of testing and debugging

- id: `kpi.information-technology.cost-of-testing-and-debugging`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.application-development`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Cost of testing and debugging measures that result inside Information Technology, subcategory Application Development. The unit is percent. The formula is (A / B) * 100, where A is Cost, B is testing and debugging. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of testing and debugging on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.testing-and-debugging` (testing and debugging)

Placements:

- organizational / functional / Information Technology / Application Development (s85.06, page_0028)
- organizational / industries / Non-profit / Other (xK6096, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time to market (TTM)

- id: `kpi.information-technology.time-to-market-ttm`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.application-development`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Time to market (TTM) measures that result inside Information Technology, subcategory Application Development. The unit is count. The formula is A, where A is Time to market (TTM). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time to market (TTM) on the desired side of its target for this period?

Inputs:

- `metric.time-to-market-ttm` (Time to market (TTM))

Placements:

- organizational / functional / Information Technology / Application Development (s80.98, page_0028)
- organizational / industries / Non-profit / Other (xK6098, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Software process execution time in seconds

- id: `kpi.information-technology.software-process-execution-time-in-seconds`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.application-development`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Software process execution time in seconds measures that result inside Information Technology, subcategory Application Development. The unit is count. The formula is A, where A is Software process execution time in seconds. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Software process execution time in seconds on the desired side of its target for this period?

Inputs:

- `metric.software-process-execution-time-in-seconds` (Software process execution time in seconds)

Placements:

- organizational / functional / Information Technology / Application Development (s85.09, page_0028)
- organizational / industries / Non-profit / Other (xK6099, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Software sales from revenue

- id: `kpi.information-technology.software-sales-from-revenue`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.application-development`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Software sales from revenue measures that result inside Information Technology, subcategory Application Development. The unit is percent. The formula is (A / B) * 100, where A is Software sales, B is revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Software sales from revenue on the desired side of its target for this period?

Inputs:

- `metric.software-sales` (Software sales)
- `metric.revenue` (revenue)

Placements:

- organizational / functional / Information Technology / Application Development (s80.15, page_0028)
- organizational / industries / Non-profit / Other (xK6105, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### User inputs with improper error handling

- id: `kpi.information-technology.user-inputs-with-improper-error-handling`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.application-development`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

User inputs with improper error handling measures that result inside Information Technology, subcategory Application Development. The unit is percent. The formula is (A / B) * 100, where A is part named by User inputs with improper error handling, B is whole named by User inputs with improper error handling. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is User inputs with improper error handling on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-user-inputs-with-improper-error-handling` (part named by User inputs with improper error handling)
- `metric.whole-named-by-user-inputs-with-improper-error-handling` (whole named by User inputs with improper error handling)

Placements:

- organizational / functional / Information Technology / Application Development (s81.15, page_0028)
- organizational / industries / Non-profit / Other (xK6115, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Encrypted servers

- id: `kpi.information-technology.encrypted-servers`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.organizational-functional-areas`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Encrypted servers measures that result inside Information Technology, subcategory Organizational » Functional Areas. The unit is percent. The formula is (A / B) * 100, where A is part named by Encrypted servers, B is whole named by Encrypted servers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Encrypted servers on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-encrypted-servers` (part named by Encrypted servers)
- `metric.whole-named-by-encrypted-servers` (whole named by Encrypted servers)

Placements:

- organizational / functional / Information Technology / Organizational » Functional Areas (xK6116, page_0032)
- organizational / industries / Non-profit / Other (xK6116, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Subscribers enrolled for automated notifications

- id: `kpi.management.subscribers-enrolled-for-automated-notifications`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Subscribers enrolled for automated notifications measures that result inside Management, subcategory Organizational » Functional Areas. The unit is count. The formula is A, where A is Subscribers enrolled for automated notifications. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Subscribers enrolled for automated notifications on the desired side of its target for this period?

Inputs:

- `metric.subscribers-enrolled-for-automated-notifications` (Subscribers enrolled for automated notifications)

Placements:

- organizational / functional / Management / Organizational » Functional Areas (sK6039, page_0035)
- organizational / industries / Non-profit / Other (xK6039, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### User load capacity

- id: `kpi.management.user-load-capacity`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

User load capacity measures that result inside Management, subcategory Organizational » Functional Areas. The unit is count. The formula is A, where A is User load capacity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is User load capacity on the desired side of its target for this period?

Inputs:

- `metric.user-load-capacity` (User load capacity)

Placements:

- organizational / functional / Management / Organizational » Functional Areas (sK6110, page_0035)
- organizational / industries / Non-profit / Other (xK6110, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Frequency of customer complaints

- id: `kpi.sales-and-customer-service.frequency-of-customer-complaints`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Frequency of customer complaints measures that result inside Sales and Customer Service, subcategory Organizational » Functional Areas. The unit is count. The formula is A, where A is Frequency of customer complaints. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Frequency of customer complaints on the desired side of its target for this period?

Inputs:

- `metric.frequency-of-customer-complaints` (Frequency of customer complaints)

Placements:

- organizational / functional / Sales and Customer Service / Organizational » Functional Areas (sE24273, page_0050)
- organizational / industries / Non-profit / Other (xK22473, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Visit customers served within 3 minutes

- id: `kpi.sales-and-customer-service.visit-customers-served-within-3-minutes`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Visit customers served within 3 minutes measures that result inside Sales and Customer Service, subcategory Organizational » Functional Areas. The unit is count. The formula is A, where A is Visit customers served within 3 minutes. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Visit customers served within 3 minutes on the desired side of its target for this period?

Inputs:

- `metric.visit-customers-served-within-3-minutes` (Visit customers served within 3 minutes)

Placements:

- organizational / functional / Sales and Customer Service / Organizational » Functional Areas (sE25299, page_0050)
- organizational / industries / Non-profit / Other (xK22597, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### On-time and accurate raw material orders

- id: `kpi.management.on-time-and-accurate-raw-material-orders`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.organizational-functional-areas`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

On-time and accurate raw material orders measures that result inside Management, subcategory Organizational > Functional Areas. The unit is percent. The formula is (A / B) * 100, where A is numerator of On-time and accurate raw material orders, B is base of On-time and accurate raw material orders. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is On-time and accurate raw material orders on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-on-time-and-accurate-raw-material-orders` (numerator of On-time and accurate raw material orders)
- `metric.base-of-on-time-and-accurate-raw-material-orders` (base of On-time and accurate raw material orders)

Placements:

- organizational / functional / Management / Organizational > Functional Areas (s42959, page_0056)
- organizational / industries / Non-profit / Other (xK4529, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Services

- id: `kpi.non-profit.services`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Services measures that result inside Non-profit, subcategory Other. The unit is number. The formula is A, where A is Services. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Services on the desired side of its target for this period?

Inputs:

- `metric.services` (Services)

Placements:

- organizational / industries / Non-profit / Other (xK6095, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Clicks

- id: `kpi.non-profit.clicks`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Clicks measures that result inside Non-profit, subcategory Other. The unit is count. The formula is A, where A is Clicks. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Clicks on the desired side of its target for this period?

Inputs:

- `metric.clicks` (Clicks)

Placements:

- organizational / industries / Non-profit / Other (xK22474, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Bugg's Rep. 1,000 Hours of code (RIOC)

- id: `kpi.non-profit.bugg-s-rep-1-000-hours-of-code-rioc`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Bugg's Rep. 1,000 Hours of code (RIOC) measures that result inside Non-profit, subcategory Other. The unit is count. The formula is A, where A is Bugg's Rep. 1,000 Hours of code (RIOC). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Bugg's Rep. 1,000 Hours of code (RIOC) on the desired side of its target for this period?

Inputs:

- `metric.bugg-s-rep-1-000-hours-of-code-rioc` (Bugg's Rep. 1,000 Hours of code (RIOC))

Placements:

- organizational / industries / Non-profit / Other (xK6096, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cheques cleared to standard

- id: `kpi.non-profit.cheques-cleared-to-standard`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.non-profit.other`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cheques cleared to standard measures that result inside Non-profit, subcategory Other. The unit is percent. The formula is (A / B) * 100, where A is Cheques cleared, B is standard. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cheques cleared to standard on the desired side of its target for this period?

Inputs:

- `metric.cheques-cleared` (Cheques cleared)
- `metric.standard` (standard)

Placements:

- organizational / industries / Non-profit / Other (xK22593, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Staff key competencies

- id: `kpi.non-profit.staff-key-competencies`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Staff key competencies measures that result inside Non-profit, subcategory Other. The unit is count. The formula is A, where A is Staff key competencies. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Staff key competencies on the desired side of its target for this period?

Inputs:

- `metric.staff-key-competencies` (Staff key competencies)

Placements:

- organizational / industries / Non-profit / Other (xK22598, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Software defects per testing minute

- id: `kpi.non-profit.software-defects-per-testing-minute`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Software defects per testing minute measures that result inside Non-profit, subcategory Other. The unit is count. The formula is A / B, where A is Software defects, B is testing minute. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Software defects per testing minute on the desired side of its target for this period?

Inputs:

- `metric.software-defects` (Software defects)
- `metric.testing-minute` (testing minute)

Placements:

- organizational / industries / Non-profit / Other (xK6102, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Performance management maturity level

- id: `kpi.non-profit.performance-management-maturity-level`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Performance management maturity level measures that result inside Non-profit, subcategory Other. The unit is count. The formula is A, where A is Performance management maturity level. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Performance management maturity level on the desired side of its target for this period?

Inputs:

- `metric.performance-management-maturity-level` (Performance management maturity level)

Placements:

- organizational / industries / Non-profit / Other (xK22583, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Single-user licensee sold

- id: `kpi.non-profit.single-user-licensee-sold`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.non-profit.other`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Single-user licensee sold measures that result inside Non-profit, subcategory Other. The unit is percent. The formula is (A / B) * 100, where A is part named by Single-user licensee sold, B is whole named by Single-user licensee sold. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Single-user licensee sold on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-single-user-licensee-sold` (part named by Single-user licensee sold)
- `metric.whole-named-by-single-user-licensee-sold` (whole named by Single-user licensee sold)

Placements:

- organizational / industries / Non-profit / Other (xK6103, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Total Quality Management (TQM) maturity level

- id: `kpi.non-profit.total-quality-management-tqm-maturity-level`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Total Quality Management (TQM) maturity level measures that result inside Non-profit, subcategory Other. The unit is count. The formula is A, where A is Total Quality Management (TQM) maturity level. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Total Quality Management (TQM) maturity level on the desired side of its target for this period?

Inputs:

- `metric.total-quality-management-tqm-maturity-level` (Total Quality Management (TQM) maturity level)

Placements:

- organizational / industries / Non-profit / Other (xK22598, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Multi-user licensees sold

- id: `kpi.non-profit.multi-user-licensees-sold`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.non-profit.other`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Multi-user licensees sold measures that result inside Non-profit, subcategory Other. The unit is percent. The formula is (A / B) * 100, where A is part named by Multi-user licensees sold, B is whole named by Multi-user licensees sold. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Multi-user licensees sold on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-multi-user-licensees-sold` (part named by Multi-user licensees sold)
- `metric.whole-named-by-multi-user-licensees-sold` (whole named by Multi-user licensees sold)

Placements:

- organizational / industries / Non-profit / Other (xK6104, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Activity Based Costing maturity level

- id: `kpi.non-profit.activity-based-costing-maturity-level`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Activity Based Costing maturity level measures that result inside Non-profit, subcategory Other. The unit is count. The formula is A, where A is Activity Based Costing maturity level. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Activity Based Costing maturity level on the desired side of its target for this period?

Inputs:

- `metric.activity-based-costing-maturity-level` (Activity Based Costing maturity level)

Placements:

- organizational / industries / Non-profit / Other (xK22986, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Environmental Management System maturity level

- id: `kpi.non-profit.environmental-management-system-maturity-level`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Environmental Management System maturity level measures that result inside Non-profit, subcategory Other. The unit is count. The formula is A, where A is Environmental Management System maturity level. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Environmental Management System maturity level on the desired side of its target for this period?

Inputs:

- `metric.environmental-management-system-maturity-level` (Environmental Management System maturity level)

Placements:

- organizational / industries / Non-profit / Other (xK22987, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Single-user licence price

- id: `kpi.non-profit.single-user-licence-price`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Single-user licence price measures that result inside Non-profit, subcategory Other. The unit is count. The formula is A, where A is Single-user licence price. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Single-user licence price on the desired side of its target for this period?

Inputs:

- `metric.single-user-licence-price` (Single-user licence price)

Placements:

- organizational / industries / Non-profit / Other (xK6106, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Balanced Scorecard maturity level

- id: `kpi.non-profit.balanced-scorecard-maturity-level`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: survey
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Balanced Scorecard maturity level measures that result inside Non-profit, subcategory Other. The unit is count. The formula is A, where A is Balanced Scorecard maturity level. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Balanced Scorecard maturity level on the desired side of its target for this period?

Inputs:

- `metric.balanced-scorecard-maturity-level` (Balanced Scorecard maturity level)

Placements:

- organizational / industries / Non-profit / Other (xK22988, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Business Process Re-engineering maturity level

- id: `kpi.non-profit.business-process-re-engineering-maturity-level`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Business Process Re-engineering maturity level measures that result inside Non-profit, subcategory Other. The unit is count. The formula is A, where A is Business Process Re-engineering maturity level. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Business Process Re-engineering maturity level on the desired side of its target for this period?

Inputs:

- `metric.business-process-re-engineering-maturity-level` (Business Process Re-engineering maturity level)

Placements:

- organizational / industries / Non-profit / Other (xK22989, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Quality Management System maturity level

- id: `kpi.non-profit.quality-management-system-maturity-level`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Quality Management System maturity level measures that result inside Non-profit, subcategory Other. The unit is count. The formula is A, where A is Quality Management System maturity level. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Quality Management System maturity level on the desired side of its target for this period?

Inputs:

- `metric.quality-management-system-maturity-level` (Quality Management System maturity level)

Placements:

- organizational / industries / Non-profit / Other (xK22990, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### EFQM maturity level

- id: `kpi.non-profit.efqm-maturity-level`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

EFQM maturity level measures that result inside Non-profit, subcategory Other. The unit is count. The formula is A, where A is EFQM maturity level. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is EFQM maturity level on the desired side of its target for this period?

Inputs:

- `metric.efqm-maturity-level` (EFQM maturity level)

Placements:

- organizational / industries / Non-profit / Other (xK22991, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Value based Management maturity level

- id: `kpi.non-profit.value-based-management-maturity-level`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Value based Management maturity level measures that result inside Non-profit, subcategory Other. The unit is count. The formula is A, where A is Value based Management maturity level. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Value based Management maturity level on the desired side of its target for this period?

Inputs:

- `metric.value-based-management-maturity-level` (Value based Management maturity level)

Placements:

- organizational / industries / Non-profit / Other (xK22992, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Malcolm Baldridge Award assessment level

- id: `kpi.non-profit.malcolm-baldridge-award-assessment-level`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Malcolm Baldridge Award assessment level measures that result inside Non-profit, subcategory Other. The unit is count. The formula is A, where A is Malcolm Baldridge Award assessment level. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Malcolm Baldridge Award assessment level on the desired side of its target for this period?

Inputs:

- `metric.malcolm-baldridge-award-assessment-level` (Malcolm Baldridge Award assessment level)

Placements:

- organizational / industries / Non-profit / Other (xK22993, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Vehicles loaded or unloaded per labor hour

- id: `kpi.non-profit.vehicles-loaded-or-unloaded-per-labor-hour`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Vehicles loaded or unloaded per labor hour measures that result inside Non-profit, subcategory Other. The unit is count. The formula is A / B, where A is Vehicles loaded or unloaded, B is labor hour. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Vehicles loaded or unloaded per labor hour on the desired side of its target for this period?

Inputs:

- `metric.vehicles-loaded-or-unloaded` (Vehicles loaded or unloaded)
- `metric.labor-hour` (labor hour)

Placements:

- organizational / industries / Non-profit / Other (xK22996, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Weight loaded or unloaded per labor hour

- id: `kpi.non-profit.weight-loaded-or-unloaded-per-labor-hour`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.non-profit.other`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Weight loaded or unloaded per labor hour measures that result inside Non-profit, subcategory Other. The unit is count. The formula is A / B, where A is Weight loaded or unloaded, B is labor hour. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Weight loaded or unloaded per labor hour on the desired side of its target for this period?

Inputs:

- `metric.weight-loaded-or-unloaded` (Weight loaded or unloaded)
- `metric.labor-hour` (labor hour)

Placements:

- organizational / industries / Non-profit / Other (xK22997, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
