# Management / xKPI # Key Performance Indicator name

Context: organizational. Group: functional. KPIs: 103.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Timely production of management reports

- id: `kpi.management.timely-production-of-management-reports`
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

Timely production of management reports measures that result inside Management, subcategory Organizational > Functional Areas. The unit is percent. The formula is (A / B) * 100, where A is Timely production, B is management reports. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Timely production of management reports on the desired side of its target for this period?

Inputs:

- `metric.timely-production` (Timely production)
- `metric.management-reports` (management reports)

Placements:

- organizational / functional / Management / Organizational > Functional Areas (sK3558, page_0034)
- organizational / functional / Management / xKPI # Key Performance Indicator name (xK3358, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Project budget variance

- id: `kpi.management.project-budget-variance`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `A - B`
- formula type: difference
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Project budget variance measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is A - B, where A is actual Project budget variance, B is reference Project budget variance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Project budget variance on the desired side of its target for this period?

Inputs:

- `metric.actual-project-budget-variance` (actual Project budget variance)
- `metric.reference-project-budget-variance` (reference Project budget variance)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK27, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Conflicts arising during the project

- id: `kpi.management.conflicts-arising-during-the-project`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Conflicts arising during the project measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Conflicts arising during the project. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Conflicts arising during the project on the desired side of its target for this period?

Inputs:

- `metric.conflicts-arising-during-the-project` (Conflicts arising during the project)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK28, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Project issues addressed ratio

- id: `kpi.management.project-issues-addressed-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Project issues addressed ratio measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Project issues addressed ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Project issues addressed ratio on the desired side of its target for this period?

Inputs:

- `metric.project-issues-addressed-ratio` (Project issues addressed ratio)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK29, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Project or program budget spent on training

- id: `kpi.management.project-or-program-budget-spent-on-training`
- kind: kpi
- unit: percent
- direction: up
- timing: leading
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Project or program budget spent on training measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Project or program budget spent on training, B is whole named by Project or program budget spent on training. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Project or program budget spent on training on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-project-or-program-budget-spent-on-training` (part named by Project or program budget spent on training)
- `metric.whole-named-by-project-or-program-budget-spent-on-training` (whole named by Project or program budget spent on training)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK54, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Overdue project tasks

- id: `kpi.management.overdue-project-tasks`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Overdue project tasks measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Overdue project tasks, B is whole named by Overdue project tasks. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Overdue project tasks on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-overdue-project-tasks` (part named by Overdue project tasks)
- `metric.whole-named-by-overdue-project-tasks` (whole named by Overdue project tasks)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK159, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Funnel man-hours

- id: `kpi.management.funnel-man-hours`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Funnel man-hours measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Funnel man-hours. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Funnel man-hours on the desired side of its target for this period?

Inputs:

- `metric.funnel-man-hours` (Funnel man-hours)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK347, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time per project task

- id: `kpi.management.time-per-project-task`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time per project task measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A / B, where A is Time, B is project task. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time per project task on the desired side of its target for this period?

Inputs:

- `metric.time` (Time)
- `metric.project-task` (project task)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK10, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time spent as planned

- id: `kpi.management.time-spent-as-planned`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time spent as planned measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Time spent as planned, B is whole named by Time spent as planned. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time spent as planned on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-time-spent-as-planned` (part named by Time spent as planned)
- `metric.whole-named-by-time-spent-as-planned` (whole named by Time spent as planned)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK11, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Progress reports submitted as planned

