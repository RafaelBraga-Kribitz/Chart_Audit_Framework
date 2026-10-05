# Administration / Corporate Travel

Context: organizational. Group: functional. KPIs: 26.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Ticket price

- id: `kpi.administration.ticket-price`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Ticket price measures that result inside Administration, subcategory Corporate Travel. The unit is currency. The formula is A, where A is Ticket price. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Ticket price on the desired side of its target for this period?

Inputs:

- `metric.ticket-price` (Ticket price)

Placements:

- organizational / functional / Administration / Corporate Travel (x8169, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Lowest fare obtained

- id: `kpi.administration.lowest-fare-obtained`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Lowest fare obtained measures that result inside Administration, subcategory Corporate Travel. The unit is currency. The formula is A, where A is Lowest fare obtained. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Lowest fare obtained on the desired side of its target for this period?

Inputs:

- `metric.lowest-fare-obtained` (Lowest fare obtained)

Placements:

- organizational / functional / Administration / Corporate Travel (x8170, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Online booking adoption rate

- id: `kpi.administration.online-booking-adoption-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Online booking adoption rate measures that result inside Administration, subcategory Corporate Travel. The unit is percent. The formula is (A / B) * 100, where A is numerator of Online booking adoption rate, B is base of Online booking adoption rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Online booking adoption rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-online-booking-adoption-rate` (numerator of Online booking adoption rate)
- `metric.base-of-online-booking-adoption-rate` (base of Online booking adoption rate)

Placements:

- organizational / functional / Administration / Corporate Travel (x8171, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Travel and accommodation requests fulfilled

- id: `kpi.administration.travel-and-accommodation-requests-fulfilled`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Travel and accommodation requests fulfilled measures that result inside Administration, subcategory Corporate Travel. The unit is percent. The formula is (A / B) * 100, where A is part named by Travel and accommodation requests fulfilled, B is whole named by Travel and accommodation requests fulfilled. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Travel and accommodation requests fulfilled on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-travel-and-accommodation-requests-fulfilled` (part named by Travel and accommodation requests fulfilled)
- `metric.whole-named-by-travel-and-accommodation-requests-fulfilled` (whole named by Travel and accommodation requests fulfilled)

Placements:

- organizational / functional / Administration / Corporate Travel (x83071, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Mechanical used to manage travel policy compliance

- id: `kpi.administration.mechanical-used-to-manage-travel-policy-compliance`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Mechanical used to manage travel policy compliance measures that result inside Administration, subcategory Corporate Travel. The unit is count. The formula is A, where A is Mechanical used to manage travel policy compliance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Mechanical used to manage travel policy compliance on the desired side of its target for this period?

Inputs:

- `metric.mechanical-used-to-manage-travel-policy-compliance` (Mechanical used to manage travel policy compliance)

Placements:

- organizational / functional / Administration / Corporate Travel (x85838, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Pre-booked travel tickets

- id: `kpi.administration.pre-booked-travel-tickets`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: operational
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Pre-booked travel tickets measures that result inside Administration, subcategory Corporate Travel. The unit is percent. The formula is (A / B) * 100, where A is part named by Pre-booked travel tickets, B is whole named by Pre-booked travel tickets. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Pre-booked travel tickets on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-pre-booked-travel-tickets` (part named by Pre-booked travel tickets)
- `metric.whole-named-by-pre-booked-travel-tickets` (whole named by Pre-booked travel tickets)

Placements:

- organizational / functional / Administration / Corporate Travel (x85862, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### ROI of business travel

- id: `kpi.administration.roi-of-business-travel`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

ROI of business travel measures that result inside Administration, subcategory Corporate Travel. The unit is count. The formula is A, where A is ROI of business travel. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is ROI of business travel on the desired side of its target for this period?

Inputs:

- `metric.roi-of-business-travel` (ROI of business travel)

Placements:

- organizational / functional / Administration / Corporate Travel (x85866, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Travel management services coverage

- id: `kpi.administration.travel-management-services-coverage`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Travel management services coverage measures that result inside Administration, subcategory Corporate Travel. The unit is percent. The formula is (A / B) * 100, where A is part named by Travel management services coverage, B is whole named by Travel management services coverage. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Travel management services coverage on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-travel-management-services-coverage` (part named by Travel management services coverage)
- `metric.whole-named-by-travel-management-services-coverage` (whole named by Travel management services coverage)

Placements:

- organizational / functional / Administration / Corporate Travel (x86066, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Virtual meetings

- id: `kpi.administration.virtual-meetings`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Virtual meetings measures that result inside Administration, subcategory Corporate Travel. The unit is percent. The formula is (A / B) * 100, where A is part named by Virtual meetings, B is whole named by Virtual meetings. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Virtual meetings on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-virtual-meetings` (part named by Virtual meetings)
- `metric.whole-named-by-virtual-meetings` (whole named by Virtual meetings)

Placements:

- organizational / functional / Administration / Corporate Travel (x86077, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Travel policy compliance

- id: `kpi.administration.travel-policy-compliance`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Travel policy compliance measures that result inside Administration, subcategory Corporate Travel. The unit is count. The formula is A, where A is Travel policy compliance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Travel policy compliance on the desired side of its target for this period?

Inputs:

- `metric.travel-policy-compliance` (Travel policy compliance)

Placements:

- organizational / functional / Administration / Corporate Travel (x86608, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Share of corporate credit volume

- id: `kpi.administration.share-of-corporate-credit-volume`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Share of corporate credit volume measures that result inside Administration, subcategory Corporate Travel. The unit is percent. The formula is (A / B) * 100, where A is Share, B is corporate credit volume. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Share of corporate credit volume on the desired side of its target for this period?

Inputs:

- `metric.share` (Share)
- `metric.corporate-credit-volume` (corporate credit volume)

Placements:

- organizational / functional / Administration / Corporate Travel (x86609, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Travel expense productivity

- id: `kpi.administration.travel-expense-productivity`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Travel expense productivity measures that result inside Administration, subcategory Corporate Travel. The unit is count. The formula is A, where A is Travel expense productivity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Travel expense productivity on the desired side of its target for this period?

Inputs:

- `metric.travel-expense-productivity` (Travel expense productivity)

Placements:

- organizational / functional / Administration / Corporate Travel (x86610, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Travel agency productivity index

- id: `kpi.administration.travel-agency-productivity-index`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: index
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Travel agency productivity index measures that result inside Administration, subcategory Corporate Travel. The unit is count. The formula is (A / B) * 100, where A is current Travel agency productivity index, B is base-period Travel agency productivity index. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Travel agency productivity index on the desired side of its target for this period?

Inputs:

- `metric.current-travel-agency-productivity-index` (current Travel agency productivity index)
- `metric.base-period-travel-agency-productivity-index` (base-period Travel agency productivity index)

Placements:

- organizational / functional / Administration / Corporate Travel (x86611, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Business travel share of carbon footprint

- id: `kpi.administration.business-travel-share-of-carbon-footprint`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Business travel share of carbon footprint measures that result inside Administration, subcategory Corporate Travel. The unit is percent. The formula is (A / B) * 100, where A is Business travel share, B is carbon footprint. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Business travel share of carbon footprint on the desired side of its target for this period?

Inputs:

- `metric.business-travel-share` (Business travel share)
- `metric.carbon-footprint` (carbon footprint)

Placements:

- organizational / functional / Administration / Corporate Travel (x86612, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Per trip footprint intensity ratio

- id: `kpi.administration.per-trip-footprint-intensity-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Per trip footprint intensity ratio measures that result inside Administration, subcategory Corporate Travel. The unit is count. The formula is A, where A is Per trip footprint intensity ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Per trip footprint intensity ratio on the desired side of its target for this period?

Inputs:

- `metric.per-trip-footprint-intensity-ratio` (Per trip footprint intensity ratio)

Placements:

- organizational / functional / Administration / Corporate Travel (x86613, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Age of supplier fleet

- id: `kpi.administration.age-of-supplier-fleet`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Age of supplier fleet measures that result inside Administration, subcategory Corporate Travel. The unit is count. The formula is A, where A is Age of supplier fleet. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Age of supplier fleet on the desired side of its target for this period?

Inputs:

- `metric.age-of-supplier-fleet` (Age of supplier fleet)

Placements:

- organizational / functional / Administration / Corporate Travel (x86631, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Trips per week

- id: `kpi.administration.trips-per-week`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Trips per week measures that result inside Administration, subcategory Corporate Travel. The unit is count. The formula is A / B, where A is Trips, B is week. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Trips per week on the desired side of its target for this period?

Inputs:

- `metric.trips` (Trips)
- `metric.week` (week)

Placements:

- organizational / functional / Administration / Corporate Travel (x86652, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Total supply chain

- id: `kpi.administration.total-supply-chain`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Total supply chain measures that result inside Administration, subcategory Corporate Travel. The unit is count. The formula is A, where A is Total supply chain. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Total supply chain on the desired side of its target for this period?

Inputs:

- `metric.total-supply-chain` (Total supply chain)

Placements:

- organizational / functional / Administration / Corporate Travel (x86653, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of video conferencing versus travel costs

- id: `kpi.administration.cost-of-video-conferencing-versus-travel-costs`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `scatter-plot` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of video conferencing versus travel costs measures that result inside Administration, subcategory Corporate Travel. The unit is count. The formula is (A / B) * 100, where A is Cost of video conferencing, B is travel costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of video conferencing versus travel costs on the desired side of its target for this period?

Inputs:

- `metric.cost-of-video-conferencing` (Cost of video conferencing)
- `metric.travel-costs` (travel costs)

Placements:

- organizational / functional / Administration / Corporate Travel (x86654, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### One-day business trips

- id: `kpi.administration.one-day-business-trips`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

One-day business trips measures that result inside Administration, subcategory Corporate Travel. The unit is count. The formula is A, where A is One-day business trips. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is One-day business trips on the desired side of its target for this period?

Inputs:

- `metric.one-day-business-trips` (One-day business trips)

Placements:

- organizational / functional / Administration / Corporate Travel (x86662, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Traveler satisfaction

- id: `kpi.administration.traveler-satisfaction`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: survey
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Traveler satisfaction measures that result inside Administration, subcategory Corporate Travel. The unit is count. The formula is A, where A is Traveler satisfaction. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Traveler satisfaction on the desired side of its target for this period?

Inputs:

- `metric.traveler-satisfaction` (Traveler satisfaction)

Placements:

- organizational / functional / Administration / Corporate Travel (x86663, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unused tickets

- id: `kpi.administration.unused-tickets`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Unused tickets measures that result inside Administration, subcategory Corporate Travel. The unit is count. The formula is A, where A is Unused tickets. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unused tickets on the desired side of its target for this period?

Inputs:

- `metric.unused-tickets` (Unused tickets)

Placements:

- organizational / functional / Administration / Corporate Travel (x86664, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of trip

- id: `kpi.administration.cost-of-trip`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of trip measures that result inside Administration, subcategory Corporate Travel. The unit is currency. The formula is A, where A is Cost of trip. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of trip on the desired side of its target for this period?

Inputs:

- `metric.cost-of-trip` (Cost of trip)

Placements:

- organizational / functional / Administration / Corporate Travel (x86704, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Out-of-policy bookings

- id: `kpi.administration.out-of-policy-bookings`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Out-of-policy bookings measures that result inside Administration, subcategory Corporate Travel. The unit is percent. The formula is (A / B) * 100, where A is part named by Out-of-policy bookings, B is whole named by Out-of-policy bookings. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Out-of-policy bookings on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-out-of-policy-bookings` (part named by Out-of-policy bookings)
- `metric.whole-named-by-out-of-policy-bookings` (whole named by Out-of-policy bookings)

Placements:

- organizational / functional / Administration / Corporate Travel (x86705, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost per attendee

- id: `kpi.administration.cost-per-attendee`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost per attendee measures that result inside Administration, subcategory Corporate Travel. The unit is currency. The formula is A / B, where A is Cost, B is attendee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost per attendee on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.attendee` (attendee)

Placements:

- organizational / functional / Administration / Corporate Travel (x86707, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Agency transaction fee

- id: `kpi.administration.agency-transaction-fee`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.corporate-travel`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Agency transaction fee measures that result inside Administration, subcategory Corporate Travel. The unit is currency. The formula is A, where A is Agency transaction fee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Agency transaction fee on the desired side of its target for this period?

Inputs:

- `metric.agency-transaction-fee` (Agency transaction fee)

Placements:

- organizational / functional / Administration / Corporate Travel (x86709, page_0012)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
