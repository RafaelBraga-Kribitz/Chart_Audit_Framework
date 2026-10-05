# Management / Production

Context: organizational. Group: functional. KPIs: 60.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Energy used per unit of production

- id: `kpi.management.energy-used-per-unit-of-production`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.environmental-care`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Energy used per unit of production measures that result inside Management, subcategory Environmental Care. The unit is count. The formula is A / B, where A is Energy used, B is unit of production. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Energy used per unit of production on the desired side of its target for this period?

Inputs:

- `metric.energy-used` (Energy used)
- `metric.unit-of-production` (unit of production)

Placements:

- organizational / functional / Management / Environmental Care (sK182, page_0014)
- organizational / functional / Management / Production (sK182, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hazardous operational waste

- id: `kpi.management.hazardous-operational-waste`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.environmental-care`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Hazardous operational waste measures that result inside Management, subcategory Environmental Care. The unit is percent. The formula is (A / B) * 100, where A is numerator of Hazardous operational waste, B is base of Hazardous operational waste. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hazardous operational waste on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-hazardous-operational-waste` (numerator of Hazardous operational waste)
- `metric.base-of-hazardous-operational-waste` (base of Hazardous operational waste)

Placements:

- organizational / functional / Management / Environmental Care (sK591, page_0014)
- organizational / functional / Management / Production (sK591, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### * Unit production time

- id: `kpi.management.unit-production-time`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

* Unit production time measures that result inside Management, subcategory Production. The unit is number. The formula is A, where A is * Unit production time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is * Unit production time on the desired side of its target for this period?

Inputs:

- `metric.unit-production-time` (* Unit production time)

Placements:

- organizational / functional / Management / Production (sK84, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### § Energy cost per unit of production

- id: `kpi.management.energy-cost-per-unit-of-production`
- kind: kpi
- unit: number
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

§ Energy cost per unit of production measures that result inside Management, subcategory Production. The unit is number. The formula is A / B, where A is § Energy cost, B is unit of production. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § Energy cost per unit of production on the desired side of its target for this period?

Inputs:

- `metric.energy-cost` (§ Energy cost)
- `metric.unit-of-production` (unit of production)

Placements:

- organizational / functional / Management / Production (sK181, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### § Fixed production overhead volume capacity variance

- id: `kpi.management.fixed-production-overhead-volume-capacity-variance`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: strategic
- formula: `A - B`
- formula type: difference
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

§ Fixed production overhead volume capacity variance measures that result inside Management, subcategory Production. The unit is number. The formula is A - B, where A is actual § Fixed production overhead volume capacity variance, B is reference § Fixed production overhead volume capacity variance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § Fixed production overhead volume capacity variance on the desired side of its target for this period?

Inputs:

- `metric.actual-fixed-production-overhead-volume-capacity-variance` (actual § Fixed production overhead volume capacity variance)
- `metric.reference-fixed-production-overhead-volume-capacity-variance` (reference § Fixed production overhead volume capacity variance)

Placements:

- organizational / functional / Management / Production (sK335, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### § Units per man-hour

- id: `kpi.management.units-per-man-hour`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

§ Units per man-hour measures that result inside Management, subcategory Production. The unit is number. The formula is A / B, where A is § Units, B is man-hour. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § Units per man-hour on the desired side of its target for this period?

Inputs:

- `metric.units` (§ Units)
- `metric.man-hour` (man-hour)

Placements:

- organizational / functional / Management / Production (sK443, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### § Time yield

- id: `kpi.management.time-yield`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

§ Time yield measures that result inside Management, subcategory Production. The unit is number. The formula is A, where A is § Time yield. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § Time yield on the desired side of its target for this period?

Inputs:

- `metric.time-yield` (§ Time yield)

Placements:

- organizational / functional / Management / Production (sK497, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Piece variance

- id: `kpi.management.piece-variance`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A - B`
- formula type: difference
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Piece variance measures that result inside Management, subcategory Production. The unit is count. The formula is A - B, where A is actual Piece variance, B is reference Piece variance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Piece variance on the desired side of its target for this period?

Inputs:

- `metric.actual-piece-variance` (actual Piece variance)
- `metric.reference-piece-variance` (reference Piece variance)

Placements:

- organizational / functional / Management / Production (sK502, page_0047)
- organizational / functional / Management / General (xK503, page_0053)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Average cycle time (ACT)

