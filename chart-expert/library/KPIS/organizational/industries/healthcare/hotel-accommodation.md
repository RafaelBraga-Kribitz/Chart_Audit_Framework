# Healthcare / Hotel/Accommodation

Context: organizational. Group: industries. KPIs: 50.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### ▼ Hotel waste per occupied bed night

- id: `kpi.management.hotel-waste-per-occupied-bed-night`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

▼ Hotel waste per occupied bed night measures that result inside Management, subcategory Organizational + Functional Areas. The unit is number. The formula is A / B, where A is ▼ Hotel waste, B is occupied bed night. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is ▼ Hotel waste per occupied bed night on the desired side of its target for this period?

Inputs:

- `metric.hotel-waste` (▼ Hotel waste)
- `metric.occupied-bed-night` (occupied bed night)

Placements:

- organizational / functional / Management / Organizational + Functional Areas (xK4778, page_0015)
- organizational / industries / Healthcare / Hotel/Accommodation (sB778, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Absent days per employee during peak operational periods

- id: `kpi.human-resources.absent-days-per-employee-during-peak-operational-periods`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.service-delivery`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Absent days per employee during peak operational periods measures that result inside Human Resources, subcategory Service Delivery. The unit is count. The formula is A / B, where A is Absent days, B is employee during peak operational periods. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Absent days per employee during peak operational periods on the desired side of its target for this period?

Inputs:

- `metric.absent-days` (Absent days)
- `metric.employee-during-peak-operational-periods` (employee during peak operational periods)

Placements:

- organizational / functional / Human Resources / Service Delivery (k8752, page_0024)
- organizational / industries / Healthcare / Hotel/Accommodation (sB752, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hotel occupancy

- id: `kpi.finance.hotel-occupancy`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.finance.economic-and-business-affairs`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Hotel occupancy measures that result inside Finance, subcategory Economic & Business Affairs. The unit is percent. The formula is (A / B) * 100, where A is part named by Hotel occupancy, B is whole named by Hotel occupancy. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hotel occupancy on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-hotel-occupancy` (part named by Hotel occupancy)
- `metric.whole-named-by-hotel-occupancy` (whole named by Hotel occupancy)

Placements:

- organizational / industries / Finance / Economic & Business Affairs (xX135, page_0087)
- organizational / industries / Resources / Organizational » Industries (sK135, page_0108)
- organizational / industries / Healthcare / Hotel/Accommodation (sB135, page_0131)

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

### Unrelated pestilential revenue

- id: `kpi.healthcare.unrelated-pestilential-revenue`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Unrelated pestilential revenue measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is number. The formula is A, where A is Unrelated pestilential revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unrelated pestilential revenue on the desired side of its target for this period?

Inputs:

- `metric.unrelated-pestilential-revenue` (Unrelated pestilential revenue)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB50, page_0131)

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

### Stays of 2+ nights

- id: `kpi.healthcare.stays-of-2-nights`
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

Stays of 2+ nights measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is (A / B) * 100, where A is Stays, B is 2+ nights. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Stays of 2+ nights on the desired side of its target for this period?

Inputs:

- `metric.stays` (Stays)
- `metric.2-nights` (2+ nights)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB136, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Room occupancy

- id: `kpi.healthcare.room-occupancy`
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

Room occupancy measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is (A / B) * 100, where A is part named by Room occupancy, B is whole named by Room occupancy. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Room occupancy on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-room-occupancy` (part named by Room occupancy)
- `metric.whole-named-by-room-occupancy` (whole named by Room occupancy)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB139, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Nights of hotel stays sold

- id: `kpi.healthcare.nights-of-hotel-stays-sold`
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

Nights of hotel stays sold measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is (A / B) * 100, where A is Nights, B is hotel stays sold. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Nights of hotel stays sold on the desired side of its target for this period?

Inputs:

- `metric.nights` (Nights)
- `metric.hotel-stays-sold` (hotel stays sold)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB213, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Length of stay in hotel

- id: `kpi.healthcare.length-of-stay-in-hotel`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Length of stay in hotel measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A, where A is Length of stay in hotel. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Length of stay in hotel on the desired side of its target for this period?

Inputs:

- `metric.length-of-stay-in-hotel` (Length of stay in hotel)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB215, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Rooms with maintenance problems

- id: `kpi.healthcare.rooms-with-maintenance-problems`
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

Rooms with maintenance problems measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is (A / B) * 100, where A is part named by Rooms with maintenance problems, B is whole named by Rooms with maintenance problems. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Rooms with maintenance problems on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-rooms-with-maintenance-problems` (part named by Rooms with maintenance problems)
- `metric.whole-named-by-rooms-with-maintenance-problems` (whole named by Rooms with maintenance problems)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB218, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Canceled*reviews

- id: `kpi.healthcare.canceled-reviews`
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

Canceled*reviews measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is (A / B) * 100, where A is part named by Canceled*reviews, B is whole named by Canceled*reviews. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Canceled*reviews on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-canceled-reviews` (part named by Canceled*reviews)
- `metric.whole-named-by-canceled-reviews` (whole named by Canceled*reviews)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB222, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue per available room (RevPAR)

- id: `kpi.healthcare.revenue-per-available-room-revpar`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Revenue per available room (RevPAR) measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is A / B, where A is Revenue, B is available room (RevPAR). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue per available room (RevPAR) on the desired side of its target for this period?

Inputs:

- `metric.revenue` (Revenue)
- `metric.available-room-revpar` (available room (RevPAR))

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB676, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Guests per employee

- id: `kpi.healthcare.guests-per-employee`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Guests per employee measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is A / B, where A is Guests, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Guests per employee on the desired side of its target for this period?

Inputs:

- `metric.guests` (Guests)
- `metric.employee` (employee)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB697, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cleaning cost per room

- id: `kpi.healthcare.cleaning-cost-per-room`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Cleaning cost per room measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is A / B, where A is Cleaning cost, B is room. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cleaning cost per room on the desired side of its target for this period?

Inputs:

- `metric.cleaning-cost` (Cleaning cost)
- `metric.room` (room)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB738, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Average daily room rate (ADR)

- id: `kpi.healthcare.average-daily-room-rate-adr`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: average
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Average daily room rate (ADR) measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is number. The formula is A / B, where A is sum underlying Average daily room rate (ADR), B is count of observations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Average daily room rate (ADR) on the desired side of its target for this period?

Inputs:

- `metric.sum-underlying-average-daily-room-rate-adr` (sum underlying Average daily room rate (ADR))
- `metric.count-of-observations` (count of observations)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB770, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Gross operating profit per available room (GOPPAR)

- id: `kpi.healthcare.gross-operating-profit-per-available-room-goppar`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Gross operating profit per available room (GOPPAR) measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is A / B, where A is Gross operating profit, B is available room (GOPPAR). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Gross operating profit per available room (GOPPAR) on the desired side of its target for this period?

Inputs:

- `metric.gross-operating-profit` (Gross operating profit)
- `metric.available-room-goppar` (available room (GOPPAR))

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB740, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Rooms booked through own reservation channels

- id: `kpi.healthcare.rooms-booked-through-own-reservation-channels`
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

Rooms booked through own reservation channels measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is (A / B) * 100, where A is part named by Rooms booked through own reservation channels, B is whole named by Rooms booked through own reservation channels. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Rooms booked through own reservation channels on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-rooms-booked-through-own-reservation-channels` (part named by Rooms booked through own reservation channels)
- `metric.whole-named-by-rooms-booked-through-own-reservation-channels` (whole named by Rooms booked through own reservation channels)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB741, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Reservation channel revenue

- id: `kpi.healthcare.reservation-channel-revenue`
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

Reservation channel revenue measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is (A / B) * 100, where A is part named by Reservation channel revenue, B is whole named by Reservation channel revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Reservation channel revenue on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-reservation-channel-revenue` (part named by Reservation channel revenue)
- `metric.whole-named-by-reservation-channel-revenue` (whole named by Reservation channel revenue)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB742, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue per booking

- id: `kpi.healthcare.revenue-per-booking`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Revenue per booking measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A / B, where A is Revenue, B is booking. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue per booking on the desired side of its target for this period?

Inputs:

- `metric.revenue` (Revenue)
- `metric.booking` (booking)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB1222, page_0131)

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

