# Manufacturing / General

Context: organizational. Group: industries. KPIs: 54.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### § Cost of goods sold (COGS)

- id: `kpi.planning.cost-of-goods-sold-cogs`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

§ Cost of goods sold (COGS) measures that result inside Planning, subcategory General. The unit is number. The formula is A, where A is § Cost of goods sold (COGS). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § Cost of goods sold (COGS) on the desired side of its target for this period?

Inputs:

- `metric.cost-of-goods-sold-cogs` (§ Cost of goods sold (COGS))

Placements:

- personal / productivity / Planning / General (xK414, page_0009)
- organizational / industries / Manufacturing / General (▲K14, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### ▼ Electricity consumption per manufactured product

- id: `kpi.management.electricity-consumption-per-manufactured-product`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

▼ Electricity consumption per manufactured product measures that result inside Management, subcategory Organizational + Functional Areas. The unit is number. The formula is A / B, where A is ▼ Electricity consumption, B is manufactured product. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is ▼ Electricity consumption per manufactured product on the desired side of its target for this period?

Inputs:

- `metric.electricity-consumption` (▼ Electricity consumption)
- `metric.manufactured-product` (manufactured product)

Placements:

- organizational / functional / Management / Organizational + Functional Areas (xK1369, page_0015)
- organizational / industries / Manufacturing / General (▲K1569, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### ▼ Hazardous raw material per kilogram of product

- id: `kpi.management.hazardous-raw-material-per-kilogram-of-product`
- kind: kri
- unit: number
- direction: up
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

▼ Hazardous raw material per kilogram of product measures that result inside Management, subcategory Organizational + Functional Areas. The unit is number. The formula is A / B, where A is ▼ Hazardous raw material, B is kilogram of product. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is ▼ Hazardous raw material per kilogram of product on the desired side of its target for this period?

Inputs:

- `metric.hazardous-raw-material` (▼ Hazardous raw material)
- `metric.kilogram-of-product` (kilogram of product)

Placements:

- organizational / functional / Management / Organizational + Functional Areas (xK1373, page_0015)
- organizational / industries / Manufacturing / General (▲K1573, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Maintenance cost from equipment cost

- id: `kpi.management.maintenance-cost-from-equipment-cost`
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

Maintenance cost from equipment cost measures that result inside Management, subcategory Organizational » Functional Areas. The unit is percent. The formula is (A / B) * 100, where A is Maintenance cost, B is equipment cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Maintenance cost from equipment cost on the desired side of its target for this period?

Inputs:

- `metric.maintenance-cost` (Maintenance cost)
- `metric.equipment-cost` (equipment cost)

Placements:

- organizational / functional / Management / Organizational » Functional Areas (sK3034, page_0047)
- organizational / industries / Manufacturing / General (▲K3204, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Working stock

- id: `kpi.management.working-stock`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Working stock measures that result inside Management, subcategory Production. The unit is count. The formula is A, where A is Working stock. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Working stock on the desired side of its target for this period?

Inputs:

- `metric.working-stock` (Working stock)

Placements:

- organizational / functional / Management / Production (sK638, page_0047)
- organizational / functional / Management / General (xK638, page_0053)
- organizational / industries / Manufacturing / General (▲K638, page_0142)
- organizational / industries / Retail / General (sK638, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Decoupling stock

- id: `kpi.management.decoupling-stock`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Decoupling stock measures that result inside Management, subcategory Production. The unit is count. The formula is A, where A is Decoupling stock. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Decoupling stock on the desired side of its target for this period?

Inputs:

- `metric.decoupling-stock` (Decoupling stock)

Placements:

- organizational / functional / Management / Production (sK639, page_0047)
- organizational / functional / Management / General (xK639, page_0053)
- organizational / industries / Manufacturing / General (▲K629, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production costs per unit

- id: `kpi.management.production-costs-per-unit`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Production costs per unit measures that result inside Management, subcategory Production. The unit is currency. The formula is A / B, where A is Production costs, B is unit. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production costs per unit on the desired side of its target for this period?

Inputs:

- `metric.production-costs` (Production costs)
- `metric.unit` (unit)

Placements:

- organizational / functional / Management / Production (sK1628, page_0047)
- organizational / industries / Manufacturing / General (▲K1638, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Recovery yield rate of returned products

- id: `kpi.management.recovery-yield-rate-of-returned-products`
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

Recovery yield rate of returned products measures that result inside Management, subcategory Organizational » Functional Areas. The unit is percent. The formula is (A / B) * 100, where A is Recovery yield rate, B is returned products. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Recovery yield rate of returned products on the desired side of its target for this period?

Inputs:

- `metric.recovery-yield-rate` (Recovery yield rate)
- `metric.returned-products` (returned products)

Placements:

- organizational / functional / Management / Organizational » Functional Areas (K8600, page_0048)
- organizational / industries / Manufacturing / General (▲K660, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production plants

- id: `kpi.management.production-plants`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Production plants measures that result inside Management, subcategory Organizational » Functional Areas. The unit is count. The formula is A, where A is Production plants. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production plants on the desired side of its target for this period?

Inputs:

- `metric.production-plants` (Production plants)

Placements:

- organizational / functional / Management / Organizational » Functional Areas (K8684, page_0048)
- organizational / industries / Manufacturing / General (▲K634, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Scrap rate

- id: `kpi.management.scrap-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Scrap rate measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is numerator of Scrap rate, B is base of Scrap rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Scrap rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-scrap-rate` (numerator of Scrap rate)
- `metric.base-of-scrap-rate` (base of Scrap rate)

Placements:

- organizational / functional / Management / K997 # Regression testing (K8745, page_0048)
- organizational / industries / Manufacturing / General (▲K745, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Quality awareness programs

- id: `kpi.management.quality-awareness-programs`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Quality awareness programs measures that result inside Management, subcategory K997 # Regression testing. The unit is count. The formula is A, where A is Quality awareness programs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Quality awareness programs on the desired side of its target for this period?

Inputs:

- `metric.quality-awareness-programs` (Quality awareness programs)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1655, page_0048)
- organizational / industries / Manufacturing / General (▲K1655, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Informative inspections

- id: `kpi.management.informative-inspections`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Informative inspections measures that result inside Management, subcategory Organizational » Functional Areas. The unit is count. The formula is A, where A is Informative inspections. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Informative inspections on the desired side of its target for this period?

Inputs:

- `metric.informative-inspections` (Informative inspections)

Placements:

- organizational / functional / Management / Organizational » Functional Areas (sK4169, page_0049)
- organizational / industries / Manufacturing / General (▲K450, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Stock value

- id: `kpi.management.stock-value`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Stock value measures that result inside Management, subcategory General. The unit is currency. The formula is A, where A is Stock value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Stock value on the desired side of its target for this period?

Inputs:

- `metric.stock-value` (Stock value)

Placements:

- organizational / functional / Management / General (xK425, page_0053)
- organizational / industries / Manufacturing / General (▲K425, page_0142)
- organizational / industries / Retail / General (sK425, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sales order cancellation rate

- id: `kpi.management.sales-order-cancellation-rate`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Sales order cancellation rate measures that result inside Management, subcategory General. The unit is currency. The formula is A, where A is Sales order cancellation rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sales order cancellation rate on the desired side of its target for this period?

Inputs:

- `metric.sales-order-cancellation-rate` (Sales order cancellation rate)

Placements:

- organizational / functional / Management / General (xK428, page_0053)
- organizational / industries / Manufacturing / General (▲K24, page_0142)
- organizational / industries / Retail / General (sK428, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Safety stock

- id: `kpi.management.safety-stock`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Safety stock measures that result inside Management, subcategory General. The unit is count. The formula is A, where A is Safety stock. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Safety stock on the desired side of its target for this period?

Inputs:

- `metric.safety-stock` (Safety stock)

Placements:

- organizational / functional / Management / General (xK634, page_0053)
- organizational / industries / Manufacturing / General (▲K634, page_0142)
- organizational / industries / Retail / General (sK634, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Reorder point (ROP)

- id: `kpi.management.reorder-point-rop`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Reorder point (ROP) measures that result inside Management, subcategory General. The unit is count. The formula is A, where A is Reorder point (ROP). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Reorder point (ROP) on the desired side of its target for this period?

Inputs:

- `metric.reorder-point-rop` (Reorder point (ROP))

Placements:

- organizational / functional / Management / General (xK635, page_0053)
- organizational / industries / Manufacturing / General (▲K625, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Anticipation stock

- id: `kpi.management.anticipation-stock`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Anticipation stock measures that result inside Management, subcategory General. The unit is count. The formula is A, where A is Anticipation stock. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Anticipation stock on the desired side of its target for this period?

Inputs:

- `metric.anticipation-stock` (Anticipation stock)

Placements:

- organizational / functional / Management / General (xK635, page_0053)
- organizational / industries / Manufacturing / General (▲K613, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Distracted stock

- id: `kpi.management.distracted-stock`
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

Distracted stock measures that result inside Management, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Distracted stock, B is whole named by Distracted stock. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Distracted stock on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-distracted-stock` (part named by Distracted stock)
- `metric.whole-named-by-distracted-stock` (whole named by Distracted stock)

Placements:

- organizational / functional / Management / General (xK640, page_0053)
- organizational / industries / Manufacturing / General (▲K640, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Obsolete stock

- id: `kpi.management.obsolete-stock`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Obsolete stock measures that result inside Management, subcategory Organizational » Functional Areas. The unit is currency. The formula is A, where A is Obsolete stock. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Obsolete stock on the desired side of its target for this period?

Inputs:

- `metric.obsolete-stock` (Obsolete stock)

Placements:

- organizational / functional / Management / Organizational » Functional Areas (sK49, page_0054)
- organizational / industries / Manufacturing / General (▲K649, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of goods sold

- id: `kpi.supply-chain.cost-of-goods-sold`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.supply-chain.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of goods sold measures that result inside Supply Chain, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Cost, B is goods sold. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of goods sold on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.goods-sold` (goods sold)

Placements:

- organizational / functional / Supply Chain / General (xK2436, page_0057)
- organizational / industries / Manufacturing / General (▲K2436, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time to manufacturing

- id: `kpi.manufacturing.time-to-manufacturing`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time to manufacturing measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is Time to manufacturing. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time to manufacturing on the desired side of its target for this period?

Inputs:

- `metric.time-to-manufacturing` (Time to manufacturing)

Placements:

- organizational / industries / Manufacturing / General (▲K26, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### bulk containers with obvious signs of internal rusting

- id: `kpi.manufacturing.bulk-containers-with-obvious-signs-of-internal-rusting`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.manufacturing.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

bulk containers with obvious signs of internal rusting measures that result inside Manufacturing, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is bulk containers with obvious signs, B is internal rusting. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is bulk containers with obvious signs of internal rusting on the desired side of its target for this period?

Inputs:

- `metric.bulk-containers-with-obvious-signs` (bulk containers with obvious signs)
- `metric.internal-rusting` (internal rusting)

Placements:

- organizational / industries / Manufacturing / General (▲K336, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### unit production limit

- id: `kpi.manufacturing.unit-production-limit`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

unit production limit measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is unit production limit. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is unit production limit on the desired side of its target for this period?

Inputs:

- `metric.unit-production-limit` (unit production limit)

Placements:

- organizational / industries / Manufacturing / General (▲K84, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### interruptions in raw material supply

- id: `kpi.manufacturing.interruptions-in-raw-material-supply`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

interruptions in raw material supply measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is interruptions in raw material supply. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is interruptions in raw material supply on the desired side of its target for this period?

Inputs:

- `metric.interruptions-in-raw-material-supply` (interruptions in raw material supply)

Placements:

- organizational / industries / Manufacturing / General (▲K363, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Manufacturing contractors not used

- id: `kpi.manufacturing.manufacturing-contractors-not-used`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.manufacturing.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Manufacturing contractors not used measures that result inside Manufacturing, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Manufacturing contractors not used, B is whole named by Manufacturing contractors not used. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Manufacturing contractors not used on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-manufacturing-contractors-not-used` (part named by Manufacturing contractors not used)
- `metric.whole-named-by-manufacturing-contractors-not-used` (whole named by Manufacturing contractors not used)

Placements:

- organizational / industries / Manufacturing / General (▲K471, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Deflections improvement

- id: `kpi.manufacturing.deflections-improvement`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.manufacturing.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Deflections improvement measures that result inside Manufacturing, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Deflections improvement, B is whole named by Deflections improvement. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Deflections improvement on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-deflections-improvement` (part named by Deflections improvement)
- `metric.whole-named-by-deflections-improvement` (whole named by Deflections improvement)

Placements:

- organizational / industries / Manufacturing / General (▲K582, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Altman 2-Score

- id: `kpi.manufacturing.altman-2-score`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: survey
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Altman 2-Score measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is Altman 2-Score. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Altman 2-Score on the desired side of its target for this period?

Inputs:

- `metric.altman-2-score` (Altman 2-Score)

Placements:

- organizational / industries / Manufacturing / General (▲K494, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Deflections per manufacturing plant inspection

- id: `kpi.manufacturing.deflections-per-manufacturing-plant-inspection`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Deflections per manufacturing plant inspection measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A / B, where A is Deflections, B is manufacturing plant inspection. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Deflections per manufacturing plant inspection on the desired side of its target for this period?

Inputs:

- `metric.deflections` (Deflections)
- `metric.manufacturing-plant-inspection` (manufacturing plant inspection)

Placements:

- organizational / industries / Manufacturing / General (▲K141, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Critical equipment availability

- id: `kpi.manufacturing.critical-equipment-availability`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.manufacturing.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Critical equipment availability measures that result inside Manufacturing, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Critical equipment availability, B is whole named by Critical equipment availability. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Critical equipment availability on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-critical-equipment-availability` (part named by Critical equipment availability)
- `metric.whole-named-by-critical-equipment-availability` (whole named by Critical equipment availability)

Placements:

- organizational / industries / Manufacturing / General (▲K596, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Bulk containers compliance

- id: `kpi.manufacturing.bulk-containers-compliance`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.manufacturing.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Bulk containers compliance measures that result inside Manufacturing, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Bulk containers compliance, B is whole named by Bulk containers compliance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Bulk containers compliance on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-bulk-containers-compliance` (part named by Bulk containers compliance)
- `metric.whole-named-by-bulk-containers-compliance` (whole named by Bulk containers compliance)

Placements:

- organizational / industries / Manufacturing / General (▲K617, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### 3 Manufacturing flow control system utilization

- id: `kpi.manufacturing.3-manufacturing-flow-control-system-utilization`
- kind: kpi
- unit: number
- direction: corridor
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

3 Manufacturing flow control system utilization measures that result inside Manufacturing, subcategory General. The unit is number. The formula is A, where A is 3 Manufacturing flow control system utilization. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is 3 Manufacturing flow control system utilization on the desired side of its target for this period?

Inputs:

- `metric.3-manufacturing-flow-control-system-utilization` (3 Manufacturing flow control system utilization)

Placements:

- organizational / industries / Manufacturing / General (▲K630, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### People productivity

- id: `kpi.manufacturing.people-productivity`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

People productivity measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is People productivity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is People productivity on the desired side of its target for this period?

Inputs:

- `metric.people-productivity` (People productivity)

Placements:

- organizational / industries / Manufacturing / General (▲K631, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Not right first time

- id: `kpi.manufacturing.not-right-first-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.manufacturing.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Not right first time measures that result inside Manufacturing, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Not right first time, B is whole named by Not right first time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Not right first time on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-not-right-first-time` (part named by Not right first time)
- `metric.whole-named-by-not-right-first-time` (whole named by Not right first time)

Placements:

- organizational / industries / Manufacturing / General (▲K632, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Delivery cost on time and in fall

- id: `kpi.manufacturing.delivery-cost-on-time-and-in-fall`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.manufacturing.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Delivery cost on time and in fall measures that result inside Manufacturing, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Delivery cost on time and in fall, B is whole named by Delivery cost on time and in fall. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Delivery cost on time and in fall on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-delivery-cost-on-time-and-in-fall` (part named by Delivery cost on time and in fall)
- `metric.whole-named-by-delivery-cost-on-time-and-in-fall` (whole named by Delivery cost on time and in fall)

Placements:

- organizational / industries / Manufacturing / General (▲K633, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Inventory turns

- id: `kpi.manufacturing.inventory-turns`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Inventory turns measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is Inventory turns. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Inventory turns on the desired side of its target for this period?

Inputs:

- `metric.inventory-turns` (Inventory turns)

Placements:

- organizational / industries / Manufacturing / General (▲K17663, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Parts ordered

- id: `kpi.manufacturing.parts-ordered`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Parts ordered measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is Parts ordered. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Parts ordered on the desired side of its target for this period?

Inputs:

- `metric.parts-ordered` (Parts ordered)

Placements:

- organizational / industries / Manufacturing / General (▲K19666, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Calendar time

- id: `kpi.manufacturing.calendar-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Calendar time measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is Calendar time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Calendar time on the desired side of its target for this period?

Inputs:

- `metric.calendar-time` (Calendar time)

Placements:

- organizational / industries / Manufacturing / General (▲K2022, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Flannel downtime

- id: `kpi.manufacturing.flannel-downtime`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Flannel downtime measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is Flannel downtime. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Flannel downtime on the desired side of its target for this period?

Inputs:

- `metric.flannel-downtime` (Flannel downtime)

Placements:

- organizational / industries / Manufacturing / General (▲K20223, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Value of work is proper

- id: `kpi.manufacturing.value-of-work-is-proper`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.manufacturing.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Value of work is proper measures that result inside Manufacturing, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Value, B is work is proper. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Value of work is proper on the desired side of its target for this period?

Inputs:

- `metric.value` (Value)
- `metric.work-is-proper` (work is proper)

Placements:

- organizational / industries / Manufacturing / General (▲K1609, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Schedule operation time

- id: `kpi.manufacturing.schedule-operation-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Schedule operation time measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is Schedule operation time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Schedule operation time on the desired side of its target for this period?

Inputs:

- `metric.schedule-operation-time` (Schedule operation time)

Placements:

- organizational / industries / Manufacturing / General (▲K20204, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Set-up and change of coils

- id: `kpi.manufacturing.set-up-and-change-of-coils`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Set-up and change of coils measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is Set-up and change of coils. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Set-up and change of coils on the desired side of its target for this period?

Inputs:

- `metric.set-up-and-change-of-coils` (Set-up and change of coils)

Placements:

- organizational / industries / Manufacturing / General (▲K20225, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Lost manufacturing capacity

- id: `kpi.manufacturing.lost-manufacturing-capacity`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.manufacturing.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Lost manufacturing capacity measures that result inside Manufacturing, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Lost manufacturing capacity, B is whole named by Lost manufacturing capacity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Lost manufacturing capacity on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-lost-manufacturing-capacity` (part named by Lost manufacturing capacity)
- `metric.whole-named-by-lost-manufacturing-capacity` (whole named by Lost manufacturing capacity)

Placements:

- organizational / industries / Manufacturing / General (▲K1638, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Tests

- id: `kpi.manufacturing.tests`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Tests measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is Tests. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Tests on the desired side of its target for this period?

Inputs:

- `metric.tests` (Tests)

Placements:

- organizational / industries / Manufacturing / General (▲K20206, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Defects of machines

- id: `kpi.manufacturing.defects-of-machines`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Defects of machines measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is Defects of machines. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Defects of machines on the desired side of its target for this period?

Inputs:

- `metric.defects-of-machines` (Defects of machines)

Placements:

- organizational / industries / Manufacturing / General (▲K20227, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Defects of transfer

- id: `kpi.manufacturing.defects-of-transfer`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Defects of transfer measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is Defects of transfer. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Defects of transfer on the desired side of its target for this period?

Inputs:

- `metric.defects-of-transfer` (Defects of transfer)

Placements:

- organizational / industries / Manufacturing / General (▲K20228, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Defects of tools

- id: `kpi.manufacturing.defects-of-tools`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Defects of tools measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is Defects of tools. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Defects of tools on the desired side of its target for this period?

Inputs:

- `metric.defects-of-tools` (Defects of tools)

Placements:

- organizational / industries / Manufacturing / General (▲K20229, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Value added per manufacturing employee

- id: `kpi.manufacturing.value-added-per-manufacturing-employee`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.manufacturing.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Value added per manufacturing employee measures that result inside Manufacturing, subcategory General. The unit is percent. The formula is A / B, where A is Value added, B is manufacturing employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Value added per manufacturing employee on the desired side of its target for this period?

Inputs:

- `metric.value-added` (Value added)
- `metric.manufacturing-employee` (manufacturing employee)

Placements:

- organizational / industries / Manufacturing / General (▲K3952, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Defects in material and faults in disposition

- id: `kpi.manufacturing.defects-in-material-and-faults-in-disposition`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Defects in material and faults in disposition measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is Defects in material and faults in disposition. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Defects in material and faults in disposition on the desired side of its target for this period?

Inputs:

- `metric.defects-in-material-and-faults-in-disposition` (Defects in material and faults in disposition)

Placements:

- organizational / industries / Manufacturing / General (▲K20300, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Omissions of allergens in list of ingredients

- id: `kpi.manufacturing.omissions-of-allergens-in-list-of-ingredients`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Omissions of allergens in list of ingredients measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is Omissions of allergens in list of ingredients. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Omissions of allergens in list of ingredients on the desired side of its target for this period?

Inputs:

- `metric.omissions-of-allergens-in-list-of-ingredients` (Omissions of allergens in list of ingredients)

Placements:

- organizational / industries / Manufacturing / General (▲K4163, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Faults in logistic

- id: `kpi.manufacturing.faults-in-logistic`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Faults in logistic measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is Faults in logistic. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Faults in logistic on the desired side of its target for this period?

Inputs:

- `metric.faults-in-logistic` (Faults in logistic)

Placements:

- organizational / industries / Manufacturing / General (▲K20311, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Label accuracy

- id: `kpi.manufacturing.label-accuracy`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.manufacturing.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Label accuracy measures that result inside Manufacturing, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Label accuracy, B is whole named by Label accuracy. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Label accuracy on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-label-accuracy` (part named by Label accuracy)
- `metric.whole-named-by-label-accuracy` (whole named by Label accuracy)

Placements:

- organizational / industries / Manufacturing / General (▲K4244, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Container not available

- id: `kpi.manufacturing.container-not-available`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Container not available measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is Container not available. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Container not available on the desired side of its target for this period?

Inputs:

- `metric.container-not-available` (Container not available)

Placements:

- organizational / industries / Manufacturing / General (▲K20302, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Manufacturing plant inspections with zero deficiency

- id: `kpi.manufacturing.manufacturing-plant-inspections-with-zero-deficiency`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.manufacturing.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Manufacturing plant inspections with zero deficiency measures that result inside Manufacturing, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Manufacturing plant inspections with zero deficiency, B is whole named by Manufacturing plant inspections with zero deficiency. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Manufacturing plant inspections with zero deficiency on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-manufacturing-plant-inspections-with-zero-deficiency` (part named by Manufacturing plant inspections with zero deficiency)
- `metric.whole-named-by-manufacturing-plant-inspections-with-zero-deficiency` (whole named by Manufacturing plant inspections with zero deficiency)

Placements:

- organizational / industries / Manufacturing / General (▲K4346, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Operators not available

- id: `kpi.manufacturing.operators-not-available`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Operators not available measures that result inside Manufacturing, subcategory General. The unit is count. The formula is A, where A is Operators not available. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Operators not available on the desired side of its target for this period?

Inputs:

- `metric.operators-not-available` (Operators not available)

Placements:

- organizational / industries / Manufacturing / General (▲K20353, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
