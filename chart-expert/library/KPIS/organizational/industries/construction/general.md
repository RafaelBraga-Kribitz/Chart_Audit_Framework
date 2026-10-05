# Construction / General

Context: organizational. Group: industries. KPIs: 69.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Project cost contingency

- id: `kpi.management.project-cost-contingency`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Project cost contingency measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Project cost contingency, B is whole named by Project cost contingency. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Project cost contingency on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-project-cost-contingency` (part named by Project cost contingency)
- `metric.whole-named-by-project-cost-contingency` (whole named by Project cost contingency)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK6257, page_0046)
- organizational / industries / Construction / General (sS6527, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Requests for time extension submitted

- id: `kpi.management.requests-for-time-extension-submitted`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Requests for time extension submitted measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Requests for time extension submitted. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Requests for time extension submitted on the desired side of its target for this period?

Inputs:

- `metric.requests-for-time-extension-submitted` (Requests for time extension submitted)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK6758, page_0046)
- organizational / industries / Construction / Organizational » Industries (s80758, page_0068)
- organizational / industries / Construction / General (sS6758, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Order value variance from original contract value

- id: `kpi.management.order-value-variance-from-original-contract-value`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.xkpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Order value variance from original contract value measures that result inside Management, subcategory xKPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is Order value variance, B is original contract value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Order value variance from original contract value on the desired side of its target for this period?

Inputs:

- `metric.order-value-variance` (Order value variance)
- `metric.original-contract-value` (original contract value)

Placements:

- organizational / functional / Management / xKPI # Key Performance Indicator name (xK6855, page_0046)
- organizational / functional / Management / xKPI # Key Performance Indicator name (xK6865, page_0053)
- organizational / industries / Construction / General (sS6865, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time to rectify defects

- id: `kpi.sales-and-customer-service.time-to-rectify-defects`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time to rectify defects measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is count. The formula is A, where A is Time to rectify defects. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time to rectify defects on the desired side of its target for this period?

Inputs:

- `metric.time-to-rectify-defects` (Time to rectify defects)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK433, page_0049)
- organizational / industries / Construction / General (sK433, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of construction

- id: `kpi.construction.cost-of-construction`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.kpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of construction measures that result inside Construction, subcategory KPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is Cost, B is construction. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of construction on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.construction` (construction)

Placements:

