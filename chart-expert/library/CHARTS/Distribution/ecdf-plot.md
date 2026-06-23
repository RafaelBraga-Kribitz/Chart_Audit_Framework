---
name: ECDF Plot
category: Distribution
input_type: [xy-simple, cat-value]
it_variants: []
analytical_function: Distribution
visual_family: Plot
shape_primitive: [Line, Dot]
cardinality_fit: [medium, large, very-large]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position]
tool_support: [matplotlib, plotly, altair, d3, tableau]
failure_modes: [E, C]
alternatives: [histogram, density-plot, qq-plot, box-plot]
source: [datavizproject]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
---

# ECDF Plot

## Description
An Empirical Cumulative Distribution Function (ECDF) plot displays the proportion of observations that fall at or below each value of a continuous variable. The x-axis shows the variable's value and the y-axis shows the cumulative proportion (0 to 1). For n observations, the curve steps up by 1/n at each observed value. Unlike a histogram or density plot, the ECDF requires no binning or smoothing — it is a non-parametric, exact representation of the data. It enables direct reading of any percentile and facilitates precise group comparisons.

## When to Use
- When exact percentile reading is required (e.g., "what fraction of users have latency < 200ms?")
- Comparing two or more distributions precisely without binning artefacts
- Checking distributional assumptions (e.g., comparing to a theoretical CDF)
- When the histogram bin count choice is contentious and you need a bin-free alternative
- Communicating service level objectives and performance benchmarks

## When NOT to Use
- When the audience needs an intuitive "shape" reading — CDFs are less intuitive than histograms for non-technical audiences
- When the distribution's mode (peak) is the primary message (density plots are better)
- When n is so large that individual steps are invisible and a smooth CDF line would be more readable

## Data Requirements
- One continuous numeric column
- Optional: a grouping column for overlaid multi-group ECDFs
- Works at any n; steps are visible at small n, nearly continuous at large n

## Best Practices
- Label the y-axis as "Cumulative proportion" or "P(X ≤ x)" — not "probability" of a specific point
- Add reference lines at key percentiles (25th, 50th, 75th, 95th, 99th) for reading convenience
- Use open/closed dot conventions to indicate step direction (left-continuous vs. right-continuous)
- When comparing groups, use the same colour scheme and include a legend
- For very large n, plot as a thin line without individual step markers

## Common Mistakes
- C (percentile-mislabeled-HDI): labelling a range as "the 90th percentile" when it is the 90th percentile threshold (a value, not an interval)
- E (MC-noise-as-difference): concluding two ECDFs represent different distributions based on visual gap without a KS test or confidence bands
- Confusing the ECDF with the survival function (1 − ECDF) — both are valid but serve different contexts
- Plotting an ECDF on a log y-scale without labelling — the steps at extreme tails become visible but the interpretation changes

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np

sorted_data = np.sort(data)
y = np.arange(1, len(data) + 1) / len(data)

fig, ax = plt.subplots()
ax.step(sorted_data, y, where='post', linewidth=1.5, label='ECDF')
ax.set_xlabel('Value')
ax.set_ylabel('Cumulative proportion')
ax.set_ylim(0, 1)
ax.axhline(0.5, color='grey', linestyle='--', linewidth=0.8, label='Median')
plt.tight_layout()
```
Or: `sns.ecdfplot(data=df, x='value')`

### plotly
```python
import plotly.express as px
fig = px.ecdf(df, x='value', color='group')
fig.show()
```
`ecdfnorm='percent'` scales y-axis to 0–100. `marginal='rug'` adds a rug plot.

### altair
```python
import altair as alt
alt.Chart(df).mark_line(interpolate='step-after').encode(
    x='value:Q',
    y=alt.Y('cumulative_count:Q', title='Cumulative proportion')
).transform_window(
    cumulative_count='cume_dist()',
    sort=[alt.SortField('value')]
)
```

### excel / tableau
- **Excel**: Sort data, compute running count / total n with COUNTIF or manual formula, plot as step line chart.
- **Tableau**: Use a `RUNNING_COUNT(COUNT([value])) / TOTAL(COUNT([value]))` table calculation; plot as Line with step interpolation.
