# -*- coding: utf-8 -*-
"""Write theory, IBCS, report, and story cards. Original prose, not book excerpts.

    python chart-expert/scripts/write_foundations.py            # write
    python chart-expert/scripts/write_foundations.py --check    # exit 1 if anything would change

The cards under library/THEORY, STANDARDS, REPORTS, and STORIES are generated from the strings
below. Edit the strings, not the output.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEORY = ROOT / "library" / "THEORY"
STAND = ROOT / "library" / "STANDARDS"
REPORTS_DIR = ROOT / "library" / "REPORTS"
STORIES_DIR = ROOT / "library" / "STORIES"


CHECK = "--check" in sys.argv[1:]
CHANGED: list[Path] = []


def write(path: Path, text: str) -> None:
    text = text.strip() + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return
    CHANGED.append(path)
    if not CHECK:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")


CHAPTERS = {
    "01-on-performance.md": """
# On performance

Performance is the relationship between an intended result and the result that actually occurred. It is not activity, and it is not a software score. A team can be busy and still miss the result. A dashboard can be full and still say nothing about that gap.

Three pieces have to be named before a number is useful:

- The result someone intends (an objective).
- The evidence that would show the result is happening (a key result, usually a KPI with a target).
- The conditions that produce the result (process, capacity, risk). Those conditions are where leading indicators live.

Performance is comparative. A number without a baseline, a target, or a peer is a measure, not a judgment. Say what the comparison is: prior period, plan, forecast, benchmark, or a corridor.

## Rule

Do not call a figure a performance result until the intended result, the comparison, and the owner are written down.

## Worked example

An agency wants projects to earn the gross profit that was quoted. The result is not "hours worked." The result is project contribution margin versus the estimate. Hours and cost are the conditions. Open `kpi` cards for contribution margin, estimated-versus-actual hours, and estimated-versus-actual cost.

## Failure this chapter prevents

Treating a report full of activity counts as proof that the organization performed.

## Open next

`02-performance-management-and-measurement.md`, then `library/ONTOLOGY.md`.
""",
    "02-performance-management-and-measurement.md": """
# Performance management and measurement

Measurement is the act of producing a number. Management is the act of using numbers to choose, to learn, and to change the system of work. A KPI program that only publishes numbers is measurement. It becomes management when someone is accountable for the gap and for the response.

The loop is short:

1. Set an objective and a small set of key results.
2. Define the KPI, the formula, and the source of each input.
3. Compare the result to the target at a fixed cadence.
4. Explain the gap with the sub-metrics, not with a new adjective.
5. Change the work. Then measure again.

## Rule

Every KPI on a management dashboard needs an owner, a cadence, and a response that is allowed when it moves the wrong way. A number with no response is a souvenir.

## Worked example

Monthly recurring revenue is reviewed on the first working day. If it is below the target, the owner looks at new business, expansion, and churn as sub-metrics before changing the target. The chart is a waterfall or a variance bar, not a gauge. See `library/OMTM/saas.md` and `library/DASHBOARDS/sales-and-customer-service/revenue.md`.

## Failure this chapter prevents

Building a measurement system that nobody is allowed to act on.

## Open next

`03-performance-management-levels.md` and `library/REPORTS/monthly-business-review.md`.
""",
    "03-performance-management-levels.md": """
# Performance management levels

The same KPI does not serve every altitude. Mixing altitudes on one screen makes every number look equally urgent.

- **Strategic.** Few lagging outcomes for the organization: profit, retention, cash, safety, mission result. Cadence is month or quarter. Audience is the executive.
- **Tactical.** The function's contribution to those outcomes: pipeline coverage, utilization, on-time delivery, acquisition cost. Cadence is week or month.
- **Operational.** The process signals that move first: queue age, cycle time, error rate, schedule adherence. Cadence is day or week. Audience is the team.
- **Individual.** A person's own work, used for learning. It should not be a secret ranking pasted onto a wall.

A key result at one level should be explainable by indicators at the level below. If it cannot, the tree is decorative.

## Rule

Label the level on the KPI (`level` in the catalog). Do not put operational counts in the board pack unless they explain a strategic gap.

## Worked example

Company objective: grow global sales. Strategic KPI: revenue versus the annual target. Tactical KPI: pipeline coverage. Operational KPI: demos per week. The executive dashboard shows the first, with the second as the breakdown. Demos stay on the sales-manager dashboard.

## Failure this chapter prevents

A single page that asks a board and a dispatcher to read the same grain of data.

## Open next

`10-kpis-formulation-and-selection.md` and `library/OKRS/`.
""",
    "04-history-of-performance-management.md": """
# History of performance management

People have tallied work for as long as they have coordinated it. Double-entry bookkeeping, associated with Luca Pacioli's 1494 synthesis of Venetian practice, made financial stocks and flows checkable. Industrial management added time, cost, and standard rates. The twentieth century added quality control charts, management by objectives, and the balanced scorecard's reminder that financial results are late.