- id: `kpi.management.progress-reports-submitted-as-planned`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Progress reports submitted as planned measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Progress reports submitted as planned, B is whole named by Progress reports submitted as planned. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Progress reports submitted as planned on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-progress-reports-submitted-as-planned` (part named by Progress reports submitted as planned)
- `metric.whole-named-by-progress-reports-submitted-as-planned` (whole named by Progress reports submitted as planned)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK178, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Elimination at completion (EAC)

- id: `kpi.management.elimination-at-completion-eac`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Elimination at completion (EAC) measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Elimination at completion (EAC). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Elimination at completion (EAC) on the desired side of its target for this period?

Inputs:

- `metric.elimination-at-completion-eac` (Elimination at completion (EAC))

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK83, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Estimate to complete

- id: `kpi.management.estimate-to-complete`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Estimate to complete measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Estimate to complete. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Estimate to complete on the desired side of its target for this period?

Inputs:

- `metric.estimate-to-complete` (Estimate to complete)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK84, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost performance index (CPI)

- id: `kpi.management.cost-performance-index-cpi`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: index
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost performance index (CPI) measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is (A / B) * 100, where A is current Cost performance index (CPI), B is base-period Cost performance index (CPI). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost performance index (CPI) on the desired side of its target for this period?

Inputs:

- `metric.current-cost-performance-index-cpi` (current Cost performance index (CPI))
- `metric.base-period-cost-performance-index-cpi` (base-period Cost performance index (CPI))

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK85, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Schedule performance index (SPI)

- id: `kpi.management.schedule-performance-index-spi`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: index
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Schedule performance index (SPI) measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is (A / B) * 100, where A is current Schedule performance index (SPI), B is base-period Schedule performance index (SPI). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Schedule performance index (SPI) on the desired side of its target for this period?

Inputs:

- `metric.current-schedule-performance-index-spi` (current Schedule performance index (SPI))
- `metric.base-period-schedule-performance-index-spi` (base-period Schedule performance index (SPI))

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK86, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost schedule index (CSI)

- id: `kpi.management.cost-schedule-index-csi`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: index
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost schedule index (CSI) measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is (A / B) * 100, where A is current Cost schedule index (CSI), B is base-period Cost schedule index (CSI). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost schedule index (CSI) on the desired side of its target for this period?

Inputs:

- `metric.current-cost-schedule-index-csi` (current Cost schedule index (CSI))
- `metric.base-period-cost-schedule-index-csi` (base-period Cost schedule index (CSI))

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK87, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Project schedule variance

- id: `kpi.management.project-schedule-variance`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `A - B`
- formula type: difference
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Project schedule variance measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is A - B, where A is actual Project schedule variance, B is reference Project schedule variance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Project schedule variance on the desired side of its target for this period?

Inputs:

- `metric.actual-project-schedule-variance` (actual Project schedule variance)
- `metric.reference-project-schedule-variance` (reference Project schedule variance)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK88, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### To complete schedule performance index (TSP)

- id: `kpi.management.to-complete-schedule-performance-index-tsp`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: index
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

To complete schedule performance index (TSP) measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is (A / B) * 100, where A is current To complete schedule performance index (TSP), B is base-period To complete schedule performance index (TSP). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is To complete schedule performance index (TSP) on the desired side of its target for this period?

Inputs:

- `metric.current-to-complete-schedule-performance-index-tsp` (current To complete schedule performance index (TSP))
- `metric.base-period-to-complete-schedule-performance-index-tsp` (base-period To complete schedule performance index (TSP))

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK89, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost variance

- id: `kpi.management.cost-variance`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A - B`
- formula type: difference
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost variance measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A - B, where A is actual Cost variance, B is reference Cost variance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost variance on the desired side of its target for this period?

Inputs:

- `metric.actual-cost-variance` (actual Cost variance)
- `metric.reference-cost-variance` (reference Cost variance)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK92, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### To complete performance index (TCPI)

- id: `kpi.management.to-complete-performance-index-tcpi`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: index
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

To complete performance index (TCPI) measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is (A / B) * 100, where A is current To complete performance index (TCPI), B is base-period To complete performance index (TCPI). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is To complete performance index (TCPI) on the desired side of its target for this period?

Inputs:

- `metric.current-to-complete-performance-index-tcpi` (current To complete performance index (TCPI))
- `metric.base-period-to-complete-performance-index-tcpi` (base-period To complete performance index (TCPI))

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK93, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Proposed changes without impact analysis

- id: `kpi.management.proposed-changes-without-impact-analysis`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Proposed changes without impact analysis measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Proposed changes without impact analysis, B is whole named by Proposed changes without impact analysis. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Proposed changes without impact analysis on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-proposed-changes-without-impact-analysis` (part named by Proposed changes without impact analysis)
- `metric.whole-named-by-proposed-changes-without-impact-analysis` (whole named by Proposed changes without impact analysis)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK1049, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Stakeholder satisfaction with the accuracy of the project feasibility study

- id: `kpi.management.stakeholder-satisfaction-with-the-accuracy-of-the-project-feasibility-st`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Stakeholder satisfaction with the accuracy of the project feasibility study measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is Stakeholder satisfaction with the accuracy, B is the project feasibility study. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Stakeholder satisfaction with the accuracy of the project feasibility study on the desired side of its target for this period?

Inputs:

- `metric.stakeholder-satisfaction-with-the-accuracy` (Stakeholder satisfaction with the accuracy)
- `metric.the-project-feasibility-study` (the project feasibility study)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK1236, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Requirements changed during project execution

- id: `kpi.management.requirements-changed-during-project-execution`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Requirements changed during project execution measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Requirements changed during project execution, B is whole named by Requirements changed during project execution. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Requirements changed during project execution on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-requirements-changed-during-project-execution` (part named by Requirements changed during project execution)
- `metric.whole-named-by-requirements-changed-during-project-execution` (whole named by Requirements changed during project execution)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2070, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Project issues identified

