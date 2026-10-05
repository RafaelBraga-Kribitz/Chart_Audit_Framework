# Healthcare / Food and Beverage Service

Context: organizational. Group: industries. KPIs: 42.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Food costs from food sales

- id: `kpi.healthcare.food-costs-from-food-sales`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Food costs from food sales measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is percent. The formula is (A / B) * 100, where A is Food costs, B is food sales. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Food costs from food sales on the desired side of its target for this period?

Inputs:

- `metric.food-costs` (Food costs)
- `metric.food-sales` (food sales)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KPI # KSS130, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Food use hours labor

- id: `kpi.healthcare.food-use-hours-labor`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Food use hours labor measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A, where A is Food use hours labor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Food use hours labor on the desired side of its target for this period?

Inputs:

- `metric.food-use-hours-labor` (Food use hours labor)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KPI # KSS225, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New menu items

- id: `kpi.healthcare.new-menu-items`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

New menu items measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is percent. The formula is (A / B) * 100, where A is part named by New menu items, B is whole named by New menu items. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New menu items on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-new-menu-items` (part named by New menu items)
- `metric.whole-named-by-new-menu-items` (whole named by New menu items)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KPI # KSS221, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Guests

- id: `kpi.healthcare.guests`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Guests measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A, where A is Guests. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Guests on the desired side of its target for this period?

Inputs:

- `metric.guests` (Guests)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KPI # KSS225, page_0129)
- organizational / industries / Healthcare / Hotel/Accommodation (sB2325, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Customers satisfied with the time to be served

- id: `kpi.healthcare.customers-satisfied-with-the-time-to-be-served`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Customers satisfied with the time to be served measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is percent. The formula is (A / B) * 100, where A is Customers satisfied with the time, B is be served. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Customers satisfied with the time to be served on the desired side of its target for this period?

Inputs:

- `metric.customers-satisfied-with-the-time` (Customers satisfied with the time)
- `metric.be-served` (be served)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KPI # KSS264, page_0129)

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

### Reserved tables

- id: `kpi.healthcare.reserved-tables`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Reserved tables measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Reserved tables, B is whole named by Reserved tables. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Reserved tables on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-reserved-tables` (part named by Reserved tables)
- `metric.whole-named-by-reserved-tables` (whole named by Reserved tables)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KPI # KSS710, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Spent on equipment

- id: `kpi.healthcare.spent-on-equipment`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Spent on equipment measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is currency. The formula is A, where A is Spent on equipment. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Spent on equipment on the desired side of its target for this period?

Inputs:

- `metric.spent-on-equipment` (Spent on equipment)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KPI # KSS732, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Restaurant that apply principles of managing the purchasing process

- id: `kpi.healthcare.restaurant-that-apply-principles-of-managing-the-purchasing-process`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Restaurant that apply principles of managing the purchasing process measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is percent. The formula is (A / B) * 100, where A is Restaurant that apply principles, B is managing the purchasing process. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Restaurant that apply principles of managing the purchasing process on the desired side of its target for this period?

Inputs:

- `metric.restaurant-that-apply-principles` (Restaurant that apply principles)
- `metric.managing-the-purchasing-process` (managing the purchasing process)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KPI # KSS736, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Restaurants that apply principles of menu planning

- id: `kpi.healthcare.restaurants-that-apply-principles-of-menu-planning`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Restaurants that apply principles of menu planning measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is percent. The formula is (A / B) * 100, where A is Restaurants that apply principles, B is menu planning. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Restaurants that apply principles of menu planning on the desired side of its target for this period?

Inputs:

- `metric.restaurants-that-apply-principles` (Restaurants that apply principles)
- `metric.menu-planning` (menu planning)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KPI # KSS737, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Restaurants that apply principles of workplace safety and sanitation

- id: `kpi.healthcare.restaurants-that-apply-principles-of-workplace-safety-and-sanitation`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Restaurants that apply principles of workplace safety and sanitation measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is percent. The formula is (A / B) * 100, where A is Restaurants that apply principles, B is workplace safety and sanitation. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Restaurants that apply principles of workplace safety and sanitation on the desired side of its target for this period?

