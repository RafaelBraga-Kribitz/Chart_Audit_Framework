# Transportation / Airlines

Context: organizational. Group: industries. KPIs: 64.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Aircraft emissions

- id: `kpi.management.aircraft-emissions`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.environmental-care`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Aircraft emissions measures that result inside Management, subcategory Environmental Care. The unit is count. The formula is A, where A is Aircraft emissions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Aircraft emissions on the desired side of its target for this period?

Inputs:

- `metric.aircraft-emissions` (Aircraft emissions)

Placements:

- organizational / functional / Management / Environmental Care (sK592, page_0014)
- organizational / industries / Transportation / Airlines (sK259, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Baggage transfer time

- id: `kpi.management.baggage-transfer-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.logistics-distribution`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Baggage transfer time measures that result inside Management, subcategory Logistics / Distribution. The unit is count. The formula is A, where A is Baggage transfer time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Baggage transfer time on the desired side of its target for this period?

Inputs:

- `metric.baggage-transfer-time` (Baggage transfer time)

Placements:

- organizational / functional / Management / Logistics / Distribution (sK264, page_0054)
- organizational / industries / Transportation / Airlines (sK264, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fuel cost

- id: `kpi.management.fuel-cost`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.logistics-distribution`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fuel cost measures that result inside Management, subcategory Logistics / Distribution. The unit is count. The formula is A, where A is Fuel cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fuel cost on the desired side of its target for this period?

Inputs:

- `metric.fuel-cost` (Fuel cost)

Placements:

