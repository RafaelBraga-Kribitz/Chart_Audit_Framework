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