Each wave fixed a blindness and created a new one. Financial accounts ignored non-financial drivers. Management by objectives often turned into a stack of personal tasks. The balanced scorecard multiplied perspectives and, in careless hands, multiplied indicators until nothing was key. Indicator catalogues then made it easy to import a number that no one in the building owns.

## Rule

Use the history as a warning about fashion. Adopt a measure because it answers a current question, not because a catalogue lists it.

## Worked example

A team imports forty "best practice" marketing KPIs. The history of this pattern is a scorecard nobody reads. The repair is the selection rule in chapter 10: start from the objective, keep the few indicators that would change a decision, and file the rest as metrics.

## Failure this chapter prevents

Confusing a long inherited list with a management system.

## Open next

`05-theory-informing-performance-management.md`.
""",
    "05-theory-informing-performance-management.md": """
# Theory informing performance management

Several ideas constrain this library. They are named here so an agent can apply them without quoting a book.

- **Systems.** Results come from the design of the work, not only from individual effort. A KPI that blames a person for a system rate will be gamed.
- **Leading and lagging.** Outcomes arrive late. Activities and stocks of work move earlier. A steering review needs both. See `library/ONTOLOGY.md`.
- **Balanced views.** Financial, customer, process, and capability results can contradict each other. A single financial ratio is not the whole story, and four perspectives are not an excuse for forty KPIs.
- **Objectives and key results.** The objective is qualitative. The key result is a measured outcome. Tasks are initiatives.
- **Statistical thinking.** A point above a target is not always a signal. Stable processes vary. Control charts and process behavior charts exist so noise is not managed as if it were news.
- **Measurement as learning.** The first use of a KPI is to see. Pay schemes that hang on a single indicator teach people to move the indicator.

Writers associated with these ideas include Kaplan and Norton (balanced scorecard), Parmenter (few winning KPIs), Marr (practical indicator design), Neely (measurement system design), and the KPI Institute's separation of measures, indicators, and the few that are key. This primer does not reproduce their texts.

## Rule

If a proposed KPI conflicts with one of these ideas, say which idea and why before recommending it.

## Worked example

Utilization above a ceiling looks like efficiency and is often overload. The corridor, not "higher is better," is the theory-correct reading. The card's `direction` should be `corridor`.

## Failure this chapter prevents

A library that treats every indicator as "up is good."

## Open next

`06-principles-of-performance-measurement.md` and `08-types-of-kpis.md`.
""",
    "06-principles-of-performance-measurement.md": """
# Principles of performance measurement

1. **Decision first.** A measure that cannot change a decision does not belong on the dashboard. It may still belong in the metric library.
2. **One concept, one name.** "Churn", "logo churn", and "revenue churn" are different. In this library `kpi.sales-and-customer-service.customer-churn-rate` is logo churn; revenue churn needs its own card and its own id.
3. **Formula before target.** Agree what is included and excluded before arguing about the number.
4. **Comparable.** State the period, the population, and the comparison (plan, prior, peer).
5. **Owned.** Someone can explain the inputs.
6. **Few keys.** Most numbers are metrics. Keys are selected.
7. **Honest grain.** Do not average away the segment that is failing.
8. **Direction is explicit.** Up, down, or corridor.
9. **Leading pair.** Where the outcome is lagging, name at least one indicator that moves earlier.
10. **Visual integrity.** The chart must encode the comparison the principle requires. See chapter 14 and the IBCS note.

## Rule

Reject a KPI card that has a name and no formula, or a formula whose inputs are not metrics.

## Worked example

"Customer profitability" fails principle 2 until it says contribution after direct cost, over a trailing twelve months, for active customers. The formula cites revenue and direct cost. The chart is a bar ranked by customer, not a pie.

## Failure this chapter prevents

Dashboards whose numbers cannot be reconstructed from the warehouse.

## Open next

`07-metrics-kpis-kris-and-analytics.md`.
""",
    "07-metrics-kpis-kris-and-analytics.md": """
# Metrics, KPIs, KRIs, and analytics

Analytics is the practice of asking questions of data. Metrics are the quantities. KPIs are the quantities tied to objectives. KRIs are the quantities tied to risk. A chart is an argument about one of those quantities, not a type of metric.

Use the stack in this order:

- A **metric** describes. Example: invoices issued.
- A **sub-metric** is an input. Example: credit sales, which enters DSO.
- A **KPI** judges a success result. Example: DSO versus the target.
- A **KRI** judges a risk. Example: share of receivables older than 90 days.
- An **analysis** explains a movement. Example: a waterfall from last month's DSO to this month's, split by terms, disputes, and collections.

Analytics without a KPI becomes a tour. A KPI without analysis becomes a verdict with no cause.

## Rule

