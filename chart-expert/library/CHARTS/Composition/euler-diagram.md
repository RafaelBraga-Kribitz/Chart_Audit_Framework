---
name: Euler Diagram
category: Composition
input_type: [composition]
it_variants: []
analytical_function: Part-to-whole
visual_family: Diagram
shape_primitive: [Circle, Polygon]
cardinality_fit: [small-N]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [area, color-hue]
tool_support: [d3, matplotlib]
failure_modes: []
alternatives: [venn-diagram, upset-plot]
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
# Euler Diagram

## Description
An Euler Diagram is a variation of the Venn Diagram that only shows relationships that actually exist in the data, rather than all possible logical relationships. If two sets have no intersection, their circles do not overlap. If one set is entirely contained within another, its circle is drawn inside. This makes Euler Diagrams more accurate representations of real-world set relationships than Venn Diagrams, where all possible intersections are always shown even if empty.

## When to Use
- Representing actual set relationships where some intersections are empty or one set is a subset of another
- Logic, taxonomy, and classification diagrams where completeness of possible states matters less than accuracy
- Teaching or communicating subset and containment relationships

## When NOT to Use
- When the audience expects a symmetric Venn Diagram (all possible intersections shown)
- More than 4–5 sets (layout becomes infeasible or confusing)
- When proportional area accuracy is critical (curves become distorted to fit constraints)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| set_name | categorical | Name of each set |
| size | numeric | Total membership of each set |
| intersection | numeric | Size of each pairwise (or higher-order) intersection |

## Best Practices
- Use proportional circle sizes to represent relative set sizes
- Omit the overlap region entirely (no crossing circles) when sets are disjoint
- Draw one circle fully inside another when one set is a true subset
- Label clearly which region represents the intersection

## Common Mistakes
- Drawing all circles overlapping (defaulting to Venn layout) when intersections are empty
- Forcing circular shapes when containment or disjointness constraints make it geometrically impossible
- Using Euler Diagrams for very many sets without interactive zoom

## Implementation Notes

### matplotlib
```python
from matplotlib_venn import venn2
# Pass subsets=(A_only, B_only, AB_intersection)
# If AB_intersection = 0, circles are drawn non-overlapping
venn2(subsets=(100, 80, 0), set_labels=('A', 'B'))
```

### plotly
Not natively supported; construct using `go.Scatter` shapes or SVG-based custom rendering.

### altair
Not natively supported.

### excel / tableau
Not available natively; use drawing tools in PowerPoint or Illustrator for conceptual diagrams.
