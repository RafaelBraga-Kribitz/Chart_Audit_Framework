---
name: Slope Chart
category: Comparison
input_type: [cat-multi-value, demo-grouped]
it_variants: []
analytical_function: Comparison
visual_family: Chart
shape_primitive: [Line, Dot]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics, Public]
complexity: Basic
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi]
failure_modes: [D]
alternatives: [dumbbell-plot, grouped-bar-chart, bump-chart, line-chart]
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

# Slope Chart

## Description
A slope chart compares values across exactly two conditions or categories for multiple entities by drawing a line between the two values. When used in a Comparison context, the two columns often represent different groups, regions, or conditions (rather than two time points), and the slope of each line encodes which group scores higher and by how much for each entity. It directly answers "which entity changed direction and by how much?"

## When to Use
- Comparing the same metric across exactly two groups (regions, demographics, product lines) for many entities
- When direction and magnitude of difference between the two groups is the primary message
- Highlighting which entities reverse direction between the two groups
- When a grouped bar chart feels too bulky and a dumbbell plot requires more zero-baseline context

## When NOT to Use
- More than two comparison points (use a bump chart or parallel coordinates)
- Too many entities create unreadable spaghetti lines (limit to ~15)
- The two columns represent non-comparable quantities (different scales or units)
- Precise absolute values matter more than the slope direction (use a bar chart)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| entity | categorical | The items being compared (countries, products, etc.) |
| group_a | numeric | Value under the first condition/group |
| group_b | numeric | Value under the second condition/group |
| category (optional) | categorical | For color grouping of entities |

## Best Practices
- Sort entities by the magnitude of change (group_b - group_a) to reveal the largest movers — see Smell D
- Label both endpoints of each line; avoid legend-only identification
- Use color to encode category or direction (increases vs. decreases)
- Highlight specific entities of interest with bolder lines; gray out the rest
- Ensure both axes share the same scale for meaningful slope comparison

## Common Mistakes
- Leaving entities in arbitrary or alphabetical order, hiding which has the largest change — see Smell D
- Using two different y-axis scales for the two columns, creating misleading slope steepness
- Adding too many entities making lines overlap and become unreadable
- Confusing a slope chart with a parallel coordinates plot (slope charts always have exactly two axes)

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(4, 6))
for _, row in df.iterrows():
    ax.plot([0, 1], [row['group_a'], row['group_b']], 'o-',
            color='steelblue', alpha=0.6, linewidth=1.2)
    ax.text(-0.05, row['group_a'], row['entity'], ha='right', fontsize=8)
    ax.text(1.05, row['group_b'], row['entity'], ha='left', fontsize=8)
ax.set_xticks([0, 1])
ax.set_xticklabels(['Group A', 'Group B'])
ax.set_xlim(-0.5, 1.5)
plt.tight_layout()
```

### plotly
One `go.Scatter` trace per entity with `x=['Group A', 'Group B']` and `y=[group_a_val, group_b_val]`.

### altair
Melt data to long format, then `alt.Chart(df_long).mark_line(point=True).encode(x='group:O', y='value:Q', color='entity:N', detail='entity:N')`

### excel / tableau
Tableau: Line chart with two-column axis and one mark per entity. Excel: Line chart with two-point axis.