- id: `kpi.management.average-cycle-time-act`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: average
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Average cycle time (ACT) measures that result inside Management, subcategory Production. The unit is count. The formula is A / B, where A is sum underlying Average cycle time (ACT), B is count of observations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Average cycle time (ACT) on the desired side of its target for this period?

Inputs:

- `metric.sum-underlying-average-cycle-time-act` (sum underlying Average cycle time (ACT))
- `metric.count-of-observations` (count of observations)

Placements:

- organizational / functional / Management / Production (sK504, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Tak time

- id: `kpi.management.tak-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Tak time measures that result inside Management, subcategory Production. The unit is count. The formula is A, where A is Tak time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Tak time on the desired side of its target for this period?

Inputs:

- `metric.tak-time` (Tak time)

Placements:

- organizational / functional / Management / Production (sK505, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Startup rejects

- id: `kpi.management.startup-rejects`
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

Startup rejects measures that result inside Management, subcategory Production. The unit is count. The formula is A, where A is Startup rejects. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Startup rejects on the desired side of its target for this period?

Inputs:

- `metric.startup-rejects` (Startup rejects)

Placements:

- organizational / functional / Management / Production (sK507, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production rejects

- id: `kpi.management.production-rejects`
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

Production rejects measures that result inside Management, subcategory Production. The unit is count. The formula is A, where A is Production rejects. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production rejects on the desired side of its target for this period?

Inputs:

- `metric.production-rejects` (Production rejects)

Placements:

- organizational / functional / Management / Production (sK509, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production losses

- id: `kpi.management.production-losses`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Production losses measures that result inside Management, subcategory Production. The unit is percent. The formula is (A / B) * 100, where A is part named by Production losses, B is whole named by Production losses. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production losses on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-production-losses` (part named by Production losses)
- `metric.whole-named-by-production-losses` (whole named by Production losses)

Placements:

- organizational / functional / Management / Production (sK521, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production lead time

- id: `kpi.management.production-lead-time`
- kind: kpi
- unit: count
- direction: down
- timing: leading
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Production lead time measures that result inside Management, subcategory Production. The unit is count. The formula is A, where A is Production lead time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production lead time on the desired side of its target for this period?

Inputs:

- `metric.production-lead-time` (Production lead time)

Placements:

- organizational / functional / Management / Production (sK522, page_0047)

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

### Slow servoing stock

- id: `kpi.management.slow-servoing-stock`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Slow servoing stock measures that result inside Management, subcategory Production. The unit is percent. The formula is (A / B) * 100, where A is part named by Slow servoing stock, B is whole named by Slow servoing stock. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Slow servoing stock on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-slow-servoing-stock` (part named by Slow servoing stock)
- `metric.whole-named-by-slow-servoing-stock` (whole named by Slow servoing stock)

Placements:

- organizational / functional / Management / Production (sK651, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Boomerang return rate

- id: `kpi.management.boomerang-return-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Boomerang return rate measures that result inside Management, subcategory Production. The unit is percent. The formula is (A / B) * 100, where A is numerator of Boomerang return rate, B is base of Boomerang return rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Boomerang return rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-boomerang-return-rate` (numerator of Boomerang return rate)
- `metric.base-of-boomerang-return-rate` (base of Boomerang return rate)

Placements:

- organizational / functional / Management / Production (sK797, page_0047)
- organizational / functional / Management / Organizational » Functional Areas (sK707, page_0055)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Residual value

- id: `kpi.management.residual-value`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Residual value measures that result inside Management, subcategory Production. The unit is percent. The formula is (A / B) * 100, where A is part named by Residual value, B is whole named by Residual value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Residual value on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-residual-value` (part named by Residual value)
- `metric.whole-named-by-residual-value` (whole named by Residual value)

Placements:

- organizational / functional / Management / Production (sK754, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fired production overhead total variance

- id: `kpi.management.fired-production-overhead-total-variance`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A - B`
- formula type: difference
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fired production overhead total variance measures that result inside Management, subcategory Production. The unit is currency. The formula is A - B, where A is actual Fired production overhead total variance, B is reference Fired production overhead total variance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fired production overhead total variance on the desired side of its target for this period?

Inputs:

- `metric.actual-fired-production-overhead-total-variance` (actual Fired production overhead total variance)
- `metric.reference-fired-production-overhead-total-variance` (reference Fired production overhead total variance)

Placements:

- organizational / functional / Management / Production (sK1597, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Emissions from production

- id: `kpi.management.emissions-from-production`
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

Emissions from production measures that result inside Management, subcategory Production. The unit is count. The formula is A, where A is Emissions from production. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Emissions from production on the desired side of its target for this period?

Inputs:

- `metric.emissions-from-production` (Emissions from production)

Placements:

- organizational / functional / Management / Production (sK1600, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Direct labor efficiency variance

- id: `kpi.management.direct-labor-efficiency-variance`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A - B`
- formula type: difference
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Direct labor efficiency variance measures that result inside Management, subcategory Production. The unit is currency. The formula is A - B, where A is actual Direct labor efficiency variance, B is reference Direct labor efficiency variance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Direct labor efficiency variance on the desired side of its target for this period?

Inputs:

- `metric.actual-direct-labor-efficiency-variance` (actual Direct labor efficiency variance)
- `metric.reference-direct-labor-efficiency-variance` (reference Direct labor efficiency variance)

Placements:

- organizational / functional / Management / Production (sK1601, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production delays due to raw material shortage

- id: `kpi.management.production-delays-due-to-raw-material-shortage`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Production delays due to raw material shortage measures that result inside Management, subcategory Production. The unit is percent. The formula is (A / B) * 100, where A is Production delays due, B is raw material shortage. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production delays due to raw material shortage on the desired side of its target for this period?

Inputs:

- `metric.production-delays-due` (Production delays due)
- `metric.raw-material-shortage` (raw material shortage)

Placements:

- organizational / functional / Management / Production (sK1603, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production uptime

- id: `kpi.management.production-uptime`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Production uptime measures that result inside Management, subcategory Production. The unit is percent. The formula is (A / B) * 100, where A is part named by Production uptime, B is whole named by Production uptime. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production uptime on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-production-uptime` (part named by Production uptime)
- `metric.whole-named-by-production-uptime` (whole named by Production uptime)

Placements:

- organizational / functional / Management / Production (sK1604, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Work in progress days

- id: `kpi.management.work-in-progress-days`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Work in progress days measures that result inside Management, subcategory Production. The unit is percent. The formula is (A / B) * 100, where A is part named by Work in progress days, B is whole named by Work in progress days. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Work in progress days on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-work-in-progress-days` (part named by Work in progress days)
- `metric.whole-named-by-work-in-progress-days` (whole named by Work in progress days)

Placements:

- organizational / functional / Management / Production (sK1605, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unplanned maintenance

- id: `kpi.management.unplanned-maintenance`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Unplanned maintenance measures that result inside Management, subcategory Production. The unit is percent. The formula is (A / B) * 100, where A is part named by Unplanned maintenance, B is whole named by Unplanned maintenance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unplanned maintenance on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-unplanned-maintenance` (part named by Unplanned maintenance)
- `metric.whole-named-by-unplanned-maintenance` (whole named by Unplanned maintenance)

Placements:

- organizational / functional / Management / Production (sK1606, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Value of finished products

- id: `kpi.management.value-of-finished-products`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Value of finished products measures that result inside Management, subcategory Production. The unit is percent. The formula is (A / B) * 100, where A is Value, B is finished products. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Value of finished products on the desired side of its target for this period?

Inputs:

- `metric.value` (Value)
- `metric.finished-products` (finished products)

Placements:

- organizational / functional / Management / Production (sK1608, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Value of work in progress

- id: `kpi.management.value-of-work-in-progress`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Value of work in progress measures that result inside Management, subcategory Production. The unit is percent. The formula is (A / B) * 100, where A is Value, B is work in progress. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Value of work in progress on the desired side of its target for this period?

Inputs:

- `metric.value` (Value)
- `metric.work-in-progress` (work in progress)

Placements:

- organizational / functional / Management / Production (sK1609, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Material cost per product

- id: `kpi.management.material-cost-per-product`
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

Material cost per product measures that result inside Management, subcategory Production. The unit is currency. The formula is A / B, where A is Material cost, B is product. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Material cost per product on the desired side of its target for this period?

Inputs:

- `metric.material-cost` (Material cost)
- `metric.product` (product)

Placements:

- organizational / functional / Management / Production (sK1610, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

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

### Labor cost per unit production

- id: `kpi.management.labor-cost-per-unit-production`
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

Labor cost per unit production measures that result inside Management, subcategory Production. The unit is currency. The formula is A / B, where A is Labor cost, B is unit production. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Labor cost per unit production on the desired side of its target for this period?

Inputs:

- `metric.labor-cost` (Labor cost)
- `metric.unit-production` (unit production)

Placements:

- organizational / functional / Management / Production (sK1614, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Small tasks

- id: `kpi.management.small-tasks`
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

Small tasks measures that result inside Management, subcategory Production. The unit is count. The formula is A, where A is Small tasks. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Small tasks on the desired side of its target for this period?

Inputs:

- `metric.small-tasks` (Small tasks)

Placements:

- organizational / functional / Management / Production (sK1615, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production volume

- id: `kpi.management.production-volume`
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

Production volume measures that result inside Management, subcategory Production. The unit is count. The formula is A, where A is Production volume. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production volume on the desired side of its target for this period?

Inputs:

- `metric.production-volume` (Production volume)

Placements:

- organizational / functional / Management / Production (sK1617, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Idle time

- id: `kpi.management.idle-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Idle time measures that result inside Management, subcategory Production. The unit is percent. The formula is (A / B) * 100, where A is part named by Idle time, B is whole named by Idle time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Idle time on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-idle-time` (part named by Idle time)
- `metric.whole-named-by-idle-time` (whole named by Idle time)

Placements:

- organizational / functional / Management / Production (sK1620, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Material consumption per product

- id: `kpi.management.material-consumption-per-product`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Material consumption per product measures that result inside Management, subcategory Production. The unit is count. The formula is A / B, where A is Material consumption, B is product. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Material consumption per product on the desired side of its target for this period?

Inputs:

- `metric.material-consumption` (Material consumption)
- `metric.product` (product)

Placements:

- organizational / functional / Management / Production (sK1621, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production orders finished late

- id: `kpi.management.production-orders-finished-late`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Production orders finished late measures that result inside Management, subcategory Production. The unit is percent. The formula is (A / B) * 100, where A is part named by Production orders finished late, B is whole named by Production orders finished late. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production orders finished late on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-production-orders-finished-late` (part named by Production orders finished late)
- `metric.whole-named-by-production-orders-finished-late` (whole named by Production orders finished late)

Placements:

- organizational / functional / Management / Production (sK1623, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production orders shipped ahead time

- id: `kpi.management.production-orders-shipped-ahead-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Production orders shipped ahead time measures that result inside Management, subcategory Production. The unit is percent. The formula is (A / B) * 100, where A is part named by Production orders shipped ahead time, B is whole named by Production orders shipped ahead time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production orders shipped ahead time on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-production-orders-shipped-ahead-time` (part named by Production orders shipped ahead time)
- `metric.whole-named-by-production-orders-shipped-ahead-time` (whole named by Production orders shipped ahead time)

Placements:

- organizational / functional / Management / Production (sK1624, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production schedule adherence

- id: `kpi.management.production-schedule-adherence`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Production schedule adherence measures that result inside Management, subcategory Production. The unit is percent. The formula is (A / B) * 100, where A is part named by Production schedule adherence, B is whole named by Production schedule adherence. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production schedule adherence on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-production-schedule-adherence` (part named by Production schedule adherence)
- `metric.whole-named-by-production-schedule-adherence` (whole named by Production schedule adherence)

Placements:

- organizational / functional / Management / Production (sK1627, page_0047)

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

### Actual to projected unit production costs

- id: `kpi.management.actual-to-projected-unit-production-costs`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Actual to projected unit production costs measures that result inside Management, subcategory Production. The unit is count. The formula is A, where A is Actual to projected unit production costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Actual to projected unit production costs on the desired side of its target for this period?

Inputs:

- `metric.actual-to-projected-unit-production-costs` (Actual to projected unit production costs)

Placements:

- organizational / functional / Management / Production (sK1629, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Machine utilisation in production

- id: `kpi.management.machine-utilisation-in-production`
- kind: kpi
- unit: percent
- direction: corridor
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.production`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Machine utilisation in production measures that result inside Management, subcategory Production. The unit is percent. The formula is (A / B) * 100, where A is part named by Machine utilisation in production, B is whole named by Machine utilisation in production. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Machine utilisation in production on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-machine-utilisation-in-production` (part named by Machine utilisation in production)
- `metric.whole-named-by-machine-utilisation-in-production` (whole named by Machine utilisation in production)

Placements:

- organizational / functional / Management / Production (sK1631, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Product line extensions

- id: `kpi.management.product-line-extensions`
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

Product line extensions measures that result inside Management, subcategory Production. The unit is count. The formula is A, where A is Product line extensions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Product line extensions on the desired side of its target for this period?

Inputs:

- `metric.product-line-extensions` (Product line extensions)

Placements:

- organizational / functional / Management / Production (sK1633, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production lot size

- id: `kpi.management.production-lot-size`
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

Production lot size measures that result inside Management, subcategory Production. The unit is count. The formula is A, where A is Production lot size. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production lot size on the desired side of its target for this period?

Inputs:

- `metric.production-lot-size` (Production lot size)

Placements:

- organizational / functional / Management / Production (sK1634, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Manufacturing process steps

- id: `kpi.management.manufacturing-process-steps`
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

Manufacturing process steps measures that result inside Management, subcategory Production. The unit is count. The formula is A, where A is Manufacturing process steps. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Manufacturing process steps on the desired side of its target for this period?

Inputs:

- `metric.manufacturing-process-steps` (Manufacturing process steps)

Placements:

- organizational / functional / Management / Production (sK1636, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Work in progress

- id: `kpi.management.work-in-progress`
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

Work in progress measures that result inside Management, subcategory Production. The unit is count. The formula is A, where A is Work in progress. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Work in progress on the desired side of its target for this period?

Inputs:

- `metric.work-in-progress` (Work in progress)

Placements:

- organizational / functional / Management / Production (sK1637, page_0047)
- organizational / industries / Accounting / Organizational + Industries (sK19869, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Variable overhead expenditure variance

- id: `kpi.management.variable-overhead-expenditure-variance`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A - B`
- formula type: difference
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Variable overhead expenditure variance measures that result inside Management, subcategory Production. The unit is currency. The formula is A - B, where A is actual Variable overhead expenditure variance, B is reference Variable overhead expenditure variance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Variable overhead expenditure variance on the desired side of its target for this period?

Inputs:

- `metric.actual-variable-overhead-expenditure-variance` (actual Variable overhead expenditure variance)
- `metric.reference-variable-overhead-expenditure-variance` (reference Variable overhead expenditure variance)

Placements:

- organizational / functional / Management / Production (sK1639, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Floor space utilized

- id: `kpi.management.floor-space-utilized`
- kind: kpi
- unit: currency
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

Floor space utilized measures that result inside Management, subcategory Production. The unit is currency. The formula is A, where A is Floor space utilized. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Floor space utilized on the desired side of its target for this period?

Inputs:

- `metric.floor-space-utilized` (Floor space utilized)

Placements:

- organizational / functional / Management / Production (sK1640, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fixed production overhead volume efficiency variance

- id: `kpi.management.fixed-production-overhead-volume-efficiency-variance`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A - B`
- formula type: difference
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fixed production overhead volume efficiency variance measures that result inside Management, subcategory Production. The unit is currency. The formula is A - B, where A is actual Fixed production overhead volume efficiency variance, B is reference Fixed production overhead volume efficiency variance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fixed production overhead volume efficiency variance on the desired side of its target for this period?

Inputs:

- `metric.actual-fixed-production-overhead-volume-efficiency-variance` (actual Fixed production overhead volume efficiency variance)
- `metric.reference-fixed-production-overhead-volume-efficiency-variance` (reference Fixed production overhead volume efficiency variance)

Placements:

- organizational / functional / Management / Production (sK1643, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fixed overhead volume variance

- id: `kpi.management.fixed-overhead-volume-variance`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A - B`
- formula type: difference
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fixed overhead volume variance measures that result inside Management, subcategory Production. The unit is currency. The formula is A - B, where A is actual Fixed overhead volume variance, B is reference Fixed overhead volume variance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fixed overhead volume variance on the desired side of its target for this period?

Inputs:

- `metric.actual-fixed-overhead-volume-variance` (actual Fixed overhead volume variance)
- `metric.reference-fixed-overhead-volume-variance` (reference Fixed overhead volume variance)

Placements:

- organizational / functional / Management / Production (sK1644, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production within task time

- id: `kpi.management.production-within-task-time`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Production within task time measures that result inside Management, subcategory Production. The unit is currency. The formula is A, where A is Production within task time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production within task time on the desired side of its target for this period?

Inputs:

- `metric.production-within-task-time` (Production within task time)

Placements:

- organizational / functional / Management / Production (sK1646, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### On time value rate

- id: `kpi.management.on-time-value-rate`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

On time value rate measures that result inside Management, subcategory Production. The unit is currency. The formula is A, where A is On time value rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is On time value rate on the desired side of its target for this period?

Inputs:

- `metric.on-time-value-rate` (On time value rate)

Placements:

- organizational / functional / Management / Production (sK1647, page_0047)
- organizational / industries / Sport / Organization= Industries (sK21128, page_0199)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production processes out of control

- id: `kpi.management.production-processes-out-of-control`
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

Production processes out of control measures that result inside Management, subcategory Production. The unit is count. The formula is A, where A is Production processes out of control. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production processes out of control on the desired side of its target for this period?

Inputs:

- `metric.production-processes-out-of-control` (Production processes out of control)

Placements:

- organizational / functional / Management / Production (sK1658, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Downtime costs

- id: `kpi.management.downtime-costs`
- kind: kri
- unit: currency
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Downtime costs measures that result inside Management, subcategory Production. The unit is currency. The formula is A, where A is Downtime costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Downtime costs on the desired side of its target for this period?

Inputs:

- `metric.downtime-costs` (Downtime costs)

Placements:

- organizational / functional / Management / Production (sK1666, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production downtime per occurrence

- id: `kpi.management.production-downtime-per-occurrence`
- kind: kri
- unit: count
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

Production downtime per occurrence measures that result inside Management, subcategory Production. The unit is count. The formula is A / B, where A is Production downtime, B is occurrence. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production downtime per occurrence on the desired side of its target for this period?

Inputs:

- `metric.production-downtime` (Production downtime)
- `metric.occurrence` (occurrence)

Placements:

- organizational / functional / Management / Production (sK1672, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unplanned downtime in production

- id: `kpi.management.unplanned-downtime-in-production`
- kind: kri
- unit: currency
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Unplanned downtime in production measures that result inside Management, subcategory Production. The unit is currency. The formula is A, where A is Unplanned downtime in production. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unplanned downtime in production on the desired side of its target for this period?

Inputs:

- `metric.unplanned-downtime-in-production` (Unplanned downtime in production)

Placements:

- organizational / functional / Management / Production (sK1675, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production costs

- id: `kpi.management.production-costs`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Production costs measures that result inside Management, subcategory Production. The unit is currency. The formula is A, where A is Production costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production costs on the desired side of its target for this period?

Inputs:

- `metric.production-costs` (Production costs)

Placements:

- organizational / functional / Management / Production (sK1676, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production cost variance

- id: `kpi.management.production-cost-variance`
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

Production cost variance measures that result inside Management, subcategory Production. The unit is currency. The formula is A - B, where A is actual Production cost variance, B is reference Production cost variance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production cost variance on the desired side of its target for this period?

Inputs:

- `metric.actual-production-cost-variance` (actual Production cost variance)
- `metric.reference-production-cost-variance` (reference Production cost variance)

Placements:

- organizational / functional / Management / Production (sK1678, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Direct material total variance

- id: `kpi.management.direct-material-total-variance`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A - B`
- formula type: difference
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Direct material total variance measures that result inside Management, subcategory Production. The unit is currency. The formula is A - B, where A is actual Direct material total variance, B is reference Direct material total variance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Direct material total variance on the desired side of its target for this period?

Inputs:

- `metric.actual-direct-material-total-variance` (actual Direct material total variance)
- `metric.reference-direct-material-total-variance` (reference Direct material total variance)

Placements:

- organizational / functional / Management / Production (sK1679, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Direct labor rate variance

- id: `kpi.management.direct-labor-rate-variance`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A - B`
- formula type: difference
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Direct labor rate variance measures that result inside Management, subcategory Production. The unit is currency. The formula is A - B, where A is actual Direct labor rate variance, B is reference Direct labor rate variance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Direct labor rate variance on the desired side of its target for this period?

Inputs:

- `metric.actual-direct-labor-rate-variance` (actual Direct labor rate variance)
- `metric.reference-direct-labor-rate-variance` (reference Direct labor rate variance)

Placements:

- organizational / functional / Management / Production (sK1680, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Direct material usage variance

- id: `kpi.management.direct-material-usage-variance`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A - B`
- formula type: difference
- dashboard: `dash.management.production`
- analysis chart: `bar-chart` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Direct material usage variance measures that result inside Management, subcategory Production. The unit is currency. The formula is A - B, where A is actual Direct material usage variance, B is reference Direct material usage variance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Direct material usage variance on the desired side of its target for this period?

Inputs:

- `metric.actual-direct-material-usage-variance` (actual Direct material usage variance)
- `metric.reference-direct-material-usage-variance` (reference Direct material usage variance)

Placements:

- organizational / functional / Management / Production (sK1681, page_0047)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
