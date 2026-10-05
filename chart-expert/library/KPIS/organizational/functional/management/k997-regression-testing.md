# Management / K997 # Regression testing

Context: organizational. Group: functional. KPIs: 42.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### ▼ Waste per product

- id: `kpi.management.waste-per-product`
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

▼ Waste per product measures that result inside Management, subcategory Organizational + Functional Areas. The unit is number. The formula is A / B, where A is ▼ Waste, B is product. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is ▼ Waste per product on the desired side of its target for this period?

Inputs:

- `metric.waste` (▼ Waste)
- `metric.product` (product)

Placements:

- organizational / functional / Management / Organizational + Functional Areas (xK1583, page_0015)
- organizational / functional / Management / K997 # Regression testing (K8158, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production first time yield (FTY)

- id: `kpi.management.production-first-time-yield-fty`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Production first time yield (FTY) measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is part named by Production first time yield (FTY), B is whole named by Production first time yield (FTY). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production first time yield (FTY) on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-production-first-time-yield-fty` (part named by Production first time yield (FTY))
- `metric.whole-named-by-production-first-time-yield-fty` (whole named by Production first time yield (FTY))

Placements:

- organizational / functional / Management / K997 # Regression testing (K896, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Defects per million opportunities (DPMO)

- id: `kpi.management.defects-per-million-opportunities-dpmo`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Defects per million opportunities (DPMO) measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is A / B, where A is Defects, B is million opportunities (DPMO). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Defects per million opportunities (DPMO) on the desired side of its target for this period?

Inputs:

- `metric.defects` (Defects)
- `metric.million-opportunities-dpmo` (million opportunities (DPMO))

Placements:

- organizational / functional / Management / K997 # Regression testing (K898, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of new quality (COPQ)

- id: `kpi.management.cost-of-new-quality-copq`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of new quality (COPQ) measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is Cost, B is new quality (COPQ). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of new quality (COPQ) on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.new-quality-copq` (new quality (COPQ))

Placements:

- organizational / functional / Management / K997 # Regression testing (K899, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Final products which do not meet quality criteria

- id: `kpi.management.final-products-which-do-not-meet-quality-criteria`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Final products which do not meet quality criteria measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is part named by Final products which do not meet quality criteria, B is whole named by Final products which do not meet quality criteria. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Final products which do not meet quality criteria on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-final-products-which-do-not-meet-quality-criteria` (part named by Final products which do not meet quality criteria)
- `metric.whole-named-by-final-products-which-do-not-meet-quality-criteria` (whole named by Final products which do not meet quality criteria)

Placements:

- organizational / functional / Management / K997 # Regression testing (K500, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Price of non-conformance

- id: `kpi.management.price-of-non-conformance`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Price of non-conformance measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is Price, B is non-conformance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Price of non-conformance on the desired side of its target for this period?

Inputs:

- `metric.price` (Price)
- `metric.non-conformance` (non-conformance)

Placements:

- organizational / functional / Management / K997 # Regression testing (K526, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Scrap rate

- id: `kpi.management.scrap-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Scrap rate measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is numerator of Scrap rate, B is base of Scrap rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Scrap rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-scrap-rate` (numerator of Scrap rate)
- `metric.base-of-scrap-rate` (base of Scrap rate)

Placements:

- organizational / functional / Management / K997 # Regression testing (K8745, page_0048)
- organizational / industries / Manufacturing / General (▲K745, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Processes under statistical control

- id: `kpi.management.processes-under-statistical-control`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Processes under statistical control measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is part named by Processes under statistical control, B is whole named by Processes under statistical control. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Processes under statistical control on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-processes-under-statistical-control` (part named by Processes under statistical control)
- `metric.whole-named-by-processes-under-statistical-control` (whole named by Processes under statistical control)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1602, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Duration of quality control inspection

- id: `kpi.management.duration-of-quality-control-inspection`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Duration of quality control inspection measures that result inside Management, subcategory K997 # Regression testing. The unit is count. The formula is A, where A is Duration of quality control inspection. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Duration of quality control inspection on the desired side of its target for this period?

Inputs:

- `metric.duration-of-quality-control-inspection` (Duration of quality control inspection)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1641, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production failures by type of defect

- id: `kpi.management.production-failures-by-type-of-defect`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Production failures by type of defect measures that result inside Management, subcategory K997 # Regression testing. The unit is count. The formula is A, where A is Production failures by type of defect. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production failures by type of defect on the desired side of its target for this period?

