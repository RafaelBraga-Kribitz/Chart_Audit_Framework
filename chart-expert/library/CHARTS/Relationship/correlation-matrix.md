---
name: Correlation Matrix
category: Relationship
input_type: [matrix-grid, cat-multi-value]
it_variants: []
analytical_function: Correlation
visual_family: Chart
shape_primitive: [Square, Circle]
cardinality_fit: [medium, large]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, color-value, area]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi]
failure_modes: [K, E]
alternatives: [scatter-matrix, heat-map, bubble-heatmap, parallel-coordinates]
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

# Correlation Matrix

## Description
A Correlation Matrix visualises the pairwise correlation coefficients between multiple numeric variables, typically displayed as a colour-coded symmetric matrix where each cell shows the correlation between the row variable and the column variable. Cell colour encodes the magnitude and direction of correlation (diverging scale: dark blue for strong positive, dark red for strong negative, white near zero). Correlation matrices are a standard first step in exploratory multivariate analysis, feature selection, and identifying multicollinearity in regression models.

## When to Use
- Exploratory analysis of multivariate datasets to quickly survey pairwise relationships
- Feature selection for machine learning — identifying highly correlated predictors that may cause multicollinearity
- Domain knowledge validation — checking that expected correlations appear in the data
- Summarising a large scatter matrix as a more compact numeric summary

## When NOT to Use
- When the relationship between variables is non-linear — Pearson correlation is misleading (use Spearman or scatter matrix)
- When variables are categorical — Pearson correlation does not apply
- When the audience needs to see the actual scatter patterns, not just summary coefficients (use scatter matrix)
- When the number of variables exceeds ~25 — the matrix becomes too dense and individual cells too small

## Data Requirements
- Multiple (3+) continuous numeric columns
- n per pair sufficient for reliable correlation estimation (recommended n >= 30)
- All columns should be on the same dataset (same rows)

## Best Practices
- Use a diverging colour scale centred at 0 (e.g., RdBu) — never a sequential scale for correlation
- Display only the lower (or upper) triangle to avoid redundancy — the diagonal is always 1.0
- Annotate cells with the numeric correlation coefficient when the matrix is small enough (< ~15×15)
- Apply hierarchical clustering to reorder variables — correlated groups cluster together
- Add significance stars or mask non-significant correlations to avoid overinterpretation
- Document the correlation method used (Pearson, Spearman, Kendall tau)

## Common Mistakes
- K (self-correlated scatter): including derived variables (e.g., ratios, cumulative sums) alongside their components will produce artificially high correlations
- E (MC-noise-as-difference): treating a small correlation difference (e.g., 0.3 vs. 0.4) as practically significant without testing for difference
- Using Pearson correlation on non-normal or non-linear data without checking scatter plots first
- Displaying the full symmetric matrix with diagonal — wastes space and adds no information

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

corr = df[numeric_cols].corr(method='pearson')
mask = np.triu(np.ones_like(corr, dtype=bool))  # upper triangle mask

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, mask=mask, cmap='RdBu_r', center=0,
            vmin=-1, vmax=1, annot=True, fmt='.2f',
            square=True, linewidths=0.5, ax=ax)
ax.set_title('Correlation Matrix (Pearson)')
plt.tight_layout()
```

### plotly
```python
import plotly.express as px
import pandas as pd

corr = df[numeric_cols].corr()
fig = px.imshow(corr, color_continuous_scale='RdBu_r',
                color_continuous_midpoint=0, zmin=-1, zmax=1,
                text_auto='.2f', title='Correlation Matrix')
fig.show()
```

### altair
```python
import altair as alt

corr_long = df[cols].corr().reset_index().melt('index')
corr_long.columns = ['var1', 'var2', 'correlation']

alt.Chart(corr_long).mark_rect().encode(
    x='var1:O',
    y='var2:O',
    color=alt.Color('correlation:Q',
                    scale=alt.Scale(scheme='redblue', domainMid=0, domain=[-1, 1])),
    tooltip=['var1', 'var2', 'correlation']
)
```

### excel / tableau
- **Excel**: Compute correlation table using CORREL() formulas; apply Conditional Formatting > Colour Scale (3-colour, diverging) to the table.
- **Tableau**: Compute pairwise correlations in a preparatory step (Python/R), import as a flat table, then create a Heat Map with colour on the correlation field.
