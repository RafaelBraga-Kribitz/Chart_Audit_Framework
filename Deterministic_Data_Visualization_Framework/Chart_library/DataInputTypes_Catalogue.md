# Data Input Type Catalogue

A structured system for identifying data shapes and auto-selecting appropriate visualizations.

---

## 1. Simple Bivariate (X-Y)

**Visual Pattern:**
```
| X  | Y  |
|----|----| 
| 1  | 30 |
| 2  | 34 |
| 3  | 38 |
```

**Shorthand Tag:** `#xy-simple`

**Data Signature:** `[numeric, numeric]`

**Characteristics:**
- 2 columns exactly
- One independent variable (X)
- One dependent variable (Y)
- All numeric values

**Suitable Charts:**
- Line Chart
- Scatter Plot
- Area Chart
- Column/Bar Chart

**Claude Filter:** `data_input_type: 'bivariate-simple' | columns: 2 | numeric_cols: [all]`

---

## 2. Bivariate with Two Series (X-Y₁-Y₂)

**Visual Pattern:**
```
| X   | Y₁ | Y₂ |
|-----|----|----|
| 0-2 | 30 | 45 |
| 2-4 | 34 | 80 |
| 4-6 | 38 | 60 |
```

**Shorthand Tag:** `#xy-dual-series`

**Data Signature:** `[numeric/categorical, numeric, numeric]`

**Characteristics:**
- 3 columns exactly
- One X axis (independent)
- Two Y series (dependent, comparable scales)
- Numeric throughout

**Suitable Charts:**
- Multi-Line Chart
- Multi-Series Column/Bar
- Dual-Axis Chart (if scales differ)
- Grouped Bar Chart

**Claude Filter:** `data_input_type: 'bivariate-dual' | columns: 3 | numeric_cols: [1, 2]`

---

## 3. Trivariate (X-Y-Z)

**Visual Pattern:**
```
| X  | Y  | Z  |
|----|----|----|
| 1  | 10 | 30 |
| 2  | 34 | 14 |
| 3  | 38 | 12 |
```

**Shorthand Tag:** `#xyz-trivariate`

**Data Signature:** `[numeric, numeric, numeric]`

**Characteristics:**
- 3 columns of numeric data
- Three independent/dependent relationships possible
- Represents 3-dimensional space

**Suitable Charts:**
- Bubble Chart (X, Y position + Z as size)
- 3D Scatter
- Heatmap (if Z represents intensity)
- Small Multiple (X-Y charts sized by Z)

**Claude Filter:** `data_input_type: 'trivariate' | columns: 3 | numeric_cols: [all]`

---

## 4. Categorical-Value (Category-Numeric)

**Visual Pattern:**
```
| Category | Value |
|----------|-------|
| A        | 32%   |
| B        | 40%   |
| C        | 28%   |
```

**Shorthand Tag:** `#cat-value`

**Data Signature:** `[categorical, numeric]`

**Characteristics:**
- 2 columns
- First column: discrete categories (no order)
- Second column: numeric values
- Often percentages or counts

**Suitable Charts:**
- Bar Chart (horizontal preferred for long labels)
- Pie Chart
- Donut Chart
- Waffle Chart

**Claude Filter:** `data_input_type: 'categorical-value' | columns: 2 | col_types: ['string', 'numeric']`

---

## 5. Categorical-Multi-Value (Category-Y₁-Y₂-...)

**Visual Pattern:**
```
| Item | X  | Y  | Z  |
|------|----|----|-----|
| A    | 14 | 6  | 10  |
| B    | 16 | 12 | 8   |
| C    | 12 | 20 | 15  |
```

**Shorthand Tag:** `#cat-multi-value`

**Data Signature:** `[categorical, numeric, numeric, ...]`

**Characteristics:**
- First column: categories
- Multiple numeric columns (2+)
- Represents grouped comparisons
- Values comparable across groups

**Suitable Charts:**
- Grouped Bar Chart
- Stacked Bar Chart (if parts of whole)
- Small Multiples
- Slope Chart

**Claude Filter:** `data_input_type: 'categorical-multi' | numeric_cols: [1, 2, ...] | group_by: col_0`

---

## 6. Time Series (Time-Value or Time-Multiple Values)

**Visual Pattern:**
```
| Start time | End time   |
|------------|------------|
| 1-4-2015   | 6-4-2015   |
| 10-4-2015  | 18-4-2015  |
| 12-4-2015  | 20-4-2015  |
```

**Shorthand Tag:** `#time-series`