### Overseas to local customer travel bookings

- id: `kpi.healthcare.overseas-to-local-customer-travel-bookings`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Overseas to local customer travel bookings measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A, where A is Overseas to local customer travel bookings. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Overseas to local customer travel bookings on the desired side of its target for this period?

Inputs:

- `metric.overseas-to-local-customer-travel-bookings` (Overseas to local customer travel bookings)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB4909, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Bovenable customer reviews

- id: `kpi.healthcare.bovenable-customer-reviews`
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

Bovenable customer reviews measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is (A / B) * 100, where A is part named by Bovenable customer reviews, B is whole named by Bovenable customer reviews. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Bovenable customer reviews on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-bovenable-customer-reviews` (part named by Bovenable customer reviews)
- `metric.whole-named-by-bovenable-customer-reviews` (whole named by Bovenable customer reviews)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB4922, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Booking value

- id: `kpi.healthcare.booking-value`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Booking value measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is currency. The formula is A, where A is Booking value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Booking value on the desired side of its target for this period?

Inputs:

- `metric.booking-value` (Booking value)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB763, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Bookings conversion rate

- id: `kpi.healthcare.bookings-conversion-rate`
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

Bookings conversion rate measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is (A / B) * 100, where A is numerator of Bookings conversion rate, B is base of Bookings conversion rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Bookings conversion rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-bookings-conversion-rate` (numerator of Bookings conversion rate)
- `metric.base-of-bookings-conversion-rate` (base of Bookings conversion rate)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB764, page_0131)
- organizational / industries / Healthcare / Tour Operator (kX4764, page_0133)
- organizational / industries / Healthcare / Tour Operator (kK4764, page_0133)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Wages costs from total sales

