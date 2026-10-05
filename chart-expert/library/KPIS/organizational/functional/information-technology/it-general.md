# Information Technology / IT - General

Context: organizational. Group: functional. KPIs: 47.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Productivity lost due to infrastructure

- id: `kpi.human-resources.productivity-lost-due-to-infrastructure`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.efficiency-and-effectiveness`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Productivity lost due to infrastructure measures that result inside Human Resources, subcategory Efficiency and Effectiveness. The unit is percent. The formula is (A / B) * 100, where A is Productivity lost due, B is infrastructure. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Productivity lost due to infrastructure on the desired side of its target for this period?

Inputs:

- `metric.productivity-lost-due` (Productivity lost due)
- `metric.infrastructure` (infrastructure)

Placements:

- organizational / functional / Human Resources / Efficiency and Effectiveness (K86718, page_0022)
- organizational / functional / Information Technology / IT - General (sK6718, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S Cost per PC

- id: `kpi.information-technology.s-cost-per-pc`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

S Cost per PC measures that result inside Information Technology, subcategory IT - General. The unit is number. The formula is A / B, where A is S Cost, B is PC. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S Cost per PC on the desired side of its target for this period?

Inputs:

- `metric.s-cost` (S Cost)
- `metric.pc` (PC)

Placements:

- organizational / functional / Information Technology / IT - General (sK99, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Obstet # IT infrastructure

- id: `kpi.information-technology.obstet-it-infrastructure`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Obstet # IT infrastructure measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A, where A is Obstet # IT infrastructure. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Obstet # IT infrastructure on the desired side of its target for this period?

Inputs:

- `metric.obstet-it-infrastructure` (Obstet # IT infrastructure)

Placements:

- organizational / functional / Information Technology / IT - General (sK857, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### IT network equipment replacement time

- id: `kpi.information-technology.it-network-equipment-replacement-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

IT network equipment replacement time measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A, where A is IT network equipment replacement time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is IT network equipment replacement time on the desired side of its target for this period?

Inputs:

- `metric.it-network-equipment-replacement-time` (IT network equipment replacement time)

Placements:

- organizational / functional / Information Technology / IT - General (sK860, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Server connection time

- id: `kpi.information-technology.server-connection-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Server connection time measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A, where A is Server connection time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Server connection time on the desired side of its target for this period?

Inputs:

- `metric.server-connection-time` (Server connection time)

Placements:

- organizational / functional / Information Technology / IT - General (sK874, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### IT operations staff with advanced ITIL certification

- id: `kpi.information-technology.it-operations-staff-with-advanced-itil-certification`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

IT operations staff with advanced ITIL certification measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is numerator of IT operations staff with advanced ITIL certification, B is base of IT operations staff with advanced ITIL certification. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is IT operations staff with advanced ITIL certification on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-it-operations-staff-with-advanced-itil-certification` (numerator of IT operations staff with advanced ITIL certification)
- `metric.base-of-it-operations-staff-with-advanced-itil-certification` (base of IT operations staff with advanced ITIL certification)

Placements:

- organizational / functional / Information Technology / IT - General (sK1054, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### IT operations and ITIL aware

- id: `kpi.information-technology.it-operations-and-itil-aware`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

IT operations and ITIL aware measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is numerator of IT operations and ITIL aware, B is base of IT operations and ITIL aware. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is IT operations and ITIL aware on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-it-operations-and-itil-aware` (numerator of IT operations and ITIL aware)
- `metric.base-of-it-operations-and-itil-aware` (base of IT operations and ITIL aware)

Placements:

- organizational / functional / Information Technology / IT - General (sK1064, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Joint IT / business planning meetings held

- id: `kpi.information-technology.joint-it-business-planning-meetings-held`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Joint IT / business planning meetings held measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A, where A is Joint IT / business planning meetings held. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Joint IT / business planning meetings held on the desired side of its target for this period?

Inputs:

- `metric.joint-it-business-planning-meetings-held` (Joint IT / business planning meetings held)

Placements:

- organizational / functional / Information Technology / IT - General (sK1074, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### IT steering committee meetings held

- id: `kpi.information-technology.it-steering-committee-meetings-held`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

IT steering committee meetings held measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A, where A is IT steering committee meetings held. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is IT steering committee meetings held on the desired side of its target for this period?

Inputs:

- `metric.it-steering-committee-meetings-held` (IT steering committee meetings held)

Placements:

- organizational / functional / Information Technology / IT - General (sK1097, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Timeline for regulatory compliance to new IT regulatory requirements

- id: `kpi.information-technology.timeline-for-regulatory-compliance-to-new-it-regulatory-requirements`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Timeline for regulatory compliance to new IT regulatory requirements measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A, where A is Timeline for regulatory compliance to new IT regulatory requirements. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Timeline for regulatory compliance to new IT regulatory requirements on the desired side of its target for this period?

Inputs:

- `metric.timeline-for-regulatory-compliance-to-new-it-regulatory-requirements` (Timeline for regulatory compliance to new IT regulatory requirements)

Placements:

- organizational / functional / Information Technology / IT - General (sK1152, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### IT budget spend on service delivery

- id: `kpi.information-technology.it-budget-spend-on-service-delivery`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

IT budget spend on service delivery measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is part named by IT budget spend on service delivery, B is whole named by IT budget spend on service delivery. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is IT budget spend on service delivery on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-it-budget-spend-on-service-delivery` (part named by IT budget spend on service delivery)
- `metric.whole-named-by-it-budget-spend-on-service-delivery` (whole named by IT budget spend on service delivery)

Placements:

- organizational / functional / Information Technology / IT - General (sK1169, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Maintenance cost per application

- id: `kpi.information-technology.maintenance-cost-per-application`
- kind: kpi
- unit: count
- direction: down
- timing: leading
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Maintenance cost per application measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A / B, where A is Maintenance cost, B is application. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Maintenance cost per application on the desired side of its target for this period?

Inputs:

- `metric.maintenance-cost` (Maintenance cost)
- `metric.application` (application)

Placements:

- organizational / functional / Information Technology / IT - General (sK1162, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### IT spending per employee

- id: `kpi.information-technology.it-spending-per-employee`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

IT spending per employee measures that result inside Information Technology, subcategory IT - General. The unit is currency. The formula is A / B, where A is IT spending, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is IT spending per employee on the desired side of its target for this period?

Inputs:

- `metric.it-spending` (IT spending)
- `metric.employee` (employee)

Placements:

- organizational / functional / Information Technology / IT - General (sK124, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time dedicated to creative IT activities

- id: `kpi.information-technology.time-dedicated-to-creative-it-activities`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Time dedicated to creative IT activities measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is Time dedicated, B is creative IT activities. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time dedicated to creative IT activities on the desired side of its target for this period?

Inputs:

- `metric.time-dedicated` (Time dedicated)
- `metric.creative-it-activities` (creative IT activities)

Placements:

- organizational / functional / Information Technology / IT - General (sK1266, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### IT spending for IT maintenance

- id: `kpi.information-technology.it-spending-for-it-maintenance`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

IT spending for IT maintenance measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is part named by IT spending for IT maintenance, B is whole named by IT spending for IT maintenance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is IT spending for IT maintenance on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-it-spending-for-it-maintenance` (part named by IT spending for IT maintenance)
- `metric.whole-named-by-it-spending-for-it-maintenance` (whole named by IT spending for IT maintenance)

Placements:

- organizational / functional / Information Technology / IT - General (sK127, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### IT spending per customer

- id: `kpi.information-technology.it-spending-per-customer`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

IT spending per customer measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A / B, where A is IT spending, B is customer. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is IT spending per customer on the desired side of its target for this period?

Inputs:

- `metric.it-spending` (IT spending)
- `metric.customer` (customer)

Placements:

- organizational / functional / Information Technology / IT - General (sK129, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### IT budget from total company revenues

- id: `kpi.information-technology.it-budget-from-total-company-revenues`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

IT budget from total company revenues measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is IT budget, B is total company revenues. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is IT budget from total company revenues on the desired side of its target for this period?

Inputs:

- `metric.it-budget` (IT budget)
- `metric.total-company-revenues` (total company revenues)

Placements:

- organizational / functional / Information Technology / IT - General (sK1210, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### IT capital spending

- id: `kpi.information-technology.it-capital-spending`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

IT capital spending measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is part named by IT capital spending, B is whole named by IT capital spending. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is IT capital spending on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-it-capital-spending` (part named by IT capital spending)
- `metric.whole-named-by-it-capital-spending` (whole named by IT capital spending)

Placements:

- organizational / functional / Information Technology / IT - General (sK1211, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### IT work outsourced

- id: `kpi.information-technology.it-work-outsourced`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

IT work outsourced measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is part named by IT work outsourced, B is whole named by IT work outsourced. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is IT work outsourced on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-it-work-outsourced` (part named by IT work outsourced)
- `metric.whole-named-by-it-work-outsourced` (whole named by IT work outsourced)

Placements:

- organizational / functional / Information Technology / IT - General (sK1214, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Strategic business initiatives driven by IT

- id: `kpi.information-technology.strategic-business-initiatives-driven-by-it`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Strategic business initiatives driven by IT measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is numerator of Strategic business initiatives driven by IT, B is base of Strategic business initiatives driven by IT. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Strategic business initiatives driven by IT on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-strategic-business-initiatives-driven-by-it` (numerator of Strategic business initiatives driven by IT)
- `metric.base-of-strategic-business-initiatives-driven-by-it` (base of Strategic business initiatives driven by IT)

Placements:

- organizational / functional / Information Technology / IT - General (sK1215, page_0030)
- organizational / functional / Management / General (#K1215, page_0045)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### IT budget growth

- id: `kpi.information-technology.it-budget-growth`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

IT budget growth measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is part named by IT budget growth, B is whole named by IT budget growth. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is IT budget growth on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-it-budget-growth` (part named by IT budget growth)
- `metric.whole-named-by-it-budget-growth` (whole named by IT budget growth)

Placements:

- organizational / functional / Information Technology / IT - General (sK1216, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Critical business processes not covered by a defined service availability plan

- id: `kpi.information-technology.critical-business-processes-not-covered-by-a-defined-service-availabilit`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Critical business processes not covered by a defined service availability plan measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is part named by Critical business processes not covered by a defined service availability plan, B is whole named by Critical business processes not covered by a defined service availability plan. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Critical business processes not covered by a defined service availability plan on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-critical-business-processes-not-covered-by-a-defined-servi` (part named by Critical business processes not covered by a defined service availability plan)
- `metric.whole-named-by-critical-business-processes-not-covered-by-a-defined-serv` (whole named by Critical business processes not covered by a defined service availability plan)

Placements:

- organizational / functional / Information Technology / IT - General (sK1227, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### IT budget spent on risk management

- id: `kpi.information-technology.it-budget-spent-on-risk-management`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

IT budget spent on risk management measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is part named by IT budget spent on risk management, B is whole named by IT budget spent on risk management. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is IT budget spent on risk management on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-it-budget-spent-on-risk-management` (part named by IT budget spent on risk management)
- `metric.whole-named-by-it-budget-spent-on-risk-management` (whole named by IT budget spent on risk management)

Placements:

- organizational / functional / Information Technology / IT - General (sK1234, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### IT service bills paid by business management

- id: `kpi.information-technology.it-service-bills-paid-by-business-management`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

IT service bills paid by business management measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is part named by IT service bills paid by business management, B is whole named by IT service bills paid by business management. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is IT service bills paid by business management on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-it-service-bills-paid-by-business-management` (part named by IT service bills paid by business management)
- `metric.whole-named-by-it-service-bills-paid-by-business-management` (whole named by IT service bills paid by business management)

Placements:

- organizational / functional / Information Technology / IT - General (sK1245, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Frequency of IT reporting to the board

- id: `kpi.information-technology.frequency-of-it-reporting-to-the-board`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Frequency of IT reporting to the board measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A, where A is Frequency of IT reporting to the board. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Frequency of IT reporting to the board on the desired side of its target for this period?

Inputs:

- `metric.frequency-of-it-reporting-to-the-board` (Frequency of IT reporting to the board)

Placements:

- organizational / functional / Information Technology / IT - General (sK1251, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Frequency of review of the IT risk management process

- id: `kpi.information-technology.frequency-of-review-of-the-it-risk-management-process`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Frequency of review of the IT risk management process measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A, where A is Frequency of review of the IT risk management process. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Frequency of review of the IT risk management process on the desired side of its target for this period?

Inputs:

- `metric.frequency-of-review-of-the-it-risk-management-process` (Frequency of review of the IT risk management process)

Placements:

- organizational / functional / Information Technology / IT - General (sK1253, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Spending of current technology capital budget

- id: `kpi.information-technology.spending-of-current-technology-capital-budget`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Spending of current technology capital budget measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is Spending, B is current technology capital budget. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Spending of current technology capital budget on the desired side of its target for this period?

Inputs:

- `metric.spending` (Spending)
- `metric.current-technology-capital-budget` (current technology capital budget)

Placements:

- organizational / functional / Information Technology / IT - General (sK1261, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Spam fitting cost per email mailbox

- id: `kpi.information-technology.spam-fitting-cost-per-email-mailbox`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Spam fitting cost per email mailbox measures that result inside Information Technology, subcategory IT - General. The unit is currency. The formula is A / B, where A is Spam fitting cost, B is email mailbox. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Spam fitting cost per email mailbox on the desired side of its target for this period?

Inputs:

- `metric.spam-fitting-cost` (Spam fitting cost)
- `metric.email-mailbox` (email mailbox)

Placements:

- organizational / functional / Information Technology / IT - General (sK1271, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost per available treaty

- id: `kpi.information-technology.cost-per-available-treaty`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Cost per available treaty measures that result inside Information Technology, subcategory IT - General. The unit is currency. The formula is A / B, where A is Cost, B is available treaty. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost per available treaty on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.available-treaty` (available treaty)

Placements:

- organizational / functional / Information Technology / IT - General (sK1274, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost per stored treaty

- id: `kpi.information-technology.cost-per-stored-treaty`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Cost per stored treaty measures that result inside Information Technology, subcategory IT - General. The unit is currency. The formula is A / B, where A is Cost, B is stored treaty. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost per stored treaty on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.stored-treaty` (stored treaty)

Placements:

- organizational / functional / Information Technology / IT - General (sK1275, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Expenditure with financial system

- id: `kpi.information-technology.expenditure-with-financial-system`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Expenditure with financial system measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is part named by Expenditure with financial system, B is whole named by Expenditure with financial system. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Expenditure with financial system on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-expenditure-with-financial-system` (part named by Expenditure with financial system)
- `metric.whole-named-by-expenditure-with-financial-system` (whole named by Expenditure with financial system)

Placements:

- organizational / functional / Information Technology / IT - General (sK1295, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Affected users by IT infrastructure incidents

- id: `kpi.information-technology.affected-users-by-it-infrastructure-incidents`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Affected users by IT infrastructure incidents measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A, where A is Affected users by IT infrastructure incidents. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Affected users by IT infrastructure incidents on the desired side of its target for this period?

Inputs:

- `metric.affected-users-by-it-infrastructure-incidents` (Affected users by IT infrastructure incidents)

Placements:

- organizational / functional / Information Technology / IT - General (sK4612, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Spam login time

- id: `kpi.information-technology.spam-login-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Spam login time measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is part named by Spam login time, B is whole named by Spam login time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Spam login time on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-spam-login-time` (part named by Spam login time)
- `metric.whole-named-by-spam-login-time` (whole named by Spam login time)

Placements:

- organizational / functional / Information Technology / IT - General (sK4626, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Peak infrastructure utilization

- id: `kpi.information-technology.peak-infrastructure-utilization`
- kind: kpi
- unit: percent
- direction: corridor
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Peak infrastructure utilization measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is part named by Peak infrastructure utilization, B is whole named by Peak infrastructure utilization. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Peak infrastructure utilization on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-peak-infrastructure-utilization` (part named by Peak infrastructure utilization)
- `metric.whole-named-by-peak-infrastructure-utilization` (whole named by Peak infrastructure utilization)

Placements:

- organizational / functional / Information Technology / IT - General (sK4627, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Disk utilization

- id: `kpi.information-technology.disk-utilization`
- kind: kpi
- unit: percent
- direction: corridor
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Disk utilization measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is part named by Disk utilization, B is whole named by Disk utilization. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Disk utilization on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-disk-utilization` (part named by Disk utilization)
- `metric.whole-named-by-disk-utilization` (whole named by Disk utilization)

Placements:

- organizational / functional / Information Technology / IT - General (sK4628, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### IT Infrastructure changes completed

- id: `kpi.information-technology.it-infrastructure-changes-completed`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

IT Infrastructure changes completed measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A, where A is IT Infrastructure changes completed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is IT Infrastructure changes completed on the desired side of its target for this period?

Inputs:

- `metric.it-infrastructure-changes-completed` (IT Infrastructure changes completed)

Placements:

- organizational / functional / Information Technology / IT - General (sK4633, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### IT infrastructure change success rate

- id: `kpi.information-technology.it-infrastructure-change-success-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

IT infrastructure change success rate measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is numerator of IT infrastructure change success rate, B is base of IT infrastructure change success rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is IT infrastructure change success rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-it-infrastructure-change-success-rate` (numerator of IT infrastructure change success rate)
- `metric.base-of-it-infrastructure-change-success-rate` (base of IT infrastructure change success rate)

Placements:

- organizational / functional / Information Technology / IT - General (sK4634, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cases derived using the new technology

- id: `kpi.information-technology.cases-derived-using-the-new-technology`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Cases derived using the new technology measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A, where A is Cases derived using the new technology. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cases derived using the new technology on the desired side of its target for this period?

Inputs:

- `metric.cases-derived-using-the-new-technology` (Cases derived using the new technology)

Placements:

- organizational / functional / Information Technology / IT - General (sK6025, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Automated information exchanges in use

- id: `kpi.information-technology.automated-information-exchanges-in-use`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Automated information exchanges in use measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A, where A is Automated information exchanges in use. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Automated information exchanges in use on the desired side of its target for this period?

Inputs:

- `metric.automated-information-exchanges-in-use` (Automated information exchanges in use)

Placements:

- organizational / functional / Information Technology / IT - General (sK6026, page_0030)
- organizational / industries / Sport / Organizational » Industries (&K5026, page_0106)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Case dispositions recorded in repository

- id: `kpi.information-technology.case-dispositions-recorded-in-repository`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Case dispositions recorded in repository measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is part named by Case dispositions recorded in repository, B is whole named by Case dispositions recorded in repository. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Case dispositions recorded in repository on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-case-dispositions-recorded-in-repository` (part named by Case dispositions recorded in repository)
- `metric.whole-named-by-case-dispositions-recorded-in-repository` (whole named by Case dispositions recorded in repository)

Placements:

- organizational / functional / Information Technology / IT - General (sK6028, page_0030)
- organizational / industries / Sport / Organizational » Industries (&K5028, page_0106)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Personnel who log on to a Court Management System

- id: `kpi.information-technology.personnel-who-log-on-to-a-court-management-system`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Personnel who log on to a Court Management System measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is Personnel who log on, B is a Court Management System. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Personnel who log on to a Court Management System on the desired side of its target for this period?

Inputs:

- `metric.personnel-who-log-on` (Personnel who log on)
- `metric.a-court-management-system` (a Court Management System)

Placements:

- organizational / functional / Information Technology / IT - General (sK6042, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### modified each day

- id: `kpi.information-technology.modified-each-day`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

modified each day measures that result inside Information Technology, subcategory IT - General. The unit is number. The formula is A, where A is modified each day. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is modified each day on the desired side of its target for this period?

Inputs:

- `metric.modified-each-day` (modified each day)

Placements:

- organizational / functional / Information Technology / IT - General (sK6014, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Age of PC

- id: `kpi.information-technology.age-of-pc`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Age of PC measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A, where A is Age of PC. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Age of PC on the desired side of its target for this period?

Inputs:

- `metric.age-of-pc` (Age of PC)

Placements:

- organizational / functional / Information Technology / IT - General (sK6924, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Handheld devices in the enterprise

- id: `kpi.information-technology.handheld-devices-in-the-enterprise`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Handheld devices in the enterprise measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A, where A is Handheld devices in the enterprise. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Handheld devices in the enterprise on the desired side of its target for this period?

Inputs:

- `metric.handheld-devices-in-the-enterprise` (Handheld devices in the enterprise)

Placements:

- organizational / functional / Information Technology / IT - General (sK6945, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Laptop rollups to address stability issues

- id: `kpi.information-technology.laptop-rollups-to-address-stability-issues`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.information-technology.it-general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Laptop rollups to address stability issues measures that result inside Information Technology, subcategory IT - General. The unit is percent. The formula is (A / B) * 100, where A is Laptop rollups, B is address stability issues. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Laptop rollups to address stability issues on the desired side of its target for this period?

Inputs:

- `metric.laptop-rollups` (Laptop rollups)
- `metric.address-stability-issues` (address stability issues)

Placements:

- organizational / functional / Information Technology / IT - General (sK6944, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Laptop to desktop ratio

- id: `kpi.information-technology.laptop-to-desktop-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Laptop to desktop ratio measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A, where A is Laptop to desktop ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Laptop to desktop ratio on the desired side of its target for this period?

Inputs:

- `metric.laptop-to-desktop-ratio` (Laptop to desktop ratio)

Placements:

- organizational / functional / Information Technology / IT - General (sK6947, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Desktop and roley lip services performed during the quarter

- id: `kpi.information-technology.desktop-and-roley-lip-services-performed-during-the-quarter`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.it-general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Desktop and roley lip services performed during the quarter measures that result inside Information Technology, subcategory IT - General. The unit is count. The formula is A, where A is Desktop and roley lip services performed during the quarter. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Desktop and roley lip services performed during the quarter on the desired side of its target for this period?

Inputs:

- `metric.desktop-and-roley-lip-services-performed-during-the-quarter` (Desktop and roley lip services performed during the quarter)

Placements:

- organizational / functional / Information Technology / IT - General (sK1409, page_0030)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