When a user asks for "analytics," ask which decision, then which KPI, then which breakdown. Do not start by choosing a chart type.

## Worked example

Question: why did cash slip? KPI: operating cash flow. KRI: receivables older than 90 days. Analysis: waterfall of cash flow and an aging bar. Charts come from those jobs, not from a gallery.

## Failure this chapter prevents

Calling every tile a KPI, and every chart an analysis.

## Open next

`library/ONTOLOGY.md` and `09-characteristics-of-good-kpis.md`.
""",
    "08-types-of-kpis.md": """
# Types of KPIs

Type the indicator before you chart it. The type chooses the comparison and the chart family.

- **Input.** Resources consumed. Often a sub-metric. Direction depends on waste versus necessary capacity.
- **Process / activity.** Work done. Often leading. Counts and cycle times.
- **Output.** Work completed. Volume. Not the same as the outcome.
- **Outcome.** The result the objective named. Often lagging.
- **Efficiency.** Output per input, or cost per unit. A ratio.
- **Effectiveness.** Degree to which the outcome met the intent. Often a percent of a target or a quality rate.
- **Lagging outcome versus leading driver.** A pair, not two rivals.
- **Absolute, ratio, index.** Absolute values need a scale. Ratios need a declared base. Indexes need a base period.
- **Corridor.** Too low and too high are both failures (utilization, cash buffer, mix).
- **Risk (KRI).** Exposure or loss. Usually down, or inside a limit.

The catalog field `formula_type` records ratio, difference, average, index, survey, or count. `direction` records up, down, or corridor. `leading_lagging` records timing.

## Rule

Do not put an input and an outcome on the same axis and call them one KPI.

## Worked example

Demos per week is an activity KPI (leading, count, up toward a capacity). Win rate is an effectiveness KPI (lagging, percent, up). Pipeline value is a stock. The sales dashboard gives each its own encoding.

## Failure this chapter prevents

A combo chart that implies a count and a percent share a meaning because they share a category axis.

## Open next

`14-kpi-visualisation-and-software.md` and `references/chart-library-index.md`.
""",
    "09-characteristics-of-good-kpis.md": """
# Characteristics of good KPIs

A good KPI is:

- **Relevant.** It tracks the objective, not a nearby curiosity.
- **Owned.** A person can defend the formula.
- **Understandable.** A new manager can say what a movement means.
- **Timely.** The cadence is faster than the decision cycle.
- **Comparable.** Period, population, and comparison are fixed.
- **Resistant to easy gaming.** Moving the number without moving the result is hard, or is visible in a paired indicator.
- **Cheap enough.** The cost of the data is smaller than the cost of the blind decision.
- **Few.** It earned its place against the other candidates.

Quantitative tests used in practice: a clear formula, a declared direction, a target or a corridor, a leading or lagging label, and a chart that keeps the comparison honest.

## Rule

If you cannot write the formula and the failure mode on the card, it is not ready to be called good.

## Worked example

Net promoter score is understandable and owned only if the survey population and the cadence are on the card. Without those, it is a slogan. Pair it with retention, which is harder to game with a single campaign.

## Failure this chapter prevents

Promoting a popular metric that no one can recompute.

## Open next

`10-kpis-formulation-and-selection.md`.
""",
    "10-kpis-formulation-and-selection.md": """
# KPIs formulation and selection

Formulate the indicator in this order. Skipping a step produces a name with no meaning.

1. Write the decision and the objective.
2. Name the result in words, including what is in and what is out.
3. Choose the unit (`$`, `#`, `%`, duration, index, survey).
4. Write the formula as named sub-metrics. Define each input.
5. Set direction and whether the indicator leads or lags.
6. Set the level (strategic, tactical, operational, individual) and the cadence.
7. Only then pick a target.
8. Pick the chart from the analytical job (comparison, trend, part-to-whole, deviation, distribution, flow, rank).
9. Place it on the dashboard specification for its function and area.

Selection among candidates:

- Prefer indicators that are outcomes or proven drivers over indicators that are easy to extract.
- Prefer one ratio with a clear base over several absolutes that cannot be compared.
- Drop duplicates (cost per acquisition and customer acquisition cost, when they share a formula).
- Keep a KRI beside a KPI when success and risk move apart (growth and concentration, speed and defects).
- Stop when the set answers the question. More indicators do not make the answer finer.

A long KPI inventory is a menu, not a mandate. This library publishes only measures with a full entry (formula, inputs, direction, charts). A team still selects.

## Rule

Selection is a cut. Formulation is a specification. Do not confuse a long catalog with a chosen scorecard.

## Worked example

Objective: improve collections. Candidates: DSO, aging buckets, collector calls, cash collected. Select DSO as the lagging KPI, share of receivables older than 90 days as the KRI, and calls or promises as a leading metric if the team controls them. Chart DSO as a line against the target and aging as a stacked bar.

