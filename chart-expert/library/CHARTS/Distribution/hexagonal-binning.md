---
name: Hexagonal Binning
category: Distribution
input_type: [xy-simple]
it_variants: []
analytical_function: Distribution
visual_family: Chart
shape_primitive: [Polygon]
cardinality_fit: [large, very-large]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, color-value]
tool_support: [matplotlib, plotly, altair, d3, tableau]
failure_modes: [E, J]
alternatives: [scatter-plot, contour-plot, heat-map, density-plot]
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

# Hexagonal Binning

## Description
Hexagonal Binning (hexbin plot) is a 2D density chart that partitions the plotting area into a regular hexagonal grid and encodes the number of data points falling in each hexagon using colour (or occasionally size). Hexagons are preferred over squares for 2D binning because they are closer to circular (reducing directionality bias), they have a single shared distance from centre to all neighbours, and they tile the plane efficiently. Hexbin charts are the standard solution for scatter plot overplotting at large n.

## When to Use
- Visualising the joint distribution of two continuous variables when n is large (> ~1000 points)
- Replacing an overplotted scatter plot while preserving the bivariate distributional shape
- Identifying high-density regions, bivariate modes, and outlier zones
- Engineering and scientific contexts: sensor data, simulation outputs, log-scale price data

## When NOT to Use
- When individual point identity or labelling matters (use scatter plot)
- When n is small (< ~200) — many hexagons will be empty or have counts of 1, creating a sparse misleading grid
- When the exact boundary between density regions is important (use contour plot)
- When a simple correlation value would suffice for the communication goal

## Data Requirements
- Two continuous numeric columns (x and y)
- n >= 500 recommended for hexbins to show meaningful density variation
- Optional: a weight column to sum a value per hexagon rather than counting points

## Best Practices
- Use a perceptually uniform sequential colour scale (viridis, plasma) — avoid rainbow
- Set hexagon size (gridsize) deliberately: too coarse loses structure, too fine creates noise
- Include a colour bar with a clear label ("Count" or the aggregated measure)
- Overlay contour lines at selected density thresholds for improved readability
- Log-scale the colour axis when density varies by orders of magnitude

## Common Mistakes
- E (MC-noise-as-difference): small hex-count differences in low-density regions look visually equal to large differences in high-density regions — use log colour scale to address
- J (silently-dropped-categories): empty hexagons are typically omitted; this can misrepresent the data range boundary
- Choosing a gridsize that is too large and hides important bimodal structure
- Using a diverging colour scale on a one-sided count variable

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
hb = ax.hexbin(x, y, gridsize=30, cmap='viridis', mincnt=1)
plt.colorbar(hb, ax=ax, label='Count')
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.tight_layout()
```
`C` parameter + `reduce_C_function=np.mean` aggregates a third variable per hexagon. `bins='log'` applies log colour scale.

### plotly
```python
import plotly.express as px
fig = px.density_heatmap(df, x='x', y='y', nbinsx=30, nbinsy=30)
fig.show()
```
Use `marginal_x='histogram'` and `marginal_y='histogram'` for marginal distributions.

### altair
```python
import altair as alt
alt.Chart(df).mark_rect().encode(
    alt.X('x:Q', bin=alt.Bin(maxbins=30)),
    alt.Y('y:Q', bin=alt.Bin(maxbins=30)),
    alt.Color('count():Q', scale=alt.Scale(scheme='viridis'))
)
```
Altair bins rectangularly by default. For true hexagonal bins, pre-compute hex coordinates with `datashader` or `h3`.

### excel / tableau
- **Excel**: No native hexbin. Approximate with rectangular heatmap using COUNTIFS.
- **Tableau**: Density mark type provides a smooth 2D density approximation; true hexbins require pre-computed geometry.
