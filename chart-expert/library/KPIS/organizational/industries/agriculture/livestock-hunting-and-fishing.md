# Agriculture / Livestock, Hunting and Fishing

Context: organizational. Group: industries. KPIs: 67.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Teams no steep ratio

- id: `kpi.agriculture.teams-no-steep-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Teams no steep ratio measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Teams no steep ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Teams no steep ratio on the desired side of its target for this period?

Inputs:

- `metric.teams-no-steep-ratio` (Teams no steep ratio)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s3814, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Harvesting rate

- id: `kpi.agriculture.harvesting-rate`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Harvesting rate measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Harvesting rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Harvesting rate on the desired side of its target for this period?

Inputs:

- `metric.harvesting-rate` (Harvesting rate)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s1810, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Killdown piglets

- id: `kpi.agriculture.killdown-piglets`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Killdown piglets measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is part named by Killdown piglets, B is whole named by Killdown piglets. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Killdown piglets on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-killdown-piglets` (part named by Killdown piglets)
- `metric.whole-named-by-killdown-piglets` (whole named by Killdown piglets)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s8120, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Pilegut survival

- id: `kpi.agriculture.pilegut-survival`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Pilegut survival measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is part named by Pilegut survival, B is whole named by Pilegut survival. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Pilegut survival on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-pilegut-survival` (part named by Pilegut survival)
- `metric.whole-named-by-pilegut-survival` (whole named by Pilegut survival)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s1121, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Artificial insemination cost per mating

- id: `kpi.agriculture.artificial-insemination-cost-per-mating`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Artificial insemination cost per mating measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is number. The formula is A / B, where A is Artificial insemination cost, B is mating. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Artificial insemination cost per mating on the desired side of its target for this period?

Inputs:

- `metric.artificial-insemination-cost` (Artificial insemination cost)
- `metric.mating` (mating)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s8216, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Price per kilogram of meat sold

- id: `kpi.agriculture.price-per-kilogram-of-meat-sold`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Price per kilogram of meat sold measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is currency. The formula is A / B, where A is Price, B is kilogram of meat sold. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Price per kilogram of meat sold on the desired side of its target for this period?

Inputs:

- `metric.price` (Price)
- `metric.kilogram-of-meat-sold` (kilogram of meat sold)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s8286, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Prime caresses

- id: `kpi.agriculture.prime-caresses`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Prime caresses measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is part named by Prime caresses, B is whole named by Prime caresses. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Prime caresses on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-prime-caresses` (part named by Prime caresses)
- `metric.whole-named-by-prime-caresses` (whole named by Prime caresses)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s3818, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Supplementary feed cost per lamb

- id: `kpi.agriculture.supplementary-feed-cost-per-lamb`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Supplementary feed cost per lamb measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Supplementary feed cost, B is lamb. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Supplementary feed cost per lamb on the desired side of its target for this period?

Inputs:

- `metric.supplementary-feed-cost` (Supplementary feed cost)
- `metric.lamb` (lamb)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s3846, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Preweigh meat rate

- id: `kpi.agriculture.preweigh-meat-rate`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Preweigh meat rate measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is currency. The formula is A, where A is Preweigh meat rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Preweigh meat rate on the desired side of its target for this period?

Inputs:

- `metric.preweigh-meat-rate` (Preweigh meat rate)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s8439, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Live weight at slaughter

- id: `kpi.agriculture.live-weight-at-slaughter`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Live weight at slaughter measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Live weight at slaughter. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Live weight at slaughter on the desired side of its target for this period?

Inputs:

- `metric.live-weight-at-slaughter` (Live weight at slaughter)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s8508, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Milk yield per cow

- id: `kpi.agriculture.milk-yield-per-cow`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Milk yield per cow measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Milk yield, B is cow. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Milk yield per cow on the desired side of its target for this period?

Inputs:

- `metric.milk-yield` (Milk yield)
- `metric.cow` (cow)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s8552, page_0060)
- organizational / industries / Agriculture / Organizational > Industries (sK4622, page_0061)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Piglets born dead per farrowing

