---
name: Bubble Chart
category: Relationship
input_type: [xyz-trivariate, cat-multi-value]
it_variants: []
analytical_function: Correlation
visual_family: Chart
shape_primitive: [Circle]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical, Executive]
complexity: Intermediate
encoding_channels: [position, area, color-hue, color-value]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [F, K, E]
alternatives: [scatter-plot, connected-scatter-plot, 3d-scatter-plot, matrix-diagram]
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

# Bubble Chart

## Description
A Bubble Chart is a multi-variable chart that extends the scatter plot by encoding a third numeric variable through the area of each plotted circle (bubble). Like a scatter plot, the x and y axes represent two continuous variables; unlike a scatter plot, each data point is drawn as a circle whose size is proportional to a third value. Colour can optionally encode a fourth variable (category or magnitude). Bubble charts are widely used to compare entities along three simultaneous numeric dimensions — a classic example being GDP, life expectancy, and population for countries.

## When to Use
- Displaying the relationship among three continuous numeric variables for a set of entities
- Comparing entities (countries, products, segments) across three dimensions simultaneously
- Making the relative magnitude of a third variable visually intuitive (via bubble size)
- Animated bubble charts to show change over time as a fourth dimension (e.g., Gapminder-style)

## When NOT to Use
- When the number of data points is large (> ~30–40) — bubbles overlap and become illegible
- When exact size comparison is critical — area perception is imprecise
- When all three variables carry equal analytical weight — a parallel coordinates chart may be more readable
- When the third variable has a very wide range — small bubbles become invisible next to large ones

## Data Requirements
- Two continuous numeric columns for x and y position
- One continuous numeric column for bubble size (must be non-negative)
- Optional: a categorical or numeric column for bubble colour
- Optional: a label column for bubble annotations
- n between 5 and ~40 for readable charts

## Best Practices
- Scale bubble area proportional to the value, never radius or diameter (smell F)
- Include a size legend with labelled reference bubbles at known values
- Use transparency (alpha 0.5–0.7) to handle overlap
- Label notable bubbles directly; provide tooltips for interactive charts
- Avoid more than 2–3 colour groups — more become indistinguishable

## Common Mistakes
- F (bounding-box-geometry): scaling radius (not area) to the value causes exponential distortion — a value of 4 looks 4× larger in radius but 16× larger in area
- K (self-correlated scatter): plotting ratio variables where numerator or denominator appears on an axis
- E (MC-noise-as-difference): interpreting small bubble size differences as meaningful when the underlying difference is within measurement error
- Omitting a size legend — readers cannot extract absolute values from bubble area without reference

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
# Scale area: s = value * scale_factor (area, not radius)
scatter = ax.scatter(x, y, s=size_values * 10, c=color_values,
                     cmap='tab10', alpha=0.6, edgecolors='white', linewidth=0.5)
plt.colorbar(scatter, ax=ax, label='Colour variable')
ax.set_xlabel('X Variable')
ax.set_ylabel('Y Variable')
# Size legend
for ref_size in [10, 100, 1000]:
    ax.scatter([], [], s=ref_size * 10, c='grey', alpha=0.5,
               label=f'{ref_size}')
ax.legend(title='Size variable', labelspacing=1.5)
plt.tight_layout()
```

### plotly
```python
import plotly.express as px
fig = px.scatter(df, x='x', y='y', size='size_var',
                 color='category', hover_name='label',
                 size_max=60, opacity=0.7)
fig.show()
```
`animation_frame='year'` adds Gapminder-style time animation.

### altair
```python
import altair as alt
alt.Chart(df).mark_circle(opacity=0.7).encode(
    x='x:Q',
    y='y:Q',
    size=alt.Size('size_var:Q', scale=alt.Scale(range=[50, 2000])),
    color='category:N',
    tooltip=['label', 'x', 'y', 'size_var']
)
```

### excel / tableau
- **Excel**: Insert > Chart > Bubble. Assign x, y, and bubble size series. Format > Data Labels for annotations.
- **Tableau**: Drag two measures to Rows and Columns; drag third measure to Size shelf; set mark to Circle.