- organizational / functional / Management / Logistics / Distribution (sK265, page_0054)
- organizational / industries / Postal and Courier / General (▲K265, page_0154)
- organizational / industries / Transportation / Airlines (sK265, page_0181)
- organizational / industries / Sport / General (aK265, page_0192)
- organizational / industries / Sport / General (xK255, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Freight revenue per ton-mile

- id: `kpi.management.freight-revenue-per-ton-mile`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.logistics-distribution`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Freight revenue per ton-mile measures that result inside Management, subcategory Logistics / Distribution. The unit is count. The formula is A / B, where A is Freight revenue, B is ton-mile. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Freight revenue per ton-mile on the desired side of its target for this period?

Inputs:

- `metric.freight-revenue` (Freight revenue)
- `metric.ton-mile` (ton-mile)

Placements:

- organizational / functional / Management / Logistics / Distribution (sK267, page_0054)
- organizational / industries / Transportation / Airlines (sK267, page_0181)
- organizational / industries / Sport / General (aK287, page_0192)
- organizational / industries / Sport / General (xK207, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Empty running

- id: `kpi.supply-chain.empty-running`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.supply-chain.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Empty running measures that result inside Supply Chain, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Empty running, B is whole named by Empty running. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Empty running on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-empty-running` (part named by Empty running)
- `metric.whole-named-by-empty-running` (whole named by Empty running)

Placements:

- organizational / functional / Supply Chain / General (xK699, page_0057)
- organizational / industries / Transportation / Airlines (sK609, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Internet bookings

- id: `kpi.healthcare.internet-bookings`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Internet bookings measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is (A / B) * 100, where A is part named by Internet bookings, B is whole named by Internet bookings. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Internet bookings on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-internet-bookings` (part named by Internet bookings)
- `metric.whole-named-by-internet-bookings` (whole named by Internet bookings)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB12, page_0131)
- organizational / industries / Healthcare / Tour Operator (kK82, page_0133)
- organizational / industries / Transportation / Airlines (sK82, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Duplicate bookings

- id: `kpi.healthcare.duplicate-bookings`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Duplicate bookings measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is (A / B) * 100, where A is part named by Duplicate bookings, B is whole named by Duplicate bookings. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Duplicate bookings on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-duplicate-bookings` (part named by Duplicate bookings)
- `metric.whole-named-by-duplicate-bookings` (whole named by Duplicate bookings)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB1724, page_0131)
- organizational / industries / Healthcare / Tour Operator (kX1724, page_0133)
- organizational / industries / Transportation / Airlines (sK724, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Canceled reservations

- id: `kpi.healthcare.canceled-reservations`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.tour-operator`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Canceled reservations measures that result inside Healthcare, subcategory Tour Operator. The unit is percent. The formula is (A / B) * 100, where A is part named by Canceled reservations, B is whole named by Canceled reservations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Canceled reservations on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-canceled-reservations` (part named by Canceled reservations)
- `metric.whole-named-by-canceled-reservations` (whole named by Canceled reservations)

Placements:

- organizational / industries / Healthcare / Tour Operator (iX222, page_0133)
- organizational / industries / Transportation / Airlines (sK222, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Passenger transfers between flights

- id: `kpi.infrastructure.passenger-transfers-between-flights`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Passenger transfers between flights measures that result inside Infrastructure, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Passenger transfers between flights. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Passenger transfers between flights on the desired side of its target for this period?

Inputs:

- `metric.passenger-transfers-between-flights` (Passenger transfers between flights)

Placements:

- organizational / industries / Infrastructure / Organizational » Industries (sK3521, page_0134)
- organizational / industries / Transportation / Airlines (sK521, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Express services tonnes

- id: `kpi.postal-and-courier.express-services-tonnes`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.postal-and-courier.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Express services tonnes measures that result inside Postal and Courier, subcategory General. The unit is count. The formula is A, where A is Express services tonnes. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Express services tonnes on the desired side of its target for this period?

Inputs:

- `metric.express-services-tonnes` (Express services tonnes)

Placements:

- organizational / industries / Postal and Courier / General (▲K3476, page_0154)
- organizational / industries / Transportation / Airlines (sK476, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Passenger seats sold

- id: `kpi.transportation.passenger-seats-sold`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Passenger seats sold measures that result inside Transportation, subcategory Airlines. The unit is percent. The formula is (A / B) * 100, where A is part named by Passenger seats sold, B is whole named by Passenger seats sold. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Passenger seats sold on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-passenger-seats-sold` (part named by Passenger seats sold)
- `metric.whole-named-by-passenger-seats-sold` (whole named by Passenger seats sold)

Placements:

- organizational / industries / Transportation / Airlines (sK12, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fuel consumption per 100 kilometers

- id: `kpi.transportation.fuel-consumption-per-100-kilometers`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fuel consumption per 100 kilometers measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A / B, where A is Fuel consumption, B is 100 kilometers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fuel consumption per 100 kilometers on the desired side of its target for this period?

Inputs:

- `metric.fuel-consumption` (Fuel consumption)
- `metric.100-kilometers` (100 kilometers)

Placements:

- organizational / industries / Transportation / Airlines (sK143, page_0181)
- organizational / industries / Sport / General (aK143, page_0192)
- organizational / industries / Sport / General (xK143, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Transport capacity utilisation

- id: `kpi.transportation.transport-capacity-utilisation`
- kind: kpi
- unit: percent
- direction: corridor
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Transport capacity utilisation measures that result inside Transportation, subcategory Airlines. The unit is percent. The formula is (A / B) * 100, where A is part named by Transport capacity utilisation, B is whole named by Transport capacity utilisation. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Transport capacity utilisation on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-transport-capacity-utilisation` (part named by Transport capacity utilisation)
- `metric.whole-named-by-transport-capacity-utilisation` (whole named by Transport capacity utilisation)

Placements:

- organizational / industries / Transportation / Airlines (sK235, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue per available seat mile (RASM)

- id: `kpi.transportation.revenue-per-available-seat-mile-rasm`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Revenue per available seat mile (RASM) measures that result inside Transportation, subcategory Airlines. The unit is currency. The formula is A / B, where A is Revenue, B is available seat mile (RASM). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue per available seat mile (RASM) on the desired side of its target for this period?

Inputs:

- `metric.revenue` (Revenue)
- `metric.available-seat-mile-rasm` (available seat mile (RASM))

Placements:

- organizational / industries / Transportation / Airlines (sK255, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost per available seat mile (CASM)

- id: `kpi.transportation.cost-per-available-seat-mile-casm`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost per available seat mile (CASM) measures that result inside Transportation, subcategory Airlines. The unit is currency. The formula is A / B, where A is Cost, B is available seat mile (CASM). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost per available seat mile (CASM) on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.available-seat-mile-casm` (available seat mile (CASM))

Placements:

- organizational / industries / Transportation / Airlines (sK256, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue passenger kilometer (RPK)

- id: `kpi.transportation.revenue-passenger-kilometer-rpk`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Revenue passenger kilometer (RPK) measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Revenue passenger kilometer (RPK). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue passenger kilometer (RPK) on the desired side of its target for this period?

Inputs:

- `metric.revenue-passenger-kilometer-rpk` (Revenue passenger kilometer (RPK))

Placements:

- organizational / industries / Transportation / Airlines (sK257, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### On-time departure of transport vehicles

- id: `kpi.transportation.on-time-departure-of-transport-vehicles`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

On-time departure of transport vehicles measures that result inside Transportation, subcategory Airlines. The unit is percent. The formula is (A / B) * 100, where A is On-time departure, B is transport vehicles. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is On-time departure of transport vehicles on the desired side of its target for this period?

Inputs:

- `metric.on-time-departure` (On-time departure)
- `metric.transport-vehicles` (transport vehicles)

Placements:

- organizational / industries / Transportation / Airlines (sK258, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Delay per flight

- id: `kpi.transportation.delay-per-flight`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Delay per flight measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A / B, where A is Delay, B is flight. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Delay per flight on the desired side of its target for this period?

Inputs:

- `metric.delay` (Delay)
- `metric.flight` (flight)

Placements:

- organizational / industries / Transportation / Airlines (sK259, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Ground crew trained

- id: `kpi.transportation.ground-crew-trained`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Ground crew trained measures that result inside Transportation, subcategory Airlines. The unit is percent. The formula is (A / B) * 100, where A is part named by Ground crew trained, B is whole named by Ground crew trained. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Ground crew trained on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-ground-crew-trained` (part named by Ground crew trained)
- `metric.whole-named-by-ground-crew-trained` (whole named by Ground crew trained)

Placements:

- organizational / industries / Transportation / Airlines (sK260, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Turnaround time

- id: `kpi.transportation.turnaround-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Turnaround time measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Turnaround time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Turnaround time on the desired side of its target for this period?

Inputs:

- `metric.turnaround-time` (Turnaround time)

Placements:

- organizational / industries / Transportation / Airlines (sK263, page_0181)
- organizational / industries / Sport / General (xK263, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Airplane block time

- id: `kpi.transportation.airplane-block-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Airplane block time measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Airplane block time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Airplane block time on the desired side of its target for this period?

Inputs:

- `metric.airplane-block-time` (Airplane block time)

Placements:

- organizational / industries / Transportation / Airlines (sK266, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Airplane maintenance cost

- id: `kpi.transportation.airplane-maintenance-cost`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Airplane maintenance cost measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Airplane maintenance cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Airplane maintenance cost on the desired side of its target for this period?

Inputs:

- `metric.airplane-maintenance-cost` (Airplane maintenance cost)

Placements:

- organizational / industries / Transportation / Airlines (sK268, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Deferrals per aircraft

- id: `kpi.transportation.deferrals-per-aircraft`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Deferrals per aircraft measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A / B, where A is Deferrals, B is aircraft. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Deferrals per aircraft on the desired side of its target for this period?

Inputs:

- `metric.deferrals` (Deferrals)
- `metric.aircraft` (aircraft)

Placements:

- organizational / industries / Transportation / Airlines (sK364, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Check-in counters per flight

- id: `kpi.transportation.check-in-counters-per-flight`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Check-in counters per flight measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A / B, where A is Check-in counters, B is flight. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Check-in counters per flight on the desired side of its target for this period?

Inputs:

- `metric.check-in-counters` (Check-in counters)
- `metric.flight` (flight)

Placements:

- organizational / industries / Transportation / Airlines (sK467, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Check-in time

- id: `kpi.transportation.check-in-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Check-in time measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Check-in time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Check-in time on the desired side of its target for this period?

Inputs:

- `metric.check-in-time` (Check-in time)

Placements:

- organizational / industries / Transportation / Airlines (sK468, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Soft luggage on connecting flights

- id: `kpi.transportation.soft-luggage-on-connecting-flights`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Soft luggage on connecting flights measures that result inside Transportation, subcategory Airlines. The unit is percent. The formula is (A / B) * 100, where A is part named by Soft luggage on connecting flights, B is whole named by Soft luggage on connecting flights. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Soft luggage on connecting flights on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-soft-luggage-on-connecting-flights` (part named by Soft luggage on connecting flights)
- `metric.whole-named-by-soft-luggage-on-connecting-flights` (whole named by Soft luggage on connecting flights)

Placements:

- organizational / industries / Transportation / Airlines (sK469, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Terminal handling capacity

- id: `kpi.transportation.terminal-handling-capacity`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Terminal handling capacity measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Terminal handling capacity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Terminal handling capacity on the desired side of its target for this period?

Inputs:

- `metric.terminal-handling-capacity` (Terminal handling capacity)

Placements:

- organizational / industries / Transportation / Airlines (sK471, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Capacity (ATK) per employee

- id: `kpi.transportation.capacity-atk-per-employee`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Capacity (ATK) per employee measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A / B, where A is Capacity (ATK), B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Capacity (ATK) per employee on the desired side of its target for this period?

Inputs:

- `metric.capacity-atk` (Capacity (ATK))
- `metric.employee` (employee)

Placements:

- organizational / industries / Transportation / Airlines (sK472, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Overnight workload accomplished

- id: `kpi.transportation.overnight-workload-accomplished`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Overnight workload accomplished measures that result inside Transportation, subcategory Airlines. The unit is percent. The formula is (A / B) * 100, where A is part named by Overnight workload accomplished, B is whole named by Overnight workload accomplished. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Overnight workload accomplished on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-overnight-workload-accomplished` (part named by Overnight workload accomplished)
- `metric.whole-named-by-overnight-workload-accomplished` (whole named by Overnight workload accomplished)

Placements:

- organizational / industries / Transportation / Airlines (sK473, page_0181)
- organizational / industries / Transportation / Organizationals - Industries (sK3473, page_0187)
- organizational / industries / Sport / General (xK373, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Freight tonnes kilometres (FTK)

- id: `kpi.transportation.freight-tonnes-kilometres-ftk`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Freight tonnes kilometres (FTK) measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Freight tonnes kilometres (FTK). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Freight tonnes kilometres (FTK) on the desired side of its target for this period?

Inputs:

- `metric.freight-tonnes-kilometres-ftk` (Freight tonnes kilometres (FTK))

Placements:

- organizational / industries / Transportation / Airlines (sK47F, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Overall load factor

- id: `kpi.transportation.overall-load-factor`
- kind: kpi
- unit: percent
- direction: corridor
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Overall load factor measures that result inside Transportation, subcategory Airlines. The unit is percent. The formula is (A / B) * 100, where A is part named by Overall load factor, B is whole named by Overall load factor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Overall load factor on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-overall-load-factor` (part named by Overall load factor)
- `metric.whole-named-by-overall-load-factor` (whole named by Overall load factor)

Placements:

- organizational / industries / Transportation / Airlines (sK478, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Break-even load factor

- id: `kpi.transportation.break-even-load-factor`
- kind: kpi
- unit: percent
- direction: corridor
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Break-even load factor measures that result inside Transportation, subcategory Airlines. The unit is percent. The formula is (A / B) * 100, where A is part named by Break-even load factor, B is whole named by Break-even load factor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Break-even load factor on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-break-even-load-factor` (part named by Break-even load factor)
- `metric.whole-named-by-break-even-load-factor` (whole named by Break-even load factor)

Placements:

- organizational / industries / Transportation / Airlines (sK479, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost with pilot salaries

- id: `kpi.transportation.cost-with-pilot-salaries`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost with pilot salaries measures that result inside Transportation, subcategory Airlines. The unit is currency. The formula is A, where A is Cost with pilot salaries. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost with pilot salaries on the desired side of its target for this period?

Inputs:

- `metric.cost-with-pilot-salaries` (Cost with pilot salaries)

Placements:

- organizational / industries / Transportation / Airlines (sK480, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Pilot salaries per block hour

- id: `kpi.transportation.pilot-salaries-per-block-hour`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Pilot salaries per block hour measures that result inside Transportation, subcategory Airlines. The unit is currency. The formula is A / B, where A is Pilot salaries, B is block hour. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Pilot salaries per block hour on the desired side of its target for this period?

Inputs:

- `metric.pilot-salaries` (Pilot salaries)
- `metric.block-hour` (block hour)

Placements:

- organizational / industries / Transportation / Airlines (sK481, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Controlled crew cost per aircraft block hour

- id: `kpi.transportation.controlled-crew-cost-per-aircraft-block-hour`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Controlled crew cost per aircraft block hour measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A / B, where A is Controlled crew cost, B is aircraft block hour. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Controlled crew cost per aircraft block hour on the desired side of its target for this period?

Inputs:

- `metric.controlled-crew-cost` (Controlled crew cost)
- `metric.aircraft-block-hour` (aircraft block hour)

Placements:

- organizational / industries / Transportation / Airlines (sK482, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost per flight hour

- id: `kpi.transportation.cost-per-flight-hour`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost per flight hour measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A / B, where A is Cost, B is flight hour. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost per flight hour on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.flight-hour` (flight hour)

Placements:

- organizational / industries / Transportation / Airlines (sK484, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Aircraft fleet operating costs

- id: `kpi.transportation.aircraft-fleet-operating-costs`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Aircraft fleet operating costs measures that result inside Transportation, subcategory Airlines. The unit is currency. The formula is A, where A is Aircraft fleet operating costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Aircraft fleet operating costs on the desired side of its target for this period?

Inputs:

- `metric.aircraft-fleet-operating-costs` (Aircraft fleet operating costs)

Placements:

- organizational / industries / Transportation / Airlines (sK485, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Block spells

- id: `kpi.transportation.block-spells`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Block spells measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Block spells. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Block spells on the desired side of its target for this period?

Inputs:

- `metric.block-spells` (Block spells)

Placements:

- organizational / industries / Transportation / Airlines (sK486, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Flight crew per aircraft

- id: `kpi.transportation.flight-crew-per-aircraft`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Flight crew per aircraft measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A / B, where A is Flight crew, B is aircraft. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Flight crew per aircraft on the desired side of its target for this period?

Inputs:

- `metric.flight-crew` (Flight crew)
- `metric.aircraft` (aircraft)

Placements:

- organizational / industries / Transportation / Airlines (sK489, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Crew complaints

- id: `kpi.transportation.crew-complaints`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Crew complaints measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Crew complaints. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Crew complaints on the desired side of its target for this period?

Inputs:

- `metric.crew-complaints` (Crew complaints)

Placements:

- organizational / industries / Transportation / Airlines (sK490, page_0181)
- organizational / industries / Sport / General (xK490, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Crew control errors

- id: `kpi.transportation.crew-control-errors`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Crew control errors measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Crew control errors. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Crew control errors on the desired side of its target for this period?

Inputs:

- `metric.crew-control-errors` (Crew control errors)

Placements:

- organizational / industries / Transportation / Airlines (sK491, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Crew related delay minutes

- id: `kpi.transportation.crew-related-delay-minutes`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Crew related delay minutes measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Crew related delay minutes. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Crew related delay minutes on the desired side of its target for this period?

Inputs:

- `metric.crew-related-delay-minutes` (Crew related delay minutes)

Placements:

- organizational / industries / Transportation / Airlines (sK492, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Flights delayed due to technical issues

- id: `kpi.transportation.flights-delayed-due-to-technical-issues`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Flights delayed due to technical issues measures that result inside Transportation, subcategory Airlines. The unit is percent. The formula is (A / B) * 100, where A is Flights delayed due, B is technical issues. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Flights delayed due to technical issues on the desired side of its target for this period?

Inputs:

- `metric.flights-delayed-due` (Flights delayed due)
- `metric.technical-issues` (technical issues)

Placements:

- organizational / industries / Transportation / Airlines (sK493, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Flight delay due to wet weather conditions

- id: `kpi.transportation.flight-delay-due-to-wet-weather-conditions`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Flight delay due to wet weather conditions measures that result inside Transportation, subcategory Airlines. The unit is percent. The formula is (A / B) * 100, where A is Flight delay due, B is wet weather conditions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Flight delay due to wet weather conditions on the desired side of its target for this period?

Inputs:

- `metric.flight-delay-due` (Flight delay due)
- `metric.wet-weather-conditions` (wet weather conditions)

Placements:

- organizational / industries / Transportation / Airlines (sK494, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Aircraft emissions up by payload capacity

- id: `kpi.transportation.aircraft-emissions-up-by-payload-capacity`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Aircraft emissions up by payload capacity measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Aircraft emissions up by payload capacity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Aircraft emissions up by payload capacity on the desired side of its target for this period?

Inputs:

- `metric.aircraft-emissions-up-by-payload-capacity` (Aircraft emissions up by payload capacity)

Placements:

- organizational / industries / Transportation / Airlines (sK495, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Flights departures delayed more than 15 minutes

- id: `kpi.transportation.flights-departures-delayed-more-than-15-minutes`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Flights departures delayed more than 15 minutes measures that result inside Transportation, subcategory Airlines. The unit is percent. The formula is (A / B) * 100, where A is part named by Flights departures delayed more than 15 minutes, B is whole named by Flights departures delayed more than 15 minutes. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Flights departures delayed more than 15 minutes on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-flights-departures-delayed-more-than-15-minutes` (part named by Flights departures delayed more than 15 minutes)
- `metric.whole-named-by-flights-departures-delayed-more-than-15-minutes` (whole named by Flights departures delayed more than 15 minutes)

Placements:

- organizational / industries / Transportation / Airlines (sK496, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### In flight shutdown rate (FSO)

- id: `kpi.transportation.in-flight-shutdown-rate-fso`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

In flight shutdown rate (FSO) measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is In flight shutdown rate (FSO). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is In flight shutdown rate (FSO) on the desired side of its target for this period?

Inputs:

- `metric.in-flight-shutdown-rate-fso` (In flight shutdown rate (FSO))

Placements:

- organizational / industries / Transportation / Airlines (sK499, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Rejected takeoffs

- id: `kpi.transportation.rejected-takeoffs`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Rejected takeoffs measures that result inside Transportation, subcategory Airlines. The unit is number. The formula is A, where A is Rejected takeoffs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Rejected takeoffs on the desired side of its target for this period?

Inputs:

- `metric.rejected-takeoffs` (Rejected takeoffs)

Placements:

- organizational / industries / Transportation / Airlines (sK500, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Flight diversion rate

- id: `kpi.transportation.flight-diversion-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Flight diversion rate measures that result inside Transportation, subcategory Airlines. The unit is percent. The formula is (A / B) * 100, where A is numerator of Flight diversion rate, B is base of Flight diversion rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Flight diversion rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-flight-diversion-rate` (numerator of Flight diversion rate)
- `metric.base-of-flight-diversion-rate` (base of Flight diversion rate)

Placements:

- organizational / industries / Transportation / Airlines (sK501, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Ground damage rate

- id: `kpi.transportation.ground-damage-rate`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Ground damage rate measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Ground damage rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Ground damage rate on the desired side of its target for this period?

Inputs:

- `metric.ground-damage-rate` (Ground damage rate)

Placements:

- organizational / industries / Transportation / Airlines (sK502, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cancelled flights

- id: `kpi.transportation.cancelled-flights`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cancelled flights measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Cancelled flights. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cancelled flights on the desired side of its target for this period?

Inputs:

- `metric.cancelled-flights` (Cancelled flights)

Placements:

- organizational / industries / Transportation / Airlines (sK504, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Air operations covered by user charges

- id: `kpi.transportation.air-operations-covered-by-user-charges`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Air operations covered by user charges measures that result inside Transportation, subcategory Airlines. The unit is percent. The formula is (A / B) * 100, where A is numerator of Air operations covered by user charges, B is base of Air operations covered by user charges. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Air operations covered by user charges on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-air-operations-covered-by-user-charges` (numerator of Air operations covered by user charges)
- `metric.base-of-air-operations-covered-by-user-charges` (base of Air operations covered by user charges)

Placements:

- organizational / industries / Transportation / Airlines (sK506, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Flights per week during peak season

- id: `kpi.transportation.flights-per-week-during-peak-season`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Flights per week during peak season measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A / B, where A is Flights, B is week during peak season. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Flights per week during peak season on the desired side of its target for this period?

Inputs:

- `metric.flights` (Flights)
- `metric.week-during-peak-season` (week during peak season)

Placements:

- organizational / industries / Transportation / Airlines (sK507, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Distance flown

- id: `kpi.transportation.distance-flown`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Distance flown measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Distance flown. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Distance flown on the desired side of its target for this period?

Inputs:

- `metric.distance-flown` (Distance flown)

Placements:

- organizational / industries / Transportation / Airlines (sK509, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time flown

- id: `kpi.transportation.time-flown`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time flown measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Time flown. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time flown on the desired side of its target for this period?

Inputs:

- `metric.time-flown` (Time flown)

Placements:

- organizational / industries / Transportation / Airlines (sK510, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Airline network size

- id: `kpi.transportation.airline-network-size`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Airline network size measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Airline network size. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Airline network size on the desired side of its target for this period?

Inputs:

- `metric.airline-network-size` (Airline network size)

Placements:

- organizational / industries / Transportation / Airlines (sK511, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Punctuality “ready to go”

- id: `kpi.transportation.punctuality-ready-to-go`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Punctuality “ready to go” measures that result inside Transportation, subcategory Airlines. The unit is percent. The formula is (A / B) * 100, where A is Punctuality “ready, B is go”. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Punctuality “ready to go” on the desired side of its target for this period?

Inputs:

- `metric.punctuality-ready` (Punctuality “ready)
- `metric.go` (go”)

Placements:

- organizational / industries / Transportation / Airlines (sK512, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Destination cities serviced

- id: `kpi.transportation.destination-cities-serviced`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Destination cities serviced measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Destination cities serviced. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Destination cities serviced on the desired side of its target for this period?

Inputs:

- `metric.destination-cities-serviced` (Destination cities serviced)

Placements:

- organizational / industries / Transportation / Airlines (sK513, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Destinations served by direct air services

- id: `kpi.transportation.destinations-served-by-direct-air-services`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Destinations served by direct air services measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Destinations served by direct air services. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Destinations served by direct air services on the desired side of its target for this period?

Inputs:

- `metric.destinations-served-by-direct-air-services` (Destinations served by direct air services)

Placements:

- organizational / industries / Transportation / Airlines (sK514, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Flight duration

- id: `kpi.transportation.flight-duration`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Flight duration measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A, where A is Flight duration. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Flight duration on the desired side of its target for this period?

Inputs:

- `metric.flight-duration` (Flight duration)

Placements:

- organizational / industries / Transportation / Airlines (sK515, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Passenger injury rate

- id: `kpi.transportation.passenger-injury-rate`
- kind: kri
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Passenger injury rate measures that result inside Transportation, subcategory Airlines. The unit is percent. The formula is (A / B) * 100, where A is numerator of Passenger injury rate, B is base of Passenger injury rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Passenger injury rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-passenger-injury-rate` (numerator of Passenger injury rate)
- `metric.base-of-passenger-injury-rate` (base of Passenger injury rate)

Placements:

- organizational / industries / Transportation / Airlines (sK516, page_0181)
- organizational / industries / Transportation / Organizationals - Industries (sK3516, page_0187)
- organizational / industries / Sport / General (aK3516, page_0192)
- organizational / industries / Sport / General (xK518, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fuel consumed per block hour

- id: `kpi.transportation.fuel-consumed-per-block-hour`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fuel consumed per block hour measures that result inside Transportation, subcategory Airlines. The unit is count. The formula is A / B, where A is Fuel consumed, B is block hour. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fuel consumed per block hour on the desired side of its target for this period?

Inputs:

- `metric.fuel-consumed` (Fuel consumed)
- `metric.block-hour` (block hour)

Placements:

- organizational / industries / Transportation / Airlines (sK518, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Customer recommendation

- id: `kpi.transportation.customer-recommendation`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Customer recommendation measures that result inside Transportation, subcategory Airlines. The unit is percent. The formula is (A / B) * 100, where A is part named by Customer recommendation, B is whole named by Customer recommendation. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Customer recommendation on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-customer-recommendation` (part named by Customer recommendation)
- `metric.whole-named-by-customer-recommendation` (whole named by Customer recommendation)

Placements:

- organizational / industries / Transportation / Airlines (sK527, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Load carried per employee

- id: `kpi.transportation.load-carried-per-employee`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation.airlines`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Load carried per employee measures that result inside Transportation, subcategory Airlines. The unit is percent. The formula is A / B, where A is Load carried, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Load carried per employee on the desired side of its target for this period?

Inputs:

- `metric.load-carried` (Load carried)
- `metric.employee` (employee)

Placements:

- organizational / industries / Transportation / Airlines (sK530, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
