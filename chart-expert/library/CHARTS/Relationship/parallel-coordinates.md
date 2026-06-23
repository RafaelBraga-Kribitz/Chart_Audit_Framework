---
name: Parallel Coordinates
category: Relationship
input_type: [cat-multi-value, demo-grouped]
it_variants: []
analytical_function: Correlation
visual_family: Chart
shape_primitive: [Line]
cardinality_fit: [medium, large]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, color-hue, color-value]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi]
failure_modes: [E, J]
alternatives: [scatter-matrix, heat-map, radar-chart, 3d-scatter-plot]
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

# Parallel Coordinates

## Description
A Parallel Coordinates Plot visualises multivariate numerical data by arranging each variable on its own vertical axis, with all axes drawn in parallel and equidistant from each other. Each data observation is represented as a polyline that crosses all axes at the position corresponding to its value on each variable. The resulting bundle of lines reveals correlations (lines that cross between two axes indicate negative correlation; lines that are parallel indicate positive correlation), clusters (lines that converge into bands), and outliers (lines that deviate from the main bundle). Axes can be reordered to bring adjacent variables next to each other for clearer pattern detection.

## When to Use
- Exploring relationships and correlations across many numeric variables simultaneously
- Identifying clusters of observations that behave similarly across multiple dimensions
- Comparing multi-attribute profiles of entities (e.g., computer models, car specs, patient profiles)
- Detecting outliers that are unusual on multiple dimensions simultaneously
- When the number of variables exceeds what can be shown in a scatter matrix

## When NOT to Use
- When n is very large (> ~500) without interactivity — lines overlap into an unreadable mass
- When variables are categorical and ordinal categories are not meaningfully ordered
- For non-technical audiences — the line-crossing correlation convention is not intuitive
- When only 2–3 variables need comparison (use scatter plot or bar chart instead)

## Data Requirements
- Multiple (3+) continuous numeric columns
- Optional: a categorical column for colour-coding lines by group
- n between 20 and ~500 for static charts; up to thousands with interactive brushing
- Variables benefit from normalisation/standardisation for cross-axis comparison (unless the raw scale is meaningful)

## Best Practices
- Normalise all axes to 0–1 or z-scores when variables have different units and scales
- Use "brushing" (interactive axis range selection) to highlight subsets and filter out noise
- Reorder axes thoughtfully — variables expected to be correlated should be adjacent
- Use colour to encode class membership or a key numeric variable
- Apply transparency to lines to reveal density — heavily overlapping lines should be semi-transparent

## Common Mistakes
- E (MC-noise-as-difference): interpreting crossing patterns between two axes as definitive negative correlation without computing the actual correlation coefficient
- J (silently-dropped-categories): observations with missing values on any axis are often silently dropped — document this
- Displaying too many lines without brushing or transparency — the chart becomes a solid block of colour
- Not normalising axes — variables with very different scales make the chart unreadable as lines cluster near extreme ends

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.path import Path
import matplotlib.patches as mpatches

# Normalise columns
df_norm = (df[cols] - df[cols].min()) / (df[cols].max() - df[cols].min())
x = list(range(len(cols)))

fig, axes = plt.subplots(1, len(cols) - 1, sharey=False, figsize=(12, 5))
for i, ax in enumerate(axes):
    for j, row in df_norm.iterrows():
        ax.plot([0, 1], [row[cols[i]], row[cols[i+1]]], alpha=0.3, color='steelblue')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([0, 1])
    ax.set_xticklabels([cols[i], cols[i+1]])
plt.tight_layout()
```
For a cleaner implementation, use `pd.plotting.parallel_coordinates(df, 'class_column')`.

### plotly
```python
import plotly.express as px
fig = px.parallel_coordinates(df, color='class_col',
                              dimensions=numeric_cols,
                              color_continuous_scale=px.colors.sequential.Viridis)
fig.show()
```
`px.parallel_coordinates` is fully interactive with built-in brushing on each axis.

### altair
Altair does not have a native parallel coordinates mark. Use `vega-embed` with the Vega parallel coordinates example or pre-transform to long format and layer line marks.

### excel / tableau
- **Excel**: No native parallel coordinates. Use Spider/Radar chart as a limited approximation.
- **Tableau**: No native implementation. Requires a calculated field trick transforming data to long format and using Lines + Axis Number encoding.
