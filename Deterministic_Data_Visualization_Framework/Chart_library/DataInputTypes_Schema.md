# Data Input Type Schema (Machine-Readable)

For use in Claude skills and automated chart selection logic.

```json
{
  "data_input_types": [
    {
      "id": "bivariate-simple",
      "name": "Simple Bivariate (X-Y)",
      "shorthand": "xy-simple",
      "signature": "[numeric, numeric]",
      "columns": {
        "min": 2,
        "max": 2,
        "structure": ["independent_var", "dependent_var"]
      },
      "characteristics": [
        "2 columns exactly",
        "all numeric",
        "one independent variable",
        "one dependent variable"
      ],
      "charts": {
        "primary": ["line", "scatter", "area"],
        "secondary": ["bar", "column"]
      },
      "filters": "data_input_type: 'bivariate-simple' | columns: 2 | numeric_cols: [all]"
    },
    {
      "id": "bivariate-dual",
      "name": "Bivariate with Two Series (X-Y₁-Y₂)",
      "shorthand": "xy-dual-series",
      "signature": "[numeric|categorical, numeric, numeric]",
      "columns": {
        "min": 3,
        "max": 3,
        "structure": ["x_axis", "y_series_1", "y_series_2"]
      },
      "characteristics": [
        "3 columns exactly",
        "two numeric dependent variables",
        "comparable scales",
        "single x-axis"
      ],
      "charts": {
        "primary": ["multi-line", "multi-bar", "grouped-bar"],
        "secondary": ["dual-axis", "area"]
      },
      "filters": "data_input_type: 'bivariate-dual' | columns: 3 | numeric_cols: [1, 2]"
    },
    {
      "id": "trivariate",
      "name": "Trivariate (X-Y-Z)",
      "shorthand": "xyz-trivariate",
      "signature": "[numeric, numeric, numeric]",
      "columns": {
        "min": 3,
        "max": 3,
        "structure": ["x_dimension", "y_dimension", "z_dimension"]
      },
      "characteristics": [
        "3 numeric columns",
        "3-dimensional space",
        "all numeric values"
      ],
      "charts": {
        "primary": ["bubble", "3d-scatter"],
        "secondary": ["heatmap", "small-multiple"]
      },
      "filters": "data_input_type: 'trivariate' | columns: 3 | numeric_cols: [all]",
      "note": "Z typically represented as size (bubble) or color intensity (heatmap)"
    },
    {
      "id": "categorical-value",
      "name": "Categorical-Value",
      "shorthand": "cat-value",
      "signature": "[categorical, numeric]",
      "columns": {
        "min": 2,
        "max": 2,
        "structure": ["category", "value"]
      },
      "characteristics": [
        "2 columns",
        "discrete unordered categories",
        "numeric values",
        "often percentages or counts"
      ],
      "charts": {
        "primary": ["bar", "pie", "donut"],
        "secondary": ["waffle", "lollipop"]
      },
      "filters": "data_input_type: 'categorical-value' | col_types: ['string', 'numeric']"
    },
    {
      "id": "categorical-multi",
      "name": "Categorical-Multi-Value",
      "shorthand": "cat-multi-value",
      "signature": "[categorical, numeric, numeric, ...]",
      "columns": {
        "min": 3,
        "unlimited": true,
        "structure": ["category", "value_1", "value_2", "..."]
      },
      "characteristics": [
        "first column categorical",
        "2+ numeric columns",
        "represents grouped comparisons",
        "comparable across groups"
      ],
      "charts": {
        "primary": ["grouped-bar", "stacked-bar"],
        "secondary": ["small-multiple", "slope"]
      },
      "filters": "data_input_type: 'categorical-multi' | numeric_cols: [1, 2, ...] | group_by: col_0"
    },
    {
      "id": "time-series",
      "name": "Time Series",
      "shorthand": "time-series",
      "signature": "[datetime, numeric]|[datetime, numeric, numeric, ...]",
      "columns": {
        "min": 2,
        "unlimited": true,
        "structure": ["temporal", "value_1", "value_2", "..."]
      },
      "characteristics": [
        "first column is datetime/date/timestamp",
        "ordered temporally",
        "may be single or multiple series",
        "represents change over time"
      ],
      "charts": {
        "primary": ["line", "area"],
        "secondary": ["column", "candlestick"]
      },
      "filters": "data_input_type: 'time-series' | temporal_col: 0 | numeric_cols: [1, ...]",
      "detection": "column_0_type == 'datetime' OR column_0_contains(date_pattern)"
    },
    {
      "id": "interval-range",
      "name": "Interval/Range Data",
      "shorthand": "interval-range",
      "signature": "[categorical, numeric, numeric]|[categorical, numeric, numeric, numeric, numeric]",
      "columns": {
        "min": 3,
        "max": 5,
        "structure": ["category", "lower|open", "close|value", "upper|high", "optional"]
      },
      "characteristics": [
        "represents bounds or ranges",
        "OHLC format: Open-High-Low-Close",
        "financial or range data",
        "4-5 columns for OHLC"
      ],
      "charts": {
        "primary": ["candlestick", "box-plot"],
        "secondary": ["range-chart", "error-bar"]
      },
      "filters": "data_input_type: 'interval-range' | columns: [3-5] | bounds: [lower, upper]",
      "detection": "column_structure matches [cat, num, num, num, num]"
    },
    {
      "id": "grouped-categorical",
      "name": "Demographic/Grouped Categorical",
      "shorthand": "demo-grouped",
      "signature": "[categorical, categorical, numeric]|[categorical, categorical, numeric, numeric, ...]",
      "columns": {
        "min": 3,
        "unlimited": true,
        "structure": ["primary_category", "subcategory_1", "numeric_1", "numeric_2", "..."]
      },
      "characteristics": [
        "first column: primary category (age, region, etc.)",
        "subsequent columns: subcategories (F/M, product lines, etc.)",
        "numeric values at intersection",
        "cross-tabulation structure"
      ],
      "charts": {
        "primary": ["grouped-bar", "stacked-bar", "heatmap"],
        "secondary": ["treemap"]
      },
      "filters": "data_input_type: 'grouped-categorical' | group_cols: [0, 1] | cross_tab: true"
    },
    {
      "id": "composition",
      "name": "Composition/Parts-of-Whole",
      "shorthand": "composition",
      "signature": "[categorical, numeric, numeric, ...]",
      "columns": {
        "min": 3,
        "unlimited": true,
        "structure": ["item", "part_1", "part_2", "..."]
      },
      "characteristics": [
        "each row is a 'whole'",
        "multiple columns represent parts",
        "values sum to 100% per row",
        "represents proportions"
      ],
      "charts": {
        "primary": ["stacked-bar-100", "stacked-area"],
        "secondary": ["pie", "waffle"]
      },
      "filters": "data_input_type: 'composition' | sum_check: 'per_row_100'",
      "detection": "sum(numeric_cols) per row ≈ 100 OR ≈ 1.0"
    },
    {
      "id": "hierarchical",
      "name": "Ordered Categorical with Levels",
      "shorthand": "hierarchical-cat",
      "signature": "[numeric|ordered, categorical, categorical, categorical, ...]",
      "columns": {
        "min": 4,
        "unlimited": true,
        "structure": ["order", "level_1", "level_2", "level_3", "..."]
      },
      "characteristics": [
        "multiple categorical levels (3+)",
        "hierarchical/taxonomy structure",
        "first column may be ordering",
        "drill-down possible"
      ],
      "charts": {
        "primary": ["treemap", "sunburst"],
        "secondary": ["icicle", "dendrogram"]
      },
      "filters": "data_input_type: 'hierarchical' | levels: 3+ | order_col: 0"
    },
    {
      "id": "matrix",
      "name": "Matrix/Grid",
      "shorthand": "matrix-grid",
      "signature": "[categorical (rows), categorical (cols), numeric|categorical]",
      "columns": {
        "shape": "2D grid",
        "structure": "row_labels × col_labels = cell_values"
      },
      "characteristics": [
        "2D grid structure",
        "row headers and column headers both categorical",
        "cells contain numeric or categorical values",
        "contingency table or confusion matrix"
      ],
      "charts": {
        "primary": ["heatmap", "mosaic-plot"],
        "secondary": ["confusion-matrix", "network"]
      },
      "filters": "data_input_type: 'matrix' | shape: 'grid' | row_labels: categorical | col_labels: categorical"
    },
    {
      "id": "event-time",
      "name": "Event-Timeseries",
      "shorthand": "event-time",
      "signature": "[categorical, datetime]",
      "columns": {
        "min": 2,
        "max": 2,
        "structure": ["event", "timestamp"]
      },
      "characteristics": [
        "event/location identifier",
        "associated datetime",
        "represents point-in-time events",
        "often discrete rather than continuous"
      ],
      "charts": {
        "primary": ["timeline", "calendar-heatmap"],
        "secondary": ["strip-plot", "scatter"]
      },
      "filters": "data_input_type: 'event-time' | col_0: 'categorical' | col_1: 'datetime'"
    }
  ],

  "detector_function": {
    "inputs": ["column_count", "column_types", "column_values_sample"],
    "logic": [
      {
        "condition": "column_count == 2 && all_numeric",
        "output": "bivariate-simple"
      },
      {
        "condition": "column_count == 3 && col_types == [numeric|cat, numeric, numeric]",
        "output": "bivariate-dual OR time-series (if col_0 is datetime)"
      },
      {
        "condition": "column_count == 3 && all_numeric",
        "output": "trivariate"
      },
      {
        "condition": "column_count == 2 && col_types == [categorical, numeric]",
        "output": "categorical-value"
      },
      {
        "condition": "column_count >= 3 && col_0_categorical && col_1_plus_numeric",
        "output": "categorical-multi"
      },
      {
        "condition": "col_0_type == 'datetime' && col_count >= 2",
        "output": "time-series"
      },
      {
        "condition": "column_count == 4 && col_types match [cat, num, num, num]",
        "output": "interval-range"
      },
      {
        "condition": "column_count == 5 && col_types match [cat, num, num, num, num]",
        "output": "interval-range (OHLC)"
      },
      {
        "condition": "sum(numeric_cols) per row ≈ 100",
        "output": "composition"
      },
      {
        "condition": "col_count >= 4 && col_0_cat && col_1_cat && rest_numeric",
        "output": "grouped-categorical"
      },
      {
        "condition": "col_count >= 4 && col_count_numeric >= 3",
        "output": "hierarchical"
      },
      {
        "condition": "shape == 'grid' && row_labels_cat && col_labels_cat",
        "output": "matrix"
      },
      {
        "condition": "col_count == 2 && col_types == [categorical, datetime]",
        "output": "event-time"
      }
    ]
  },

  "chart_capabilities": {
    "line": ["bivariate-simple", "bivariate-dual", "time-series"],
    "scatter": ["bivariate-simple", "trivariate"],
    "bar": ["categorical-value", "categorical-multi", "grouped-categorical"],
    "pie": ["categorical-value", "composition"],
    "area": ["bivariate-simple", "bivariate-dual", "time-series"],
    "bubble": ["trivariate"],
    "heatmap": ["trivariate", "grouped-categorical", "matrix"],
    "treemap": ["hierarchical", "grouped-categorical"],
    "sunburst": ["hierarchical"],
    "candlestick": ["interval-range", "time-series"],
    "timeline": ["event-time", "time-series"],
    "stacked-bar-100": ["composition", "grouped-categorical"],
    "3d-scatter": ["trivariate"]
  },

  "skill_implementation_notes": {
    "priority_detection": "Use detector_logic in order - first match wins",
    "ambiguity_resolution": "If multiple types match, prefer: time-series > categorical-multi > bivariate-dual",
    "fallback": "If uncertain, return ['xy-simple', 'cat-value'] and let user confirm",
    "integration": "Call detector on incoming data, match to data_input_types[id], return charts.primary"
  }
}
```

