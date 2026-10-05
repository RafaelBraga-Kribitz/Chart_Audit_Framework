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

The audience is part of the specification. Executive, public, HR business partner, marketing lead, and agency principal need a short comparison they can act on. Researcher, R&D, data scientist, marketing analytics, data analytics, and development teams often need the distribution, the residual, the diagnostic plot, or the model check. Those charts stay in the library. They are not mistakes.

The same finding can use two surfaces:

- **Analysis.** A Jupyter notebook, a pandas or matplotlib plot, an exploratory dashboard for analysts. Complexity follows the question.
- **Communication.** A dashboard, a report, or a story for the people who decide. The chart may be a simpler cousin of the one used in analysis.

`ibcs_status: avoid` means "do not use this as the mark in executive or client communication." It does not mean the chart is removed, and it does not mean a data scientist should avoid it in a notebook.

## KRI

A KRI is a key risk indicator. It tracks exposure, failure, or breach (spills, downtime, concentration, compliance misses). It is not a success target. The schema is the same as a KPI, with `measure_kind: kri`. Improving a KRI usually means driving it down or keeping it inside a corridor.

## OMTM

The one metric that matters is the single focus metric for a business model or a bet. It is a KPI, not a new kind of math. A company still has a scorecard. The OMTM is the metric that, if it moved and nothing else did, would change the decision.

## Objective

An objective is a qualitative theme: significant, concrete, and action-oriented. It states what should become true. It does not contain the number.

## Key result

A key result is the quantitative evidence that the objective is happening. It cites one KPI, a target, a direction, and a cadence. One to three key results per objective is the working range. A task ("hire a bookkeeper", "update the website") is an initiative, not a key result, until it has a number that measures an outcome.

## Target

A target is the number on a KPI or a key result. A benchmark from a published rule of thumb (for example team cost as a share of gross profit) is a target note. It is not a universal law. The card says where the number came from.

## Leading and lagging

A leading indicator moves before the outcome and is usually an activity, a stock of work, or a quality of input. A lagging indicator records the outcome after it has happened (revenue, profit, churn, incidents already closed). A dashboard that contains only lagging indicators can explain the past and cannot steer the week.

## Unit prefixes

- `$` currency or other monetary stock or flow
- `#` count, duration, or a ratio that is not expressed as a percent
- `%` a ratio scaled to 100

## How the objects connect

Audience and question choose an OMTM and an objective. The objective's key results cite KPIs. Each KPI cites sub-metrics and a chart. The chart sits in a dashboard zone. The dashboard is carried by a report. The report is told as a story. The story follows the notation rules in `library/STANDARDS/ibcs-success.md`.

Links run both ways. A chart names the questions it can answer. A KPI names the chart and the dashboard. A dashboard names the audience, the OMTM, the KPIs, and the charts.