- organizational / industries / Construction / KPI # Key Performance Indicator name (s6411, page_0067)
- organizational / industries / Construction / General (sS4417, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Construction related incidents, injuries and fatalities reported

- id: `kpi.construction.construction-related-incidents-injuries-and-fatalities-reported`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.kpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Construction related incidents, injuries and fatalities reported measures that result inside Construction, subcategory KPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Construction related incidents, injuries and fatalities reported. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Construction related incidents, injuries and fatalities reported on the desired side of its target for this period?

Inputs:

- `metric.construction-related-incidents-injuries-and-fatalities-reported` (Construction related incidents, injuries and fatalities reported)

Placements:

- organizational / industries / Construction / KPI # Key Performance Indicator name (sK5454, page_0067)
- organizational / industries / Construction / General (sS4544, page_0068)
- global / human-development / Transportation and Infrastructure / General (sK5454, page_0109)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Committed costs

- id: `kpi.construction.committed-costs`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.kpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Committed costs measures that result inside Construction, subcategory KPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Committed costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Committed costs on the desired side of its target for this period?

Inputs:

- `metric.committed-costs` (Committed costs)

Placements:

- organizational / industries / Construction / KPI # Key Performance Indicator name (sK5606, page_0067)
- organizational / industries / Construction / General (sS5666, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time predictability for design

- id: `kpi.construction.time-predictability-for-design`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.kpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time predictability for design measures that result inside Construction, subcategory KPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Time predictability for design, B is whole named by Time predictability for design. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time predictability for design on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-time-predictability-for-design` (part named by Time predictability for design)
- `metric.whole-named-by-time-predictability-for-design` (whole named by Time predictability for design)

Placements:

- organizational / industries / Construction / KPI # Key Performance Indicator name (sK6089, page_0067)
- organizational / industries / Construction / General (sS6089, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time predictability for construction

- id: `kpi.construction.time-predictability-for-construction`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.kpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time predictability for construction measures that result inside Construction, subcategory KPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Time predictability for construction, B is whole named by Time predictability for construction. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time predictability for construction on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-time-predictability-for-construction` (part named by Time predictability for construction)
- `metric.whole-named-by-time-predictability-for-construction` (whole named by Time predictability for construction)

Placements:

- organizational / industries / Construction / KPI # Key Performance Indicator name (sK6090, page_0067)
- organizational / industries / Construction / General (sS6090, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time predictability for design and construction

- id: `kpi.construction.time-predictability-for-design-and-construction`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.kpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time predictability for design and construction measures that result inside Construction, subcategory KPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Time predictability for design and construction, B is whole named by Time predictability for design and construction. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time predictability for design and construction on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-time-predictability-for-design-and-construction` (part named by Time predictability for design and construction)
- `metric.whole-named-by-time-predictability-for-design-and-construction` (whole named by Time predictability for design and construction)

Placements:

- organizational / industries / Construction / KPI # Key Performance Indicator name (sK6091, page_0067)
- organizational / industries / Construction / General (sS6091, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Construction design scope specifications met in full

- id: `kpi.construction.construction-design-scope-specifications-met-in-full`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.kpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Construction design scope specifications met in full measures that result inside Construction, subcategory KPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Construction design scope specifications met in full, B is whole named by Construction design scope specifications met in full. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Construction design scope specifications met in full on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-construction-design-scope-specifications-met-in-full` (part named by Construction design scope specifications met in full)
- `metric.whole-named-by-construction-design-scope-specifications-met-in-full` (whole named by Construction design scope specifications met in full)

Placements:

- organizational / industries / Construction / KPI # Key Performance Indicator name (sK6092, page_0067)
- organizational / industries / Construction / General (sS6092, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost to rectify defects in the maintenance period

- id: `kpi.construction.cost-to-rectify-defects-in-the-maintenance-period`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.kpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost to rectify defects in the maintenance period measures that result inside Construction, subcategory KPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is Cost, B is rectify defects in the maintenance period. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost to rectify defects in the maintenance period on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.rectify-defects-in-the-maintenance-period` (rectify defects in the maintenance period)

Placements:

- organizational / industries / Construction / KPI # Key Performance Indicator name (sK6304, page_0067)
- organizational / industries / Construction / General (sS6344, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost predictability at construction

- id: `kpi.construction.cost-predictability-at-construction`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.kpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost predictability at construction measures that result inside Construction, subcategory KPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is part named by Cost predictability at construction, B is whole named by Cost predictability at construction. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost predictability at construction on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-cost-predictability-at-construction` (part named by Cost predictability at construction)
- `metric.whole-named-by-cost-predictability-at-construction` (whole named by Cost predictability at construction)

Placements:

- organizational / industries / Construction / KPI # Key Performance Indicator name (sK6306, page_0067)
- organizational / industries / Construction / General (sS6306, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost predictability at construction due to project manager change orders

- id: `kpi.construction.cost-predictability-at-construction-due-to-project-manager-change-orders`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.kpi-key-performance-indicator-name`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost predictability at construction due to project manager change orders measures that result inside Construction, subcategory KPI # Key Performance Indicator name. The unit is percent. The formula is (A / B) * 100, where A is Cost predictability at construction due, B is project manager change orders. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost predictability at construction due to project manager change orders on the desired side of its target for this period?

Inputs:

- `metric.cost-predictability-at-construction-due` (Cost predictability at construction due)
- `metric.project-manager-change-orders` (project manager change orders)

Placements:

- organizational / industries / Construction / KPI # Key Performance Indicator name (sK6333, page_0067)
- organizational / industries / Construction / General (sS6333, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Predictability of the construction project profit

- id: `kpi.construction.predictability-of-the-construction-project-profit`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.organizational-industries`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Predictability of the construction project profit measures that result inside Construction, subcategory Organizational » Industries. The unit is percent. The formula is (A / B) * 100, where A is Predictability, B is the construction project profit. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Predictability of the construction project profit on the desired side of its target for this period?

Inputs:

- `metric.predictability` (Predictability)
- `metric.the-construction-project-profit` (the construction project profit)

Placements:

- organizational / industries / Construction / Organizational » Industries (s80337, page_0068)
- organizational / industries / Construction / General (sS6337, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost predictability

- id: `kpi.construction.cost-predictability`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost predictability measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Cost predictability, B is whole named by Cost predictability. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost predictability on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-cost-predictability` (part named by Cost predictability)
- `metric.whole-named-by-cost-predictability` (whole named by Cost predictability)

Placements:

- organizational / industries / Construction / General (sS438, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Construction cost in use

- id: `kpi.construction.construction-cost-in-use`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Construction cost in use measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Construction cost in use, B is whole named by Construction cost in use. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Construction cost in use on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-construction-cost-in-use` (part named by Construction cost in use)
- `metric.whole-named-by-construction-cost-in-use` (whole named by Construction cost in use)

Placements:

- organizational / industries / Construction / General (sS773, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### cost to complete

- id: `kpi.construction.cost-to-complete`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

cost to complete measures that result inside Construction, subcategory General. The unit is currency. The formula is A, where A is cost to complete. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is cost to complete on the desired side of its target for this period?

Inputs:

- `metric.cost-to-complete` (cost to complete)

Placements:

- organizational / industries / Construction / General (sK3256, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Man hours spent for punch items

- id: `kpi.construction.man-hours-spent-for-punch-items`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Man hours spent for punch items measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Man hours spent for punch items, B is whole named by Man hours spent for punch items. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Man hours spent for punch items on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-man-hours-spent-for-punch-items` (part named by Man hours spent for punch items)
- `metric.whole-named-by-man-hours-spent-for-punch-items` (whole named by Man hours spent for punch items)

Placements:

- organizational / industries / Construction / General (sS5902, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time to rectify defects in maintenance period

- id: `kpi.construction.time-to-rectify-defects-in-maintenance-period`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time to rectify defects in maintenance period measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Time to rectify defects in maintenance period. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time to rectify defects in maintenance period on the desired side of its target for this period?

Inputs:

- `metric.time-to-rectify-defects-in-maintenance-period` (Time to rectify defects in maintenance period)

Placements:

- organizational / industries / Construction / General (sS6093, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost predictability at design

- id: `kpi.construction.cost-predictability-at-design`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost predictability at design measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Cost predictability at design, B is whole named by Cost predictability at design. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost predictability at design on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-cost-predictability-at-design` (part named by Cost predictability at design)
- `metric.whole-named-by-cost-predictability-at-design` (whole named by Cost predictability at design)

Placements:

- organizational / industries / Construction / General (sS6305, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Quality reliability at design and construction

- id: `kpi.construction.quality-reliability-at-design-and-construction`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Quality reliability at design and construction measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Quality reliability at design and construction. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Quality reliability at design and construction on the desired side of its target for this period?

Inputs:

- `metric.quality-reliability-at-design-and-construction` (Quality reliability at design and construction)

Placements:

- organizational / industries / Construction / General (sS6307, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Quality issues at Available for Use

- id: `kpi.construction.quality-issues-at-available-for-use`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Quality issues at Available for Use measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Quality issues at Available for Use. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Quality issues at Available for Use on the desired side of its target for this period?

Inputs:

- `metric.quality-issues-at-available-for-use` (Quality issues at Available for Use)

Placements:

- organizational / industries / Construction / General (sS6309, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of rewards

- id: `kpi.construction.cost-of-rewards`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of rewards measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Cost of rewards. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of rewards on the desired side of its target for this period?

Inputs:

- `metric.cost-of-rewards` (Cost of rewards)

Placements:

- organizational / industries / Construction / General (sS6309, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Precedural audits

- id: `kpi.construction.precedural-audits`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Precedural audits measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Precedural audits. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Precedural audits on the desired side of its target for this period?

Inputs:

- `metric.precedural-audits` (Precedural audits)

Placements:

- organizational / industries / Construction / General (sS6310, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Accident prediction techniques in place

- id: `kpi.construction.accident-prediction-techniques-in-place`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Accident prediction techniques in place measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Accident prediction techniques in place. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Accident prediction techniques in place on the desired side of its target for this period?

Inputs:

- `metric.accident-prediction-techniques-in-place` (Accident prediction techniques in place)

Placements:

- organizational / industries / Construction / General (sS6311, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Quality control tests passed

- id: `kpi.construction.quality-control-tests-passed`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Quality control tests passed measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Quality control tests passed, B is whole named by Quality control tests passed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Quality control tests passed on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-quality-control-tests-passed` (part named by Quality control tests passed)
- `metric.whole-named-by-quality-control-tests-passed` (whole named by Quality control tests passed)

Placements:

- organizational / industries / Construction / General (sS6312, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time predictability at construction due project

- id: `kpi.construction.time-predictability-at-construction-due-project`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time predictability at construction due project measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Time predictability at construction due project, B is whole named by Time predictability at construction due project. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time predictability at construction due project on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-time-predictability-at-construction-due-project` (part named by Time predictability at construction due project)
- `metric.whole-named-by-time-predictability-at-construction-due-project` (whole named by Time predictability at construction due project)

Placements:

- organizational / industries / Construction / General (sS6336, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Corrective work value

- id: `kpi.construction.corrective-work-value`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Corrective work value measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Corrective work value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Corrective work value on the desired side of its target for this period?

Inputs:

- `metric.corrective-work-value` (Corrective work value)

Placements:

- organizational / industries / Construction / General (sS6869, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Construction project value represented by punch list items

- id: `kpi.construction.construction-project-value-represented-by-punch-list-items`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Construction project value represented by punch list items measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Construction project value represented by punch list items, B is whole named by Construction project value represented by punch list items. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Construction project value represented by punch list items on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-construction-project-value-represented-by-punch-list-items` (part named by Construction project value represented by punch list items)
- `metric.whole-named-by-construction-project-value-represented-by-punch-list-item` (whole named by Construction project value represented by punch list items)

Placements:

- organizational / industries / Construction / General (sS6878, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Proactive inspections that identified violations

- id: `kpi.construction.proactive-inspections-that-identified-violations`
- kind: kri
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Proactive inspections that identified violations measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Proactive inspections that identified violations, B is whole named by Proactive inspections that identified violations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Proactive inspections that identified violations on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-proactive-inspections-that-identified-violations` (part named by Proactive inspections that identified violations)
- `metric.whole-named-by-proactive-inspections-that-identified-violations` (whole named by Proactive inspections that identified violations)

Placements:

- organizational / industries / Construction / General (sS6972, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Construction sites or locations with reoccurring complaints

- id: `kpi.construction.construction-sites-or-locations-with-reoccurring-complaints`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Construction sites or locations with reoccurring complaints measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Construction sites or locations with reoccurring complaints, B is whole named by Construction sites or locations with reoccurring complaints. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Construction sites or locations with reoccurring complaints on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-construction-sites-or-locations-with-reoccurring-complaint` (part named by Construction sites or locations with reoccurring complaints)
- `metric.whole-named-by-construction-sites-or-locations-with-reoccurring-complain` (whole named by Construction sites or locations with reoccurring complaints)

Placements:

- organizational / industries / Construction / General (sS6973, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Complaints received that were followed by an onsite check

- id: `kpi.construction.complaints-received-that-were-followed-by-an-onsite-check`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Complaints received that were followed by an onsite check measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Complaints received that were followed by an onsite check, B is whole named by Complaints received that were followed by an onsite check. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Complaints received that were followed by an onsite check on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-complaints-received-that-were-followed-by-an-onsite-check` (part named by Complaints received that were followed by an onsite check)
- `metric.whole-named-by-complaints-received-that-were-followed-by-an-onsite-check` (whole named by Complaints received that were followed by an onsite check)

Placements:

- organizational / industries / Construction / General (sS6974, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Queries accepted for major construction projects

- id: `kpi.construction.queries-accepted-for-major-construction-projects`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Queries accepted for major construction projects measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Queries accepted for major construction projects. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Queries accepted for major construction projects on the desired side of its target for this period?

Inputs:

- `metric.queries-accepted-for-major-construction-projects` (Queries accepted for major construction projects)

Placements:

- organizational / industries / Construction / General (sS6975, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Building orders opened to closed ratio

- id: `kpi.construction.building-orders-opened-to-closed-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Building orders opened to closed ratio measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Building orders opened to closed ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Building orders opened to closed ratio on the desired side of its target for this period?

Inputs:

- `metric.building-orders-opened-to-closed-ratio` (Building orders opened to closed ratio)

Placements:

- organizational / industries / Construction / General (sS6976, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Existing building results

- id: `kpi.construction.existing-building-results`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Existing building results measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Existing building results, B is whole named by Existing building results. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Existing building results on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-existing-building-results` (part named by Existing building results)
- `metric.whole-named-by-existing-building-results` (whole named by Existing building results)

Placements:

- organizational / industries / Construction / General (sS6977, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Building manager is used on site

- id: `kpi.construction.building-manager-is-used-on-site`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Building manager is used on site measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Building manager is used on site, B is whole named by Building manager is used on site. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Building manager is used on site on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-building-manager-is-used-on-site` (part named by Building manager is used on site)
- `metric.whole-named-by-building-manager-is-used-on-site` (whole named by Building manager is used on site)

Placements:

- organizational / industries / Construction / General (sS6978, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Building appliances and fittings that have an energy and water ratings

- id: `kpi.construction.building-appliances-and-fittings-that-have-an-energy-and-water-ratings`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Building appliances and fittings that have an energy and water ratings measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Building appliances and fittings that have an energy and water ratings, B is whole named by Building appliances and fittings that have an energy and water ratings. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Building appliances and fittings that have an energy and water ratings on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-building-appliances-and-fittings-that-have-an-energy-and-w` (part named by Building appliances and fittings that have an energy and water ratings)
- `metric.whole-named-by-building-appliances-and-fittings-that-have-an-energy-and` (whole named by Building appliances and fittings that have an energy and water ratings)

Placements:

- organizational / industries / Construction / General (sS6979, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Days to complete first plan review

- id: `kpi.construction.days-to-complete-first-plan-review`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Days to complete first plan review measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Days to complete first plan review. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Days to complete first plan review on the desired side of its target for this period?

Inputs:

- `metric.days-to-complete-first-plan-review` (Days to complete first plan review)

Placements:

- organizational / industries / Construction / General (sS6980, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Jobs professionally certified in compliance with local regulations

- id: `kpi.construction.jobs-professionally-certified-in-compliance-with-local-regulations`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Jobs professionally certified in compliance with local regulations measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Jobs professionally certified in compliance with local regulations, B is whole named by Jobs professionally certified in compliance with local regulations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Jobs professionally certified in compliance with local regulations on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-jobs-professionally-certified-in-compliance-with-local-reg` (part named by Jobs professionally certified in compliance with local regulations)
- `metric.whole-named-by-jobs-professionally-certified-in-compliance-with-local-re` (whole named by Jobs professionally certified in compliance with local regulations)

Placements:

- organizational / industries / Construction / General (sS6981, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Construction sites proactively checked for compliance with permit conditions

- id: `kpi.construction.construction-sites-proactively-checked-for-compliance-with-permit-condit`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Construction sites proactively checked for compliance with permit conditions measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Construction sites proactively checked for compliance with permit conditions, B is whole named by Construction sites proactively checked for compliance with permit conditions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Construction sites proactively checked for compliance with permit conditions on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-construction-sites-proactively-checked-for-compliance-with` (part named by Construction sites proactively checked for compliance with permit conditions)
- `metric.whole-named-by-construction-sites-proactively-checked-for-compliance-wit` (whole named by Construction sites proactively checked for compliance with permit conditions)

Placements:

- organizational / industries / Construction / General (sS6982, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Impact on the environment

- id: `kpi.construction.impact-on-the-environment`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Impact on the environment measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Impact on the environment. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Impact on the environment on the desired side of its target for this period?

Inputs:

- `metric.impact-on-the-environment` (Impact on the environment)

Placements:

- organizational / industries / Construction / General (sS6983, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Impact on biodiversity

- id: `kpi.construction.impact-on-biodiversity`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Impact on biodiversity measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Impact on biodiversity, B is whole named by Impact on biodiversity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Impact on biodiversity on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-impact-on-biodiversity` (part named by Impact on biodiversity)
- `metric.whole-named-by-impact-on-biodiversity` (whole named by Impact on biodiversity)

Placements:

- organizational / industries / Construction / General (sS6984, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Area of habitat created or retained

- id: `kpi.construction.area-of-habitat-created-or-retained`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Area of habitat created or retained measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Area, B is habitat created or retained. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Area of habitat created or retained on the desired side of its target for this period?

Inputs:

- `metric.area` (Area)
- `metric.habitat-created-or-retained` (habitat created or retained)

Placements:

- organizational / industries / Construction / General (sS6985, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### General construction contractor

- id: `kpi.construction.general-construction-contractor`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

General construction contractor measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is General construction contractor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is General construction contractor on the desired side of its target for this period?

Inputs:

- `metric.general-construction-contractor` (General construction contractor)

Placements:

- organizational / industries / Construction / General (sS7230, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### House construction contractor

- id: `kpi.construction.house-construction-contractor`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

House construction contractor measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is House construction contractor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is House construction contractor on the desired side of its target for this period?

Inputs:

- `metric.house-construction-contractor` (House construction contractor)

Placements:

- organizational / industries / Construction / General (sS7231, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Non-residential building construction contractor

- id: `kpi.construction.non-residential-building-construction-contractor`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Non-residential building construction contractor measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Non-residential building construction contractor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Non-residential building construction contractor on the desired side of its target for this period?

Inputs:

- `metric.non-residential-building-construction-contractor` (Non-residential building construction contractor)

Placements:

- organizational / industries / Construction / General (sS7232, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Construction trade services contractor

- id: `kpi.construction.construction-trade-services-contractor`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Construction trade services contractor measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Construction trade services contractor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Construction trade services contractor on the desired side of its target for this period?

Inputs:

- `metric.construction-trade-services-contractor` (Construction trade services contractor)

Placements:

- organizational / industries / Construction / General (sS7234, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Building structure services contractor

- id: `kpi.construction.building-structure-services-contractor`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Building structure services contractor measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Building structure services contractor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Building structure services contractor on the desired side of its target for this period?

Inputs:

- `metric.building-structure-services-contractor` (Building structure services contractor)

Placements:

- organizational / industries / Construction / General (sS7235, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Building completion services contractor

- id: `kpi.construction.building-completion-services-contractor`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Building completion services contractor measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Building completion services contractor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Building completion services contractor on the desired side of its target for this period?

Inputs:

- `metric.building-completion-services-contractor` (Building completion services contractor)

Placements:

- organizational / industries / Construction / General (sS7236, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Building construction contractor

- id: `kpi.construction.building-construction-contractor`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Building construction contractor measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Building construction contractor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Building construction contractor on the desired side of its target for this period?

Inputs:

- `metric.building-construction-contractor` (Building construction contractor)

Placements:

- organizational / industries / Construction / General (sS7237, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Residential building construction contractor

- id: `kpi.construction.residential-building-construction-contractor`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Residential building construction contractor measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Residential building construction contractor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Residential building construction contractor on the desired side of its target for this period?

Inputs:

- `metric.residential-building-construction-contractor` (Residential building construction contractor)

Placements:

- organizational / industries / Construction / General (sS7238, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Non-building construction contractor

- id: `kpi.construction.non-building-construction-contractor`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Non-building construction contractor measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Non-building construction contractor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Non-building construction contractor on the desired side of its target for this period?

Inputs:

- `metric.non-building-construction-contractor` (Non-building construction contractor)

Placements:

- organizational / industries / Construction / General (sS7239, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Site preparation services contractor

- id: `kpi.construction.site-preparation-services-contractor`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Site preparation services contractor measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Site preparation services contractor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Site preparation services contractor on the desired side of its target for this period?

Inputs:

- `metric.site-preparation-services-contractor` (Site preparation services contractor)

Placements:

- organizational / industries / Construction / General (sS7241, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Installation trade services contractor

- id: `kpi.construction.installation-trade-services-contractor`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Installation trade services contractor measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Installation trade services contractor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Installation trade services contractor on the desired side of its target for this period?

Inputs:

- `metric.installation-trade-services-contractor` (Installation trade services contractor)

Placements:

- organizational / industries / Construction / General (sS7242, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Spending on new buildings

- id: `kpi.construction.spending-on-new-buildings`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Spending on new buildings measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Spending on new buildings. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Spending on new buildings on the desired side of its target for this period?

Inputs:

- `metric.spending-on-new-buildings` (Spending on new buildings)

Placements:

- organizational / industries / Construction / General (sS7243, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Spending on refurbishment

- id: `kpi.construction.spending-on-refurbishment`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Spending on refurbishment measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Spending on refurbishment. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Spending on refurbishment on the desired side of its target for this period?

Inputs:

- `metric.spending-on-refurbishment` (Spending on refurbishment)

Placements:

- organizational / industries / Construction / General (sS7244, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Spending on repairs and maintenance

- id: `kpi.construction.spending-on-repairs-and-maintenance`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Spending on repairs and maintenance measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Spending on repairs and maintenance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Spending on repairs and maintenance on the desired side of its target for this period?

Inputs:

- `metric.spending-on-repairs-and-maintenance` (Spending on repairs and maintenance)

Placements:

- organizational / industries / Construction / General (sS7245, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New project commissioned

- id: `kpi.construction.new-project-commissioned`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

New project commissioned measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is New project commissioned. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New project commissioned on the desired side of its target for this period?

Inputs:

- `metric.new-project-commissioned` (New project commissioned)

Placements:

- organizational / industries / Construction / General (sS7274, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New rebuild projects commissioned

- id: `kpi.construction.new-rebuild-projects-commissioned`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

New rebuild projects commissioned measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is New rebuild projects commissioned. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New rebuild projects commissioned on the desired side of its target for this period?

Inputs:

- `metric.new-rebuild-projects-commissioned` (New rebuild projects commissioned)

Placements:

- organizational / industries / Construction / General (sS7277, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New refurbishment projects commissioned

- id: `kpi.construction.new-refurbishment-projects-commissioned`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

New refurbishment projects commissioned measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is New refurbishment projects commissioned. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New refurbishment projects commissioned on the desired side of its target for this period?

Inputs:

- `metric.new-refurbishment-projects-commissioned` (New refurbishment projects commissioned)

Placements:

- organizational / industries / Construction / General (sS7278, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New repair and maintenance projects commissioned

- id: `kpi.construction.new-repair-and-maintenance-projects-commissioned`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

New repair and maintenance projects commissioned measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is New repair and maintenance projects commissioned. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New repair and maintenance projects commissioned on the desired side of its target for this period?

Inputs:

- `metric.new-repair-and-maintenance-projects-commissioned` (New repair and maintenance projects commissioned)

Placements:

- organizational / industries / Construction / General (sS7279, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Defects

- id: `kpi.construction.defects`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Defects measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Defects. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Defects on the desired side of its target for this period?

Inputs:

- `metric.defects` (Defects)

Placements:

- organizational / industries / Construction / General (sS7276, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Client satisfaction index for construction products

- id: `kpi.construction.client-satisfaction-index-for-construction-products`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: index
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Client satisfaction index for construction products measures that result inside Construction, subcategory General. The unit is count. The formula is (A / B) * 100, where A is current Client satisfaction index for construction products, B is base-period Client satisfaction index for construction products. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Client satisfaction index for construction products on the desired side of its target for this period?

Inputs:

- `metric.current-client-satisfaction-index-for-construction-products` (current Client satisfaction index for construction products)
- `metric.base-period-client-satisfaction-index-for-construction-products` (base-period Client satisfaction index for construction products)

Placements:

- organizational / industries / Construction / General (sS7271, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Clients satisfaction index for construction services

- id: `kpi.construction.clients-satisfaction-index-for-construction-services`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Clients satisfaction index for construction services measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Clients satisfaction index for construction services, B is whole named by Clients satisfaction index for construction services. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Clients satisfaction index for construction services on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-clients-satisfaction-index-for-construction-services` (part named by Clients satisfaction index for construction services)
- `metric.whole-named-by-clients-satisfaction-index-for-construction-services` (whole named by Clients satisfaction index for construction services)

Placements:

- organizational / industries / Construction / General (sS7272, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Defects on handover

- id: `kpi.construction.defects-on-handover`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Defects on handover measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Defects on handover, B is whole named by Defects on handover. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Defects on handover on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-defects-on-handover` (part named by Defects on handover)
- `metric.whole-named-by-defects-on-handover` (whole named by Defects on handover)

Placements:

- organizational / industries / Construction / General (sS7273, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Safety accidents

- id: `kpi.construction.safety-accidents`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.construction.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Safety accidents measures that result inside Construction, subcategory General. The unit is count. The formula is A, where A is Safety accidents. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Safety accidents on the desired side of its target for this period?

Inputs:

- `metric.safety-accidents` (Safety accidents)

Placements:

- organizational / industries / Construction / General (sS7274, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Predictability of construction cost

- id: `kpi.construction.predictability-of-construction-cost`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Predictability of construction cost measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Predictability, B is construction cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Predictability of construction cost on the desired side of its target for this period?

Inputs:

- `metric.predictability` (Predictability)
- `metric.construction-cost` (construction cost)

Placements:

- organizational / industries / Construction / General (sS7275, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Predictability of construction time

- id: `kpi.construction.predictability-of-construction-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.construction.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Predictability of construction time measures that result inside Construction, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Predictability, B is construction time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Predictability of construction time on the desired side of its target for this period?

Inputs:

- `metric.predictability` (Predictability)
- `metric.construction-time` (construction time)

Placements:

- organizational / industries / Construction / General (sS7276, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
