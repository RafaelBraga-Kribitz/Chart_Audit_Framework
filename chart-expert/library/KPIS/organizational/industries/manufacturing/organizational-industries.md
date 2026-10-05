# Manufacturing / Organizational » Industries

Context: organizational. Group: industries. KPIs: 42.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Schedule cycle variances

- id: `kpi.management.schedule-cycle-variances`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: strategic
- formula: `A - B`
- formula type: difference
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Schedule cycle variances measures that result inside Management, subcategory Production. The unit is currency. The formula is A - B, where A is actual Schedule cycle variances, B is reference Schedule cycle variances. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Schedule cycle variances on the desired side of its target for this period?

Inputs:

- `metric.actual-schedule-cycle-variances` (actual Schedule cycle variances)
- `metric.reference-schedule-cycle-variances` (reference Schedule cycle variances)

Placements:

- organizational / functional / Management / Production (sK1611, page_0047)
- organizational / industries / Manufacturing / Organizational » Industries (3E22050, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Preventive maintenance

- id: `kpi.manufacturing.preventive-maintenance`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Preventive maintenance measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Preventive maintenance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Preventive maintenance on the desired side of its target for this period?

Inputs:

- `metric.preventive-maintenance` (Preventive maintenance)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22034, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Faults in organisation

- id: `kpi.manufacturing.faults-in-organisation`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Faults in organisation measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Faults in organisation. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Faults in organisation on the desired side of its target for this period?

Inputs:

- `metric.faults-in-organisation` (Faults in organisation)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22035, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Inventory levels

- id: `kpi.manufacturing.inventory-levels`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Inventory levels measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Inventory levels. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Inventory levels on the desired side of its target for this period?

Inputs:

- `metric.inventory-levels` (Inventory levels)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22036, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fixed management costs

- id: `kpi.manufacturing.fixed-management-costs`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fixed management costs measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Fixed management costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fixed management costs on the desired side of its target for this period?

Inputs:

- `metric.fixed-management-costs` (Fixed management costs)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22037, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cycle times

- id: `kpi.manufacturing.cycle-times`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cycle times measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Cycle times. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cycle times on the desired side of its target for this period?

Inputs:

- `metric.cycle-times` (Cycle times)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22038, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Scrap and rework

- id: `kpi.manufacturing.scrap-and-rework`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Scrap and rework measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Scrap and rework. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Scrap and rework on the desired side of its target for this period?

Inputs:

- `metric.scrap-and-rework` (Scrap and rework)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22039, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Variable management costs

- id: `kpi.manufacturing.variable-management-costs`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Variable management costs measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Variable management costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Variable management costs on the desired side of its target for this period?

Inputs:

- `metric.variable-management-costs` (Variable management costs)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22040, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Profitability of product mix across sites

- id: `kpi.manufacturing.profitability-of-product-mix-across-sites`
- kind: kpi
- unit: count
- direction: corridor
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Profitability of product mix across sites measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Profitability of product mix across sites. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Profitability of product mix across sites on the desired side of its target for this period?

Inputs:

- `metric.profitability-of-product-mix-across-sites` (Profitability of product mix across sites)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22041, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Raw material quality

- id: `kpi.manufacturing.raw-material-quality`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Raw material quality measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Raw material quality. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Raw material quality on the desired side of its target for this period?

Inputs:

- `metric.raw-material-quality` (Raw material quality)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22042, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Finished good quality

- id: `kpi.manufacturing.finished-good-quality`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Finished good quality measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Finished good quality. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Finished good quality on the desired side of its target for this period?

Inputs:

- `metric.finished-good-quality` (Finished good quality)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22043, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Demand variance

- id: `kpi.manufacturing.demand-variance`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A - B`
- formula type: difference
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Demand variance measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A - B, where A is actual Demand variance, B is reference Demand variance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Demand variance on the desired side of its target for this period?

Inputs:

- `metric.actual-demand-variance` (actual Demand variance)
- `metric.reference-demand-variance` (reference Demand variance)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22044, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Management line scheduling visibility

- id: `kpi.manufacturing.management-line-scheduling-visibility`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Management line scheduling visibility measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is percent. The formula is (A / B) * 100, where A is part named by Management line scheduling visibility, B is whole named by Management line scheduling visibility. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Management line scheduling visibility on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-management-line-scheduling-visibility` (part named by Management line scheduling visibility)
- `metric.whole-named-by-management-line-scheduling-visibility` (whole named by Management line scheduling visibility)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22045, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Transportation logistics schedules

- id: `kpi.manufacturing.transportation-logistics-schedules`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Transportation logistics schedules measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Transportation logistics schedules. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Transportation logistics schedules on the desired side of its target for this period?

Inputs:

- `metric.transportation-logistics-schedules` (Transportation logistics schedules)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22046, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Management line capacity visibility

- id: `kpi.manufacturing.management-line-capacity-visibility`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Management line capacity visibility measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is percent. The formula is (A / B) * 100, where A is part named by Management line capacity visibility, B is whole named by Management line capacity visibility. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Management line capacity visibility on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-management-line-capacity-visibility` (part named by Management line capacity visibility)
- `metric.whole-named-by-management-line-capacity-visibility` (whole named by Management line capacity visibility)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22047, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Supplies on-line delivery

- id: `kpi.manufacturing.supplies-on-line-delivery`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Supplies on-line delivery measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Supplies on-line delivery. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Supplies on-line delivery on the desired side of its target for this period?

Inputs:

- `metric.supplies-on-line-delivery` (Supplies on-line delivery)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22048, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Statistical process control

- id: `kpi.manufacturing.statistical-process-control`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Statistical process control measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Statistical process control. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Statistical process control on the desired side of its target for this period?

Inputs:

- `metric.statistical-process-control` (Statistical process control)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22049, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### First pass yield

- id: `kpi.manufacturing.first-pass-yield`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

First pass yield measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is First pass yield. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is First pass yield on the desired side of its target for this period?

Inputs:

- `metric.first-pass-yield` (First pass yield)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22051, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Variability of cycle times

- id: `kpi.manufacturing.variability-of-cycle-times`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Variability of cycle times measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Variability of cycle times. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Variability of cycle times on the desired side of its target for this period?

Inputs:

- `metric.variability-of-cycle-times` (Variability of cycle times)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22052, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Asset availability maintenance

- id: `kpi.manufacturing.asset-availability-maintenance`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Asset availability maintenance measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Asset availability maintenance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Asset availability maintenance on the desired side of its target for this period?

Inputs:

- `metric.asset-availability-maintenance` (Asset availability maintenance)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22053, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Downtime events

- id: `kpi.manufacturing.downtime-events`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Downtime events measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Downtime events. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Downtime events on the desired side of its target for this period?

Inputs:

- `metric.downtime-events` (Downtime events)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22055, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### OEE availability

- id: `kpi.manufacturing.oee-availability`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

OEE availability measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is percent. The formula is (A / B) * 100, where A is part named by OEE availability, B is whole named by OEE availability. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is OEE availability on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-oee-availability` (part named by OEE availability)
- `metric.whole-named-by-oee-availability` (whole named by OEE availability)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (3E22057, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Slow cycles

- id: `kpi.manufacturing.slow-cycles`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Slow cycles measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Slow cycles. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Slow cycles on the desired side of its target for this period?

Inputs:

- `metric.slow-cycles` (Slow cycles)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22058, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### OEE performance

- id: `kpi.manufacturing.oee-performance`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

OEE performance measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is OEE performance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is OEE performance on the desired side of its target for this period?

Inputs:

- `metric.oee-performance` (OEE performance)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22060, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### OEE quality

- id: `kpi.manufacturing.oee-quality`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

OEE quality measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is OEE quality. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is OEE quality on the desired side of its target for this period?

Inputs:

- `metric.oee-quality` (OEE quality)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22063, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Performance to take time

- id: `kpi.manufacturing.performance-to-take-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Performance to take time measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Performance to take time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Performance to take time on the desired side of its target for this period?

Inputs:

- `metric.performance-to-take-time` (Performance to take time)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22066, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Estimated time to completion

- id: `kpi.manufacturing.estimated-time-to-completion`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Estimated time to completion measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Estimated time to completion. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Estimated time to completion on the desired side of its target for this period?

Inputs:

- `metric.estimated-time-to-completion` (Estimated time to completion)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22067, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Run rate

- id: `kpi.manufacturing.run-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Run rate measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is percent. The formula is (A / B) * 100, where A is numerator of Run rate, B is base of Run rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Run rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-run-rate` (numerator of Run rate)
- `metric.base-of-run-rate` (base of Run rate)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22068, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Piece per labor hour

- id: `kpi.manufacturing.piece-per-labor-hour`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Piece per labor hour measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A / B, where A is Piece, B is labor hour. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Piece per labor hour on the desired side of its target for this period?

Inputs:

- `metric.piece` (Piece)
- `metric.labor-hour` (labor hour)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22069, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Effective equipment productivity (EEP)

- id: `kpi.manufacturing.effective-equipment-productivity-eep`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Effective equipment productivity (EEP) measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Effective equipment productivity (EEP). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Effective equipment productivity (EEP) on the desired side of its target for this period?

Inputs:

- `metric.effective-equipment-productivity-eep` (Effective equipment productivity (EEP))

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22070, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Waste of overproduction

- id: `kpi.manufacturing.waste-of-overproduction`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Waste of overproduction measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Waste of overproduction. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Waste of overproduction on the desired side of its target for this period?

Inputs:

- `metric.waste-of-overproduction` (Waste of overproduction)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22072, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Waste of waiting

- id: `kpi.manufacturing.waste-of-waiting`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Waste of waiting measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Waste of waiting. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Waste of waiting on the desired side of its target for this period?

Inputs:

- `metric.waste-of-waiting` (Waste of waiting)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22073, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Waste of inappropriate processing

- id: `kpi.manufacturing.waste-of-inappropriate-processing`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Waste of inappropriate processing measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Waste of inappropriate processing. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Waste of inappropriate processing on the desired side of its target for this period?

Inputs:

- `metric.waste-of-inappropriate-processing` (Waste of inappropriate processing)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22074, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Waste of unnecessary inventory

- id: `kpi.manufacturing.waste-of-unnecessary-inventory`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Waste of unnecessary inventory measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Waste of unnecessary inventory. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Waste of unnecessary inventory on the desired side of its target for this period?

Inputs:

- `metric.waste-of-unnecessary-inventory` (Waste of unnecessary inventory)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22075, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Waste of unnecessary motions

- id: `kpi.manufacturing.waste-of-unnecessary-motions`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Waste of unnecessary motions measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Waste of unnecessary motions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Waste of unnecessary motions on the desired side of its target for this period?

Inputs:

- `metric.waste-of-unnecessary-motions` (Waste of unnecessary motions)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22077, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Waste of defects

- id: `kpi.manufacturing.waste-of-defects`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Waste of defects measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Waste of defects. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Waste of defects on the desired side of its target for this period?

Inputs:

- `metric.waste-of-defects` (Waste of defects)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22078, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Waste of not utilising everyone's talents

- id: `kpi.manufacturing.waste-of-not-utilising-everyone-s-talents`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Waste of not utilising everyone's talents measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Waste of not utilising everyone's talents. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Waste of not utilising everyone's talents on the desired side of its target for this period?

Inputs:

- `metric.waste-of-not-utilising-everyone-s-talents` (Waste of not utilising everyone's talents)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22079, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Working time lost by the employee

- id: `kpi.manufacturing.working-time-lost-by-the-employee`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Working time lost by the employee measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Working time lost by the employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Working time lost by the employee on the desired side of its target for this period?

Inputs:

- `metric.working-time-lost-by-the-employee` (Working time lost by the employee)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22080, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time lost indirectly to the issued injury

- id: `kpi.manufacturing.time-lost-indirectly-to-the-issued-injury`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time lost indirectly to the issued injury measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Time lost indirectly to the issued injury. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time lost indirectly to the issued injury on the desired side of its target for this period?

Inputs:

- `metric.time-lost-indirectly-to-the-issued-injury` (Time lost indirectly to the issued injury)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22081, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time lost to determine the cause of the accident

- id: `kpi.manufacturing.time-lost-to-determine-the-cause-of-the-accident`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time lost to determine the cause of the accident measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Time lost to determine the cause of the accident. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time lost to determine the cause of the accident on the desired side of its target for this period?

Inputs:

- `metric.time-lost-to-determine-the-cause-of-the-accident` (Time lost to determine the cause of the accident)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22082, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of interrupting the process and of equipment repaying or safety modifications

- id: `kpi.manufacturing.cost-of-interrupting-the-process-and-of-equipment-repaying-or-safety-mod`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of interrupting the process and of equipment repaying or safety modifications measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is currency. The formula is A, where A is Cost of interrupting the process and of equipment repaying or safety modifications. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of interrupting the process and of equipment repaying or safety modifications on the desired side of its target for this period?

Inputs:

- `metric.cost-of-interrupting-the-process-and-of-equipment-repaying-or-safety-mod` (Cost of interrupting the process and of equipment repaying or safety modifications)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22083, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Potentially large compensation payments and legal procedures following any pay-outs

- id: `kpi.manufacturing.potentially-large-compensation-payments-and-legal-procedures-following-a`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.manufacturing.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Potentially large compensation payments and legal procedures following any pay-outs measures that result inside Manufacturing, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Potentially large compensation payments and legal procedures following any pay-outs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Potentially large compensation payments and legal procedures following any pay-outs on the desired side of its target for this period?

Inputs:

- `metric.potentially-large-compensation-payments-and-legal-procedures-following-a` (Potentially large compensation payments and legal procedures following any pay-outs)

Placements:

- organizational / industries / Manufacturing / Organizational » Industries (4K22084, page_0143)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