**Data Signature:** `[datetime/date, numeric]` or `[datetime, numeric, numeric, ...]`

**Characteristics:**
- First column: temporal data (dates, times, timestamps)
- Subsequent columns: numeric values over time
- Ordered by time
- May have single or multiple series

**Suitable Charts:**
- Time Series Line Chart
- Area Chart
- Candlestick Chart (OHLC data)
- Gantt Chart (if intervals/durations)

**Claude Filter:** `data_input_type: 'time-series' | temporal_col: 0 | numeric_cols: [1, ...]`

---

## 7. Interval/Range Data (Start-End or Lower-Upper)

**Visual Pattern:**
```
| Time | 2000 | 2005 | 2010 |
|------|------|------|------|
| A    | C    | C    | -    |
| B    | A    | A    | A    |
| C    | A    | B    | C    |
```

Or:

```
| lower | close | open | upper |
|-------|-------|------|-------|
| $10   | $20   | $60  | $70   |
| $25   | $30   | $45  | $65   |
```

**Shorthand Tag:** `#interval-range`

**Data Signature:** `[categorical, numeric, numeric]` (as bounds) or `[categorical, numeric, numeric, numeric, numeric]` (OHLC)

**Characteristics:**
- Lower and Upper bounds or Open/Close/High/Low
- Represents ranges or financial data
- May include mid-point or opening value

**Suitable Charts:**
- Candlestick Chart (OHLC)
- Box Plot
- Range Chart
- Error Bar Chart

**Claude Filter:** `data_input_type: 'interval-range' | bounds: [lower, upper] | optional: [open, close]`

---

## 8. Demographic/Grouped Categorical (Category-Subcategory-Numeric)

**Visual Pattern:**
```
| Age    | F  | M  |
|--------|----|----|
| 10-20  | 30 | 28 |
| 20-30  | 34 | 22 |
| 30-40  | 38 | 26 |
```

**Shorthand Tag:** `#demo-grouped`

**Data Signature:** `[categorical, categorical, numeric]` (or multiple numeric columns for subcategories)

**Characteristics:**
- First column: primary category (e.g., age group, region)
- Subsequent columns: subcategories (e.g., F/M, product lines)
- Numeric values at intersection
- Represents cross-tabulation

**Suitable Charts:**
- Grouped/Clustered Bar Chart
- Stacked Bar Chart
- Heatmap
- Treemap

**Claude Filter:** `data_input_type: 'grouped-categorical' | group_cols: [0] | cross_tab: true | numeric_cols: [1, ...]`

---

## 9. Composition/Parts-of-Whole (Category-Percentage or Category-Parts)

**Visual Pattern:**
```
| Item  | A   | B   |
|-------|-----|-----|
| Pie 1 | 65% | 35% |
| Pie 2 | 50% | 50% |
| Pie 3 | 80% | 20% |
```

**Shorthand Tag:** `#composition`

**Data Signature:** `[categorical, numeric, numeric, ...]` where sum per row ≈ 100%

**Characteristics:**
- Each row represents a "whole"
- Multiple columns represent parts
- Values sum to 100% (or 1.0) per row
- Represents proportions or percentages

**Suitable Charts:**
- Stacked Bar Chart (100%)
- Stacked Area Chart
- Pie Chart (single item)
- Waffle Chart

**Claude Filter:** `data_input_type: 'composition' | sum_check: 'per_row_100' | numeric_cols: [1, ...]`

---

## 10. Ordered Categorical with Levels (Category-Level Ranking)

**Visual Pattern:**
```
| Order | Level 1 | Level 2   | Level 3  |
|-------|---------|-----------|----------|
| 1     | Fruit   | Citrus    | Orange   |
| 2     | Fruit   | Citrus    | Lemon    |
| 3     | Meat    | Pork      | Chop     |
```

**Shorthand Tag:** `#hierarchical-cat`

**Data Signature:** `[numeric/ordered, categorical, categorical, categorical, ...]`

**Characteristics:**
- First column: ordering/ranking
- Multiple categorical levels (hierarchical)
- Represents taxonomy or drill-down structure
- May have associated numeric values

**Suitable Charts:**
- Treemap
- Sunburst Chart
- Dendrogram
- Icicle Chart

**Claude Filter:** `data_input_type: 'hierarchical' | levels: 3+ | order_col: 0`

---

## 11. Matrix/Grid (N×M Categorical Grid)

**Visual Pattern:**
```
|   | A  | ¬A |
|---|----|----|
| B | W  | X  |
| ¬B| Y  | Z  |
```

