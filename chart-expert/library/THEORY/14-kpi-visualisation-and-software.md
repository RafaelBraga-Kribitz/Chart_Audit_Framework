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

Dashboards in this library are zone grids (score, trend, breakdown, variance, detail). A placeholder dashboard is still a specification: which KPI, which chart, which source. Scraped Databox and Zebra templates are concrete layouts when a link exists. They do not replace the formula.

## Rule

Choose the chart from the analytical function and the IBCS status. Then choose the tool. Never the other way around.

## Worked example

DSO versus a 45-day target, monthly, for an executive: bullet or a line with a target, plus an aging stacked bar in the breakdown zone. The tool can be a spreadsheet or Power BI. The gauge is rejected even if it is the tool's default.

## Failure this chapter prevents

A tool demo that dictates both the KPI list and the chart.

## Open next

`references/selection-playbook.md` and `15-key-directions-for-performance-management.md`.
