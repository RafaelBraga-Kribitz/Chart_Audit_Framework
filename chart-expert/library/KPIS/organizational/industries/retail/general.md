# Retail / General

Context: organizational. Group: industries. KPIs: 64.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Net cash flow per customer

- id: `kpi.management.net-cash-flow-per-customer`
- kind: kpi
- unit: count
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

Net cash flow per customer measures that result inside Management, subcategory Organizational» Functional Areas. The unit is count. The formula is A / B, where A is Net cash flow, B is customer. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Net cash flow per customer on the desired side of its target for this period?

Inputs:

- `metric.net-cash-flow` (Net cash flow)
- `metric.customer` (customer)

Placements:

- organizational / functional / Management / Organizational» Functional Areas (x85457, page_0018)
- organizational / industries / Retail / General (sK4547, page_0173)

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

### Sales by product category

- id: `kpi.sales-and-customer-service.sales-by-product-category`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.organizational-functional-areas`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Sales by product category measures that result inside Sales and Customer Service, subcategory Organizational > Functional Areas. The unit is percent. The formula is (A / B) * 100, where A is part named by Sales by product category, B is whole named by Sales by product category. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sales by product category on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-sales-by-product-category` (part named by Sales by product category)
- `metric.whole-named-by-sales-by-product-category` (whole named by Sales by product category)

Placements:

- organizational / functional / Sales and Customer Service / Organizational > Functional Areas (sK5418, page_0052)
- organizational / industries / Retail / General (sK4546, page_0173)

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

### Sales per labor hour

- id: `kpi.healthcare.sales-per-labor-hour`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Sales per labor hour measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is currency. The formula is A / B, where A is Sales, B is labor hour. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sales per labor hour on the desired side of its target for this period?

Inputs:

