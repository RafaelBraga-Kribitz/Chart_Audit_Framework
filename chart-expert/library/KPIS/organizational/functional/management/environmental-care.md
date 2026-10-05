# Management / Environmental Care

Context: organizational. Group: functional. KPIs: 24.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Energy consumption

- id: `kpi.management.energy-consumption`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.environmental-care`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Energy consumption measures that result inside Management, subcategory Environmental Care. The unit is count. The formula is A, where A is Energy consumption. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Energy consumption on the desired side of its target for this period?

Inputs:

- `metric.energy-consumption` (Energy consumption)

Placements:

- organizational / functional / Management / Environmental Care (sK59, page_0014)
- organizational / industries / Resources / General (x859, page_0107)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Energy produced from renewable sources

- id: `kpi.management.energy-produced-from-renewable-sources`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.environmental-care`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Energy produced from renewable sources measures that result inside Management, subcategory Environmental Care. The unit is percent. The formula is (A / B) * 100, where A is Energy produced, B is renewable sources. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Energy produced from renewable sources on the desired side of its target for this period?

Inputs:

- `metric.energy-produced` (Energy produced)
- `metric.renewable-sources` (renewable sources)

Placements:

- organizational / functional / Management / Environmental Care (sK61, page_0014)
- organizational / industries / Resources / Sustainability/Green Energy (kS61, page_0172)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Paper documents to electronic format ratio

- id: `kpi.management.paper-documents-to-electronic-format-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.environmental-care`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Paper documents to electronic format ratio measures that result inside Management, subcategory Environmental Care. The unit is count. The formula is A, where A is Paper documents to electronic format ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Paper documents to electronic format ratio on the desired side of its target for this period?

Inputs:

- `metric.paper-documents-to-electronic-format-ratio` (Paper documents to electronic format ratio)

Placements:

- organizational / functional / Management / Environmental Care (sK113, page_0014)
- organizational / functional / Knowledge and Innovation / Innovation (#K111, page_0036)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

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

### Penalties resulting from environmental non-compliance

- id: `kpi.management.penalties-resulting-from-environmental-non-compliance`
- kind: kri
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.environmental-care`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Penalties resulting from environmental non-compliance measures that result inside Management, subcategory Environmental Care. The unit is currency. The formula is A, where A is Penalties resulting from environmental non-compliance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Penalties resulting from environmental non-compliance on the desired side of its target for this period?

Inputs:

- `metric.penalties-resulting-from-environmental-non-compliance` (Penalties resulting from environmental non-compliance)

Placements:

- organizational / functional / Management / Environmental Care (sK183, page_0014)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Water consumption per capita per day

- id: `kpi.management.water-consumption-per-capita-per-day`
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

Water consumption per capita per day measures that result inside Management, subcategory Environmental Care. The unit is count. The formula is A / B, where A is Water consumption, B is capita per day. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Water consumption per capita per day on the desired side of its target for this period?

Inputs:

- `metric.water-consumption` (Water consumption)
- `metric.capita-per-day` (capita per day)

Placements:

- organizational / functional / Management / Environmental Care (sK184, page_0014)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Carbon dioxide emissions per capita

- id: `kpi.management.carbon-dioxide-emissions-per-capita`
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

Carbon dioxide emissions per capita measures that result inside Management, subcategory Environmental Care. The unit is count. The formula is A / B, where A is Carbon dioxide emissions, B is capita. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Carbon dioxide emissions per capita on the desired side of its target for this period?

Inputs:

- `metric.carbon-dioxide-emissions` (Carbon dioxide emissions)
- `metric.capita` (capita)

Placements:

- organizational / functional / Management / Environmental Care (sK186, page_0014)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Energy used from renewable sources

- id: `kpi.management.energy-used-from-renewable-sources`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.environmental-care`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Energy used from renewable sources measures that result inside Management, subcategory Environmental Care. The unit is percent. The formula is (A / B) * 100, where A is Energy used, B is renewable sources. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Energy used from renewable sources on the desired side of its target for this period?

Inputs:

- `metric.energy-used` (Energy used)
- `metric.renewable-sources` (renewable sources)

Placements:

- organizational / functional / Management / Environmental Care (sK436, page_0014)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Recycled paper used per employee

- id: `kpi.management.recycled-paper-used-per-employee`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.environmental-care`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Recycled paper used per employee measures that result inside Management, subcategory Environmental Care. The unit is count. The formula is A / B, where A is Recycled paper used, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Recycled paper used per employee on the desired side of its target for this period?

Inputs:

- `metric.recycled-paper-used` (Recycled paper used)
- `metric.employee` (employee)

Placements:

- organizational / functional / Management / Environmental Care (sK574, page_0014)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Paper pages used per employee

- id: `kpi.management.paper-pages-used-per-employee`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.environmental-care`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Paper pages used per employee measures that result inside Management, subcategory Environmental Care. The unit is count. The formula is A / B, where A is Paper pages used, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Paper pages used per employee on the desired side of its target for this period?

Inputs:

- `metric.paper-pages-used` (Paper pages used)
- `metric.employee` (employee)

Placements:

- organizational / functional / Management / Environmental Care (sK77, page_0014)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Landfill volume in use

- id: `kpi.management.landfill-volume-in-use`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.environmental-care`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Landfill volume in use measures that result inside Management, subcategory Environmental Care. The unit is percent. The formula is (A / B) * 100, where A is part named by Landfill volume in use, B is whole named by Landfill volume in use. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Landfill volume in use on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-landfill-volume-in-use` (part named by Landfill volume in use)
- `metric.whole-named-by-landfill-volume-in-use` (whole named by Landfill volume in use)

Placements:

- organizational / functional / Management / Environmental Care (sK577, page_0014)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Volume of recycled waste

- id: `kpi.management.volume-of-recycled-waste`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.environmental-care`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Volume of recycled waste measures that result inside Management, subcategory Environmental Care. The unit is count. The formula is A, where A is Volume of recycled waste. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Volume of recycled waste on the desired side of its target for this period?

Inputs:

- `metric.volume-of-recycled-waste` (Volume of recycled waste)

Placements:

- organizational / functional / Management / Environmental Care (sK578, page_0014)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Consumption of recycled paper

- id: `kpi.management.consumption-of-recycled-paper`
- kind: kpi
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

Consumption of recycled paper measures that result inside Management, subcategory Environmental Care. The unit is percent. The formula is (A / B) * 100, where A is Consumption, B is recycled paper. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Consumption of recycled paper on the desired side of its target for this period?

Inputs:

- `metric.consumption` (Consumption)
- `metric.recycled-paper` (recycled paper)

Placements:

- organizational / functional / Management / Environmental Care (sK587, page_0014)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Initiatives to promote greater governmental responsibility

- id: `kpi.management.initiatives-to-promote-greater-governmental-responsibility`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.environmental-care`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Initiatives to promote greater governmental responsibility measures that result inside Management, subcategory Environmental Care. The unit is count. The formula is A, where A is Initiatives to promote greater governmental responsibility. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Initiatives to promote greater governmental responsibility on the desired side of its target for this period?

Inputs:

- `metric.initiatives-to-promote-greater-governmental-responsibility` (Initiatives to promote greater governmental responsibility)

Placements:

- organizational / functional / Management / Environmental Care (sK590, page_0014)

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

### Aircraft emissions

- id: `kpi.management.aircraft-emissions`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.environmental-care`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Aircraft emissions measures that result inside Management, subcategory Environmental Care. The unit is count. The formula is A, where A is Aircraft emissions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Aircraft emissions on the desired side of its target for this period?

Inputs:

- `metric.aircraft-emissions` (Aircraft emissions)

Placements:

- organizational / functional / Management / Environmental Care (sK592, page_0014)
- organizational / industries / Transportation / Airlines (sK259, page_0181)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Recycled hazardous operational waste

- id: `kpi.management.recycled-hazardous-operational-waste`
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

Recycled hazardous operational waste measures that result inside Management, subcategory Environmental Care. The unit is percent. The formula is (A / B) * 100, where A is numerator of Recycled hazardous operational waste, B is base of Recycled hazardous operational waste. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Recycled hazardous operational waste on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-recycled-hazardous-operational-waste` (numerator of Recycled hazardous operational waste)
- `metric.base-of-recycled-hazardous-operational-waste` (base of Recycled hazardous operational waste)

Placements:

- organizational / functional / Management / Environmental Care (sK593, page_0014)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Wastewater

- id: `kpi.management.wastewater`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.environmental-care`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Wastewater measures that result inside Management, subcategory Environmental Care. The unit is count. The formula is A, where A is Wastewater. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Wastewater on the desired side of its target for this period?

Inputs:

- `metric.wastewater` (Wastewater)

Placements:

- organizational / functional / Management / Environmental Care (sK594, page_0014)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Biodegradable carrier bags

- id: `kpi.management.biodegradable-carrier-bags`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.environmental-care`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Biodegradable carrier bags measures that result inside Management, subcategory Environmental Care. The unit is percent. The formula is (A / B) * 100, where A is part named by Biodegradable carrier bags, B is whole named by Biodegradable carrier bags. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Biodegradable carrier bags on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-biodegradable-carrier-bags` (part named by Biodegradable carrier bags)
- `metric.whole-named-by-biodegradable-carrier-bags` (whole named by Biodegradable carrier bags)

Placements:

- organizational / functional / Management / Environmental Care (sK595, page_0014)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Paper reduction

- id: `kpi.management.paper-reduction`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.environmental-care`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Paper reduction measures that result inside Management, subcategory Environmental Care. The unit is percent. The formula is (A / B) * 100, where A is part named by Paper reduction, B is whole named by Paper reduction. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Paper reduction on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-paper-reduction` (part named by Paper reduction)
- `metric.whole-named-by-paper-reduction` (whole named by Paper reduction)

Placements:

- organizational / functional / Management / Environmental Care (sK796, page_0014)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Reduced paper consumption due to duplicating

- id: `kpi.management.reduced-paper-consumption-due-to-duplicating`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.environmental-care`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Reduced paper consumption due to duplicating measures that result inside Management, subcategory Environmental Care. The unit is percent. The formula is (A / B) * 100, where A is Reduced paper consumption due, B is duplicating. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Reduced paper consumption due to duplicating on the desired side of its target for this period?

Inputs:

- `metric.reduced-paper-consumption-due` (Reduced paper consumption due)
- `metric.duplicating` (duplicating)

Placements:

- organizational / functional / Management / Environmental Care (sK787, page_0014)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Entries to environment / community awards

- id: `kpi.management.entries-to-environment-community-awards`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.environmental-care`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Entries to environment / community awards measures that result inside Management, subcategory Environmental Care. The unit is count. The formula is A, where A is Entries to environment / community awards. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Entries to environment / community awards on the desired side of its target for this period?

Inputs:

- `metric.entries-to-environment-community-awards` (Entries to environment / community awards)

Placements:

- organizational / functional / Management / Environmental Care (sK1382, page_0014)
- organizational / functional / Management / Public Relations (sK1382, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Marketing projects that are environmentally friendly

- id: `kpi.management.marketing-projects-that-are-environmentally-friendly`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.environmental-care`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Marketing projects that are environmentally friendly measures that result inside Management, subcategory Environmental Care. The unit is percent. The formula is (A / B) * 100, where A is part named by Marketing projects that are environmentally friendly, B is whole named by Marketing projects that are environmentally friendly. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Marketing projects that are environmentally friendly on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-marketing-projects-that-are-environmentally-friendly` (part named by Marketing projects that are environmentally friendly)
- `metric.whole-named-by-marketing-projects-that-are-environmentally-friendly` (whole named by Marketing projects that are environmentally friendly)

Placements:

- organizational / functional / Management / Environmental Care (sK1389, page_0014)
- organizational / functional / Management / Public Relations (sK1389, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Accidental releases of substances

- id: `kpi.management.accidental-releases-of-substances`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.environmental-care`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Accidental releases of substances measures that result inside Management, subcategory Environmental Care. The unit is count. The formula is A, where A is Accidental releases of substances. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Accidental releases of substances on the desired side of its target for this period?

Inputs:

- `metric.accidental-releases-of-substances` (Accidental releases of substances)

Placements:

- organizational / functional / Management / Environmental Care (sK1480, page_0014)
- organizational / industries / Sport / Organizational » Industries (sK1381, page_0197)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
