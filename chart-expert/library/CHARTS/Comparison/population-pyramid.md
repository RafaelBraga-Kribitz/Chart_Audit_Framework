---
name: Population Pyramid
category: Comparison
input_type: [demo-grouped, cat-multi-value]
it_variants: []
analytical_function: Comparison
visual_family: Chart
shape_primitive: [Bar]
cardinality_fit: [small-N, medium]
audience: [Analytics, Public, Executive]
complexity: Intermediate
encoding_channels: [position, length, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi]
failure_modes: [D, J]
alternatives: [butterfly-chart, grouped-bar-chart]
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

# Population Pyramid

## Description
A population pyramid is a back-to-back horizontal bar chart specifically designed to show the age-sex (or age-gender) distribution of a population. Age groups are listed vertically on the shared y-axis (youngest at bottom, oldest at top), males on one side (traditionally left) and females on the other (traditionally right). The shape of the resulting chart reveals the population's demographic structure: expansive (young population), constrictive (aging), or stationary.

## When to Use
- Visualizing demographic age-sex distributions of a population, country, or cohort
- Comparing two demographic groups' age distributions side by side
- Communicating population aging trends or demographic transitions
- Public health, policy, and social science reporting

## When NOT to Use
- Data does not represent an age-sex breakdown (use a butterfly chart for general two-group comparison)
- The two groups being compared are not meaningfully mirrored (use a grouped bar chart)
- Percentages are not comparable across two different-sized populations without normalization
- Very few age bands where a table or grouped bar chart would suffice

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| age_group | ordered categorical | Standard age bands (0-4, 5-9, ..., 80+) |
| male_count | numeric | Population count or percentage for males |
| female_count | numeric | Population count or percentage for females |

## Best Practices
- Use percentage of total population (not raw counts) when comparing populations of different sizes
- Place age groups in ascending order from bottom to top (youngest at bottom)
- Use conventional blue for male (left) and pink/orange for female (right), or choose accessible alternatives
- Show absolute x-axis labels (not negatives) on both sides
- Annotate notable cohort bulges or gaps that carry demographic meaning

## Common Mistakes
- Using raw counts without normalization when comparing two populations of vastly different sizes
- Placing youngest age groups at the top instead of the bottom — see Smell D
- Silently dropping age bands with zero count — see Smell J
- Using the same color for both sides, making them indistinguishable

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.barh(age_groups, male_pct, color='steelblue', label='Male')
ax.barh(age_groups, [-v for v in female_pct], color='coral', label='Female')
ax.axvline(0, color='black', linewidth=0.8)
max_val = max(max(male_pct), max(female_pct))
ax.set_xticks([-max_val, -max_val/2, 0, max_val/2, max_val])
ax.set_xticklabels([f'{max_val}%', f'{max_val/2}%', '0',
                     f'{max_val/2}%', f'{max_val}%'])
ax.legend()
plt.tight_layout()
```

### plotly
Two horizontal `go.Bar` traces (one for each sex), with female values negated; customize x-axis tick labels.

### altair
Layer two horizontal `mark_bar` charts; negate female values; share the y (age) axis.

### excel / tableau
Tableau: Dual-axis back-to-back bar chart with negative values on one axis. Excel: Standard bar chart with one series negated.
