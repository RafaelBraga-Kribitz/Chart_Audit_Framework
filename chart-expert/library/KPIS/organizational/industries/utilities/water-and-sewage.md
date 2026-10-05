# Utilities / Water and Sewage

Context: organizational. Group: industries. KPIs: 54.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Gross volume of water resource available

- id: `kpi.administration.gross-volume-of-water-resource-available`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Gross volume of water resource available measures that result inside Administration, subcategory Organizational + Industries. The unit is count. The formula is A, where A is Gross volume of water resource available. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Gross volume of water resource available on the desired side of its target for this period?

Inputs:

- `metric.gross-volume-of-water-resource-available` (Gross volume of water resource available)

Placements:

- organizational / functional / Administration / Organizational + Industries (sK89B9, page_0093)
- organizational / industries / Utilities / Water and Sewage (xK4979, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Water connection rate

- id: `kpi.administration.water-connection-rate`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Water connection rate measures that result inside Administration, subcategory Organizational + Industries. The unit is count. The formula is A, where A is Water connection rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Water connection rate on the desired side of its target for this period?

Inputs:

- `metric.water-connection-rate` (Water connection rate)

Placements:

- organizational / functional / Administration / Organizational + Industries (sK89B8, page_0093)
- organizational / industries / Utilities / Water and Sewage (xK4980, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Population with access to piped water

- id: `kpi.administration.population-with-access-to-piped-water`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Population with access to piped water measures that result inside Administration, subcategory Organizational + Industries. The unit is count. The formula is A, where A is Population with access to piped water. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Population with access to piped water on the desired side of its target for this period?

Inputs:

- `metric.population-with-access-to-piped-water` (Population with access to piped water)

Placements:

- organizational / functional / Administration / Organizational + Industries (sK85D10, page_0093)
- organizational / industries / Utilities / Water and Sewage (xK5010, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Households with access to safe water

- id: `kpi.resources.households-with-access-to-safe-water`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.resources.organizational-industries`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Households with access to safe water measures that result inside Resources, subcategory Organizational » Industries. The unit is percent. The formula is (A / B) * 100, where A is Households with access, B is safe water. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Households with access to safe water on the desired side of its target for this period?

Inputs:

- `metric.households-with-access` (Households with access)
- `metric.safe-water` (safe water)

Placements:

- organizational / industries / Resources / Organizational » Industries (sK5015, page_0108)
- organizational / industries / Utilities / Water and Sewage (xK5011, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Consumers hours of supply per 1000 customers

- id: `kpi.utilities.consumers-hours-of-supply-per-1000-customers`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.utilities.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Consumers hours of supply per 1000 customers measures that result inside Utilities, subcategory Organizational > Industries. The unit is count. The formula is A / B, where A is Consumers hours of supply, B is 1000 customers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Consumers hours of supply per 1000 customers on the desired side of its target for this period?

Inputs:

- `metric.consumers-hours-of-supply` (Consumers hours of supply)
- `metric.1000-customers` (1000 customers)

Placements:

- organizational / industries / Utilities / Organizational > Industries (▲K4931, page_0200)
- organizational / industries / Utilities / Water and Sewage (xK4933, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Utility customer density

- id: `kpi.utilities.utility-customer-density`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.utilities.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Utility customer density measures that result inside Utilities, subcategory Organizational > Industries. The unit is count. The formula is A, where A is Utility customer density. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Utility customer density on the desired side of its target for this period?

Inputs:

- `metric.utility-customer-density` (Utility customer density)

Placements:

- organizational / industries / Utilities / Organizational > Industries (▲K4882, page_0200)
- organizational / industries / Utilities / Water and Sewage (xK4882, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Accounts receivable in days of utility bill equivalent

- id: `kpi.utilities.accounts-receivable-in-days-of-utility-bill-equivalent`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.utilities.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Accounts receivable in days of utility bill equivalent measures that result inside Utilities, subcategory Organizational > Industries. The unit is count. The formula is A, where A is Accounts receivable in days of utility bill equivalent. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Accounts receivable in days of utility bill equivalent on the desired side of its target for this period?

Inputs:

- `metric.accounts-receivable-in-days-of-utility-bill-equivalent` (Accounts receivable in days of utility bill equivalent)

Placements:

- organizational / industries / Utilities / Organizational > Industries (▲K4885, page_0200)
- organizational / industries / Utilities / Water and Sewage (xK4885, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Residential connections with an operating meter

- id: `kpi.utilities.residential-connections-with-an-operating-meter`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.utilities.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Residential connections with an operating meter measures that result inside Utilities, subcategory Organizational > Industries. The unit is count. The formula is A, where A is Residential connections with an operating meter. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Residential connections with an operating meter on the desired side of its target for this period?

Inputs:

- `metric.residential-connections-with-an-operating-meter` (Residential connections with an operating meter)

Placements:

- organizational / industries / Utilities / Organizational > Industries (▲K4898, page_0200)
- organizational / industries / Utilities / Water and Sewage (xK498, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Residual household waste per household

- id: `kpi.utilities.residual-household-waste-per-household`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Residual household waste per household measures that result inside Utilities, subcategory Water and Sewage. The unit is count. The formula is A / B, where A is Residual household waste, B is household. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Residual household waste per household on the desired side of its target for this period?

Inputs:

- `metric.residual-household-waste` (Residual household waste)
- `metric.household` (household)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK180, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Water consumption per capita

- id: `kpi.utilities.water-consumption-per-capita`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Water consumption per capita measures that result inside Utilities, subcategory Water and Sewage. The unit is count. The formula is A / B, where A is Water consumption, B is capita. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Water consumption per capita on the desired side of its target for this period?

Inputs:

- `metric.water-consumption` (Water consumption)
- `metric.capita` (capita)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK184, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Supplied water volume per person

- id: `kpi.utilities.supplied-water-volume-per-person`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Supplied water volume per person measures that result inside Utilities, subcategory Water and Sewage. The unit is count. The formula is A / B, where A is Supplied water volume, B is person. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Supplied water volume per person on the desired side of its target for this period?

Inputs:

- `metric.supplied-water-volume` (Supplied water volume)
- `metric.person` (person)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK185, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sewage treatment capacity sufficiency

- id: `kpi.utilities.sewage-treatment-capacity-sufficiency`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Sewage treatment capacity sufficiency measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is part named by Sewage treatment capacity sufficiency, B is whole named by Sewage treatment capacity sufficiency. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sewage treatment capacity sufficiency on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-sewage-treatment-capacity-sufficiency` (part named by Sewage treatment capacity sufficiency)
- `metric.whole-named-by-sewage-treatment-capacity-sufficiency` (whole named by Sewage treatment capacity sufficiency)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK1011, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Amount of water hot before any use for the consumers

- id: `kpi.utilities.amount-of-water-hot-before-any-use-for-the-consumers`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Amount of water hot before any use for the consumers measures that result inside Utilities, subcategory Water and Sewage. The unit is count. The formula is A, where A is Amount of water hot before any use for the consumers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Amount of water hot before any use for the consumers on the desired side of its target for this period?

Inputs:

- `metric.amount-of-water-hot-before-any-use-for-the-consumers` (Amount of water hot before any use for the consumers)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK124, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Utility service bill collection rates

- id: `kpi.utilities.utility-service-bill-collection-rates`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Utility service bill collection rates measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is numerator of Utility service bill collection rates, B is base of Utility service bill collection rates. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Utility service bill collection rates on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-utility-service-bill-collection-rates` (numerator of Utility service bill collection rates)
- `metric.base-of-utility-service-bill-collection-rates` (base of Utility service bill collection rates)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK484, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Defective meters replaced

- id: `kpi.utilities.defective-meters-replaced`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Defective meters replaced measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is part named by Defective meters replaced, B is whole named by Defective meters replaced. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Defective meters replaced on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-defective-meters-replaced` (part named by Defective meters replaced)
- `metric.whole-named-by-defective-meters-replaced` (whole named by Defective meters replaced)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4914, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Meters per meter reader

- id: `kpi.utilities.meters-per-meter-reader`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Meters per meter reader measures that result inside Utilities, subcategory Water and Sewage. The unit is count. The formula is A / B, where A is Meters, B is meter reader. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Meters per meter reader on the desired side of its target for this period?

Inputs:

- `metric.meters` (Meters)
- `metric.meter-reader` (meter reader)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4915, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Completed meter readings per meter reader

- id: `kpi.utilities.completed-meter-readings-per-meter-reader`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Completed meter readings per meter reader measures that result inside Utilities, subcategory Water and Sewage. The unit is count. The formula is A / B, where A is Completed meter readings, B is meter reader. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Completed meter readings per meter reader on the desired side of its target for this period?

Inputs:

- `metric.completed-meter-readings` (Completed meter readings)
- `metric.meter-reader` (meter reader)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4916, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Active utility meters

- id: `kpi.utilities.active-utility-meters`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Active utility meters measures that result inside Utilities, subcategory Water and Sewage. The unit is count. The formula is A, where A is Active utility meters. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Active utility meters on the desired side of its target for this period?

Inputs:

- `metric.active-utility-meters` (Active utility meters)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4949, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Utility service账单 collection requests

- id: `kpi.utilities.utility-service-collection-requests`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Utility service账单 collection requests measures that result inside Utilities, subcategory Water and Sewage. The unit is count. The formula is A, where A is Utility service账单 collection requests. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Utility service账单 collection requests on the desired side of its target for this period?

Inputs:

- `metric.utility-service-collection-requests` (Utility service账单 collection requests)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4962, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Utility service connection status requests

- id: `kpi.utilities.utility-service-connection-status-requests`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Utility service connection status requests measures that result inside Utilities, subcategory Water and Sewage. The unit is count. The formula is A, where A is Utility service connection status requests. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Utility service connection status requests on the desired side of its target for this period?

Inputs:

- `metric.utility-service-connection-status-requests` (Utility service connection status requests)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4963, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Utility meters consolidation requests

- id: `kpi.utilities.utility-meters-consolidation-requests`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Utility meters consolidation requests measures that result inside Utilities, subcategory Water and Sewage. The unit is count. The formula is A, where A is Utility meters consolidation requests. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Utility meters consolidation requests on the desired side of its target for this period?

Inputs:

- `metric.utility-meters-consolidation-requests` (Utility meters consolidation requests)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4965, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Functional meters

- id: `kpi.utilities.functional-meters`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Functional meters measures that result inside Utilities, subcategory Water and Sewage. The unit is count. The formula is A, where A is Functional meters. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Functional meters on the desired side of its target for this period?

Inputs:

- `metric.functional-meters` (Functional meters)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK496, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unplanned water interruptions per property

- id: `kpi.utilities.unplanned-water-interruptions-per-property`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Unplanned water interruptions per property measures that result inside Utilities, subcategory Water and Sewage. The unit is count. The formula is A / B, where A is Unplanned water interruptions, B is property. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unplanned water interruptions per property on the desired side of its target for this period?

Inputs:

- `metric.unplanned-water-interruptions` (Unplanned water interruptions)
- `metric.property` (property)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4969, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Households with reliable supply of water

- id: `kpi.utilities.households-with-reliable-supply-of-water`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Households with reliable supply of water measures that result inside Utilities, subcategory Water and Sewage. The unit is count. The formula is A, where A is Households with reliable supply of water. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Households with reliable supply of water on the desired side of its target for this period?

Inputs:

- `metric.households-with-reliable-supply-of-water` (Households with reliable supply of water)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4971, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Properties that experienced an unplanned water interruption

- id: `kpi.utilities.properties-that-experienced-an-unplanned-water-interruption`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Properties that experienced an unplanned water interruption measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is part named by Properties that experienced an unplanned water interruption, B is whole named by Properties that experienced an unplanned water interruption. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Properties that experienced an unplanned water interruption on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-properties-that-experienced-an-unplanned-water-interruptio` (part named by Properties that experienced an unplanned water interruption)
- `metric.whole-named-by-properties-that-experienced-an-unplanned-water-interrupti` (whole named by Properties that experienced an unplanned water interruption)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4972, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Water supply continuity

- id: `kpi.utilities.water-supply-continuity`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Water supply continuity measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is part named by Water supply continuity, B is whole named by Water supply continuity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Water supply continuity on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-water-supply-continuity` (part named by Water supply continuity)
- `metric.whole-named-by-water-supply-continuity` (whole named by Water supply continuity)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4973, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Drinking water compliance rate

- id: `kpi.utilities.drinking-water-compliance-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Drinking water compliance rate measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is numerator of Drinking water compliance rate, B is base of Drinking water compliance rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Drinking water compliance rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-drinking-water-compliance-rate` (numerator of Drinking water compliance rate)
- `metric.base-of-drinking-water-compliance-rate` (base of Drinking water compliance rate)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4974, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Incidents of sewer flooding

- id: `kpi.utilities.incidents-of-sewer-flooding`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Incidents of sewer flooding measures that result inside Utilities, subcategory Water and Sewage. The unit is count. The formula is A, where A is Incidents of sewer flooding. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Incidents of sewer flooding on the desired side of its target for this period?

Inputs:

- `metric.incidents-of-sewer-flooding` (Incidents of sewer flooding)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4975, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Properties affected by low water pressure

- id: `kpi.utilities.properties-affected-by-low-water-pressure`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Properties affected by low water pressure measures that result inside Utilities, subcategory Water and Sewage. The unit is count. The formula is A, where A is Properties affected by low water pressure. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Properties affected by low water pressure on the desired side of its target for this period?

Inputs:

- `metric.properties-affected-by-low-water-pressure` (Properties affected by low water pressure)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4976, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Length of sewer pipes removed

- id: `kpi.utilities.length-of-sewer-pipes-removed`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Length of sewer pipes removed measures that result inside Utilities, subcategory Water and Sewage. The unit is count. The formula is A, where A is Length of sewer pipes removed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Length of sewer pipes removed on the desired side of its target for this period?

Inputs:

- `metric.length-of-sewer-pipes-removed` (Length of sewer pipes removed)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4977, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Daily water demand consumption per capita

- id: `kpi.utilities.daily-water-demand-consumption-per-capita`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Daily water demand consumption per capita measures that result inside Utilities, subcategory Water and Sewage. The unit is count. The formula is A / B, where A is Daily water demand consumption, B is capita. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Daily water demand consumption per capita on the desired side of its target for this period?

Inputs:

- `metric.daily-water-demand-consumption` (Daily water demand consumption)
- `metric.capita` (capita)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4978, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Urban rainwater treatment rate

- id: `kpi.utilities.urban-rainwater-treatment-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Urban rainwater treatment rate measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is numerator of Urban rainwater treatment rate, B is base of Urban rainwater treatment rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Urban rainwater treatment rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-urban-rainwater-treatment-rate` (numerator of Urban rainwater treatment rate)
- `metric.base-of-urban-rainwater-treatment-rate` (base of Urban rainwater treatment rate)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4981, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Industrial wastewater treatment rate

- id: `kpi.utilities.industrial-wastewater-treatment-rate`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Industrial wastewater treatment rate measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is numerator of Industrial wastewater treatment rate, B is base of Industrial wastewater treatment rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Industrial wastewater treatment rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-industrial-wastewater-treatment-rate` (numerator of Industrial wastewater treatment rate)
- `metric.base-of-industrial-wastewater-treatment-rate` (base of Industrial wastewater treatment rate)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4982, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Properties that experienced a planned water interruption since year but no fallaround sweet treatment plants (STPs) and ocean STPs

- id: `kpi.utilities.properties-that-experienced-a-planned-water-interruption-since-year-but`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Properties that experienced a planned water interruption since year but no fallaround sweet treatment plants (STPs) and ocean STPs measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is part named by Properties that experienced a planned water interruption since year but no fallaround sweet treatment plants (STPs) and ocean STPs, B is whole named by Properties that experienced a planned water interruption since year but no fallaround sweet treatment plants (STPs) and ocean STPs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Properties that experienced a planned water interruption since year but no fallaround sweet treatment plants (STPs) and ocean STPs on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-properties-that-experienced-a-planned-water-interruption-s` (part named by Properties that experienced a planned water interruption since year but no fallaround sweet treatment plants (STPs) and ocean STPs)
- `metric.whole-named-by-properties-that-experienced-a-planned-water-interruption` (whole named by Properties that experienced a planned water interruption since year but no fallaround sweet treatment plants (STPs) and ocean STPs)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4983, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Water biosolid residuals produced and recured

- id: `kpi.utilities.water-biosolid-residuals-produced-and-recured`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Water biosolid residuals produced and recured measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is part named by Water biosolid residuals produced and recured, B is whole named by Water biosolid residuals produced and recured. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Water biosolid residuals produced and recured on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-water-biosolid-residuals-produced-and-recured` (part named by Water biosolid residuals produced and recured)
- `metric.whole-named-by-water-biosolid-residuals-produced-and-recured` (whole named by Water biosolid residuals produced and recured)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4985, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Water levels that meet the industry water guidelines and standards

- id: `kpi.utilities.water-levels-that-meet-the-industry-water-guidelines-and-standards`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Water levels that meet the industry water guidelines and standards measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is part named by Water levels that meet the industry water guidelines and standards, B is whole named by Water levels that meet the industry water guidelines and standards. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Water levels that meet the industry water guidelines and standards on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-water-levels-that-meet-the-industry-water-guidelines-and-s` (part named by Water levels that meet the industry water guidelines and standards)
- `metric.whole-named-by-water-levels-that-meet-the-industry-water-guidelines-and` (whole named by Water levels that meet the industry water guidelines and standards)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4988, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Compliance with water health guideline values

- id: `kpi.utilities.compliance-with-water-health-guideline-values`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Compliance with water health guideline values measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is part named by Compliance with water health guideline values, B is whole named by Compliance with water health guideline values. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Compliance with water health guideline values on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-compliance-with-water-health-guideline-values` (part named by Compliance with water health guideline values)
- `metric.whole-named-by-compliance-with-water-health-guideline-values` (whole named by Compliance with water health guideline values)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4989, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Compliance with water aesthetic guideline values

- id: `kpi.utilities.compliance-with-water-aesthetic-guideline-values`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Compliance with water aesthetic guideline values measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is part named by Compliance with water aesthetic guideline values, B is whole named by Compliance with water aesthetic guideline values. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Compliance with water aesthetic guideline values on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-compliance-with-water-aesthetic-guideline-values` (part named by Compliance with water aesthetic guideline values)
- `metric.whole-named-by-compliance-with-water-aesthetic-guideline-values` (whole named by Compliance with water aesthetic guideline values)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4990, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Drinking water saved on account of demand management program

- id: `kpi.utilities.drinking-water-saved-on-account-of-demand-management-program`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Drinking water saved on account of demand management program measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is Drinking water saved on account, B is demand management program. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Drinking water saved on account of demand management program on the desired side of its target for this period?

Inputs:

- `metric.drinking-water-saved-on-account` (Drinking water saved on account)
- `metric.demand-management-program` (demand management program)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4991, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Beach watch and harbor-watch sites complying with swimming water quality guidelines

- id: `kpi.utilities.beach-watch-and-harbor-watch-sites-complying-with-swimming-water-quality`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Beach watch and harbor-watch sites complying with swimming water quality guidelines measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is part named by Beach watch and harbor-watch sites complying with swimming water quality guidelines, B is whole named by Beach watch and harbor-watch sites complying with swimming water quality guidelines. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Beach watch and harbor-watch sites complying with swimming water quality guidelines on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-beach-watch-and-harbor-watch-sites-complying-with-swimming` (part named by Beach watch and harbor-watch sites complying with swimming water quality guidelines)
- `metric.whole-named-by-beach-watch-and-harbor-watch-sites-complying-with-swimmin` (whole named by Beach watch and harbor-watch sites complying with swimming water quality guidelines)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4995, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Mass of phosphorus discharged to rivers from inland water treatment plants

- id: `kpi.utilities.mass-of-phosphorus-discharged-to-rivers-from-inland-water-treatment-plan`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Mass of phosphorus discharged to rivers from inland water treatment plants measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is Mass, B is phosphorus discharged to rivers from inland water treatment plants. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Mass of phosphorus discharged to rivers from inland water treatment plants on the desired side of its target for this period?

Inputs:

- `metric.mass` (Mass)
- `metric.phosphorus-discharged-to-rivers-from-inland-water-treatment-plants` (phosphorus discharged to rivers from inland water treatment plants)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK4999, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Mass of unregistered discharges to rivers from inland water treatment plants

- id: `kpi.utilities.mass-of-unregistered-discharges-to-rivers-from-inland-water-treatment-pl`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Mass of unregistered discharges to rivers from inland water treatment plants measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is Mass, B is unregistered discharges to rivers from inland water treatment plants. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Mass of unregistered discharges to rivers from inland water treatment plants on the desired side of its target for this period?

Inputs:

- `metric.mass` (Mass)
- `metric.unregistered-discharges-to-rivers-from-inland-water-treatment-plants` (unregistered discharges to rivers from inland water treatment plants)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK5000, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Mass of unregistered solids discharged from ocean sewage treatment plants

- id: `kpi.utilities.mass-of-unregistered-solids-discharged-from-ocean-sewage-treatment-plant`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Mass of unregistered solids discharged from ocean sewage treatment plants measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is Mass, B is unregistered solids discharged from ocean sewage treatment plants. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Mass of unregistered solids discharged from ocean sewage treatment plants on the desired side of its target for this period?

Inputs:

- `metric.mass` (Mass)
- `metric.unregistered-solids-discharged-from-ocean-sewage-treatment-plants` (unregistered solids discharged from ocean sewage treatment plants)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK5001, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Mass of grease discharged from ocean sewage treatment plants

- id: `kpi.utilities.mass-of-grease-discharged-from-ocean-sewage-treatment-plants`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Mass of grease discharged from ocean sewage treatment plants measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is Mass, B is grease discharged from ocean sewage treatment plants. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Mass of grease discharged from ocean sewage treatment plants on the desired side of its target for this period?

Inputs:

- `metric.mass` (Mass)
- `metric.grease-discharged-from-ocean-sewage-treatment-plants` (grease discharged from ocean sewage treatment plants)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK5002, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Controlled sewage overflow that occurs in dry or wet weather

- id: `kpi.utilities.controlled-sewage-overflow-that-occurs-in-dry-or-wet-weather`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Controlled sewage overflow that occurs in dry or wet weather measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is part named by Controlled sewage overflow that occurs in dry or wet weather, B is whole named by Controlled sewage overflow that occurs in dry or wet weather. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Controlled sewage overflow that occurs in dry or wet weather on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-controlled-sewage-overflow-that-occurs-in-dry-or-wet-weath` (part named by Controlled sewage overflow that occurs in dry or wet weather)
- `metric.whole-named-by-controlled-sewage-overflow-that-occurs-in-dry-or-wet-weat` (whole named by Controlled sewage overflow that occurs in dry or wet weather)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK5003, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Treated wastewater discharged in the environment

- id: `kpi.utilities.treated-wastewater-discharged-in-the-environment`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Treated wastewater discharged in the environment measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is part named by Treated wastewater discharged in the environment, B is whole named by Treated wastewater discharged in the environment. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Treated wastewater discharged in the environment on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-treated-wastewater-discharged-in-the-environment` (part named by Treated wastewater discharged in the environment)
- `metric.whole-named-by-treated-wastewater-discharged-in-the-environment` (whole named by Treated wastewater discharged in the environment)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK5004, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Wastewater reused or prevented from entering waterways

- id: `kpi.utilities.wastewater-reused-or-prevented-from-entering-waterways`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Wastewater reused or prevented from entering waterways measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is Wastewater reused or prevented, B is entering waterways. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Wastewater reused or prevented from entering waterways on the desired side of its target for this period?

Inputs:

- `metric.wastewater-reused-or-prevented` (Wastewater reused or prevented)
- `metric.entering-waterways` (entering waterways)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK5005, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Properties affected by uncontrolled sewage water reuse

- id: `kpi.utilities.properties-affected-by-uncontrolled-sewage-water-reuse`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Properties affected by uncontrolled sewage water reuse measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is part named by Properties affected by uncontrolled sewage water reuse, B is whole named by Properties affected by uncontrolled sewage water reuse. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Properties affected by uncontrolled sewage water reuse on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-properties-affected-by-uncontrolled-sewage-water-reuse` (part named by Properties affected by uncontrolled sewage water reuse)
- `metric.whole-named-by-properties-affected-by-uncontrolled-sewage-water-reuse` (whole named by Properties affected by uncontrolled sewage water reuse)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK5006, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Properties affected by repeat sewage overflows

- id: `kpi.utilities.properties-affected-by-repeat-sewage-overflows`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Properties affected by repeat sewage overflows measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is part named by Properties affected by repeat sewage overflows, B is whole named by Properties affected by repeat sewage overflows. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Properties affected by repeat sewage overflows on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-properties-affected-by-repeat-sewage-overflows` (part named by Properties affected by repeat sewage overflows)
- `metric.whole-named-by-properties-affected-by-repeat-sewage-overflows` (whole named by Properties affected by repeat sewage overflows)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK5007, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Response time to sewage overflows

- id: `kpi.utilities.response-time-to-sewage-overflows`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Response time to sewage overflows measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is Response time, B is sewage overflows. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Response time to sewage overflows on the desired side of its target for this period?

Inputs:

- `metric.response-time` (Response time)
- `metric.sewage-overflows` (sewage overflows)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK5008, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Frequency of sewer main breaks and blockages per 1,000 properties

- id: `kpi.utilities.frequency-of-sewer-main-breaks-and-blockages-per-1-000-properties`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Frequency of sewer main breaks and blockages per 1,000 properties measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is A / B, where A is Frequency of sewer main breaks and blockages, B is 1,000 properties. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Frequency of sewer main breaks and blockages per 1,000 properties on the desired side of its target for this period?

Inputs:

- `metric.frequency-of-sewer-main-breaks-and-blockages` (Frequency of sewer main breaks and blockages)
- `metric.1-000-properties` (1,000 properties)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK5009, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Non residential water connections

- id: `kpi.utilities.non-residential-water-connections`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Non residential water connections measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is part named by Non residential water connections, B is whole named by Non residential water connections. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Non residential water connections on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-non-residential-water-connections` (part named by Non residential water connections)
- `metric.whole-named-by-non-residential-water-connections` (whole named by Non residential water connections)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK5012, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Residential sewerage connections

- id: `kpi.utilities.residential-sewerage-connections`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Residential sewerage connections measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is part named by Residential sewerage connections, B is whole named by Residential sewerage connections. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Residential sewerage connections on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-residential-sewerage-connections` (part named by Residential sewerage connections)
- `metric.whole-named-by-residential-sewerage-connections` (whole named by Residential sewerage connections)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK5017, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Non residential sewerage connections

- id: `kpi.utilities.non-residential-sewerage-connections`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.utilities.water-and-sewage`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Non residential sewerage connections measures that result inside Utilities, subcategory Water and Sewage. The unit is percent. The formula is (A / B) * 100, where A is part named by Non residential sewerage connections, B is whole named by Non residential sewerage connections. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Non residential sewerage connections on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-non-residential-sewerage-connections` (part named by Non residential sewerage connections)
- `metric.whole-named-by-non-residential-sewerage-connections` (whole named by Non residential sewerage connections)

Placements:

- organizational / industries / Utilities / Water and Sewage (xK5019, page_0205)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
