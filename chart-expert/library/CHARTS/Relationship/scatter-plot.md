---
name: Scatter Plot
category: Relationship
input_type: [xy-simple, xy-dual-series]
it_variants: []
analytical_function: Correlation
visual_family: Plot
shape_primitive: [Dot]
cardinality_fit: [medium, large, very-large]
audience: [Analytics, Technical]
complexity: Basic
encoding_channels: [position, color-hue, shape, area]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [K, E]
alternatives: [bubble-chart, connected-scatter-plot, hexagonal-binning, contour-plot]
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

# Scatter Plot

## Description
A Scatter Plot (also called Scatter Graph, Point Graph, X-Y Plot, or Scattergram) places individual data points on a Cartesian coordinate system where each axis represents a distinct continuous variable. The resulting pattern of points reveals whether and how the two variables are related — positively, negatively, or not at all — and whether the relationship is linear, exponential, or U-shaped. Additional variables can be encoded through colour, shape, or point size, enabling up to five dimensions on a single chart. A trend line or line of best fit is commonly overlaid to make the relationship direction and strength explicit.

## When to Use
- Exploring the relationship or correlation between two continuous variables
- Detecting clusters, gaps, outliers, and non-linear patterns in paired data
- Comparing multiple groups' bivariate distributions when colour/shape encodes groups
- Supporting or refuting hypotheses about variable relationships in exploratory analysis
- Displaying paired measurements (e.g., predicted vs. actual, before vs. after)

## When NOT to Use
- When n is so large (> ~10,000) that overplotting obscures all structure (use hexbin or contour instead)
- When both variables are categorical (use a mosaic/contingency chart or heatmap instead)
- When the causal direction is not established — scatter plots show correlation, not causation
- When the audience will mistake visual clustering for statistical significance without supporting tests
- When there is only one variable (use histogram or box plot instead)

## Data Requirements
- Two continuous numeric columns (x and y)
- Optional: a categorical column for colour/shape grouping
- Optional: a third numeric column for point size (creates a bubble chart)
- n >= 10 for any meaningful pattern; ideal range 30 – 10,000

## Best Practices
- Add a trend line (linear regression or LOESS) to make the relationship direction legible
- Label axis units and include a descriptive axis title, not just variable names
- Use alpha transparency (0.3–0.6) to reveal density when points overlap
- Annotate notable outliers by label if they are interpretively significant
- Include the correlation coefficient (r) and p-value in the caption or subtitle if it is an analytical chart
- Square the axes when plotting residuals vs. fitted values to aid interpretation

## Common Mistakes
- K (self-correlated scatter): plotting a derived variable on one axis that is algebraically constructed from the other (e.g., ratio vs. denominator) creates spurious correlation
- E (MC-noise-as-difference): treating a visually apparent cluster as a distinct population without a statistical test
- Conflating correlation with causation in chart titles or annotations
- Using a logarithmic axis without labelling it clearly
- Plotting many more than 3–4 colour-coded groups — beyond that, colour is indistinguishable

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
scatter = ax.scatter(x, y, c=color_values, alpha=0.6, cmap='tab10', s=30)
ax.set_xlabel('Variable X')
ax.set_ylabel('Variable Y')
ax.set_title('Scatter Plot')
# Add trend line
m, b = np.polyfit(x, y, 1)
ax.plot(np.sort(x), m * np.sort(x) + b, color='red', linewidth=1.5)
plt.tight_layout()
```

### plotly
```python
import plotly.express as px
fig = px.scatter(df, x='x', y='y', color='group',
                 trendline='ols', trendline_scope='overall',
                 opacity=0.7)
fig.show()
```
`trendline='lowess'` for non-linear. `marginal_x='histogram'` adds marginal distributions.

### altair
```python
import altair as alt
points = alt.Chart(df).mark_circle(opacity=0.6).encode(
    x='x:Q', y='y:Q', color='group:N', tooltip=['x', 'y', 'group']
)
trend = points.transform_regression('x', 'y').mark_line(color='red')
(points + trend).interactive()
```

### excel / tableau
- **Excel**: Insert > Chart > Scatter. Add trendline via right-click > Add Trendline.
- **Tableau**: Drag two measures to Rows and Columns; mark type automatically becomes Scatter. Analytics pane > Trend Line to overlay.
