# Human Resources / Recruitment

Context: organizational. Group: functional. KPIs: 70.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Cost per hire

- id: `kpi.human-resources.cost-per-hire`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Cost per hire measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A / B, where A is Cost, B is hire. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost per hire on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.hire` (hire)

Placements:

- organizational / functional / Human Resources / Recruitment (sK49, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time to start

- id: `kpi.human-resources.time-to-start`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Time to start measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Time to start. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time to start on the desired side of its target for this period?

Inputs:

- `metric.time-to-start` (Time to start)

Placements:

- organizational / functional / Human Resources / Recruitment (sK50, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Internal promotion rate

- id: `kpi.human-resources.internal-promotion-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Internal promotion rate measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is numerator of Internal promotion rate, B is base of Internal promotion rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Internal promotion rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-internal-promotion-rate` (numerator of Internal promotion rate)
- `metric.base-of-internal-promotion-rate` (base of Internal promotion rate)

Placements:

- organizational / functional / Human Resources / Recruitment (sK51, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Job offer acceptance rate

- id: `kpi.human-resources.job-offer-acceptance-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Job offer acceptance rate measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is numerator of Job offer acceptance rate, B is base of Job offer acceptance rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Job offer acceptance rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-job-offer-acceptance-rate` (numerator of Job offer acceptance rate)
- `metric.base-of-job-offer-acceptance-rate` (base of Job offer acceptance rate)

Placements:

- organizational / functional / Human Resources / Recruitment (sK53, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Open job requisitions

- id: `kpi.human-resources.open-job-requisitions`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Open job requisitions measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Open job requisitions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Open job requisitions on the desired side of its target for this period?

Inputs:

- `metric.open-job-requisitions` (Open job requisitions)

Placements:

- organizational / functional / Human Resources / Recruitment (sK241, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Open requisitions to current staff

- id: `kpi.human-resources.open-requisitions-to-current-staff`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Open requisitions to current staff measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Open requisitions to current staff. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Open requisitions to current staff on the desired side of its target for this period?

Inputs:

- `metric.open-requisitions-to-current-staff` (Open requisitions to current staff)

Placements:

- organizational / functional / Human Resources / Recruitment (sK242, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Recruiters to open requisitions ratio

- id: `kpi.human-resources.recruiters-to-open-requisitions-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Recruiters to open requisitions ratio measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Recruiters to open requisitions ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Recruiters to open requisitions ratio on the desired side of its target for this period?

Inputs:

- `metric.recruiters-to-open-requisitions-ratio` (Recruiters to open requisitions ratio)

Placements:

- organizational / functional / Human Resources / Recruitment (sK243, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Signing bonus expense

- id: `kpi.human-resources.signing-bonus-expense`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Signing bonus expense measures that result inside Human Resources, subcategory Recruitment. The unit is currency. The formula is A, where A is Signing bonus expense. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Signing bonus expense on the desired side of its target for this period?

Inputs:

- `metric.signing-bonus-expense` (Signing bonus expense)

Placements:

- organizational / functional / Human Resources / Recruitment (sK860, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Open time of job positions

- id: `kpi.human-resources.open-time-of-job-positions`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Open time of job positions measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Open time of job positions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Open time of job positions on the desired side of its target for this period?

Inputs:

- `metric.open-time-of-job-positions` (Open time of job positions)

Placements:

- organizational / functional / Human Resources / Recruitment (sK872, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Applications received per vacancy

- id: `kpi.human-resources.applications-received-per-vacancy`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Applications received per vacancy measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A / B, where A is Applications received, B is vacancy. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Applications received per vacancy on the desired side of its target for this period?

Inputs:

- `metric.applications-received` (Applications received)
- `metric.vacancy` (vacancy)

Placements:

- organizational / functional / Human Resources / Recruitment (sK873, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Interns from a banditist CVs

- id: `kpi.human-resources.interns-from-a-banditist-cvs`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Interns from a banditist CVs measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is Interns, B is a banditist CVs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Interns from a banditist CVs on the desired side of its target for this period?

Inputs:

- `metric.interns` (Interns)
- `metric.a-banditist-cvs` (a banditist CVs)

Placements:

- organizational / functional / Human Resources / Recruitment (sK868, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time to fill a vacant position

- id: `kpi.human-resources.time-to-fill-a-vacant-position`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Time to fill a vacant position measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Time to fill a vacant position. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time to fill a vacant position on the desired side of its target for this period?

Inputs:

- `metric.time-to-fill-a-vacant-position` (Time to fill a vacant position)

Placements:

- organizational / functional / Human Resources / Recruitment (sK868, page_0023)
- organizational / industries / Media / Recruitment/Employment Activities (sK688, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Recruitment costs

- id: `kpi.human-resources.recruitment-costs`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Recruitment costs measures that result inside Human Resources, subcategory Recruitment. The unit is currency. The formula is A, where A is Recruitment costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Recruitment costs on the desired side of its target for this period?

Inputs:

- `metric.recruitment-costs` (Recruitment costs)

Placements:

- organizational / functional / Human Resources / Recruitment (sK710, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Staffing rate

- id: `kpi.human-resources.staffing-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Staffing rate measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is numerator of Staffing rate, B is base of Staffing rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Staffing rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-staffing-rate` (numerator of Staffing rate)
- `metric.base-of-staffing-rate` (base of Staffing rate)

Placements:

- organizational / functional / Human Resources / Recruitment (sK763, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Applicants referred by current employees

- id: `kpi.human-resources.applicants-referred-by-current-employees`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Applicants referred by current employees measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Applicants referred by current employees. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Applicants referred by current employees on the desired side of its target for this period?

Inputs:

- `metric.applicants-referred-by-current-employees` (Applicants referred by current employees)

Placements:

- organizational / functional / Human Resources / Recruitment (sK765, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New staff post-employment interview completed

- id: `kpi.human-resources.new-staff-post-employment-interview-completed`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

New staff post-employment interview completed measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is part named by New staff post-employment interview completed, B is whole named by New staff post-employment interview completed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New staff post-employment interview completed on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-new-staff-post-employment-interview-completed` (part named by New staff post-employment interview completed)
- `metric.whole-named-by-new-staff-post-employment-interview-completed` (whole named by New staff post-employment interview completed)

Placements:

- organizational / functional / Human Resources / Recruitment (sK779, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Succession plans for key positions

- id: `kpi.human-resources.succession-plans-for-key-positions`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Succession plans for key positions measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is part named by Succession plans for key positions, B is whole named by Succession plans for key positions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Succession plans for key positions on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-succession-plans-for-key-positions` (part named by Succession plans for key positions)
- `metric.whole-named-by-succession-plans-for-key-positions` (whole named by Succession plans for key positions)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1777, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Junior and middle managers who were promoted internally

- id: `kpi.human-resources.junior-and-middle-managers-who-were-promoted-internally`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Junior and middle managers who were promoted internally measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is part named by Junior and middle managers who were promoted internally, B is whole named by Junior and middle managers who were promoted internally. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Junior and middle managers who were promoted internally on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-junior-and-middle-managers-who-were-promoted-internally` (part named by Junior and middle managers who were promoted internally)
- `metric.whole-named-by-junior-and-middle-managers-who-were-promoted-internally` (whole named by Junior and middle managers who were promoted internally)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1779, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employment offers made within the target timeframe

- id: `kpi.human-resources.employment-offers-made-within-the-target-timeframe`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employment offers made within the target timeframe measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is part named by Employment offers made within the target timeframe, B is whole named by Employment offers made within the target timeframe. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employment offers made within the target timeframe on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-employment-offers-made-within-the-target-timeframe` (part named by Employment offers made within the target timeframe)
- `metric.whole-named-by-employment-offers-made-within-the-target-timeframe` (whole named by Employment offers made within the target timeframe)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1781, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Signing bonus rate

- id: `kpi.human-resources.signing-bonus-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Signing bonus rate measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is numerator of Signing bonus rate, B is base of Signing bonus rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Signing bonus rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-signing-bonus-rate` (numerator of Signing bonus rate)
- `metric.base-of-signing-bonus-rate` (base of Signing bonus rate)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1782, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Career path ratio

- id: `kpi.human-resources.career-path-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Career path ratio measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Career path ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Career path ratio on the desired side of its target for this period?

Inputs:

- `metric.career-path-ratio` (Career path ratio)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1783, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cross functional mobility

- id: `kpi.human-resources.cross-functional-mobility`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Cross functional mobility measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is part named by Cross functional mobility, B is whole named by Cross functional mobility. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cross functional mobility on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-cross-functional-mobility` (part named by Cross functional mobility)
- `metric.whole-named-by-cross-functional-mobility` (whole named by Cross functional mobility)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1784, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Internal hire rate

- id: `kpi.human-resources.internal-hire-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Internal hire rate measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is numerator of Internal hire rate, B is base of Internal hire rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Internal hire rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-internal-hire-rate` (numerator of Internal hire rate)
- `metric.base-of-internal-hire-rate` (base of Internal hire rate)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1785, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Internal placement rate

- id: `kpi.human-resources.internal-placement-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Internal placement rate measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is numerator of Internal placement rate, B is base of Internal placement rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Internal placement rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-internal-placement-rate` (numerator of Internal placement rate)
- `metric.base-of-internal-placement-rate` (base of Internal placement rate)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1786, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees lateral mobility

- id: `kpi.human-resources.employees-lateral-mobility`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employees lateral mobility measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is part named by Employees lateral mobility, B is whole named by Employees lateral mobility. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees lateral mobility on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-employees-lateral-mobility` (part named by Employees lateral mobility)
- `metric.whole-named-by-employees-lateral-mobility` (whole named by Employees lateral mobility)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1787, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Promotion speed ratio

- id: `kpi.human-resources.promotion-speed-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Promotion speed ratio measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Promotion speed ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Promotion speed ratio on the desired side of its target for this period?

Inputs:

- `metric.promotion-speed-ratio` (Promotion speed ratio)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1788, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employee transfer rate

- id: `kpi.human-resources.employee-transfer-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employee transfer rate measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is numerator of Employee transfer rate, B is base of Employee transfer rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employee transfer rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-employee-transfer-rate` (numerator of Employee transfer rate)
- `metric.base-of-employee-transfer-rate` (base of Employee transfer rate)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1789, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Recruitment source breakdown

- id: `kpi.human-resources.recruitment-source-breakdown`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Recruitment source breakdown measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is part named by Recruitment source breakdown, B is whole named by Recruitment source breakdown. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Recruitment source breakdown on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-recruitment-source-breakdown` (part named by Recruitment source breakdown)
- `metric.whole-named-by-recruitment-source-breakdown` (whole named by Recruitment source breakdown)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1790, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Recruitment source ratio

- id: `kpi.human-resources.recruitment-source-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Recruitment source ratio measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Recruitment source ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Recruitment source ratio on the desired side of its target for this period?

Inputs:

- `metric.recruitment-source-ratio` (Recruitment source ratio)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1791, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Interviewer mix

- id: `kpi.human-resources.interviewer-mix`
- kind: kpi
- unit: count
- direction: corridor
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Interviewer mix measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Interviewer mix. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Interviewer mix on the desired side of its target for this period?

Inputs:

- `metric.interviewer-mix` (Interviewer mix)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1792, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Recruitment referral

- id: `kpi.human-resources.recruitment-referral`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Recruitment referral measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Recruitment referral. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Recruitment referral on the desired side of its target for this period?

Inputs:

- `metric.recruitment-referral` (Recruitment referral)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1793, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Applicant interview rate

- id: `kpi.human-resources.applicant-interview-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Applicant interview rate measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is numerator of Applicant interview rate, B is base of Applicant interview rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Applicant interview rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-applicant-interview-rate` (numerator of Applicant interview rate)
- `metric.base-of-applicant-interview-rate` (base of Applicant interview rate)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1795, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Interview employment offer rate

- id: `kpi.human-resources.interview-employment-offer-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Interview employment offer rate measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is numerator of Interview employment offer rate, B is base of Interview employment offer rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Interview employment offer rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-interview-employment-offer-rate` (numerator of Interview employment offer rate)
- `metric.base-of-interview-employment-offer-rate` (base of Interview employment offer rate)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1796, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Interview rate

- id: `kpi.human-resources.interview-rate`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Interview rate measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Interview rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Interview rate on the desired side of its target for this period?

Inputs:

- `metric.interview-rate` (Interview rate)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1797, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New hires terminated within 30 days

- id: `kpi.human-resources.new-hires-terminated-within-30-days`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

New hires terminated within 30 days measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is part named by New hires terminated within 30 days, B is whole named by New hires terminated within 30 days. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New hires terminated within 30 days on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-new-hires-terminated-within-30-days` (part named by New hires terminated within 30 days)
- `metric.whole-named-by-new-hires-terminated-within-30-days` (whole named by New hires terminated within 30 days)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1798, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New hire performance satisfaction index

- id: `kpi.human-resources.new-hire-performance-satisfaction-index`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: index
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

New hire performance satisfaction index measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is (A / B) * 100, where A is current New hire performance satisfaction index, B is base-period New hire performance satisfaction index. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New hire performance satisfaction index on the desired side of its target for this period?

Inputs:

- `metric.current-new-hire-performance-satisfaction-index` (current New hire performance satisfaction index)
- `metric.base-period-new-hire-performance-satisfaction-index` (base-period New hire performance satisfaction index)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1799, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New hire satisfaction with recruiting index

- id: `kpi.human-resources.new-hire-satisfaction-with-recruiting-index`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: index
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

New hire satisfaction with recruiting index measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is (A / B) * 100, where A is current New hire satisfaction with recruiting index, B is base-period New hire satisfaction with recruiting index. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New hire satisfaction with recruiting index on the desired side of its target for this period?

Inputs:

- `metric.current-new-hire-satisfaction-with-recruiting-index` (current New hire satisfaction with recruiting index)
- `metric.base-period-new-hire-satisfaction-with-recruiting-index` (base-period New hire satisfaction with recruiting index)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1800, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### External hire rate

- id: `kpi.human-resources.external-hire-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

External hire rate measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is numerator of External hire rate, B is base of External hire rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is External hire rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-external-hire-rate` (numerator of External hire rate)
- `metric.base-of-external-hire-rate` (base of External hire rate)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1801, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Net hire ratio

- id: `kpi.human-resources.net-hire-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Net hire ratio measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Net hire ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Net hire ratio on the desired side of its target for this period?

Inputs:

- `metric.net-hire-ratio` (Net hire ratio)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1802, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New position recruitment rate

- id: `kpi.human-resources.new-position-recruitment-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

New position recruitment rate measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is numerator of New position recruitment rate, B is base of New position recruitment rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New position recruitment rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-new-position-recruitment-rate` (numerator of New position recruitment rate)
- `metric.base-of-new-position-recruitment-rate` (base of New position recruitment rate)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1803, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New position recruitment ratio

- id: `kpi.human-resources.new-position-recruitment-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

New position recruitment ratio measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is New position recruitment ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New position recruitment ratio on the desired side of its target for this period?

Inputs:

- `metric.new-position-recruitment-ratio` (New position recruitment ratio)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1804, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Applicant ratio

- id: `kpi.human-resources.applicant-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Applicant ratio measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Applicant ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Applicant ratio on the desired side of its target for this period?

Inputs:

- `metric.applicant-ratio` (Applicant ratio)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1805, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### On time talent delivery

- id: `kpi.human-resources.on-time-talent-delivery`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

On time talent delivery measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is On time talent delivery. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is On time talent delivery on the desired side of its target for this period?

Inputs:

- `metric.on-time-talent-delivery` (On time talent delivery)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1806, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employee probation reports assessed

- id: `kpi.human-resources.employee-probation-reports-assessed`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employee probation reports assessed measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is part named by Employee probation reports assessed, B is whole named by Employee probation reports assessed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employee probation reports assessed on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-employee-probation-reports-assessed` (part named by Employee probation reports assessed)
- `metric.whole-named-by-employee-probation-reports-assessed` (whole named by Employee probation reports assessed)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1808, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Long term vacancies per total number of jobs

- id: `kpi.human-resources.long-term-vacancies-per-total-number-of-jobs`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Long term vacancies per total number of jobs measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A / B, where A is Long term vacancies, B is total number of jobs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Long term vacancies per total number of jobs on the desired side of its target for this period?

Inputs:

- `metric.long-term-vacancies` (Long term vacancies)
- `metric.total-number-of-jobs` (total number of jobs)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1811, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Applications received by recruiting source

- id: `kpi.human-resources.applications-received-by-recruiting-source`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Applications received by recruiting source measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Applications received by recruiting source. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Applications received by recruiting source on the desired side of its target for this period?

Inputs:

- `metric.applications-received-by-recruiting-source` (Applications received by recruiting source)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1813, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Response time for recruitment inquiries

- id: `kpi.human-resources.response-time-for-recruitment-inquiries`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Response time for recruitment inquiries measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Response time for recruitment inquiries. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Response time for recruitment inquiries on the desired side of its target for this period?

Inputs:

- `metric.response-time-for-recruitment-inquiries` (Response time for recruitment inquiries)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1814, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Newly recruited employees screened

- id: `kpi.human-resources.newly-recruited-employees-screened`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Newly recruited employees screened measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is part named by Newly recruited employees screened, B is whole named by Newly recruited employees screened. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Newly recruited employees screened on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-newly-recruited-employees-screened` (part named by Newly recruited employees screened)
- `metric.whole-named-by-newly-recruited-employees-screened` (whole named by Newly recruited employees screened)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1815, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Interviewing cost

- id: `kpi.human-resources.interviewing-cost`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Interviewing cost measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Interviewing cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Interviewing cost on the desired side of its target for this period?

Inputs:

- `metric.interviewing-cost` (Interviewing cost)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1819, page_0023)
- organizational / industries / Media / Recruitment/Employment Activities (sK1819, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Internal questions above level

- id: `kpi.human-resources.internal-questions-above-level`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Internal questions above level measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is part named by Internal questions above level, B is whole named by Internal questions above level. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Internal questions above level on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-internal-questions-above-level` (part named by Internal questions above level)
- `metric.whole-named-by-internal-questions-above-level` (whole named by Internal questions above level)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1823, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hire of in-house recruitment ratio

- id: `kpi.human-resources.hire-of-in-house-recruitment-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Hire of in-house recruitment ratio measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Hire of in-house recruitment ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hire of in-house recruitment ratio on the desired side of its target for this period?

Inputs:

- `metric.hire-of-in-house-recruitment-ratio` (Hire of in-house recruitment ratio)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1824, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Applicants average age

- id: `kpi.human-resources.applicants-average-age`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: average
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Applicants average age measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A / B, where A is sum underlying Applicants average age, B is count of observations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Applicants average age on the desired side of its target for this period?

Inputs:

- `metric.sum-underlying-applicants-average-age` (sum underlying Applicants average age)
- `metric.count-of-observations` (count of observations)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1825, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unsolicited applications net of

- id: `kpi.human-resources.unsolicited-applications-net-of`
- kind: kpi
- unit: percent
- direction: up
- timing: leading
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Unsolicited applications net of measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is part named by Unsolicited applications net of, B is whole named by Unsolicited applications net of. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unsolicited applications net of on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-unsolicited-applications-net-of` (part named by Unsolicited applications net of)
- `metric.whole-named-by-unsolicited-applications-net-of` (whole named by Unsolicited applications net of)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1826, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employment or requirements fill schedule

- id: `kpi.human-resources.employment-or-requirements-fill-schedule`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employment or requirements fill schedule measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is part named by Employment or requirements fill schedule, B is whole named by Employment or requirements fill schedule. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employment or requirements fill schedule on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-employment-or-requirements-fill-schedule` (part named by Employment or requirements fill schedule)
- `metric.whole-named-by-employment-or-requirements-fill-schedule` (whole named by Employment or requirements fill schedule)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1828, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Promotions and management changes publicized

- id: `kpi.human-resources.promotions-and-management-changes-publicized`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Promotions and management changes publicized measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is part named by Promotions and management changes publicized, B is whole named by Promotions and management changes publicized. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Promotions and management changes publicized on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-promotions-and-management-changes-publicized` (part named by Promotions and management changes publicized)
- `metric.whole-named-by-promotions-and-management-changes-publicized` (whole named by Promotions and management changes publicized)

Placements:

- organizational / functional / Human Resources / Recruitment (sK1829, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Requisitions handled per recruiter

- id: `kpi.human-resources.requisitions-handled-per-recruiter`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Requisitions handled per recruiter measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A / B, where A is Requisitions handled, B is recruiter. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Requisitions handled per recruiter on the desired side of its target for this period?

Inputs:

- `metric.requisitions-handled` (Requisitions handled)
- `metric.recruiter` (recruiter)

Placements:

- organizational / functional / Human Resources / Recruitment (sKf723, page_0023)
- organizational / industries / Media / Recruitment/Employment Activities (sK4723, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Abandonment per new hire

- id: `kpi.human-resources.abandonment-per-new-hire`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Abandonment per new hire measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A / B, where A is Abandonment, B is new hire. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Abandonment per new hire on the desired side of its target for this period?

Inputs:

- `metric.abandonment` (Abandonment)
- `metric.new-hire` (new hire)

Placements:

- organizational / functional / Human Resources / Recruitment (sKf726, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Inquiries per app. job positions

- id: `kpi.human-resources.inquiries-per-app-job-positions`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Inquiries per app. job positions measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A / B, where A is Inquiries, B is app. job positions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Inquiries per app. job positions on the desired side of its target for this period?

Inputs:

- `metric.inquiries` (Inquiries)
- `metric.app-job-positions` (app. job positions)

Placements:

- organizational / functional / Human Resources / Recruitment (sKf727, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Recruit to hire ratio for job placements

- id: `kpi.human-resources.recruit-to-hire-ratio-for-job-placements`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Recruit to hire ratio for job placements measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Recruit to hire ratio for job placements. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Recruit to hire ratio for job placements on the desired side of its target for this period?

Inputs:

- `metric.recruit-to-hire-ratio-for-job-placements` (Recruit to hire ratio for job placements)

Placements:

- organizational / functional / Human Resources / Recruitment (sKf492, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Resource requests overdue

- id: `kpi.human-resources.resource-requests-overdue`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Resource requests overdue measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is part named by Resource requests overdue, B is whole named by Resource requests overdue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Resource requests overdue on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-resource-requests-overdue` (part named by Resource requests overdue)
- `metric.whole-named-by-resource-requests-overdue` (whole named by Resource requests overdue)

Placements:

- organizational / functional / Human Resources / Recruitment (sK6521, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Recruiter positions filled internally

- id: `kpi.human-resources.recruiter-positions-filled-internally`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Recruiter positions filled internally measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is part named by Recruiter positions filled internally, B is whole named by Recruiter positions filled internally. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Recruiter positions filled internally on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-recruiter-positions-filled-internally` (part named by Recruiter positions filled internally)
- `metric.whole-named-by-recruiter-positions-filled-internally` (whole named by Recruiter positions filled internally)

Placements:

- organizational / functional / Human Resources / Recruitment (sK6422, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Traineeship job openings

- id: `kpi.human-resources.traineeship-job-openings`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Traineeship job openings measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is part named by Traineeship job openings, B is whole named by Traineeship job openings. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Traineeship job openings on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-traineeship-job-openings` (part named by Traineeship job openings)
- `metric.whole-named-by-traineeship-job-openings` (whole named by Traineeship job openings)

Placements:

- organizational / functional / Human Resources / Recruitment (sK6825, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Recruitment partnerships

- id: `kpi.human-resources.recruitment-partnerships`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Recruitment partnerships measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Recruitment partnerships. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Recruitment partnerships on the desired side of its target for this period?

Inputs:

- `metric.recruitment-partnerships` (Recruitment partnerships)

Placements:

- organizational / functional / Human Resources / Recruitment (sK6826, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Administrative staff per recruiter

- id: `kpi.human-resources.administrative-staff-per-recruiter`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Administrative staff per recruiter measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A / B, where A is Administrative staff, B is recruiter. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Administrative staff per recruiter on the desired side of its target for this period?

Inputs:

- `metric.administrative-staff` (Administrative staff)
- `metric.recruiter` (recruiter)

Placements:

- organizational / functional / Human Resources / Recruitment (sK6919, page_0023)
- organizational / industries / Media / Organizational » Industries (sE0519, page_0164)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Candidates database use

- id: `kpi.human-resources.candidates-database-use`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Candidates database use measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Candidates database use. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Candidates database use on the desired side of its target for this period?

Inputs:

- `metric.candidates-database-use` (Candidates database use)

Placements:

- organizational / functional / Human Resources / Recruitment (sK6922, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Candidate files up to date in database

- id: `kpi.human-resources.candidate-files-up-to-date-in-database`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Candidate files up to date in database measures that result inside Human Resources, subcategory Recruitment. The unit is percent. The formula is (A / B) * 100, where A is Candidate files up, B is date in database. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Candidate files up to date in database on the desired side of its target for this period?

Inputs:

- `metric.candidate-files-up` (Candidate files up)
- `metric.date-in-database` (date in database)

Placements:

- organizational / functional / Human Resources / Recruitment (sK6924, page_0023)
- organizational / industries / Media / Organizational » Industries (sE0524, page_0164)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employed persons

- id: `kpi.human-resources.employed-persons`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Employed persons measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Employed persons. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employed persons on the desired side of its target for this period?

Inputs:

- `metric.employed-persons` (Employed persons)

Placements:

- organizational / functional / Human Resources / Recruitment (sK14107, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Internal promotions

- id: `kpi.human-resources.internal-promotions`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Internal promotions measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Internal promotions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Internal promotions on the desired side of its target for this period?

Inputs:

- `metric.internal-promotions` (Internal promotions)

Placements:

- organizational / functional / Human Resources / Recruitment (sK14213, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Interviews conducted

- id: `kpi.human-resources.interviews-conducted`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Interviews conducted measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Interviews conducted. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Interviews conducted on the desired side of its target for this period?

Inputs:

- `metric.interviews-conducted` (Interviews conducted)

Placements:

- organizational / functional / Human Resources / Recruitment (sK14214, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Officers employed

- id: `kpi.human-resources.officers-employed`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.recruitment`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Officers employed measures that result inside Human Resources, subcategory Recruitment. The unit is count. The formula is A, where A is Officers employed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Officers employed on the desired side of its target for this period?

Inputs:

- `metric.officers-employed` (Officers employed)

Placements:

- organizational / functional / Human Resources / Recruitment (sK14247, page_0023)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