Inputs:

- `metric.restaurants-that-apply-principles` (Restaurants that apply principles)
- `metric.workplace-safety-and-sanitation` (workplace safety and sanitation)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KPI # KSS738, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Additional services provided by restaurant

- id: `kpi.healthcare.additional-services-provided-by-restaurant`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Additional services provided by restaurant measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A, where A is Additional services provided by restaurant. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Additional services provided by restaurant on the desired side of its target for this period?

Inputs:

- `metric.additional-services-provided-by-restaurant` (Additional services provided by restaurant)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KPI # KSS739, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Menu items

- id: `kpi.healthcare.menu-items`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Menu items measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A, where A is Menu items. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Menu items on the desired side of its target for this period?

Inputs:

- `metric.menu-items` (Menu items)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KPI # KSS740, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Product quality uniformity

- id: `kpi.healthcare.product-quality-uniformity`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Product quality uniformity measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A, where A is Product quality uniformity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Product quality uniformity on the desired side of its target for this period?

Inputs:

- `metric.product-quality-uniformity` (Product quality uniformity)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KPI # KSS741, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unavailability of menu items

- id: `kpi.healthcare.unavailability-of-menu-items`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Unavailability of menu items measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is percent. The formula is (A / B) * 100, where A is Unavailability, B is menu items. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unavailability of menu items on the desired side of its target for this period?

Inputs:

- `metric.unavailability` (Unavailability)
- `metric.menu-items` (menu items)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KPI # KSS742, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Guests per table

- id: `kpi.healthcare.guests-per-table`
- kind: kpi
- unit: count
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

Guests per table measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A / B, where A is Guests, B is table. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Guests per table on the desired side of its target for this period?

Inputs:

- `metric.guests` (Guests)
- `metric.table` (table)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS743, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### People per party (catering)

- id: `kpi.healthcare.people-per-party-catering`
- kind: kpi
- unit: count
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

People per party (catering) measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A / B, where A is People, B is party (catering). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is People per party (catering) on the desired side of its target for this period?

Inputs:

- `metric.people` (People)
- `metric.party-catering` (party (catering))

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS744, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Car are served over a span of time