---

## Compact Reference Table

| Type | Tag | Columns | Column Types | Primary Charts |
|------|-----|---------|--------------|----------------|
| Simple Bivariate | `xy-simple` | 2 | `[num, num]` | Line, Scatter, Area |
| Dual Series | `xy-dual-series` | 3 | `[num\|cat, num, num]` | Multi-Line, Grouped-Bar |
| Trivariate | `xyz-trivariate` | 3 | `[num, num, num]` | Bubble, 3D-Scatter |
| Category-Value | `cat-value` | 2 | `[cat, num]` | Bar, Pie, Donut |
| Category-Multi | `cat-multi-value` | 3+ | `[cat, num, num...]` | Grouped-Bar, Stacked-Bar |
| Time Series | `time-series` | 2+ | `[date, num, num...]` | Line, Area, Candlestick |
| Interval/Range | `interval-range` | 3-5 | `[cat, num, num, num]` | Candlestick, Box-Plot |
| Grouped Categorical | `demo-grouped` | 3+ | `[cat, cat, num...]` | Grouped-Bar, Heatmap |
| Composition | `composition` | 3+ | `[cat, num, num...]` | Stacked-Bar (100%), Pie |
| Hierarchical | `hierarchical-cat` | 4+ | `[num, cat, cat, cat...]` | Treemap, Sunburst |
| Matrix/Grid | `matrix-grid` | Grid | `[row-cat, col-cat, val]` | Heatmap, Mosaic |
| Event-Time | `event-time` | 2 | `[cat, date]` | Timeline, Calendar-HM |