## Failure this chapter prevents

A scorecard copied from a catalogue with no objective attached.

## Open next

`11-working-with-targets.md` and `library/KPIS/_catalog/kpis.jsonl`.
""",
    "11-working-with-targets.md": """
# Working with targets

A target is a commitment about a future value of a KPI. It is not the historical average, and it is not a decoration in a gauge.

Set targets from, in order of preference:

1. A decision threshold (the point at which the action changes).
2. A plan or a quote the organization already made (estimated hours, budget).
3. A statistical baseline plus an explicit improvement, after the process is stable.
4. An external benchmark, labeled as a benchmark. Agency rules of thumb in this library (gross profit per fee earner, team cost at most 60 percent of gross profit, marketing spend around 5 to 10 percent of gross profit) are this kind. They are notes, not laws.

A corridor target has a floor and a ceiling. A one-sided target has a direction. A milestone target has a date.

Do not reset the target every time the number misses, or the target teaches nothing. Do not set a target before the formula is stable, or people will negotiate the definition instead of the work.

## Rule

Store the target on the key result and as a note on the KPI. State the source. Never draw a target line whose definition differs from the KPI.

## Worked example

Key result: cost per lead at or below 4 currency units, this quarter, source = the campaign plan. The bullet chart encodes actual, the target, and a qualitative range. If the definition of "lead" changes mid-quarter, the target is void until the series is restated.

## Failure this chapter prevents

Targets that move so the indicator can be called green.

## Open next

`12-using-kpis.md` and `library/STORIES/pace-to-goal.md`.
""",
    "12-using-kpis.md": """
# Using KPIs

Use a KPI in four rooms. Do not use the same pack in all four.

- **Learning review.** What moved, what is noise, what will we change in the system? Leading and lagging together. Psychological safety matters more than a red tile.
- **Steering meeting.** Are we on pace? What decision is due this cycle? Few KPIs, each with a comparison.
- **Accountability.** Did the owner do what the key result required? Keep this tied to outcomes the person can influence. Do not pay on a single ratio.
- **Reporting outward.** Clients, boards, regulators. Fewer series, declared definitions, no internal slang.

A good use produces a sentence: "Margin is 3 points under the quote because delivery hours ran 12 percent over, concentrated in two projects." A bad use produces a color.

## Rule

Leave the meeting with a decision, a changed assumption, or an explicit "no action because the series is inside normal variation." A meeting that only "reviewed the dashboard" did not use the KPI.

## Worked example

The monthly review opens on the OMTM, then the three key results, then one diagnostic waterfall. Project-level rows stay in the detail zone for the owner who must act. See `library/REPORTS/monthly-business-review.md`.

## Failure this chapter prevents

KPI theatre: a recurring meeting that never changes work.

## Open next

`13-kpi-pitfalls.md` and `library/STORIES/diagnostic.md`.
""",
    "13-kpi-pitfalls.md": """
# KPI pitfalls and how to avoid them

- **Too many keys.** Remedy: selection in chapter 10. File the rest as metrics.
- **Activity as outcome.** "Posts published" can be an initiative count. It is not proof of demand. Pair it with a result.
- **Undefined base.** A percent without a denominator. Put the base in the formula.
- **Mixed populations.** Churn of logos versus churn of revenue. Split the ids.
- **Gaming.** If a single indicator is rewarded, watch the paired KRI (speed and defects, collection and disputes, utilization and attrition).
- **Vanity.** A number that can only go up because the definition accumulates (cumulative users) and is presented as a performance result.
- **False precision.** Targets to the second decimal on a survey. Round to the decision.
- **Survivorship.** Ratios on the customers who remain. Show the lost cohort.
- **Level mix.** Board charts of ticket handles.
- **Moving definitions.** Restate history or start a new series. Do not splice.
- **Target theater.** See chapter 11.
- **Chart that lies about the KPI.** A pie for a trend, a gauge for a composition, a dual axis that implies a relationship the formula does not state.

## Rule

When you recommend a KPI, name the pitfall it is most exposed to and the paired indicator that would reveal gaming.

## Worked example

Utilization is gamed by logging hours to internal codes or by refusing necessary work. Pair it with project contribution margin and with a quality or rework KRI. Direction is a corridor.

## Failure this chapter prevents

A confident dashboard of indicators that improve while the objective gets worse.

## Open next

`14-kpi-visualisation-and-software.md` and `library/STANDARDS/ibcs-success.md`.
""",
    "14-kpi-visualisation-and-software.md": """
# KPI visualisation and enabling software

Visualisation is part of the definition. A KPI that is a percent versus a target is a deviation problem. A KPI that is a stock over time is a trend problem. The chart library's analytical function is the bridge.

Match the job:

