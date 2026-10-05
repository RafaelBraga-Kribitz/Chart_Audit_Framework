# Administration / Local Public Safety

Context: organizational. Group: industries. KPIs: 53.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Crimes against visitors

- id: `kpi.administration.crimes-against-visitors`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Crimes against visitors measures that result inside Administration, subcategory Local Public Safety. The unit is percent. The formula is (A / B) * 100, where A is part named by Crimes against visitors, B is whole named by Crimes against visitors. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Crimes against visitors on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-crimes-against-visitors` (part named by Crimes against visitors)
- `metric.whole-named-by-crimes-against-visitors` (whole named by Crimes against visitors)

Placements:

- organizational / industries / Administration / Local Public Safety (sK211, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Domestic burglaries per 1,000 households

- id: `kpi.administration.domestic-burglaries-per-1-000-households`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Domestic burglaries per 1,000 households measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A / B, where A is Domestic burglaries, B is 1,000 households. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Domestic burglaries per 1,000 households on the desired side of its target for this period?

Inputs:

- `metric.domestic-burglaries` (Domestic burglaries)
- `metric.1-000-households` (1,000 households)

Placements:

- organizational / industries / Administration / Local Public Safety (sK558, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Incidents satisfactorily managed

- id: `kpi.administration.incidents-satisfactorily-managed`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Incidents satisfactorily managed measures that result inside Administration, subcategory Local Public Safety. The unit is percent. The formula is (A / B) * 100, where A is part named by Incidents satisfactorily managed, B is whole named by Incidents satisfactorily managed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Incidents satisfactorily managed on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-incidents-satisfactorily-managed` (part named by Incidents satisfactorily managed)
- `metric.whole-named-by-incidents-satisfactorily-managed` (whole named by Incidents satisfactorily managed)

Placements:

