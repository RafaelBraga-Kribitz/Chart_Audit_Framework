---
name: Venn Diagram
category: Composition
input_type: [composition]
it_variants: []
analytical_function: Part-to-whole
visual_family: Diagram
shape_primitive: [Circle]
cardinality_fit: [small-N]
audience: [Executive, Analytics, Public]
complexity: Basic
encoding_channels: [area, color-hue, color-value]
tool_support: [matplotlib, d3, powerbi]
failure_modes: []
alternatives: [euler-diagram, chord-diagram]
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
# Venn Diagram

## Description
Also known as a Set Diagram. A Venn Diagram shows all possible logical relationships between a collection of sets, each represented as a circle (or ellipse). Overlapping regions (intersections) represent entities or items that belong to multiple sets simultaneously. The classic 2-set or 3-set Venn Diagram is ubiquitous in presentations; 4- to 7-set variants use more complex geometric shapes and are rare in practice.

## When to Use
- Illustrating set membership and overlaps between 2–3 groups conceptually
- Showing what is shared and what is unique between two or three categories
- Concept visualisation in educational, business strategy, or marketing contexts

## When NOT to Use
- More than 3 sets (geometry becomes unwieldy and unreadable)
- When precise proportional representation of set sizes is required (use Euler Diagram)
- When the goal is to show quantities rather than logical relationships

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| set_name | categorical | Name of each set |
| members | list/set | Items belonging to each set |
| intersection_value | numeric (optional) | Size of each intersection region |

## Best Practices
- Use proportionally-sized circles (Euler-style) when set sizes differ significantly
- Label each circle with the set name outside the overlap zone
- Annotate intersection regions with counts or key items
- Keep to 2–3 sets; use Euler Diagram for proportional accuracy

## Common Mistakes
- Drawing equal-sized circles when sets are very different in size (misleading)
- Attempting 4+ sets without proportional scaling (becomes conceptual art, not data viz)
- Omitting the values in intersection regions, leaving viewers to guess overlap sizes
- Using Venn where an upset plot or UpSet diagram would handle complex multi-set intersections better

## Implementation Notes

### matplotlib
```python
from matplotlib_venn import venn2, venn3
venn2(subsets=(len_A_only, len_B_only, len_intersection),
      set_labels=('Set A', 'Set B'))
```

### plotly
No native Venn; use `go.Scatter` with circle shapes or the `plotly-venn` community package.

### altair
Not natively supported; use overlapping `mark_circle()` with opacity for a conceptual version.

### excel / tableau
Not natively supported in either tool. Use SmartArt in PowerPoint for simple conceptual diagrams. **Tableau**: Not practical for data-driven Venn.
