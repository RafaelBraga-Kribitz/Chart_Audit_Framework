---
name: Bagplot
category: Distribution
input_type: [xy-simple]
it_variants: []
analytical_function: Distribution
visual_family: Plot
shape_primitive: [Polygon, Dot]
cardinality_fit: [medium, large]
audience: [Analytics, Technical]
complexity: Advanced
encoding_channels: [position, area, color-value]
tool_support: [d3, matplotlib]
failure_modes: [E, G]
alternatives: [scatter-plot, contour-plot, hexagonal-binning, box-plot]
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

# Bagplot

## Description
A Bagplot is a bivariate generalisation of the box plot, extending five-number summary concepts to two dimensions. It consists of three nested regions: a central "bag" containing the deepest 50% of data points (analogous to the IQR box), a "fence" that is an inflated version of the bag (typically at a 3× inflation factor, analogous to whiskers), and a loop — the convex hull of all non-outlier points. Points outside the loop are flagged as outliers. The depth function used (typically Tukey halfspace depth) provides a robust, centre-outward ordering of bivariate data.

## When to Use
- Robustly summarising the centre, spread, and outliers of a bivariate continuous dataset
- Comparing two groups' bivariate distributions using overlaid bagplots
- Detecting bivariate outliers that would be invisible in two separate univariate plots
- Academic or statistical reporting contexts where robust depth-based methods are required

## When NOT to Use
- When the audience is non-technical — the three-region encoding is not intuitive
- When n is very small (< ~50) — depth computation becomes unstable
- When more than 2–3 groups need comparison (visual complexity explodes)
- When a standard scatter plot with a contour overlay suffices for the communication goal
- When data has multimodal bivariate structure that the convex regions would mask

## Data Requirements
- Two continuous numeric columns (x and y variables)
- n >= 50 recommended for stable depth computation; n >= 100 preferred
- Optional: a grouping column for overlaid multi-group bagplots

## Best Practices
- Always show the raw scatter points alongside the bag and loop regions for transparency
- Label the "bag" and "fence/loop" regions in a legend or annotation
- Use contrasting fills (typically darker for bag, lighter for fence) with transparency
- Mark the depth median (the deepest point) with a distinct symbol
- Document the inflation factor and depth function used in the chart caption

## Common Mistakes
- G (KDE-over-atoms): the bag boundary is computed via convex hull operations that can look smooth but imply false precision on small n
- E (MC-noise-as-difference): comparing two bagplots visually for group differences without a formal bivariate test
- Conflating the depth median with the arithmetic mean — they can differ substantially for skewed distributions
- Using a non-robust depth function without noting the assumption

## Implementation Notes

### matplotlib
No native bagplot in matplotlib. Use the `aplpy` or R-ported implementations:
```python
# Requires external library; example using scipy for depth approximation
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Compute 50th percentile depth region (bag) and fence manually
# Plot as filled polygons
hull_bag = ConvexHull(inner_50pct_points)
plt.fill(inner_50pct_points[hull_bag.vertices, 0],
         inner_50pct_points[hull_bag.vertices, 1],
         alpha=0.5, label='Bag (50%)')
```
For production use, consider calling R's `aplpack::bagplot` via `rpy2`.

### plotly
No native bagplot. Approximate by plotting convex hull regions as filled scatter traces:
```python
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=bag_x, y=bag_y, fill='toself', name='Bag'))
fig.add_trace(go.Scatter(x=fence_x, y=fence_y, fill='toself', opacity=0.3, name='Fence'))
```

### altair
No native support. Pre-compute bag and fence polygon coordinates in Python/R and render as `mark_area` or `mark_line` with filled paths.

### excel / tableau
Not natively supported. Requires pre-computed polygon coordinates imported as data.