- organizational / industries / Administration / Local Public Safety (sK1094, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Suicide rate

- id: `kpi.administration.suicide-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Suicide rate measures that result inside Administration, subcategory Local Public Safety. The unit is percent. The formula is (A / B) * 100, where A is numerator of Suicide rate, B is base of Suicide rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Suicide rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-suicide-rate` (numerator of Suicide rate)
- `metric.base-of-suicide-rate` (base of Suicide rate)

Placements:

- organizational / industries / Administration / Local Public Safety (sK2728, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Public safety cases by category

- id: `kpi.administration.public-safety-cases-by-category`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Public safety cases by category measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Public safety cases by category. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Public safety cases by category on the desired side of its target for this period?

Inputs:

- `metric.public-safety-cases-by-category` (Public safety cases by category)

Placements:

- organizational / industries / Administration / Local Public Safety (sK3994, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Active missing childernces

- id: `kpi.administration.active-missing-childernces`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Active missing childernces measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Active missing childernces. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Active missing childernces on the desired side of its target for this period?

Inputs:

- `metric.active-missing-childernces` (Active missing childernces)

Placements:

- organizational / industries / Administration / Local Public Safety (sK0122, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Registered sexual offenders identified to the public

- id: `kpi.administration.registered-sexual-offenders-identified-to-the-public`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Registered sexual offenders identified to the public measures that result inside Administration, subcategory Local Public Safety. The unit is percent. The formula is (A / B) * 100, where A is Registered sexual offenders identified, B is the public. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Registered sexual offenders identified to the public on the desired side of its target for this period?

Inputs:

- `metric.registered-sexual-offenders-identified` (Registered sexual offenders identified)
- `metric.the-public` (the public)

Placements:

- organizational / industries / Administration / Local Public Safety (sK0113, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Youth who remain crime free one year after release

- id: `kpi.administration.youth-who-remain-crime-free-one-year-after-release`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Youth who remain crime free one year after release measures that result inside Administration, subcategory Local Public Safety. The unit is percent. The formula is (A / B) * 100, where A is part named by Youth who remain crime free one year after release, B is whole named by Youth who remain crime free one year after release. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Youth who remain crime free one year after release on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-youth-who-remain-crime-free-one-year-after-release` (part named by Youth who remain crime free one year after release)
- `metric.whole-named-by-youth-who-remain-crime-free-one-year-after-release` (whole named by Youth who remain crime free one year after release)

Placements:

- organizational / industries / Administration / Local Public Safety (sK0211, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Population h non detention

- id: `kpi.administration.population-h-non-detention`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Population h non detention measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Population h non detention. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Population h non detention on the desired side of its target for this period?

Inputs:

- `metric.population-h-non-detention` (Population h non detention)

Placements:

- organizational / industries / Administration / Local Public Safety (sK0602, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Random image drug tests that are negative

- id: `kpi.administration.random-image-drug-tests-that-are-negative`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Random image drug tests that are negative measures that result inside Administration, subcategory Local Public Safety. The unit is percent. The formula is (A / B) * 100, where A is part named by Random image drug tests that are negative, B is whole named by Random image drug tests that are negative. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Random image drug tests that are negative on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-random-image-drug-tests-that-are-negative` (part named by Random image drug tests that are negative)
- `metric.whole-named-by-random-image-drug-tests-that-are-negative` (whole named by Random image drug tests that are negative)

Placements:

- organizational / industries / Administration / Local Public Safety (sK403, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Domestic violence incidents

- id: `kpi.administration.domestic-violence-incidents`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Domestic violence incidents measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Domestic violence incidents. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Domestic violence incidents on the desired side of its target for this period?

Inputs:

- `metric.domestic-violence-incidents` (Domestic violence incidents)

Placements:

- organizational / industries / Administration / Local Public Safety (sK0433, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Civil protection orders

- id: `kpi.administration.civil-protection-orders`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Civil protection orders measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Civil protection orders. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Civil protection orders on the desired side of its target for this period?

Inputs:

- `metric.civil-protection-orders` (Civil protection orders)

Placements:

- organizational / industries / Administration / Local Public Safety (sK4366, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Pushing age-embedded or cleared

- id: `kpi.administration.pushing-age-embedded-or-cleared`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Pushing age-embedded or cleared measures that result inside Administration, subcategory Local Public Safety. The unit is percent. The formula is (A / B) * 100, where A is part named by Pushing age-embedded or cleared, B is whole named by Pushing age-embedded or cleared. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Pushing age-embedded or cleared on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-pushing-age-embedded-or-cleared` (part named by Pushing age-embedded or cleared)
- `metric.whole-named-by-pushing-age-embedded-or-cleared` (whole named by Pushing age-embedded or cleared)

Placements:

- organizational / industries / Administration / Local Public Safety (sK4907, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Properties provided with storm water drainage facilities

- id: `kpi.administration.properties-provided-with-storm-water-drainage-facilities`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Properties provided with storm water drainage facilities measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Properties provided with storm water drainage facilities. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Properties provided with storm water drainage facilities on the desired side of its target for this period?

Inputs:

- `metric.properties-provided-with-storm-water-drainage-facilities` (Properties provided with storm water drainage facilities)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5071, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Perception of safety and occurrence of crime

- id: `kpi.administration.perception-of-safety-and-occurrence-of-crime`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Perception of safety and occurrence of crime measures that result inside Administration, subcategory Local Public Safety. The unit is percent. The formula is (A / B) * 100, where A is Perception, B is safety and occurrence of crime. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Perception of safety and occurrence of crime on the desired side of its target for this period?

Inputs:

- `metric.perception` (Perception)
- `metric.safety-and-occurrence-of-crime` (safety and occurrence of crime)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5258, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Case closures per investigator

- id: `kpi.administration.case-closures-per-investigator`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Case closures per investigator measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A / B, where A is Case closures, B is investigator. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Case closures per investigator on the desired side of its target for this period?

Inputs:

- `metric.case-closures` (Case closures)
- `metric.investigator` (investigator)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5283, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### famous incident in vocational skills training

- id: `kpi.administration.famous-incident-in-vocational-skills-training`
- kind: kri
- unit: count
- direction: down
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

famous incident in vocational skills training measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is famous incident in vocational skills training. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is famous incident in vocational skills training on the desired side of its target for this period?

Inputs:

- `metric.famous-incident-in-vocational-skills-training` (famous incident in vocational skills training)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5305, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Female health clinic visits

- id: `kpi.administration.female-health-clinic-visits`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Female health clinic visits measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Female health clinic visits. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Female health clinic visits on the desired side of its target for this period?

Inputs:

- `metric.female-health-clinic-visits` (Female health clinic visits)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5309, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fire safety education presentations completed

- id: `kpi.administration.fire-safety-education-presentations-completed`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fire safety education presentations completed measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Fire safety education presentations completed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fire safety education presentations completed on the desired side of its target for this period?

Inputs:

- `metric.fire-safety-education-presentations-completed` (Fire safety education presentations completed)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5330, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Counter terrorism training hours conducted

- id: `kpi.administration.counter-terrorism-training-hours-conducted`
- kind: kpi
- unit: count
- direction: down
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Counter terrorism training hours conducted measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Counter terrorism training hours conducted. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Counter terrorism training hours conducted on the desired side of its target for this period?

Inputs:

- `metric.counter-terrorism-training-hours-conducted` (Counter terrorism training hours conducted)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5347, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Gang motivated incidents

- id: `kpi.administration.gang-motivated-incidents`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Gang motivated incidents measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Gang motivated incidents. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Gang motivated incidents on the desired side of its target for this period?

Inputs:

- `metric.gang-motivated-incidents` (Gang motivated incidents)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5349, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fire weapons seized during arrests

- id: `kpi.administration.fire-weapons-seized-during-arrests`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fire weapons seized during arrests measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Fire weapons seized during arrests. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fire weapons seized during arrests on the desired side of its target for this period?

Inputs:

- `metric.fire-weapons-seized-during-arrests` (Fire weapons seized during arrests)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5352, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Major felony crimes in public housing developments

- id: `kpi.administration.major-felony-crimes-in-public-housing-developments`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Major felony crimes in public housing developments measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Major felony crimes in public housing developments. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Major felony crimes in public housing developments on the desired side of its target for this period?

Inputs:

- `metric.major-felony-crimes-in-public-housing-developments` (Major felony crimes in public housing developments)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5366, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Incidents of unsafe faeade conditions and falling debris resulting in injuries

- id: `kpi.administration.incidents-of-unsafe-faeade-conditions-and-falling-debris-resulting-in-in`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Incidents of unsafe faeade conditions and falling debris resulting in injuries measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Incidents of unsafe faeade conditions and falling debris resulting in injuries. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Incidents of unsafe faeade conditions and falling debris resulting in injuries on the desired side of its target for this period?

Inputs:

- `metric.incidents-of-unsafe-faeade-conditions-and-falling-debris-resulting-in-in` (Incidents of unsafe faeade conditions and falling debris resulting in injuries)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5435, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Complaints from unsafe faeade conditions and falling debris received

- id: `kpi.administration.complaints-from-unsafe-faeade-conditions-and-falling-debris-received`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Complaints from unsafe faeade conditions and falling debris received measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Complaints from unsafe faeade conditions and falling debris received. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Complaints from unsafe faeade conditions and falling debris received on the desired side of its target for this period?

Inputs:

- `metric.complaints-from-unsafe-faeade-conditions-and-falling-debris-received` (Complaints from unsafe faeade conditions and falling debris received)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5444, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Medicalisation safety and emissions inspections completed on time

- id: `kpi.administration.medicalisation-safety-and-emissions-inspections-completed-on-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Medicalisation safety and emissions inspections completed on time measures that result inside Administration, subcategory Local Public Safety. The unit is percent. The formula is (A / B) * 100, where A is part named by Medicalisation safety and emissions inspections completed on time, B is whole named by Medicalisation safety and emissions inspections completed on time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Medicalisation safety and emissions inspections completed on time on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-medicalisation-safety-and-emissions-inspections-completed` (part named by Medicalisation safety and emissions inspections completed on time)
- `metric.whole-named-by-medicalisation-safety-and-emissions-inspections-completed` (whole named by Medicalisation safety and emissions inspections completed on time)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5501, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Traffic monitoring started across national speed

- id: `kpi.administration.traffic-monitoring-started-across-national-speed`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Traffic monitoring started across national speed measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Traffic monitoring started across national speed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Traffic monitoring started across national speed on the desired side of its target for this period?

Inputs:

- `metric.traffic-monitoring-started-across-national-speed` (Traffic monitoring started across national speed)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5526, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Speeds moving installed near school doors

- id: `kpi.administration.speeds-moving-installed-near-school-doors`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Speeds moving installed near school doors measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Speeds moving installed near school doors. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Speeds moving installed near school doors on the desired side of its target for this period?

Inputs:

- `metric.speeds-moving-installed-near-school-doors` (Speeds moving installed near school doors)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5535, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sunlasses testing positive for coliform bacteria

- id: `kpi.administration.sunlasses-testing-positive-for-coliform-bacteria`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Sunlasses testing positive for coliform bacteria measures that result inside Administration, subcategory Local Public Safety. The unit is percent. The formula is (A / B) * 100, where A is part named by Sunlasses testing positive for coliform bacteria, B is whole named by Sunlasses testing positive for coliform bacteria. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sunlasses testing positive for coliform bacteria on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-sunlasses-testing-positive-for-coliform-bacteria` (part named by Sunlasses testing positive for coliform bacteria)
- `metric.whole-named-by-sunlasses-testing-positive-for-coliform-bacteria` (whole named by Sunlasses testing positive for coliform bacteria)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5562, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Drinking water tests above maximum contaminant level

- id: `kpi.administration.drinking-water-tests-above-maximum-contaminant-level`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Drinking water tests above maximum contaminant level measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Drinking water tests above maximum contaminant level. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Drinking water tests above maximum contaminant level on the desired side of its target for this period?

Inputs:

- `metric.drinking-water-tests-above-maximum-contaminant-level` (Drinking water tests above maximum contaminant level)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5562, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Daily test per infection in detention

- id: `kpi.administration.daily-test-per-infection-in-detention`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Daily test per infection in detention measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A / B, where A is Daily test, B is infection in detention. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Daily test per infection in detention on the desired side of its target for this period?

Inputs:

- `metric.daily-test` (Daily test)
- `metric.infection-in-detention` (infection in detention)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5567, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Population in detention

- id: `kpi.administration.population-in-detention`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Population in detention measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Population in detention. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Population in detention on the desired side of its target for this period?

Inputs:

- `metric.population-in-detention` (Population in detention)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5569, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Combined average length of stay in secure room and secure detention

- id: `kpi.administration.combined-average-length-of-stay-in-secure-room-and-secure-detention`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: average
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Combined average length of stay in secure room and secure detention measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A / B, where A is sum underlying Combined average length of stay in secure room and secure detention, B is count of observations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Combined average length of stay in secure room and secure detention on the desired side of its target for this period?

Inputs:

- `metric.sum-underlying-combined-average-length-of-stay-in-secure-room-and-secure` (sum underlying Combined average length of stay in secure room and secure detention)
- `metric.count-of-observations` (count of observations)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5579, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Request from secure detention facilities

- id: `kpi.administration.request-from-secure-detention-facilities`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Request from secure detention facilities measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Request from secure detention facilities. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Request from secure detention facilities on the desired side of its target for this period?

Inputs:

- `metric.request-from-secure-detention-facilities` (Request from secure detention facilities)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5571, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Person-issued investigation reports on adults cases submitted 24 hours prior to scheduled hearing

- id: `kpi.administration.person-issued-investigation-reports-on-adults-cases-submitted-24-hours-p`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Person-issued investigation reports on adults cases submitted 24 hours prior to scheduled hearing measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Person-issued investigation reports on adults cases submitted 24 hours prior to scheduled hearing. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Person-issued investigation reports on adults cases submitted 24 hours prior to scheduled hearing on the desired side of its target for this period?

Inputs:

- `metric.person-issued-investigation-reports-on-adults-cases-submitted-24-hours-p` (Person-issued investigation reports on adults cases submitted 24 hours prior to scheduled hearing)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5582, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Family court javelin cases with investigations and reports submitted on time

- id: `kpi.administration.family-court-javelin-cases-with-investigations-and-reports-submitted-on`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Family court javelin cases with investigations and reports submitted on time measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Family court javelin cases with investigations and reports submitted on time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Family court javelin cases with investigations and reports submitted on time on the desired side of its target for this period?

Inputs:

- `metric.family-court-javelin-cases-with-investigations-and-reports-submitted-on` (Family court javelin cases with investigations and reports submitted on time)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5585, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Business rate of adults on probation

- id: `kpi.administration.business-rate-of-adults-on-probation`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Business rate of adults on probation measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Business rate of adults on probation. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Business rate of adults on probation on the desired side of its target for this period?

Inputs:

- `metric.business-rate-of-adults-on-probation` (Business rate of adults on probation)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5586, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Adult police arrest that are probationers

- id: `kpi.administration.adult-police-arrest-that-are-probationers`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Adult police arrest that are probationers measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Adult police arrest that are probationers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Adult police arrest that are probationers on the desired side of its target for this period?

Inputs:

- `metric.adult-police-arrest-that-are-probationers` (Adult police arrest that are probationers)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5587, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Juvenile delinquency cases diverted from court through adjustment

- id: `kpi.administration.juvenile-delinquency-cases-diverted-from-court-through-adjustment`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Juvenile delinquency cases diverted from court through adjustment measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Juvenile delinquency cases diverted from court through adjustment. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Juvenile delinquency cases diverted from court through adjustment on the desired side of its target for this period?

Inputs:

- `metric.juvenile-delinquency-cases-diverted-from-court-through-adjustment` (Juvenile delinquency cases diverted from court through adjustment)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5888, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Juvenile probationer arrest rate

- id: `kpi.administration.juvenile-probationer-arrest-rate`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Juvenile probationer arrest rate measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Juvenile probationer arrest rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Juvenile probationer arrest rate on the desired side of its target for this period?

Inputs:

- `metric.juvenile-probationer-arrest-rate` (Juvenile probationer arrest rate)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5889, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Juvenile police arrest that are probationers

- id: `kpi.administration.juvenile-police-arrest-that-are-probationers`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Juvenile police arrest that are probationers measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Juvenile police arrest that are probationers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Juvenile police arrest that are probationers on the desired side of its target for this period?

Inputs:

- `metric.juvenile-police-arrest-that-are-probationers` (Juvenile police arrest that are probationers)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5909, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time to respond to traffic signal defects and make the traffic signs

- id: `kpi.administration.time-to-respond-to-traffic-signal-defects-and-make-the-traffic-signs`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time to respond to traffic signal defects and make the traffic signs measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Time to respond to traffic signal defects and make the traffic signs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time to respond to traffic signal defects and make the traffic signs on the desired side of its target for this period?

Inputs:

- `metric.time-to-respond-to-traffic-signal-defects-and-make-the-traffic-signs` (Time to respond to traffic signal defects and make the traffic signs)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5911, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Citywide traffic fatalities

- id: `kpi.administration.citywide-traffic-fatalities`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Citywide traffic fatalities measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Citywide traffic fatalities. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Citywide traffic fatalities on the desired side of its target for this period?

Inputs:

- `metric.citywide-traffic-fatalities` (Citywide traffic fatalities)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5912, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Traffic problems

- id: `kpi.administration.traffic-problems`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Traffic problems measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Traffic problems. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Traffic problems on the desired side of its target for this period?

Inputs:

- `metric.traffic-problems` (Traffic problems)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5913, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Major felonies in park

- id: `kpi.administration.major-felonies-in-park`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Major felonies in park measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Major felonies in park. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Major felonies in park on the desired side of its target for this period?

Inputs:

- `metric.major-felonies-in-park` (Major felonies in park)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5914, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Response time to life threatening medical emergencies by ambulance units

- id: `kpi.administration.response-time-to-life-threatening-medical-emergencies-by-ambulance-units`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Response time to life threatening medical emergencies by ambulance units measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Response time to life threatening medical emergencies by ambulance units. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Response time to life threatening medical emergencies by ambulance units on the desired side of its target for this period?

Inputs:

- `metric.response-time-to-life-threatening-medical-emergencies-by-ambulance-units` (Response time to life threatening medical emergencies by ambulance units)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5916, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Combined response time to life threatening medical emergencies by ambulance units and fire units

- id: `kpi.administration.combined-response-time-to-life-threatening-medical-emergencies-by-ambula`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Combined response time to life threatening medical emergencies by ambulance units and fire units measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Combined response time to life threatening medical emergencies by ambulance units and fire units. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Combined response time to life threatening medical emergencies by ambulance units and fire units on the desired side of its target for this period?

Inputs:

- `metric.combined-response-time-to-life-threatening-medical-emergencies-by-ambula` (Combined response time to life threatening medical emergencies by ambulance units and fire units)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5917, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Response time to structural fires

- id: `kpi.administration.response-time-to-structural-fires`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Response time to structural fires measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Response time to structural fires. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Response time to structural fires on the desired side of its target for this period?

Inputs:

- `metric.response-time-to-structural-fires` (Response time to structural fires)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5918, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Civilian fire fatalities

- id: `kpi.administration.civilian-fire-fatalities`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Civilian fire fatalities measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Civilian fire fatalities. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Civilian fire fatalities on the desired side of its target for this period?

Inputs:

- `metric.civilian-fire-fatalities` (Civilian fire fatalities)

Placements:

- organizational / industries / Administration / Local Public Safety (sK5919, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Critical fires per 1000 structural fires

- id: `kpi.administration.critical-fires-per-1000-structural-fires`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Critical fires per 1000 structural fires measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A / B, where A is Critical fires, B is 1000 structural fires. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Critical fires per 1000 structural fires on the desired side of its target for this period?

Inputs:

- `metric.critical-fires` (Critical fires)
- `metric.1000-structural-fires` (1000 structural fires)

Placements:

- organizational / industries / Administration / Local Public Safety (sK600, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Firefighter burns and injuries while on duty

- id: `kpi.administration.firefighter-burns-and-injuries-while-on-duty`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Firefighter burns and injuries while on duty measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Firefighter burns and injuries while on duty. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Firefighter burns and injuries while on duty on the desired side of its target for this period?

Inputs:

- `metric.firefighter-burns-and-injuries-while-on-duty` (Firefighter burns and injuries while on duty)

Placements:

- organizational / industries / Administration / Local Public Safety (sK602, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Major felony crime by factory

- id: `kpi.administration.major-felony-crime-by-factory`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Major felony crime by factory measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A, where A is Major felony crime by factory. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Major felony crime by factory on the desired side of its target for this period?

Inputs:

- `metric.major-felony-crime-by-factory` (Major felony crime by factory)

Placements:

- organizational / industries / Administration / Local Public Safety (sK604, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Women who die from intimate partner homicide per 100,000 women

- id: `kpi.administration.women-who-die-from-intimate-partner-homicide-per-100-000-women`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.administration.local-public-safety`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Women who die from intimate partner homicide per 100,000 women measures that result inside Administration, subcategory Local Public Safety. The unit is count. The formula is A / B, where A is Women who die from intimate partner homicide, B is 100,000 women. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Women who die from intimate partner homicide per 100,000 women on the desired side of its target for this period?

Inputs:

- `metric.women-who-die-from-intimate-partner-homicide` (Women who die from intimate partner homicide)
- `metric.100-000-women` (100,000 women)

Placements:

- organizational / industries / Administration / Local Public Safety (sK6058, page_0091)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.
