---
name: Phase Diagram
category: Distribution
input_type: [xy-simple, xyz-trivariate]
it_variants: []
analytical_function: Distribution
visual_family: Diagram
shape_primitive: [Area, Line, Polygon]
cardinality_fit: [medium, large]
audience: [Technical]
complexity: Advanced
encoding_channels: [position, color-hue, color-value, area]
tool_support: [matplotlib, plotly, d3]
failure_modes: [E]
alternatives: [contour-plot, ternary-plot, scatter-plot, heat-map]
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

# Phase Diagram

## Description
A Phase Diagram is a domain-specific chart type originating in physics, chemistry, and materials science that maps the stable phases (states of matter or thermodynamic equilibrium states) of a substance or mixture as a function of two intensive variables — most commonly temperature and pressure (for single-component systems) or temperature and composition (for binary/ternary systems). Phase boundaries (liquidus, solidus, eutectic lines, phase transition curves) separate regions on the diagram. Each region is labelled with the phase(s) that are thermodynamically stable under those conditions.

## When to Use
- Chemistry and materials science: displaying which phase (solid, liquid, gas, mixed) is stable at given T-P or T-composition combinations
- Engineering: determining processing windows (which conditions yield a desired phase)
- Metallurgy: showing alloy microstructure as a function of composition and temperature (e.g., Fe-C diagram)
- Informing experimental design: selecting temperature-composition combinations to reach a target phase

## When NOT to Use
- Outside thermodynamic / physical chemistry contexts — the chart form is domain-specific and confusing to general audiences
- When the phase boundary data comes from a poorly calibrated model — misleading precision in boundary lines is dangerous for engineering decisions
- When a simpler binary classification plot (e.g., region plot) would communicate the same information

## Data Requirements
- Two continuous axis variables (e.g., temperature, pressure, or composition fraction)
- Phase region labels or a numeric phase identifier per point or region
- Phase boundary coordinates (often from thermodynamic calculations or experimental measurements)
- For ternary systems: three composition components summing to 1 (use ternary plot instead)

## Best Practices
- Clearly label all phase regions directly on the diagram, not only in a legend
- Mark critical points (triple point, eutectic, peritectic) with a distinct marker and label
- Use colour to distinguish phases, with consistent colour conventions within the domain (e.g., liquid = blue, solid = grey)
- Annotate key boundary lines (liquidus, solidus) by name
- Specify the reference pressure for T-composition diagrams (usually 1 atm / 101.325 kPa)

## Common Mistakes
- E (MC-noise-as-difference): drawing phase boundaries as sharp lines when experimental data supports only approximate locations with uncertainty bands
- Omitting critical points or invariant points that define the topology of the diagram
- Confusing a phase diagram with a stability diagram or Pourbaix diagram (electrochemical analogue)
- Plotting with non-linear temperature scales without labelling the scale type

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np

fig, ax = plt.subplots()
# Draw phase regions as filled polygons
liquid_region = Polygon([[300, 1], [800, 1], [800, 100], [300, 100]], closed=True)
solid_region = Polygon([[100, 1], [300, 1], [300, 100], [100, 100]], closed=True)
p = PatchCollection([liquid_region, solid_region],
                    facecolors=['lightblue', 'lightgrey'], alpha=0.7)
ax.add_collection(p)
# Draw phase boundary
ax.plot([300, 300], [1, 100], 'k-', linewidth=2, label='Liquidus')
ax.set_xlabel('Temperature (°C)')
ax.set_ylabel('Pressure (atm)')
ax.set_title('Phase Diagram')
plt.tight_layout()
```

### plotly
Use `go.Scatter` with `fill='toself'` for phase regions and `go.Scatter` lines for phase boundaries. Annotate region labels with `go.layout.Annotation`.

### altair
Pre-compute polygon coordinates for each phase region. Use `mark_geoshape` or `mark_area` with layered Line marks for boundaries.

### excel / tableau
Not natively supported for proper phase diagrams. Use a scatter chart with region shading approximated via area charts or background images.
