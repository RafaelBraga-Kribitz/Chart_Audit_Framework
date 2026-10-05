# Sport / Football/Soccer

Context: organizational. Group: industries. KPIs: 27.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Season deviation standard (SD) of top five clubs over the last 15 years

- id: `kpi.management.season-deviation-standard-sd-of-top-five-clubs-over-the-last-15-years`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Season deviation standard (SD) of top five clubs over the last 15 years measures that result inside Management, subcategory General. The unit is count. The formula is A, where A is Season deviation standard (SD) of top five clubs over the last 15 years. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Season deviation standard (SD) of top five clubs over the last 15 years on the desired side of its target for this period?

Inputs:

- `metric.season-deviation-standard-sd-of-top-five-clubs-over-the-last-15-years` (Season deviation standard (SD) of top five clubs over the last 15 years)

Placements:

- organizational / functional / Management / General (%R131, page_0175)
- organizational / industries / Sport / Football/Soccer (sK4219, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Passing accuracy

- id: `kpi.sport.passing-accuracy`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.kpi-key-performance-indicator-name`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Passing accuracy measures that result inside Sport, subcategory KPI # Key Performance Indicator name. The unit is number. The formula is A, where A is Passing accuracy. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Passing accuracy on the desired side of its target for this period?

Inputs:

- `metric.passing-accuracy` (Passing accuracy)

Placements:

- organizational / industries / Sport / KPI # Key Performance Indicator name (k892, page_0177)
- organizational / industries / Sport / Football/Soccer (sK892, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Shots on target

- id: `kpi.sport.shots-on-target`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.football-soccer`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Shots on target measures that result inside Sport, subcategory Football/Soccer. The unit is percent. The formula is (A / B) * 100, where A is part named by Shots on target, B is whole named by Shots on target. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Shots on target on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-shots-on-target` (part named by Shots on target)
- `metric.whole-named-by-shots-on-target` (whole named by Shots on target)

Placements:

- organizational / industries / Sport / Football/Soccer (sK921, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Minutes per goal scored

- id: `kpi.sport.minutes-per-goal-scored`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.football-soccer`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Minutes per goal scored measures that result inside Sport, subcategory Football/Soccer. The unit is count. The formula is A / B, where A is Minutes, B is goal scored. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Minutes per goal scored on the desired side of its target for this period?

Inputs:

- `metric.minutes` (Minutes)
- `metric.goal-scored` (goal scored)

Placements:

- organizational / industries / Sport / Football/Soccer (sK922, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Chances created per game

- id: `kpi.sport.chances-created-per-game`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.football-soccer`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Chances created per game measures that result inside Sport, subcategory Football/Soccer. The unit is count. The formula is A / B, where A is Chances created, B is game. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Chances created per game on the desired side of its target for this period?

Inputs:

- `metric.chances-created` (Chances created)
- `metric.game` (game)

Placements:

- organizational / industries / Sport / Football/Soccer (sK922, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Goals created per game

- id: `kpi.sport.goals-created-per-game`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.football-soccer`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Goals created per game measures that result inside Sport, subcategory Football/Soccer. The unit is count. The formula is A / B, where A is Goals created, B is game. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Goals created per game on the desired side of its target for this period?

Inputs:

- `metric.goals-created` (Goals created)
- `metric.game` (game)

Placements:

- organizational / industries / Sport / Football/Soccer (sK932, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Goal conversion rate

- id: `kpi.sport.goal-conversion-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.football-soccer`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Goal conversion rate measures that result inside Sport, subcategory Football/Soccer. The unit is percent. The formula is (A / B) * 100, where A is numerator of Goal conversion rate, B is base of Goal conversion rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Goal conversion rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-goal-conversion-rate` (numerator of Goal conversion rate)
- `metric.base-of-goal-conversion-rate` (base of Goal conversion rate)

Placements:

- organizational / industries / Sport / Football/Soccer (sK933, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Minutes per goal conceded

- id: `kpi.sport.minutes-per-goal-conceded`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.football-soccer`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Minutes per goal conceded measures that result inside Sport, subcategory Football/Soccer. The unit is count. The formula is A / B, where A is Minutes, B is goal conceded. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Minutes per goal conceded on the desired side of its target for this period?

Inputs:

- `metric.minutes` (Minutes)
- `metric.goal-conceded` (goal conceded)

Placements:

- organizational / industries / Sport / Football/Soccer (sK939, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Catch success rate

- id: `kpi.sport.catch-success-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.football-soccer`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Catch success rate measures that result inside Sport, subcategory Football/Soccer. The unit is percent. The formula is (A / B) * 100, where A is numerator of Catch success rate, B is base of Catch success rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Catch success rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-catch-success-rate` (numerator of Catch success rate)
- `metric.base-of-catch-success-rate` (base of Catch success rate)

Placements:

- organizational / industries / Sport / Football/Soccer (sK957, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Ball possession

- id: `kpi.sport.ball-possession`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.football-soccer`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Ball possession measures that result inside Sport, subcategory Football/Soccer. The unit is percent. The formula is (A / B) * 100, where A is part named by Ball possession, B is whole named by Ball possession. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Ball possession on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-ball-possession` (part named by Ball possession)
- `metric.whole-named-by-ball-possession` (whole named by Ball possession)

Placements:

- organizational / industries / Sport / Football/Soccer (sK1119, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Shots off target

- id: `kpi.sport.shots-off-target`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.football-soccer`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Shots off target measures that result inside Sport, subcategory Football/Soccer. The unit is count. The formula is A, where A is Shots off target. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Shots off target on the desired side of its target for this period?

Inputs:

- `metric.shots-off-target` (Shots off target)

Placements:

- organizational / industries / Sport / Football/Soccer (sK1160, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Corner kicks

- id: `kpi.sport.corner-kicks`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.football-soccer`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Corner kicks measures that result inside Sport, subcategory Football/Soccer. The unit is count. The formula is A, where A is Corner kicks. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Corner kicks on the desired side of its target for this period?

Inputs:

- `metric.corner-kicks` (Corner kicks)

Placements:

- organizational / industries / Sport / Football/Soccer (sK1700, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Off sides

- id: `kpi.sport.off-sides`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.football-soccer`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Off sides measures that result inside Sport, subcategory Football/Soccer. The unit is count. The formula is A, where A is Off sides. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Off sides on the desired side of its target for this period?

Inputs:

- `metric.off-sides` (Off sides)

Placements:

- organizational / industries / Sport / Football/Soccer (sK2421, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Duels won

- id: `kpi.sport.duels-won`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.football-soccer`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Duels won measures that result inside Sport, subcategory Football/Soccer. The unit is percent. The formula is (A / B) * 100, where A is part named by Duels won, B is whole named by Duels won. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Duels won on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-duels-won` (part named by Duels won)
- `metric.whole-named-by-duels-won` (whole named by Duels won)

Placements:

- organizational / industries / Sport / Football/Soccer (sK2422, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Duels lost

- id: `kpi.sport.duels-lost`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.football-soccer`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Duels lost measures that result inside Sport, subcategory Football/Soccer. The unit is percent. The formula is (A / B) * 100, where A is part named by Duels lost, B is whole named by Duels lost. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Duels lost on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-duels-lost` (part named by Duels lost)
- `metric.whole-named-by-duels-lost` (whole named by Duels lost)

Placements:

- organizational / industries / Sport / Football/Soccer (sK2433, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Goal passes

- id: `kpi.sport.goal-passes`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.football-soccer`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Goal passes measures that result inside Sport, subcategory Football/Soccer. The unit is count. The formula is A, where A is Goal passes. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Goal passes on the desired side of its target for this period?

Inputs:

- `metric.goal-passes` (Goal passes)

Placements:

- organizational / industries / Sport / Football/Soccer (sK2434, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Level of excitement

- id: `kpi.sport.level-of-excitement`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.football-soccer`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Level of excitement measures that result inside Sport, subcategory Football/Soccer. The unit is percent. The formula is (A / B) * 100, where A is Level, B is excitement. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Level of excitement on the desired side of its target for this period?

Inputs:

- `metric.level` (Level)
- `metric.excitement` (excitement)

Placements:

- organizational / industries / Sport / Football/Soccer (sK4119, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Season standard deviation (SD)

- id: `kpi.sport.season-standard-deviation-sd`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.football-soccer`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Season standard deviation (SD) measures that result inside Sport, subcategory Football/Soccer. The unit is count. The formula is A, where A is Season standard deviation (SD). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Season standard deviation (SD) on the desired side of its target for this period?

Inputs:

- `metric.season-standard-deviation-sd` (Season standard deviation (SD))

Placements:

- organizational / industries / Sport / Football/Soccer (sK4121, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Average points obtained per season

- id: `kpi.sport.average-points-obtained-per-season`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sport.football-soccer`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Average points obtained per season measures that result inside Sport, subcategory Football/Soccer. The unit is count. The formula is A / B, where A is Average points obtained, B is season. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Average points obtained per season on the desired side of its target for this period?

Inputs:

- `metric.average-points-obtained` (Average points obtained)
- `metric.season` (season)

Placements:

- organizational / industries / Sport / Football/Soccer (sK4122, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Concentration rate (CR)

- id: `kpi.sport.concentration-rate-cr`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.football-soccer`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Concentration rate (CR) measures that result inside Sport, subcategory Football/Soccer. The unit is count. The formula is A, where A is Concentration rate (CR). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Concentration rate (CR) on the desired side of its target for this period?

Inputs:

- `metric.concentration-rate-cr` (Concentration rate (CR))

Placements:

- organizational / industries / Sport / Football/Soccer (sK4123, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Ratio of concentration rates (CRs)

- id: `kpi.sport.ratio-of-concentration-rates-crs`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.football-soccer`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Ratio of concentration rates (CRs) measures that result inside Sport, subcategory Football/Soccer. The unit is count. The formula is A, where A is Ratio of concentration rates (CRs). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Ratio of concentration rates (CRs) on the desired side of its target for this period?

Inputs:

- `metric.ratio-of-concentration-rates-crs` (Ratio of concentration rates (CRs))

Placements:

- organizational / industries / Sport / Football/Soccer (sK4128, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Competition level for the champion title

- id: `kpi.sport.competition-level-for-the-champion-title`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sport.football-soccer`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Competition level for the champion title measures that result inside Sport, subcategory Football/Soccer. The unit is count. The formula is A, where A is Competition level for the champion title. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Competition level for the champion title on the desired side of its target for this period?

Inputs:

- `metric.competition-level-for-the-champion-title` (Competition level for the champion title)

Placements:

- organizational / industries / Sport / Football/Soccer (sK4134, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Qualification success

- id: `kpi.sport.qualification-success`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.football-soccer`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Qualification success measures that result inside Sport, subcategory Football/Soccer. The unit is percent. The formula is (A / B) * 100, where A is part named by Qualification success, B is whole named by Qualification success. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Qualification success on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-qualification-success` (part named by Qualification success)
- `metric.whole-named-by-qualification-success` (whole named by Qualification success)

Placements:

- organizational / industries / Sport / Football/Soccer (sK4135, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### UEFA Champions League qualification success concentration ratio

- id: `kpi.sport.uefa-champions-league-qualification-success-concentration-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.football-soccer`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

UEFA Champions League qualification success concentration ratio measures that result inside Sport, subcategory Football/Soccer. The unit is percent. The formula is (A / B) * 100, where A is numerator of UEFA Champions League qualification success concentration ratio, B is base of UEFA Champions League qualification success concentration ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is UEFA Champions League qualification success concentration ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-uefa-champions-league-qualification-success-concentration-r` (numerator of UEFA Champions League qualification success concentration ratio)
- `metric.base-of-uefa-champions-league-qualification-success-concentration-ratio` (base of UEFA Champions League qualification success concentration ratio)

Placements:

- organizational / industries / Sport / Football/Soccer (sK4136, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Swift relegation rate

- id: `kpi.sport.swift-relegation-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.football-soccer`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Swift relegation rate measures that result inside Sport, subcategory Football/Soccer. The unit is percent. The formula is (A / B) * 100, where A is numerator of Swift relegation rate, B is base of Swift relegation rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Swift relegation rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-swift-relegation-rate` (numerator of Swift relegation rate)
- `metric.base-of-swift-relegation-rate` (base of Swift relegation rate)

Placements:

- organizational / industries / Sport / Football/Soccer (sK4137, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Volatility among top five clubs

- id: `kpi.sport.volatility-among-top-five-clubs`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.football-soccer`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Volatility among top five clubs measures that result inside Sport, subcategory Football/Soccer. The unit is percent. The formula is (A / B) * 100, where A is part named by Volatility among top five clubs, B is whole named by Volatility among top five clubs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Volatility among top five clubs on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-volatility-among-top-five-clubs` (part named by Volatility among top five clubs)
- `metric.whole-named-by-volatility-among-top-five-clubs` (whole named by Volatility among top five clubs)

Placements:

- organizational / industries / Sport / Football/Soccer (sK4138, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Volatility among bottom three clubs

- id: `kpi.sport.volatility-among-bottom-three-clubs`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sport.football-soccer`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Volatility among bottom three clubs measures that result inside Sport, subcategory Football/Soccer. The unit is percent. The formula is (A / B) * 100, where A is part named by Volatility among bottom three clubs, B is whole named by Volatility among bottom three clubs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Volatility among bottom three clubs on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-volatility-among-bottom-three-clubs` (part named by Volatility among bottom three clubs)
- `metric.whole-named-by-volatility-among-bottom-three-clubs` (whole named by Volatility among bottom three clubs)

Placements:

- organizational / industries / Sport / Football/Soccer (sK4141, page_0178)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
