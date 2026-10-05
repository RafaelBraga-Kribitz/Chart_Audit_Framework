# Infrastructure / Roads

Context: organizational. Group: industries. KPIs: 45.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Bicycle lane length installed

- id: `kpi.administration.bicycle-lane-length-installed`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Bicycle lane length installed measures that result inside Administration, subcategory Organizational » industries. The unit is count. The formula is A, where A is Bicycle lane length installed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Bicycle lane length installed on the desired side of its target for this period?

Inputs:

- `metric.bicycle-lane-length-installed` (Bicycle lane length installed)

Placements:

- organizational / industries / Administration / Organizational » industries (sK512, page_0094)
- organizational / industries / Infrastructure / Roads (kR5512, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Road user charge collected

- id: `kpi.finance.road-user-charge-collected`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.finance.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Road user charge collected measures that result inside Finance, subcategory Organizational = Industries. The unit is count. The formula is A, where A is Road user charge collected. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Road user charge collected on the desired side of its target for this period?

Inputs:

- `metric.road-user-charge-collected` (Road user charge collected)

Placements:

- organizational / industries / Finance / Organizational = Industries (sK3659, page_0102)
- organizational / industries / Infrastructure / Roads (kR2659, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time freeways operate above capacity

- id: `kpi.transportation-and-infrastructure.time-freeways-operate-above-capacity`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation-and-infrastructure.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time freeways operate above capacity measures that result inside Transportation and Infrastructure, subcategory General. The unit is count. The formula is A, where A is Time freeways operate above capacity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time freeways operate above capacity on the desired side of its target for this period?

Inputs:

- `metric.time-freeways-operate-above-capacity` (Time freeways operate above capacity)

Placements:

- global / human-development / Transportation and Infrastructure / General (sK5318, page_0109)
- organizational / industries / Infrastructure / Roads (kR5318, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of highway maintenance per 100 miles traveled by a vehicle

- id: `kpi.transportation-and-infrastructure.cost-of-highway-maintenance-per-100-miles-traveled-by-a-vehicle`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation-and-infrastructure.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of highway maintenance per 100 miles traveled by a vehicle measures that result inside Transportation and Infrastructure, subcategory General. The unit is currency. The formula is A / B, where A is Cost of highway maintenance, B is 100 miles traveled by a vehicle. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of highway maintenance per 100 miles traveled by a vehicle on the desired side of its target for this period?

Inputs:

- `metric.cost-of-highway-maintenance` (Cost of highway maintenance)
- `metric.100-miles-traveled-by-a-vehicle` (100 miles traveled by a vehicle)

Placements:

- global / human-development / Transportation and Infrastructure / General (sK5432, page_0109)
- organizational / industries / Infrastructure / Roads (kR5432, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of snow removal

- id: `kpi.infrastructure.cost-of-snow-removal`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of snow removal measures that result inside Infrastructure, subcategory Organizational » Industries. The unit is currency. The formula is A, where A is Cost of snow removal. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of snow removal on the desired side of its target for this period?

Inputs:

- `metric.cost-of-snow-removal` (Cost of snow removal)

Placements:

- organizational / industries / Infrastructure / Organizational » Industries (sK6618, page_0134)
- organizational / industries / Infrastructure / Roads (kR6468, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of preventive maintenance

- id: `kpi.infrastructure.cost-of-preventive-maintenance`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of preventive maintenance measures that result inside Infrastructure, subcategory Organizational » Industries. The unit is currency. The formula is A, where A is Cost of preventive maintenance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of preventive maintenance on the desired side of its target for this period?

Inputs:

- `metric.cost-of-preventive-maintenance` (Cost of preventive maintenance)

Placements:

- organizational / industries / Infrastructure / Organizational » Industries (sK6619, page_0134)
- organizational / industries / Infrastructure / Railways (%R6469, page_0141)
- organizational / industries / Infrastructure / Roads (kR6469, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Daily utilized parking spaces

- id: `kpi.infrastructure.daily-utilized-parking-spaces`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Daily utilized parking spaces measures that result inside Infrastructure, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Daily utilized parking spaces. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Daily utilized parking spaces on the desired side of its target for this period?

Inputs:

- `metric.daily-utilized-parking-spaces` (Daily utilized parking spaces)

Placements:

- organizational / industries / Infrastructure / Organizational » Industries (sK6527, page_0134)
- organizational / industries / Infrastructure / Roads (kR6527, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Daily revenue per parking space

- id: `kpi.infrastructure.daily-revenue-per-parking-space`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.infrastructure.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Daily revenue per parking space measures that result inside Infrastructure, subcategory Organizational » Industries. The unit is count. The formula is A / B, where A is Daily revenue, B is parking space. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Daily revenue per parking space on the desired side of its target for this period?

Inputs:

- `metric.daily-revenue` (Daily revenue)
- `metric.parking-space` (parking space)

Placements:

- organizational / industries / Infrastructure / Organizational » Industries (sK6528, page_0134)
- organizational / industries / Infrastructure / Roads (kR6528, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Parking revenue per transaction

- id: `kpi.infrastructure.parking-revenue-per-transaction`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.infrastructure.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Parking revenue per transaction measures that result inside Infrastructure, subcategory Organizational » Industries. The unit is count. The formula is A / B, where A is Parking revenue, B is transaction. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Parking revenue per transaction on the desired side of its target for this period?

Inputs:

- `metric.parking-revenue` (Parking revenue)
- `metric.transaction` (transaction)

Placements:

- organizational / industries / Infrastructure / Organizational » Industries (sK6529, page_0134)
- organizational / industries / Infrastructure / Roads (kR6529, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of corrective maintenance

- id: `kpi.infrastructure.cost-of-corrective-maintenance`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of corrective maintenance measures that result inside Infrastructure, subcategory Organizational = Industries. The unit is currency. The formula is A, where A is Cost of corrective maintenance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of corrective maintenance on the desired side of its target for this period?

Inputs:

- `metric.cost-of-corrective-maintenance` (Cost of corrective maintenance)

Placements:

- organizational / industries / Infrastructure / Organizational = Industries (sK6469, page_0138)
- organizational / industries / Infrastructure / Roads (kR6470, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Traffic lights

- id: `kpi.infrastructure.traffic-lights`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.railways`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Traffic lights measures that result inside Infrastructure, subcategory Railways. The unit is number. The formula is A, where A is Traffic lights. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Traffic lights on the desired side of its target for this period?

Inputs:

- `metric.traffic-lights` (Traffic lights)

Placements:

- organizational / industries / Infrastructure / Railways (%R352f, page_0141)
- organizational / industries / Infrastructure / Roads (kR2637, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Pollutant emissions

- id: `kpi.infrastructure.pollutant-emissions`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.railways`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Pollutant emissions measures that result inside Infrastructure, subcategory Railways. The unit is number. The formula is A, where A is Pollutant emissions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Pollutant emissions on the desired side of its target for this period?

Inputs:

- `metric.pollutant-emissions` (Pollutant emissions)

Placements:

- organizational / industries / Infrastructure / Railways (%R572, page_0141)
- organizational / industries / Infrastructure / Roads (kR2972, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Planned maintenance and repair programs completed to install

- id: `kpi.infrastructure.planned-maintenance-and-repair-programs-completed-to-install`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.infrastructure.roads`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Planned maintenance and repair programs completed to install measures that result inside Infrastructure, subcategory Roads. The unit is percent. The formula is (A / B) * 100, where A is Planned maintenance and repair programs completed, B is install. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Planned maintenance and repair programs completed to install on the desired side of its target for this period?

Inputs:

- `metric.planned-maintenance-and-repair-programs-completed` (Planned maintenance and repair programs completed)
- `metric.install` (install)

Placements:

- organizational / industries / Infrastructure / Roads (kR327, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Asphalt surfacing projects with defects within 3 years of completion

- id: `kpi.infrastructure.asphalt-surfacing-projects-with-defects-within-3-years-of-completion`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.infrastructure.roads`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Asphalt surfacing projects with defects within 3 years of completion measures that result inside Infrastructure, subcategory Roads. The unit is percent. The formula is (A / B) * 100, where A is Asphalt surfacing projects with defects within 3 years, B is completion. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Asphalt surfacing projects with defects within 3 years of completion on the desired side of its target for this period?

Inputs:

- `metric.asphalt-surfacing-projects-with-defects-within-3-years` (Asphalt surfacing projects with defects within 3 years)
- `metric.completion` (completion)

Placements:

- organizational / industries / Infrastructure / Roads (kR328, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Major road network covered by controlled traffic management system

- id: `kpi.infrastructure.major-road-network-covered-by-controlled-traffic-management-system`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.infrastructure.roads`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Major road network covered by controlled traffic management system measures that result inside Infrastructure, subcategory Roads. The unit is percent. The formula is (A / B) * 100, where A is part named by Major road network covered by controlled traffic management system, B is whole named by Major road network covered by controlled traffic management system. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Major road network covered by controlled traffic management system on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-major-road-network-covered-by-controlled-traffic-managemen` (part named by Major road network covered by controlled traffic management system)
- `metric.whole-named-by-major-road-network-covered-by-controlled-traffic-manageme` (whole named by Major road network covered by controlled traffic management system)

Placements:

- organizational / industries / Infrastructure / Roads (kR3631, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Road network length

- id: `kpi.infrastructure.road-network-length`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Road network length measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Road network length. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Road network length on the desired side of its target for this period?

Inputs:

- `metric.road-network-length` (Road network length)

Placements:

- organizational / industries / Infrastructure / Roads (kR263, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Flyovers

- id: `kpi.infrastructure.flyovers`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Flyovers measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Flyovers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Flyovers on the desired side of its target for this period?

Inputs:

- `metric.flyovers` (Flyovers)

Placements:

- organizational / industries / Infrastructure / Roads (kR2634, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Vehicular bridges

- id: `kpi.infrastructure.vehicular-bridges`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Vehicular bridges measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Vehicular bridges. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Vehicular bridges on the desired side of its target for this period?

Inputs:

- `metric.vehicular-bridges` (Vehicular bridges)

Placements:

- organizational / industries / Infrastructure / Roads (kR2635, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Vehicle underpasses

- id: `kpi.infrastructure.vehicle-underpasses`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Vehicle underpasses measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Vehicle underpasses. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Vehicle underpasses on the desired side of its target for this period?

Inputs:

- `metric.vehicle-underpasses` (Vehicle underpasses)

Placements:

- organizational / industries / Infrastructure / Roads (kR2636, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Pedestrian overhead bridges

- id: `kpi.infrastructure.pedestrian-overhead-bridges`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Pedestrian overhead bridges measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Pedestrian overhead bridges. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Pedestrian overhead bridges on the desired side of its target for this period?

Inputs:

- `metric.pedestrian-overhead-bridges` (Pedestrian overhead bridges)

Placements:

- organizational / industries / Infrastructure / Roads (kR2638, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Pedestrian underpasses built

- id: `kpi.infrastructure.pedestrian-underpasses-built`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Pedestrian underpasses built measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Pedestrian underpasses built. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Pedestrian underpasses built on the desired side of its target for this period?

Inputs:

- `metric.pedestrian-underpasses-built` (Pedestrian underpasses built)

Placements:

- organizational / industries / Infrastructure / Roads (kR2639, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Footbridge under administration

- id: `kpi.infrastructure.footbridge-under-administration`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Footbridge under administration measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Footbridge under administration. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Footbridge under administration on the desired side of its target for this period?

Inputs:

- `metric.footbridge-under-administration` (Footbridge under administration)

Placements:

- organizational / industries / Infrastructure / Roads (kR2640, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Public street lights

- id: `kpi.infrastructure.public-street-lights`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Public street lights measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Public street lights. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Public street lights on the desired side of its target for this period?

Inputs:

- `metric.public-street-lights` (Public street lights)

Placements:

- organizational / industries / Infrastructure / Roads (kR2642, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Area lane teleometers of freeway 100 population

- id: `kpi.infrastructure.area-lane-teleometers-of-freeway-100-population`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Area lane teleometers of freeway 100 population measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Area lane teleometers of freeway 100 population. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Area lane teleometers of freeway 100 population on the desired side of its target for this period?

Inputs:

- `metric.area-lane-teleometers-of-freeway-100-population` (Area lane teleometers of freeway 100 population)

Placements:

- organizational / industries / Infrastructure / Roads (kR2644, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### City and town toll conditions

- id: `kpi.infrastructure.city-and-town-toll-conditions`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

City and town toll conditions measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is City and town toll conditions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is City and town toll conditions on the desired side of its target for this period?

Inputs:

- `metric.city-and-town-toll-conditions` (City and town toll conditions)

Placements:

- organizational / industries / Infrastructure / Roads (kR2646, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Speed driving peak hours

- id: `kpi.infrastructure.speed-driving-peak-hours`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Speed driving peak hours measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Speed driving peak hours. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Speed driving peak hours on the desired side of its target for this period?

Inputs:

- `metric.speed-driving-peak-hours` (Speed driving peak hours)

Placements:

- organizational / industries / Infrastructure / Roads (kR2697, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Distance between bus stops

- id: `kpi.infrastructure.distance-between-bus-stops`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Distance between bus stops measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Distance between bus stops. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Distance between bus stops on the desired side of its target for this period?

Inputs:

- `metric.distance-between-bus-stops` (Distance between bus stops)

Placements:

- organizational / industries / Infrastructure / Roads (kR2899, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost per lane mile resurfaced

- id: `kpi.infrastructure.cost-per-lane-mile-resurfaced`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost per lane mile resurfaced measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A / B, where A is Cost, B is lane mile resurfaced. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost per lane mile resurfaced on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.lane-mile-resurfaced` (lane mile resurfaced)

Placements:

- organizational / industries / Infrastructure / Roads (kR5513, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost per tonne of asphalt used

- id: `kpi.infrastructure.cost-per-tonne-of-asphalt-used`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost per tonne of asphalt used measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A / B, where A is Cost, B is tonne of asphalt used. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost per tonne of asphalt used on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.tonne-of-asphalt-used` (tonne of asphalt used)

Placements:

- organizational / industries / Infrastructure / Roads (kR5280, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Length of ranked bicycle paths

- id: `kpi.infrastructure.length-of-ranked-bicycle-paths`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Length of ranked bicycle paths measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Length of ranked bicycle paths. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Length of ranked bicycle paths on the desired side of its target for this period?

Inputs:

- `metric.length-of-ranked-bicycle-paths` (Length of ranked bicycle paths)

Placements:

- organizational / industries / Infrastructure / Roads (kR6531, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Delays caused by roadworks

- id: `kpi.infrastructure.delays-caused-by-roadworks`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Delays caused by roadworks measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Delays caused by roadworks. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Delays caused by roadworks on the desired side of its target for this period?

Inputs:

- `metric.delays-caused-by-roadworks` (Delays caused by roadworks)

Placements:

- organizational / industries / Infrastructure / Roads (kR6533, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Delays causing by traffic volume

- id: `kpi.infrastructure.delays-causing-by-traffic-volume`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Delays causing by traffic volume measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Delays causing by traffic volume. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Delays causing by traffic volume on the desired side of its target for this period?

Inputs:

- `metric.delays-causing-by-traffic-volume` (Delays causing by traffic volume)

Placements:

- organizational / industries / Infrastructure / Roads (kR6534, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Length of traffic congestion

- id: `kpi.infrastructure.length-of-traffic-congestion`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Length of traffic congestion measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Length of traffic congestion. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Length of traffic congestion on the desired side of its target for this period?

Inputs:

- `metric.length-of-traffic-congestion` (Length of traffic congestion)

Placements:

- organizational / industries / Infrastructure / Roads (kR6535, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Duration of traffic congestion

- id: `kpi.infrastructure.duration-of-traffic-congestion`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Duration of traffic congestion measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Duration of traffic congestion. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Duration of traffic congestion on the desired side of its target for this period?

Inputs:

- `metric.duration-of-traffic-congestion` (Duration of traffic congestion)

Placements:

- organizational / industries / Infrastructure / Roads (kR6536, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Road defects reported and repaired within 4 hours

- id: `kpi.infrastructure.road-defects-reported-and-repaired-within-4-hours`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Road defects reported and repaired within 4 hours measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Road defects reported and repaired within 4 hours. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Road defects reported and repaired within 4 hours on the desired side of its target for this period?

Inputs:

- `metric.road-defects-reported-and-repaired-within-4-hours` (Road defects reported and repaired within 4 hours)

Placements:

- organizational / industries / Infrastructure / Roads (kR6537, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Road inspections carried out within established frequency

- id: `kpi.infrastructure.road-inspections-carried-out-within-established-frequency`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Road inspections carried out within established frequency measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Road inspections carried out within established frequency. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Road inspections carried out within established frequency on the desired side of its target for this period?

Inputs:

- `metric.road-inspections-carried-out-within-established-frequency` (Road inspections carried out within established frequency)

Placements:

- organizational / industries / Infrastructure / Roads (kR6538, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Road network where maintenance work should be considered

- id: `kpi.infrastructure.road-network-where-maintenance-work-should-be-considered`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Road network where maintenance work should be considered measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Road network where maintenance work should be considered. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Road network where maintenance work should be considered on the desired side of its target for this period?

Inputs:

- `metric.road-network-where-maintenance-work-should-be-considered` (Road network where maintenance work should be considered)

Placements:

- organizational / industries / Infrastructure / Roads (kR6539, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Street lights in working order

- id: `kpi.infrastructure.street-lights-in-working-order`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Street lights in working order measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Street lights in working order. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Street lights in working order on the desired side of its target for this period?

Inputs:

- `metric.street-lights-in-working-order` (Street lights in working order)

Placements:

- organizational / industries / Infrastructure / Roads (kR6540, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Distance traveled with plow down

- id: `kpi.infrastructure.distance-traveled-with-plow-down`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Distance traveled with plow down measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Distance traveled with plow down. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Distance traveled with plow down on the desired side of its target for this period?

Inputs:

- `metric.distance-traveled-with-plow-down` (Distance traveled with plow down)

Placements:

- organizational / industries / Infrastructure / Roads (kR6541, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Distance traveled by plowing vehicle per snow event

- id: `kpi.infrastructure.distance-traveled-by-plowing-vehicle-per-snow-event`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Distance traveled by plowing vehicle per snow event measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A / B, where A is Distance traveled by plowing vehicle, B is snow event. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Distance traveled by plowing vehicle per snow event on the desired side of its target for this period?

Inputs:

- `metric.distance-traveled-by-plowing-vehicle` (Distance traveled by plowing vehicle)
- `metric.snow-event` (snow event)

Placements:

- organizational / industries / Infrastructure / Roads (kR6542, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Distance traveled to plow down distance ratio

- id: `kpi.infrastructure.distance-traveled-to-plow-down-distance-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Distance traveled to plow down distance ratio measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Distance traveled to plow down distance ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Distance traveled to plow down distance ratio on the desired side of its target for this period?

Inputs:

- `metric.distance-traveled-to-plow-down-distance-ratio` (Distance traveled to plow down distance ratio)

Placements:

- organizational / industries / Infrastructure / Roads (kR6543, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Quantity of salt/sand mixture applied per distance traveled

- id: `kpi.infrastructure.quantity-of-salt-sand-mixture-applied-per-distance-traveled`
- kind: kpi
- unit: count
- direction: corridor
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Quantity of salt/sand mixture applied per distance traveled measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A / B, where A is Quantity of salt/sand mixture applied, B is distance traveled. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Quantity of salt/sand mixture applied per distance traveled on the desired side of its target for this period?

Inputs:

- `metric.quantity-of-salt-sand-mixture-applied` (Quantity of salt/sand mixture applied)
- `metric.distance-traveled` (distance traveled)

Placements:

- organizational / industries / Infrastructure / Roads (kR6544, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Quantity of salt/sand mixture applied per vehicle

- id: `kpi.infrastructure.quantity-of-salt-sand-mixture-applied-per-vehicle`
- kind: kpi
- unit: count
- direction: corridor
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Quantity of salt/sand mixture applied per vehicle measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A / B, where A is Quantity of salt/sand mixture applied, B is vehicle. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Quantity of salt/sand mixture applied per vehicle on the desired side of its target for this period?

Inputs:

- `metric.quantity-of-salt-sand-mixture-applied` (Quantity of salt/sand mixture applied)
- `metric.vehicle` (vehicle)

Placements:

- organizational / industries / Infrastructure / Roads (kR6545, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time to bare pavement

- id: `kpi.infrastructure.time-to-bare-pavement`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time to bare pavement measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Time to bare pavement. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time to bare pavement on the desired side of its target for this period?

Inputs:

- `metric.time-to-bare-pavement` (Time to bare pavement)

Placements:

- organizational / industries / Infrastructure / Roads (kR6546, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time to provide one wheel track friction

- id: `kpi.infrastructure.time-to-provide-one-wheel-track-friction`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.roads`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time to provide one wheel track friction measures that result inside Infrastructure, subcategory Roads. The unit is count. The formula is A, where A is Time to provide one wheel track friction. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time to provide one wheel track friction on the desired side of its target for this period?

Inputs:

- `metric.time-to-provide-one-wheel-track-friction` (Time to provide one wheel track friction)

Placements:

- organizational / industries / Infrastructure / Roads (kR6548, page_0141)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