- id: `kpi.healthcare.wages-costs-from-total-sales`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Wages costs from total sales measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is (A / B) * 100, where A is Wages costs, B is total sales. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Wages costs from total sales on the desired side of its target for this period?

Inputs:

- `metric.wages-costs` (Wages costs)
- `metric.total-sales` (total sales)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB765, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Available customer nights

- id: `kpi.healthcare.available-customer-nights`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Available customer nights measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A, where A is Available customer nights. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Available customer nights on the desired side of its target for this period?

Inputs:

- `metric.available-customer-nights` (Available customer nights)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB766, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Occupied rooms per employee

- id: `kpi.healthcare.occupied-rooms-per-employee`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Occupied rooms per employee measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A / B, where A is Occupied rooms, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Occupied rooms per employee on the desired side of its target for this period?

Inputs:

- `metric.occupied-rooms` (Occupied rooms)
- `metric.employee` (employee)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB767, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Equipment occupancy

- id: `kpi.healthcare.equipment-occupancy`
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

Equipment occupancy measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is (A / B) * 100, where A is part named by Equipment occupancy, B is whole named by Equipment occupancy. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Equipment occupancy on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-equipment-occupancy` (part named by Equipment occupancy)
- `metric.whole-named-by-equipment-occupancy` (whole named by Equipment occupancy)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB769, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hotel bed occupancy

- id: `kpi.healthcare.hotel-bed-occupancy`
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

Hotel bed occupancy measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is (A / B) * 100, where A is part named by Hotel bed occupancy, B is whole named by Hotel bed occupancy. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hotel bed occupancy on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-hotel-bed-occupancy` (part named by Hotel bed occupancy)
- `metric.whole-named-by-hotel-bed-occupancy` (whole named by Hotel bed occupancy)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB770, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### No show rate

- id: `kpi.healthcare.no-show-rate`
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

No show rate measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is (A / B) * 100, where A is numerator of No show rate, B is base of No show rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is No show rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-no-show-rate` (numerator of No show rate)
- `metric.base-of-no-show-rate` (base of No show rate)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB771, page_0131)
- organizational / industries / Healthcare / Tour Operator (kX4771, page_0133)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hotel-to-chain ratio

- id: `kpi.healthcare.hotel-to-chain-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Hotel-to-chain ratio measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A, where A is Hotel-to-chain ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hotel-to-chain ratio on the desired side of its target for this period?

Inputs:

- `metric.hotel-to-chain-ratio` (Hotel-to-chain ratio)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB772, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hotel-to-city ratio

- id: `kpi.healthcare.hotel-to-city-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Hotel-to-city ratio measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A, where A is Hotel-to-city ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hotel-to-city ratio on the desired side of its target for this period?

Inputs:

- `metric.hotel-to-city-ratio` (Hotel-to-city ratio)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB773, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hotel-to-migrant ratio

- id: `kpi.healthcare.hotel-to-migrant-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Hotel-to-migrant ratio measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A, where A is Hotel-to-migrant ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hotel-to-migrant ratio on the desired side of its target for this period?

Inputs:

- `metric.hotel-to-migrant-ratio` (Hotel-to-migrant ratio)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB774, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hotel-to-region ratio

