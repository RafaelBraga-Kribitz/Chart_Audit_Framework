---
name: Ternary Plot
category: Distribution
input_type: [composition, xyz-trivariate]
it_variants: []
analytical_function: Distribution
visual_family: Plot
shape_primitive: [Dot, Line, Area]
cardinality_fit: [medium, large]
audience: [Technical, Analytics]
complexity: Advanced
encoding_channels: [position, color-hue, color-value, area]
tool_support: [matplotlib, plotly, d3]
failure_modes: [E, G]
alternatives: [scatter-plot, parallel-coordinates, phase-diagram, bubble-chart]
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

# Ternary Plot

## Description
A Ternary Plot (also called a ternary diagram, triangle plot, or simplex plot) represents the proportions of three components in a mixture as a single point in an equilateral triangle. Each vertex of the triangle represents 100% of one component (0% of the other two), each edge represents 0% of the opposite vertex component, and each interior point represents a mixture of all three. The constraint that the three components must sum to 100% (or 1) confines the data to a 2D simplex, which the equilateral triangle represents geometrically. Ternary plots are standard in geochemistry, materials science, ecology, and compositional data analysis.

## When to Use
- Visualising the distribution or mixing relationships of three-component compositional data
- Geochemistry: mineral composition, soil texture (sand-silt-clay triangles), rock classification
- Materials science: alloy compositions, phase diagrams for ternary systems
- Any domain where three proportions must sum to a fixed total

## When NOT to Use
- When there are more than three components (use parallel coordinates or a parts-of-whole chart instead)
- When proportions do not sum to a constant (the fundamental constraint is violated)
- When the audience is unfamiliar with ternary diagrams — they require explanation of the coordinate system
- When the actual values rather than ratios are what matter (ternary plots lose magnitude information)

## Data Requirements
- Three continuous numeric columns, each representing a component proportion
- All three columns must sum to the same constant (typically 100 or 1) for each observation
- Optional: a fourth variable for colour-coding points

## Best Practices
- Label each vertex clearly with the component name and the value at that vertex (100%)
- Draw grid lines at regular intervals (10% or 20%) to enable approximate reading
- Use a clear legend if colour encodes a secondary variable
- Annotate any classification boundaries (e.g., soil texture triangles have named zones)
- For density, overlay contour lines computed from bivariate KDE on the transformed coordinates

## Common Mistakes
- G (KDE-over-atoms): applying density contours on small n in ternary space
- E (MC-noise-as-difference): treating close points on the triangle as meaningfully different without considering measurement error
- Confusing ternary plot with a triangle bar chart or stacked chart — they encode fundamentally different things
- Plotting data that does not actually sum to a constant and not normalising first

## Implementation Notes

### matplotlib
```python
# Use the `python-ternary` library
import ternary
import matplotlib.pyplot as plt

figure, tax = ternary.figure(scale=100)
tax.scatter(points, marker='o', color='blue', label='Samples')
tax.boundary(linewidth=1.5)
tax.gridlines(color='grey', multiple=10)
tax.set_title('Ternary Plot')
tax.left_axis_label('Component C')
tax.right_axis_label('Component B')
tax.bottom_axis_label('Component A')
plt.tight_layout()
```
Install: `pip install python-ternary`

### plotly
```python
import plotly.express as px
fig = px.scatter_ternary(df, a='comp_a', b='comp_b', c='comp_c',
                         color='group', title='Ternary Plot')
fig.show()
```
`px.scatter_ternary` and `px.line_ternary` provide native support.

### altair
No native ternary coordinate system. Pre-convert ternary coordinates to Cartesian (x = b + c/2, y = c * sqrt(3)/2) and use `mark_point` in a standard chart with hidden axes.

### excel / tableau
Not natively supported. Requires pre-converting ternary coordinates to Cartesian and using a scatter chart.