- One result versus a target: bullet graph or a variance bar. Not a gauge.
- Change over time: line. Not a spaghetti of twelve series; use small multiples or a horizon chart when the count of series is the problem.
- Rank of categories: horizontal bar, sorted.
- Part of a whole: stacked bar or a table with shares. Pie and donut stay in the library marked `ibcs_status: avoid` for management reporting.
- Bridge from one total to the next: waterfall.
- Distribution: histogram, box, or dot plot. Not a single average.
- Flow from state to state: Sankey or a funnel used only when the stages are a real sequence.

Software (spreadsheets, BI tools, finance systems) is acceptable when it preserves the formula, the comparison, and the notation. It is not acceptable when the default chart contradicts the job. The IBCS note in `library/STANDARDS/ibcs-success.md` is the notation layer: titles that state the message, consistent scales, semantic color for actual, plan, and forecast, no decoration.

Dashboards in this library are zone grids (score, trend, breakdown, variance, detail). A dashboard specification names the KPI, the chart, and the zone before any tool is chosen. A Databox or Zebra template is a concrete layout. It does not replace the formula.

## Rule

Choose the chart from the analytical function and the IBCS status. Then choose the tool. Never the other way around.

## Worked example

DSO versus a 45-day target, monthly, for an executive: bullet or a line with a target, plus an aging stacked bar in the breakdown zone. The tool can be a spreadsheet or Power BI. The gauge is rejected even if it is the tool's default.

## Failure this chapter prevents

A tool demo that dictates both the KPI list and the chart.

## Open next

`references/selection-playbook.md` and `15-key-directions-for-performance-management.md`.
""",
    "15-key-directions-for-performance-management.md": """
# Key directions for performance management

The useful directions, stated so a later design can follow them:

- **Fewer keys, fuller definitions.** Breadth belongs in the catalog. The live scorecard stays short. Every entry in this library has a full definition so selection is possible.
- **Formulas that cite inputs.** Sub-metrics are first-class. A KPI that cannot be recomputed is retired.
- **Leading and lagging as pairs.** Steering views include a driver. Reporting views may be lagging, but they say so.
- **Risk beside success.** KRIs sit next to the KPI they can contradict.
- **Levels kept apart.** Strategic, tactical, operational, and individual packs do not share a canvas.
- **Targets with a source.** Plan, threshold, baseline, or labeled benchmark.
- **Notation over decoration.** IBCS-style comparison (actual, plan, forecast) beats ornamental dials.
- **Stories with a decision.** A dashboard that cannot produce a sentence is a dead end.
- **Learning over punishment.** Individual indicators are for the person who owns the work.
- **Systems over heroes.** If a rate is produced by the process, manage the process.

## Rule

When you extend this library, add a full entry or an explicit exception. Do not add a name-only row and call the catalog finished.

## Worked example

A new function or area arrives. Add each KPI to `CORE` in `scripts/build_measures.py` with its formula, inputs, and charts; the build writes its dashboard specification. Add at least one objective whose key results cite those KPIs. Then select the live scorecard from that menu.

## Failure this chapter prevents

A measurement program that grows by accumulation and shrinks in meaning.

## Open next

`references/selection-playbook.md`.
""",
}


IBCS = """
# IBCS SUCCESS (working rules)

These are original working rules for this library, aligned to the seven SUCCESS rule groups of the International Business Communication Standards (IBCS), published by the IBCS Association (ibcs.com). They are not the text of the standard. Chart cards carry `ibcs_status`; `library/_INDICES/by-ibcs.md` lists the charts by status.

SUCCESS: **S**ay, **U**nify, **C**ondense, **C**heck, **E**xpress, **S**implify, **S**tructure.

## Say: convey a message

The title is a message, not a topic. "Margin missed the quote by 3 points" is a title. "Margin overview" is a label. State the objective of the page before adding charts. Introduce the comparison, deliver the evidence, support it with the breakdown, and end with the implication.

## Unify: apply semantic notation

One term per measure, the same term as the KPI card. One format for dates, units, and variances. Scenarios have stable meanings and stable visual treatment across pages: actual (AC) is the solid series, previous year (PY) and plan (PL) are references, forecast (FC) is visually distinct from actual. Color is not a second rainbow for categories that are already labeled.

## Condense: increase information density

Prefer small multiples, overlays of actual and plan, and sparklines inside a variance table to a stack of single-number tiles. A lonely number needs a comparison. Embed the trend in the row when the row is the entity (a project, a customer, a rep).

## Check: ensure visual integrity

Axes start at zero when length encodes magnitude. Scales that compare are shared. Do not crop a bar axis. Label omissions. If a component is missing, say so. Adjustments (currency, restatement, partial period) are written next to the title, not hidden in a footnote no one opens.

## Express: choose a proper visualization

Use the chart that encodes the comparison:

- Time: line, column only when the periods are few.
- Rank: bar, sorted.
- Part-to-whole: stacked column or bar, or a table of shares.
- Deviation: bar diverging from a baseline, bullet, waterfall.
- Distribution: dots, box, histogram.
- Correlation: scatter.

