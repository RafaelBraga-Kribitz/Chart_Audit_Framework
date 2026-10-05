# Postal and Courier / General

Context: organizational. Group: industries. KPIs: 30.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Transport capacity utilization

- id: `kpi.management.transport-capacity-utilization`
- kind: kpi
- unit: percent
- direction: corridor
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.logistics-distribution`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Transport capacity utilization measures that result inside Management, subcategory Logistics / Distribution. The unit is percent. The formula is (A / B) * 100, where A is part named by Transport capacity utilization, B is whole named by Transport capacity utilization. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Transport capacity utilization on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-transport-capacity-utilization` (part named by Transport capacity utilization)
- `metric.whole-named-by-transport-capacity-utilization` (whole named by Transport capacity utilization)

Placements:

- organizational / functional / Management / Logistics / Distribution (sK235, page_0054)
- organizational / industries / Postal and Courier / General (▲K235, page_0154)
- organizational / industries / Sport / General (xK235, page_0196)

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

### Customer shipment to delivery cycle time

- id: `kpi.management.customer-shipment-to-delivery-cycle-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.management.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Customer shipment to delivery cycle time measures that result inside Management, subcategory Organizational » Functional Areas. The unit is count. The formula is A, where A is Customer shipment to delivery cycle time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Customer shipment to delivery cycle time on the desired side of its target for this period?

Inputs:

- `metric.customer-shipment-to-delivery-cycle-time` (Customer shipment to delivery cycle time)

Placements:

- organizational / functional / Management / Organizational » Functional Areas (sK898, page_0055)
- organizational / industries / Postal and Courier / General (▲K98, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Shipment traceability

- id: `kpi.management.shipment-traceability`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.organizational-functional-areas`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Shipment traceability measures that result inside Management, subcategory Organizational > Functional Areas. The unit is percent. The formula is (A / B) * 100, where A is part named by Shipment traceability, B is whole named by Shipment traceability. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Shipment traceability on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-shipment-traceability` (part named by Shipment traceability)
- `metric.whole-named-by-shipment-traceability` (whole named by Shipment traceability)

Placements:

- organizational / functional / Management / Organizational > Functional Areas (s42978, page_0056)
- organizational / industries / Postal and Courier / General (▲K2776, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Transit time

- id: `kpi.management.transit-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Transit time measures that result inside Management, subcategory Organizational > Functional Areas. The unit is count. The formula is A, where A is Transit time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Transit time on the desired side of its target for this period?

Inputs:

- `metric.transit-time` (Transit time)

Placements:

- organizational / functional / Management / Organizational > Functional Areas (s42985, page_0056)
- organizational / industries / Postal and Courier / General (▲K376, page_0154)
- organizational / industries / Sport / Organizational » Industries (sK3785, page_0197)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Delivery routes competing each day

- id: `kpi.postal-and-courier.delivery-routes-competing-each-day`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.postal-and-courier.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Delivery routes competing each day measures that result inside Postal and Courier, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Delivery routes competing each day, B is whole named by Delivery routes competing each day. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Delivery routes competing each day on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-delivery-routes-competing-each-day` (part named by Delivery routes competing each day)
- `metric.whole-named-by-delivery-routes-competing-each-day` (whole named by Delivery routes competing each day)

Placements:

- organizational / industries / Postal and Courier / General (▲K304, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### ▲Transbound time

- id: `kpi.postal-and-courier.transbound-time`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.postal-and-courier.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

▲Transbound time measures that result inside Postal and Courier, subcategory General. The unit is number. The formula is A, where A is ▲Transbound time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is ▲Transbound time on the desired side of its target for this period?

Inputs:

- `metric.transbound-time` (▲Transbound time)

Placements:

- organizational / industries / Postal and Courier / General (▲K263, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Special delivery by end day

- id: `kpi.postal-and-courier.special-delivery-by-end-day`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.postal-and-courier.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Special delivery by end day measures that result inside Postal and Courier, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Special delivery by end day, B is whole named by Special delivery by end day. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Special delivery by end day on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-special-delivery-by-end-day` (part named by Special delivery by end day)
- `metric.whole-named-by-special-delivery-by-end-day` (whole named by Special delivery by end day)

Placements:

- organizational / industries / Postal and Courier / General (▲K305, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Residential deliveries

- id: `kpi.postal-and-courier.residential-deliveries`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.postal-and-courier.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Residential deliveries measures that result inside Postal and Courier, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Residential deliveries, B is whole named by Residential deliveries. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Residential deliveries on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-residential-deliveries` (part named by Residential deliveries)
- `metric.whole-named-by-residential-deliveries` (whole named by Residential deliveries)

Placements:

- organizational / industries / Postal and Courier / General (▲K306, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Business deliveries

- id: `kpi.postal-and-courier.business-deliveries`
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

Business deliveries measures that result inside Postal and Courier, subcategory General. The unit is count. The formula is A, where A is Business deliveries. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Business deliveries on the desired side of its target for this period?

Inputs:

- `metric.business-deliveries` (Business deliveries)

Placements:

- organizational / industries / Postal and Courier / General (▲K307, page_0154)

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

### Post office delivery losses

- id: `kpi.postal-and-courier.post-office-delivery-losses`
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

Post office delivery losses measures that result inside Postal and Courier, subcategory General. The unit is count. The formula is A, where A is Post office delivery losses. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Post office delivery losses on the desired side of its target for this period?

Inputs:

- `metric.post-office-delivery-losses` (Post office delivery losses)

Placements:

- organizational / industries / Postal and Courier / General (▲K309, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Collection points served each day

- id: `kpi.postal-and-courier.collection-points-served-each-day`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.postal-and-courier.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Collection points served each day measures that result inside Postal and Courier, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Collection points served each day, B is whole named by Collection points served each day. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Collection points served each day on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-collection-points-served-each-day` (part named by Collection points served each day)
- `metric.whole-named-by-collection-points-served-each-day` (whole named by Collection points served each day)

Placements:

- organizational / industries / Postal and Courier / General (▲K311, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Public mail collection points

- id: `kpi.postal-and-courier.public-mail-collection-points`
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

Public mail collection points measures that result inside Postal and Courier, subcategory General. The unit is count. The formula is A, where A is Public mail collection points. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Public mail collection points on the desired side of its target for this period?

Inputs:

- `metric.public-mail-collection-points` (Public mail collection points)

Placements:

- organizational / industries / Postal and Courier / General (▲K313, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Mail volume processed per hour

- id: `kpi.postal-and-courier.mail-volume-processed-per-hour`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.postal-and-courier.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Mail volume processed per hour measures that result inside Postal and Courier, subcategory General. The unit is count. The formula is A / B, where A is Mail volume processed, B is hour. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Mail volume processed per hour on the desired side of its target for this period?

Inputs:

- `metric.mail-volume-processed` (Mail volume processed)
- `metric.hour` (hour)

Placements:

- organizational / industries / Postal and Courier / General (▲K3787, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Delivery points

- id: `kpi.postal-and-courier.delivery-points`
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

Delivery points measures that result inside Postal and Courier, subcategory General. The unit is count. The formula is A, where A is Delivery points. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Delivery points on the desired side of its target for this period?

Inputs:

- `metric.delivery-points` (Delivery points)

Placements:

- organizational / industries / Postal and Courier / General (▲K314, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Nolauklans served by post office

- id: `kpi.postal-and-courier.nolauklans-served-by-post-office`
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

Nolauklans served by post office measures that result inside Postal and Courier, subcategory General. The unit is count. The formula is A, where A is Nolauklans served by post office. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Nolauklans served by post office on the desired side of its target for this period?

Inputs:

- `metric.nolauklans-served-by-post-office` (Nolauklans served by post office)

Placements:

- organizational / industries / Postal and Courier / General (▲K3795, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Stamped and metered mail sent by first class

- id: `kpi.postal-and-courier.stamped-and-metered-mail-sent-by-first-class`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.postal-and-courier.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Stamped and metered mail sent by first class measures that result inside Postal and Courier, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Stamped and metered mail sent by first class, B is whole named by Stamped and metered mail sent by first class. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Stamped and metered mail sent by first class on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-stamped-and-metered-mail-sent-by-first-class` (part named by Stamped and metered mail sent by first class)
- `metric.whole-named-by-stamped-and-metered-mail-sent-by-first-class` (whole named by Stamped and metered mail sent by first class)

Placements:

- organizational / industries / Postal and Courier / General (▲K315, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Post offices

- id: `kpi.postal-and-courier.post-offices`
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

Post offices measures that result inside Postal and Courier, subcategory General. The unit is count. The formula is A, where A is Post offices. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Post offices on the desired side of its target for this period?

Inputs:

- `metric.post-offices` (Post offices)

Placements:

- organizational / industries / Postal and Courier / General (▲K3796, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Electronic sorting machines

- id: `kpi.postal-and-courier.electronic-sorting-machines`
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

Electronic sorting machines measures that result inside Postal and Courier, subcategory General. The unit is count. The formula is A, where A is Electronic sorting machines. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Electronic sorting machines on the desired side of its target for this period?

Inputs:

- `metric.electronic-sorting-machines` (Electronic sorting machines)

Placements:

- organizational / industries / Postal and Courier / General (▲K317, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Distance traveled by postal vehicles

- id: `kpi.postal-and-courier.distance-traveled-by-postal-vehicles`
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

Distance traveled by postal vehicles measures that result inside Postal and Courier, subcategory General. The unit is count. The formula is A, where A is Distance traveled by postal vehicles. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Distance traveled by postal vehicles on the desired side of its target for this period?

Inputs:

- `metric.distance-traveled-by-postal-vehicles` (Distance traveled by postal vehicles)

Placements:

- organizational / industries / Postal and Courier / General (▲K3799, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Parcels posted at the post offices

- id: `kpi.postal-and-courier.parcels-posted-at-the-post-offices`
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

Parcels posted at the post offices measures that result inside Postal and Courier, subcategory General. The unit is count. The formula is A, where A is Parcels posted at the post offices. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Parcels posted at the post offices on the desired side of its target for this period?

Inputs:

- `metric.parcels-posted-at-the-post-offices` (Parcels posted at the post offices)

Placements:

- organizational / industries / Postal and Courier / General (▲K302, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Mail delivered by next working day

- id: `kpi.postal-and-courier.mail-delivered-by-next-working-day`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.postal-and-courier.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Mail delivered by next working day measures that result inside Postal and Courier, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Mail delivered by next working day, B is whole named by Mail delivered by next working day. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Mail delivered by next working day on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-mail-delivered-by-next-working-day` (part named by Mail delivered by next working day)
- `metric.whole-named-by-mail-delivered-by-next-working-day` (whole named by Mail delivered by next working day)

Placements:

- organizational / industries / Postal and Courier / General (▲K3800, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Parcels posted in the post offices that were the origin of a complaint

- id: `kpi.postal-and-courier.parcels-posted-in-the-post-offices-that-were-the-origin-of-a-complaint`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.postal-and-courier.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Parcels posted in the post offices that were the origin of a complaint measures that result inside Postal and Courier, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Parcels posted in the post offices that were the origin, B is a complaint. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Parcels posted in the post offices that were the origin of a complaint on the desired side of its target for this period?

Inputs:

- `metric.parcels-posted-in-the-post-offices-that-were-the-origin` (Parcels posted in the post offices that were the origin)
- `metric.a-complaint` (a complaint)

Placements:

- organizational / industries / Postal and Courier / General (▲K321, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Outgoing international mail shipped by next working day

- id: `kpi.postal-and-courier.outgoing-international-mail-shipped-by-next-working-day`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.postal-and-courier.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Outgoing international mail shipped by next working day measures that result inside Postal and Courier, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Outgoing international mail shipped by next working day, B is whole named by Outgoing international mail shipped by next working day. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Outgoing international mail shipped by next working day on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-outgoing-international-mail-shipped-by-next-working-day` (part named by Outgoing international mail shipped by next working day)
- `metric.whole-named-by-outgoing-international-mail-shipped-by-next-working-day` (whole named by Outgoing international mail shipped by next working day)

Placements:

- organizational / industries / Postal and Courier / General (▲K3801, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Mail volume processed per day

- id: `kpi.postal-and-courier.mail-volume-processed-per-day`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.postal-and-courier.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Mail volume processed per day measures that result inside Postal and Courier, subcategory General. The unit is count. The formula is A / B, where A is Mail volume processed, B is day. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Mail volume processed per day on the desired side of its target for this period?

Inputs:

- `metric.mail-volume-processed` (Mail volume processed)
- `metric.day` (day)

Placements:

- organizational / industries / Postal and Courier / General (▲K324, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Mail delivered by postcode area

- id: `kpi.postal-and-courier.mail-delivered-by-postcode-area`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.postal-and-courier.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Mail delivered by postcode area measures that result inside Postal and Courier, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Mail delivered by postcode area, B is whole named by Mail delivered by postcode area. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Mail delivered by postcode area on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-mail-delivered-by-postcode-area` (part named by Mail delivered by postcode area)
- `metric.whole-named-by-mail-delivered-by-postcode-area` (whole named by Mail delivered by postcode area)

Placements:

- organizational / industries / Postal and Courier / General (▲K3802, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Mail volume handled

- id: `kpi.postal-and-courier.mail-volume-handled`
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

Mail volume handled measures that result inside Postal and Courier, subcategory General. The unit is count. The formula is A, where A is Mail volume handled. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Mail volume handled on the desired side of its target for this period?

Inputs:

- `metric.mail-volume-handled` (Mail volume handled)

Placements:

- organizational / industries / Postal and Courier / General (▲K325, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Postal address changes processed

- id: `kpi.postal-and-courier.postal-address-changes-processed`
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

Postal address changes processed measures that result inside Postal and Courier, subcategory General. The unit is count. The formula is A, where A is Postal address changes processed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Postal address changes processed on the desired side of its target for this period?

Inputs:

- `metric.postal-address-changes-processed` (Postal address changes processed)

Placements:

- organizational / industries / Postal and Courier / General (▲K3803, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Advertising mail out of domestic letter posts

- id: `kpi.postal-and-courier.advertising-mail-out-of-domestic-letter-posts`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.postal-and-courier.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Advertising mail out of domestic letter posts measures that result inside Postal and Courier, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Advertising mail out, B is domestic letter posts. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Advertising mail out of domestic letter posts on the desired side of its target for this period?

Inputs:

- `metric.advertising-mail-out` (Advertising mail out)
- `metric.domestic-letter-posts` (domestic letter posts)

Placements:

- organizational / industries / Postal and Courier / General (▲K326, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
