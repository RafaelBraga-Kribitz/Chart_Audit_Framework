---
name: Dendrogram
category: Specialized
input_type: [hierarchical-cat, matrix-grid]
it_variants: []
analytical_function: Concept-viz
visual_family: Diagram
shape_primitive: [Line]
cardinality_fit: [small-N, medium, large]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, length, color-hue]
tool_support: [matplotlib, plotly, d3]
failure_modes: [J]
alternatives: [network-diagram, treemap, organisational-chart]
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
# Dendrogram

## Description
A Dendrogram is a tree diagram that shows hierarchical clustering relationships between entities. Leaf nodes (individual entities) are arranged along one axis; branch heights (internal node positions) encode the distance or dissimilarity at which clusters merge. The taller a merge node, the more dissimilar the two clusters being joined. Dendrograms are the standard output of hierarchical clustering algorithms and are also used in phylogenetic trees, linguistics, and taxonomy.

## When to Use
- Visualising the result of hierarchical (agglomerative or divisive) clustering
- Phylogenetic trees showing evolutionary relationships between species
- Showing the hierarchical organisation of a corpus, ontology, or taxonomy
- Paired with a heatmap to show cluster structure alongside data values

## When NOT to Use
- Flat (non-hierarchical) data without a tree structure
- More than ~200 leaf nodes without interaction (labels become unreadable)
- When cluster assignments (not cluster structure) are the primary output (use colour-coded scatter)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| linkage_matrix | numeric array | Output of scipy.cluster.hierarchy.linkage (or equivalent) |
| labels | string | Leaf node labels |

Or equivalently: any hierarchical tree structure with nodes and parent-child relationships.

## Best Practices
- Colour branches to highlight selected clusters (using a threshold cut)
- Include a scale bar or axis label for the distance metric
- Rotate the dendrogram to match the orientation of a paired heatmap
- Use `truncate_mode='lastp'` for large dendrograms to show only top N clusters

## Common Mistakes
- Using the wrong linkage method for the data type (Ward's for Euclidean distance only)
- Implying exact distances from branch heights when the scale is relative
- Silently dropping leaf nodes when truncating without disclosure (smell J)
- Labelling the x-axis "distance" without specifying the metric

## Implementation Notes

### matplotlib
```python
from scipy.cluster.hierarchy import linkage, dendrogram
Z = linkage(data, method='ward')
dendrogram(Z, labels=labels, color_threshold=threshold, ax=ax)
ax.set_xlabel('Sample')
ax.set_ylabel('Distance')
```

### plotly
`ff.create_dendrogram(data, labels=labels)` via `plotly.figure_factory`.

### altair
Not natively supported; pre-compute dendrogram coordinates and render as `mark_rule()` + `mark_point()`.

### excel / tableau
Not natively available. Use Python (scipy + matplotlib) or R (ggdendro) for dendrogram creation.
