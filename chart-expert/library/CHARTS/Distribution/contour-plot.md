---
name: Contour Plot
category: Distribution
input_type: [xy-simple, xyz-trivariate]
it_variants: []
analytical_function: Distribution
visual_family: Plot
shape_primitive: [Line, Area]
cardinality_fit: [large, very-large]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, color-value, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau]
failure_modes: [G, E]
alternatives: [hexagonal-binning, heat-map, scatter-plot, density-plot]
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

# Contour Plot

## Description
A Contour Plot represents a three-dimensional surface on a two-dimensional plane using isolines (contour lines) that connect points of equal value. In the context of data distribution, contour plots most commonly show the estimated bivariate probability density of two continuous variables — each contour line encloses a region of equal estimated density. Filled contour plots (contourf) shade the regions between isolines with colour, while unfilled versions show lines only. They are the bivariate analogue of a density plot.

## When to Use
- Visualising the joint distribution of two continuous variables on a 2D plane
- Detecting correlation, clustering, and multimodality in bivariate data
- Overlaying distribution summaries on a scatter plot for large-n datasets where individual points overplot
- Scientific and engineering contexts requiring isovalue display of a function over a grid

## When NOT to Use
- When n is small (< ~100) — bivariate KDE contours are unreliable (smell G)
- When audiences need exact values rather than approximate density contours (use hexbin or scatter with colour)
- When the data has hard boundaries that the KDE would violate without correction
- When there is no interpretable joint structure between the two variables

## Data Requirements
- Two continuous numeric columns (x and y)
- n >= 100 recommended for bivariate KDE; >= 300 for reliable contour shape
- Optional: a third numeric column for a true z-value grid (if not computing KDE from scatter)

## Best Practices
- Choose contour level spacing to highlight meaningful density thresholds (e.g., 50%, 90%, 99% probability mass)
- Use a perceptually uniform colour scale for filled contours (viridis, plasma)
- Overlay raw scatter points at reduced alpha to show actual data alongside the contour estimate
- Label contour lines or include a colour legend for the fill scale
- Document the KDE kernel and bandwidth method when publishing

## Common Mistakes
- G (KDE-over-atoms): computing contours from too few points gives misleadingly smooth, confident-looking shapes
- E (MC-noise-as-difference): treating a contour that barely separates two groups as evidence of real separation
- Using the wrong number of levels — too few hide structure, too many create visual noise
- Confusing a filled contourf (colour bands) with a wireframe 3D surface plot

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

xy = np.vstack([x, y])
kde = gaussian_kde(xy)
xi, yi = np.mgrid[x.min():x.max():100j, y.min():y.max():100j]
zi = kde(np.vstack([xi.ravel(), yi.ravel()])).reshape(xi.shape)

fig, ax = plt.subplots()
ax.contourf(xi, yi, zi, levels=10, cmap='viridis')
ax.scatter(x, y, s=5, alpha=0.2, color='white')
ax.set_xlabel('X'); ax.set_ylabel('Y')
plt.colorbar(ax.contourf(xi, yi, zi, cmap='viridis'), ax=ax, label='Density')
plt.tight_layout()
```

### plotly
```python
import plotly.graph_objects as go
fig = go.Figure(go.Histogram2dContour(x=x, y=y, colorscale='Viridis'))
fig.show()
```
Or `px.density_contour(df, x='x', y='y')`.

### altair
```python
import altair as alt
alt.Chart(df).transform_density(density=['x', 'y'], ...).mark_geoshape()
```
Altair supports bivariate density via `transform_kde` (Vega-Lite extension). For simpler use, combine `mark_rect` with bin aggregation.

### excel / tableau
- **Excel**: No native contour. Use 3D Surface chart type as an approximation if z-values are on a grid.
- **Tableau**: Density mark type (heatmap) approximates contours; true isolines require external computation.
