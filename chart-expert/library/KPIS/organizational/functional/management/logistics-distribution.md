# Management / Logistics / Distribution

Context: organizational. Group: functional. KPIs: 19.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### On-time delivery

- id: `kpi.online-presence.on-time-delivery`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

On-time delivery measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is part named by On-time delivery, B is whole named by On-time delivery. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is On-time delivery on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-on-time-delivery` (part named by On-time delivery)
- `metric.whole-named-by-on-time-delivery` (whole named by On-time delivery)

Placements:

- organizational / functional / Online Presence / eCommerce (x810, page_0042)
- organizational / functional / Sales and Customer Service / Customer Service (xK10, page_0049)
- organizational / functional / Management / Logistics / Distribution (sK10, page_0054)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Items per order

- id: `kpi.online-presence.items-per-order`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Items per order measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A / B, where A is Items, B is order. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Items per order on the desired side of its target for this period?

Inputs:

- `metric.items` (Items)
- `metric.order` (order)

Placements:

- organizational / functional / Online Presence / eCommerce (x884, page_0042)
- organizational / functional / Management / Logistics / Distribution (sK240, page_0054)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Orders delivered with complete and accurate documentation

- id: `kpi.management.orders-delivered-with-complete-and-accurate-documentation`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.logistics-distribution`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Orders delivered with complete and accurate documentation measures that result inside Management, subcategory Logistics / Distribution. The unit is percent. The formula is (A / B) * 100, where A is numerator of Orders delivered with complete and accurate documentation, B is base of Orders delivered with complete and accurate documentation. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Orders delivered with complete and accurate documentation on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-orders-delivered-with-complete-and-accurate-documentation` (numerator of Orders delivered with complete and accurate documentation)
- `metric.base-of-orders-delivered-with-complete-and-accurate-documentation` (base of Orders delivered with complete and accurate documentation)

Placements:

- organizational / functional / Management / Logistics / Distribution (sK56, page_0054)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Point consumption per 100 kilometers

- id: `kpi.management.point-consumption-per-100-kilometers`
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

Point consumption per 100 kilometers measures that result inside Management, subcategory Logistics / Distribution. The unit is count. The formula is A / B, where A is Point consumption, B is 100 kilometers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Point consumption per 100 kilometers on the desired side of its target for this period?

Inputs:

- `metric.point-consumption` (Point consumption)
- `metric.100-kilometers` (100 kilometers)

Placements:

- organizational / functional / Management / Logistics / Distribution (sK143, page_0054)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Spots rep trip

- id: `kpi.management.spots-rep-trip`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.logistics-distribution`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Spots rep trip measures that result inside Management, subcategory Logistics / Distribution. The unit is count. The formula is A, where A is Spots rep trip. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Spots rep trip on the desired side of its target for this period?

Inputs:

- `metric.spots-rep-trip` (Spots rep trip)

Placements:

- organizational / functional / Management / Logistics / Distribution (sK160, page_0054)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

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

### Order fill rate

