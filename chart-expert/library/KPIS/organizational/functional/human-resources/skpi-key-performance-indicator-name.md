# Human Resources / sKPI # Key Performance Indicator name

Context: organizational. Group: functional. KPIs: 13.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Overtime hours per employee

- id: `kpi.human-resources.overtime-hours-per-employee`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.skpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Overtime hours per employee measures that result inside Human Resources, subcategory sKPI # Key Performance Indicator name. The unit is count. The formula is A / B, where A is Overtime hours, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Overtime hours per employee on the desired side of its target for this period?

Inputs:

- `metric.overtime-hours` (Overtime hours)
- `metric.employee` (employee)

Placements:

- organizational / functional / Human Resources / sKPI # Key Performance Indicator name (sK47, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sickness absence days per full time equivalent (FTE) employee

- id: `kpi.human-resources.sickness-absence-days-per-full-time-equivalent-fte-employee`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.skpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Sickness absence days per full time equivalent (FTE) employee measures that result inside Human Resources, subcategory sKPI # Key Performance Indicator name. The unit is count. The formula is A / B, where A is Sickness absence days, B is full time equivalent (FTE) employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sickness absence days per full time equivalent (FTE) employee on the desired side of its target for this period?

Inputs:

- `metric.sickness-absence-days` (Sickness absence days)
- `metric.full-time-equivalent-fte-employee` (full time equivalent (FTE) employee)

Placements:

- organizational / functional / Human Resources / sKPI # Key Performance Indicator name (sK48, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Long time due to accidents per 100,000 hours worked

- id: `kpi.human-resources.long-time-due-to-accidents-per-100-000-hours-worked`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.skpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Long time due to accidents per 100,000 hours worked measures that result inside Human Resources, subcategory sKPI # Key Performance Indicator name. The unit is count. The formula is A / B, where A is Long time due to accidents, B is 100,000 hours worked. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Long time due to accidents per 100,000 hours worked on the desired side of its target for this period?

Inputs:

- `metric.long-time-due-to-accidents` (Long time due to accidents)
- `metric.100-000-hours-worked` (100,000 hours worked)

Placements:

- organizational / functional / Human Resources / sKPI # Key Performance Indicator name (sK87, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Accidental or Pay 100,000 hours worked

- id: `kpi.human-resources.accidental-or-pay-100-000-hours-worked`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.skpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Accidental or Pay 100,000 hours worked measures that result inside Human Resources, subcategory sKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Accidental or Pay 100,000 hours worked. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Accidental or Pay 100,000 hours worked on the desired side of its target for this period?

Inputs:

- `metric.accidental-or-pay-100-000-hours-worked` (Accidental or Pay 100,000 hours worked)

Placements:

- organizational / functional / Human Resources / sKPI # Key Performance Indicator name (sK88, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Harassment and discrimination complaints received

- id: `kpi.human-resources.harassment-and-discrimination-complaints-received`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.skpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Harassment and discrimination complaints received measures that result inside Human Resources, subcategory sKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Harassment and discrimination complaints received. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Harassment and discrimination complaints received on the desired side of its target for this period?

Inputs:

- `metric.harassment-and-discrimination-complaints-received` (Harassment and discrimination complaints received)

Placements:

- organizational / functional / Human Resources / sKPI # Key Performance Indicator name (sK54, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Paid time off

- id: `kpi.human-resources.paid-time-off`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.skpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Paid time off measures that result inside Human Resources, subcategory sKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Paid time off. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Paid time off on the desired side of its target for this period?

Inputs:

- `metric.paid-time-off` (Paid time off)

Placements:

- organizational / functional / Human Resources / sKPI # Key Performance Indicator name (sK686, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Misradiation, luring, bullying or retaliation campaign received

- id: `kpi.human-resources.misradiation-luring-bullying-or-retaliation-campaign-received`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.skpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Misradiation, luring, bullying or retaliation campaign received measures that result inside Human Resources, subcategory sKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Misradiation, luring, bullying or retaliation campaign received. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Misradiation, luring, bullying or retaliation campaign received on the desired side of its target for this period?

Inputs:

- `metric.misradiation-luring-bullying-or-retaliation-campaign-received` (Misradiation, luring, bullying or retaliation campaign received)

Placements:

- organizational / functional / Human Resources / sKPI # Key Performance Indicator name (sK687, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Total accidents

- id: `kpi.human-resources.total-accidents`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.skpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Total accidents measures that result inside Human Resources, subcategory sKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Total accidents. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Total accidents on the desired side of its target for this period?

Inputs:

- `metric.total-accidents` (Total accidents)

Placements:

- organizational / functional / Human Resources / sKPI # Key Performance Indicator name (sK94, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Health and safety prevention costs

- id: `kpi.human-resources.health-and-safety-prevention-costs`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.skpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Health and safety prevention costs measures that result inside Human Resources, subcategory sKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Health and safety prevention costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Health and safety prevention costs on the desired side of its target for this period?

Inputs:

- `metric.health-and-safety-prevention-costs` (Health and safety prevention costs)

Placements:

- organizational / functional / Human Resources / sKPI # Key Performance Indicator name (sK95, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hours lost due to absenteeism

- id: `kpi.human-resources.hours-lost-due-to-absenteeism`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.skpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Hours lost due to absenteeism measures that result inside Human Resources, subcategory sKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Hours lost due to absenteeism. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hours lost due to absenteeism on the desired side of its target for this period?

Inputs:

- `metric.hours-lost-due-to-absenteeism` (Hours lost due to absenteeism)

Placements:

- organizational / functional / Human Resources / sKPI # Key Performance Indicator name (sK720, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Lost time due to strike action

- id: `kpi.human-resources.lost-time-due-to-strike-action`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.skpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Lost time due to strike action measures that result inside Human Resources, subcategory sKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is Lost time due, B is strike action. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Lost time due to strike action on the desired side of its target for this period?

Inputs:

- `metric.lost-time-due` (Lost time due)
- `metric.strike-action` (strike action)

Placements:

- organizational / functional / Human Resources / sKPI # Key Performance Indicator name (sK721, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees with working home agreements

- id: `kpi.human-resources.employees-with-working-home-agreements`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.skpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employees with working home agreements measures that result inside Human Resources, subcategory sKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Employees with working home agreements, B is whole named by Employees with working home agreements. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees with working home agreements on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-employees-with-working-home-agreements` (part named by Employees with working home agreements)
- `metric.whole-named-by-employees-with-working-home-agreements` (whole named by Employees with working home agreements)

Placements:

- organizational / functional / Human Resources / sKPI # Key Performance Indicator name (sK732, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Job sharing agreements

- id: `kpi.human-resources.job-sharing-agreements`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.skpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Job sharing agreements measures that result inside Human Resources, subcategory sKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Job sharing agreements, B is whole named by Job sharing agreements. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Job sharing agreements on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-job-sharing-agreements` (part named by Job sharing agreements)
- `metric.whole-named-by-job-sharing-agreements` (whole named by Job sharing agreements)

Placements:

- organizational / functional / Human Resources / sKPI # Key Performance Indicator name (sK733, page_0026)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