- id: `kpi.healthcare.hotel-to-region-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Hotel-to-region ratio measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A, where A is Hotel-to-region ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hotel-to-region ratio on the desired side of its target for this period?

Inputs:

- `metric.hotel-to-region-ratio` (Hotel-to-region ratio)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB775, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Occupied rooms per recognition

- id: `kpi.healthcare.occupied-rooms-per-recognition`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Occupied rooms per recognition measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A / B, where A is Occupied rooms, B is recognition. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Occupied rooms per recognition on the desired side of its target for this period?

Inputs:

- `metric.occupied-rooms` (Occupied rooms)
- `metric.recognition` (recognition)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB776, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Guest rooms in operation

- id: `kpi.healthcare.guest-rooms-in-operation`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Guest rooms in operation measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A, where A is Guest rooms in operation. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Guest rooms in operation on the desired side of its target for this period?

Inputs:

- `metric.guest-rooms-in-operation` (Guest rooms in operation)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB777, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Rooms of hotel waste per year per employee

- id: `kpi.healthcare.rooms-of-hotel-waste-per-year-per-employee`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Rooms of hotel waste per year per employee measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A / B, where A is Rooms of hotel waste, B is year per employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Rooms of hotel waste per year per employee on the desired side of its target for this period?

Inputs:

- `metric.rooms-of-hotel-waste` (Rooms of hotel waste)
- `metric.year-per-employee` (year per employee)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB779, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Areas of catering division

- id: `kpi.healthcare.areas-of-catering-division`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Areas of catering division measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A, where A is Areas of catering division. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Areas of catering division on the desired side of its target for this period?

Inputs:

- `metric.areas-of-catering-division` (Areas of catering division)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB780, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Weight of 1床用的 1床用的

- id: `kpi.healthcare.weight-of-1-1`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Weight of 1床用的 1床用的 measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A, where A is Weight of 1床用的 1床用的. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Weight of 1床用的 1床用的 on the desired side of its target for this period?

Inputs:

- `metric.weight-of-1-1` (Weight of 1床用的 1床用的)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB781, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Catering division production value per employee

- id: `kpi.healthcare.catering-division-production-value-per-employee`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Catering division production value per employee measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A / B, where A is Catering division production value, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Catering division production value per employee on the desired side of its target for this period?

Inputs:

- `metric.catering-division-production-value` (Catering division production value)
- `metric.employee` (employee)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB782, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Perched bed cleanliness

- id: `kpi.healthcare.perched-bed-cleanliness`
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

Perched bed cleanliness measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is (A / B) * 100, where A is part named by Perched bed cleanliness, B is whole named by Perched bed cleanliness. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Perched bed cleanliness on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-perched-bed-cleanliness` (part named by Perched bed cleanliness)
- `metric.whole-named-by-perched-bed-cleanliness` (whole named by Perched bed cleanliness)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB783, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Guests dining in-house

- id: `kpi.healthcare.guests-dining-in-house`
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

Guests dining in-house measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is percent. The formula is (A / B) * 100, where A is part named by Guests dining in-house, B is whole named by Guests dining in-house. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Guests dining in-house on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-guests-dining-in-house` (part named by Guests dining in-house)
- `metric.whole-named-by-guests-dining-in-house` (whole named by Guests dining in-house)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB784, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Monthly room revenue divided by total payroll and benefits

- id: `kpi.healthcare.monthly-room-revenue-divided-by-total-payroll-and-benefits`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Monthly room revenue divided by total payroll and benefits measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A, where A is Monthly room revenue divided by total payroll and benefits. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Monthly room revenue divided by total payroll and benefits on the desired side of its target for this period?

Inputs:

- `metric.monthly-room-revenue-divided-by-total-payroll-and-benefits` (Monthly room revenue divided by total payroll and benefits)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB786, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Room rate

- id: `kpi.healthcare.room-rate`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Room rate measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A, where A is Room rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Room rate on the desired side of its target for this period?

Inputs:

- `metric.room-rate` (Room rate)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB787, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Profitability per accommodation unit

- id: `kpi.healthcare.profitability-per-accommodation-unit`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Profitability per accommodation unit measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A / B, where A is Profitability, B is accommodation unit. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Profitability per accommodation unit on the desired side of its target for this period?

Inputs:

- `metric.profitability` (Profitability)
- `metric.accommodation-unit` (accommodation unit)

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB789, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue per available customer (RevPMC)

- id: `kpi.healthcare.revenue-per-available-customer-revpmc`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Revenue per available customer (RevPMC) measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A / B, where A is Revenue, B is available customer (RevPMC). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue per available customer (RevPMC) on the desired side of its target for this period?

Inputs:

- `metric.revenue` (Revenue)
- `metric.available-customer-revpmc` (available customer (RevPMC))

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB790, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Total revenue per available room (TRevPAR)

- id: `kpi.healthcare.total-revenue-per-available-room-trevpar`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Total revenue per available room (TRevPAR) measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A / B, where A is Total revenue, B is available room (TRevPAR). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Total revenue per available room (TRevPAR) on the desired side of its target for this period?

Inputs:

- `metric.total-revenue` (Total revenue)
- `metric.available-room-trevpar` (available room (TRevPAR))

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB791, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Total revenue per client (TRevPIC)

- id: `kpi.healthcare.total-revenue-per-client-trevpic`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.hotel-accommodation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Total revenue per client (TRevPIC) measures that result inside Healthcare, subcategory Hotel/Accommodation. The unit is count. The formula is A / B, where A is Total revenue, B is client (TRevPIC). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Total revenue per client (TRevPIC) on the desired side of its target for this period?

Inputs:

- `metric.total-revenue` (Total revenue)
- `metric.client-trevpic` (client (TRevPIC))

Placements:

- organizational / industries / Healthcare / Hotel/Accommodation (sB792, page_0131)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
