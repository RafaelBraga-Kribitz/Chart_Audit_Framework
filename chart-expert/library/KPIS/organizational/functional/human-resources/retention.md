# Human Resources / Retention

Context: organizational. Group: functional. KPIs: 27.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Hours volunteered by employees

- id: `kpi.management.hours-volunteered-by-employees`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.corporate-social-responsibility`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Hours volunteered by employees measures that result inside Management, subcategory Corporate Social Responsibility. The unit is count. The formula is A, where A is Hours volunteered by employees. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hours volunteered by employees on the desired side of its target for this period?

Inputs:

- `metric.hours-volunteered-by-employees` (Hours volunteered by employees)

Placements:

- organizational / functional / Management / Corporate Social Responsibility (sK588, page_0013)
- organizational / functional / Human Resources / Retention (sK588, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New hire failure

- id: `kpi.human-resources.new-hire-failure`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.retention`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

New hire failure measures that result inside Human Resources, subcategory Retention. The unit is percent. The formula is (A / B) * 100, where A is part named by New hire failure, B is whole named by New hire failure. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New hire failure on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-new-hire-failure` (part named by New hire failure)
- `metric.whole-named-by-new-hire-failure` (whole named by New hire failure)

Placements:

- organizational / functional / Human Resources / Retention (sK52, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Turnover cost

- id: `kpi.human-resources.turnover-cost`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.retention`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Turnover cost measures that result inside Human Resources, subcategory Retention. The unit is count. The formula is A, where A is Turnover cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Turnover cost on the desired side of its target for this period?

Inputs:

- `metric.turnover-cost` (Turnover cost)

Placements:

- organizational / functional / Human Resources / Retention (sK91, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time to promotion

- id: `kpi.human-resources.time-to-promotion`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.retention`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Time to promotion measures that result inside Human Resources, subcategory Retention. The unit is count. The formula is A, where A is Time to promotion. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time to promotion on the desired side of its target for this period?

Inputs:

- `metric.time-to-promotion` (Time to promotion)

Placements:

- organizational / functional / Human Resources / Retention (sK244, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employee empowerment index

- id: `kpi.human-resources.employee-empowerment-index`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: index
- dashboard: `dash.human-resources.retention`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employee empowerment index measures that result inside Human Resources, subcategory Retention. The unit is count. The formula is (A / B) * 100, where A is current Employee empowerment index, B is base-period Employee empowerment index. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employee empowerment index on the desired side of its target for this period?

Inputs:

- `metric.current-employee-empowerment-index` (current Employee empowerment index)
- `metric.base-period-employee-empowerment-index` (base-period Employee empowerment index)

Placements:

- organizational / functional / Human Resources / Retention (sK1830, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employee termination value

- id: `kpi.human-resources.employee-termination-value`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.retention`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employee termination value measures that result inside Human Resources, subcategory Retention. The unit is count. The formula is A, where A is Employee termination value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employee termination value on the desired side of its target for this period?

Inputs:

- `metric.employee-termination-value` (Employee termination value)

Placements:

- organizational / functional / Human Resources / Retention (sK1831, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Voluntary termination cost

- id: `kpi.human-resources.voluntary-termination-cost`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.retention`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Voluntary termination cost measures that result inside Human Resources, subcategory Retention. The unit is count. The formula is A, where A is Voluntary termination cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Voluntary termination cost on the desired side of its target for this period?

Inputs:

- `metric.voluntary-termination-cost` (Voluntary termination cost)

Placements:

- organizational / functional / Human Resources / Retention (sK1833, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Termination value per full time equivalent (FTE)

- id: `kpi.human-resources.termination-value-per-full-time-equivalent-fte`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.retention`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Termination value per full time equivalent (FTE) measures that result inside Human Resources, subcategory Retention. The unit is count. The formula is A / B, where A is Termination value, B is full time equivalent (FTE). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Termination value per full time equivalent (FTE) on the desired side of its target for this period?

Inputs:

- `metric.termination-value` (Termination value)
- `metric.full-time-equivalent-fte` (full time equivalent (FTE))

Placements:

- organizational / functional / Human Resources / Retention (sK1833, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New employees turning over cost rate

- id: `kpi.human-resources.new-employees-turning-over-cost-rate`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.retention`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

New employees turning over cost rate measures that result inside Human Resources, subcategory Retention. The unit is percent. The formula is (A / B) * 100, where A is numerator of New employees turning over cost rate, B is base of New employees turning over cost rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New employees turning over cost rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-new-employees-turning-over-cost-rate` (numerator of New employees turning over cost rate)
- `metric.base-of-new-employees-turning-over-cost-rate` (base of New employees turning over cost rate)

Placements:

- organizational / functional / Human Resources / Retention (sK184, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employee commitment index

- id: `kpi.human-resources.employee-commitment-index`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: index
- dashboard: `dash.human-resources.retention`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employee commitment index measures that result inside Human Resources, subcategory Retention. The unit is count. The formula is (A / B) * 100, where A is current Employee commitment index, B is base-period Employee commitment index. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employee commitment index on the desired side of its target for this period?

Inputs:

- `metric.current-employee-commitment-index` (current Employee commitment index)
- `metric.base-period-employee-commitment-index` (base-period Employee commitment index)

Placements:

- organizational / functional / Human Resources / Retention (sK1835, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employee engagement index

- id: `kpi.human-resources.employee-engagement-index`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `(A / B) * 100`
- formula type: index
- dashboard: `dash.human-resources.retention`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employee engagement index measures that result inside Human Resources, subcategory Retention. The unit is count. The formula is (A / B) * 100, where A is current Employee engagement index, B is base-period Employee engagement index. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employee engagement index on the desired side of its target for this period?

Inputs:

- `metric.current-employee-engagement-index` (current Employee engagement index)
- `metric.base-period-employee-engagement-index` (base-period Employee engagement index)

Placements:

- organizational / functional / Human Resources / Retention (sK1836, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employee retention index

- id: `kpi.human-resources.employee-retention-index`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.retention`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employee retention index measures that result inside Human Resources, subcategory Retention. The unit is percent. The formula is (A / B) * 100, where A is part named by Employee retention index, B is whole named by Employee retention index. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employee retention index on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-employee-retention-index` (part named by Employee retention index)
- `metric.whole-named-by-employee-retention-index` (whole named by Employee retention index)

Placements:

- organizational / functional / Human Resources / Retention (sK1837, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Staffing rate less than 1 year tenure

- id: `kpi.human-resources.staffing-rate-less-than-1-year-tenure`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.retention`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Staffing rate less than 1 year tenure measures that result inside Human Resources, subcategory Retention. The unit is percent. The formula is (A / B) * 100, where A is numerator of Staffing rate less than 1 year tenure, B is base of Staffing rate less than 1 year tenure. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Staffing rate less than 1 year tenure on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-staffing-rate-less-than-1-year-tenure` (numerator of Staffing rate less than 1 year tenure)
- `metric.base-of-staffing-rate-less-than-1-year-tenure` (base of Staffing rate less than 1 year tenure)

Placements:

- organizational / functional / Human Resources / Retention (sK1841, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Voluntary termination rate

- id: `kpi.human-resources.voluntary-termination-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.retention`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Voluntary termination rate measures that result inside Human Resources, subcategory Retention. The unit is percent. The formula is (A / B) * 100, where A is numerator of Voluntary termination rate, B is base of Voluntary termination rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Voluntary termination rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-voluntary-termination-rate` (numerator of Voluntary termination rate)
- `metric.base-of-voluntary-termination-rate` (base of Voluntary termination rate)

Placements:

- organizational / functional / Human Resources / Retention (sK1842, page_0024)
- organizational / functional / Human Resources / Retention (sK1845, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Termination by performance rating

- id: `kpi.human-resources.termination-by-performance-rating`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.retention`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Termination by performance rating measures that result inside Human Resources, subcategory Retention. The unit is percent. The formula is (A / B) * 100, where A is part named by Termination by performance rating, B is whole named by Termination by performance rating. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Termination by performance rating on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-termination-by-performance-rating` (part named by Termination by performance rating)
- `metric.whole-named-by-termination-by-performance-rating` (whole named by Termination by performance rating)

Placements:

- organizational / functional / Human Resources / Retention (sK1843, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employment termination reason breakdown

- id: `kpi.human-resources.employment-termination-reason-breakdown`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.retention`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employment termination reason breakdown measures that result inside Human Resources, subcategory Retention. The unit is percent. The formula is (A / B) * 100, where A is part named by Employment termination reason breakdown, B is whole named by Employment termination reason breakdown. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employment termination reason breakdown on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-employment-termination-reason-breakdown` (part named by Employment termination reason breakdown)
- `metric.whole-named-by-employment-termination-reason-breakdown` (whole named by Employment termination reason breakdown)

Placements:

- organizational / functional / Human Resources / Retention (sK1844, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New hire turnover

- id: `kpi.human-resources.new-hire-turnover`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.retention`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

New hire turnover measures that result inside Human Resources, subcategory Retention. The unit is percent. The formula is (A / B) * 100, where A is part named by New hire turnover, B is whole named by New hire turnover. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New hire turnover on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-new-hire-turnover` (part named by New hire turnover)
- `metric.whole-named-by-new-hire-turnover` (whole named by New hire turnover)

Placements:

- organizational / functional / Human Resources / Retention (sK1846, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employee perceptions of external job opportunities index

- id: `kpi.human-resources.employee-perceptions-of-external-job-opportunities-index`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: index
- dashboard: `dash.human-resources.retention`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employee perceptions of external job opportunities index measures that result inside Human Resources, subcategory Retention. The unit is count. The formula is (A / B) * 100, where A is current Employee perceptions of external job opportunities index, B is base-period Employee perceptions of external job opportunities index. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employee perceptions of external job opportunities index on the desired side of its target for this period?

Inputs:

- `metric.current-employee-perceptions-of-external-job-opportunities-index` (current Employee perceptions of external job opportunities index)
- `metric.base-period-employee-perceptions-of-external-job-opportunities-index` (base-period Employee perceptions of external job opportunities index)

Placements:

- organizational / functional / Human Resources / Retention (sK1847, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Early retirements

- id: `kpi.human-resources.early-retirements`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.retention`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Early retirements measures that result inside Human Resources, subcategory Retention. The unit is percent. The formula is (A / B) * 100, where A is part named by Early retirements, B is whole named by Early retirements. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Early retirements on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-early-retirements` (part named by Early retirements)
- `metric.whole-named-by-early-retirements` (whole named by Early retirements)

Placements:

- organizational / functional / Human Resources / Retention (sK1849, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees taking ill health retirement

- id: `kpi.human-resources.employees-taking-ill-health-retirement`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.retention`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employees taking ill health retirement measures that result inside Human Resources, subcategory Retention. The unit is percent. The formula is (A / B) * 100, where A is part named by Employees taking ill health retirement, B is whole named by Employees taking ill health retirement. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees taking ill health retirement on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-employees-taking-ill-health-retirement` (part named by Employees taking ill health retirement)
- `metric.whole-named-by-employees-taking-ill-health-retirement` (whole named by Employees taking ill health retirement)

Placements:

- organizational / functional / Human Resources / Retention (sK1850, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Length of service of senior level staff

- id: `kpi.human-resources.length-of-service-of-senior-level-staff`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.retention`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Length of service of senior level staff measures that result inside Human Resources, subcategory Retention. The unit is count. The formula is A, where A is Length of service of senior level staff. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Length of service of senior level staff on the desired side of its target for this period?

Inputs:

- `metric.length-of-service-of-senior-level-staff` (Length of service of senior level staff)

Placements:

- organizational / functional / Human Resources / Retention (sK1852, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unplanned personnel losses

- id: `kpi.human-resources.unplanned-personnel-losses`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.retention`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Unplanned personnel losses measures that result inside Human Resources, subcategory Retention. The unit is count. The formula is A, where A is Unplanned personnel losses. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unplanned personnel losses on the desired side of its target for this period?

Inputs:

- `metric.unplanned-personnel-losses` (Unplanned personnel losses)

Placements:

- organizational / functional / Human Resources / Retention (sK2069, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Job subhandlement cost

- id: `kpi.human-resources.job-subhandlement-cost`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.retention`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Job subhandlement cost measures that result inside Human Resources, subcategory Retention. The unit is number. The formula is A, where A is Job subhandlement cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Job subhandlement cost on the desired side of its target for this period?

Inputs:

- `metric.job-subhandlement-cost` (Job subhandlement cost)

Placements:

- organizational / functional / Human Resources / Retention (sK3442, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unavoidable officer terminations

- id: `kpi.human-resources.unavoidable-officer-terminations`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.retention`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Unavoidable officer terminations measures that result inside Human Resources, subcategory Retention. The unit is percent. The formula is (A / B) * 100, where A is part named by Unavoidable officer terminations, B is whole named by Unavoidable officer terminations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unavoidable officer terminations on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-unavoidable-officer-terminations` (part named by Unavoidable officer terminations)
- `metric.whole-named-by-unavoidable-officer-terminations` (whole named by Unavoidable officer terminations)

Placements:

- organizational / functional / Human Resources / Retention (sK4033, page_0024)
- organizational / industries / Sport / Organizational » Industries (sK4033, page_0197)
- organizational / industries / Sport / Organizational » Industries (sK19122, page_0198)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employee satisfaction

- id: `kpi.human-resources.employee-satisfaction`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.retention`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employee satisfaction measures that result inside Human Resources, subcategory Retention. The unit is percent. The formula is (A / B) * 100, where A is part named by Employee satisfaction, B is whole named by Employee satisfaction. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employee satisfaction on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-employee-satisfaction` (part named by Employee satisfaction)
- `metric.whole-named-by-employee-satisfaction` (whole named by Employee satisfaction)

Placements:

- organizational / functional / Human Resources / Retention (sK5912, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Management lost

- id: `kpi.human-resources.management-lost`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.retention`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Management lost measures that result inside Human Resources, subcategory Retention. The unit is count. The formula is A, where A is Management lost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Management lost on the desired side of its target for this period?

Inputs:

- `metric.management-lost` (Management lost)

Placements:

- organizational / functional / Human Resources / Retention (sK1944, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Workers retaining employment after relocation

- id: `kpi.human-resources.workers-retaining-employment-after-relocation`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.retention`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Workers retaining employment after relocation measures that result inside Human Resources, subcategory Retention. The unit is count. The formula is A, where A is Workers retaining employment after relocation. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Workers retaining employment after relocation on the desired side of its target for this period?

Inputs:

- `metric.workers-retaining-employment-after-relocation` (Workers retaining employment after relocation)

Placements:

- organizational / functional / Human Resources / Retention (sK2266, page_0024)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
