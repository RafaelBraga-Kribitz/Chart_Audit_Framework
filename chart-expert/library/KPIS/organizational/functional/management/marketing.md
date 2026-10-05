# Management / Marketing

Context: organizational. Group: functional. KPIs: 3.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Customer attrition

- id: `kpi.management.customer-attrition`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.marketing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Customer attrition measures that result inside Management, subcategory Marketing. The unit is percent. The formula is (A / B) * 100, where A is part named by Customer attrition, B is whole named by Customer attrition. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Customer attrition on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-customer-attrition` (part named by Customer attrition)
- `metric.whole-named-by-customer-attrition` (whole named by Customer attrition)

Placements:

- organizational / functional / Management / Marketing (sK19, page_0039)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Marketing spend per customer

- id: `kpi.management.marketing-spend-per-customer`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.marketing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Marketing spend per customer measures that result inside Management, subcategory Marketing. The unit is currency. The formula is A / B, where A is Marketing spend, B is customer. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Marketing spend per customer on the desired side of its target for this period?

Inputs:

- `metric.marketing-spend` (Marketing spend)
- `metric.customer` (customer)

Placements:

- organizational / functional / Management / Marketing (sK20, page_0039)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Brand awareness

- id: `kpi.management.brand-awareness`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.marketing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Brand awareness measures that result inside Management, subcategory Marketing. The unit is percent. The formula is (A / B) * 100, where A is part named by Brand awareness, B is whole named by Brand awareness. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Brand awareness on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-brand-awareness` (part named by Brand awareness)
- `metric.whole-named-by-brand-awareness` (whole named by Brand awareness)

Placements:

- organizational / functional / Management / Marketing (sK27, page_0039)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
