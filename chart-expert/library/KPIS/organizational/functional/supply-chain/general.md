# Supply Chain / General

Context: organizational. Group: functional. KPIs: 59.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Product return rate

- id: `kpi.supply-chain.product-return-rate`
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

Product return rate measures that result inside Supply Chain, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is numerator of Product return rate, B is base of Product return rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Product return rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-product-return-rate` (numerator of Product return rate)
- `metric.base-of-product-return-rate` (base of Product return rate)

Placements:

- organizational / functional / Supply Chain / General (xS5S5, page_0057)

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

### Delivered in-Full, On-Time

- id: `kpi.supply-chain.delivered-in-full-on-time`
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

Delivered in-Full, On-Time measures that result inside Supply Chain, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Delivered in-Full, On-Time, B is whole named by Delivered in-Full, On-Time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Delivered in-Full, On-Time on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-delivered-in-full-on-time` (part named by Delivered in-Full, On-Time)
- `metric.whole-named-by-delivered-in-full-on-time` (whole named by Delivered in-Full, On-Time)

Placements:

- organizational / functional / Supply Chain / General (xK1599, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Order entry accuracy

- id: `kpi.supply-chain.order-entry-accuracy`
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

Order entry accuracy measures that result inside Supply Chain, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Order entry accuracy, B is whole named by Order entry accuracy. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Order entry accuracy on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-order-entry-accuracy` (part named by Order entry accuracy)
- `metric.whole-named-by-order-entry-accuracy` (whole named by Order entry accuracy)

Placements:

- organizational / functional / Supply Chain / General (xK1613, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### 'Supply chain response time

- id: `kpi.supply-chain.supply-chain-response-time`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

'Supply chain response time measures that result inside Supply Chain, subcategory General. The unit is currency. The formula is A, where A is 'Supply chain response time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is 'Supply chain response time on the desired side of its target for this period?

Inputs:

- `metric.supply-chain-response-time` ('Supply chain response time)

Placements:

- organizational / functional / Supply Chain / General (xK1616, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Order processing time

- id: `kpi.supply-chain.order-processing-time`
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

Order processing time measures that result inside Supply Chain, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Order processing time, B is whole named by Order processing time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Order processing time on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-order-processing-time` (part named by Order processing time)
- `metric.whole-named-by-order-processing-time` (whole named by Order processing time)

Placements:

- organizational / functional / Supply Chain / General (xK1626, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Order fulfillment lead time

- id: `kpi.supply-chain.order-fulfillment-lead-time`
- kind: kpi
- unit: count
- direction: down
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Order fulfillment lead time measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Order fulfillment lead time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Order fulfillment lead time on the desired side of its target for this period?

Inputs:

- `metric.order-fulfillment-lead-time` (Order fulfillment lead time)

Placements:

- organizational / functional / Supply Chain / General (xK1630, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Order receipt to order entry complete time

- id: `kpi.supply-chain.order-receipt-to-order-entry-complete-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Order receipt to order entry complete time measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Order receipt to order entry complete time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Order receipt to order entry complete time on the desired side of its target for this period?

Inputs:

- `metric.order-receipt-to-order-entry-complete-time` (Order receipt to order entry complete time)

Placements:

- organizational / functional / Supply Chain / General (xK1632, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Scheduling to customer request

- id: `kpi.supply-chain.scheduling-to-customer-request`
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

Scheduling to customer request measures that result inside Supply Chain, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Scheduling, B is customer request. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Scheduling to customer request on the desired side of its target for this period?

Inputs:

- `metric.scheduling` (Scheduling)
- `metric.customer-request` (customer request)

Placements:

- organizational / functional / Supply Chain / General (xK1635, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Delivery to request date

- id: `kpi.supply-chain.delivery-to-request-date`
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

Delivery to request date measures that result inside Supply Chain, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Delivery, B is request date. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Delivery to request date on the desired side of its target for this period?

Inputs:

- `metric.delivery` (Delivery)
- `metric.request-date` (request date)

Placements:

- organizational / functional / Supply Chain / General (xK2425, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Delivery to commit date

- id: `kpi.supply-chain.delivery-to-commit-date`
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

Delivery to commit date measures that result inside Supply Chain, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Delivery, B is commit date. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Delivery to commit date on the desired side of its target for this period?

Inputs:

- `metric.delivery` (Delivery)
- `metric.commit-date` (commit date)

Placements:

- organizational / functional / Supply Chain / General (xK2426, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time from customer authorization to order receipt

- id: `kpi.supply-chain.time-from-customer-authorization-to-order-receipt`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time from customer authorization to order receipt measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Time from customer authorization to order receipt. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time from customer authorization to order receipt on the desired side of its target for this period?

Inputs:

- `metric.time-from-customer-authorization-to-order-receipt` (Time from customer authorization to order receipt)

Placements:

- organizational / functional / Supply Chain / General (xK2427, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Order entry complete to start manufacture time

- id: `kpi.supply-chain.order-entry-complete-to-start-manufacture-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Order entry complete to start manufacture time measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Order entry complete to start manufacture time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Order entry complete to start manufacture time on the desired side of its target for this period?

Inputs:

- `metric.order-entry-complete-to-start-manufacture-time` (Order entry complete to start manufacture time)

Placements:

- organizational / functional / Supply Chain / General (xK2428, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Start manufacture to order complete manufacture time

- id: `kpi.supply-chain.start-manufacture-to-order-complete-manufacture-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Start manufacture to order complete manufacture time measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Start manufacture to order complete manufacture time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Start manufacture to order complete manufacture time on the desired side of its target for this period?

Inputs:

- `metric.start-manufacture-to-order-complete-manufacture-time` (Start manufacture to order complete manufacture time)

Placements:

- organizational / functional / Supply Chain / General (xK2429, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Order complete manufacture to customer receipt of order

- id: `kpi.supply-chain.order-complete-manufacture-to-customer-receipt-of-order`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Order complete manufacture to customer receipt of order measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Order complete manufacture to customer receipt of order. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Order complete manufacture to customer receipt of order on the desired side of its target for this period?

Inputs:

- `metric.order-complete-manufacture-to-customer-receipt-of-order` (Order complete manufacture to customer receipt of order)

Placements:

- organizational / functional / Supply Chain / General (xK2430, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Customer receipt of order to installation complete time

- id: `kpi.supply-chain.customer-receipt-of-order-to-installation-complete-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Customer receipt of order to installation complete time measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Customer receipt of order to installation complete time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Customer receipt of order to installation complete time on the desired side of its target for this period?

Inputs:

- `metric.customer-receipt-of-order-to-installation-complete-time` (Customer receipt of order to installation complete time)

Placements:

- organizational / functional / Supply Chain / General (xK2431, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cash-to-cash cycle time

- id: `kpi.supply-chain.cash-to-cash-cycle-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cash-to-cash cycle time measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Cash-to-cash cycle time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cash-to-cash cycle time on the desired side of its target for this period?

Inputs:

- `metric.cash-to-cash-cycle-time` (Cash-to-cash cycle time)

Placements:

- organizational / functional / Supply Chain / General (xK2432, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Days sales outstanding (DSO)

- id: `kpi.supply-chain.days-sales-outstanding-dso`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Days sales outstanding (DSO) measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Days sales outstanding (DSO). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Days sales outstanding (DSO) on the desired side of its target for this period?

Inputs:

- `metric.days-sales-outstanding-dso` (Days sales outstanding (DSO))

Placements:

- organizational / functional / Supply Chain / General (xK2434, page_0057)

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

### Supply chain management cost

- id: `kpi.supply-chain.supply-chain-management-cost`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Supply chain management cost measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Supply chain management cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Supply chain management cost on the desired side of its target for this period?

Inputs:

- `metric.supply-chain-management-cost` (Supply chain management cost)

Placements:

- organizational / functional / Supply Chain / General (xK2437, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Order management cost

- id: `kpi.supply-chain.order-management-cost`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Order management cost measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Order management cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Order management cost on the desired side of its target for this period?

Inputs:

- `metric.order-management-cost` (Order management cost)

Placements:

- organizational / functional / Supply Chain / General (xK2438, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### If for out supply chain

- id: `kpi.supply-chain.if-for-out-supply-chain`
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

If for out supply chain measures that result inside Supply Chain, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by If for out supply chain, B is whole named by If for out supply chain. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is If for out supply chain on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-if-for-out-supply-chain` (part named by If for out supply chain)
- `metric.whole-named-by-if-for-out-supply-chain` (whole named by If for out supply chain)

Placements:

- organizational / functional / Supply Chain / General (xK2431, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Supply chain related order management cost

- id: `kpi.supply-chain.supply-chain-related-order-management-cost`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Supply chain related order management cost measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Supply chain related order management cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Supply chain related order management cost on the desired side of its target for this period?

Inputs:

- `metric.supply-chain-related-order-management-cost` (Supply chain related order management cost)

Placements:

- organizational / functional / Supply Chain / General (xK2443, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### The supply chain related finance and planning cost

- id: `kpi.supply-chain.the-supply-chain-related-finance-and-planning-cost`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

The supply chain related finance and planning cost measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is The supply chain related finance and planning cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is The supply chain related finance and planning cost on the desired side of its target for this period?

Inputs:

- `metric.the-supply-chain-related-finance-and-planning-cost` (The supply chain related finance and planning cost)

Placements:

- organizational / functional / Supply Chain / General (xK2444, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Return management costs

- id: `kpi.supply-chain.return-management-costs`
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

Return management costs measures that result inside Supply Chain, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Return management costs, B is whole named by Return management costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Return management costs on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-return-management-costs` (part named by Return management costs)
- `metric.whole-named-by-return-management-costs` (whole named by Return management costs)

Placements:

- organizational / functional / Supply Chain / General (xK2446, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Lines per order

- id: `kpi.supply-chain.lines-per-order`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Lines per order measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A / B, where A is Lines, B is order. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Lines per order on the desired side of its target for this period?

Inputs:

- `metric.lines` (Lines)
- `metric.order` (order)

Placements:

- organizational / functional / Supply Chain / General (xK2422, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Full part for ship-from stock

- id: `kpi.supply-chain.full-part-for-ship-from-stock`
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

Full part for ship-from stock measures that result inside Supply Chain, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Full part for ship-from stock, B is whole named by Full part for ship-from stock. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Full part for ship-from stock on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-full-part-for-ship-from-stock` (part named by Full part for ship-from stock)
- `metric.whole-named-by-full-part-for-ship-from-stock` (whole named by Full part for ship-from stock)

Placements:

- organizational / functional / Supply Chain / General (xK2279, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Upside supply chain flexibility

- id: `kpi.supply-chain.upside-supply-chain-flexibility`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Upside supply chain flexibility measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Upside supply chain flexibility. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Upside supply chain flexibility on the desired side of its target for this period?

Inputs:

- `metric.upside-supply-chain-flexibility` (Upside supply chain flexibility)

Placements:

- organizational / functional / Supply Chain / General (xK2732, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Adherence to delivery schedule

- id: `kpi.supply-chain.adherence-to-delivery-schedule`
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

Adherence to delivery schedule measures that result inside Supply Chain, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Adherence, B is delivery schedule. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Adherence to delivery schedule on the desired side of its target for this period?

Inputs:

- `metric.adherence` (Adherence)
- `metric.delivery-schedule` (delivery schedule)

Placements:

- organizational / functional / Supply Chain / General (xK2735, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unshakable cost

- id: `kpi.supply-chain.unshakable-cost`
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

Unshakable cost measures that result inside Supply Chain, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Unshakable cost, B is whole named by Unshakable cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unshakable cost on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-unshakable-cost` (part named by Unshakable cost)
- `metric.whole-named-by-unshakable-cost` (whole named by Unshakable cost)

Placements:

- organizational / functional / Supply Chain / General (xK2736, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost per line dispatched

- id: `kpi.supply-chain.cost-per-line-dispatched`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.supply-chain.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost per line dispatched measures that result inside Supply Chain, subcategory General. The unit is percent. The formula is A / B, where A is Cost, B is line dispatched. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost per line dispatched on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.line-dispatched` (line dispatched)

Placements:

- organizational / functional / Supply Chain / General (xK2740, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Software used to support supply chain

- id: `kpi.supply-chain.software-used-to-support-supply-chain`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Software used to support supply chain measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Software used to support supply chain. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Software used to support supply chain on the desired side of its target for this period?

Inputs:

- `metric.software-used-to-support-supply-chain` (Software used to support supply chain)

Placements:

- organizational / functional / Supply Chain / General (xK2741, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Documents per trade transaction

- id: `kpi.supply-chain.documents-per-trade-transaction`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Documents per trade transaction measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A / B, where A is Documents, B is trade transaction. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Documents per trade transaction on the desired side of its target for this period?

Inputs:

- `metric.documents` (Documents)
- `metric.trade-transaction` (trade transaction)

Placements:

- organizational / functional / Supply Chain / General (xK2864, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Customers errors placing orders

- id: `kpi.supply-chain.customers-errors-placing-orders`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Customers errors placing orders measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Customers errors placing orders. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Customers errors placing orders on the desired side of its target for this period?

Inputs:

- `metric.customers-errors-placing-orders` (Customers errors placing orders)

Placements:

- organizational / functional / Supply Chain / General (xK2950, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to order processing

- id: `kpi.supply-chain.employees-allocated-to-order-processing`
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

Employees allocated to order processing measures that result inside Supply Chain, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is order processing. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to order processing on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.order-processing` (order processing)

Placements:

- organizational / functional / Supply Chain / General (xK3345, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Freight cost per ton shipped

- id: `kpi.supply-chain.freight-cost-per-ton-shipped`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Freight cost per ton shipped measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A / B, where A is Freight cost, B is ton shipped. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Freight cost per ton shipped on the desired side of its target for this period?

Inputs:

- `metric.freight-cost` (Freight cost)
- `metric.ton-shipped` (ton shipped)

Placements:

- organizational / functional / Supply Chain / General (xK3749, page_0057)
- organizational / industries / Sport / Organizational » Industries (sK3749, page_0197)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Intermediaries in raw material supply

- id: `kpi.supply-chain.intermediaries-in-raw-material-supply`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Intermediaries in raw material supply measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Intermediaries in raw material supply. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Intermediaries in raw material supply on the desired side of its target for this period?

Inputs:

- `metric.intermediaries-in-raw-material-supply` (Intermediaries in raw material supply)

Placements:

- organizational / functional / Supply Chain / General (xK4363, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Processing time in days

- id: `kpi.supply-chain.processing-time-in-days`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Processing time in days measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Processing time in days. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Processing time in days on the desired side of its target for this period?

Inputs:

- `metric.processing-time-in-days` (Processing time in days)

Placements:

- organizational / functional / Supply Chain / General (xK4812, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Relative asset utilization frequency

- id: `kpi.supply-chain.relative-asset-utilization-frequency`
- kind: kpi
- unit: count
- direction: corridor
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Relative asset utilization frequency measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Relative asset utilization frequency. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Relative asset utilization frequency on the desired side of its target for this period?

Inputs:

- `metric.relative-asset-utilization-frequency` (Relative asset utilization frequency)

Placements:

- organizational / functional / Supply Chain / General (xK6950, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Order cycle time

- id: `kpi.supply-chain.order-cycle-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Order cycle time measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Order cycle time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Order cycle time on the desired side of its target for this period?

Inputs:

- `metric.order-cycle-time` (Order cycle time)

Placements:

- organizational / functional / Supply Chain / General (xK3204, page_0057)
- organizational / industries / Non-profit / Organizational » Industries (▲K2304, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Customer order path

- id: `kpi.supply-chain.customer-order-path`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Customer order path measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Customer order path. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Customer order path on the desired side of its target for this period?

Inputs:

- `metric.customer-order-path` (Customer order path)

Placements:

- organizational / functional / Supply Chain / General (xK3203, page_0057)
- organizational / industries / Non-profit / Organizational » Industries (▲K2305, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Length of #haul

- id: `kpi.supply-chain.length-of-haul`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Length of #haul measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Length of #haul. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Length of #haul on the desired side of its target for this period?

Inputs:

- `metric.length-of-haul` (Length of #haul)

Placements:

- organizational / functional / Supply Chain / General (xK3206, page_0057)
- organizational / industries / Non-profit / Organizational » Industries (▲K2306, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Empty miles factor

- id: `kpi.supply-chain.empty-miles-factor`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Empty miles factor measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Empty miles factor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Empty miles factor on the desired side of its target for this period?

Inputs:

- `metric.empty-miles-factor` (Empty miles factor)

Placements:

- organizational / functional / Supply Chain / General (xK3207, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Age of revenue equipment

- id: `kpi.supply-chain.age-of-revenue-equipment`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Age of revenue equipment measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Age of revenue equipment. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Age of revenue equipment on the desired side of its target for this period?

Inputs:

- `metric.age-of-revenue-equipment` (Age of revenue equipment)

Placements:

- organizational / functional / Supply Chain / General (xK3208, page_0057)
- organizational / industries / Non-profit / Organizational » Industries (▲K2308, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Equipment utilization rate

- id: `kpi.supply-chain.equipment-utilization-rate`
- kind: kpi
- unit: count
- direction: corridor
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Equipment utilization rate measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Equipment utilization rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Equipment utilization rate on the desired side of its target for this period?

Inputs:

- `metric.equipment-utilization-rate` (Equipment utilization rate)

Placements:

- organizational / functional / Supply Chain / General (xK3029, page_0057)
- organizational / industries / Non-profit / Organizational » Industries (▲K2309, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Tractor operating life

- id: `kpi.supply-chain.tractor-operating-life`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Tractor operating life measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Tractor operating life. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Tractor operating life on the desired side of its target for this period?

Inputs:

- `metric.tractor-operating-life` (Tractor operating life)

Placements:

- organizational / functional / Supply Chain / General (xK3030, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Trailer operating life

- id: `kpi.supply-chain.trailer-operating-life`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Trailer operating life measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Trailer operating life. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Trailer operating life on the desired side of its target for this period?

Inputs:

- `metric.trailer-operating-life` (Trailer operating life)

Placements:

- organizational / functional / Supply Chain / General (xK2931, page_0057)
- organizational / industries / Non-profit / Organizational » Industries (▲K2311, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Tractors in service

- id: `kpi.supply-chain.tractors-in-service`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Tractors in service measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Tractors in service. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Tractors in service on the desired side of its target for this period?

Inputs:

- `metric.tractors-in-service` (Tractors in service)

Placements:

- organizational / functional / Supply Chain / General (xK3033, page_0057)
- organizational / industries / Non-profit / Organizational » Industries (▲K2312, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Trailers in service

- id: `kpi.supply-chain.trailers-in-service`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Trailers in service measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Trailers in service. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Trailers in service on the desired side of its target for this period?

Inputs:

- `metric.trailers-in-service` (Trailers in service)

Placements:

- organizational / functional / Supply Chain / General (xK3033, page_0057)
- organizational / industries / Non-profit / Organizational » Industries (▲K2313, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hundredweight

- id: `kpi.supply-chain.hundredweight`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Hundredweight measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Hundredweight. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hundredweight on the desired side of its target for this period?

Inputs:

- `metric.hundredweight` (Hundredweight)

Placements:

- organizational / functional / Supply Chain / General (xK2034, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Loaded miles per load

- id: `kpi.supply-chain.loaded-miles-per-load`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Loaded miles per load measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A / B, where A is Loaded miles, B is load. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Loaded miles per load on the desired side of its target for this period?

Inputs:

- `metric.loaded-miles` (Loaded miles)
- `metric.load` (load)

Placements:

- organizational / functional / Supply Chain / General (xK2035, page_0057)
- organizational / industries / Non-profit / Organizational » Industries (▲K2315, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Pounds per shipment

- id: `kpi.supply-chain.pounds-per-shipment`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Pounds per shipment measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A / B, where A is Pounds, B is shipment. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Pounds per shipment on the desired side of its target for this period?

Inputs:

- `metric.pounds` (Pounds)
- `metric.shipment` (shipment)

Placements:

- organizational / functional / Supply Chain / General (xK3036, page_0057)
- organizational / industries / Non-profit / Organizational » Industries (▲K2316, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue per hundredweight

- id: `kpi.supply-chain.revenue-per-hundredweight`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Revenue per hundredweight measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A / B, where A is Revenue, B is hundredweight. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue per hundredweight on the desired side of its target for this period?

Inputs:

- `metric.revenue` (Revenue)
- `metric.hundredweight` (hundredweight)

Placements:

- organizational / functional / Supply Chain / General (xK3037, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Reversed per load mile

- id: `kpi.supply-chain.reversed-per-load-mile`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Reversed per load mile measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A / B, where A is Reversed, B is load mile. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Reversed per load mile on the desired side of its target for this period?

Inputs:

- `metric.reversed` (Reversed)
- `metric.load-mile` (load mile)

Placements:

- organizational / functional / Supply Chain / General (xK3038, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Reversed per shipment

- id: `kpi.supply-chain.reversed-per-shipment`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Reversed per shipment measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A / B, where A is Reversed, B is shipment. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Reversed per shipment on the desired side of its target for this period?

Inputs:

- `metric.reversed` (Reversed)
- `metric.shipment` (shipment)

Placements:

- organizational / functional / Supply Chain / General (xK3039, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Shipments

- id: `kpi.supply-chain.shipments`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Shipments measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Shipments. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Shipments on the desired side of its target for this period?

Inputs:

- `metric.shipments` (Shipments)

Placements:

- organizational / functional / Supply Chain / General (xK3040, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Shipments per business day

- id: `kpi.supply-chain.shipments-per-business-day`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Shipments per business day measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A / B, where A is Shipments, B is business day. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Shipments per business day on the desired side of its target for this period?

Inputs:

- `metric.shipments` (Shipments)
- `metric.business-day` (business day)

Placements:

- organizational / functional / Supply Chain / General (xK3041, page_0057)
- organizational / industries / Non-profit / Organizational » Industries (▲K2314, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Railcars on line

- id: `kpi.supply-chain.railcars-on-line`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Railcars on line measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Railcars on line. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Railcars on line on the desired side of its target for this period?

Inputs:

- `metric.railcars-on-line` (Railcars on line)

Placements:

- organizational / functional / Supply Chain / General (xK3042, page_0057)
- organizational / industries / Non-profit / Organizational » Industries (▲K2314, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Terminal dwell time

- id: `kpi.supply-chain.terminal-dwell-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.supply-chain.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Terminal dwell time measures that result inside Supply Chain, subcategory General. The unit is count. The formula is A, where A is Terminal dwell time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Terminal dwell time on the desired side of its target for this period?

Inputs:

- `metric.terminal-dwell-time` (Terminal dwell time)

Placements:

- organizational / functional / Supply Chain / General (xK3043, page_0057)
- organizational / industries / Non-profit / Organizational » Industries (▲K2314, page_0154)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