Inputs:

- `metric.production-failures-by-type-of-defect` (Production failures by type of defect)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1642, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production conformance to present quality standards

- id: `kpi.management.production-conformance-to-present-quality-standards`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Production conformance to present quality standards measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is Production conformance, B is present quality standards. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production conformance to present quality standards on the desired side of its target for this period?

Inputs:

- `metric.production-conformance` (Production conformance)
- `metric.present-quality-standards` (present quality standards)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1648, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Quality assurance processes based on 'Best Practices' evaluation' tools

- id: `kpi.management.quality-assurance-processes-based-on-best-practices-evaluation-tools`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Quality assurance processes based on 'Best Practices' evaluation' tools measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is part named by Quality assurance processes based on 'Best Practices' evaluation' tools, B is whole named by Quality assurance processes based on 'Best Practices' evaluation' tools. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Quality assurance processes based on 'Best Practices' evaluation' tools on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-quality-assurance-processes-based-on-best-practices-evalua` (part named by Quality assurance processes based on 'Best Practices' evaluation' tools)
- `metric.whole-named-by-quality-assurance-processes-based-on-best-practices-evalu` (whole named by Quality assurance processes based on 'Best Practices' evaluation' tools)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1649, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production quality improvement methods used

- id: `kpi.management.production-quality-improvement-methods-used`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Production quality improvement methods used measures that result inside Management, subcategory K997 # Regression testing. The unit is count. The formula is A, where A is Production quality improvement methods used. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production quality improvement methods used on the desired side of its target for this period?

Inputs:

- `metric.production-quality-improvement-methods-used` (Production quality improvement methods used)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1650, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Quality assurance processes that need 'Improvement Measures'

- id: `kpi.management.quality-assurance-processes-that-need-improvement-measures`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Quality assurance processes that need 'Improvement Measures' measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is part named by Quality assurance processes that need 'Improvement Measures', B is whole named by Quality assurance processes that need 'Improvement Measures'. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Quality assurance processes that need 'Improvement Measures' on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-quality-assurance-processes-that-need-improvement-measures` (part named by Quality assurance processes that need 'Improvement Measures')
- `metric.whole-named-by-quality-assurance-processes-that-need-improvement-measure` (whole named by Quality assurance processes that need 'Improvement Measures')

Placements:

- organizational / functional / Management / K997 # Regression testing (K1652, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Quality awareness programs

- id: `kpi.management.quality-awareness-programs`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Quality awareness programs measures that result inside Management, subcategory K997 # Regression testing. The unit is count. The formula is A, where A is Quality awareness programs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Quality awareness programs on the desired side of its target for this period?

Inputs:

- `metric.quality-awareness-programs` (Quality awareness programs)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1655, page_0048)
- organizational / industries / Manufacturing / General (▲K1655, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Review costs

- id: `kpi.management.review-costs`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Review costs measures that result inside Management, subcategory K997 # Regression testing. The unit is count. The formula is A, where A is Review costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Review costs on the desired side of its target for this period?

Inputs:

- `metric.review-costs` (Review costs)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1657, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Prevention actions

- id: `kpi.management.prevention-actions`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Prevention actions measures that result inside Management, subcategory K997 # Regression testing. The unit is count. The formula is A, where A is Prevention actions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Prevention actions on the desired side of its target for this period?

Inputs:

- `metric.prevention-actions` (Prevention actions)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1659, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Defect density

- id: `kpi.management.defect-density`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Defect density measures that result inside Management, subcategory K997 # Regression testing. The unit is count. The formula is A, where A is Defect density. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Defect density on the desired side of its target for this period?

Inputs:

- `metric.defect-density` (Defect density)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1660, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Final product problems due to lack of quality assurance and control

- id: `kpi.management.final-product-problems-due-to-lack-of-quality-assurance-and-control`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Final product problems due to lack of quality assurance and control measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is Final product problems due, B is lack of quality assurance and control. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Final product problems due to lack of quality assurance and control on the desired side of its target for this period?

Inputs:

- `metric.final-product-problems-due` (Final product problems due)
- `metric.lack-of-quality-assurance-and-control` (lack of quality assurance and control)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1662, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Planned quality control review conducted

- id: `kpi.management.planned-quality-control-review-conducted`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Planned quality control review conducted measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is part named by Planned quality control review conducted, B is whole named by Planned quality control review conducted. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Planned quality control review conducted on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-planned-quality-control-review-conducted` (part named by Planned quality control review conducted)
- `metric.whole-named-by-planned-quality-control-review-conducted` (whole named by Planned quality control review conducted)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1664, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Defects per unit

- id: `kpi.management.defects-per-unit`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Defects per unit measures that result inside Management, subcategory K997 # Regression testing. The unit is count. The formula is A / B, where A is Defects, B is unit. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Defects per unit on the desired side of its target for this period?

Inputs:

- `metric.defects` (Defects)
- `metric.unit` (unit)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1665, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Quality control costs

- id: `kpi.management.quality-control-costs`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Quality control costs measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is part named by Quality control costs, B is whole named by Quality control costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Quality control costs on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-quality-control-costs` (part named by Quality control costs)
- `metric.whole-named-by-quality-control-costs` (whole named by Quality control costs)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1667, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Quality control costs within warranty costs

- id: `kpi.management.quality-control-costs-within-warranty-costs`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Quality control costs within warranty costs measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is part named by Quality control costs within warranty costs, B is whole named by Quality control costs within warranty costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Quality control costs within warranty costs on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-quality-control-costs-within-warranty-costs` (part named by Quality control costs within warranty costs)
- `metric.whole-named-by-quality-control-costs-within-warranty-costs` (whole named by Quality control costs within warranty costs)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1668, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Quality control personnel ratio

- id: `kpi.management.quality-control-personnel-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Quality control personnel ratio measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is numerator of Quality control personnel ratio, B is base of Quality control personnel ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Quality control personnel ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-quality-control-personnel-ratio` (numerator of Quality control personnel ratio)
- `metric.base-of-quality-control-personnel-ratio` (base of Quality control personnel ratio)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1669, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revolved times

- id: `kpi.management.revolved-times`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Revolved times measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is part named by Revolved times, B is whole named by Revolved times. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revolved times on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-revolved-times` (part named by Revolved times)
- `metric.whole-named-by-revolved-times` (whole named by Revolved times)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1670, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Quality assurance cost

- id: `kpi.management.quality-assurance-cost`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Quality assurance cost measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is part named by Quality assurance cost, B is whole named by Quality assurance cost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Quality assurance cost on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-quality-assurance-cost` (part named by Quality assurance cost)
- `metric.whole-named-by-quality-assurance-cost` (whole named by Quality assurance cost)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1671, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Quality assurance time

- id: `kpi.management.quality-assurance-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Quality assurance time measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is part named by Quality assurance time, B is whole named by Quality assurance time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Quality assurance time on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-quality-assurance-time` (part named by Quality assurance time)
- `metric.whole-named-by-quality-assurance-time` (whole named by Quality assurance time)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1673, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sample size

- id: `kpi.management.sample-size`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Sample size measures that result inside Management, subcategory K997 # Regression testing. The unit is currency. The formula is A, where A is Sample size. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sample size on the desired side of its target for this period?

Inputs:

- `metric.sample-size` (Sample size)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1674, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cut up/effection products per quality review

- id: `kpi.management.cut-up-effection-products-per-quality-review`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cut up/effection products per quality review measures that result inside Management, subcategory K997 # Regression testing. The unit is count. The formula is A / B, where A is Cut up/effection products, B is quality review. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cut up/effection products per quality review on the desired side of its target for this period?

Inputs:

- `metric.cut-up-effection-products` (Cut up/effection products)
- `metric.quality-review` (quality review)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1677, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Review efficiency

- id: `kpi.management.review-efficiency`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Review efficiency measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is part named by Review efficiency, B is whole named by Review efficiency. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Review efficiency on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-review-efficiency` (part named by Review efficiency)
- `metric.whole-named-by-review-efficiency` (whole named by Review efficiency)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1682, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cut of quality inspection per sample

- id: `kpi.management.cut-of-quality-inspection-per-sample`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cut of quality inspection per sample measures that result inside Management, subcategory K997 # Regression testing. The unit is number. The formula is A / B, where A is Cut of quality inspection, B is sample. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cut of quality inspection per sample on the desired side of its target for this period?

Inputs:

- `metric.cut-of-quality-inspection` (Cut of quality inspection)
- `metric.sample` (sample)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1683, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Utilization of Quality Assurance instruments

- id: `kpi.management.utilization-of-quality-assurance-instruments`
- kind: kpi
- unit: percent
- direction: corridor
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Utilization of Quality Assurance instruments measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is Utilization, B is Quality Assurance instruments. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Utilization of Quality Assurance instruments on the desired side of its target for this period?

Inputs:

- `metric.utilization` (Utilization)
- `metric.quality-assurance-instruments` (Quality Assurance instruments)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1684, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time spent on Quality Assurance (QA) activities to non-QA activities

- id: `kpi.management.time-spent-on-quality-assurance-qa-activities-to-non-qa-activities`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time spent on Quality Assurance (QA) activities to non-QA activities measures that result inside Management, subcategory K997 # Regression testing. The unit is count. The formula is A, where A is Time spent on Quality Assurance (QA) activities to non-QA activities. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time spent on Quality Assurance (QA) activities to non-QA activities on the desired side of its target for this period?

Inputs:

- `metric.time-spent-on-quality-assurance-qa-activities-to-non-qa-activities` (Time spent on Quality Assurance (QA) activities to non-QA activities)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1685, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Corrective actions

- id: `kpi.management.corrective-actions`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Corrective actions measures that result inside Management, subcategory K997 # Regression testing. The unit is count. The formula is A, where A is Corrective actions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Corrective actions on the desired side of its target for this period?

Inputs:

- `metric.corrective-actions` (Corrective actions)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1690, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Quality assurance reviews

- id: `kpi.management.quality-assurance-reviews`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Quality assurance reviews measures that result inside Management, subcategory K997 # Regression testing. The unit is count. The formula is A, where A is Quality assurance reviews. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Quality assurance reviews on the desired side of its target for this period?

Inputs:

- `metric.quality-assurance-reviews` (Quality assurance reviews)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1691, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Reports for quality control reviews

- id: `kpi.management.reports-for-quality-control-reviews`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Reports for quality control reviews measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is part named by Reports for quality control reviews, B is whole named by Reports for quality control reviews. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Reports for quality control reviews on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-reports-for-quality-control-reviews` (part named by Reports for quality control reviews)
- `metric.whole-named-by-reports-for-quality-control-reviews` (whole named by Reports for quality control reviews)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1692, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Production quality control projects

- id: `kpi.management.production-quality-control-projects`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Production quality control projects measures that result inside Management, subcategory K997 # Regression testing. The unit is count. The formula is A, where A is Production quality control projects. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Production quality control projects on the desired side of its target for this period?

Inputs:

- `metric.production-quality-control-projects` (Production quality control projects)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1694, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Rework time per item

- id: `kpi.management.rework-time-per-item`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Rework time per item measures that result inside Management, subcategory K997 # Regression testing. The unit is count. The formula is A / B, where A is Rework time, B is item. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Rework time per item on the desired side of its target for this period?

Inputs:

- `metric.rework-time` (Rework time)
- `metric.item` (item)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1696, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time between two quality inspections

- id: `kpi.management.time-between-two-quality-inspections`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time between two quality inspections measures that result inside Management, subcategory K997 # Regression testing. The unit is count. The formula is A, where A is Time between two quality inspections. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time between two quality inspections on the desired side of its target for this period?

Inputs:

- `metric.time-between-two-quality-inspections` (Time between two quality inspections)

Placements:

- organizational / functional / Management / K997 # Regression testing (K1698, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Quality problems attributable to design

- id: `kpi.management.quality-problems-attributable-to-design`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Quality problems attributable to design measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is Quality problems attributable, B is design. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Quality problems attributable to design on the desired side of its target for this period?

Inputs:

- `metric.quality-problems-attributable` (Quality problems attributable)
- `metric.design` (design)

Placements:

- organizational / functional / Management / K997 # Regression testing (K2149, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Processes optimized

- id: `kpi.management.processes-optimized`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Processes optimized measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is part named by Processes optimized, B is whole named by Processes optimized. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Processes optimized on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-processes-optimized` (part named by Processes optimized)
- `metric.whole-named-by-processes-optimized` (whole named by Processes optimized)

Placements:

- organizational / functional / Management / K997 # Regression testing (K2284, page_0048)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Error and rework rate

- id: `kpi.management.error-and-rework-rate`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.k997-regression-testing`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Error and rework rate measures that result inside Management, subcategory K997 # Regression testing. The unit is percent. The formula is (A / B) * 100, where A is numerator of Error and rework rate, B is base of Error and rework rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Error and rework rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-error-and-rework-rate` (numerator of Error and rework rate)
- `metric.base-of-error-and-rework-rate` (base of Error and rework rate)

Placements:

- organizational / functional / Management / K997 # Regression testing (K3305, page_0048)
- organizational / industries / Sport / Organizational » Industries (xK3305, page_0180)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