Replace, for management communication: gauges, radar charts, pie and donut charts, spaghetti lines, and traffic-light tiles used as the only encoding. Those types remain in the chart library with `ibcs_status: avoid` so an agent can recognize them and refuse them for this job. Tables carry precise values. Charts carry patterns.

## Simplify: avoid clutter

Remove gridlines, shadows, 3D, and legends that repeat direct labels. A marker must encode data or it goes. Whitespace is structure, not a theme.

## Structure: organize content

One page, one question. Sections are mutually exclusive and together cover the question. Put the score and the message first, then the trend, then the breakdown, then the detail a person can act on. Do not make the reader discover the structure.

## Status values on chart cards

- `preferred`: the chart can carry a management comparison without a warning.
- `conditional`: usable when the audience knows the encoding, or when a warning is attached (dual axis, horizon mirroring, radial layouts, area as the only magnitude encoding).
- `avoid`: removed from Executive, Public, and client communication surfaces (dashboard, report, story). It stays eligible on Analytics and Technical analysis surfaces (notebook, exploratory plot), and when the user is studying the chart type itself.
"""


REPORTS = {
    "board-pack.md": """
# Board pack

Audience: executive and board. Cadence: month or quarter. Level: strategic.

## Question

Are the few outcomes that define the period on pace, and what risk sits beside them?

## Section order

1. Message and OMTM versus target.
2. Three to five strategic KPIs, each as actual versus plan, with a sparkline.
3. One variance bridge for the outcome that moved.
4. KRIs that can contradict the success story (cash, concentration, safety, attrition).
5. Decisions requested. No operational catalog.

## Dashboards reused

The OMTM card for the business model (`library/OMTM/`) and the finance and customer dashboard specifications, score and variance zones only.

## IBCS

Message titles, shared scales, actual/plan/forecast notation, no gauges. See `library/STANDARDS/ibcs-success.md`.
""",
    "monthly-business-review.md": """
# Monthly business review

Audience: executive and function leads. Cadence: month. Level: strategic and tactical.

## Question

What changed since last month, what is inside normal variation, and what will we change in the work?

## Section order

1. OMTM and the key results for the active objectives.
2. Variance versus plan and versus the prior month.
3. Leading indicators for the outcomes that are off pace.
4. One diagnostic breakdown (customer, project, channel, or product).
5. Decisions, owners, and the indicator that will show the decision worked.

## Dashboards reused

Subcategory dashboards for the functions in the review. Score, trend, variance, and one breakdown zone.

## IBCS

Titles state the gap. Do not open on a pie of the mix. The mix belongs in a stacked bar or a table if it explains the gap.
""",
    "variance-report.md": """
# Variance report

Audience: finance and the budget owner. Cadence: month. Level: tactical.

## Question

Where did actual depart from plan, in what sign, and in which entity?

## Section order

1. Total variance, absolute and percent.
2. Waterfall or diverging bar from plan to actual by driver.
3. IBCS variance table: entity, actual, plan, absolute variance, percent variance, sparkline.
4. The few rows that explain most of the gap (a Pareto cut).
5. Restatements and one-off items, labeled.

## Dashboards reused

Finance dashboard specifications, variance and detail zones.

## IBCS

This report is the home of the variance table chart. Semantic notation for actual and plan. No traffic lights as the only signal. A miss and a beat must be readable in grayscale by sign and position.
""",
    "scorecard.md": """
# Scorecard

Audience: the owner of an objective. Cadence: the cadence of the key results. Level: whatever the objective's level is.

## Question

Are the key results moving toward their targets?

## Section order

1. Objective in one sentence.
2. Each key result: KPI, target, actual, direction, leading or lagging.
3. A bullet or variance mark per key result.
4. Initiatives, visually separate, so tasks are not mistaken for results.
5. The KRI paired with the objective, if one exists.

## Dashboards reused

The score zone of the dashboard specification. Do not paste the whole operational page.

## IBCS

One term per KPI, matching the catalog id's name. Targets share the KPI's formula.
""",
    "client-report.md": """
# Client report

Audience: the client and the agency lead. Context: `client`. Cadence: the contract's reporting cycle.

## Question

Did the work move the client's stated outcome, and how does that compare with what we said it would do?

## Section order

1. The client's objective and the agreed key results.
2. Actual versus the agreed target, with the definition in the client's words.
3. What changed in the period (leading activity that explains the result).
4. What we recommend next, tied to a metric.
5. Scope and data limits.

## Dashboards reused

The dashboard specification for the function the client buys (for example `library/DASHBOARDS/online-presence/conversion.md` or `library/DASHBOARDS/portfolio-and-project-management/delivery.md`), with the zones filled from the KPIs agreed in a `context: client` objective before this report is sent.

## IBCS