- id: `kpi.healthcare.car-are-served-over-a-span-of-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Car are served over a span of time measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A, where A is Car are served over a span of time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Car are served over a span of time on the desired side of its target for this period?

Inputs:

- `metric.car-are-served-over-a-span-of-time` (Car are served over a span of time)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS746, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Length of time for which a given car waits at a drive-through seating area

- id: `kpi.healthcare.length-of-time-for-which-a-given-car-waits-at-a-drive-through-seating-ar`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Length of time for which a given car waits at a drive-through seating area measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A, where A is Length of time for which a given car waits at a drive-through seating area. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Length of time for which a given car waits at a drive-through seating area on the desired side of its target for this period?

Inputs:

- `metric.length-of-time-for-which-a-given-car-waits-at-a-drive-through-seating-ar` (Length of time for which a given car waits at a drive-through seating area)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS747, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Length of time between a car leaving the drive-through seating area and arriving at the pick-up window

- id: `kpi.healthcare.length-of-time-between-a-car-leaving-the-drive-through-seating-area-and`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Length of time between a car leaving the drive-through seating area and arriving at the pick-up window measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A, where A is Length of time between a car leaving the drive-through seating area and arriving at the pick-up window. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Length of time between a car leaving the drive-through seating area and arriving at the pick-up window on the desired side of its target for this period?

Inputs:

- `metric.length-of-time-between-a-car-leaving-the-drive-through-seating-area-and` (Length of time between a car leaving the drive-through seating area and arriving at the pick-up window)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS748, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Times the server speaks with the customer, while the customer is at the drive-through dining room

- id: `kpi.healthcare.times-the-server-speaks-with-the-customer-while-the-customer-is-at-the-d`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Times the server speaks with the customer, while the customer is at the drive-through dining room measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A, where A is Times the server speaks with the customer, while the customer is at the drive-through dining room. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Times the server speaks with the customer, while the customer is at the drive-through dining room on the desired side of its target for this period?

Inputs:

- `metric.times-the-server-speaks-with-the-customer-while-the-customer-is-at-the-d` (Times the server speaks with the customer, while the customer is at the drive-through dining room)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS749, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Times employees speak with each other while receiving a drive-through customer

- id: `kpi.healthcare.times-employees-speak-with-each-other-while-receiving-a-drive-through-cu`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Times employees speak with each other while receiving a drive-through customer measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A, where A is Times employees speak with each other while receiving a drive-through customer. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Times employees speak with each other while receiving a drive-through customer on the desired side of its target for this period?

Inputs:

- `metric.times-employees-speak-with-each-other-while-receiving-a-drive-through-cu` (Times employees speak with each other while receiving a drive-through customer)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS750, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Amount of dining

- id: `kpi.healthcare.amount-of-dining`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Amount of dining measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A, where A is Amount of dining. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Amount of dining on the desired side of its target for this period?

Inputs:

- `metric.amount-of-dining` (Amount of dining)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS751, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Restaurant revenue per employee

- id: `kpi.healthcare.restaurant-revenue-per-employee`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Restaurant revenue per employee measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A / B, where A is Restaurant revenue, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Restaurant revenue per employee on the desired side of its target for this period?

Inputs:

- `metric.restaurant-revenue` (Restaurant revenue)
- `metric.employee` (employee)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS752, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue per available seat hour (RevPASH)

- id: `kpi.healthcare.revenue-per-available-seat-hour-revpash`
- kind: kpi
- unit: count
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

Revenue per available seat hour (RevPASH) measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A / B, where A is Revenue, B is available seat hour (RevPASH). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue per available seat hour (RevPASH) on the desired side of its target for this period?

Inputs:

- `metric.revenue` (Revenue)
- `metric.available-seat-hour-revpash` (available seat hour (RevPASH))

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS753, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Food service total price

- id: `kpi.healthcare.food-service-total-price`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Food service total price measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Food service total price, B is whole named by Food service total price. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Food service total price on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-food-service-total-price` (part named by Food service total price)
- `metric.whole-named-by-food-service-total-price` (whole named by Food service total price)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS755, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Typo food total collected

- id: `kpi.healthcare.typo-food-total-collected`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Typo food total collected measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Typo food total collected, B is whole named by Typo food total collected. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Typo food total collected on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-typo-food-total-collected` (part named by Typo food total collected)
- `metric.whole-named-by-typo-food-total-collected` (whole named by Typo food total collected)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS756, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Tables served per waiter

- id: `kpi.healthcare.tables-served-per-waiter`
- kind: kpi
- unit: count
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

Tables served per waiter measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A / B, where A is Tables served, B is waiter. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Tables served per waiter on the desired side of its target for this period?

Inputs:

- `metric.tables-served` (Tables served)
- `metric.waiter` (waiter)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS760, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Workforce considered to master "Cafe latte art"

- id: `kpi.healthcare.workforce-considered-to-master-cafe-latte-art`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Workforce considered to master "Cafe latte art" measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is percent. The formula is (A / B) * 100, where A is Workforce considered, B is master "Cafe latte art". Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Workforce considered to master "Cafe latte art" on the desired side of its target for this period?

Inputs:

- `metric.workforce-considered` (Workforce considered)
- `metric.master-cafe-latte-art` (master "Cafe latte art")

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS761, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### No show menu

- id: `kpi.healthcare.no-show-menu`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

No show menu measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is percent. The formula is (A / B) * 100, where A is part named by No show menu, B is whole named by No show menu. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is No show menu on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-no-show-menu` (part named by No show menu)
- `metric.whole-named-by-no-show-menu` (whole named by No show menu)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS771, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Weight of linen laundered

- id: `kpi.healthcare.weight-of-linen-laundered`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Weight of linen laundered measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A, where A is Weight of linen laundered. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Weight of linen laundered on the desired side of its target for this period?

Inputs:

- `metric.weight-of-linen-laundered` (Weight of linen laundered)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS781, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue per available square meter (RevPAM)

- id: `kpi.healthcare.revenue-per-available-square-meter-revpam`
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