- id: `kpi.management.project-issues-identified`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Project issues identified measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Project issues identified. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Project issues identified on the desired side of its target for this period?

Inputs:

- `metric.project-issues-identified` (Project issues identified)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2623, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Project resource utilization

- id: `kpi.management.project-resource-utilization`
- kind: kpi
- unit: percent
- direction: corridor
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Project resource utilization measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Project resource utilization, B is whole named by Project resource utilization. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Project resource utilization on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-project-resource-utilization` (part named by Project resource utilization)
- `metric.whole-named-by-project-resource-utilization` (whole named by Project resource utilization)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2624, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Conflicts positively resolved during the project

- id: `kpi.management.conflicts-positively-resolved-during-the-project`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Conflicts positively resolved during the project measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Conflicts positively resolved during the project, B is whole named by Conflicts positively resolved during the project. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Conflicts positively resolved during the project on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-conflicts-positively-resolved-during-the-project` (part named by Conflicts positively resolved during the project)
- `metric.whole-named-by-conflicts-positively-resolved-during-the-project` (whole named by Conflicts positively resolved during the project)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2633, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Actual cost of work performed (ACWP)

- id: `kpi.management.actual-cost-of-work-performed-acwp`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Actual cost of work performed (ACWP) measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Actual cost of work performed (ACWP). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Actual cost of work performed (ACWP) on the desired side of its target for this period?

Inputs:

- `metric.actual-cost-of-work-performed-acwp` (Actual cost of work performed (ACWP))

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2644, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Budgeted cost of work performed (BCWP)

- id: `kpi.management.budgeted-cost-of-work-performed-bcwp`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Budgeted cost of work performed (BCWP) measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is Budgeted cost, B is work performed (BCWP). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Budgeted cost of work performed (BCWP) on the desired side of its target for this period?

Inputs:

- `metric.budgeted-cost` (Budgeted cost)
- `metric.work-performed-bcwp` (work performed (BCWP))

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2645, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Budgeted cost of work scheduled (BCWPS)

- id: `kpi.management.budgeted-cost-of-work-scheduled-bcwps`
- kind: kpi
- unit: percent
- direction: down
- timing: leading
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Budgeted cost of work scheduled (BCWPS) measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is Budgeted cost, B is work scheduled (BCWPS). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Budgeted cost of work scheduled (BCWPS) on the desired side of its target for this period?

Inputs:

- `metric.budgeted-cost` (Budgeted cost)
- `metric.work-scheduled-bcwps` (work scheduled (BCWPS))

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2646, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of rectifying major defects before project completion

- id: `kpi.management.cost-of-rectifying-major-defects-before-project-completion`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of rectifying major defects before project completion measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is Cost, B is rectifying major defects before project completion. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of rectifying major defects before project completion on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.rectifying-major-defects-before-project-completion` (rectifying major defects before project completion)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2651, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Partnering development cost of project

- id: `kpi.management.partnering-development-cost-of-project`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Partnering development cost of project measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is Partnering development cost, B is project. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Partnering development cost of project on the desired side of its target for this period?

Inputs:

- `metric.partnering-development-cost` (Partnering development cost)
- `metric.project` (project)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2663, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Project cost savings from innovation

- id: `kpi.management.project-cost-savings-from-innovation`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Project cost savings from innovation measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is Project cost savings, B is innovation. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Project cost savings from innovation on the desired side of its target for this period?

Inputs:

- `metric.project-cost-savings` (Project cost savings)
- `metric.innovation` (innovation)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2654, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Project maintenance missed

- id: `kpi.management.project-maintenance-missed`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Project maintenance missed measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Project maintenance missed, B is whole named by Project maintenance missed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Project maintenance missed on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-project-maintenance-missed` (part named by Project maintenance missed)
- `metric.whole-named-by-project-maintenance-missed` (whole named by Project maintenance missed)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2661, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Third party non-consistently identified during inspections

- id: `kpi.management.third-party-non-consistently-identified-during-inspections`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Third party non-consistently identified during inspections measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Third party non-consistently identified during inspections. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Third party non-consistently identified during inspections on the desired side of its target for this period?

Inputs:

- `metric.third-party-non-consistently-identified-during-inspections` (Third party non-consistently identified during inspections)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2662, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unique project requirements