No internal benchmark presented as the client's target. No decorative donut of channel mix unless the mix is the question.
""",
    "operational-review.md": """
# Operational review

Audience: team leads. Cadence: week or day. Level: operational.

## Question

Is the process inside its corridor, and which queue or failure needs a change this cycle?

## Section order

1. Throughput, cycle time, and quality or defects.
2. A run or control chart if the question is "is this signal or noise?"
3. Aging or backlog of the queue.
4. The few entities (sites, lines, agents) outside the pattern.
5. The change to the process, not a pep talk.

## Dashboards reused

Operational dashboard specifications. Trend and distribution zones matter more than a single score.

## IBCS

Do not manage noise. A point inside historical variation is not a miss that needs a new target.
""",
    "pipeline-review.md": """
# Pipeline review

Audience: sales lead. Cadence: week. Level: tactical.

## Question

Is there enough qualified pipeline to hit the period, and where is it stuck?

## Section order

1. Pipeline value versus the coverage multiple of the quota.
2. Movement: created, advanced, slipped, lost. A waterfall.
3. Stage conversion, only if the stages are a real sequence.
4. Leading activity (demos, meetings) beside lagging win rate.
5. The accounts or reps that explain the gap.

## Dashboards reused

The pipeline and revenue dashboard specifications under `library/DASHBOARDS/sales-and-customer-service/`.

## IBCS

Funnel only for a true stage sequence. Coverage is a ratio against quota, not a vanity total.
""",
    "personal-review.md": """
# Personal or team review

Audience: the person and their manager. Cadence: week. Level: individual or team.

## Question

What did the person learn from their own indicators, and what will they change?

## Section order

1. The one or two outcomes the role owns.
2. The leading activity they control.
3. A comparison with their own prior period, not a public ranking.
4. Obstacles that sit in the system, separated from personal effort.
5. The next check.

## Dashboards reused

The score zone of the role's dashboard specification, filtered to the person's own scope.

## IBCS

No leaderboard as the page. Ranking belongs in an operational review of a process, not in a learning review of a person.
""",
}


STORIES = {
    "single-message.md": """
# Story: single message

Use when one comparison is the decision.

Open with the sentence the chart's title will repeat. Show one KPI, its comparison (target, prior, or peer), and the mark that encodes that comparison. Stop. A second chart is allowed only if it is the cause of the same sentence.

Chart pattern: bullet, variance bar, or a single line with a reference.

Failure: a title that names the topic ("Sales") and a chart that makes the reader invent the message.
""",
    "comparison.md": """
# Story: comparison

Use when the question is which entity is larger, or how two periods differ.

Sort bars by the value when the entities are nominal. Keep the axis honest. If the gap is the message, a diverging bar from the baseline is clearer than two separate columns the reader must subtract.

Chart pattern: horizontal bar, dumbbell, or slope.

Failure: alphabetical order that hides the ranking the sentence is about.
""",
    "pace-to-goal.md": """
# Story: pace to goal

Use when the question is whether the period will land on the target.

Show actual, the plan or the required run-rate, and the time left. A cumulative line against a plan line answers pace. A gauge does not, because it throws away the path.

Chart pattern: line with a target, or a bullet for the period score plus a small cumulative line.

Failure: a green tile that ignores the run-rate required for the remaining days.
""",
    "diagnostic.md": """
# Story: diagnostic

Use when the result is known and the question is why.

Start with the gap (variance). Bridge it with a waterfall whose steps are the formula's real inputs, not a decorative list. Then show the entities that hold most of the gap. End with the action and the indicator that will show the action worked.

Chart pattern: waterfall, then a sorted bar or a variance table.

Failure: a second copy of the score with no decomposition.
""",
    "part-to-whole.md": """
# Story: part to whole

Use when the mix itself is the decision (share of pipeline, share of cost, share of time).

Show the whole and the parts in one stacked bar or a table with shares. Label the parts. If there are many parts, group the tail. A pie is in the library and marked avoid for this job.

Failure: a donut of twelve slices with a legend.
""",
    "change-over-time.md": """
# Story: change over time

Use when the path matters more than the latest point.

One series, or a few labeled series, on a shared time axis. Annotate the event that explains a break. If many series must be compared, switch to small multiples or a horizon chart rather than spaghetti.

Failure: a dual axis that forces two unrelated series to look correlated.
""",
    "distribution.md": """
# Story: distribution

Use when the average would hide the decision (a few projects over budget, a long tail of cycle time).

Show the spread. A histogram, box, or dot plot. Mark the target as a reference line. Call out the tail in words.

Failure: a single average tile where the risk lives in the tail.
""",
    "flow.md": """
# Story: flow

Use when the question is how a quantity moves between states (leads to customers, cash through accounts, work through stages).

The stages must be a real sequence or a real conservation of a quantity. Sankey when the splits and merges matter. A funnel only for a narrowing sequence. Name what is lost between stages.