Revenue per available square meter (RevPAM) measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is currency. The formula is A / B, where A is Revenue, B is available square meter (RevPAM). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue per available square meter (RevPAM) on the desired side of its target for this period?

Inputs:

- `metric.revenue` (Revenue)
- `metric.available-square-meter-revpam` (available square meter (RevPAM))

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS788, page_0129)
- organizational / industries / Healthcare / Hotel/Accommodation (sB788, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Drinks revenue

- id: `kpi.healthcare.drinks-revenue`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Drinks revenue measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is currency. The formula is A, where A is Drinks revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Drinks revenue on the desired side of its target for this period?

Inputs:

- `metric.drinks-revenue` (Drinks revenue)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS801, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Food revenue per head

- id: `kpi.healthcare.food-revenue-per-head`
- kind: kpi
- unit: count
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

Food revenue per head measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A / B, where A is Food revenue, B is head. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Food revenue per head on the desired side of its target for this period?

Inputs:

- `metric.food-revenue` (Food revenue)
- `metric.head` (head)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS802, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Satisfaction with food quality

- id: `kpi.healthcare.satisfaction-with-food-quality`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: survey
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Satisfaction with food quality measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is currency. The formula is A, where A is Satisfaction with food quality. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Satisfaction with food quality on the desired side of its target for this period?

Inputs:

- `metric.satisfaction-with-food-quality` (Satisfaction with food quality)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS693, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of food material

- id: `kpi.healthcare.cost-of-food-material`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Cost of food material measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is currency. The formula is A, where A is Cost of food material. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of food material on the desired side of its target for this period?

Inputs:

- `metric.cost-of-food-material` (Cost of food material)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS695, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Satisfaction with amenities

- id: `kpi.healthcare.satisfaction-with-amenities`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: survey
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Satisfaction with amenities measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is currency. The formula is A, where A is Satisfaction with amenities. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Satisfaction with amenities on the desired side of its target for this period?

Inputs:

- `metric.satisfaction-with-amenities` (Satisfaction with amenities)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS696, page_0129)
- organizational / industries / Healthcare / Organizational » Industries (K6896, page_0132)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Customers per waiter

- id: `kpi.healthcare.customers-per-waiter`
- kind: kpi
- unit: count
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

Customers per waiter measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A / B, where A is Customers, B is waiter. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Customers per waiter on the desired side of its target for this period?

Inputs:

- `metric.customers` (Customers)
- `metric.waiter` (waiter)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS697, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Visits by top 100 guests

- id: `kpi.healthcare.visits-by-top-100-guests`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Visits by top 100 guests measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A, where A is Visits by top 100 guests. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Visits by top 100 guests on the desired side of its target for this period?

Inputs:

- `metric.visits-by-top-100-guests` (Visits by top 100 guests)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS698, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Reviews available online

- id: `kpi.healthcare.reviews-available-online`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Reviews available online measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A, where A is Reviews available online. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Reviews available online on the desired side of its target for this period?

Inputs:

- `metric.reviews-available-online` (Reviews available online)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS699, page_0129)
- organizational / industries / Healthcare / Tour Operator (kX6900, page_0133)
- organizational / industries / Healthcare / Tour Operator (kK6900, page_0133)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Vending time between placing the order and being served

- id: `kpi.healthcare.vending-time-between-placing-the-order-and-being-served`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Vending time between placing the order and being served measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is number. The formula is A, where A is Vending time between placing the order and being served. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Vending time between placing the order and being served on the desired side of its target for this period?

Inputs:

- `metric.vending-time-between-placing-the-order-and-being-served` (Vending time between placing the order and being served)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS711, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Order serving mistakes

- id: `kpi.healthcare.order-serving-mistakes`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.food-and-beverage-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Order serving mistakes measures that result inside Healthcare, subcategory Food and Beverage Service. The unit is count. The formula is A, where A is Order serving mistakes. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Order serving mistakes on the desired side of its target for this period?

Inputs:

- `metric.order-serving-mistakes` (Order serving mistakes)

Placements:

- organizational / industries / Healthcare / Food and Beverage Service (KSS692, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
