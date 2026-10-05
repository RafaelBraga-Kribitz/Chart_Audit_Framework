# Sport / General

Context: organizational. Group: industries. KPIs: 119.

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

### Motorized trips to work by public transport

- id: `kpi.administration.motorized-trips-to-work-by-public-transport`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.organizational-industries`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Motorized trips to work by public transport measures that result inside Administration, subcategory Organizational + Industries. The unit is percent. The formula is (A / B) * 100, where A is Motorized trips, B is work by public transport. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Motorized trips to work by public transport on the desired side of its target for this period?

Inputs:

- `metric.motorized-trips` (Motorized trips)
- `metric.work-by-public-transport` (work by public transport)

Placements:

- organizational / functional / Administration / Organizational + Industries (sK90B9, page_0093)
- organizational / industries / Sport / General (aK3909, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Satisfaction with public transport

- id: `kpi.administration.satisfaction-with-public-transport`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.organizational-industries`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Satisfaction with public transport measures that result inside Administration, subcategory Organizational + Industries. The unit is percent. The formula is (A / B) * 100, where A is part named by Satisfaction with public transport, B is whole named by Satisfaction with public transport. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Satisfaction with public transport on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-satisfaction-with-public-transport` (part named by Satisfaction with public transport)
- `metric.whole-named-by-satisfaction-with-public-transport` (whole named by Satisfaction with public transport)

Placements:

- organizational / functional / Administration / Organizational + Industries (sK89I7, page_0093)
- organizational / industries / Sport / General (aK3927, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Travel time for work trips by public transport

- id: `kpi.administration.travel-time-for-work-trips-by-public-transport`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Travel time for work trips by public transport measures that result inside Administration, subcategory Organizational + Industries. The unit is count. The formula is A, where A is Travel time for work trips by public transport. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Travel time for work trips by public transport on the desired side of its target for this period?

Inputs:

- `metric.travel-time-for-work-trips-by-public-transport` (Travel time for work trips by public transport)

Placements:

- organizational / functional / Administration / Organizational + Industries (sK89B3, page_0093)
- organizational / industries / Sport / General (aK3932, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Carbon dioxide vessel efficiency

- id: `kpi.resources.carbon-dioxide-vessel-efficiency`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.resources.sustainability-green-energy`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Carbon dioxide vessel efficiency measures that result inside Resources, subcategory Sustainability/Green Energy. The unit is count. The formula is A, where A is Carbon dioxide vessel efficiency. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Carbon dioxide vessel efficiency on the desired side of its target for this period?

Inputs:

- `metric.carbon-dioxide-vessel-efficiency` (Carbon dioxide vessel efficiency)

Placements:

- organizational / industries / Resources / Sustainability/Green Energy (kS2488, page_0172)
- organizational / industries / Sport / General (xK348, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Players' satisfaction with the quality of the venue

- id: `kpi.management.players-satisfaction-with-the-quality-of-the-venue`
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

Players' satisfaction with the quality of the venue measures that result inside Management, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Players' satisfaction with the quality, B is the venue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Players' satisfaction with the quality of the venue on the desired side of its target for this period?

Inputs:

- `metric.players-satisfaction-with-the-quality` (Players' satisfaction with the quality)
- `metric.the-venue` (the venue)

Placements:

- organizational / functional / Management / General (%R6482, page_0175)
- organizational / industries / Sport / General (xK6842, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Planned games that took place

- id: `kpi.management.planned-games-that-took-place`
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

Planned games that took place measures that result inside Management, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Planned games that took place, B is whole named by Planned games that took place. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Planned games that took place on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-planned-games-that-took-place` (part named by Planned games that took place)
- `metric.whole-named-by-planned-games-that-took-place` (whole named by Planned games that took place)

Placements:

- organizational / functional / Management / General (%R6849, page_0175)
- organizational / industries / Sport / General (xK6849, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Games with administrative incidents

- id: `kpi.management.games-with-administrative-incidents`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Games with administrative incidents measures that result inside Management, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Games with administrative incidents, B is whole named by Games with administrative incidents. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Games with administrative incidents on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-games-with-administrative-incidents` (part named by Games with administrative incidents)
- `metric.whole-named-by-games-with-administrative-incidents` (whole named by Games with administrative incidents)

Placements:

- organizational / functional / Management / General (%R6850, page_0175)
- organizational / industries / Sport / General (xK6850, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Games with online reviews

- id: `kpi.management.games-with-online-reviews`
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

Games with online reviews measures that result inside Management, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Games with online reviews, B is whole named by Games with online reviews. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Games with online reviews on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-games-with-online-reviews` (part named by Games with online reviews)
- `metric.whole-named-by-games-with-online-reviews` (whole named by Games with online reviews)

Placements:

- organizational / functional / Management / General (%R6854, page_0175)
- organizational / industries / Sport / General (xK6854, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Games with accurate and updated reporting

- id: `kpi.management.games-with-accurate-and-updated-reporting`
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

Games with accurate and updated reporting measures that result inside Management, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is numerator of Games with accurate and updated reporting, B is base of Games with accurate and updated reporting. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Games with accurate and updated reporting on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-games-with-accurate-and-updated-reporting` (numerator of Games with accurate and updated reporting)
- `metric.base-of-games-with-accurate-and-updated-reporting` (base of Games with accurate and updated reporting)

Placements:

- organizational / functional / Management / General (%R6856, page_0175)
- organizational / industries / Sport / General (xK6856, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### x Accredited clubs within the sport

- id: `kpi.sport.x-accredited-clubs-within-the-sport`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

x Accredited clubs within the sport measures that result inside Sport, subcategory General. The unit is number. The formula is A, where A is x Accredited clubs within the sport. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is x Accredited clubs within the sport on the desired side of its target for this period?

Inputs:

- `metric.x-accredited-clubs-within-the-sport` (x Accredited clubs within the sport)

Placements:

- organizational / industries / Sport / General (x8447, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### v Volunteers sponsoring the sport

- id: `kpi.sport.v-volunteers-sponsoring-the-sport`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

v Volunteers sponsoring the sport measures that result inside Sport, subcategory General. The unit is number. The formula is A, where A is v Volunteers sponsoring the sport. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is v Volunteers sponsoring the sport on the desired side of its target for this period?

Inputs:

- `metric.v-volunteers-sponsoring-the-sport` (v Volunteers sponsoring the sport)

Placements:

- organizational / industries / Sport / General (x8448, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### x Salaries augmented or apply utilization

- id: `kpi.sport.x-salaries-augmented-or-apply-utilization`
- kind: kpi
- unit: number
- direction: corridor
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

x Salaries augmented or apply utilization measures that result inside Sport, subcategory General. The unit is number. The formula is A, where A is x Salaries augmented or apply utilization. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is x Salaries augmented or apply utilization on the desired side of its target for this period?

Inputs:

- `metric.x-salaries-augmented-or-apply-utilization` (x Salaries augmented or apply utilization)

Placements:

- organizational / industries / Sport / General (xK1029, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### x Match tickets sold online

- id: `kpi.sport.x-match-tickets-sold-online`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

x Match tickets sold online measures that result inside Sport, subcategory General. The unit is number. The formula is A, where A is x Match tickets sold online. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is x Match tickets sold online on the desired side of its target for this period?

Inputs:

- `metric.x-match-tickets-sold-online` (x Match tickets sold online)

Placements:

- organizational / industries / Sport / General (xK1228, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Spending per spectator

- id: `kpi.sport.spending-per-spectator`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Spending per spectator measures that result inside Sport, subcategory General. The unit is currency. The formula is A / B, where A is Spending, B is spectator. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Spending per spectator on the desired side of its target for this period?

Inputs:

- `metric.spending` (Spending)
- `metric.spectator` (spectator)

Placements:

- organizational / industries / Sport / General (xK1232, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Crowd fill paying adults

- id: `kpi.sport.crowd-fill-paying-adults`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Crowd fill paying adults measures that result inside Sport, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Crowd fill paying adults, B is whole named by Crowd fill paying adults. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Crowd fill paying adults on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-crowd-fill-paying-adults` (part named by Crowd fill paying adults)
- `metric.whole-named-by-crowd-fill-paying-adults` (whole named by Crowd fill paying adults)

Placements:

- organizational / industries / Sport / General (xK1233, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Corporate events used during match days

- id: `kpi.sport.corporate-events-used-during-match-days`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Corporate events used during match days measures that result inside Sport, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is numerator of Corporate events used during match days, B is base of Corporate events used during match days. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Corporate events used during match days on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-corporate-events-used-during-match-days` (numerator of Corporate events used during match days)
- `metric.base-of-corporate-events-used-during-match-days` (base of Corporate events used during match days)

Placements:

- organizational / industries / Sport / General (xK1235, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Match day costs from match day revenues

- id: `kpi.sport.match-day-costs-from-match-day-revenues`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Match day costs from match day revenues measures that result inside Sport, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Match day costs, B is match day revenues. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Match day costs from match day revenues on the desired side of its target for this period?

Inputs:

- `metric.match-day-costs` (Match day costs)
- `metric.match-day-revenues` (match day revenues)

Placements:

- organizational / industries / Sport / General (xK1238, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sport volunteering

- id: `kpi.sport.sport-volunteering`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Sport volunteering measures that result inside Sport, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Sport volunteering, B is whole named by Sport volunteering. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sport volunteering on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-sport-volunteering` (part named by Sport volunteering)
- `metric.whole-named-by-sport-volunteering` (whole named by Sport volunteering)

Placements:

- organizational / industries / Sport / General (xK1250, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Profit per non-match day event

- id: `kpi.sport.profit-per-non-match-day-event`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Profit per non-match day event measures that result inside Sport, subcategory General. The unit is currency. The formula is A / B, where A is Profit, B is non-match day event. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Profit per non-match day event on the desired side of its target for this period?

Inputs:

- `metric.profit` (Profit)
- `metric.non-match-day-event` (non-match day event)

Placements:

- organizational / industries / Sport / General (xK1766, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Viewers per televised match

- id: `kpi.sport.viewers-per-televised-match`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Viewers per televised match measures that result inside Sport, subcategory General. The unit is count. The formula is A / B, where A is Viewers, B is televised match. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Viewers per televised match on the desired side of its target for this period?

Inputs:

- `metric.viewers` (Viewers)
- `metric.televised-match` (televised match)

Placements:

- organizational / industries / Sport / General (xK1769, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Ground facility satisfaction

- id: `kpi.sport.ground-facility-satisfaction`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Ground facility satisfaction measures that result inside Sport, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Ground facility satisfaction, B is whole named by Ground facility satisfaction. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Ground facility satisfaction on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-ground-facility-satisfaction` (part named by Ground facility satisfaction)
- `metric.whole-named-by-ground-facility-satisfaction` (whole named by Ground facility satisfaction)

Placements:

- organizational / industries / Sport / General (xK1770, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Merchandised spend per fan head

- id: `kpi.sport.merchandised-spend-per-fan-head`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Merchandised spend per fan head measures that result inside Sport, subcategory General. The unit is percent. The formula is A / B, where A is Merchandised spend, B is fan head. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Merchandised spend per fan head on the desired side of its target for this period?

Inputs:

- `metric.merchandised-spend` (Merchandised spend)
- `metric.fan-head` (fan head)

Placements:

- organizational / industries / Sport / General (xK1771, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Replica shirt sales

- id: `kpi.sport.replica-shirt-sales`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Replica shirt sales measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Replica shirt sales. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Replica shirt sales on the desired side of its target for this period?

Inputs:

- `metric.replica-shirt-sales` (Replica shirt sales)

Placements:

- organizational / industries / Sport / General (xK1772, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Dwell time

- id: `kpi.sport.dwell-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Dwell time measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Dwell time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Dwell time on the desired side of its target for this period?

Inputs:

- `metric.dwell-time` (Dwell time)

Placements:

- organizational / industries / Sport / General (xK1773, page_0176)
- organizational / industries / Transportation / Organizational→Industries (sK15137, page_0188)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sponsorship

- id: `kpi.sport.sponsorship`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Sponsorship measures that result inside Sport, subcategory General. The unit is currency. The formula is A, where A is Sponsorship. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sponsorship on the desired side of its target for this period?

Inputs:

- `metric.sponsorship` (Sponsorship)

Placements:

- organizational / industries / Sport / General (xK1776, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sport event operating costs

- id: `kpi.sport.sport-event-operating-costs`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Sport event operating costs measures that result inside Sport, subcategory General. The unit is currency. The formula is A, where A is Sport event operating costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sport event operating costs on the desired side of its target for this period?

Inputs:

- `metric.sport-event-operating-costs` (Sport event operating costs)

Placements:

- organizational / industries / Sport / General (xK1975, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Venue renovation cost

- id: `kpi.sport.venue-renovation-cost`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Venue renovation cost measures that result inside Sport, subcategory General. The unit is currency. The formula is A, where A is Venue renovation cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Venue renovation cost on the desired side of its target for this period?

Inputs:

- `metric.venue-renovation-cost` (Venue renovation cost)

Placements:

- organizational / industries / Sport / General (xK2528, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Counties participating in paralympic games

- id: `kpi.sport.counties-participating-in-paralympic-games`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Counties participating in paralympic games measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Counties participating in paralympic games. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Counties participating in paralympic games on the desired side of its target for this period?

Inputs:

- `metric.counties-participating-in-paralympic-games` (Counties participating in paralympic games)

Placements:

- organizational / industries / Sport / General (xK2619, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Counties participating in the sport event

- id: `kpi.sport.counties-participating-in-the-sport-event`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Counties participating in the sport event measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Counties participating in the sport event. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Counties participating in the sport event on the desired side of its target for this period?

Inputs:

- `metric.counties-participating-in-the-sport-event` (Counties participating in the sport event)

Placements:

- organizational / industries / Sport / General (xK2635, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Olympic torch/cheerless

- id: `kpi.sport.olympic-torch-cheerless`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Olympic torch/cheerless measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Olympic torch/cheerless. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Olympic torch/cheerless on the desired side of its target for this period?

Inputs:

- `metric.olympic-torch-cheerless` (Olympic torch/cheerless)

Placements:

- organizational / industries / Sport / General (xK2630, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Paralympic athletes and officials attending competition

- id: `kpi.sport.paralympic-athletes-and-officials-attending-competition`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Paralympic athletes and officials attending competition measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Paralympic athletes and officials attending competition. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Paralympic athletes and officials attending competition on the desired side of its target for this period?

Inputs:

- `metric.paralympic-athletes-and-officials-attending-competition` (Paralympic athletes and officials attending competition)

Placements:

- organizational / industries / Sport / General (xK2634, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Accredited media representatives

- id: `kpi.sport.accredited-media-representatives`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Accredited media representatives measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Accredited media representatives. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Accredited media representatives on the desired side of its target for this period?

Inputs:

- `metric.accredited-media-representatives` (Accredited media representatives)

Placements:

- organizational / industries / Sport / General (xK2635, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Event tickets available

- id: `kpi.sport.event-tickets-available`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Event tickets available measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Event tickets available. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Event tickets available on the desired side of its target for this period?

Inputs:

- `metric.event-tickets-available` (Event tickets available)

Placements:

- organizational / industries / Sport / General (xK2640, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Competitions venues

- id: `kpi.sport.competitions-venues`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Competitions venues measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Competitions venues. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Competitions venues on the desired side of its target for this period?

Inputs:

- `metric.competitions-venues` (Competitions venues)

Placements:

- organizational / industries / Sport / General (xK2641, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Security costs per athlete

- id: `kpi.sport.security-costs-per-athlete`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Security costs per athlete measures that result inside Sport, subcategory General. The unit is count. The formula is A / B, where A is Security costs, B is athlete. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Security costs per athlete on the desired side of its target for this period?

Inputs:

- `metric.security-costs` (Security costs)
- `metric.athlete` (athlete)

Placements:

- organizational / industries / Sport / General (xK2652, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Athlete accommodation facilities development cost

- id: `kpi.sport.athlete-accommodation-facilities-development-cost`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Athlete accommodation facilities development cost measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Athlete accommodation facilities development cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Athlete accommodation facilities development cost on the desired side of its target for this period?

Inputs:

- `metric.athlete-accommodation-facilities-development-cost` (Athlete accommodation facilities development cost)

Placements:

- organizational / industries / Sport / General (xK2665, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Distance traveled by Olympic torch

- id: `kpi.sport.distance-traveled-by-olympic-torch`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Distance traveled by Olympic torch measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Distance traveled by Olympic torch. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Distance traveled by Olympic torch on the desired side of its target for this period?

Inputs:

- `metric.distance-traveled-by-olympic-torch` (Distance traveled by Olympic torch)

Placements:

- organizational / industries / Sport / General (xK2670, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Olympic torch relay duration

- id: `kpi.sport.olympic-torch-relay-duration`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Olympic torch relay duration measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Olympic torch relay duration. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Olympic torch relay duration on the desired side of its target for this period?

Inputs:

- `metric.olympic-torch-relay-duration` (Olympic torch relay duration)

Placements:

- organizational / industries / Sport / General (xK2676, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Athletes and officials attending the competition

- id: `kpi.sport.athletes-and-officials-attending-the-competition`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Athletes and officials attending the competition measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Athletes and officials attending the competition. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Athletes and officials attending the competition on the desired side of its target for this period?

Inputs:

- `metric.athletes-and-officials-attending-the-competition` (Athletes and officials attending the competition)

Placements:

- organizational / industries / Sport / General (xK2686, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Medal events during the competition

- id: `kpi.sport.medal-events-during-the-competition`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Medal events during the competition measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Medal events during the competition. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Medal events during the competition on the desired side of its target for this period?

Inputs:

- `metric.medal-events-during-the-competition` (Medal events during the competition)

Placements:

- organizational / industries / Sport / General (xK2540, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sport event security cost+

- id: `kpi.sport.sport-event-security-cost`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Sport event security cost+ measures that result inside Sport, subcategory General. The unit is currency. The formula is A, where A is Sport event security cost+. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sport event security cost+ on the desired side of its target for this period?

Inputs:

- `metric.sport-event-security-cost` (Sport event security cost+)

Placements:

- organizational / industries / Sport / General (xK2546, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Event seats filled

- id: `kpi.sport.event-seats-filled`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Event seats filled measures that result inside Sport, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Event seats filled, B is whole named by Event seats filled. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Event seats filled on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-event-seats-filled` (part named by Event seats filled)
- `metric.whole-named-by-event-seats-filled` (whole named by Event seats filled)

Placements:

- organizational / industries / Sport / General (xK6778, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Games correct in medal

- id: `kpi.sport.games-correct-in-medal`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Games correct in medal measures that result inside Sport, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Games correct in medal, B is whole named by Games correct in medal. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Games correct in medal on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-games-correct-in-medal` (part named by Games correct in medal)
- `metric.whole-named-by-games-correct-in-medal` (whole named by Games correct in medal)

Placements:

- organizational / industries / Sport / General (xK6844, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue from food & free charges

- id: `kpi.sport.revenue-from-food-and-free-charges`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Revenue from food & free charges measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Revenue from food & free charges. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue from food & free charges on the desired side of its target for this period?

Inputs:

- `metric.revenue-from-food-and-free-charges` (Revenue from food & free charges)

Placements:

- organizational / industries / Sport / General (xK6848, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Games compliant with organizing standards

- id: `kpi.sport.games-compliant-with-organizing-standards`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Games compliant with organizing standards measures that result inside Sport, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Games compliant with organizing standards, B is whole named by Games compliant with organizing standards. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Games compliant with organizing standards on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-games-compliant-with-organizing-standards` (part named by Games compliant with organizing standards)
- `metric.whole-named-by-games-compliant-with-organizing-standards` (whole named by Games compliant with organizing standards)

Placements:

- organizational / industries / Sport / General (xK6855, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Participants in organised sport and physical activities

- id: `kpi.sport.participants-in-organised-sport-and-physical-activities`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Participants in organised sport and physical activities measures that result inside Sport, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Participants in organised sport and physical activities, B is whole named by Participants in organised sport and physical activities. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Participants in organised sport and physical activities on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-participants-in-organised-sport-and-physical-activities` (part named by Participants in organised sport and physical activities)
- `metric.whole-named-by-participants-in-organised-sport-and-physical-activities` (whole named by Participants in organised sport and physical activities)

Placements:

- organizational / industries / Sport / General (xK21205, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Pre-release of insufficient physical activity by age group

- id: `kpi.sport.pre-release-of-insufficient-physical-activity-by-age-group`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Pre-release of insufficient physical activity by age group measures that result inside Sport, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Pre-release, B is insufficient physical activity by age group. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Pre-release of insufficient physical activity by age group on the desired side of its target for this period?

Inputs:

- `metric.pre-release` (Pre-release)
- `metric.insufficient-physical-activity-by-age-group` (insufficient physical activity by age group)

Placements:

- organizational / industries / Sport / General (xK21419, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Prevalence of inactivity by gender

- id: `kpi.sport.prevalence-of-inactivity-by-gender`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Prevalence of inactivity by gender measures that result inside Sport, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Prevalence, B is inactivity by gender. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Prevalence of inactivity by gender on the desired side of its target for this period?

Inputs:

- `metric.prevalence` (Prevalence)
- `metric.inactivity-by-gender` (inactivity by gender)

Placements:

- organizational / industries / Sport / General (xK21411, page_0176)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Accredited officials

- id: `kpi.sport.accredited-officials`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Accredited officials measures that result inside Sport, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Accredited officials, B is whole named by Accredited officials. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Accredited officials on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-accredited-officials` (part named by Accredited officials)
- `metric.whole-named-by-accredited-officials` (whole named by Accredited officials)

Placements:

- organizational / industries / Sport / General (xK20903, page_0176)
- organizational / industries / Sport / General (xK14390, page_0176)

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

### Operating expense per passenger

- id: `kpi.transportation.operating-expense-per-passenger`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Operating expense per passenger measures that result inside Transportation, subcategory Organizational » Industries. The unit is count. The formula is A / B, where A is Operating expense, B is passenger. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Operating expense per passenger on the desired side of its target for this period?

Inputs:

- `metric.operating-expense` (Operating expense)
- `metric.passenger` (passenger)

Placements:

- organizational / industries / Transportation / Organizational » Industries (sK575, page_0182)
- organizational / industries / Transportation / Organizationals - Industries (sK3575, page_0187)
- organizational / industries / Sport / General (aK3575, page_0192)
- organizational / industries / Sport / General (xK575, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fuel consumption

- id: `kpi.transportation.fuel-consumption`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fuel consumption measures that result inside Transportation, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Fuel consumption. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fuel consumption on the desired side of its target for this period?

Inputs:

- `metric.fuel-consumption` (Fuel consumption)

Placements:

- organizational / industries / Transportation / Organizational » Industries (sK590, page_0182)
- organizational / industries / Transportation / Organizationals - Industries (sK3590, page_0187)
- organizational / industries / Sport / General (aK3509, page_0192)
- organizational / industries / Sport / General (xK590, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Passengers who purchased return tickets

- id: `kpi.transportation.passengers-who-purchased-return-tickets`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: operational
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.transportation.organizational-industries`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Passengers who purchased return tickets measures that result inside Transportation, subcategory Organizational » Industries. The unit is percent. The formula is (A / B) * 100, where A is part named by Passengers who purchased return tickets, B is whole named by Passengers who purchased return tickets. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Passengers who purchased return tickets on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-passengers-who-purchased-return-tickets` (part named by Passengers who purchased return tickets)
- `metric.whole-named-by-passengers-who-purchased-return-tickets` (whole named by Passengers who purchased return tickets)

Placements:

- organizational / industries / Transportation / Organizational » Industries (sK572, page_0182)
- organizational / industries / Sport / General (aK3723, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Vehicles out of service

- id: `kpi.transportation.vehicles-out-of-service`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.organizationals-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Vehicles out of service measures that result inside Transportation, subcategory Organizationals - Industries. The unit is count. The formula is A, where A is Vehicles out of service. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Vehicles out of service on the desired side of its target for this period?

Inputs:

- `metric.vehicles-out-of-service` (Vehicles out of service)

Placements:

- organizational / industries / Transportation / Organizationals - Industries (sK2835, page_0187)
- organizational / industries / Sport / General (aK2835, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fuel efficiency

- id: `kpi.transportation.fuel-efficiency`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.transportation.organizationals-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fuel efficiency measures that result inside Transportation, subcategory Organizationals - Industries. The unit is count. The formula is A, where A is Fuel efficiency. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fuel efficiency on the desired side of its target for this period?

Inputs:

- `metric.fuel-efficiency` (Fuel efficiency)

Placements:

- organizational / industries / Transportation / Organizationals - Industries (sK3591, page_0187)
- organizational / industries / Sport / General (aK3591, page_0192)
- organizational / industries / Sport / Organization= Industries (sK20841, page_0199)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Vehicle revenue per liter of fuel

- id: `kpi.transportation.vehicle-revenue-per-liter-of-fuel`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation.organizationals-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Vehicle revenue per liter of fuel measures that result inside Transportation, subcategory Organizationals - Industries. The unit is count. The formula is A / B, where A is Vehicle revenue, B is liter of fuel. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Vehicle revenue per liter of fuel on the desired side of its target for this period?

Inputs:

- `metric.vehicle-revenue` (Vehicle revenue)
- `metric.liter-of-fuel` (liter of fuel)

Placements:

- organizational / industries / Transportation / Organizationals - Industries (sK3594, page_0187)
- organizational / industries / Sport / General (aK3593, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fuel cost savings per vehicle

- id: `kpi.transportation.fuel-cost-savings-per-vehicle`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.transportation.organizationals-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fuel cost savings per vehicle measures that result inside Transportation, subcategory Organizationals - Industries. The unit is count. The formula is A / B, where A is Fuel cost savings, B is vehicle. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fuel cost savings per vehicle on the desired side of its target for this period?

Inputs:

- `metric.fuel-cost-savings` (Fuel cost savings)
- `metric.vehicle` (vehicle)

Placements:

- organizational / industries / Transportation / Organizationals - Industries (sK3594, page_0187)
- organizational / industries / Sport / General (aK3594, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Drivers per licensed vehicle

- id: `kpi.sport.drivers-per-licensed-vehicle`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Drivers per licensed vehicle measures that result inside Sport, subcategory General. The unit is count. The formula is A / B, where A is Drivers, B is licensed vehicle. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Drivers per licensed vehicle on the desired side of its target for this period?

Inputs:

- `metric.drivers` (Drivers)
- `metric.licensed-vehicle` (licensed vehicle)

Placements:

- organizational / industries / Sport / General (aK3630, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Vehicles on maintenance or repair

- id: `kpi.sport.vehicles-on-maintenance-or-repair`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Vehicles on maintenance or repair measures that result inside Sport, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Vehicles on maintenance or repair, B is whole named by Vehicles on maintenance or repair. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Vehicles on maintenance or repair on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-vehicles-on-maintenance-or-repair` (part named by Vehicles on maintenance or repair)
- `metric.whole-named-by-vehicles-on-maintenance-or-repair` (whole named by Vehicles on maintenance or repair)

Placements:

- organizational / industries / Sport / General (aK3649, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Passengers per vehicle per day (FPPVD)

- id: `kpi.sport.passengers-per-vehicle-per-day-fppvd`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Passengers per vehicle per day (FPPVD) measures that result inside Sport, subcategory General. The unit is count. The formula is A / B, where A is Passengers, B is vehicle per day (FPPVD). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Passengers per vehicle per day (FPPVD) on the desired side of its target for this period?

Inputs:

- `metric.passengers` (Passengers)
- `metric.vehicle-per-day-fppvd` (vehicle per day (FPPVD))

Placements:

- organizational / industries / Sport / General (aK3650, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Passengers carried over next work betweenly public transport

- id: `kpi.sport.passengers-carried-over-next-work-betweenly-public-transport`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Passengers carried over next work betweenly public transport measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Passengers carried over next work betweenly public transport. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Passengers carried over next work betweenly public transport on the desired side of its target for this period?

Inputs:

- `metric.passengers-carried-over-next-work-betweenly-public-transport` (Passengers carried over next work betweenly public transport)

Placements:

- organizational / industries / Sport / General (aK3652, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Kilometers traveled per vehicle

- id: `kpi.sport.kilometers-traveled-per-vehicle`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Kilometers traveled per vehicle measures that result inside Sport, subcategory General. The unit is count. The formula is A / B, where A is Kilometers traveled, B is vehicle. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Kilometers traveled per vehicle on the desired side of its target for this period?

Inputs:

- `metric.kilometers-traveled` (Kilometers traveled)
- `metric.vehicle` (vehicle)

Placements:

- organizational / industries / Sport / General (aK3695, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Passenger distance traveled per day

- id: `kpi.sport.passenger-distance-traveled-per-day`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Passenger distance traveled per day measures that result inside Sport, subcategory General. The unit is count. The formula is A / B, where A is Passenger distance traveled, B is day. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Passenger distance traveled per day on the desired side of its target for this period?

Inputs:

- `metric.passenger-distance-traveled` (Passenger distance traveled)
- `metric.day` (day)

Placements:

- organizational / industries / Sport / General (aK3696, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Public transport fare category

- id: `kpi.sport.public-transport-fare-category`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Public transport fare category measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Public transport fare category. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Public transport fare category on the desired side of its target for this period?

Inputs:

- `metric.public-transport-fare-category` (Public transport fare category)

Placements:

- organizational / industries / Sport / General (aK3670, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Bus fleet operated

- id: `kpi.sport.bus-fleet-operated`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Bus fleet operated measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Bus fleet operated. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Bus fleet operated on the desired side of its target for this period?

Inputs:

- `metric.bus-fleet-operated` (Bus fleet operated)

Placements:

- organizational / industries / Sport / General (aK3871, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Bus routes in operation

- id: `kpi.sport.bus-routes-in-operation`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Bus routes in operation measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Bus routes in operation. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Bus routes in operation on the desired side of its target for this period?

Inputs:

- `metric.bus-routes-in-operation` (Bus routes in operation)

Placements:

- organizational / industries / Sport / General (aK3874, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Public transport network density

- id: `kpi.sport.public-transport-network-density`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Public transport network density measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Public transport network density. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Public transport network density on the desired side of its target for this period?

Inputs:

- `metric.public-transport-network-density` (Public transport network density)

Placements:

- organizational / industries / Sport / General (aK3876, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of transport to main tourist sites

- id: `kpi.sport.cost-of-transport-to-main-tourist-sites`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of transport to main tourist sites measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Cost of transport to main tourist sites. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of transport to main tourist sites on the desired side of its target for this period?

Inputs:

- `metric.cost-of-transport-to-main-tourist-sites` (Cost of transport to main tourist sites)

Placements:

- organizational / industries / Sport / General (aK3877, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New public transport vehicles acquisition cost

- id: `kpi.sport.new-public-transport-vehicles-acquisition-cost`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

New public transport vehicles acquisition cost measures that result inside Sport, subcategory General. The unit is currency. The formula is A, where A is New public transport vehicles acquisition cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New public transport vehicles acquisition cost on the desired side of its target for this period?

Inputs:

- `metric.new-public-transport-vehicles-acquisition-cost` (New public transport vehicles acquisition cost)

Placements:

- organizational / industries / Sport / General (aK3878, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Daily traffic volume

- id: `kpi.sport.daily-traffic-volume`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Daily traffic volume measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Daily traffic volume. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Daily traffic volume on the desired side of its target for this period?

Inputs:

- `metric.daily-traffic-volume` (Daily traffic volume)

Placements:

- organizational / industries / Sport / General (aK3879, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Public transport fare

- id: `kpi.sport.public-transport-fare`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Public transport fare measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Public transport fare. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Public transport fare on the desired side of its target for this period?

Inputs:

- `metric.public-transport-fare` (Public transport fare)

Placements:

- organizational / industries / Sport / General (aK3880, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Monthly cost of work trips by public transport

- id: `kpi.sport.monthly-cost-of-work-trips-by-public-transport`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Monthly cost of work trips by public transport measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Monthly cost of work trips by public transport. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Monthly cost of work trips by public transport on the desired side of its target for this period?

Inputs:

- `metric.monthly-cost-of-work-trips-by-public-transport` (Monthly cost of work trips by public transport)

Placements:

- organizational / industries / Sport / General (aK3881, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Public transport share of all motorized trips to work

- id: `kpi.sport.public-transport-share-of-all-motorized-trips-to-work`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Public transport share of all motorized trips to work measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Public transport share of all motorized trips to work. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Public transport share of all motorized trips to work on the desired side of its target for this period?

Inputs:

- `metric.public-transport-share-of-all-motorized-trips-to-work` (Public transport share of all motorized trips to work)

Placements:

- organizational / industries / Sport / General (aK3883, page_0192)
- organizational / industries / Sport / Organizational » industries (xK21143, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fare subsidy per passenger trip

- id: `kpi.sport.fare-subsidy-per-passenger-trip`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fare subsidy per passenger trip measures that result inside Sport, subcategory General. The unit is count. The formula is A / B, where A is Fare subsidy, B is passenger trip. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fare subsidy per passenger trip on the desired side of its target for this period?

Inputs:

- `metric.fare-subsidy` (Fare subsidy)
- `metric.passenger-trip` (passenger trip)

Placements:

- organizational / industries / Sport / General (aK3884, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Operating buses per kilometer of public transport network length

- id: `kpi.sport.operating-buses-per-kilometer-of-public-transport-network-length`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Operating buses per kilometer of public transport network length measures that result inside Sport, subcategory General. The unit is count. The formula is A / B, where A is Operating buses, B is kilometer of public transport network length. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Operating buses per kilometer of public transport network length on the desired side of its target for this period?

Inputs:

- `metric.operating-buses` (Operating buses)
- `metric.kilometer-of-public-transport-network-length` (kilometer of public transport network length)

Placements:

- organizational / industries / Sport / General (aK3886, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Passenger trips

- id: `kpi.sport.passenger-trips`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Passenger trips measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Passenger trips. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Passenger trips on the desired side of its target for this period?

Inputs:

- `metric.passenger-trips` (Passenger trips)

Placements:

- organizational / industries / Sport / General (aK3888, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Daily vehicle kilometers traveled

- id: `kpi.sport.daily-vehicle-kilometers-traveled`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Daily vehicle kilometers traveled measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Daily vehicle kilometers traveled. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Daily vehicle kilometers traveled on the desired side of its target for this period?

Inputs:

- `metric.daily-vehicle-kilometers-traveled` (Daily vehicle kilometers traveled)

Placements:

- organizational / industries / Sport / General (aK3890, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Ticket consumption per public transport

- id: `kpi.sport.ticket-consumption-per-public-transport`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Ticket consumption per public transport measures that result inside Sport, subcategory General. The unit is count. The formula is A / B, where A is Ticket consumption, B is public transport. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Ticket consumption per public transport on the desired side of its target for this period?

Inputs:

- `metric.ticket-consumption` (Ticket consumption)
- `metric.public-transport` (public transport)

Placements:

- organizational / industries / Sport / General (aK3890, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Public transportation stations in operation

- id: `kpi.sport.public-transportation-stations-in-operation`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Public transportation stations in operation measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Public transportation stations in operation. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Public transportation stations in operation on the desired side of its target for this period?

Inputs:

- `metric.public-transportation-stations-in-operation` (Public transportation stations in operation)

Placements:

- organizational / industries / Sport / General (aK3896, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Public transport interchanges

- id: `kpi.sport.public-transport-interchanges`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Public transport interchanges measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Public transport interchanges. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Public transport interchanges on the desired side of its target for this period?

Inputs:

- `metric.public-transport-interchanges` (Public transport interchanges)

Placements:

- organizational / industries / Sport / General (aK3897, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Ticket revenue per operating bus

- id: `kpi.sport.ticket-revenue-per-operating-bus`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Ticket revenue per operating bus measures that result inside Sport, subcategory General. The unit is count. The formula is A / B, where A is Ticket revenue, B is operating bus. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Ticket revenue per operating bus on the desired side of its target for this period?

Inputs:

- `metric.ticket-revenue` (Ticket revenue)
- `metric.operating-bus` (operating bus)

Placements:

- organizational / industries / Sport / General (aK3898, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Tax stand prices per square kilometer

- id: `kpi.sport.tax-stand-prices-per-square-kilometer`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Tax stand prices per square kilometer measures that result inside Sport, subcategory General. The unit is count. The formula is A / B, where A is Tax stand prices, B is square kilometer. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Tax stand prices per square kilometer on the desired side of its target for this period?

Inputs:

- `metric.tax-stand-prices` (Tax stand prices)
- `metric.square-kilometer` (square kilometer)

Placements:

- organizational / industries / Sport / General (aK3900, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Bus stops per square kilometer

- id: `kpi.sport.bus-stops-per-square-kilometer`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Bus stops per square kilometer measures that result inside Sport, subcategory General. The unit is count. The formula is A / B, where A is Bus stops, B is square kilometer. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Bus stops per square kilometer on the desired side of its target for this period?

Inputs:

- `metric.bus-stops` (Bus stops)
- `metric.square-kilometer` (square kilometer)

Placements:

- organizational / industries / Sport / General (aK3902, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Public transport routes

- id: `kpi.sport.public-transport-routes`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Public transport routes measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Public transport routes. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Public transport routes on the desired side of its target for this period?

Inputs:

- `metric.public-transport-routes` (Public transport routes)

Placements:

- organizational / industries / Sport / General (aK3903, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Tickets revenue per operating expense

- id: `kpi.sport.tickets-revenue-per-operating-expense`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Tickets revenue per operating expense measures that result inside Sport, subcategory General. The unit is count. The formula is A / B, where A is Tickets revenue, B is operating expense. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Tickets revenue per operating expense on the desired side of its target for this period?

Inputs:

- `metric.tickets-revenue` (Tickets revenue)
- `metric.operating-expense` (operating expense)

Placements:

- organizational / industries / Sport / General (aK3904, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Daily tickets beyond tariff life

- id: `kpi.sport.daily-tickets-beyond-tariff-life`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Daily tickets beyond tariff life measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Daily tickets beyond tariff life. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Daily tickets beyond tariff life on the desired side of its target for this period?

Inputs:

- `metric.daily-tickets-beyond-tariff-life` (Daily tickets beyond tariff life)

Placements:

- organizational / industries / Sport / General (aK3906, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Daily passenger journeys

- id: `kpi.sport.daily-passenger-journeys`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Daily passenger journeys measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Daily passenger journeys. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Daily passenger journeys on the desired side of its target for this period?

Inputs:

- `metric.daily-passenger-journeys` (Daily passenger journeys)

Placements:

- organizational / industries / Sport / General (aK3907, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Daily passenger fares

- id: `kpi.sport.daily-passenger-fares`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Daily passenger fares measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Daily passenger fares. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Daily passenger fares on the desired side of its target for this period?

Inputs:

- `metric.daily-passenger-fares` (Daily passenger fares)

Placements:

- organizational / industries / Sport / General (aK3908, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Daily fares per person

- id: `kpi.sport.daily-fares-per-person`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Daily fares per person measures that result inside Sport, subcategory General. The unit is count. The formula is A / B, where A is Daily fares, B is person. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Daily fares per person on the desired side of its target for this period?

Inputs:

- `metric.daily-fares` (Daily fares)
- `metric.person` (person)

Placements:

- organizational / industries / Sport / General (aK3909, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Journey length for a public transport vehicle

- id: `kpi.sport.journey-length-for-a-public-transport-vehicle`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Journey length for a public transport vehicle measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Journey length for a public transport vehicle. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Journey length for a public transport vehicle on the desired side of its target for this period?

Inputs:

- `metric.journey-length-for-a-public-transport-vehicle` (Journey length for a public transport vehicle)

Placements:

- organizational / industries / Sport / General (aK3910, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### In service bus kilometers delivered

- id: `kpi.sport.in-service-bus-kilometers-delivered`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

In service bus kilometers delivered measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is In service bus kilometers delivered. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is In service bus kilometers delivered on the desired side of its target for this period?

Inputs:

- `metric.in-service-bus-kilometers-delivered` (In service bus kilometers delivered)

Placements:

- organizational / industries / Sport / General (aK3914, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Passenger boarding and trip per outsourced

- id: `kpi.sport.passenger-boarding-and-trip-per-outsourced`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Passenger boarding and trip per outsourced measures that result inside Sport, subcategory General. The unit is count. The formula is A / B, where A is Passenger boarding and trip, B is outsourced. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Passenger boarding and trip per outsourced on the desired side of its target for this period?

Inputs:

- `metric.passenger-boarding-and-trip` (Passenger boarding and trip)
- `metric.outsourced` (outsourced)

Placements:

- organizational / industries / Sport / General (aK3915, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Passenger satisfaction with public transport quality

- id: `kpi.sport.passenger-satisfaction-with-public-transport-quality`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: survey
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Passenger satisfaction with public transport quality measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Passenger satisfaction with public transport quality. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Passenger satisfaction with public transport quality on the desired side of its target for this period?

Inputs:

- `metric.passenger-satisfaction-with-public-transport-quality` (Passenger satisfaction with public transport quality)

Placements:

- organizational / industries / Sport / General (aK3917, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Age of public transport vehicles

- id: `kpi.sport.age-of-public-transport-vehicles`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Age of public transport vehicles measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Age of public transport vehicles. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Age of public transport vehicles on the desired side of its target for this period?

Inputs:

- `metric.age-of-public-transport-vehicles` (Age of public transport vehicles)

Placements:

- organizational / industries / Sport / General (aK3918, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Vehicles complying with the safety public transportation standards

- id: `kpi.sport.vehicles-complying-with-the-safety-public-transportation-standards`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Vehicles complying with the safety public transportation standards measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Vehicles complying with the safety public transportation standards. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Vehicles complying with the safety public transportation standards on the desired side of its target for this period?

Inputs:

- `metric.vehicles-complying-with-the-safety-public-transportation-standards` (Vehicles complying with the safety public transportation standards)

Placements:

- organizational / industries / Sport / General (aK3919, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Trips operated in full

- id: `kpi.sport.trips-operated-in-full`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Trips operated in full measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Trips operated in full. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Trips operated in full on the desired side of its target for this period?

Inputs:

- `metric.trips-operated-in-full` (Trips operated in full)

Placements:

- organizational / industries / Sport / General (aK3920, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Public transport facilities

- id: `kpi.sport.public-transport-facilities`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Public transport facilities measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Public transport facilities. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Public transport facilities on the desired side of its target for this period?

Inputs:

- `metric.public-transport-facilities` (Public transport facilities)

Placements:

- organizational / industries / Sport / General (aK3924, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### In service bus hours delivered

- id: `kpi.sport.in-service-bus-hours-delivered`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

In service bus hours delivered measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is In service bus hours delivered. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is In service bus hours delivered on the desired side of its target for this period?

Inputs:

- `metric.in-service-bus-hours-delivered` (In service bus hours delivered)

Placements:

- organizational / industries / Sport / General (aK3931, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Utilization of public transport fleet

- id: `kpi.sport.utilization-of-public-transport-fleet`
- kind: kpi
- unit: count
- direction: corridor
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Utilization of public transport fleet measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Utilization of public transport fleet. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Utilization of public transport fleet on the desired side of its target for this period?

Inputs:

- `metric.utilization-of-public-transport-fleet` (Utilization of public transport fleet)

Placements:

- organizational / industries / Sport / General (aK3935, page_0192)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Seat availability

- id: `kpi.sport.seat-availability`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Seat availability measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Seat availability. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Seat availability on the desired side of its target for this period?

Inputs:

- `metric.seat-availability` (Seat availability)

Placements:

- organizational / industries / Sport / General (xK57, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Pumping

- id: `kpi.sport.pumping`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Pumping measures that result inside Sport, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Pumping, B is whole named by Pumping. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Pumping on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-pumping` (part named by Pumping)
- `metric.whole-named-by-pumping` (whole named by Pumping)

Placements:

- organizational / industries / Sport / General (xK699, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Critical equipment and system failures

- id: `kpi.sport.critical-equipment-and-system-failures`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Critical equipment and system failures measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Critical equipment and system failures. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Critical equipment and system failures on the desired side of its target for this period?

Inputs:

- `metric.critical-equipment-and-system-failures` (Critical equipment and system failures)

Placements:

- organizational / industries / Sport / General (xK240, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Port state control (PSIC) expected ships

- id: `kpi.sport.port-state-control-psic-expected-ships`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Port state control (PSIC) expected ships measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Port state control (PSIC) expected ships. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Port state control (PSIC) expected ships on the desired side of its target for this period?

Inputs:

- `metric.port-state-control-psic-expected-ships` (Port state control (PSIC) expected ships)

Placements:

- organizational / industries / Sport / General (xK487, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Navigation deficiency ratio

- id: `kpi.sport.navigation-deficiency-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Navigation deficiency ratio measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Navigation deficiency ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Navigation deficiency ratio on the desired side of its target for this period?

Inputs:

- `metric.navigation-deficiency-ratio` (Navigation deficiency ratio)

Placements:

- organizational / industries / Sport / General (xK496, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cargo handling incidents

- id: `kpi.sport.cargo-handling-incidents`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cargo handling incidents measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Cargo handling incidents. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cargo handling incidents on the desired side of its target for this period?

Inputs:

- `metric.cargo-handling-incidents` (Cargo handling incidents)

Placements:

- organizational / industries / Sport / General (xK497, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Port state count (PSIC) detention rate

- id: `kpi.sport.port-state-count-psic-detention-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Port state count (PSIC) detention rate measures that result inside Sport, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is numerator of Port state count (PSIC) detention rate, B is base of Port state count (PSIC) detention rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Port state count (PSIC) detention rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-port-state-count-psic-detention-rate` (numerator of Port state count (PSIC) detention rate)
- `metric.base-of-port-state-count-psic-detention-rate` (base of Port state count (PSIC) detention rate)

Placements:

- organizational / industries / Sport / General (xK503, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Vessel operational deficiencies

- id: `kpi.sport.vessel-operational-deficiencies`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Vessel operational deficiencies measures that result inside Sport, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is numerator of Vessel operational deficiencies, B is base of Vessel operational deficiencies. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Vessel operational deficiencies on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-vessel-operational-deficiencies` (numerator of Vessel operational deficiencies)
- `metric.base-of-vessel-operational-deficiencies` (base of Vessel operational deficiencies)

Placements:

- organizational / industries / Sport / General (xK524, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Vessel groundings

- id: `kpi.sport.vessel-groundings`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Vessel groundings measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Vessel groundings. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Vessel groundings on the desired side of its target for this period?

Inputs:

- `metric.vessel-groundings` (Vessel groundings)

Placements:

- organizational / industries / Sport / General (xK525, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cargo units transported

- id: `kpi.sport.cargo-units-transported`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cargo units transported measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Cargo units transported. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cargo units transported on the desired side of its target for this period?

Inputs:

- `metric.cargo-units-transported` (Cargo units transported)

Placements:

- organizational / industries / Sport / General (xK526, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Crew deficiencies reported

- id: `kpi.sport.crew-deficiencies-reported`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Crew deficiencies reported measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Crew deficiencies reported. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Crew deficiencies reported on the desired side of its target for this period?

Inputs:

- `metric.crew-deficiencies-reported` (Crew deficiencies reported)

Placements:

- organizational / industries / Sport / General (xK529, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Marine safety deficiency ratio

- id: `kpi.sport.marine-safety-deficiency-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Marine safety deficiency ratio measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Marine safety deficiency ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Marine safety deficiency ratio on the desired side of its target for this period?

Inputs:

- `metric.marine-safety-deficiency-ratio` (Marine safety deficiency ratio)

Placements:

- organizational / industries / Sport / General (xK544, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Transport volume handled by the port railway

- id: `kpi.sport.transport-volume-handled-by-the-port-railway`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Transport volume handled by the port railway measures that result inside Sport, subcategory General. The unit is count. The formula is A, where A is Transport volume handled by the port railway. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Transport volume handled by the port railway on the desired side of its target for this period?

Inputs:

- `metric.transport-volume-handled-by-the-port-railway` (Transport volume handled by the port railway)

Placements:

- organizational / industries / Sport / General (xK777, page_0196)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