**Shorthand Tag:** `#matrix-grid`

**Data Signature:** `[categorical (rows), categorical (cols), numeric/categorical (values)]`

**Characteristics:**
- 2D grid structure
- Row and column headers are both categorical
- Cells contain numeric or categorical values
- Represents contingency table or confusion matrix

**Suitable Charts:**
- Heatmap
- Mosaic Plot
- Confusion Matrix Visualization
- Network Diagram

**Claude Filter:** `data_input_type: 'matrix' | shape: 'grid' | row_labels: categorical | col_labels: categorical`

---

## 12. Event-Timeseries (Event-Time-Value or Location-Value)

**Visual Pattern:**
```
| Event | Time      |
|-------|-----------|
| A     | 1-4-2015  |
| B     | 10-4-2015 |
| C     | 12-4-2015 |
```

Or:

```
| Location | Value |
|----------|-------|
| A        | 14    |
| B        | 6     |
| C        | 15    |
```

**Shorthand Tag:** `#event-time` or `#location-value`

**Data Signature:** `[categorical, datetime]` or `[categorical, numeric]` (geographic context)

**Characteristics:**
- Event/location identifier
- Associated temporal or spatial value
- Often represents point-in-time or geographic distribution
- May have discrete events rather than continuous series

**Suitable Charts:**
- Timeline
- Calendar Heatmap
- Map (if location)
- Scatter plot along time axis
- Strip Plot

**Claude Filter:** `data_input_type: 'event-time' | col_0: 'categorical' | col_1: 'datetime'`

---

## Quick Reference: Input Type to Chart Selector

```
INPUT TYPE           | PRIMARY CHARTS         | SECONDARY CHARTS
---------------------|------------------------|------------------------
xy-simple            | Line, Scatter, Area    | Bar, Column
xy-dual-series       | Multi-Line, Multi-Bar  | Dual-Axis
xyz-trivariate       | Bubble, 3D Scatter     | Small Multiple
cat-value            | Bar, Pie, Donut        | Waffle, Lollipop
cat-multi-value      | Grouped Bar, Stacked   | Small Multiple, Slope
time-series          | Line, Area             | Column, Candlestick
interval-range       | Box Plot, Range        | Candlestick (OHLC)
demo-grouped         | Grouped Bar, Stacked   | Heatmap, Treemap
composition          | Stacked Bar (100%)     | Pie, Waffle
hierarchical-cat     | Treemap, Sunburst      | Icicle, Dendrogram
matrix-grid          | Heatmap, Mosaic        | Confusion Matrix
event-time           | Timeline, Calendar HM  | Strip Plot
```

---

## Filter Tags for Obsidian

Tag all your chart examples with these:

```
#xy-simple #xy-dual-series #xyz-trivariate #cat-value #cat-multi-value
#time-series #interval-range #demo-grouped #composition #hierarchical-cat
#matrix-grid #event-time

```

Use in searches: `tag:#xy-simple` or `tag:#time-series`

---

## Claude Skill: Deterministic Selector Logic

```json
{
  "selector_logic": {
    "step_1_identify": "Count columns and detect data types",
    "step_2_classify": "Match against data signatures above",
    "step_3_filter": "Apply chart recommendations",
    "step_4_apply": "Select primary chart unless constraints differ"
  },
  
  "decision_tree": {
    "if_2_cols": {
      "both_numeric": "xy-simple → Line/Scatter",
      "numeric_categorical": "cat-value → Bar/Pie"
    },
    "if_3_cols": {
      "all_numeric": "Check if temporal → time-series OR xyz-trivariate",
      "2_numeric_1_cat": "time-series OR demo-grouped",
      "1_numeric_2_cat": "demo-grouped"
    },
    "if_4_cols_plus": {
      "first_temporal": "time-series",
      "first_categorical": "cat-multi-value OR demo-grouped",
      "all_numeric": "xyz-trivariate OR multi-series"
    },
    "if_grid_shaped": "matrix-grid → Heatmap"
  }
}
```

---

## Usage Notes for Obsidian

1. **Create separate files** for each data input type with real examples from your domain
2. **Link chart files** to relevant input types using Obsidian links
3. **Use DataView queries** to filter by tag:
   ```
   LIST WHERE contains(tags, "#time-series")
   ```
4. **Embed examples** using `![[filename]]` syntax
5. **Cross-reference** using [[xy-simple]] style links

---

**Last Updated:** 2026-06-23  
**Version:** 1.0  
**Scope:** Data input shape identification for deterministic chart selection
