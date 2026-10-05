# Human Resources / Workforce

Context: organizational. Group: functional. KPIs: 44.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### span of control

- id: `kpi.human-resources.span-of-control`
- kind: kpi
- unit: currency
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

span of control measures that result inside Human Resources, subcategory Workforce. The unit is currency. The formula is A, where A is span of control. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is span of control on the desired side of its target for this period?

Inputs:

- `metric.span-of-control` (span of control)

Placements:

- organizational / functional / Human Resources / Workforce (sK193, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Management-to-staff ratio

- id: `kpi.human-resources.management-to-staff-ratio`
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

Management-to-staff ratio measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Management-to-staff ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Management-to-staff ratio on the desired side of its target for this period?

Inputs:

- `metric.management-to-staff-ratio` (Management-to-staff ratio)

Placements:

- organizational / functional / Human Resources / Workforce (sK194, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Workforce age

- id: `kpi.human-resources.workforce-age`
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

Workforce age measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Workforce age. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Workforce age on the desired side of its target for this period?

Inputs:

- `metric.workforce-age` (Workforce age)

Placements:

- organizational / functional / Human Resources / Workforce (sK245, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Gender ratio

- id: `kpi.human-resources.gender-ratio`
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

Gender ratio measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Gender ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Gender ratio on the desired side of its target for this period?

Inputs:

- `metric.gender-ratio` (Gender ratio)

Placements:

- organizational / functional / Human Resources / Workforce (sK246, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fribic diversity ratio

- id: `kpi.human-resources.fribic-diversity-ratio`
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

Fribic diversity ratio measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Fribic diversity ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fribic diversity ratio on the desired side of its target for this period?

Inputs:

- `metric.fribic-diversity-ratio` (Fribic diversity ratio)

Placements:

- organizational / functional / Human Resources / Workforce (sK247, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Independent contractors

- id: `kpi.human-resources.independent-contractors`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Independent contractors measures that result inside Human Resources, subcategory Workforce. The unit is percent. The formula is (A / B) * 100, where A is part named by Independent contractors, B is whole named by Independent contractors. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Independent contractors on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-independent-contractors` (part named by Independent contractors)
- `metric.whole-named-by-independent-contractors` (whole named by Independent contractors)

Placements:

- organizational / functional / Human Resources / Workforce (sK252, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees nearing retirement age

- id: `kpi.human-resources.employees-nearing-retirement-age`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employees nearing retirement age measures that result inside Human Resources, subcategory Workforce. The unit is percent. The formula is (A / B) * 100, where A is part named by Employees nearing retirement age, B is whole named by Employees nearing retirement age. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees nearing retirement age on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-employees-nearing-retirement-age` (part named by Employees nearing retirement age)
- `metric.whole-named-by-employees-nearing-retirement-age` (whole named by Employees nearing retirement age)

Placements:

- organizational / functional / Human Resources / Workforce (sK698, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Accession rate

- id: `kpi.human-resources.accession-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Accession rate measures that result inside Human Resources, subcategory Workforce. The unit is percent. The formula is (A / B) * 100, where A is numerator of Accession rate, B is base of Accession rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Accession rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-accession-rate` (numerator of Accession rate)
- `metric.base-of-accession-rate` (base of Accession rate)

Placements:

- organizational / functional / Human Resources / Workforce (sK762, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Organization employment staffing breakdown

- id: `kpi.human-resources.organization-employment-staffing-breakdown`
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

Organization employment staffing breakdown measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Organization employment staffing breakdown. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Organization employment staffing breakdown on the desired side of its target for this period?

Inputs:

- `metric.organization-employment-staffing-breakdown` (Organization employment staffing breakdown)

Placements:

- organizational / functional / Human Resources / Workforce (sK1860, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees with delegated spending authority

- id: `kpi.human-resources.employees-with-delegated-spending-authority`
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

Employees with delegated spending authority measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Employees with delegated spending authority. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees with delegated spending authority on the desired side of its target for this period?

Inputs:

- `metric.employees-with-delegated-spending-authority` (Employees with delegated spending authority)

Placements:

- organizational / functional / Human Resources / Workforce (sK2623, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Part time employees

- id: `kpi.human-resources.part-time-employees`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Part time employees measures that result inside Human Resources, subcategory Workforce. The unit is percent. The formula is (A / B) * 100, where A is part named by Part time employees, B is whole named by Part time employees. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Part time employees on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-part-time-employees` (part named by Part time employees)
- `metric.whole-named-by-part-time-employees` (whole named by Part time employees)

Placements:

- organizational / functional / Human Resources / Workforce (sK2024, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Managers who are women

- id: `kpi.human-resources.managers-who-are-women`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Managers who are women measures that result inside Human Resources, subcategory Workforce. The unit is percent. The formula is (A / B) * 100, where A is part named by Managers who are women, B is whole named by Managers who are women. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Managers who are women on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-managers-who-are-women` (part named by Managers who are women)
- `metric.whole-named-by-managers-who-are-women` (whole named by Managers who are women)

Placements:

- organizational / functional / Human Resources / Workforce (sK2025, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Age staffing breakdown

- id: `kpi.human-resources.age-staffing-breakdown`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Age staffing breakdown measures that result inside Human Resources, subcategory Workforce. The unit is percent. The formula is (A / B) * 100, where A is part named by Age staffing breakdown, B is whole named by Age staffing breakdown. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Age staffing breakdown on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-age-staffing-breakdown` (part named by Age staffing breakdown)
- `metric.whole-named-by-age-staffing-breakdown` (whole named by Age staffing breakdown)

Placements:

- organizational / functional / Human Resources / Workforce (sK2026, page_0026)
- organizational / functional / Human Resources / Workforce (sK13978, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Disability staffing rate

- id: `kpi.human-resources.disability-staffing-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Disability staffing rate measures that result inside Human Resources, subcategory Workforce. The unit is percent. The formula is (A / B) * 100, where A is numerator of Disability staffing rate, B is base of Disability staffing rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Disability staffing rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-disability-staffing-rate` (numerator of Disability staffing rate)
- `metric.base-of-disability-staffing-rate` (base of Disability staffing rate)

Placements:

- organizational / functional / Human Resources / Workforce (sK2027, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Customer-facing team size

- id: `kpi.human-resources.customer-facing-team-size`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Customer-facing team size measures that result inside Human Resources, subcategory Workforce. The unit is percent. The formula is (A / B) * 100, where A is part named by Customer-facing team size, B is whole named by Customer-facing team size. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Customer-facing team size on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-customer-facing-team-size` (part named by Customer-facing team size)
- `metric.whole-named-by-customer-facing-team-size` (whole named by Customer-facing team size)

Placements:

- organizational / functional / Human Resources / Workforce (sK2028, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employment level staffing distribution

- id: `kpi.human-resources.employment-level-staffing-distribution`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `histogram` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employment level staffing distribution measures that result inside Human Resources, subcategory Workforce. The unit is percent. The formula is (A / B) * 100, where A is part named by Employment level staffing distribution, B is whole named by Employment level staffing distribution. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employment level staffing distribution on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-employment-level-staffing-distribution` (part named by Employment level staffing distribution)
- `metric.whole-named-by-employment-level-staffing-distribution` (whole named by Employment level staffing distribution)

Placements:

- organizational / functional / Human Resources / Workforce (sK2029, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees distribution by functional area

- id: `kpi.human-resources.employees-distribution-by-functional-area`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `histogram` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employees distribution by functional area measures that result inside Human Resources, subcategory Workforce. The unit is percent. The formula is (A / B) * 100, where A is part named by Employees distribution by functional area, B is whole named by Employees distribution by functional area. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees distribution by functional area on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-employees-distribution-by-functional-area` (part named by Employees distribution by functional area)
- `metric.whole-named-by-employees-distribution-by-functional-area` (whole named by Employees distribution by functional area)

Placements:

- organizational / functional / Human Resources / Workforce (sK2030, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Rookie ratio

- id: `kpi.human-resources.rookie-ratio`
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

Rookie ratio measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Rookie ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Rookie ratio on the desired side of its target for this period?

Inputs:

- `metric.rookie-ratio` (Rookie ratio)

Placements:

- organizational / functional / Human Resources / Workforce (sK2032, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees per process

- id: `kpi.human-resources.employees-per-process`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employees per process measures that result inside Human Resources, subcategory Workforce. The unit is percent. The formula is A / B, where A is Employees, B is process. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees per process on the desired side of its target for this period?

Inputs:

- `metric.employees` (Employees)
- `metric.process` (process)

Placements:

- organizational / functional / Human Resources / Workforce (sK2068, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees per department

- id: `kpi.human-resources.employees-per-department`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employees per department measures that result inside Human Resources, subcategory Workforce. The unit is percent. The formula is A / B, where A is Employees, B is department. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees per department on the desired side of its target for this period?

Inputs:

- `metric.employees` (Employees)
- `metric.department` (department)

Placements:

- organizational / functional / Human Resources / Workforce (sK1890, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Operations staff to total staff ratio

- id: `kpi.human-resources.operations-staff-to-total-staff-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Operations staff to total staff ratio measures that result inside Human Resources, subcategory Workforce. The unit is percent. The formula is (A / B) * 100, where A is Operations staff, B is total staff ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Operations staff to total staff ratio on the desired side of its target for this period?

Inputs:

- `metric.operations-staff` (Operations staff)
- `metric.total-staff-ratio` (total staff ratio)

Placements:

- organizational / functional / Human Resources / Workforce (sK1890, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Ratio of support to total staff

- id: `kpi.human-resources.ratio-of-support-to-total-staff`
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

Ratio of support to total staff measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Ratio of support to total staff. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Ratio of support to total staff on the desired side of its target for this period?

Inputs:

- `metric.ratio-of-support-to-total-staff` (Ratio of support to total staff)

Placements:

- organizational / functional / Human Resources / Workforce (sK8759, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Strategic job coverage

- id: `kpi.human-resources.strategic-job-coverage`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Strategic job coverage measures that result inside Human Resources, subcategory Workforce. The unit is percent. The formula is (A / B) * 100, where A is numerator of Strategic job coverage, B is base of Strategic job coverage. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Strategic job coverage on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-strategic-job-coverage` (numerator of Strategic job coverage)
- `metric.base-of-strategic-job-coverage` (base of Strategic job coverage)

Placements:

- organizational / functional / Human Resources / Workforce (sK8770, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Trianeship programs

- id: `kpi.human-resources.trianeship-programs`
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

Trianeship programs measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Trianeship programs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Trianeship programs on the desired side of its target for this period?

Inputs:

- `metric.trianeship-programs` (Trianeship programs)

Placements:

- organizational / functional / Human Resources / Workforce (sK6824, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Core areas of expertise covered at desired level

- id: `kpi.human-resources.core-areas-of-expertise-covered-at-desired-level`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Core areas of expertise covered at desired level measures that result inside Human Resources, subcategory Workforce. The unit is percent. The formula is (A / B) * 100, where A is Core areas, B is expertise covered at desired level. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Core areas of expertise covered at desired level on the desired side of its target for this period?

Inputs:

- `metric.core-areas` (Core areas)
- `metric.expertise-covered-at-desired-level` (expertise covered at desired level)

Placements:

- organizational / functional / Human Resources / Workforce (sK6884, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Length of contractor assignment

- id: `kpi.human-resources.length-of-contractor-assignment`
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

Length of contractor assignment measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Length of contractor assignment. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Length of contractor assignment on the desired side of its target for this period?

Inputs:

- `metric.length-of-contractor-assignment` (Length of contractor assignment)

Placements:

- organizational / functional / Human Resources / Workforce (sK6944, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Active management

- id: `kpi.human-resources.active-management`
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

Active management measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Active management. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Active management on the desired side of its target for this period?

Inputs:

- `metric.active-management` (Active management)

Placements:

- organizational / functional / Human Resources / Workforce (sK13971, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Age of staff

- id: `kpi.human-resources.age-of-staff`
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

Age of staff measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Age of staff. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Age of staff on the desired side of its target for this period?

Inputs:

- `metric.age-of-staff` (Age of staff)

Placements:

- organizational / functional / Human Resources / Workforce (sK13977, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cumulative work experience in current management team

- id: `kpi.human-resources.cumulative-work-experience-in-current-management-team`
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

Cumulative work experience in current management team measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Cumulative work experience in current management team. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cumulative work experience in current management team on the desired side of its target for this period?

Inputs:

- `metric.cumulative-work-experience-in-current-management-team` (Cumulative work experience in current management team)

Placements:

- organizational / functional / Human Resources / Workforce (sK14059, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Education levels

- id: `kpi.human-resources.education-levels`
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

Education levels measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Education levels. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Education levels on the desired side of its target for this period?

Inputs:

- `metric.education-levels` (Education levels)

Placements:

- organizational / functional / Human Resources / Workforce (sK14096, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Full Time Equivalent (FTE) employees

- id: `kpi.human-resources.full-time-equivalent-fte-employees`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.workforce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Full Time Equivalent (FTE) employees measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Full Time Equivalent (FTE) employees. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Full Time Equivalent (FTE) employees on the desired side of its target for this period?

Inputs:

- `metric.full-time-equivalent-fte-employees` (Full Time Equivalent (FTE) employees)

Placements:

- organizational / functional / Human Resources / Workforce (sK14154, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Full Time Equivalent (FTE) library staff

- id: `kpi.human-resources.full-time-equivalent-fte-library-staff`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.workforce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Full Time Equivalent (FTE) library staff measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Full Time Equivalent (FTE) library staff. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Full Time Equivalent (FTE) library staff on the desired side of its target for this period?

Inputs:

- `metric.full-time-equivalent-fte-library-staff` (Full Time Equivalent (FTE) library staff)

Placements:

- organizational / functional / Human Resources / Workforce (sK14155, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Full Time Equivalent (FTE) per 100 adjusted discharge

- id: `kpi.human-resources.full-time-equivalent-fte-per-100-adjusted-discharge`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Full Time Equivalent (FTE) per 100 adjusted discharge measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A / B, where A is Full Time Equivalent (FTE), B is 100 adjusted discharge. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Full Time Equivalent (FTE) per 100 adjusted discharge on the desired side of its target for this period?

Inputs:

- `metric.full-time-equivalent-fte` (Full Time Equivalent (FTE))
- `metric.100-adjusted-discharge` (100 adjusted discharge)

Placements:

- organizational / functional / Human Resources / Workforce (sK14156, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Full Time Equivalent (FTE) per adjusted day

- id: `kpi.human-resources.full-time-equivalent-fte-per-adjusted-day`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Full Time Equivalent (FTE) per adjusted day measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A / B, where A is Full Time Equivalent (FTE), B is adjusted day. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Full Time Equivalent (FTE) per adjusted day on the desired side of its target for this period?

Inputs:

- `metric.full-time-equivalent-fte` (Full Time Equivalent (FTE))
- `metric.adjusted-day` (adjusted day)

Placements:

- organizational / functional / Human Resources / Workforce (sK14157, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Full Time Equivalent (FTE) per age group

- id: `kpi.human-resources.full-time-equivalent-fte-per-age-group`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Full Time Equivalent (FTE) per age group measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A / B, where A is Full Time Equivalent (FTE), B is age group. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Full Time Equivalent (FTE) per age group on the desired side of its target for this period?

Inputs:

- `metric.full-time-equivalent-fte` (Full Time Equivalent (FTE))
- `metric.age-group` (age group)

Placements:

- organizational / functional / Human Resources / Workforce (sK14158, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Full Time Equivalent (FTE) per average daily census population

- id: `kpi.human-resources.full-time-equivalent-fte-per-average-daily-census-population`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.workforce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Full Time Equivalent (FTE) per average daily census population measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A / B, where A is Full Time Equivalent (FTE), B is average daily census population. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Full Time Equivalent (FTE) per average daily census population on the desired side of its target for this period?

Inputs:

- `metric.full-time-equivalent-fte` (Full Time Equivalent (FTE))
- `metric.average-daily-census-population` (average daily census population)

Placements:

- organizational / functional / Human Resources / Workforce (sK14159, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Labour hours

- id: `kpi.human-resources.labour-hours`
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

Labour hours measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Labour hours. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Labour hours on the desired side of its target for this period?

Inputs:

- `metric.labour-hours` (Labour hours)

Placements:

- organizational / functional / Human Resources / Workforce (sK14164, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Labour productivity

- id: `kpi.human-resources.labour-productivity`
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

Labour productivity measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Labour productivity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Labour productivity on the desired side of its target for this period?

Inputs:

- `metric.labour-productivity` (Labour productivity)

Placements:

- organizational / functional / Human Resources / Workforce (sK14220, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Level of diversity of skills

- id: `kpi.human-resources.level-of-diversity-of-skills`
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

Level of diversity of skills measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Level of diversity of skills. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Level of diversity of skills on the desired side of its target for this period?

Inputs:

- `metric.level-of-diversity-of-skills` (Level of diversity of skills)

Placements:

- organizational / functional / Human Resources / Workforce (sK14221, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Workyears

- id: `kpi.human-resources.workyears`
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

Workyears measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Workyears. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Workyears on the desired side of its target for this period?

Inputs:

- `metric.workyears` (Workyears)

Placements:

- organizational / functional / Human Resources / Workforce (sK14223, page_0026)

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

### Code

- id: `kpi.human-resources.code`
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

Code measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is Code. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Code on the desired side of its target for this period?

Inputs:

- `metric.code` (Code)

Placements:

- organizational / functional / Human Resources / Workforce (sK14274, page_0026)

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

### New labour force

- id: `kpi.human-resources.new-labour-force`
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

New labour force measures that result inside Human Resources, subcategory Workforce. The unit is count. The formula is A, where A is New labour force. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New labour force on the desired side of its target for this period?

Inputs:

- `metric.new-labour-force` (New labour force)

Placements:

- organizational / functional / Human Resources / Workforce (sK22961, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
