# Accounting / Business Consulting

Context: organizational. Group: functional. KPIs: 35.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Billable fees write-downs

- id: `kpi.planning.billable-fees-write-downs`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Billable fees write-downs measures that result inside Planning, subcategory Organizational » Functional Areas. The unit is count. The formula is A, where A is Billable fees write-downs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Billable fees write-downs on the desired side of its target for this period?

Inputs:

- `metric.billable-fees-write-downs` (Billable fees write-downs)

Placements:

- organizational / functional / Planning / Organizational » Functional Areas (sK4715, page_0011)
- organizational / functional / Accounting / General (aK671, page_0158)
- organizational / functional / Accounting / Business Consulting (#K715, page_0158)
- organizational / industries / Media / Recruitment/Employment Activities (sK4715, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Profitable projects

- id: `kpi.management.profitable-projects`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Profitable projects measures that result inside Management, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Profitable projects, B is whole named by Profitable projects. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Profitable projects on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-profitable-projects` (part named by Profitable projects)
- `metric.whole-named-by-profitable-projects` (whole named by Profitable projects)

Placements:

- organizational / functional / Management / General (#K116, page_0045)
- organizational / functional / Accounting / General (aK416, page_0158)
- organizational / functional / Accounting / Business Consulting (#K416, page_0158)
- organizational / industries / Accounting / Engineering (sK416, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Potential new clients contacted

- id: `kpi.sales-and-customer-service.potential-new-clients-contacted`
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

Potential new clients contacted measures that result inside Sales and Customer Service, subcategory Organizational > Functional Areas. The unit is count. The formula is A, where A is Potential new clients contacted. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Potential new clients contacted on the desired side of its target for this period?

Inputs:

- `metric.potential-new-clients-contacted` (Potential new clients contacted)

Placements:

- organizational / functional / Sales and Customer Service / Organizational > Functional Areas (sK6916, page_0052)
- organizational / functional / Accounting / General (aK6916, page_0158)
- organizational / functional / Accounting / Business Consulting (#K916, page_0158)
- organizational / industries / Media / Organizational » Industries (sE0516, page_0164)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Backlog of commissioned projects

- id: `kpi.accounting.backlog-of-commissioned-projects`
- kind: kpi
- unit: percent
- direction: up
- timing: leading
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Backlog of commissioned projects measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Backlog, B is commissioned projects. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Backlog of commissioned projects on the desired side of its target for this period?

Inputs:

- `metric.backlog` (Backlog)
- `metric.commissioned-projects` (commissioned projects)

Placements:

- organizational / functional / Accounting / General (aK016, page_0158)
- organizational / functional / Accounting / Business Consulting (#K106, page_0158)
- organizational / industries / Accounting / Engineering (sK106, page_0159)
- organizational / industries / Media / Recruitment/Employment Activities (sK016, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Bill rate

- id: `kpi.accounting.bill-rate`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Bill rate measures that result inside Accounting, subcategory General. The unit is currency. The formula is A, where A is Bill rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Bill rate on the desired side of its target for this period?

Inputs:

- `metric.bill-rate` (Bill rate)

Placements:

- organizational / functional / Accounting / General (aK131, page_0158)
- organizational / functional / Accounting / Business Consulting (#K313, page_0158)
- organizational / industries / Accounting / Engineering (sK131, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Consultant retention by client

- id: `kpi.accounting.consultant-retention-by-client`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Consultant retention by client measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Consultant retention by client, B is whole named by Consultant retention by client. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Consultant retention by client on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-consultant-retention-by-client` (part named by Consultant retention by client)
- `metric.whole-named-by-consultant-retention-by-client` (whole named by Consultant retention by client)

Placements:

- organizational / functional / Accounting / General (aK115, page_0158)
- organizational / functional / Accounting / Business Consulting (#K315, page_0158)
- organizational / industries / Accounting / Engineering (sK415, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hourly fee

- id: `kpi.accounting.hourly-fee`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Hourly fee measures that result inside Accounting, subcategory General. The unit is count. The formula is A, where A is Hourly fee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hourly fee on the desired side of its target for this period?

Inputs:

- `metric.hourly-fee` (Hourly fee)

Placements:

- organizational / functional / Accounting / General (aK417, page_0158)
- organizational / functional / Accounting / Business Consulting (#K317, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of services delivered

- id: `kpi.accounting.cost-of-services-delivered`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of services delivered measures that result inside Accounting, subcategory General. The unit is currency. The formula is A, where A is Cost of services delivered. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of services delivered on the desired side of its target for this period?

Inputs:

- `metric.cost-of-services-delivered` (Cost of services delivered)

Placements:

- organizational / functional / Accounting / General (aK650, page_0158)
- organizational / functional / Accounting / Business Consulting (#K603, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Delivery overhead costs

- id: `kpi.accounting.delivery-overhead-costs`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Delivery overhead costs measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Delivery overhead costs, B is whole named by Delivery overhead costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Delivery overhead costs on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-delivery-overhead-costs` (part named by Delivery overhead costs)
- `metric.whole-named-by-delivery-overhead-costs` (whole named by Delivery overhead costs)

Placements:

- organizational / functional / Accounting / General (aK651, page_0158)
- organizational / functional / Accounting / Business Consulting (#K651, page_0158)
- organizational / industries / Accounting / Engineering (sK451, page_0159)
- organizational / industries / Media / Recruitment/Employment Activities (sK1651, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Net revenue per technical staff

- id: `kpi.accounting.net-revenue-per-technical-staff`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Net revenue per technical staff measures that result inside Accounting, subcategory General. The unit is currency. The formula is A / B, where A is Net revenue, B is technical staff. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Net revenue per technical staff on the desired side of its target for this period?

Inputs:

- `metric.net-revenue` (Net revenue)
- `metric.technical-staff` (technical staff)

Placements:

- organizational / functional / Accounting / General (aK664, page_0158)
- organizational / functional / Accounting / Business Consulting (#K664, page_0158)
- organizational / industries / Accounting / Engineering (sK464, page_0159)
- organizational / industries / Media / Recruitment/Employment Activities (sK4665, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue by practice

- id: `kpi.accounting.revenue-by-practice`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Revenue by practice measures that result inside Accounting, subcategory General. The unit is currency. The formula is A, where A is Revenue by practice. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue by practice on the desired side of its target for this period?

Inputs:

- `metric.revenue-by-practice` (Revenue by practice)

Placements:

- organizational / functional / Accounting / General (aK666, page_0158)
- organizational / functional / Accounting / Business Consulting (#K665, page_0158)
- organizational / industries / Accounting / Engineering (sK465, page_0159)
- organizational / industries / Media / Recruitment/Employment Activities (sK4655, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Billable hours

- id: `kpi.accounting.billable-hours`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Billable hours measures that result inside Accounting, subcategory General. The unit is count. The formula is A, where A is Billable hours. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Billable hours on the desired side of its target for this period?

Inputs:

- `metric.billable-hours` (Billable hours)

Placements:

- organizational / functional / Accounting / General (aK673, page_0158)
- organizational / functional / Accounting / Business Consulting (#K703, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Blended rate

- id: `kpi.accounting.blended-rate`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Blended rate measures that result inside Accounting, subcategory General. The unit is currency. The formula is A, where A is Blended rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Blended rate on the desired side of its target for this period?

Inputs:

- `metric.blended-rate` (Blended rate)

Placements:

- organizational / functional / Accounting / General (aK671, page_0158)
- organizational / functional / Accounting / Business Consulting (#K710, page_0158)
- organizational / industries / Accounting / Engineering (sK710, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Net fees

- id: `kpi.accounting.net-fees`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Net fees measures that result inside Accounting, subcategory General. The unit is currency. The formula is A, where A is Net fees. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Net fees on the desired side of its target for this period?

Inputs:

- `metric.net-fees` (Net fees)

Placements:

- organizational / functional / Accounting / General (aK713, page_0158)
- organizational / functional / Accounting / Business Consulting (#K713, page_0158)
- organizational / industries / Accounting / Engineering (sK713, page_0159)
- organizational / industries / Media / Recruitment/Employment Activities (sK4713, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Net fees per FTE

- id: `kpi.accounting.net-fees-per-fte`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Net fees per FTE measures that result inside Accounting, subcategory General. The unit is currency. The formula is A / B, where A is Net fees, B is FTE. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Net fees per FTE on the desired side of its target for this period?

Inputs:

- `metric.net-fees` (Net fees)
- `metric.fte` (FTE)

Placements:

- organizational / functional / Accounting / General (aK714, page_0158)
- organizational / functional / Accounting / Business Consulting (#K714, page_0158)
- organizational / functional / Accounting / Business Consulting (#K715, page_0158)
- organizational / industries / Accounting / Engineering (sK714, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Travel time from chargeable time

- id: `kpi.accounting.travel-time-from-chargeable-time`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Travel time from chargeable time measures that result inside Accounting, subcategory General. The unit is currency. The formula is A, where A is Travel time from chargeable time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Travel time from chargeable time on the desired side of its target for this period?

Inputs:

- `metric.travel-time-from-chargeable-time` (Travel time from chargeable time)

Placements:

- organizational / functional / Accounting / General (aK6764, page_0158)
- organizational / functional / Accounting / Business Consulting (#K764, page_0158)
- organizational / industries / Accounting / Engineering (sK766, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Chargesave ratio

- id: `kpi.accounting.chargesave-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Chargesave ratio measures that result inside Accounting, subcategory Business Consulting. The unit is percent. The formula is (A / B) * 100, where A is numerator of Chargesave ratio, B is base of Chargesave ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Chargesave ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-chargesave-ratio` (numerator of Chargesave ratio)
- `metric.base-of-chargesave-ratio` (base of Chargesave ratio)

Placements:

- organizational / functional / Accounting / Business Consulting (#K194, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employee utilisation rate

- id: `kpi.accounting.employee-utilisation-rate`
- kind: kpi
- unit: percent
- direction: corridor
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employee utilisation rate measures that result inside Accounting, subcategory Business Consulting. The unit is percent. The formula is (A / B) * 100, where A is numerator of Employee utilisation rate, B is base of Employee utilisation rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employee utilisation rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-employee-utilisation-rate` (numerator of Employee utilisation rate)
- `metric.base-of-employee-utilisation-rate` (base of Employee utilisation rate)

Placements:

- organizational / functional / Accounting / Business Consulting (#K320, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Realization rate

- id: `kpi.accounting.realization-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Realization rate measures that result inside Accounting, subcategory Business Consulting. The unit is percent. The formula is (A / B) * 100, where A is numerator of Realization rate, B is base of Realization rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Realization rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-realization-rate` (numerator of Realization rate)
- `metric.base-of-realization-rate` (base of Realization rate)

Placements:

- organizational / functional / Accounting / Business Consulting (#K321, page_0158)
- organizational / industries / Accounting / Engineering (sK321, page_0159)
- organizational / industries / Media / Recruitment/Employment Activities (sK141, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Consultants generating revenue

- id: `kpi.accounting.consultants-generating-revenue`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Consultants generating revenue measures that result inside Accounting, subcategory Business Consulting. The unit is percent. The formula is (A / B) * 100, where A is part named by Consultants generating revenue, B is whole named by Consultants generating revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Consultants generating revenue on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-consultants-generating-revenue` (part named by Consultants generating revenue)
- `metric.whole-named-by-consultants-generating-revenue` (whole named by Consultants generating revenue)

Placements:

- organizational / functional / Accounting / Business Consulting (#K318, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Consulting hours generating revenue

- id: `kpi.accounting.consulting-hours-generating-revenue`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Consulting hours generating revenue measures that result inside Accounting, subcategory Business Consulting. The unit is percent. The formula is (A / B) * 100, where A is part named by Consulting hours generating revenue, B is whole named by Consulting hours generating revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Consulting hours generating revenue on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-consulting-hours-generating-revenue` (part named by Consulting hours generating revenue)
- `metric.whole-named-by-consulting-hours-generating-revenue` (whole named by Consulting hours generating revenue)

Placements:

- organizational / functional / Accounting / Business Consulting (#K419, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Load costs

- id: `kpi.accounting.load-costs`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Load costs measures that result inside Accounting, subcategory Business Consulting. The unit is currency. The formula is A, where A is Load costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Load costs on the desired side of its target for this period?

Inputs:

- `metric.load-costs` (Load costs)

Placements:

- organizational / functional / Accounting / Business Consulting (#K652, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Seminar & collateral materials costs

- id: `kpi.accounting.seminar-and-collateral-materials-costs`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Seminar & collateral materials costs measures that result inside Accounting, subcategory Business Consulting. The unit is currency. The formula is A, where A is Seminar & collateral materials costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Seminar & collateral materials costs on the desired side of its target for this period?

Inputs:

- `metric.seminar-and-collateral-materials-costs` (Seminar & collateral materials costs)

Placements:

- organizational / functional / Accounting / Business Consulting (#K653, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Architecture to schedule estimate

- id: `kpi.accounting.architecture-to-schedule-estimate`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Architecture to schedule estimate measures that result inside Accounting, subcategory Business Consulting. The unit is count. The formula is A, where A is Architecture to schedule estimate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Architecture to schedule estimate on the desired side of its target for this period?

Inputs:

- `metric.architecture-to-schedule-estimate` (Architecture to schedule estimate)

Placements:

- organizational / functional / Accounting / Business Consulting (#K654, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Project cost management

- id: `kpi.accounting.project-cost-management`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Project cost management measures that result inside Accounting, subcategory Business Consulting. The unit is count. The formula is A, where A is Project cost management. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Project cost management on the desired side of its target for this period?

Inputs:

- `metric.project-cost-management` (Project cost management)

Placements:

- organizational / functional / Accounting / Business Consulting (#K656, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Budgeted time against actual time

- id: `kpi.accounting.budgeted-time-against-actual-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Budgeted time against actual time measures that result inside Accounting, subcategory Business Consulting. The unit is count. The formula is A, where A is Budgeted time against actual time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Budgeted time against actual time on the desired side of its target for this period?

Inputs:

- `metric.budgeted-time-against-actual-time` (Budgeted time against actual time)

Placements:

- organizational / functional / Accounting / Business Consulting (#K665, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Solution revenue

- id: `kpi.accounting.solution-revenue`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Solution revenue measures that result inside Accounting, subcategory Business Consulting. The unit is count. The formula is A, where A is Solution revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Solution revenue on the desired side of its target for this period?

Inputs:

- `metric.solution-revenue` (Solution revenue)

Placements:

- organizational / functional / Accounting / Business Consulting (#K666, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Services revenue

- id: `kpi.accounting.services-revenue`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Services revenue measures that result inside Accounting, subcategory Business Consulting. The unit is count. The formula is A, where A is Services revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Services revenue on the desired side of its target for this period?

Inputs:

- `metric.services-revenue` (Services revenue)

Placements:

- organizational / functional / Accounting / Business Consulting (#K667, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Changeable work non recoverable

- id: `kpi.accounting.changeable-work-non-recoverable`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Changeable work non recoverable measures that result inside Accounting, subcategory Business Consulting. The unit is count. The formula is A, where A is Changeable work non recoverable. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Changeable work non recoverable on the desired side of its target for this period?

Inputs:

- `metric.changeable-work-non-recoverable` (Changeable work non recoverable)

Placements:

- organizational / functional / Accounting / Business Consulting (#K669, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Solution margin

- id: `kpi.accounting.solution-margin`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Solution margin measures that result inside Accounting, subcategory Business Consulting. The unit is count. The formula is (A / B) * 100, where A is Solution profit, B is revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Solution margin on the desired side of its target for this period?

Inputs:

- `metric.solution-profit` (Solution profit)
- `metric.revenue` (revenue)

Placements:

- organizational / functional / Accounting / Business Consulting (#K670, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Labor multiple

- id: `kpi.accounting.labor-multiple`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Labor multiple measures that result inside Accounting, subcategory Business Consulting. The unit is count. The formula is A, where A is Labor multiple. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Labor multiple on the desired side of its target for this period?

Inputs:

- `metric.labor-multiple` (Labor multiple)

Placements:

- organizational / functional / Accounting / Business Consulting (#K672, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Researches and preparation from chargeable time

- id: `kpi.accounting.researches-and-preparation-from-chargeable-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Researches and preparation from chargeable time measures that result inside Accounting, subcategory Business Consulting. The unit is count. The formula is A, where A is Researches and preparation from chargeable time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Researches and preparation from chargeable time on the desired side of its target for this period?

Inputs:

- `metric.researches-and-preparation-from-chargeable-time` (Researches and preparation from chargeable time)

Placements:

- organizational / functional / Accounting / Business Consulting (#K763, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Days of consulting

- id: `kpi.accounting.days-of-consulting`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Days of consulting measures that result inside Accounting, subcategory Business Consulting. The unit is count. The formula is A, where A is Days of consulting. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Days of consulting on the desired side of its target for this period?

Inputs:

- `metric.days-of-consulting` (Days of consulting)

Placements:

- organizational / functional / Accounting / Business Consulting (#K766, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Consulting hours sold

- id: `kpi.accounting.consulting-hours-sold`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Consulting hours sold measures that result inside Accounting, subcategory Business Consulting. The unit is count. The formula is A, where A is Consulting hours sold. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Consulting hours sold on the desired side of its target for this period?

Inputs:

- `metric.consulting-hours-sold` (Consulting hours sold)

Placements:

- organizational / functional / Accounting / Business Consulting (#K779, page_0158)
- organizational / industries / Accounting / Engineering (sK779, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Active engagements

- id: `kpi.accounting.active-engagements`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Active engagements measures that result inside Accounting, subcategory Business Consulting. The unit is count. The formula is A, where A is Active engagements. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Active engagements on the desired side of its target for this period?

Inputs:

- `metric.active-engagements` (Active engagements)

Placements:

- organizational / functional / Accounting / Business Consulting (#K1450, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