Failure: a funnel of unrelated categories.
""",
    "failure-impersonal.md": """
# Failure rule: impersonal dashboards

A dashboard that is not filtered to the viewer's responsibility invites browsing and blocks action. Personal and team reviews show the viewer's own scope. Executive packs show the organization and the few breaks, not every person's row.

Source pattern: the practice chapters of The Big Book of Dashboards (Steve Wexler, Jeffrey Shaffer, Andy Cotgreave; Wiley, 2017). This card is a rule, not the chapter.
""",
    "failure-time.md": """
# Failure rule: time encoded badly

Time is an axis, not a color legend and not a slice of a pie. Period comparisons that matter (versus prior, versus year ago) are explicit series or variance columns. Do not ask the reader to remember last month's screenshot.

Same source as the other failure rules. Rule only.
""",
    "failure-dead-end.md": """
# Failure rule: dead-end dashboard

If the reader cannot go from the score to the entity they must act on, the page is a dead end. Every score zone in this library has a breakdown or a detail zone, even when the visual template is still a placeholder.

Same source. Rule only.
""",
    "failure-red-green.md": """
# Failure rule: red and green as the only signal

Color-blind readers and grayscale prints lose the only encoding. Sign, position, and a label have to carry the variance. Traffic-light tiles used as the only mark fall under the `avoid` rule in `library/STANDARDS/ibcs-success.md`.

Same source. Rule only.
""",
    "failure-pies.md": """
# Failure rule: pies and donuts

Angles are a weak encoding for the comparisons this library cares about (rank, trend, deviation). Pie and donut cards stay in the chart library so they can be recognized and refused for management stories. Use a bar or a table of shares.

Same source. Rule only.
""",
    "failure-clouds-bubbles.md": """
# Failure rule: clouds and bubbles

Area and unordered bubbles hide magnitude and invite a reading of precision the area encoding cannot support. Use bubbles only when a third variable is real and the audience is analytical. Prefer position and length.

Same source. Rule only.
""",
}


def main() -> int:
    for name, body in CHAPTERS.items():
        write(THEORY / name, body)
    write(THEORY / "index.md", "\n".join([
        "# Performance management primer",
        "",
        "Original primer for this library. It does not quote the source books. Generated by `chart-expert/scripts/write_foundations.py`.",
        "",
        "1. [01-on-performance](01-on-performance.md)",
        "2. [02-performance-management-and-measurement](02-performance-management-and-measurement.md)",
        "3. [03-performance-management-levels](03-performance-management-levels.md)",
        "4. [04-history-of-performance-management](04-history-of-performance-management.md)",
        "5. [05-theory-informing-performance-management](05-theory-informing-performance-management.md)",
        "6. [06-principles-of-performance-measurement](06-principles-of-performance-measurement.md)",
        "7. [07-metrics-kpis-kris-and-analytics](07-metrics-kpis-kris-and-analytics.md)",
        "8. [08-types-of-kpis](08-types-of-kpis.md)",
        "9. [09-characteristics-of-good-kpis](09-characteristics-of-good-kpis.md)",
        "10. [10-kpis-formulation-and-selection](10-kpis-formulation-and-selection.md)",
        "11. [11-working-with-targets](11-working-with-targets.md)",
        "12. [12-using-kpis](12-using-kpis.md)",
        "13. [13-kpi-pitfalls](13-kpi-pitfalls.md)",
        "14. [14-kpi-visualisation-and-software](14-kpi-visualisation-and-software.md)",
        "15. [15-key-directions-for-performance-management](15-key-directions-for-performance-management.md)",
        "",
        "Notation: `library/STANDARDS/ibcs-success.md`.",
        "Walk: `references/selection-playbook.md`.",
    ]))
    write(STAND / "ibcs-success.md", IBCS)
    for name, body in REPORTS.items():
        write(REPORTS_DIR / name, "---\ntype: report\n---\n" + body)
    write(REPORTS_DIR / "index.md", "# Reports\n\nGenerated by `chart-expert/scripts/write_foundations.py`.\n\n" + "\n".join(f"- [{n}]({n})" for n in REPORTS))
    for name, body in STORIES.items():
        write(STORIES_DIR / name, "---\ntype: story\n---\n" + body)
    write(STORIES_DIR / "index.md", "# Stories\n\nGenerated by `chart-expert/scripts/write_foundations.py`.\n\n" + "\n".join(f"- [{n}]({n})" for n in STORIES))
    for path in CHANGED:
        print(("would change: " if CHECK else "wrote: ") + path.relative_to(ROOT.parent).as_posix())
    print("foundations", len(CHAPTERS), "chapters", len(REPORTS), "reports", len(STORIES), "stories", "changed", len(CHANGED))
    return 1 if CHECK and CHANGED else 0


if __name__ == "__main__":
    sys.exit(main())
