# Infrastructure / POTS

Context: organizational. Group: industries. KPIs: 9.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### J-Major shipping lines in port

- id: `kpi.infrastructure.j-major-shipping-lines-in-port`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.pots`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

J-Major shipping lines in port measures that result inside Infrastructure, subcategory POTS. The unit is number. The formula is A, where A is J-Major shipping lines in port. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is J-Major shipping lines in port on the desired side of its target for this period?

Inputs:

- `metric.j-major-shipping-lines-in-port` (J-Major shipping lines in port)

Placements:

- organizational / industries / Infrastructure / POTS (kKP11, page_0137)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### J-Turquoise union

- id: `kpi.infrastructure.j-turquoise-union`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.pots`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

J-Turquoise union measures that result inside Infrastructure, subcategory POTS. The unit is number. The formula is A, where A is J-Turquoise union. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is J-Turquoise union on the desired side of its target for this period?

Inputs:

- `metric.j-turquoise-union` (J-Turquoise union)

Placements:

- organizational / industries / Infrastructure / POTS (kK280, page_0137)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### P-Turquoise handled per ship/day in port

- id: `kpi.infrastructure.p-turquoise-handled-per-ship-day-in-port`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.infrastructure.pots`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

P-Turquoise handled per ship/day in port measures that result inside Infrastructure, subcategory POTS. The unit is number. The formula is A / B, where A is P-Turquoise handled, B is ship/day in port. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is P-Turquoise handled per ship/day in port on the desired side of its target for this period?

Inputs:

- `metric.p-turquoise-handled` (P-Turquoise handled)
- `metric.ship-day-in-port` (ship/day in port)

Placements:

- organizational / industries / Infrastructure / POTS (kK2807, page_0137)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Life time due to train

- id: `kpi.infrastructure.life-time-due-to-train`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.pots`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Life time due to train measures that result inside Infrastructure, subcategory POTS. The unit is count. The formula is A, where A is Life time due to train. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Life time due to train on the desired side of its target for this period?

Inputs:

- `metric.life-time-due-to-train` (Life time due to train)

Placements:

- organizational / industries / Infrastructure / POTS (kK3089, page_0137)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Berth utilization rate

- id: `kpi.infrastructure.berth-utilization-rate`
- kind: kpi
- unit: count
- direction: corridor
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.pots`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Berth utilization rate measures that result inside Infrastructure, subcategory POTS. The unit is count. The formula is A, where A is Berth utilization rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Berth utilization rate on the desired side of its target for this period?

Inputs:

- `metric.berth-utilization-rate` (Berth utilization rate)

Placements:

- organizational / industries / Infrastructure / POTS (kK1014, page_0137)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Container freight stations

- id: `kpi.infrastructure.container-freight-stations`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.pots`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Container freight stations measures that result inside Infrastructure, subcategory POTS. The unit is count. The formula is A, where A is Container freight stations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Container freight stations on the desired side of its target for this period?

Inputs:

- `metric.container-freight-stations` (Container freight stations)

Placements:

- organizational / industries / Infrastructure / POTS (kK3215, page_0137)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Positive measures in force due to skylams in presence of documents

- id: `kpi.infrastructure.positive-measures-in-force-due-to-skylams-in-presence-of-documents`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.pots`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Positive measures in force due to skylams in presence of documents measures that result inside Infrastructure, subcategory POTS. The unit is count. The formula is A, where A is Positive measures in force due to skylams in presence of documents. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Positive measures in force due to skylams in presence of documents on the desired side of its target for this period?

Inputs:

- `metric.positive-measures-in-force-due-to-skylams-in-presence-of-documents` (Positive measures in force due to skylams in presence of documents)

Placements:

- organizational / industries / Infrastructure / POTS (kK2723, page_0137)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Part state control (PSC inspected ships

- id: `kpi.infrastructure.part-state-control-psc-inspected-ships`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.pots`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Part state control (PSC inspected ships measures that result inside Infrastructure, subcategory POTS. The unit is count. The formula is A, where A is Part state control (PSC inspected ships. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Part state control (PSC inspected ships on the desired side of its target for this period?

Inputs:

- `metric.part-state-control-psc-inspected-ships` (Part state control (PSC inspected ships)

Placements:

- organizational / industries / Infrastructure / POTS (kK2487, page_0137)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Job-dependency directly and indirectly on the port

- id: `kpi.infrastructure.job-dependency-directly-and-indirectly-on-the-port`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.infrastructure.pots`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Job-dependency directly and indirectly on the port measures that result inside Infrastructure, subcategory POTS. The unit is count. The formula is A, where A is Job-dependency directly and indirectly on the port. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Job-dependency directly and indirectly on the port on the desired side of its target for this period?

Inputs:

- `metric.job-dependency-directly-and-indirectly-on-the-port` (Job-dependency directly and indirectly on the port)

Placements:

- organizational / industries / Infrastructure / POTS (kK2713, page_0137)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