---

## Pseudo-Code for Claude Skill

```python
def auto_select_chart(data: DataFrame) -> str:
    """
    Deterministically select appropriate chart type based on data shape.
    """
    col_count = len(data.columns)
    col_types = [infer_type(col) for col in data.columns]
    
    # Rule-based detection (order matters)
    if col_count == 2:
        if all(t == 'numeric' for t in col_types):
            return detect_time_series(data) or "line-chart"
        elif col_types == ['categorical', 'numeric']:
            return "bar-chart"
    
    if col_count == 3 and col_types[0] == 'datetime':
        return "line-chart"
    
    if col_count == 3 and all(t == 'numeric' for t in col_types):
        return "bubble-chart"
    
    if col_count >= 3 and col_types[0] == 'categorical':
        if is_composition(data):
            return "stacked-bar-chart-100"
        return "grouped-bar-chart"
    
    if is_matrix_shape(data):
        return "heatmap"
    
    # Fallback
    return "bar-chart"

def detect_time_series(data: DataFrame) -> str|None:
    """Check if first column contains datetime values."""
    if is_datetime_column(data.iloc[:, 0]):
        return "line-chart"
    return None

def is_composition(data: DataFrame) -> bool:
    """Check if numeric columns sum to ~100 per row."""
    numeric_cols = data.select_dtypes(include=['number']).columns
    row_sums = data[numeric_cols].sum(axis=1)
    return all((row_sums > 95) & (row_sums < 105))
```

---

**Version:** 1.0  
**Format:** JSON Schema + Pseudo-Code  
**Use Case:** Machine-readable spec for Claude skill implementation