- id: `kpi.management.unique-project-requirements`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Unique project requirements measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Unique project requirements. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unique project requirements on the desired side of its target for this period?

Inputs:

- `metric.unique-project-requirements` (Unique project requirements)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2671, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Initiatives for improvement of the project introduced

- id: `kpi.management.initiatives-for-improvement-of-the-project-introduced`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Initiatives for improvement of the project introduced measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Initiatives for improvement of the project introduced. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Initiatives for improvement of the project introduced on the desired side of its target for this period?

Inputs:

- `metric.initiatives-for-improvement-of-the-project-introduced` (Initiatives for improvement of the project introduced)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2692, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Overdue project status reports

- id: `kpi.management.overdue-project-status-reports`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Overdue project status reports measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Overdue project status reports, B is whole named by Overdue project status reports. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Overdue project status reports on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-overdue-project-status-reports` (part named by Overdue project status reports)
- `metric.whole-named-by-overdue-project-status-reports` (whole named by Overdue project status reports)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2695, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Progress reports submitted

- id: `kpi.management.progress-reports-submitted`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Progress reports submitted measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Progress reports submitted, B is whole named by Progress reports submitted. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Progress reports submitted on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-progress-reports-submitted` (part named by Progress reports submitted)
- `metric.whole-named-by-progress-reports-submitted` (whole named by Progress reports submitted)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2696, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Poon compliance requests generated per month

- id: `kpi.management.poon-compliance-requests-generated-per-month`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Poon compliance requests generated per month measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A / B, where A is Poon compliance requests generated, B is month. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Poon compliance requests generated per month on the desired side of its target for this period?

Inputs:

- `metric.poon-compliance-requests-generated` (Poon compliance requests generated)
- `metric.month` (month)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2704, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Project delay

- id: `kpi.management.project-delay`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Project delay measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Project delay. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Project delay on the desired side of its target for this period?

Inputs:

- `metric.project-delay` (Project delay)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2718, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Project completion

- id: `kpi.management.project-completion`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Project completion measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Project completion, B is whole named by Project completion. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Project completion on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-project-completion` (part named by Project completion)
- `metric.whole-named-by-project-completion` (whole named by Project completion)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2718, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Requirements for accessibility

- id: `kpi.management.requirements-for-accessibility`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Requirements for accessibility measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Requirements for accessibility, B is whole named by Requirements for accessibility. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Requirements for accessibility on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-requirements-for-accessibility` (part named by Requirements for accessibility)
- `metric.whole-named-by-requirements-for-accessibility` (whole named by Requirements for accessibility)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK4684, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Man-hours per occurrence spent locating problems

- id: `kpi.management.man-hours-per-occurrence-spent-locating-problems`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Man-hours per occurrence spent locating problems measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A / B, where A is Man-hours, B is occurrence spent locating problems. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Man-hours per occurrence spent locating problems on the desired side of its target for this period?

Inputs:

- `metric.man-hours` (Man-hours)
- `metric.occurrence-spent-locating-problems` (occurrence spent locating problems)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK5901, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Critical path activities

