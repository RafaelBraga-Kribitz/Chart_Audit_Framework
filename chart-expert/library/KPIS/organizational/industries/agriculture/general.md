# Agriculture / General

Context: organizational. Group: industries. KPIs: 61.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### ▼ Water quality index

- id: `kpi.management.water-quality-index`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: index
- dashboard: `dash.management.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

▼ Water quality index measures that result inside Management, subcategory Organizational + Functional Areas. The unit is number. The formula is (A / B) * 100, where A is current ▼ Water quality index, B is base-period ▼ Water quality index. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is ▼ Water quality index on the desired side of its target for this period?

Inputs:

- `metric.current-water-quality-index` (current ▼ Water quality index)
- `metric.base-period-water-quality-index` (base-period ▼ Water quality index)

Placements:

- organizational / functional / Management / Organizational + Functional Areas (xK6040, page_0015)
- organizational / industries / Agriculture / General (xS6402, page_0098)
- organizational / industries / Utilities / Organizational » Industries (xBS400, page_0206)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Pesticide regulation compliance

- id: `kpi.agriculture.pesticide-regulation-compliance`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.skpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Pesticide regulation compliance measures that result inside Agriculture, subcategory sKPI # Key Performance Indicator name. The unit is count. The formula is A, where A is Pesticide regulation compliance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Pesticide regulation compliance on the desired side of its target for this period?

Inputs:

- `metric.pesticide-regulation-compliance` (Pesticide regulation compliance)

Placements:

- organizational / industries / Agriculture / sKPI # Key Performance Indicator name (sK6411, page_0058)
- organizational / industries / Agriculture / General (xS6411, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### A area of land cultivated

- id: `kpi.agriculture.a-area-of-land-cultivated`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

A area of land cultivated measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is A area of land cultivated. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is A area of land cultivated on the desired side of its target for this period?

Inputs:

- `metric.a-area-of-land-cultivated` (A area of land cultivated)

Placements:

- organizational / industries / Agriculture / General (x9455, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### F Farm site

- id: `kpi.agriculture.f-farm-site`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

F Farm site measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is F Farm site. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is F Farm site on the desired side of its target for this period?

Inputs:

- `metric.f-farm-site` (F Farm site)

Placements:

- organizational / industries / Agriculture / General (x9457, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Food production per capita

- id: `kpi.agriculture.food-production-per-capita`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Food production per capita measures that result inside Agriculture, subcategory General. The unit is number. The formula is A / B, where A is Food production, B is capita. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Food production per capita on the desired side of its target for this period?

Inputs:

- `metric.food-production` (Food production)
- `metric.capita` (capita)

Placements:

- organizational / industries / Agriculture / General (x9559, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Value of agricultural exports

- id: `kpi.agriculture.value-of-agricultural-exports`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Value of agricultural exports measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is Value of agricultural exports. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Value of agricultural exports on the desired side of its target for this period?

Inputs:

- `metric.value-of-agricultural-exports` (Value of agricultural exports)

Placements:

- organizational / industries / Agriculture / General (x9560, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### T Tractors per hectare

- id: `kpi.agriculture.t-tractors-per-hectare`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

T Tractors per hectare measures that result inside Agriculture, subcategory General. The unit is number. The formula is A / B, where A is T Tractors, B is hectare. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is T Tractors per hectare on the desired side of its target for this period?

Inputs:

- `metric.t-tractors` (T Tractors)
- `metric.hectare` (hectare)

Placements:

- organizational / industries / Agriculture / General (x9569, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Agricultural mechanization level

- id: `kpi.agriculture.agricultural-mechanization-level`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Agricultural mechanization level measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is Agricultural mechanization level. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Agricultural mechanization level on the desired side of its target for this period?

Inputs:

- `metric.agricultural-mechanization-level` (Agricultural mechanization level)

Placements:

- organizational / industries / Agriculture / General (x9657, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### H Red site

- id: `kpi.agriculture.h-red-site`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

H Red site measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is H Red site. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is H Red site on the desired side of its target for this period?

Inputs:

- `metric.h-red-site` (H Red site)

Placements:

- organizational / industries / Agriculture / General (x10305, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### No area covered by woodland

- id: `kpi.agriculture.no-area-covered-by-woodland`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

No area covered by woodland measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is No area covered by woodland. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is No area covered by woodland on the desired side of its target for this period?

Inputs:

- `metric.no-area-covered-by-woodland` (No area covered by woodland)

Placements:

- organizational / industries / Agriculture / General (x13227, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Woodland area certified

- id: `kpi.agriculture.woodland-area-certified`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Woodland area certified measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is Woodland area certified. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Woodland area certified on the desired side of its target for this period?

Inputs:

- `metric.woodland-area-certified` (Woodland area certified)

Placements:

- organizational / industries / Agriculture / General (x13574, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Woodland surface affected by wind blow

- id: `kpi.agriculture.woodland-surface-affected-by-wind-blow`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Woodland surface affected by wind blow measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is Woodland surface affected by wind blow. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Woodland surface affected by wind blow on the desired side of its target for this period?

Inputs:

- `metric.woodland-surface-affected-by-wind-blow` (Woodland surface affected by wind blow)

Placements:

- organizational / industries / Agriculture / General (x13581, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### A Area where plant pest and disease eradication or control efforts were undertaken

- id: `kpi.agriculture.a-area-where-plant-pest-and-disease-eradication-or-control-efforts-were`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

A Area where plant pest and disease eradication or control efforts were undertaken measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is A Area where plant pest and disease eradication or control efforts were undertaken. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is A Area where plant pest and disease eradication or control efforts were undertaken on the desired side of its target for this period?

Inputs:

- `metric.a-area-where-plant-pest-and-disease-eradication-or-control-efforts-were` (A Area where plant pest and disease eradication or control efforts were undertaken)

Placements:

- organizational / industries / Agriculture / General (x13798, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S Terrible mid-Els released

- id: `kpi.agriculture.s-terrible-mid-els-released`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

S Terrible mid-Els released measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is S Terrible mid-Els released. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S Terrible mid-Els released on the desired side of its target for this period?

Inputs:

- `metric.s-terrible-mid-els-released` (S Terrible mid-Els released)

Placements:

- organizational / industries / Agriculture / General (x13985, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Commercial citrus acres surveyed for citruslurker

- id: `kpi.agriculture.commercial-citrus-acres-surveyed-for-citruslurker`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Commercial citrus acres surveyed for citruslurker measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is Commercial citrus acres surveyed for citruslurker. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Commercial citrus acres surveyed for citruslurker on the desired side of its target for this period?

Inputs:

- `metric.commercial-citrus-acres-surveyed-for-citruslurker` (Commercial citrus acres surveyed for citruslurker)

Placements:

- organizational / industries / Agriculture / General (x13986, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Commercial citrus acres free of citrus canker

- id: `kpi.agriculture.commercial-citrus-acres-free-of-citrus-canker`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Commercial citrus acres free of citrus canker measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is Commercial citrus acres free of citrus canker. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Commercial citrus acres free of citrus canker on the desired side of its target for this period?

Inputs:

- `metric.commercial-citrus-acres-free-of-citrus-canker` (Commercial citrus acres free of citrus canker)

Placements:

- organizational / industries / Agriculture / General (x13987, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S Newly introduced pests and diseases prevented from infesting plants

- id: `kpi.agriculture.s-newly-introduced-pests-and-diseases-prevented-from-infesting-plants`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

S Newly introduced pests and diseases prevented from infesting plants measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is S Newly introduced pests and diseases prevented from infesting plants. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S Newly introduced pests and diseases prevented from infesting plants on the desired side of its target for this period?

Inputs:

- `metric.s-newly-introduced-pests-and-diseases-prevented-from-infesting-plants` (S Newly introduced pests and diseases prevented from infesting plants)

Placements:

- organizational / industries / Agriculture / General (x13988, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### A Animal site inspection of vetscape

- id: `kpi.agriculture.a-animal-site-inspection-of-vetscape`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

A Animal site inspection of vetscape measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is A Animal site inspection of vetscape. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is A Animal site inspection of vetscape on the desired side of its target for this period?

Inputs:

- `metric.a-animal-site-inspection-of-vetscape` (A Animal site inspection of vetscape)

Placements:

- organizational / industries / Agriculture / General (x13989, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S Healthful processing plant inspections

- id: `kpi.agriculture.s-healthful-processing-plant-inspections`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

S Healthful processing plant inspections measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is S Healthful processing plant inspections. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S Healthful processing plant inspections on the desired side of its target for this period?

Inputs:

- `metric.s-healthful-processing-plant-inspections` (S Healthful processing plant inspections)

Placements:

- organizational / industries / Agriculture / General (x13992, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S Tonnes of fruits and vegetables inspected

- id: `kpi.agriculture.s-tonnes-of-fruits-and-vegetables-inspected`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

S Tonnes of fruits and vegetables inspected measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is S Tonnes of fruits and vegetables inspected. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S Tonnes of fruits and vegetables inspected on the desired side of its target for this period?

Inputs:

- `metric.s-tonnes-of-fruits-and-vegetables-inspected` (S Tonnes of fruits and vegetables inspected)

Placements:

- organizational / industries / Agriculture / General (x13995, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S Milk products inspections conducted

- id: `kpi.agriculture.s-milk-products-inspections-conducted`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

S Milk products inspections conducted measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is S Milk products inspections conducted. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S Milk products inspections conducted on the desired side of its target for this period?

Inputs:

- `metric.s-milk-products-inspections-conducted` (S Milk products inspections conducted)

Placements:

- organizational / industries / Agriculture / General (x38222, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### F Forest land protected from wildfires

- id: `kpi.agriculture.f-forest-land-protected-from-wildfires`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

F Forest land protected from wildfires measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is F Forest land protected from wildfires. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is F Forest land protected from wildfires on the desired side of its target for this period?

Inputs:

- `metric.f-forest-land-protected-from-wildfires` (F Forest land protected from wildfires)

Placements:

- organizational / industries / Agriculture / General (x38254, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S Land burned through prescribed burning

- id: `kpi.agriculture.s-land-burned-through-prescribed-burning`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

S Land burned through prescribed burning measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is S Land burned through prescribed burning. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S Land burned through prescribed burning on the desired side of its target for this period?

Inputs:

- `metric.s-land-burned-through-prescribed-burning` (S Land burned through prescribed burning)

Placements:

- organizational / industries / Agriculture / General (x38365, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S Wildfires detected and suppressed

- id: `kpi.agriculture.s-wildfires-detected-and-suppressed`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

S Wildfires detected and suppressed measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is S Wildfires detected and suppressed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S Wildfires detected and suppressed on the desired side of its target for this period?

Inputs:

- `metric.s-wildfires-detected-and-suppressed` (S Wildfires detected and suppressed)

Placements:

- organizational / industries / Agriculture / General (x38366, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S Wildfires caused by humans

- id: `kpi.agriculture.s-wildfires-caused-by-humans`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

S Wildfires caused by humans measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is S Wildfires caused by humans. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S Wildfires caused by humans on the desired side of its target for this period?

Inputs:

- `metric.s-wildfires-caused-by-humans` (S Wildfires caused by humans)

Placements:

- organizational / industries / Agriculture / General (x38364, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S Wildfire caused by human actions

- id: `kpi.agriculture.s-wildfire-caused-by-human-actions`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

S Wildfire caused by human actions measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is S Wildfire caused by human actions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S Wildfire caused by human actions on the desired side of its target for this period?

Inputs:

- `metric.s-wildfire-caused-by-human-actions` (S Wildfire caused by human actions)

Placements:

- organizational / industries / Agriculture / General (x39476, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S Threatened structures not burned by wildfires

- id: `kpi.agriculture.s-threatened-structures-not-burned-by-wildfires`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

S Threatened structures not burned by wildfires measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is S Threatened structures not burned by wildfires. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S Threatened structures not burned by wildfires on the desired side of its target for this period?

Inputs:

- `metric.s-threatened-structures-not-burned-by-wildfires` (S Threatened structures not burned by wildfires)

Placements:

- organizational / industries / Agriculture / General (x39473, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S Acres of protected forest and wild lands burned by wildfire

- id: `kpi.agriculture.s-acres-of-protected-forest-and-wild-lands-burned-by-wildfire`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

S Acres of protected forest and wild lands burned by wildfire measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is S Acres of protected forest and wild lands burned by wildfire. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S Acres of protected forest and wild lands burned by wildfire on the desired side of its target for this period?

Inputs:

- `metric.s-acres-of-protected-forest-and-wild-lands-burned-by-wildfire` (S Acres of protected forest and wild lands burned by wildfire)

Placements:

- organizational / industries / Agriculture / General (x39474, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S State managed forestry

- id: `kpi.agriculture.s-state-managed-forestry`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

S State managed forestry measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is S State managed forestry. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S State managed forestry on the desired side of its target for this period?

Inputs:

- `metric.s-state-managed-forestry` (S State managed forestry)

Placements:

- organizational / industries / Agriculture / General (x39477, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S State forest timber producing acres adequately stocked

- id: `kpi.agriculture.s-state-forest-timber-producing-acres-adequately-stocked`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

S State forest timber producing acres adequately stocked measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is S State forest timber producing acres adequately stocked. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S State forest timber producing acres adequately stocked on the desired side of its target for this period?

Inputs:

- `metric.s-state-forest-timber-producing-acres-adequately-stocked` (S State forest timber producing acres adequately stocked)

Placements:

- organizational / industries / Agriculture / General (x39551, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S Cattle per household

- id: `kpi.agriculture.s-cattle-per-household`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

S Cattle per household measures that result inside Agriculture, subcategory General. The unit is number. The formula is A / B, where A is S Cattle, B is household. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S Cattle per household on the desired side of its target for this period?

Inputs:

- `metric.s-cattle` (S Cattle)
- `metric.household` (household)

Placements:

- organizational / industries / Agriculture / General (x36227, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S Households with cattle

- id: `kpi.agriculture.s-households-with-cattle`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

S Households with cattle measures that result inside Agriculture, subcategory General. The unit is number. The formula is A, where A is S Households with cattle. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S Households with cattle on the desired side of its target for this period?

Inputs:

- `metric.s-households-with-cattle` (S Households with cattle)

Placements:

- organizational / industries / Agriculture / General (x36235, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Seasonal workers demand

- id: `kpi.agriculture.seasonal-workers-demand`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Seasonal workers demand measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Seasonal workers demand. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Seasonal workers demand on the desired side of its target for this period?

Inputs:

- `metric.seasonal-workers-demand` (Seasonal workers demand)

Placements:

- organizational / industries / Agriculture / General (xS4463, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Pesticide sample determinations made in the pesticide laboratory

- id: `kpi.agriculture.pesticide-sample-determinations-made-in-the-pesticide-laboratory`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Pesticide sample determinations made in the pesticide laboratory measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Pesticide sample determinations made in the pesticide laboratory. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Pesticide sample determinations made in the pesticide laboratory on the desired side of its target for this period?

Inputs:

- `metric.pesticide-sample-determinations-made-in-the-pesticide-laboratory` (Pesticide sample determinations made in the pesticide laboratory)

Placements:

- organizational / industries / Agriculture / General (xS2297, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Food, seed and fertilizer inspected products in compliance with standards

- id: `kpi.agriculture.food-seed-and-fertilizer-inspected-products-in-compliance-with-standards`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Food, seed and fertilizer inspected products in compliance with standards measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Food, seed and fertilizer inspected products in compliance with standards. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Food, seed and fertilizer inspected products in compliance with standards on the desired side of its target for this period?

Inputs:

- `metric.food-seed-and-fertilizer-inspected-products-in-compliance-with-standards` (Food, seed and fertilizer inspected products in compliance with standards)

Placements:

- organizational / industries / Agriculture / General (xS5926, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Dairy establishment inspections

- id: `kpi.agriculture.dairy-establishment-inspections`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Dairy establishment inspections measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Dairy establishment inspections. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Dairy establishment inspections on the desired side of its target for this period?

Inputs:

- `metric.dairy-establishment-inspections` (Dairy establishment inspections)

Placements:

- organizational / industries / Agriculture / General (xS5922, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### People who made at least one recreational visit from home to woodland

- id: `kpi.agriculture.people-who-made-at-least-one-recreational-visit-from-home-to-woodland`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

People who made at least one recreational visit from home to woodland measures that result inside Agriculture, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is People who made at least one recreational visit, B is home to woodland. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is People who made at least one recreational visit from home to woodland on the desired side of its target for this period?

Inputs:

- `metric.people-who-made-at-least-one-recreational-visit` (People who made at least one recreational visit)
- `metric.home-to-woodland` (home to woodland)

Placements:

- organizational / industries / Agriculture / General (xS5997, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Home visits to woodland

- id: `kpi.agriculture.home-visits-to-woodland`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Home visits to woodland measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Home visits to woodland. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Home visits to woodland on the desired side of its target for this period?

Inputs:

- `metric.home-visits-to-woodland` (Home visits to woodland)

Placements:

- organizational / industries / Agriculture / General (xS6069, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Home grown timber consumption

- id: `kpi.agriculture.home-grown-timber-consumption`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Home grown timber consumption measures that result inside Agriculture, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Home grown timber consumption, B is whole named by Home grown timber consumption. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Home grown timber consumption on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-home-grown-timber-consumption` (part named by Home grown timber consumption)
- `metric.whole-named-by-home-grown-timber-consumption` (whole named by Home grown timber consumption)

