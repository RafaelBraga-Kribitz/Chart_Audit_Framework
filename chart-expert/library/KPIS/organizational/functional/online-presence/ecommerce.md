# Online Presence / eCommerce

Context: organizational. Group: functional. KPIs: 46.

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

### Coupon conversion

- id: `kpi.online-presence.coupon-conversion`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Coupon conversion measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is part named by Coupon conversion, B is whole named by Coupon conversion. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Coupon conversion on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-coupon-conversion` (part named by Coupon conversion)
- `metric.whole-named-by-coupon-conversion` (whole named by Coupon conversion)

Placements:

- organizational / functional / Online Presence / eCommerce (x870, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Order value (OV)

- id: `kpi.online-presence.order-value-ov`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Order value (OV) measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is part named by Order value (OV), B is whole named by Order value (OV). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Order value (OV) on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-order-value-ov` (part named by Order value (OV))
- `metric.whole-named-by-order-value-ov` (whole named by Order value (OV))

Placements:

- organizational / functional / Online Presence / eCommerce (x878, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Value to purchase

- id: `kpi.online-presence.value-to-purchase`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Value to purchase measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is Value, B is purchase. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Value to purchase on the desired side of its target for this period?

Inputs:

- `metric.value` (Value)
- `metric.purchase` (purchase)

Placements:

- organizational / functional / Online Presence / eCommerce (x879, page_0042)

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

### New customer on first visit ratio

- id: `kpi.online-presence.new-customer-on-first-visit-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

New customer on first visit ratio measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A, where A is New customer on first visit ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New customer on first visit ratio on the desired side of its target for this period?

Inputs:

- `metric.new-customer-on-first-visit-ratio` (New customer on first visit ratio)

Placements:

- organizational / functional / Online Presence / eCommerce (x434, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue from new visitors

- id: `kpi.online-presence.revenue-from-new-visitors`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Revenue from new visitors measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is Revenue, B is new visitors. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue from new visitors on the desired side of its target for this period?

Inputs:

- `metric.revenue` (Revenue)
- `metric.new-visitors` (new visitors)

Placements:

- organizational / functional / Online Presence / eCommerce (x435, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost per order (CPO)

- id: `kpi.online-presence.cost-per-order-cpo`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Cost per order (CPO) measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is A / B, where A is Cost, B is order (CPO). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost per order (CPO) on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.order-cpo` (order (CPO))

Placements:

- organizational / functional / Online Presence / eCommerce (x1431, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Shopping carts abandoned

- id: `kpi.online-presence.shopping-carts-abandoned`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Shopping carts abandoned measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A, where A is Shopping carts abandoned. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Shopping carts abandoned on the desired side of its target for this period?

Inputs:

- `metric.shopping-carts-abandoned` (Shopping carts abandoned)

Placements:

- organizational / functional / Online Presence / eCommerce (x2469, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unique online buyers

- id: `kpi.online-presence.unique-online-buyers`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Unique online buyers measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A, where A is Unique online buyers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unique online buyers on the desired side of its target for this period?

Inputs:

- `metric.unique-online-buyers` (Unique online buyers)

Placements:

- organizational / functional / Online Presence / eCommerce (x2475, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue from first time online customers

- id: `kpi.online-presence.revenue-from-first-time-online-customers`
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

Revenue from first time online customers measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is Revenue, B is first time online customers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue from first time online customers on the desired side of its target for this period?

Inputs:

- `metric.revenue` (Revenue)
- `metric.first-time-online-customers` (first time online customers)

Placements:

- organizational / functional / Online Presence / eCommerce (x2490, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Shopping cart session

- id: `kpi.online-presence.shopping-cart-session`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Shopping cart session measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is part named by Shopping cart session, B is whole named by Shopping cart session. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Shopping cart session on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-shopping-cart-session` (part named by Shopping cart session)
- `metric.whole-named-by-shopping-cart-session` (whole named by Shopping cart session)

Placements:

- organizational / functional / Online Presence / eCommerce (x2491, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Shopping cart conversion rate

- id: `kpi.online-presence.shopping-cart-conversion-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Shopping cart conversion rate measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is numerator of Shopping cart conversion rate, B is base of Shopping cart conversion rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Shopping cart conversion rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-shopping-cart-conversion-rate` (numerator of Shopping cart conversion rate)
- `metric.base-of-shopping-cart-conversion-rate` (base of Shopping cart conversion rate)

Placements:

- organizational / functional / Online Presence / eCommerce (x2492, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue from first time customers to repeated customers ratio

- id: `kpi.online-presence.revenue-from-first-time-customers-to-repeated-customers-ratio`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Revenue from first time customers to repeated customers ratio measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A, where A is Revenue from first time customers to repeated customers ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue from first time customers to repeated customers ratio on the desired side of its target for this period?

Inputs:

- `metric.revenue-from-first-time-customers-to-repeated-customers-ratio` (Revenue from first time customers to repeated customers ratio)

Placements:

- organizational / functional / Online Presence / eCommerce (x2495, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost per conversion

- id: `kpi.online-presence.cost-per-conversion`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Cost per conversion measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is A / B, where A is Cost, B is conversion. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost per conversion on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.conversion` (conversion)

Placements:

- organizational / functional / Online Presence / eCommerce (x2501, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Returning customers on the site

- id: `kpi.online-presence.returning-customers-on-the-site`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Returning customers on the site measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is part named by Returning customers on the site, B is whole named by Returning customers on the site. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Returning customers on the site on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-returning-customers-on-the-site` (part named by Returning customers on the site)
- `metric.whole-named-by-returning-customers-on-the-site` (whole named by Returning customers on the site)

Placements:

- organizational / functional / Online Presence / eCommerce (x2502, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New customers on site

- id: `kpi.online-presence.new-customers-on-site`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

New customers on site measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is part named by New customers on site, B is whole named by New customers on site. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New customers on site on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-new-customers-on-site` (part named by New customers on site)
- `metric.whole-named-by-new-customers-on-site` (whole named by New customers on site)

Placements:

- organizational / functional / Online Presence / eCommerce (x2503, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Shopping cart start rate

- id: `kpi.online-presence.shopping-cart-start-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Shopping cart start rate measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is numerator of Shopping cart start rate, B is base of Shopping cart start rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Shopping cart start rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-shopping-cart-start-rate` (numerator of Shopping cart start rate)
- `metric.base-of-shopping-cart-start-rate` (base of Shopping cart start rate)

Placements:

- organizational / functional / Online Presence / eCommerce (x2504, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Browse session product page

- id: `kpi.online-presence.browse-session-product-page`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Browse session product page measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is part named by Browse session product page, B is whole named by Browse session product page. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Browse session product page on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-browse-session-product-page` (part named by Browse session product page)
- `metric.whole-named-by-browse-session-product-page` (whole named by Browse session product page)

Placements:

- organizational / functional / Online Presence / eCommerce (x2511, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Product views per session

- id: `kpi.online-presence.product-views-per-session`
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

Product views per session measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A / B, where A is Product views, B is session. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Product views per session on the desired side of its target for this period?

Inputs:

- `metric.product-views` (Product views)
- `metric.session` (session)

Placements:

- organizational / functional / Online Presence / eCommerce (x2517, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Shopping session length

- id: `kpi.online-presence.shopping-session-length`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Shopping session length measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A, where A is Shopping session length. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Shopping session length on the desired side of its target for this period?

Inputs:

- `metric.shopping-session-length` (Shopping session length)

Placements:

- organizational / functional / Online Presence / eCommerce (x2519, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Shopping cartest

- id: `kpi.online-presence.shopping-cartest`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Shopping cartest measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A, where A is Shopping cartest. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Shopping cartest on the desired side of its target for this period?

Inputs:

- `metric.shopping-cartest` (Shopping cartest)

Placements:

- organizational / functional / Online Presence / eCommerce (x2521, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Level of shipping errors

- id: `kpi.online-presence.level-of-shipping-errors`
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

Level of shipping errors measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is Level, B is shipping errors. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Level of shipping errors on the desired side of its target for this period?

Inputs:

- `metric.level` (Level)
- `metric.shipping-errors` (shipping errors)

Placements:

- organizational / functional / Online Presence / eCommerce (x2522, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue from repeat online customers

- id: `kpi.online-presence.revenue-from-repeat-online-customers`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Revenue from repeat online customers measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is Revenue, B is repeat online customers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue from repeat online customers on the desired side of its target for this period?

Inputs:

- `metric.revenue` (Revenue)
- `metric.repeat-online-customers` (repeat online customers)

Placements:

- organizational / functional / Online Presence / eCommerce (x2529, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Level of stock-outs

- id: `kpi.online-presence.level-of-stock-outs`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Level of stock-outs measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is Level, B is stock-outs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Level of stock-outs on the desired side of its target for this period?

Inputs:

- `metric.level` (Level)
- `metric.stock-outs` (stock-outs)

Placements:

- organizational / functional / Online Presence / eCommerce (x2537, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Channel-specific products and services

- id: `kpi.online-presence.channel-specific-products-and-services`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Channel-specific products and services measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A, where A is Channel-specific products and services. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Channel-specific products and services on the desired side of its target for this period?

Inputs:

- `metric.channel-specific-products-and-services` (Channel-specific products and services)

Placements:

- organizational / functional / Online Presence / eCommerce (x2538, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue per visitor

- id: `kpi.online-presence.revenue-per-visitor`
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

Revenue per visitor measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A / B, where A is Revenue, B is visitor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue per visitor on the desired side of its target for this period?

Inputs:

- `metric.revenue` (Revenue)
- `metric.visitor` (visitor)

Placements:

- organizational / functional / Online Presence / eCommerce (x2542, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue per visit

- id: `kpi.online-presence.revenue-per-visit`
- kind: kpi
- unit: currency
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

Revenue per visit measures that result inside Online Presence, subcategory eCommerce. The unit is currency. The formula is A / B, where A is Revenue, B is visit. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue per visit on the desired side of its target for this period?

Inputs:

- `metric.revenue` (Revenue)
- `metric.visit` (visit)

Placements:

- organizational / functional / Online Presence / eCommerce (x2547, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Per visit value

- id: `kpi.online-presence.per-visit-value`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Per visit value measures that result inside Online Presence, subcategory eCommerce. The unit is currency. The formula is A, where A is Per visit value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Per visit value on the desired side of its target for this period?

Inputs:

- `metric.per-visit-value` (Per visit value)

Placements:

- organizational / functional / Online Presence / eCommerce (x2548, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Problems with customer order processing

- id: `kpi.online-presence.problems-with-customer-order-processing`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Problems with customer order processing measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A, where A is Problems with customer order processing. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Problems with customer order processing on the desired side of its target for this period?

Inputs:

- `metric.problems-with-customer-order-processing` (Problems with customer order processing)

Placements:

- organizational / functional / Online Presence / eCommerce (x2549, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Checkout completion rate

- id: `kpi.online-presence.checkout-completion-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Checkout completion rate measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is numerator of Checkout completion rate, B is base of Checkout completion rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Checkout completion rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-checkout-completion-rate` (numerator of Checkout completion rate)
- `metric.base-of-checkout-completion-rate` (base of Checkout completion rate)

Placements:

- organizational / functional / Online Presence / eCommerce (xR551, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Order session

- id: `kpi.online-presence.order-session`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Order session measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is part named by Order session, B is whole named by Order session. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Order session on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-order-session` (part named by Order session)
- `metric.whole-named-by-order-session` (whole named by Order session)

Placements:

- organizational / functional / Online Presence / eCommerce (xR553, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Shopping cart abandonment rate

- id: `kpi.online-presence.shopping-cart-abandonment-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Shopping cart abandonment rate measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is numerator of Shopping cart abandonment rate, B is base of Shopping cart abandonment rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Shopping cart abandonment rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-shopping-cart-abandonment-rate` (numerator of Shopping cart abandonment rate)
- `metric.base-of-shopping-cart-abandonment-rate` (base of Shopping cart abandonment rate)

Placements:

- organizational / functional / Online Presence / eCommerce (xR554, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### On same search conversion

- id: `kpi.online-presence.on-same-search-conversion`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

On same search conversion measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is part named by On same search conversion, B is whole named by On same search conversion. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is On same search conversion on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-on-same-search-conversion` (part named by On same search conversion)
- `metric.whole-named-by-on-same-search-conversion` (whole named by On same search conversion)

Placements:

- organizational / functional / Online Presence / eCommerce (xR555, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Frequency of sales transactions

- id: `kpi.online-presence.frequency-of-sales-transactions`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Frequency of sales transactions measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A, where A is Frequency of sales transactions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Frequency of sales transactions on the desired side of its target for this period?

Inputs:

- `metric.frequency-of-sales-transactions` (Frequency of sales transactions)

Placements:

- organizational / functional / Online Presence / eCommerce (xR556, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Checkout start rate

- id: `kpi.online-presence.checkout-start-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Checkout start rate measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is numerator of Checkout start rate, B is base of Checkout start rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Checkout start rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-checkout-start-rate` (numerator of Checkout start rate)
- `metric.base-of-checkout-start-rate` (base of Checkout start rate)

Placements:

- organizational / functional / Online Presence / eCommerce (xR558, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cart completion rate

- id: `kpi.online-presence.cart-completion-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Cart completion rate measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is numerator of Cart completion rate, B is base of Cart completion rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cart completion rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-cart-completion-rate` (numerator of Cart completion rate)
- `metric.base-of-cart-completion-rate` (base of Cart completion rate)

Placements:

- organizational / functional / Online Presence / eCommerce (xR560, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unique purchases

- id: `kpi.online-presence.unique-purchases`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Unique purchases measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A, where A is Unique purchases. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unique purchases on the desired side of its target for this period?

Inputs:

- `metric.unique-purchases` (Unique purchases)

Placements:

- organizational / functional / Online Presence / eCommerce (xR564, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Level of customer cost savings achieved

- id: `kpi.online-presence.level-of-customer-cost-savings-achieved`
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

Level of customer cost savings achieved measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is Level, B is customer cost savings achieved. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Level of customer cost savings achieved on the desired side of its target for this period?

Inputs:

- `metric.level` (Level)
- `metric.customer-cost-savings-achieved` (customer cost savings achieved)

Placements:

- organizational / functional / Online Presence / eCommerce (xR575, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New features added to the site

- id: `kpi.online-presence.new-features-added-to-the-site`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

New features added to the site measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A, where A is New features added to the site. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New features added to the site on the desired side of its target for this period?

Inputs:

- `metric.new-features-added-to-the-site` (New features added to the site)

Placements:

- organizational / functional / Online Presence / eCommerce (xR579, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Visits prior to conversion

- id: `kpi.online-presence.visits-prior-to-conversion`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Visits prior to conversion measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A, where A is Visits prior to conversion. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Visits prior to conversion on the desired side of its target for this period?

Inputs:

- `metric.visits-prior-to-conversion` (Visits prior to conversion)

Placements:

- organizational / functional / Online Presence / eCommerce (xR589, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Orders from first time customers to repeated customer ratio

- id: `kpi.online-presence.orders-from-first-time-customers-to-repeated-customer-ratio`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Orders from first time customers to repeated customer ratio measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A, where A is Orders from first time customers to repeated customer ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Orders from first time customers to repeated customer ratio on the desired side of its target for this period?

Inputs:

- `metric.orders-from-first-time-customers-to-repeated-customer-ratio` (Orders from first time customers to repeated customer ratio)

Placements:

- organizational / functional / Online Presence / eCommerce (xR591, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Shopping cart transactions completed

- id: `kpi.online-presence.shopping-cart-transactions-completed`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Shopping cart transactions completed measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A, where A is Shopping cart transactions completed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Shopping cart transactions completed on the desired side of its target for this period?

Inputs:

- `metric.shopping-cart-transactions-completed` (Shopping cart transactions completed)

Placements:

- organizational / functional / Online Presence / eCommerce (xR638, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue per unique customer

- id: `kpi.online-presence.revenue-per-unique-customer`
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

Revenue per unique customer measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A / B, where A is Revenue, B is unique customer. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue per unique customer on the desired side of its target for this period?

Inputs:

- `metric.revenue` (Revenue)
- `metric.unique-customer` (unique customer)

Placements:

- organizational / functional / Online Presence / eCommerce (xR773, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Customer transactions via the Internet

- id: `kpi.online-presence.customer-transactions-via-the-internet`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Customer transactions via the Internet measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is part named by Customer transactions via the Internet, B is whole named by Customer transactions via the Internet. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Customer transactions via the Internet on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-customer-transactions-via-the-internet` (part named by Customer transactions via the Internet)
- `metric.whole-named-by-customer-transactions-via-the-internet` (whole named by Customer transactions via the Internet)

Placements:

- organizational / functional / Online Presence / eCommerce (xR645, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Activity planning accounts (RMA)

- id: `kpi.online-presence.activity-planning-accounts-rma`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Activity planning accounts (RMA) measures that result inside Online Presence, subcategory eCommerce. The unit is count. The formula is A, where A is Activity planning accounts (RMA). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Activity planning accounts (RMA) on the desired side of its target for this period?

Inputs:

- `metric.activity-planning-accounts-rma` (Activity planning accounts (RMA))

Placements:

- organizational / functional / Online Presence / eCommerce (xR764, page_0042)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
