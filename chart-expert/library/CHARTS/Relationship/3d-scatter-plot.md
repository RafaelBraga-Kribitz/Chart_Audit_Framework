---
name: 3D Scatter Plot
category: Relationship
input_type: [xyz-trivariate]
it_variants: []
analytical_function: Correlation
visual_family: Plot
shape_primitive: [Dot]
cardinality_fit: [medium, large]
audience: [Technical, Analytics]
complexity: Advanced
encoding_channels: [position, color-hue, color-value]
tool_support: [matplotlib, plotly, d3]
failure_modes: [E, K]
alternatives: [scatter-plot, bubble-chart, parallel-coordinates, scatter-matrix]
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

# 3D Scatter Plot

## Description
A 3D Scatter Plot extends the two-dimensional scatter plot by adding a third position axis (z), allowing three continuous variables to be shown simultaneously as spatial coordinates. Each data point is rendered as a dot in a three-dimensional Cartesian space. The chart is typically displayed in a perspective projection that can be rotated interactively, or in a fixed viewing angle in static media. Colour and size can encode additional variables. 3D scatter plots are most useful as exploratory tools for high-dimensional data, particularly in conjunction with dimensionality reduction techniques.

## When to Use
- Exploring trivariate relationships in a three-dimensional variable space
- Visualising clusters in 3D space (e.g., PCA/t-SNE output projected to first 3 components)
- Scientific and engineering contexts where three physical dimensions carry genuine meaning
- Interactive presentations where the viewer can rotate the plot to see structure from multiple angles

## When NOT to Use
- Static media where the viewing angle is fixed — depth cues are lost and the chart often misleads
- When audience cannot interact with the chart and rotate it
- When a bubble chart (3 vars on a 2D plane) or a scatter matrix (all pairwise 2D plots) would communicate the same relationships more clearly
- When more than ~3 variable relationships need to be shown simultaneously (use parallel coordinates)

## Data Requirements
- Three continuous numeric columns (x, y, z)
- Optional: a categorical or numeric column for colour
- n between 20 and ~5,000 (above this, overplotting in 3D becomes severe)

## Best Practices
- Always provide interactivity (rotation, zoom) when the medium supports it
- In static form, show the 3D plot alongside 2D projections (xy, xz, yz planes) to disambiguate depth
- Use colour to encode a fourth variable or group membership — it remains visible regardless of viewing angle
- Add reference planes or grid lines at meaningful value thresholds
- Label axes clearly with variable names, units, and scale marks

## Common Mistakes
- E (MC-noise-as-difference): what appears as a cluster at one viewing angle may dissolve when the plot is rotated — always verify from multiple angles
- K (self-correlated scatter): plotting derived variables where one is computed from another creates spurious 3D structure
- Fixed perspective that happens to align two separate clusters — readers must rotate to verify
- Overplotting without alpha transparency — dense point clouds appear as opaque blobs

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(x, y, z, c=color_values, cmap='tab10', alpha=0.6, s=20)
ax.set_xlabel('X Variable')
ax.set_ylabel('Y Variable')
ax.set_zlabel('Z Variable')
plt.colorbar(scatter, ax=ax, label='Group')
ax.view_init(elev=20, azim=45)  # set initial viewing angle
plt.tight_layout()
```

### plotly
```python
import plotly.express as px
fig = px.scatter_3d(df, x='x', y='y', z='z',
                    color='group', opacity=0.7,
                    hover_name='label')
fig.update_traces(marker=dict(size=4))
fig.show()
```
Plotly 3D scatter is fully interactive in Jupyter and web contexts. Use `scene` layout property to set axis ranges and labels.

### altair
Altair does not support native 3D rendering. Use Plotly or matplotlib for 3D scatter plots.

### excel / tableau
- **Excel**: No native 3D scatter plot. The 3D chart types in Excel are surface/bar charts, not point clouds.
- **Tableau**: No native 3D scatter. Use Plotly embedded via Extension or export to a 3D-capable tool.
