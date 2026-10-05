# Marketing and Communications / Spend

Context: organizational. Group: functional. KPIs: 1.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Marketing spend to gross profit

- id: `kpi.marketing-and-communications.marketing-spend-to-gross-profit`
- kind: kpi
- unit: percent
- direction: corridor
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.marketing-and-communications.spend`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Marketing spend as a share of gross profit. Placed under Marketing and Communications / Spend.

Questions: Is Marketing spend to gross profit on the desired side of its target for this period?

Inputs:

- `metric.marketing-spend` (marketing spend)
- `metric.gross-profit` (gross profit)

Placements:

- organizational / functional / Marketing and Communications / Spend (user-note, note)

Target notes:

- Published agency rule of thumb: marketing spend around 5 to 10 percent of gross profit.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.
