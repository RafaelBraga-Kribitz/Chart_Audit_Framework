---
name: Scatter Matrix
category: Relationship
input_type: [cat-multi-value, demo-grouped]
it_variants: []
analytical_function: Correlation
visual_family: Chart
shape_primitive: [Dot, Line, Area, Bar]
cardinality_fit: [medium, large]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, color-hue, area]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi]
failure_modes: [K, E]
alternatives: [correlation-matrix, parallel-coordinates, heat-map, bubble-heatmap]
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

# Scatter Matrix

## Description
A Scatter Matrix (also called a SPLOM — Scatter PLot Matrix, or pair plot) is a grid of scatter plots showing all pairwise combinations of multiple numeric variables. Each off-diagonal cell shows the scatter plot of one variable against another. The diagonal typically shows the univariate distribution of each variable (histogram, density plot, or KDE). When groups are present, colour-coding each point by group membership allows visual comparison of how groups separate across multiple variable pairs simultaneously. Scatter matrices are one of the most information-dense charts for multivariate exploratory analysis.

## When to Use
- Comprehensive exploratory analysis of relationships across all pairs of numeric variables
- Identifying which variable pairs exhibit strong correlation or non-linear relationships
- Detecting how well groups separate across different variable combinations (classification EDA)
- Feature engineering and selection: understanding which variables carry redundant or complementary information

## When NOT to Use
- When the number of variables exceeds ~8–10 — the grid becomes too large (n² panels)
- When the audience needs a summary rather than all pairwise detail (use correlation matrix instead)
- When individual scatter plots would need too much annotation to be interpretable at the small panel size
- For executive or public audiences who need simple, focused charts

## Data Requirements
- 3–8 continuous numeric columns (more than 8 creates an unwieldy grid)
- Optional: a categorical column for colour-coded group membership
- n >= 50 for meaningful scatter patterns in each panel

## Best Practices
- Show univariate distribution plots (KDE or histogram) on the diagonal
- Use colour to encode group membership — the scatter matrix then simultaneously shows both pairwise correlations and group separation
- Display correlation coefficients in the upper triangle panels to provide a numeric summary alongside visual patterns
- Adjust point size and alpha for n — larger n requires smaller, more transparent points
- Sort variables by importance or correlation magnitude to put the most informative pairs near the top-left

## Common Mistakes
- K (self-correlated scatter): including ratio variables alongside their components — the algebraic relationship produces guaranteed correlations independent of the data
- E (MC-noise-as-difference): treating visual correlations in small panels as equivalent to statistically significant relationships
- Using too many variables — an 8×8 SPLOM has 56 unique pairwise panels, overwhelming the reader
- Defaulting to raw variable scales when extreme outliers compress the visible scatter into a corner

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import pandas as pd

# Seaborn pairplot (most convenient)
import seaborn as sns
g = sns.pairplot(df, vars=numeric_cols, hue='group',
                 diag_kind='kde', plot_kws={'alpha': 0.5, 's': 20})
g.fig.suptitle('Scatter Matrix', y=1.02)
plt.tight_layout()
```
Pure matplotlib: use `pd.plotting.scatter_matrix(df, alpha=0.5, figsize=(12, 12), diagonal='kde')`.

### plotly
```python
import plotly.express as px
fig = px.scatter_matrix(df, dimensions=numeric_cols,
                        color='group', opacity=0.6)
fig.update_traces(diagonal_visible=False)
fig.show()
```
Fully interactive with zoom and selection brushing across all panels.

### altair
```python
import altair as alt

# Altair SPLOM via repeated encodings
alt.Chart(df).mark_circle(opacity=0.5, size=20).encode(
    alt.X(alt.repeat('column'), type='quantitative'),
    alt.Y(alt.repeat('row'), type='quantitative'),
    color='group:N'
).repeat(
    row=numeric_cols,
    column=numeric_cols
).interactive()
```

### excel / tableau
- **Excel**: No native SPLOM. Create individual scatter charts manually for key pairs.
- **Tableau**: No native SPLOM. Use separate scatter sheets for each pair, or use a third-party extension. The Tableau "SPLOM" workaround uses a matrix of calculated fields.