- id: `kpi.management.order-fill-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.logistics-distribution`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Order fill rate measures that result inside Management, subcategory Logistics / Distribution. The unit is percent. The formula is (A / B) * 100, where A is numerator of Order fill rate, B is base of Order fill rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Order fill rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-order-fill-rate` (numerator of Order fill rate)
- `metric.base-of-order-fill-rate` (base of Order fill rate)

Placements:

- organizational / functional / Management / Logistics / Distribution (sK26, page_0054)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Backorder costs

- id: `kpi.management.backorder-costs`
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

Backorder costs measures that result inside Management, subcategory Logistics / Distribution. The unit is count. The formula is A, where A is Backorder costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Backorder costs on the desired side of its target for this period?

Inputs:

- `metric.backorder-costs` (Backorder costs)

Placements:

- organizational / functional / Management / Logistics / Distribution (sK237, page_0054)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time spent picking back orders or stock-outs

- id: `kpi.management.time-spent-picking-back-orders-or-stock-outs`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.logistics-distribution`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time spent picking back orders or stock-outs measures that result inside Management, subcategory Logistics / Distribution. The unit is percent. The formula is (A / B) * 100, where A is part named by Time spent picking back orders or stock-outs, B is whole named by Time spent picking back orders or stock-outs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time spent picking back orders or stock-outs on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-time-spent-picking-back-orders-or-stock-outs` (part named by Time spent picking back orders or stock-outs)
- `metric.whole-named-by-time-spent-picking-back-orders-or-stock-outs` (whole named by Time spent picking back orders or stock-outs)

Placements:

- organizational / functional / Management / Logistics / Distribution (sK238, page_0054)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Orders picked per hour

- id: `kpi.management.orders-picked-per-hour`
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

Orders picked per hour measures that result inside Management, subcategory Logistics / Distribution. The unit is count. The formula is A / B, where A is Orders picked, B is hour. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Orders picked per hour on the desired side of its target for this period?

Inputs:

- `metric.orders-picked` (Orders picked)
- `metric.hour` (hour)

Placements:

- organizational / functional / Management / Logistics / Distribution (sK239, page_0054)

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

### Packaging to product ratio

- id: `kpi.management.packaging-to-product-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.logistics-distribution`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Packaging to product ratio measures that result inside Management, subcategory Logistics / Distribution. The unit is percent. The formula is (A / B) * 100, where A is Packaging, B is product ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Packaging to product ratio on the desired side of its target for this period?

Inputs:

- `metric.packaging` (Packaging)
- `metric.product-ratio` (product ratio)

Placements:

- organizational / functional / Management / Logistics / Distribution (sK282, page_0054)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Distribution cost

- id: `kpi.management.distribution-cost`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.logistics-distribution`
- analysis chart: `histogram` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Distribution cost measures that result inside Management, subcategory Logistics / Distribution. The unit is percent. The formula is (A / B) * 100, where A is part named by Distribution cost, B is whole named by Distribution cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Distribution cost on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-distribution-cost` (part named by Distribution cost)
- `metric.whole-named-by-distribution-cost` (whole named by Distribution cost)

Placements:

- organizational / functional / Management / Logistics / Distribution (sK700, page_0054)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Pick-to-chip service time for customer orders

- id: `kpi.management.pick-to-chip-service-time-for-customer-orders`
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

Pick-to-chip service time for customer orders measures that result inside Management, subcategory Logistics / Distribution. The unit is count. The formula is A, where A is Pick-to-chip service time for customer orders. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Pick-to-chip service time for customer orders on the desired side of its target for this period?

Inputs:

- `metric.pick-to-chip-service-time-for-customer-orders` (Pick-to-chip service time for customer orders)

Placements:

- organizational / functional / Management / Logistics / Distribution (sK701, page_0054)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Institutional logistics costs

- id: `kpi.management.institutional-logistics-costs`
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

Institutional logistics costs measures that result inside Management, subcategory Logistics / Distribution. The unit is count. The formula is A, where A is Institutional logistics costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Institutional logistics costs on the desired side of its target for this period?

Inputs:

- `metric.institutional-logistics-costs` (Institutional logistics costs)

Placements:

- organizational / functional / Management / Logistics / Distribution (sK703, page_0054)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Outsourced logistics costs

- id: `kpi.management.outsourced-logistics-costs`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.logistics-distribution`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Outsourced logistics costs measures that result inside Management, subcategory Logistics / Distribution. The unit is percent. The formula is (A / B) * 100, where A is part named by Outsourced logistics costs, B is whole named by Outsourced logistics costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Outsourced logistics costs on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-outsourced-logistics-costs` (part named by Outsourced logistics costs)
- `metric.whole-named-by-outsourced-logistics-costs` (whole named by Outsourced logistics costs)

Placements:

- organizational / functional / Management / Logistics / Distribution (sK704, page_0054)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Class-docking operations

- id: `kpi.management.class-docking-operations`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.logistics-distribution`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Class-docking operations measures that result inside Management, subcategory Logistics / Distribution. The unit is percent. The formula is (A / B) * 100, where A is numerator of Class-docking operations, B is base of Class-docking operations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Class-docking operations on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-class-docking-operations` (numerator of Class-docking operations)
- `metric.base-of-class-docking-operations` (base of Class-docking operations)

Placements:

- organizational / functional / Management / Logistics / Distribution (sK705, page_0054)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