Placements:

- organizational / industries / Agriculture / General (xS6205, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Nitrogen use in emissions per populated land area

- id: `kpi.agriculture.nitrogen-use-in-emissions-per-populated-land-area`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Nitrogen use in emissions per populated land area measures that result inside Agriculture, subcategory General. The unit is count. The formula is A / B, where A is Nitrogen use in emissions, B is populated land area. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Nitrogen use in emissions per populated land area on the desired side of its target for this period?

Inputs:

- `metric.nitrogen-use-in-emissions` (Nitrogen use in emissions)
- `metric.populated-land-area` (populated land area)

Placements:

- organizational / industries / Agriculture / General (xS6997, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Biozone protection

- id: `kpi.agriculture.biozone-protection`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Biozone protection measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Biozone protection. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Biozone protection on the desired side of its target for this period?

Inputs:

- `metric.biozone-protection` (Biozone protection)

Placements:

- organizational / industries / Agriculture / General (xS6403, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Master protect against use

- id: `kpi.agriculture.master-protect-against-use`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Master protect against use measures that result inside Agriculture, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Master protect against use, B is whole named by Master protect against use. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Master protect against use on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-master-protect-against-use` (part named by Master protect against use)
- `metric.whole-named-by-master-protect-against-use` (whole named by Master protect against use)

Placements:

- organizational / industries / Agriculture / General (xS6044, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Critical habitat protection

- id: `kpi.agriculture.critical-habitat-protection`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Critical habitat protection measures that result inside Agriculture, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Critical habitat protection, B is whole named by Critical habitat protection. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Critical habitat protection on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-critical-habitat-protection` (part named by Critical habitat protection)
- `metric.whole-named-by-critical-habitat-protection` (whole named by Critical habitat protection)

Placements:

- organizational / industries / Agriculture / General (xS6455, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Marine trophic index

- id: `kpi.agriculture.marine-trophic-index`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: index
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Marine trophic index measures that result inside Agriculture, subcategory General. The unit is count. The formula is (A / B) * 100, where A is current Marine trophic index, B is base-period Marine trophic index. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Marine trophic index on the desired side of its target for this period?

Inputs:

- `metric.current-marine-trophic-index` (current Marine trophic index)
- `metric.base-period-marine-trophic-index` (base-period Marine trophic index)

Placements:

- organizational / industries / Agriculture / General (xS6408, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Trawling intensity

- id: `kpi.agriculture.trawling-intensity`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Trawling intensity measures that result inside Agriculture, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Trawling intensity, B is whole named by Trawling intensity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Trawling intensity on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-trawling-intensity` (part named by Trawling intensity)
- `metric.whole-named-by-trawling-intensity` (whole named by Trawling intensity)

Placements:

- organizational / industries / Agriculture / General (xS6499, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Agriculture subsidies

- id: `kpi.agriculture.agriculture-subsidies`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Agriculture subsidies measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Agriculture subsidies. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Agriculture subsidies on the desired side of its target for this period?

Inputs:

- `metric.agriculture-subsidies` (Agriculture subsidies)

Placements:

- organizational / industries / Agriculture / General (xS6412, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Livestock production

- id: `kpi.agriculture.livestock-production`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Livestock production measures that result inside Agriculture, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Livestock production, B is whole named by Livestock production. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Livestock production on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-livestock-production` (part named by Livestock production)
- `metric.whole-named-by-livestock-production` (whole named by Livestock production)

Placements:

- organizational / industries / Agriculture / General (xS19583, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Losses in the livestock sector

- id: `kpi.agriculture.losses-in-the-livestock-sector`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Losses in the livestock sector measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Losses in the livestock sector. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Losses in the livestock sector on the desired side of its target for this period?

Inputs:

- `metric.losses-in-the-livestock-sector` (Losses in the livestock sector)

Placements:

- organizational / industries / Agriculture / General (xS19587, page_0098)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fertilizer consumption in kilograms per hectare of arable land

- id: `kpi.agriculture.fertilizer-consumption-in-kilograms-per-hectare-of-arable-land`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fertilizer consumption in kilograms per hectare of arable land measures that result inside Agriculture, subcategory General. The unit is count. The formula is A / B, where A is Fertilizer consumption in kilograms, B is hectare of arable land. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fertilizer consumption in kilograms per hectare of arable land on the desired side of its target for this period?

Inputs:

- `metric.fertilizer-consumption-in-kilograms` (Fertilizer consumption in kilograms)
- `metric.hectare-of-arable-land` (hectare of arable land)

Placements:

- organizational / industries / Agriculture / General (sK7110 sK7098, page_0209)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fodder from arable land

- id: `kpi.agriculture.fodder-from-arable-land`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fodder from arable land measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Fodder from arable land. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fodder from arable land on the desired side of its target for this period?

Inputs:

- `metric.fodder-from-arable-land` (Fodder from arable land)

Placements:

- organizational / industries / Agriculture / General (sK7111 sK7081, page_0209)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hectares of land under millet production

- id: `kpi.agriculture.hectares-of-land-under-millet-production`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Hectares of land under millet production measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Hectares of land under millet production. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hectares of land under millet production on the desired side of its target for this period?

Inputs:

- `metric.hectares-of-land-under-millet-production` (Hectares of land under millet production)

Placements:

- organizational / industries / Agriculture / General (sK7115 sK7082, page_0209)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Kitchen gardens land use

- id: `kpi.agriculture.kitchen-gardens-land-use`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Kitchen gardens land use measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Kitchen gardens land use. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Kitchen gardens land use on the desired side of its target for this period?

Inputs:

- `metric.kitchen-gardens-land-use` (Kitchen gardens land use)

Placements:

- organizational / industries / Agriculture / General (sK7116 sK7083, page_0209)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Aggregate direct, trademark applications

- id: `kpi.agriculture.aggregate-direct-trademark-applications`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Aggregate direct, trademark applications measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Aggregate direct, trademark applications. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Aggregate direct, trademark applications on the desired side of its target for this period?

Inputs:

- `metric.aggregate-direct-trademark-applications` (Aggregate direct, trademark applications)

Placements:

- organizational / industries / Agriculture / General (sK7117 sK7107, page_0209)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Agricultural area farmed by owner

- id: `kpi.agriculture.agricultural-area-farmed-by-owner`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Agricultural area farmed by owner measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Agricultural area farmed by owner. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Agricultural area farmed by owner on the desired side of its target for this period?

Inputs:

- `metric.agricultural-area-farmed-by-owner` (Agricultural area farmed by owner)

Placements:

- organizational / industries / Agriculture / General (sK7108, page_0209)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Agricultural area farmed by tenant

- id: `kpi.agriculture.agricultural-area-farmed-by-tenant`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Agricultural area farmed by tenant measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Agricultural area farmed by tenant. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Agricultural area farmed by tenant on the desired side of its target for this period?

Inputs:

- `metric.agricultural-area-farmed-by-tenant` (Agricultural area farmed by tenant)

Placements:

- organizational / industries / Agriculture / General (sK7109, page_0209)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Agricultural area in less favoured area

- id: `kpi.agriculture.agricultural-area-in-less-favoured-area`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Agricultural area in less favoured area measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Agricultural area in less favoured area. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Agricultural area in less favoured area on the desired side of its target for this period?

Inputs:

- `metric.agricultural-area-in-less-favoured-area` (Agricultural area in less favoured area)

Placements:

- organizational / industries / Agriculture / General (sK7111, page_0209)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Agricultural area holdings with 100 ESU and over

- id: `kpi.agriculture.agricultural-area-holdings-with-100-esu-and-over`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Agricultural area holdings with 100 ESU and over measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Agricultural area holdings with 100 ESU and over. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Agricultural area holdings with 100 ESU and over on the desired side of its target for this period?

Inputs:

- `metric.agricultural-area-holdings-with-100-esu-and-over` (Agricultural area holdings with 100 ESU and over)

Placements:

- organizational / industries / Agriculture / General (sK7113, page_0209)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Agricultural area of holdings with 16 to 40 ESU

- id: `kpi.agriculture.agricultural-area-of-holdings-with-16-to-40-esu`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Agricultural area of holdings with 16 to 40 ESU measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Agricultural area of holdings with 16 to 40 ESU. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Agricultural area of holdings with 16 to 40 ESU on the desired side of its target for this period?

Inputs:

- `metric.agricultural-area-of-holdings-with-16-to-40-esu` (Agricultural area of holdings with 16 to 40 ESU)

Placements:

- organizational / industries / Agriculture / General (sK7114, page_0209)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Agricultural area of holdings with 3 to 4 ESU

- id: `kpi.agriculture.agricultural-area-of-holdings-with-3-to-4-esu`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Agricultural area of holdings with 3 to 4 ESU measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Agricultural area of holdings with 3 to 4 ESU. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Agricultural area of holdings with 3 to 4 ESU on the desired side of its target for this period?

Inputs:

- `metric.agricultural-area-of-holdings-with-3-to-4-esu` (Agricultural area of holdings with 3 to 4 ESU)

Placements:

- organizational / industries / Agriculture / General (sK7115, page_0209)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Agricultural area of holdings with 40 to 100 ESU

- id: `kpi.agriculture.agricultural-area-of-holdings-with-40-to-100-esu`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Agricultural area of holdings with 40 to 100 ESU measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Agricultural area of holdings with 40 to 100 ESU. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Agricultural area of holdings with 40 to 100 ESU on the desired side of its target for this period?

Inputs:

- `metric.agricultural-area-of-holdings-with-40-to-100-esu` (Agricultural area of holdings with 40 to 100 ESU)

Placements:

- organizational / industries / Agriculture / General (sK7116, page_0209)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Agricultural area of holdings with 8 to 16 ESU

- id: `kpi.agriculture.agricultural-area-of-holdings-with-8-to-16-esu`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Agricultural area of holdings with 8 to 16 ESU measures that result inside Agriculture, subcategory General. The unit is count. The formula is A, where A is Agricultural area of holdings with 8 to 16 ESU. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Agricultural area of holdings with 8 to 16 ESU on the desired side of its target for this period?

Inputs:

- `metric.agricultural-area-of-holdings-with-8-to-16-esu` (Agricultural area of holdings with 8 to 16 ESU)

Placements:

- organizational / industries / Agriculture / General (sK7118, page_0209)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