- `metric.sales` (Sales)
- `metric.labor-hour` (labor hour)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KPI # KSS549, page_0129)
- organizational / industries / Retail / General (sK4569, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Product shelf-space profitability

- id: `kpi.retail.product-shelf-space-profitability`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.retail.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Product shelf-space profitability measures that result inside Retail, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Product shelf-space profitability, B is whole named by Product shelf-space profitability. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Product shelf-space profitability on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-product-shelf-space-profitability` (part named by Product shelf-space profitability)
- `metric.whole-named-by-product-shelf-space-profitability` (whole named by Product shelf-space profitability)

Placements:

- organizational / industries / Retail / General (sK69, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Inventory to sales ratio (ISR)

- id: `kpi.retail.inventory-to-sales-ratio-isr`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Inventory to sales ratio (ISR) measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Inventory to sales ratio (ISR). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Inventory to sales ratio (ISR) on the desired side of its target for this period?

Inputs:

- `metric.inventory-to-sales-ratio-isr` (Inventory to sales ratio (ISR))

Placements:

- organizational / industries / Retail / General (sK4808, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sell-through

- id: `kpi.retail.sell-through`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.retail.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Sell-through measures that result inside Retail, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Sell-through, B is whole named by Sell-through. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sell-through on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-sell-through` (part named by Sell-through)
- `metric.whole-named-by-sell-through` (whole named by Sell-through)

Placements:

- organizational / industries / Retail / General (sK317, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Perishable items with past due date

- id: `kpi.retail.perishable-items-with-past-due-date`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.retail.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Perishable items with past due date measures that result inside Retail, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Perishable items with past due date, B is whole named by Perishable items with past due date. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Perishable items with past due date on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-perishable-items-with-past-due-date` (part named by Perishable items with past due date)
- `metric.whole-named-by-perishable-items-with-past-due-date` (whole named by Perishable items with past due date)

Placements:

- organizational / industries / Retail / General (sK4809, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Selling opportunities

- id: `kpi.retail.selling-opportunities`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Selling opportunities measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Selling opportunities. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Selling opportunities on the desired side of its target for this period?

Inputs:

- `metric.selling-opportunities` (Selling opportunities)

Placements:

- organizational / industries / Retail / General (sK331, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Previous usage of store visits

- id: `kpi.retail.previous-usage-of-store-visits`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Previous usage of store visits measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Previous usage of store visits. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Previous usage of store visits on the desired side of its target for this period?

Inputs:

- `metric.previous-usage-of-store-visits` (Previous usage of store visits)

Placements:

- organizational / industries / Retail / General (sK5788, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sales by department

- id: `kpi.retail.sales-by-department`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Sales by department measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Sales by department. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sales by department on the desired side of its target for this period?

Inputs:

- `metric.sales-by-department` (Sales by department)

Placements:

- organizational / industries / Retail / General (sK332, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Store loyalty

- id: `kpi.retail.store-loyalty`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.retail.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Store loyalty measures that result inside Retail, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Store loyalty, B is whole named by Store loyalty. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Store loyalty on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-store-loyalty` (part named by Store loyalty)
- `metric.whole-named-by-store-loyalty` (whole named by Store loyalty)

Placements:

- organizational / industries / Retail / General (sK5799, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of goods sold (CGOS)

- id: `kpi.retail.cost-of-goods-sold-cgos`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.retail.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Cost of goods sold (CGOS) measures that result inside Retail, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Cost, B is goods sold (CGOS). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of goods sold (CGOS) on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.goods-sold-cgos` (goods sold (CGOS))

Placements:

- organizational / industries / Retail / General (sK414, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Volume of purchase

- id: `kpi.retail.volume-of-purchase`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Volume of purchase measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Volume of purchase. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Volume of purchase on the desired side of its target for this period?

Inputs:

- `metric.volume-of-purchase` (Volume of purchase)

Placements:

- organizational / industries / Retail / General (sK6247, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Markdown goods

- id: `kpi.retail.markdown-goods`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.retail.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Markdown goods measures that result inside Retail, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Markdown goods, B is whole named by Markdown goods. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Markdown goods on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-markdown-goods` (part named by Markdown goods)
- `metric.whole-named-by-markdown-goods` (whole named by Markdown goods)

Placements:

- organizational / industries / Retail / General (sK420, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Units sold per customer

- id: `kpi.retail.units-sold-per-customer`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Units sold per customer measures that result inside Retail, subcategory General. The unit is count. The formula is A / B, where A is Units sold, B is customer. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Units sold per customer on the desired side of its target for this period?

Inputs:

- `metric.units-sold` (Units sold)
- `metric.customer` (customer)

Placements:

- organizational / industries / Retail / General (sK6131, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Store conversion rate

- id: `kpi.retail.store-conversion-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.retail.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Store conversion rate measures that result inside Retail, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is numerator of Store conversion rate, B is base of Store conversion rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Store conversion rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-store-conversion-rate` (numerator of Store conversion rate)
- `metric.base-of-store-conversion-rate` (base of Store conversion rate)

Placements:

- organizational / industries / Retail / General (sK421, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Customer per day

- id: `kpi.retail.customer-per-day`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Customer per day measures that result inside Retail, subcategory General. The unit is count. The formula is A / B, where A is Customer, B is day. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Customer per day on the desired side of its target for this period?

Inputs:

- `metric.customer` (Customer)
- `metric.day` (day)

Placements:

- organizational / industries / Retail / General (sK6134, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sales revenue per hour

- id: `kpi.retail.sales-revenue-per-hour`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Sales revenue per hour measures that result inside Retail, subcategory General. The unit is currency. The formula is A / B, where A is Sales revenue, B is hour. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sales revenue per hour on the desired side of its target for this period?

Inputs:

- `metric.sales-revenue` (Sales revenue)
- `metric.hour` (hour)

Placements:

- organizational / industries / Retail / General (sK422, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sale value

- id: `kpi.retail.sale-value`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Sale value measures that result inside Retail, subcategory General. The unit is currency. The formula is A, where A is Sale value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sale value on the desired side of its target for this period?

Inputs:

- `metric.sale-value` (Sale value)

Placements:

- organizational / industries / Retail / General (sK6315, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Out of stock product lines

- id: `kpi.retail.out-of-stock-product-lines`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Out of stock product lines measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Out of stock product lines. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Out of stock product lines on the desired side of its target for this period?

Inputs:

- `metric.out-of-stock-product-lines` (Out of stock product lines)

Placements:

- organizational / industries / Retail / General (sK6316, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Product sells per transaction

- id: `kpi.retail.product-sells-per-transaction`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Product sells per transaction measures that result inside Retail, subcategory General. The unit is count. The formula is A / B, where A is Product sells, B is transaction. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Product sells per transaction on the desired side of its target for this period?

Inputs:

- `metric.product-sells` (Product sells)
- `metric.transaction` (transaction)

Placements:

- organizational / industries / Retail / General (sK6317, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Store satisfaction while shopping

- id: `kpi.retail.store-satisfaction-while-shopping`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.retail.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Store satisfaction while shopping measures that result inside Retail, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Store satisfaction while shopping, B is whole named by Store satisfaction while shopping. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Store satisfaction while shopping on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-store-satisfaction-while-shopping` (part named by Store satisfaction while shopping)
- `metric.whole-named-by-store-satisfaction-while-shopping` (whole named by Store satisfaction while shopping)

Placements:

- organizational / industries / Retail / General (sK536, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Planned opening hours achieved

- id: `kpi.retail.planned-opening-hours-achieved`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.retail.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Planned opening hours achieved measures that result inside Retail, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Planned opening hours achieved, B is whole named by Planned opening hours achieved. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Planned opening hours achieved on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-planned-opening-hours-achieved` (part named by Planned opening hours achieved)
- `metric.whole-named-by-planned-opening-hours-achieved` (whole named by Planned opening hours achieved)

Placements:

- organizational / industries / Retail / General (sK6888, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Stock rotations

- id: `kpi.retail.stock-rotations`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Stock rotations measures that result inside Retail, subcategory General. The unit is currency. The formula is A, where A is Stock rotations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Stock rotations on the desired side of its target for this period?

Inputs:

- `metric.stock-rotations` (Stock rotations)

Placements:

- organizational / industries / Retail / General (sK633, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Adoption rate ratio

- id: `kpi.retail.adoption-rate-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Adoption rate ratio measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Adoption rate ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Adoption rate ratio on the desired side of its target for this period?

Inputs:

- `metric.adoption-rate-ratio` (Adoption rate ratio)

Placements:

- organizational / industries / Retail / General (sK68493, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Births of retail secondary locations by employment

- id: `kpi.retail.births-of-retail-secondary-locations-by-employment`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Births of retail secondary locations by employment measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Births of retail secondary locations by employment. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Births of retail secondary locations by employment on the desired side of its target for this period?

Inputs:

- `metric.births-of-retail-secondary-locations-by-employment` (Births of retail secondary locations by employment)

Placements:

- organizational / industries / Retail / General (sK14360, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Reorganization stock

- id: `kpi.retail.reorganization-stock`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Reorganization stock measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Reorganization stock. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Reorganization stock on the desired side of its target for this period?

Inputs:

- `metric.reorganization-stock` (Reorganization stock)

Placements:

- organizational / industries / Retail / General (sK635, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### size

- id: `kpi.retail.size`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

size measures that result inside Retail, subcategory General. The unit is number. The formula is A, where A is size. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is size on the desired side of its target for this period?

Inputs:

- `metric.size` (size)

Placements:

- organizational / industries / Retail / General (sK14364, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Consumption of refreshment ratio

- id: `kpi.retail.consumption-of-refreshment-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Consumption of refreshment ratio measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Consumption of refreshment ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Consumption of refreshment ratio on the desired side of its target for this period?

Inputs:

- `metric.consumption-of-refreshment-ratio` (Consumption of refreshment ratio)

Placements:

- organizational / industries / Retail / General (sK14834, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Outsource stock

- id: `kpi.retail.outsource-stock`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Outsource stock measures that result inside Retail, subcategory General. The unit is currency. The formula is A, where A is Outsource stock. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Outsource stock on the desired side of its target for this period?

Inputs:

- `metric.outsource-stock` (Outsource stock)

Placements:

- organizational / industries / Retail / General (sK649, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contracts awarded for supermarket developments

- id: `kpi.retail.contracts-awarded-for-supermarket-developments`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Contracts awarded for supermarket developments measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Contracts awarded for supermarket developments. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contracts awarded for supermarket developments on the desired side of its target for this period?

Inputs:

- `metric.contracts-awarded-for-supermarket-developments` (Contracts awarded for supermarket developments)

Placements:

- organizational / industries / Retail / General (sK14864, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Same store sales growth

- id: `kpi.retail.same-store-sales-growth`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Same store sales growth measures that result inside Retail, subcategory General. The unit is currency. The formula is A, where A is Same store sales growth. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Same store sales growth on the desired side of its target for this period?

Inputs:

- `metric.same-store-sales-growth` (Same store sales growth)

Placements:

- organizational / industries / Retail / General (sK782, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Controlled food production

- id: `kpi.retail.controlled-food-production`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Controlled food production measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Controlled food production. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Controlled food production on the desired side of its target for this period?

Inputs:

- `metric.controlled-food-production` (Controlled food production)

Placements:

- organizational / industries / Retail / General (sK14886, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sales growth in stores open at least 12 months

- id: `kpi.retail.sales-growth-in-stores-open-at-least-12-months`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Sales growth in stores open at least 12 months measures that result inside Retail, subcategory General. The unit is currency. The formula is A, where A is Sales growth in stores open at least 12 months. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sales growth in stores open at least 12 months on the desired side of its target for this period?

Inputs:

- `metric.sales-growth-in-stores-open-at-least-12-months` (Sales growth in stores open at least 12 months)

Placements:

- organizational / industries / Retail / General (sK1699, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Days involving for general merchandise and cigarettes

- id: `kpi.retail.days-involving-for-general-merchandise-and-cigarettes`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Days involving for general merchandise and cigarettes measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Days involving for general merchandise and cigarettes. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Days involving for general merchandise and cigarettes on the desired side of its target for this period?

Inputs:

- `metric.days-involving-for-general-merchandise-and-cigarettes` (Days involving for general merchandise and cigarettes)

Placements:

- organizational / industries / Retail / General (sK14907, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Stock keeping units in portfolio

- id: `kpi.retail.stock-keeping-units-in-portfolio`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Stock keeping units in portfolio measures that result inside Retail, subcategory General. The unit is currency. The formula is A, where A is Stock keeping units in portfolio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Stock keeping units in portfolio on the desired side of its target for this period?

Inputs:

- `metric.stock-keeping-units-in-portfolio` (Stock keeping units in portfolio)

Placements:

- organizational / industries / Retail / General (sK2264, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Deaths of retail secondary locations by employment

- id: `kpi.retail.deaths-of-retail-secondary-locations-by-employment`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Deaths of retail secondary locations by employment measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Deaths of retail secondary locations by employment. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Deaths of retail secondary locations by employment on the desired side of its target for this period?

Inputs:

- `metric.deaths-of-retail-secondary-locations-by-employment` (Deaths of retail secondary locations by employment)

Placements:

- organizational / industries / Retail / General (sK15006, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Out of stock items

- id: `kpi.retail.out-of-stock-items`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.retail.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Out of stock items measures that result inside Retail, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Out, B is stock items. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Out of stock items on the desired side of its target for this period?

Inputs:

- `metric.out` (Out)
- `metric.stock-items` (stock items)

Placements:

- organizational / industries / Retail / General (sK3982, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### ERITDA to value of equipment and leaseholds

- id: `kpi.retail.eritda-to-value-of-equipment-and-leaseholds`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

ERITDA to value of equipment and leaseholds measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is ERITDA to value of equipment and leaseholds. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is ERITDA to value of equipment and leaseholds on the desired side of its target for this period?

Inputs:

- `metric.eritda-to-value-of-equipment-and-leaseholds` (ERITDA to value of equipment and leaseholds)

Placements:

- organizational / industries / Retail / General (sK15141, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Stores

- id: `kpi.retail.stores`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Stores measures that result inside Retail, subcategory General. The unit is currency. The formula is A, where A is Stores. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Stores on the desired side of its target for this period?

Inputs:

- `metric.stores` (Stores)

Placements:

- organizational / industries / Retail / General (sK4524, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employee and employees per establishment

- id: `kpi.retail.employee-and-employees-per-establishment`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Employee and employees per establishment measures that result inside Retail, subcategory General. The unit is count. The formula is A / B, where A is Employee and employees, B is establishment. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employee and employees per establishment on the desired side of its target for this period?

Inputs:

- `metric.employee-and-employees` (Employee and employees)
- `metric.establishment` (establishment)

Placements:

- organizational / industries / Retail / General (sK15187, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time spent in the store

- id: `kpi.retail.time-spent-in-the-store`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Time spent in the store measures that result inside Retail, subcategory General. The unit is currency. The formula is A, where A is Time spent in the store. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time spent in the store on the desired side of its target for this period?

Inputs:

- `metric.time-spent-in-the-store` (Time spent in the store)

Placements:

- organizational / industries / Retail / General (sK4525, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employment size of retail from

- id: `kpi.retail.employment-size-of-retail-from`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Employment size of retail from measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Employment size of retail from. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employment size of retail from on the desired side of its target for this period?

Inputs:

- `metric.employment-size-of-retail-from` (Employment size of retail from)

Placements:

- organizational / industries / Retail / General (sK15198, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Gross leaseable area per employee

- id: `kpi.retail.gross-leaseable-area-per-employee`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Gross leaseable area per employee measures that result inside Retail, subcategory General. The unit is currency. The formula is A / B, where A is Gross leaseable area, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Gross leaseable area per employee on the desired side of its target for this period?

Inputs:

- `metric.gross-leaseable-area` (Gross leaseable area)
- `metric.employee` (employee)

Placements:

- organizational / industries / Retail / General (sK4528, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Well-being and audit and mystery shopper ratings of compliance with specific implementation standards

- id: `kpi.retail.well-being-and-audit-and-mystery-shopper-ratings-of-compliance-with-spec`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Well-being and audit and mystery shopper ratings of compliance with specific implementation standards measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Well-being and audit and mystery shopper ratings of compliance with specific implementation standards. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Well-being and audit and mystery shopper ratings of compliance with specific implementation standards on the desired side of its target for this period?

Inputs:

- `metric.well-being-and-audit-and-mystery-shopper-ratings-of-compliance-with-spec` (Well-being and audit and mystery shopper ratings of compliance with specific implementation standards)

Placements:

- organizational / industries / Retail / General (sK17254, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Furniture fit

- id: `kpi.retail.furniture-fit`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Furniture fit measures that result inside Retail, subcategory General. The unit is currency. The formula is A, where A is Furniture fit. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Furniture fit on the desired side of its target for this period?

Inputs:

- `metric.furniture-fit` (Furniture fit)

Placements:

- organizational / industries / Retail / General (sK4535, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Well-being and audit and mystery shopper ratings of compliance with basic operating standards

- id: `kpi.retail.well-being-and-audit-and-mystery-shopper-ratings-of-compliance-with-basi`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Well-being and audit and mystery shopper ratings of compliance with basic operating standards measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Well-being and audit and mystery shopper ratings of compliance with basic operating standards. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Well-being and audit and mystery shopper ratings of compliance with basic operating standards on the desired side of its target for this period?

Inputs:

- `metric.well-being-and-audit-and-mystery-shopper-ratings-of-compliance-with-basi` (Well-being and audit and mystery shopper ratings of compliance with basic operating standards)

Placements:

- organizational / industries / Retail / General (sK17255, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Women in the retail workforce

- id: `kpi.retail.women-in-the-retail-workforce`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Women in the retail workforce measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Women in the retail workforce. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Women in the retail workforce on the desired side of its target for this period?

Inputs:

- `metric.women-in-the-retail-workforce` (Women in the retail workforce)

Placements:

- organizational / industries / Retail / General (sK17286, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Gross leaseable area

- id: `kpi.retail.gross-leaseable-area`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Gross leaseable area measures that result inside Retail, subcategory General. The unit is currency. The formula is A, where A is Gross leaseable area. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Gross leaseable area on the desired side of its target for this period?

Inputs:

- `metric.gross-leaseable-area` (Gross leaseable area)

Placements:

- organizational / industries / Retail / General (sK4540, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Floor space by selected kind of business

- id: `kpi.retail.floor-space-by-selected-kind-of-business`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Floor space by selected kind of business measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Floor space by selected kind of business. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Floor space by selected kind of business on the desired side of its target for this period?

Inputs:

- `metric.floor-space-by-selected-kind-of-business` (Floor space by selected kind of business)

Placements:

- organizational / industries / Retail / General (sK17201, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sales per unit area

- id: `kpi.retail.sales-per-unit-area`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Sales per unit area measures that result inside Retail, subcategory General. The unit is currency. The formula is A / B, where A is Sales, B is unit area. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sales per unit area on the desired side of its target for this period?

Inputs:

- `metric.sales` (Sales)
- `metric.unit-area` (unit area)

Placements:

- organizational / industries / Retail / General (sK4543, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Free disposable plastic check-out bags

- id: `kpi.retail.free-disposable-plastic-check-out-bags`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Free disposable plastic check-out bags measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Free disposable plastic check-out bags. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Free disposable plastic check-out bags on the desired side of its target for this period?

Inputs:

- `metric.free-disposable-plastic-check-out-bags` (Free disposable plastic check-out bags)

Placements:

- organizational / industries / Retail / General (sK17321, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Toy selling items

- id: `kpi.retail.toy-selling-items`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Toy selling items measures that result inside Retail, subcategory General. The unit is currency. The formula is A, where A is Toy selling items. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Toy selling items on the desired side of its target for this period?

Inputs:

- `metric.toy-selling-items` (Toy selling items)

Placements:

- organizational / industries / Retail / General (sK4545, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Holiday employment

- id: `kpi.retail.holiday-employment`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Holiday employment measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Holiday employment. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Holiday employment on the desired side of its target for this period?

Inputs:

- `metric.holiday-employment` (Holiday employment)

Placements:

- organizational / industries / Retail / General (sK17482, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Inventory shirktags

- id: `kpi.retail.inventory-shirktags`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Inventory shirktags measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Inventory shirktags. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Inventory shirktags on the desired side of its target for this period?

Inputs:

- `metric.inventory-shirktags` (Inventory shirktags)

Placements:

- organizational / industries / Retail / General (sK17662, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Level of staff, employees with stakeholders

- id: `kpi.retail.level-of-staff-employees-with-stakeholders`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Level of staff, employees with stakeholders measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Level of staff, employees with stakeholders. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Level of staff, employees with stakeholders on the desired side of its target for this period?

Inputs:

- `metric.level-of-staff-employees-with-stakeholders` (Level of staff, employees with stakeholders)

Placements:

- organizational / industries / Retail / General (sK17774, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Level of information provided to consumers

- id: `kpi.retail.level-of-information-provided-to-consumers`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Level of information provided to consumers measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Level of information provided to consumers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Level of information provided to consumers on the desired side of its target for this period?

Inputs:

- `metric.level-of-information-provided-to-consumers` (Level of information provided to consumers)

Placements:

- organizational / industries / Retail / General (sK17775, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Size of grocery bill

- id: `kpi.retail.size-of-grocery-bill`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Size of grocery bill measures that result inside Retail, subcategory General. The unit is currency. The formula is A, where A is Size of grocery bill. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Size of grocery bill on the desired side of its target for this period?

Inputs:

- `metric.size-of-grocery-bill` (Size of grocery bill)

Placements:

- organizational / industries / Retail / General (sK4574, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Level of quality procedure for controlled food products

- id: `kpi.retail.level-of-quality-procedure-for-controlled-food-products`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.retail.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Level of quality procedure for controlled food products measures that result inside Retail, subcategory General. The unit is count. The formula is A, where A is Level of quality procedure for controlled food products. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Level of quality procedure for controlled food products on the desired side of its target for this period?

Inputs:

- `metric.level-of-quality-procedure-for-controlled-food-products` (Level of quality procedure for controlled food products)

Placements:

- organizational / industries / Retail / General (sK17779, page_0173)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
