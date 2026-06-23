---
name: Radar Chart
category: Comparison
input_type: [cat-multi-value, demo-grouped]
it_variants: []
analytical_function: Comparison
visual_family: Chart
shape_primitive: [Polygon, Line]
cardinality_fit: [small-N]
audience: [Executive, Analytics, Public]
complexity: Intermediate
encoding_channels: [position, area, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [D, K]
alternatives: [grouped-bar-chart, dot-plot, parallel-coordinates, heatmap]
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

# Radar Chart

## Description
A radar chart (also called a spider chart or polar chart) plots multivariate data on equidistant axes radiating from a central point. Each axis represents a different variable, and the values for each entity are plotted along the respective axes and connected to form a polygon. Multiple entities can be overlaid as distinct polygons. The overall shape of each polygon gives an impression of a multi-dimensional profile.

## When to Use
- Comparing an entity's performance across 4–8 distinct dimensions simultaneously
- Communicating profiles or archetypes (e.g., athlete profiles, product feature comparisons)
- When the shape of the multi-dimensional profile is more important than precise values
- Small number of entities (2–3) compared across the same set of dimensions

## When NOT to Use
- More than 8 axes (polygon shapes become uninterpretable)
- The order of axes on the radial layout affects visual shape perception, implying false relationships
- Precise value comparisons are needed (bar charts or dot plots are more readable)
- Axes have very different scales and normalization hides meaningful absolute differences
- Variables are correlated and their arrangement on the axes creates misleading visual patterns — see Smell K

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| entity | categorical | The items being profiled |
| dimension | categorical | The variable/axis name |
| value | numeric | Normalized (0-1 or 0-100) for comparability across axes |

## Best Practices
- Normalize all axes to the same scale (0–100 or z-scores) before plotting
- Limit to 4–8 axes; fewer axes = bar chart; more axes = parallel coordinates
- Use transparent polygon fills when overlaying multiple entities
- Label each axis directly at its outer endpoint
- Consider ordering axes by related domain clusters rather than arbitrarily — see Smell D

## Common Mistakes
- Leaving axes in arbitrary or alphabetical order, creating polygon shapes that imply false patterns — see Smell D
- Using axes with different natural scales without normalization
- Overlaying so many entities that polygons become completely illegible
- Treating adjacent axis proximity as implying correlation between variables — see Smell K

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np
angles = np.linspace(0, 2*np.pi, n_vars, endpoint=False).tolist()
angles += angles[:1]  # close the polygon
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
for entity, values in entity_data.items():
    vals = values + values[:1]
    ax.plot(angles, vals, linewidth=1.5, label=entity)
    ax.fill(angles, vals, alpha=0.15)
ax.set_thetagrids([a * 180/np.pi for a in angles[:-1]], labels)
ax.legend(loc='upper right')
```

### plotly
`go.Scatterpolar(r=values, theta=dimensions, fill='toself', name=entity)` — one trace per entity.

### altair
Not natively supported as a polar chart; requires `theta` encoding with specialized transformation.

### excel / tableau
Excel: Insert > Radar Chart. Tableau: Not native; requires calculated fields with polar coordinate conversion.