- id: `kpi.management.critical-path-activities`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Critical path activities measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Critical path activities, B is whole named by Critical path activities. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Critical path activities on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-critical-path-activities` (part named by Critical path activities)
- `metric.whole-named-by-critical-path-activities` (whole named by Critical path activities)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK6023, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Project cost contingency

- id: `kpi.management.project-cost-contingency`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Project cost contingency measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Project cost contingency, B is whole named by Project cost contingency. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Project cost contingency on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-project-cost-contingency` (part named by Project cost contingency)
- `metric.whole-named-by-project-cost-contingency` (whole named by Project cost contingency)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK6257, page_0046)
- organizational / industries / Construction / General (sS6527, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Delivery deadline met

- id: `kpi.management.delivery-deadline-met`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Delivery deadline met measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Delivery deadline met, B is whole named by Delivery deadline met. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Delivery deadline met on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-delivery-deadline-met` (part named by Delivery deadline met)
- `metric.whole-named-by-delivery-deadline-met` (whole named by Delivery deadline met)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK6355, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Inactive projects

- id: `kpi.management.inactive-projects`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Inactive projects measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Inactive projects. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Inactive projects on the desired side of its target for this period?

Inputs:

- `metric.inactive-projects` (Inactive projects)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK6616, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Requests for time extension submitted

- id: `kpi.management.requests-for-time-extension-submitted`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Requests for time extension submitted measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Requests for time extension submitted. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Requests for time extension submitted on the desired side of its target for this period?

Inputs:

- `metric.requests-for-time-extension-submitted` (Requests for time extension submitted)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK6758, page_0046)
- organizational / industries / Construction / Organizational » Industries (s80758, page_0068)
- organizational / industries / Construction / General (sS6758, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Order value variance from original contract value

- id: `kpi.management.order-value-variance-from-original-contract-value`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Order value variance from original contract value measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is Order value variance, B is original contract value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Order value variance from original contract value on the desired side of its target for this period?

Inputs:

- `metric.order-value-variance` (Order value variance)
- `metric.original-contract-value` (original contract value)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK6855, page_0046)
- organizational / functional / Management / xKPI # Key Performance Indicator name (xK6865, page_0053)
- organizational / industries / Construction / General (sS6865, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Planned projects that have started

- id: `kpi.management.planned-projects-that-have-started`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Planned projects that have started measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Planned projects that have started, B is whole named by Planned projects that have started. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Planned projects that have started on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-planned-projects-that-have-started` (part named by Planned projects that have started)
- `metric.whole-named-by-planned-projects-that-have-started` (whole named by Planned projects that have started)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK7052, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Completed projects reviewed

- id: `kpi.management.completed-projects-reviewed`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Completed projects reviewed measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Completed projects reviewed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Completed projects reviewed on the desired side of its target for this period?

Inputs:

- `metric.completed-projects-reviewed` (Completed projects reviewed)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK1049, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cycle time to done projects

- id: `kpi.management.cycle-time-to-done-projects`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cycle time to done projects measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Cycle time to done projects. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cycle time to done projects on the desired side of its target for this period?

Inputs:

- `metric.cycle-time-to-done-projects` (Cycle time to done projects)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK10471, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Goals achieved versus goals set

- id: `kpi.management.goals-achieved-versus-goals-set`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `scatter-plot` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Goals achieved versus goals set measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is (A / B) * 100, where A is Goals achieved, B is goals set. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Goals achieved versus goals set on the desired side of its target for this period?

Inputs:

- `metric.goals-achieved` (Goals achieved)
- `metric.goals-set` (goals set)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK1148, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Infrastructure projects facilitated

- id: `kpi.management.infrastructure-projects-facilitated`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Infrastructure projects facilitated measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Infrastructure projects facilitated. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Infrastructure projects facilitated on the desired side of its target for this period?

Inputs:

- `metric.infrastructure-projects-facilitated` (Infrastructure projects facilitated)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK1203, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Infrastructure projects facilitated within an agreed time frame

- id: `kpi.management.infrastructure-projects-facilitated-within-an-agreed-time-frame`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Infrastructure projects facilitated within an agreed time frame measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Infrastructure projects facilitated within an agreed time frame. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Infrastructure projects facilitated within an agreed time frame on the desired side of its target for this period?

Inputs:

- `metric.infrastructure-projects-facilitated-within-an-agreed-time-frame` (Infrastructure projects facilitated within an agreed time frame)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK1204, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### # Office projects roll-up

- id: `kpi.management.office-projects-roll-up`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

# Office projects roll-up measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is # Office projects roll-up. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is # Office projects roll-up on the desired side of its target for this period?

Inputs:

- `metric.office-projects-roll-up` (# Office projects roll-up)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK1248, page_0046)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract variations

- id: `kpi.management.contract-variations`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract variations measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Contract variations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract variations on the desired side of its target for this period?

Inputs:

- `metric.contract-variations` (Contract variations)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK145, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Reclamation rate of active contracts

- id: `kpi.management.reclamation-rate-of-active-contracts`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Reclamation rate of active contracts measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Reclamation rate of active contracts. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Reclamation rate of active contracts on the desired side of its target for this period?

Inputs:

- `metric.reclamation-rate-of-active-contracts` (Reclamation rate of active contracts)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK146, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract value

- id: `kpi.management.contract-value`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract value measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Contract value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract value on the desired side of its target for this period?

Inputs:

- `metric.contract-value` (Contract value)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK147, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Value of activated contract renewals

- id: `kpi.management.value-of-activated-contract-renewals`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Value of activated contract renewals measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Value of activated contract renewals. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Value of activated contract renewals on the desired side of its target for this period?

Inputs:

- `metric.value-of-activated-contract-renewals` (Value of activated contract renewals)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK149, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract terms and related whole value with contractors

- id: `kpi.management.contract-terms-and-related-whole-value-with-contractors`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract terms and related whole value with contractors measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Contract terms and related whole value with contractors. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract terms and related whole value with contractors on the desired side of its target for this period?

Inputs:

- `metric.contract-terms-and-related-whole-value-with-contractors` (Contract terms and related whole value with contractors)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK150, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Identification contract breaches

- id: `kpi.management.identification-contract-breaches`
- kind: kri
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Identification contract breaches measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Identification contract breaches. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Identification contract breaches on the desired side of its target for this period?

Inputs:

- `metric.identification-contract-breaches` (Identification contract breaches)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK151, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cancelled and suspended contracts

- id: `kpi.management.cancelled-and-suspended-contracts`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cancelled and suspended contracts measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Cancelled and suspended contracts. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cancelled and suspended contracts on the desired side of its target for this period?

Inputs:

- `metric.cancelled-and-suspended-contracts` (Cancelled and suspended contracts)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK152, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract compliance

- id: `kpi.management.contract-compliance`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract compliance measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Contract compliance, B is whole named by Contract compliance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract compliance on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-contract-compliance` (part named by Contract compliance)
- `metric.whole-named-by-contract-compliance` (whole named by Contract compliance)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK261, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract reviewed

- id: `kpi.management.contract-reviewed`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract reviewed measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Contract reviewed, B is whole named by Contract reviewed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract reviewed on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-contract-reviewed` (part named by Contract reviewed)
- `metric.whole-named-by-contract-reviewed` (whole named by Contract reviewed)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK294, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contracts delivered within original budget

- id: `kpi.management.contracts-delivered-within-original-budget`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contracts delivered within original budget measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Contracts delivered within original budget, B is whole named by Contracts delivered within original budget. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contracts delivered within original budget on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-contracts-delivered-within-original-budget` (part named by Contracts delivered within original budget)
- `metric.whole-named-by-contracts-delivered-within-original-budget` (whole named by Contracts delivered within original budget)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK295, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract complaints

- id: `kpi.management.contract-complaints`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract complaints measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Contract complaints. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract complaints on the desired side of its target for this period?

Inputs:

- `metric.contract-complaints` (Contract complaints)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK296, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Termination contract remaining value

- id: `kpi.management.termination-contract-remaining-value`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Termination contract remaining value measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Termination contract remaining value, B is whole named by Termination contract remaining value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Termination contract remaining value on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-termination-contract-remaining-value` (part named by Termination contract remaining value)
- `metric.whole-named-by-termination-contract-remaining-value` (whole named by Termination contract remaining value)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK701, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Claims recovery rate

- id: `kpi.management.claims-recovery-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Claims recovery rate measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is numerator of Claims recovery rate, B is base of Claims recovery rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Claims recovery rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-claims-recovery-rate` (numerator of Claims recovery rate)
- `metric.base-of-claims-recovery-rate` (base of Claims recovery rate)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK908, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Transaction cost with new service providers

- id: `kpi.management.transaction-cost-with-new-service-providers`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Transaction cost with new service providers measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Transaction cost with new service providers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Transaction cost with new service providers on the desired side of its target for this period?

Inputs:

- `metric.transaction-cost-with-new-service-providers` (Transaction cost with new service providers)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK1095, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contracts awarded through competitive tendering process

- id: `kpi.management.contracts-awarded-through-competitive-tendering-process`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contracts awarded through competitive tendering process measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Contracts awarded through competitive tendering process, B is whole named by Contracts awarded through competitive tendering process. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contracts awarded through competitive tendering process on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-contracts-awarded-through-competitive-tendering-process` (part named by Contracts awarded through competitive tendering process)
- `metric.whole-named-by-contracts-awarded-through-competitive-tendering-process` (whole named by Contracts awarded through competitive tendering process)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2788, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contracts due to expire in the next X days

- id: `kpi.management.contracts-due-to-expire-in-the-next-x-days`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contracts due to expire in the next X days measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is Contracts due, B is expire in the next X days. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contracts due to expire in the next X days on the desired side of its target for this period?

Inputs:

- `metric.contracts-due` (Contracts due)
- `metric.expire-in-the-next-x-days` (expire in the next X days)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2917, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract expired value

- id: `kpi.management.contract-expired-value`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract expired value measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Contract expired value, B is whole named by Contract expired value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract expired value on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-contract-expired-value` (part named by Contract expired value)
- `metric.whole-named-by-contract-expired-value` (whole named by Contract expired value)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2918, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract renewals

- id: `kpi.management.contract-renewals`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract renewals measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Contract renewals. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract renewals on the desired side of its target for this period?

Inputs:

- `metric.contract-renewals` (Contract renewals)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2920, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract renewals growth rate

- id: `kpi.management.contract-renewals-growth-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract renewals growth rate measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is numerator of Contract renewals growth rate, B is base of Contract renewals growth rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract renewals growth rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-contract-renewals-growth-rate` (numerator of Contract renewals growth rate)
- `metric.base-of-contract-renewals-growth-rate` (base of Contract renewals growth rate)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2921, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract renewals value upfiting

- id: `kpi.management.contract-renewals-value-upfiting`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract renewals value upfiting measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Contract renewals value upfiting, B is whole named by Contract renewals value upfiting. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract renewals value upfiting on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-contract-renewals-value-upfiting` (part named by Contract renewals value upfiting)
- `metric.whole-named-by-contract-renewals-value-upfiting` (whole named by Contract renewals value upfiting)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2922, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Changes to contract specifications

- id: `kpi.management.changes-to-contract-specifications`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Changes to contract specifications measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is Changes, B is contract specifications. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Changes to contract specifications on the desired side of its target for this period?

Inputs:

- `metric.changes` (Changes)
- `metric.contract-specifications` (contract specifications)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2923, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contracts up for renewal

- id: `kpi.management.contracts-up-for-renewal`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contracts up for renewal measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Contracts up for renewal. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contracts up for renewal on the desired side of its target for this period?

Inputs:

- `metric.contracts-up-for-renewal` (Contracts up for renewal)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2924, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract value per client

- id: `kpi.management.contract-value-per-client`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract value per client measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A / B, where A is Contract value, B is client. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract value per client on the desired side of its target for this period?

Inputs:

- `metric.contract-value` (Contract value)
- `metric.client` (client)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2925, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contractual contract value

- id: `kpi.management.contractual-contract-value`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contractual contract value measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Contractual contract value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contractual contract value on the desired side of its target for this period?

Inputs:

- `metric.contractual-contract-value` (Contractual contract value)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2928, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Annual contracts value

- id: `kpi.management.annual-contracts-value`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Annual contracts value measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Annual contracts value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Annual contracts value on the desired side of its target for this period?

Inputs:

- `metric.annual-contracts-value` (Annual contracts value)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2930, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract negotiation time

- id: `kpi.management.contract-negotiation-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract negotiation time measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Contract negotiation time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract negotiation time on the desired side of its target for this period?

Inputs:

- `metric.contract-negotiation-time` (Contract negotiation time)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2931, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract response times not met

- id: `kpi.management.contract-response-times-not-met`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract response times not met measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Contract response times not met, B is whole named by Contract response times not met. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract response times not met on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-contract-response-times-not-met` (part named by Contract response times not met)
- `metric.whole-named-by-contract-response-times-not-met` (whole named by Contract response times not met)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2932, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contracts completion on-time

- id: `kpi.management.contracts-completion-on-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contracts completion on-time measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Contracts completion on-time, B is whole named by Contracts completion on-time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contracts completion on-time on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-contracts-completion-on-time` (part named by Contracts completion on-time)
- `metric.whole-named-by-contracts-completion-on-time` (whole named by Contracts completion on-time)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2933, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost reimbursement contracts

- id: `kpi.management.cost-reimbursement-contracts`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost reimbursement contracts measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Cost reimbursement contracts, B is whole named by Cost reimbursement contracts. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost reimbursement contracts on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-cost-reimbursement-contracts` (part named by Cost reimbursement contracts)
- `metric.whole-named-by-cost-reimbursement-contracts` (whole named by Cost reimbursement contracts)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2934, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract breaches due to non-compliance

- id: `kpi.management.contract-breaches-due-to-non-compliance`
- kind: kri
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract breaches due to non-compliance measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is Contract breaches due, B is non-compliance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract breaches due to non-compliance on the desired side of its target for this period?

Inputs:

- `metric.contract-breaches-due` (Contract breaches due)
- `metric.non-compliance` (non-compliance)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2935, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Penalty payments for constant failure

- id: `kpi.management.penalty-payments-for-constant-failure`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Penalty payments for constant failure measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Penalty payments for constant failure. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Penalty payments for constant failure on the desired side of its target for this period?

Inputs:

- `metric.penalty-payments-for-constant-failure` (Penalty payments for constant failure)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2937, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract time to completion

- id: `kpi.management.contract-time-to-completion`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract time to completion measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Contract time to completion. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract time to completion on the desired side of its target for this period?

Inputs:

- `metric.contract-time-to-completion` (Contract time to completion)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2941, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract penalties

- id: `kpi.management.contract-penalties`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract penalties measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Contract penalties, B is whole named by Contract penalties. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract penalties on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-contract-penalties` (part named by Contract penalties)
- `metric.whole-named-by-contract-penalties` (whole named by Contract penalties)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2944, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Frequency of contract renewals

- id: `kpi.management.frequency-of-contract-renewals`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Frequency of contract renewals measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Frequency of contract renewals. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Frequency of contract renewals on the desired side of its target for this period?

Inputs:

- `metric.frequency-of-contract-renewals` (Frequency of contract renewals)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2944, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contracts that fail to deliver direct agreements

- id: `kpi.management.contracts-that-fail-to-deliver-direct-agreements`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contracts that fail to deliver direct agreements measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is Contracts that fail, B is deliver direct agreements. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contracts that fail to deliver direct agreements on the desired side of its target for this period?

Inputs:

- `metric.contracts-that-fail` (Contracts that fail)
- `metric.deliver-direct-agreements` (deliver direct agreements)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2945, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Estimated value of contract extension

- id: `kpi.management.estimated-value-of-contract-extension`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Estimated value of contract extension measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Estimated value of contract extension. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Estimated value of contract extension on the desired side of its target for this period?

Inputs:

- `metric.estimated-value-of-contract-extension` (Estimated value of contract extension)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2946, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract variation value

- id: `kpi.management.contract-variation-value`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract variation value measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Contract variation value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract variation value on the desired side of its target for this period?

Inputs:

- `metric.contract-variation-value` (Contract variation value)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2948, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Requirements contracts

- id: `kpi.management.requirements-contracts`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Requirements contracts measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Requirements contracts, B is whole named by Requirements contracts. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Requirements contracts on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-requirements-contracts` (part named by Requirements contracts)
- `metric.whole-named-by-requirements-contracts` (whole named by Requirements contracts)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2949, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Changes to contract milestone dates

- id: `kpi.management.changes-to-contract-milestone-dates`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Changes to contract milestone dates measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is Changes, B is contract milestone dates. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Changes to contract milestone dates on the desired side of its target for this period?

Inputs:

- `metric.changes` (Changes)
- `metric.contract-milestone-dates` (contract milestone dates)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2951, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract duration

- id: `kpi.management.contract-duration`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract duration measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Contract duration. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract duration on the desired side of its target for this period?

Inputs:

- `metric.contract-duration` (Contract duration)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2952, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Length of contract extensions

- id: `kpi.management.length-of-contract-extensions`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Length of contract extensions measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Length of contract extensions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Length of contract extensions on the desired side of its target for this period?

Inputs:

- `metric.length-of-contract-extensions` (Length of contract extensions)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2954, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract report

- id: `kpi.management.contract-report`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract report measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Contract report. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract report on the desired side of its target for this period?

Inputs:

- `metric.contract-report` (Contract report)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2955, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Variations of supply quantity

- id: `kpi.management.variations-of-supply-quantity`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Variations of supply quantity measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Variations of supply quantity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Variations of supply quantity on the desired side of its target for this period?

Inputs:

- `metric.variations-of-supply-quantity` (Variations of supply quantity)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK2958, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Bid and proposal costs

- id: `kpi.management.bid-and-proposal-costs`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Bid and proposal costs measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Bid and proposal costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Bid and proposal costs on the desired side of its target for this period?

Inputs:

- `metric.bid-and-proposal-costs` (Bid and proposal costs)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK3033, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Vendor fraud

- id: `kpi.management.vendor-fraud`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Vendor fraud measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Vendor fraud. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Vendor fraud on the desired side of its target for this period?

Inputs:

- `metric.vendor-fraud` (Vendor fraud)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK3037, page_0053)
- organizational / industries / Retail / General (sK4537, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Policies, agreements and contracts updated

- id: `kpi.management.policies-agreements-and-contracts-updated`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Policies, agreements and contracts updated measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Policies, agreements and contracts updated. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Policies, agreements and contracts updated on the desired side of its target for this period?

Inputs:

- `metric.policies-agreements-and-contracts-updated` (Policies, agreements and contracts updated)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK6231, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contracts filed without error

- id: `kpi.management.contracts-filed-without-error`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contracts filed without error measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Contracts filed without error. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contracts filed without error on the desired side of its target for this period?

Inputs:

- `metric.contracts-filed-without-error` (Contracts filed without error)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK6090, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contract concessions

- id: `kpi.management.contract-concessions`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contract concessions measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Contract concessions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contract concessions on the desired side of its target for this period?

Inputs:

- `metric.contract-concessions` (Contract concessions)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK7055, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
