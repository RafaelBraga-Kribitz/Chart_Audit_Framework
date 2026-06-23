---
name: Error Bars
category: Comparison
input_type: [cat-value, interval-range]
it_variants: []
analytical_function: Deviation
visual_family: Chart
shape_primitive: [Bar, Line]
cardinality_fit: [small-N, medium]
audience: [Technical, Analytics]
complexity: Intermediate
encoding_channels: [position, length]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [C, B, E]
alternatives: [span-chart, column-range, violin-plot, box-plot]
source: [datavizproject, datavizcatalogue]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
---

# Error Bars

## Description
Error bars are graphical embellishments added to point estimates (on bar charts, line charts, or dot plots) to show the uncertainty or variability around each value. A typical error bar extends above and below the central estimate by a defined amount: standard error, standard deviation, confidence interval width, or a custom range. They communicate both the central tendency and the precision or spread of a measurement.

## When to Use
- Scientific and analytical charts where uncertainty must be communicated alongside estimates
- Comparing group means and assessing whether differences are statistically meaningful
- Showing variability of repeated measurements across experimental conditions
- When the central value alone would misrepresent the reliability of the estimate

## When NOT to Use
- The error metric is unknown or undefined (error bars with arbitrary lengths are misleading)
- Data has zero variance and error bars would collapse to points — see Smell B
- Audience is a general public who may not know how to interpret the specific error metric
- Monte Carlo noise is being confused with true estimation uncertainty — see Smell E

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | The groups or conditions |
| central | numeric | The point estimate (mean, median) |
| error_lower | numeric | Distance below central (or full lower bound) |
| error_upper | numeric | Distance above central (or full upper bound) |

## Best Practices
- Always label what the error bars represent: SD, SE, 95% CI, IQR, or min/max
- Use symmetric error bars only when the interval is truly symmetric
- Cap the ends of error bars with short horizontal ticks for legibility
- Do not mislabel SEM bars as confidence intervals — they have different interpretations — see Smell C
- For small sample sizes, individual data points should be shown alongside error bars

## Common Mistakes
- Not specifying what the error bars represent in the chart title or caption — see Smell C
- Treating Monte Carlo noise as a meaningful uncertainty estimate — see Smell E
- Showing error bars for a metric with definitionally zero variance — see Smell B
- Using error bars so large that the central value is visually swamped

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(categories, means, yerr=[lower_errors, upper_errors],
       capsize=5, color='steelblue', error_kw={'linewidth': 1.5})
ax.set_ylabel('Mean ± 95% CI')
plt.tight_layout()
```
`yerr` can be a 2-row array `[lower, upper]` for asymmetric bars.

### plotly
`go.Bar(error_y=dict(type='data', symmetric=False, array=upper_errors, arrayminus=lower_errors))`

### altair
`alt.Chart(df).mark_errorbar().encode(x='category:N', y='central:Q', yError='error:Q')` — also layer with `mark_point` or `mark_bar`.

### excel / tableau
Excel: Right-click data series > Add Error Bars > Custom; specify positive/negative ranges. Tableau: Analytics pane > Add Reference Band; or use dual-axis with error bar fields.
