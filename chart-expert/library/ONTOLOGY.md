# Ontology

These words are fixed for every card in this library. An agent should not treat them as synonyms.

## Measure

A measure is a number plus a unit. The number is the magnitude. The unit says what the magnitude is (dollars, hours, people, percent). A measure can be observed directly. It does not, by itself, say whether the result is good.

## Metric

A metric is any quantified measure used to describe a result. Metrics include inputs, activity counts, and diagnostic breakdowns. A metric does not have to be on a scorecard.

## Sub-metric

A sub-metric is a named input to a formula. In "gross profit margin = gross profit / revenue", gross profit and revenue are sub-metrics. They live in the metrics library. The margin lives in the KPI library and cites them.

## Performance indicator

A performance indicator is a metric chosen to judge a result against a direction or a target. Many indicators can describe a process. Few of them should steer it.

## KPI

A KPI is a performance indicator selected because it tracks an objective, an outcome, or a key result that matters to a decision. A KPI is not "every number we can query." If a department lists forty KPIs, most of them are metrics. The KPI is the short list a manager would act on.

A finished KPI card has a definition, a unit, a formula, sub-metrics, a direction, a leading or lagging label, the question it answers, and at least one chart. A dashboard is one place that chart may appear. It is not the only place.

## Audience and surface

The audience is part of the specification. Reader roles are a fixed list, and each role reads charts at one of the four tolerances chart cards use (`audience:` in a chart card):

| Role | Chart tolerance |
|---|---|
| Executive, Client, HR business partner, Marketing lead | `Executive` |
| Marketing analytics, Data analytics | `Analytics` |
| Data scientist, Researcher, R&D, Development | `Technical` |
| Public | `Public` |

KPI cards and dashboard specifications list roles (`audience_roles`); chart cards list tolerances (`audience`). An agency principal is an Executive; a client sponsor is a Client. The first group needs a short comparison it can act on. The technical group often needs the distribution, the residual, the diagnostic plot, or the model check. Those charts stay in the library. They are not mistakes.

The same finding can use two surfaces:

- **Analysis.** A Jupyter notebook, a pandas or matplotlib plot, an exploratory dashboard for analysts. Complexity follows the question.
- **Communication.** A dashboard, a report, or a story for the people who decide. The chart may be a simpler cousin of the one used in analysis.

`ibcs_status: avoid` removes a chart from Executive, Public, and client communication surfaces (dashboard, report, story). It stays eligible on Analytics and Technical analysis surfaces (notebook, exploratory plot). It does not mean the chart is removed, and it does not mean a data scientist should avoid it in a notebook.

## KRI

A KRI is a key risk indicator. It tracks exposure, failure, or breach (spills, downtime, concentration, compliance misses). It is not a success target. The schema is the same as a KPI, with `measure_kind: kri`; the id keeps the `kpi.` prefix so one lookup covers both. Improving a KRI usually means driving it down or keeping it inside a corridor.

## OMTM

The one metric that matters is the single focus metric for a business model or a bet. It is a KPI, not a new kind of math. A company still has a scorecard. The OMTM is the metric that, if it moved and nothing else did, would change the decision.

## Objective

An objective is a qualitative theme: significant, concrete, and action-oriented. It states what should become true. It does not contain the number.

## Key result

A key result is the quantitative evidence that the objective is happening. It cites one KPI, a target, a direction, and a cadence; the direction is the KPI's own. Two to five key results per objective is the working range, usually three. A task ("hire a bookkeeper", "update the website") is an initiative, not a key result, until it has a number that measures an outcome.

## Target

A target is the number on a KPI or a key result. A benchmark from a published rule of thumb (for example team cost as a share of gross profit) is a target note. It is not a universal law. The card says where the number came from.

## Leading and lagging

A leading indicator moves before the outcome and is usually an activity, a stock of work, or a quality of input. A lagging indicator records the outcome after it has happened (revenue, profit, churn, incidents already closed). A dashboard that contains only lagging indicators can explain the past and cannot steer the week.

## Units

The `unit` field of a KPI takes one of:

- `currency`: a monetary stock or flow
- `percent`: a ratio scaled to 100
- `number`: a ratio, index, or score that is not a percent
- `count`: things counted in the period
- `days`, `hours`, `months`: a duration

## Context and level

- `context` on an OKR says whose result it is: `internal` (the organization's own), `project` (one engagement), or `client` (a result reported in the client's numbers).
- `level` on an OKR says who owns it: `company`, `function`, or `team`.
- `level` on a KPI says the decision horizon it serves: `strategic`, `tactical`, or `operational`.

## How the objects connect

Audience and question choose an OMTM and an objective. The objective's key results cite KPIs. Each KPI cites sub-metrics and a chart. The chart sits in a dashboard zone. The dashboard is carried by a report. The report is told as a story. The story follows the notation rules in `library/STANDARDS/ibcs-success.md`.

Links run both ways. A chart names the questions it can answer and the KPIs that cite it (`related_kpis`). A KPI names its charts and its dashboard. A dashboard specification names its reader roles, its KPIs, and their charts. An OMTM card names its KPI.
