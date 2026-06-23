---
name: Box Plot
category: Distribution
input_type: [cat-value, demo-grouped]
it_variants: []
analytical_function: Distribution
visual_family: Plot
shape_primitive: [Bar, Line]
cardinality_fit: [medium, large, very-large]
audience: [Analytics, Technical]
complexity: Basic
encoding_channels: [position, length]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [E, G]
alternatives: [violin-plot, strip-plot, beeswarm-plot, density-plot]
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

# Box Plot

## Description
A Box Plot (also called Box-and-Whisker Plot) summarises the distribution of a continuous variable through five statistics: minimum, first quartile (Q1), median, third quartile (Q3), and maximum. The box spans Q1 to Q3 (the interquartile range, IQR); a line inside marks the median; whiskers extend to the furthest non-outlier values (typically 1.5 × IQR); and individual points beyond the whiskers are plotted as outliers. Box plots excel at comparing distributions across multiple groups in a compact space.

## When to Use
- Comparing the central tendency and spread of a continuous variable across groups
- Quickly identifying skewness and outliers in each group
- Displaying many groups side-by-side where a full histogram per group would be overwhelming
- QA workflows where per-group summary statistics need rapid scanning

## When NOT to Use
- When the distribution is multimodal — the box will not reveal multiple peaks (use violin plot instead)
- When n per group is very small (< 10) — five-number summaries are misleading on tiny samples
- When the audience needs to see the actual data density shape, not just quartiles
- When communicating to a non-technical audience unfamiliar with quartiles

## Data Requirements
- One continuous numeric column (the value)
- One categorical column for grouping (optional, but most useful with groups)
- Minimum recommended n per group: ~20 for summary stats to be reliable

## Best Practices
- Orient horizontally when group label names are long
- Overlay individual data points (jitter) when n per group is small (< 100) to show actual distribution
- Use notched box plots to visualise confidence intervals around the median for significance testing hints
- Always clarify whisker definition in a footnote (1.5 × IQR is standard but not universal)
- Sort groups by median for ranked comparison rather than alphabetically

## Common Mistakes
- E (MC-noise-as-difference): treating visual overlap of boxes as evidence of no difference without a test
- G (KDE-over-atoms): adding a smoothed overlay to groups with very few observations
- Hiding bimodality — a flat, symmetric box can describe either a uniform or bimodal distribution identically
- Using variable-width whiskers without documenting the rule used
- Cutting the y-axis above zero when outliers exist, causing them to disappear off-chart

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.boxplot([group_a, group_b, group_c], labels=['A', 'B', 'C'],
           notch=False, sym='o', whis=1.5)
ax.set_ylabel('Value')
plt.tight_layout()
```
Use `notch=True` for confidence-interval notches. `showfliers=False` hides outlier points.

### plotly
```python
import plotly.express as px
fig = px.box(df, x='group', y='value', points='outliers')
fig.show()
```
`points='all'` overlays all raw points. `notched=True` adds notches.

### altair
```python
import altair as alt
alt.Chart(df).mark_boxplot().encode(
    x='group:N',
    y='value:Q'
)
```
`mark_boxplot(extent=1.5)` controls whisker rule. Add `color='group:N'` for colour coding.

### excel / tableau
- **Excel**: Insert > Statistical Chart > Box and Whisker (Excel 2016+). Right-click for quartile exclusion options.
- **Tableau**: Drag dimension to Columns, measure to Rows; Show Me > Box-and-Whisker Plot. Use Analytics pane to add reference lines.