- id: `kpi.agriculture.piglets-born-dead-per-farrowing`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Piglets born dead per farrowing measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Piglets born dead, B is farrowing. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Piglets born dead per farrowing on the desired side of its target for this period?

Inputs:

- `metric.piglets-born-dead` (Piglets born dead)
- `metric.farrowing` (farrowing)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s8696, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Milk quota delivered

- id: `kpi.agriculture.milk-quota-delivered`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Milk quota delivered measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is part named by Milk quota delivered, B is whole named by Milk quota delivered. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Milk quota delivered on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-milk-quota-delivered` (part named by Milk quota delivered)
- `metric.whole-named-by-milk-quota-delivered` (whole named by Milk quota delivered)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s8727, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Milk production per kilogram body weight

- id: `kpi.agriculture.milk-production-per-kilogram-body-weight`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Milk production per kilogram body weight measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Milk production, B is kilogram body weight. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Milk production per kilogram body weight on the desired side of its target for this period?

Inputs:

- `metric.milk-production` (Milk production)
- `metric.kilogram-body-weight` (kilogram body weight)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s8784, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Dressed weight at slaughter

- id: `kpi.agriculture.dressed-weight-at-slaughter`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Dressed weight at slaughter measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Dressed weight at slaughter. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Dressed weight at slaughter on the desired side of its target for this period?

Inputs:

- `metric.dressed-weight-at-slaughter` (Dressed weight at slaughter)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s1321, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Animal deaths in transit

- id: `kpi.agriculture.animal-deaths-in-transit`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Animal deaths in transit measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Animal deaths in transit. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Animal deaths in transit on the desired side of its target for this period?

Inputs:

- `metric.animal-deaths-in-transit` (Animal deaths in transit)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s1432, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Meat sold per sow

- id: `kpi.agriculture.meat-sold-per-sow`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Meat sold per sow measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Meat sold, B is sow. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Meat sold per sow on the desired side of its target for this period?

Inputs:

- `metric.meat-sold` (Meat sold)
- `metric.sow` (sow)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s1433, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Pigs weight gained

- id: `kpi.agriculture.pigs-weight-gained`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Pigs weight gained measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Pigs weight gained. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Pigs weight gained on the desired side of its target for this period?

Inputs:

- `metric.pigs-weight-gained` (Pigs weight gained)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s1434, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fertilizer to milk price ratio

- id: `kpi.agriculture.fertilizer-to-milk-price-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fertilizer to milk price ratio measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Fertilizer to milk price ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fertilizer to milk price ratio on the desired side of its target for this period?

Inputs:

- `metric.fertilizer-to-milk-price-ratio` (Fertilizer to milk price ratio)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s1466, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Milk solids production per cow

- id: `kpi.agriculture.milk-solids-production-per-cow`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Milk solids production per cow measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Milk solids production, B is cow. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Milk solids production per cow on the desired side of its target for this period?

Inputs:

- `metric.milk-solids-production` (Milk solids production)
- `metric.cow` (cow)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s1479, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Milk solids production per hectare

- id: `kpi.agriculture.milk-solids-production-per-hectare`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Milk solids production per hectare measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Milk solids production, B is hectare. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Milk solids production per hectare on the desired side of its target for this period?

Inputs:

- `metric.milk-solids-production` (Milk solids production)
- `metric.hectare` (hectare)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (s1489, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Milk flow rate

- id: `kpi.agriculture.milk-flow-rate`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Milk flow rate measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Milk flow rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Milk flow rate on the desired side of its target for this period?

Inputs:

- `metric.milk-flow-rate` (Milk flow rate)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK1491, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Lamb carcass weight

- id: `kpi.agriculture.lamb-carcass-weight`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Lamb carcass weight measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Lamb carcass weight. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Lamb carcass weight on the desired side of its target for this period?

Inputs:

- `metric.lamb-carcass-weight` (Lamb carcass weight)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK1506, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Wool production per sheep

- id: `kpi.agriculture.wool-production-per-sheep`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Wool production per sheep measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Wool production, B is sheep. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Wool production per sheep on the desired side of its target for this period?

Inputs:

- `metric.wool-production` (Wool production)
- `metric.sheep` (sheep)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK1507, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Stalls idle

- id: `kpi.agriculture.stalls-idle`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Stalls idle measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Stalls idle. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Stalls idle on the desired side of its target for this period?

Inputs:

- `metric.stalls-idle` (Stalls idle)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK1508, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Piglets born alive per farrowing

- id: `kpi.agriculture.piglets-born-alive-per-farrowing`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Piglets born alive per farrowing measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Piglets born alive, B is farrowing. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Piglets born alive per farrowing on the desired side of its target for this period?

Inputs:

- `metric.piglets-born-alive` (Piglets born alive)
- `metric.farrowing` (farrowing)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK1584, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### 80 days subordination rate

- id: `kpi.agriculture.80-days-subordination-rate`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

80 days subordination rate measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is numerator of 80 days subordination rate, B is base of 80 days subordination rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is 80 days subordination rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-80-days-subordination-rate` (numerator of 80 days subordination rate)
- `metric.base-of-80-days-subordination-rate` (base of 80 days subordination rate)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK1778, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Concentrated cost per litter milk produced

- id: `kpi.agriculture.concentrated-cost-per-litter-milk-produced`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Concentrated cost per litter milk produced measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is A / B, where A is Concentrated cost, B is litter milk produced. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Concentrated cost per litter milk produced on the desired side of its target for this period?

Inputs:

- `metric.concentrated-cost` (Concentrated cost)
- `metric.litter-milk-produced` (litter milk produced)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK1780, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Concentrate use per litter of milk produced

- id: `kpi.agriculture.concentrate-use-per-litter-of-milk-produced`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Concentrate use per litter of milk produced measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Concentrate use, B is litter of milk produced. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Concentrate use per litter of milk produced on the desired side of its target for this period?

Inputs:

- `metric.concentrate-use` (Concentrate use)
- `metric.litter-of-milk-produced` (litter of milk produced)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK1809, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cows milk in stall

- id: `kpi.agriculture.cows-milk-in-stall`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cows milk in stall measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Cows milk in stall. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cows milk in stall on the desired side of its target for this period?

Inputs:

- `metric.cows-milk-in-stall` (Cows milk in stall)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK1811, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cows in stall off from second round of mating

- id: `kpi.agriculture.cows-in-stall-off-from-second-round-of-mating`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cows in stall off from second round of mating measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Cows in stall off from second round of mating. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cows in stall off from second round of mating on the desired side of its target for this period?

Inputs:

- `metric.cows-in-stall-off-from-second-round-of-mating` (Cows in stall off from second round of mating)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK1815, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cows per weight gained by calves

- id: `kpi.agriculture.cows-per-weight-gained-by-calves`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cows per weight gained by calves measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Cows, B is weight gained by calves. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cows per weight gained by calves on the desired side of its target for this period?

Inputs:

- `metric.cows` (Cows)
- `metric.weight-gained-by-calves` (weight gained by calves)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK1817, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Calving to conception interval

- id: `kpi.agriculture.calving-to-conception-interval`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Calving to conception interval measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Calving to conception interval. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Calving to conception interval on the desired side of its target for this period?

Inputs:

- `metric.calving-to-conception-interval` (Calving to conception interval)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK1818, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Calf body weight gained per day

- id: `kpi.agriculture.calf-body-weight-gained-per-day`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Calf body weight gained per day measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Calf body weight gained, B is day. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Calf body weight gained per day on the desired side of its target for this period?

Inputs:

- `metric.calf-body-weight-gained` (Calf body weight gained)
- `metric.day` (day)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK1821, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Costs to new calf born in stall with 1x to sale

- id: `kpi.agriculture.costs-to-new-calf-born-in-stall-with-1x-to-sale`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Costs to new calf born in stall with 1x to sale measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is currency. The formula is A, where A is Costs to new calf born in stall with 1x to sale. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Costs to new calf born in stall with 1x to sale on the desired side of its target for this period?

Inputs:

- `metric.costs-to-new-calf-born-in-stall-with-1x-to-sale` (Costs to new calf born in stall with 1x to sale)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK1827, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost to rear a calf from weaning to 12 weeks or 300 kg

- id: `kpi.agriculture.cost-to-rear-a-calf-from-weaning-to-12-weeks-or-300-kg`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost to rear a calf from weaning to 12 weeks or 300 kg measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is currency. The formula is A, where A is Cost to rear a calf from weaning to 12 weeks or 300 kg. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost to rear a calf from weaning to 12 weeks or 300 kg on the desired side of its target for this period?

Inputs:

- `metric.cost-to-rear-a-calf-from-weaning-to-12-weeks-or-300-kg` (Cost to rear a calf from weaning to 12 weeks or 300 kg)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK1839, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost to rear a calf from birth to weaning

- id: `kpi.agriculture.cost-to-rear-a-calf-from-birth-to-weaning`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost to rear a calf from birth to weaning measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is currency. The formula is A, where A is Cost to rear a calf from birth to weaning. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost to rear a calf from birth to weaning on the desired side of its target for this period?

Inputs:

- `metric.cost-to-rear-a-calf-from-birth-to-weaning` (Cost to rear a calf from birth to weaning)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK1899, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### 100 day in calf

- id: `kpi.agriculture.100-day-in-calf`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

100 day in calf measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is part named by 100 day in calf, B is whole named by 100 day in calf. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is 100 day in calf on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-100-day-in-calf` (part named by 100 day in calf)
- `metric.whole-named-by-100-day-in-calf` (whole named by 100 day in calf)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK1947, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Piglets fit for weaning

- id: `kpi.agriculture.piglets-fit-for-weaning`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Piglets fit for weaning measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is part named by Piglets fit for weaning, B is whole named by Piglets fit for weaning. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Piglets fit for weaning on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-piglets-fit-for-weaning` (part named by Piglets fit for weaning)
- `metric.whole-named-by-piglets-fit-for-weaning` (whole named by Piglets fit for weaning)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2156, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Oestrous rate

- id: `kpi.agriculture.oestrous-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Oestrous rate measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is numerator of Oestrous rate, B is base of Oestrous rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Oestrous rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-oestrous-rate` (numerator of Oestrous rate)
- `metric.base-of-oestrous-rate` (base of Oestrous rate)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2295, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Piglets weaned per litter born

- id: `kpi.agriculture.piglets-weaned-per-litter-born`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Piglets weaned per litter born measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Piglets weaned, B is litter born. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Piglets weaned per litter born on the desired side of its target for this period?

Inputs:

- `metric.piglets-weaned` (Piglets weaned)
- `metric.litter-born` (litter born)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2308, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### 200 day not in calf rate

- id: `kpi.agriculture.200-day-not-in-calf-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

200 day not in calf rate measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is numerator of 200 day not in calf rate, B is base of 200 day not in calf rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is 200 day not in calf rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-200-day-not-in-calf-rate` (numerator of 200 day not in calf rate)
- `metric.base-of-200-day-not-in-calf-rate` (base of 200 day not in calf rate)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2464, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Ileat detection rate

- id: `kpi.agriculture.ileat-detection-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Ileat detection rate measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is numerator of Ileat detection rate, B is base of Ileat detection rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Ileat detection rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-ileat-detection-rate` (numerator of Ileat detection rate)
- `metric.base-of-ileat-detection-rate` (base of Ileat detection rate)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2478, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cow replacement cost

- id: `kpi.agriculture.cow-replacement-cost`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cow replacement cost measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is currency. The formula is A, where A is Cow replacement cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cow replacement cost on the desired side of its target for this period?

Inputs:

- `metric.cow-replacement-cost` (Cow replacement cost)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2479, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cow pregnancy value

- id: `kpi.agriculture.cow-pregnancy-value`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cow pregnancy value measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is currency. The formula is A, where A is Cow pregnancy value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cow pregnancy value on the desired side of its target for this period?

Inputs:

- `metric.cow-pregnancy-value` (Cow pregnancy value)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2480, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Dry days

- id: `kpi.agriculture.dry-days`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Dry days measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Dry days. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Dry days on the desired side of its target for this period?

Inputs:

- `metric.dry-days` (Dry days)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2483, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Calf weight gained at weaning

- id: `kpi.agriculture.calf-weight-gained-at-weaning`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Calf weight gained at weaning measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Calf weight gained at weaning. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Calf weight gained at weaning on the desired side of its target for this period?

Inputs:

- `metric.calf-weight-gained-at-weaning` (Calf weight gained at weaning)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2496, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Calves weaning weight

- id: `kpi.agriculture.calves-weaning-weight`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Calves weaning weight measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Calves weaning weight. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Calves weaning weight on the desired side of its target for this period?

Inputs:

- `metric.calves-weaning-weight` (Calves weaning weight)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2525, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cow pregnancy rate

- id: `kpi.agriculture.cow-pregnancy-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cow pregnancy rate measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is numerator of Cow pregnancy rate, B is base of Cow pregnancy rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cow pregnancy rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-cow-pregnancy-rate` (numerator of Cow pregnancy rate)
- `metric.base-of-cow-pregnancy-rate` (base of Cow pregnancy rate)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2532, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Concentrate mixture used per head

- id: `kpi.agriculture.concentrate-mixture-used-per-head`
- kind: kpi
- unit: count
- direction: corridor
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Concentrate mixture used per head measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Concentrate mixture used, B is head. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Concentrate mixture used per head on the desired side of its target for this period?

Inputs:

- `metric.concentrate-mixture-used` (Concentrate mixture used)
- `metric.head` (head)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2539, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Daily calf dose diluted under 1 month old

- id: `kpi.agriculture.daily-calf-dose-diluted-under-1-month-old`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: operational
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Daily calf dose diluted under 1 month old measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is part named by Daily calf dose diluted under 1 month old, B is whole named by Daily calf dose diluted under 1 month old. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Daily calf dose diluted under 1 month old on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-daily-calf-dose-diluted-under-1-month-old` (part named by Daily calf dose diluted under 1 month old)
- `metric.whole-named-by-daily-calf-dose-diluted-under-1-month-old` (whole named by Daily calf dose diluted under 1 month old)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2541, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Concentrate mixture cost per tonne

- id: `kpi.agriculture.concentrate-mixture-cost-per-tonne`
- kind: kpi
- unit: count
- direction: corridor
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Concentrate mixture cost per tonne measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Concentrate mixture cost, B is tonne. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Concentrate mixture cost per tonne on the desired side of its target for this period?

Inputs:

- `metric.concentrate-mixture-cost` (Concentrate mixture cost)
- `metric.tonne` (tonne)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2543, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Herd replacement rate

- id: `kpi.agriculture.herd-replacement-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Herd replacement rate measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is numerator of Herd replacement rate, B is base of Herd replacement rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Herd replacement rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-herd-replacement-rate` (numerator of Herd replacement rate)
- `metric.base-of-herd-replacement-rate` (base of Herd replacement rate)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2545, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### 21 day service submission rate

- id: `kpi.agriculture.21-day-service-submission-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

21 day service submission rate measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is numerator of 21 day service submission rate, B is base of 21 day service submission rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is 21 day service submission rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-21-day-service-submission-rate` (numerator of 21 day service submission rate)
- `metric.base-of-21-day-service-submission-rate` (base of 21 day service submission rate)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2550, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cow milkings days lost

- id: `kpi.agriculture.cow-milkings-days-lost`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cow milkings days lost measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Cow milkings days lost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cow milkings days lost on the desired side of its target for this period?

Inputs:

- `metric.cow-milkings-days-lost` (Cow milkings days lost)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2552, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### 6 weeks in calf farce

- id: `kpi.agriculture.6-weeks-in-calf-farce`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

6 weeks in calf farce measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is part named by 6 weeks in calf farce, B is whole named by 6 weeks in calf farce. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is 6 weeks in calf farce on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-6-weeks-in-calf-farce` (part named by 6 weeks in calf farce)
- `metric.whole-named-by-6-weeks-in-calf-farce` (whole named by 6 weeks in calf farce)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2559, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cows per hectare

- id: `kpi.agriculture.cows-per-hectare`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cows per hectare measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Cows, B is hectare. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cows per hectare on the desired side of its target for this period?

Inputs:

- `metric.cows` (Cows)
- `metric.hectare` (hectare)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2569, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Dry cows

- id: `kpi.agriculture.dry-cows`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Dry cows measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is part named by Dry cows, B is whole named by Dry cows. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Dry cows on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-dry-cows` (part named by Dry cows)
- `metric.whole-named-by-dry-cows` (whole named by Dry cows)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2576, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Milk lactose

- id: `kpi.agriculture.milk-lactose`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Milk lactose measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is part named by Milk lactose, B is whole named by Milk lactose. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Milk lactose on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-milk-lactose` (part named by Milk lactose)
- `metric.whole-named-by-milk-lactose` (whole named by Milk lactose)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2585, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Feed conversion ratio

- id: `kpi.agriculture.feed-conversion-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Feed conversion ratio measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Feed conversion ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Feed conversion ratio on the desired side of its target for this period?

Inputs:

- `metric.feed-conversion-ratio` (Feed conversion ratio)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2594, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Milk yield per hectare

- id: `kpi.agriculture.milk-yield-per-hectare`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Milk yield per hectare measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Milk yield, B is hectare. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Milk yield per hectare on the desired side of its target for this period?

Inputs:

- `metric.milk-yield` (Milk yield)
- `metric.hectare` (hectare)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2595, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Calves live weight as months

- id: `kpi.agriculture.calves-live-weight-as-months`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Calves live weight as months measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is Calves live weight as months. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Calves live weight as months on the desired side of its target for this period?

Inputs:

- `metric.calves-live-weight-as-months` (Calves live weight as months)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2600, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### 50 age and first farceing

- id: `kpi.agriculture.50-age-and-first-farceing`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

50 age and first farceing measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A, where A is 50 age and first farceing. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is 50 age and first farceing on the desired side of its target for this period?

Inputs:

- `metric.50-age-and-first-farceing` (50 age and first farceing)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2617, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Inheifers first lactation milk yield

- id: `kpi.agriculture.inheifers-first-lactation-milk-yield`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Inheifers first lactation milk yield measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is part named by Inheifers first lactation milk yield, B is whole named by Inheifers first lactation milk yield. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Inheifers first lactation milk yield on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-inheifers-first-lactation-milk-yield` (part named by Inheifers first lactation milk yield)
- `metric.whole-named-by-inheifers-first-lactation-milk-yield` (whole named by Inheifers first lactation milk yield)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2678, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Non pregnant heifers

- id: `kpi.agriculture.non-pregnant-heifers`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Non pregnant heifers measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is percent. The formula is (A / B) * 100, where A is part named by Non pregnant heifers, B is whole named by Non pregnant heifers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Non pregnant heifers on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-non-pregnant-heifers` (part named by Non pregnant heifers)
- `metric.whole-named-by-non-pregnant-heifers` (whole named by Non pregnant heifers)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2695, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Operating profit per cow

- id: `kpi.agriculture.operating-profit-per-cow`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Operating profit per cow measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is count. The formula is A / B, where A is Operating profit, B is cow. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Operating profit per cow on the desired side of its target for this period?

Inputs:

- `metric.operating-profit` (Operating profit)
- `metric.cow` (cow)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2698, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S Replacement cost per cow

- id: `kpi.agriculture.s-replacement-cost-per-cow`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.agriculture.livestock-hunting-and-fishing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

S Replacement cost per cow measures that result inside Agriculture, subcategory Livestock, Hunting and Fishing. The unit is number. The formula is A / B, where A is S Replacement cost, B is cow. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S Replacement cost per cow on the desired side of its target for this period?

Inputs:

- `metric.s-replacement-cost` (S Replacement cost)
- `metric.cow` (cow)

Placements:

- organizational / industries / Agriculture / Livestock, Hunting and Fishing (sK2681, page_0060)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
