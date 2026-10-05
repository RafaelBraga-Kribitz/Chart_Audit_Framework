# -*- coding: utf-8 -*-
"""Enrich chart cards and add every catalogue type that is not an alias."""
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

ROOT = Path(r"C:\Users\Benutzer1\Documents\doing\Chart_Audit_Framework\chart-expert")
CHARTS = ROOT / "library" / "CHARTS"
REF = Path(r"C:\Users\Benutzer1\Documents\doing\Chart_Audit_Framework\Deterministic_Data_Visualization_Framework\references")
INDEX = ROOT / "library" / "_INDICES"
LIBINDEX = ROOT / "references" / "chart-library-index.md"

IT_FOR = {
    "time-series": "IT001",
    "cat-value": "IT026",
    "cat-multi-value": "IT029",
    "xy-simple": "IT001",
    "xyz-trivariate": "IT012",
    "interval-range": "IT040",
    "demo-grouped": "IT011",
    "composition": "IT007",
    "hierarchical-cat": "IT024",
    "matrix-grid": "IT021",
    "event-time": "IT009",
}
FT_FOR = {
    "Comparison": "magnitude",
    "Correlation": "correlation",
    "Distribution": "distribution",
    "Part-to-whole": "part-to-whole",
    "Trend-over-time": "change",
    "Geographical": "spatial",
    "Flow": "flow",
    "Ranking": "magnitude",
    "Deviation": "deviation",
    "Concept-viz": "flow",
}
AVOID = ("pie", "donut", "gauge", "radar", "spaghetti", "traffic-light", "traffic light")
CONDITIONAL = ("bubble", "3d", "dual-axis", "combo", "tag-cloud", "word-cloud", "horizon", "sankey", "chord", "alluvial", "stream")

# slug in a catalogue -> existing library stem
ALIASES = {
    "3d-scatterplot": "3d-scatter-plot",
    "bar-chart-horizontal": "horizontal-bar-chart",
    "beeswarm-blot": "beeswarm-plot",
    "bubble-based-heat-map": "bubble-heatmap",
    "bubble-map-chart": "bubble-map",
    "bump-chart-2": "bump-chart",
    "choropleth-map-2": "choropleth-map",
    "column-chart": "bar-chart",
    "gannt-chart": "gantt-chart",
    "gantt": "gantt-chart",
    "dot-chart": "dot-plot",
    "heat-map": "heat-map",
    "heatmap": "heat-map",
    "piechart": "pie-chart",
    "scatterplot": "scatter-plot",
    "stacked-bar": "stacked-bar-chart",
    "swot-analysis": "swot-diagram",
    "table-chart": "data-table",
    "waterfall-plot": "waterfall-chart",
    "win-loss-sparkline": "win-loss-sparkline",
    "bulletgraph": "bullet-graph",
    "barchart": "bar-chart",
    "lollipop": "lollipop-chart",
    "dumbbell": "dumbbell-plot",
    "diverging-bar": "diverging-bar",
    "rose-chart": "nightingale-rose",
    "coxcomb": "nightingale-rose",
    "pictogram": "pictogram",
    "isotype": "pictogram",
    "qq-plot": "qq-plot",
    "q-q-plot": "qq-plot",
    "joyplot": "ridgeline",
    "joy-plot": "ridgeline",
    "circle-packing": "circle-packing",
    "packed-circle": "packed-circle-chart",
    "mosaic-plot": "marimekko-chart",
    "mekko": "marimekko-chart",
    "column": "bar-chart",
    "vertical-bar": "bar-chart",
}


def slugify(name: str) -> str:
    s = name.lower().strip()
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def split_doc(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end < 0:
        return "", text
    return text[4:end], text[end + 4 :]


def fm_get(fm: str, key: str) -> str:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.*)$", fm)
    return m.group(1).strip() if m else ""


def fm_has(fm: str, key: str) -> bool:
    return re.search(rf"(?m)^{re.escape(key)}:", fm) is not None


def parse_list(raw: str) -> list[str]:
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        return [p.strip().strip("'\"") for p in inner.split(",") if p.strip()]
    return [raw] if raw else []


def yaml_list(items: list[str]) -> str:
    return "[" + ", ".join(items) + "]"


def ibcs_for(name: str, complexity: str) -> str:
    n = name.lower()
    if any(k in n for k in AVOID):
        return "avoid"
    if any(k in n for k in CONDITIONAL) or complexity == "Advanced":
        return "conditional"
    return "preferred"


def questions_for(function: str, name: str) -> list[str]:
    q = {
        "Comparison": f"Which category is higher on {name}?",
        "Correlation": f"Do the two measures in {name} move together?",
        "Distribution": f"What is the shape and the tail, not only the average, on {name}?",
        "Part-to-whole": f"How is the whole split on {name}?",
        "Trend-over-time": f"How has the series changed over time on {name}?",
        "Geographical": f"Where is the measure concentrated on {name}?",
        "Flow": f"How does quantity move between states on {name}?",
        "Ranking": f"What is the order of entities on {name}?",
        "Deviation": f"How far is the result from the reference on {name}?",
        "Concept-viz": f"What structure or process does {name} explain?",
    }
    return [q.get(function, f"What does {name} show?"), "Who is the audience, and is this the analysis surface or the communication surface?"]


def surface_note(name: str, complexity: str, ibcs: str, alternatives: list[str]) -> str:
    alt = ", ".join(alternatives[:3]) if alternatives else "a sorted bar or a table"
    if ibcs == "avoid" or complexity == "Advanced":
        return (
            f"`{name}` is a valid analysis chart for a data scientist, researcher, R&D, or development notebook "
            f"(matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. "
            f"Communication surface: retell the finding with {alt}. "
            f"`ibcs_status: {ibcs}` applies to that communication surface only."
        )
    return (
        f"`{name}` can sit on a dashboard, in a report, or in a notebook. "
        f"Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. "
        f"If the page is only a score, pair it with {alt}."
    )


def vault_type(function: str, name: str) -> str:
    n = name.lower()
    if "table" in n:
        return "Table"
    if "scatter" in n or "bubble" in n:
        return "Scatter" if "bubble" not in n else "Bubble"
    if "funnel" in n:
        return "Funnel"
    if "heat" in n:
        return "Heatmap"
    if "waterfall" in n:
        return "Waterfall"
    if "gauge" in n or "bullet" in n:
        return "Gauge" if "gauge" in n else "Bullet"
    if "spark" in n:
        return "Sparkline"
    if "area" in n:
        return "Area"
    if "stack" in n:
        return "Stacked bar"
    if "line" in n or function == "Trend-over-time":
        return "Line"
    if "donut" in n or "pie" in n:
        return "Donut"
    if function in {"Comparison", "Ranking", "Deviation", "Part-to-whole"}:
        return "Bar"
    return "Number"


def dashboard_section(name: str, function: str, complexity: str, ibcs: str, alternatives: list[str]) -> str:
    vt = vault_type(function, name)
    zone = {
        "Trend-over-time": "trend",
        "Deviation": "variance",
        "Distribution": "breakdown",
        "Part-to-whole": "breakdown",
        "Ranking": "breakdown",
        "Flow": "breakdown",
        "Geographical": "breakdown",
        "Correlation": "breakdown",
        "Concept-viz": "detail",
    }.get(function, "score")
    return f"""
## Dashboard and other surfaces

status: placeholder

{surface_note(name, complexity, ibcs, alternatives)}

Suggested communication placement: **{zone}** zone. Vault coarse type, when a scraped template is the layout: **{vt}**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.
"""


# Full cards for types the current 116 miss. purpose is original.
GAP: dict[str, dict] = {}


def g(slug, name, category, function, family, shape, inputs, card, complexity, channels, purpose, use, avoid, mistakes, ibcs=None):
    GAP[slug] = {
        "name": name,
        "category": category,
        "function": function,
        "family": family,
        "shape": shape,
        "inputs": inputs,
        "cardinality": card,
        "complexity": complexity,
        "channels": channels,
        "purpose": purpose,
        "use": use,
        "avoid": avoid,
        "mistakes": mistakes,
        "ibcs": ibcs or ibcs_for(name, complexity),
    }


def load_gap():
    g("horizon-chart", "Horizon Chart", "Temporal", "Trend-over-time", "Chart", ["Area"], ["time-series"], ["medium", "large"], "Advanced", ["position", "color-value"],
      "A horizon chart slices a time series into bands and mirrors negative bands upward so many series fit in a short column.",
      ["Comparing dozens of series for a shared spike", "An analyst scanning a panel in a notebook"],
      ["An executive who has not learned the mirroring", "A single series"],
      ["Leaving the mirror unlabeled", "Using color as the only sign of negative values"])
    g("cycle-plot", "Cycle Plot", "Temporal", "Trend-over-time", "Chart", ["Line"], ["time-series"], ["medium"], "Intermediate", ["position"],
      "A cycle plot shows each season (month, weekday) as its own small series across years, so the seasonal shape and the year trend are both visible.",
      ["Seasonality with a trend underneath", "Operations and demand planning"],
      ["A series with no repeating cycle"],
      ["Averaging the season away before plotting"])
    g("seasonal-subseries", "Seasonal Subseries Plot", "Temporal", "Trend-over-time", "Chart", ["Line"], ["time-series"], ["medium"], "Intermediate", ["position"],
      "Each season gets its own panel, in seasonal order, so a data scientist can see whether January is drifting while the year as a whole looks flat.",
      ["Forecast diagnostics", "R&D and analytics notebooks"],
      ["A non-seasonal series", "An executive score page"],
      ["Panels with different scales that invite false comparison"])
    g("calendar-heatmap", "Calendar Heatmap", "Temporal", "Trend-over-time", "Chart", ["Square"], ["time-series", "matrix-grid"], ["large"], "Basic", ["color-value", "position"],
      "A calendar heatmap maps one value onto each day in a year grid.",
      ["Daily activity, outages, or publishing cadence", "A year at a glance"],
      ["Comparing precise magnitudes", "More than one measure per day"],
      ["A color scale with no zero", "Tiny cells with no tooltip or table behind them"])
    g("punchcard", "Punchcard Plot", "Temporal", "Trend-over-time", "Plot", ["Circle"], ["matrix-grid", "time-series"], ["medium"], "Intermediate", ["position", "area"],
      "A punchcard places a mark on a weekday-by-hour grid. Size or color encodes the count.",
      ["When work, incidents, or traffic cluster in the week", "Operations analytics"],
      ["Precise reading of small differences in area"],
      ["Encoding the value only as area"])
    g("ohlc-chart", "OHLC Chart", "Temporal", "Trend-over-time", "Chart", ["Line"], ["interval-range", "time-series"], ["medium", "large"], "Intermediate", ["position"],
      "An open-high-low-close chart draws the session range and the open and close ticks without a candle body.",
      ["Price or any four-number interval per period", "Finance and trading analysis"],
      ["A general business KPI with one number per period"],
      ["Dropping the open or close so the range is ambiguous"])
    g("heikin-ashi", "Heikin-Ashi Chart", "Temporal", "Trend-over-time", "Chart", ["Bar"], ["interval-range", "time-series"], ["medium"], "Advanced", ["position", "color-hue"],
      "Heikin-Ashi replaces each open and close with a smoothed average of recent prices so the trend is easier to see and the exact price is harder to read.",
      ["Trend direction in a trading notebook"],
      ["Reporting an actual close to a finance audience", "Any KPI that is not a price"],
      ["Treating the smoothed close as the real close"])
    g("point-and-figure", "Point and Figure Chart", "Temporal", "Trend-over-time", "Chart", ["Dot"], ["time-series"], ["medium"], "Advanced", ["position"],
      "Point and figure records price moves of a fixed size and ignores time, so columns alternate between rises and falls.",
      ["Filtering small price noise"],
      ["Anything that must stay on a calendar axis"],
      ["Forgetting that equal columns are not equal time"])
    g("volume-profile", "Volume Profile", "Distribution", "Distribution", "Plot", ["Bar"], ["xy-simple", "cat-value"], ["medium"], "Advanced", ["length", "position"],
      "A volume profile is a histogram turned sideways, showing how much activity occurred at each price or level.",
      ["Market or capacity analysis by level"],
      ["A time trend"],
      ["Reading the tallest bin as a forecast rather than a concentration"])
    g("burndown-chart", "Burndown Chart", "Temporal", "Trend-over-time", "Chart", ["Line"], ["time-series"], ["small-N", "medium"], "Basic", ["position"],
      "A burndown shows work remaining against an ideal line toward zero.",
      ["A development team tracking a sprint or a release"],
      ["Work that is still being added without showing scope changes"],
      ["Hiding added scope so the line looks healthy"])
    g("burnup-chart", "Burnup Chart", "Temporal", "Trend-over-time", "Chart", ["Line"], ["time-series", "cat-multi-value"], ["small-N", "medium"], "Basic", ["position"],
      "A burnup shows work completed rising toward a scope line, so scope changes stay visible.",
      ["Development and project reviews where scope moves"],
      ["A single remaining-work number with no scope"],
      ["One line that mixes completed work and scope"])
    g("cumulative-flow", "Cumulative Flow Diagram", "Temporal", "Flow", "Chart", ["Area"], ["time-series", "composition"], ["medium"], "Intermediate", ["position", "color-hue"],
      "A cumulative flow diagram stacks the count of items in each workflow state over time. Band width is queue size.",
      ["Development and operations flow", "Seeing a bottleneck as a widening band"],
      ["A state model that is not a real sequence"],
      ["A stacked area of unrelated categories"])
    g("run-chart", "Run Chart", "Temporal", "Trend-over-time", "Chart", ["Line", "Dot"], ["time-series"], ["medium", "large"], "Basic", ["position"],
      "A run chart plots a process measure in time order, often with the median, so shifts and trends can be seen before control limits exist.",
      ["Operations, quality, HR cycle time", "A first look before a control chart"],
      ["A ranked category comparison"],
      ["Connecting points that are not in time order"])
    g("win-loss-sparkline", "Win-Loss Sparkline", "Temporal", "Trend-over-time", "Chart", ["Bar"], ["time-series"], ["small-N", "medium"], "Basic", ["position"],
      "A win-loss sparkline encodes only the sign of each period, not the magnitude.",
      ["A row in a table where up or down is enough", "A communication surface with no room for a line"],
      ["When the size of the move is the decision"],
      ["Using it as a bar chart of magnitude"])
    g("ridgeline", "Ridgeline Plot", "Distribution", "Distribution", "Plot", ["Area"], ["cat-value", "demo-grouped"], ["medium"], "Intermediate", ["position", "area"],
      "Ridgelines stack partially overlapping density curves so several groups can be compared.",
      ["A data scientist comparing distributions across segments"],
      ["An executive score", "More groups than the overlap can bear"],
      ["Hidden baselines", "Densities with different sample sizes and no note"])
    g("raincloud-plot", "Raincloud Plot", "Distribution", "Distribution", "Plot", ["Area", "Dot"], ["cat-value", "demo-grouped"], ["medium"], "Advanced", ["position", "area"],
      "A raincloud combines a density, a box or interval, and the raw points.",
      ["Research and R&D figures where the reader must see atoms and the summary"],
      ["A dashboard tile"],
      ["Dropping the points and keeping only the cloud"])
    g("qq-plot", "Q-Q Plot", "Distribution", "Distribution", "Plot", ["Dot"], ["xy-simple"], ["medium", "large"], "Advanced", ["position"],
      "A Q-Q plot compares the quantiles of a sample with a reference distribution or another sample.",
      ["Model checking in a notebook", "Asking whether a residual is roughly normal"],
      ["A business dashboard"],
      ["A diagonal that is decorative rather than the reference"])
    g("stem-and-leaf", "Stem-and-Leaf Plot", "Distribution", "Distribution", "Plot", ["Dot"], ["xy-simple"], ["small-N", "medium"], "Intermediate", ["position"],
      "A stem-and-leaf keeps the digits of each value and bins them, so the distribution and the raw numbers are the same picture.",
      ["Small samples in teaching or a working note"],
      ["Large N", "An executive page"],
      ["Stems with inconsistent interval width"])
    g("letter-value-plot", "Letter-Value Plot", "Distribution", "Distribution", "Plot", ["Box"], ["cat-value"], ["medium", "large"], "Advanced", ["position", "length"],
      "A letter-value plot extends the box plot with more quantiles so the tail is described without hiding it in a fence.",
      ["Large samples where a box plot's whisker is too crude"],
      ["Tiny samples"],
      ["Reading every box as a confidence interval"])
    g("frequency-polygon", "Frequency Polygon", "Distribution", "Distribution", "Chart", ["Line"], ["xy-simple", "demo-grouped"], ["medium"], "Intermediate", ["position"],
      "A frequency polygon joins bin counts with a line so several distributions can be overlaid more lightly than histograms.",
      ["Comparing a few distributions in an analysis notebook"],
      ["A single precise bin count for an audit"],
      ["Bins of unequal width drawn as if they were equal"])
    g("barcode-plot", "Barcode Plot", "Distribution", "Distribution", "Plot", ["Line"], ["xy-simple"], ["large"], "Intermediate", ["position"],
      "A barcode plot draws one thin line per observation on a single axis.",
      ["Seeing atoms and clumps when N is large"],
      ["Reading a mean"],
      ["Overlapping lines with no jitter and no density companion"])
    g("statistical-funnel-plot", "Statistical Funnel Plot", "Distribution", "Deviation", "Plot", ["Dot"], ["xy-simple", "cat-value"], ["medium"], "Advanced", ["position"],
      "A statistical funnel plot shows an estimate against its precision, with control limits that narrow as the sample grows. It is not a sales funnel.",
      ["Institution or site comparisons in research and quality"],
      ["A stage-conversion story"],
      ["Limits that ignore the sample size"])
    g("forest-plot", "Forest Plot", "Comparison", "Comparison", "Plot", ["Dot", "Line"], ["cat-value", "interval-range"], ["medium"], "Advanced", ["position"],
      "A forest plot shows an estimate and an interval for each study, group, or model, often with a pooled mark.",
      ["Research synthesis", "A data scientist comparing segments with uncertainty"],
      ["A dashboard of point KPIs with no interval"],
      ["Intervals that are not the same statistic"])
    g("bland-altman", "Bland-Altman Plot", "Relationship", "Correlation", "Plot", ["Dot"], ["xy-simple"], ["medium"], "Advanced", ["position"],
      "A Bland-Altman plot shows the difference of two methods against their average, so bias and limits of agreement are visible.",
      ["Method comparison in R&D or a lab notebook"],
      ["A correlation slide for executives"],
      ["A scatter of the two methods presented as agreement"])
    g("survival-curve", "Survival Curve", "Temporal", "Trend-over-time", "Chart", ["Line"], ["time-series", "interval-range"], ["medium"], "Advanced", ["position"],
      "A survival curve shows the share of a cohort still in a state as time passes, accounting for cases that have not finished.",
      ["Retention research, reliability, clinical or product cohorts"],
      ["A simple churn percent with no time axis"],
      ["Dropping censored cases and calling the rest a rate"])
    g("roc-curve", "ROC Curve", "Relationship", "Correlation", "Chart", ["Line"], ["xy-simple"], ["small-N", "medium"], "Advanced", ["position"],
      "A ROC curve plots true positive rate against false positive rate as a threshold moves.",
      ["Model evaluation by a data scientist or development team"],
      ["A business KPI dashboard"],
      ["A curve with no baseline and no prevalence note"])
    g("precision-recall-curve", "Precision-Recall Curve", "Relationship", "Correlation", "Chart", ["Line"], ["xy-simple"], ["small-N", "medium"], "Advanced", ["position"],
      "A precision-recall curve shows the tradeoff when the class of interest is rare.",
      ["Model evaluation when positives are scarce"],
      ["A balanced accuracy story told only with ROC"],
      ["Omitting the base rate"])
    g("diverging-bar", "Diverging Bar", "Comparison", "Deviation", "Chart", ["Bar"], ["cat-value"], ["small-N", "medium"], "Basic", ["position", "length"],
      "A diverging bar grows left or right from a baseline so the sign of the gap is the position.",
      ["Actual versus plan", "Sentiment or surplus and deficit", "Executive variance"],
      ["A baseline that is not meaningful"],
      ["Sorting alphabetically", "A y-axis that does not include the baseline"])
    g("diverging-stacked-bar", "Diverging Stacked Bar", "Composition", "Part-to-whole", "Chart", ["Bar"], ["composition", "demo-grouped"], ["small-N", "medium"], "Intermediate", ["position", "length", "color-hue"],
      "A diverging stacked bar centers a Likert or sentiment scale so agreement and disagreement grow in opposite directions.",
      ["Survey results for HR, research, or customer analytics"],
      ["Unordered categories", "More than about seven scale points"],
      ["A stack that hides the neutral share"])
    g("spine-chart", "Spine Chart", "Comparison", "Deviation", "Chart", ["Bar"], ["cat-value", "composition"], ["small-N", "medium"], "Intermediate", ["position", "length"],
      "A spine chart (surplus-deficit) shows the excess or shortfall against a reference share.",
      ["Mix versus a standard mix", "Budget share versus actual share"],
      ["A plain part-to-whole with no reference"],
      ["A reference that is not stated"])
    g("arrow-plot", "Arrow Plot", "Comparison", "Deviation", "Chart", ["Line"], ["cat-multi-value"], ["small-N", "medium"], "Basic", ["position"],
      "An arrow or comet plot connects a start value to an end value for each entity.",
      ["Before and after", "Two periods when slope charts are wanted with direction"],
      ["More than two times"],
      ["Arrows so dense the direction cannot be read"])
    g("combo-chart", "Combo Chart", "Comparison", "Comparison", "Chart", ["Bar", "Line"], ["cat-multi-value", "time-series"], ["small-N", "medium"], "Intermediate", ["position", "length"],
      "A combo chart draws bars and a line on the same category or time axis. A second axis is a warning, not a feature.",
      ["A volume and a rate that share a category and are both labeled in units", "Marketing analytics when bars are counts and the line is a rate"],
      ["Two series forced to share a scale that makes one invisible", "An executive page that implies correlation from a dual axis"],
      ["Dual axes with no unit labels", "A line that is a second copy of the bars"])
    g("big-number", "Big Number Tile", "Specialized", "Comparison", "Chart", ["Icon"], ["cat-value"], ["small-N"], "Basic", ["position"],
      "A big number is a single value with its comparison (delta, target, or prior) written next to it. The number without the comparison is not the chart.",
      ["A score zone", "The communication surface of any KPI"],
      ["A distribution", "A lonely number with no comparison"],
      ["Color as the only sign of good or bad", "More precision than the decision uses"])
    g("thermometer", "Thermometer", "Specialized", "Deviation", "Chart", ["Bar"], ["cat-value"], ["small-N"], "Basic", ["length"],
      "A thermometer fills toward a target. It is a one-series progress mark.",
      ["A single fundraising or quota total against one goal"],
      ["Comparing categories", "A rate that is not a fill toward a known total"],
      ["A fill that is not scaled to the target"])
    g("progress-bar", "Progress Bar", "Specialized", "Deviation", "Chart", ["Bar"], ["cat-value"], ["small-N", "medium"], "Basic", ["length"],
      "A progress bar shows completion toward a declared total.",
      ["Implementation status, quota, or a project percent complete"],
      ["A KPI that has no meaningful total"],
      ["Percents that can exceed 100 with no note"])
    g("nightingale-rose", "Nightingale Rose", "Composition", "Part-to-whole", "Chart", ["Area"], ["cat-value", "composition"], ["small-N"], "Intermediate", ["area", "angle"],
      "A Nightingale rose encodes values as the radius or area of equal-angle sectors. Area, not angle, carries the value.",
      ["A historical or analytical look at cyclic magnitudes"],
      ["Precise comparison", "An executive management page"],
      ["Reading angle as the value", "Too many sectors"])
    g("pictogram", "Pictogram", "Composition", "Part-to-whole", "Glyph", ["Icon"], ["cat-value", "composition"], ["small-N"], "Basic", ["position"],
      "A pictogram or isotype repeats a symbol so each icon is a stated number of units.",
      ["Public and executive counts where a unit is concrete", "A communication surface"],
      ["Unequal icons", "Values that do not divide cleanly and are faked"],
      ["Icons of different sizes", "A partial icon with no legend"])
    g("icon-array", "Icon Array", "Composition", "Part-to-whole", "Glyph", ["Icon"], ["composition"], ["small-N"], "Basic", ["position", "color-hue"],
      "An icon array shows a percent as a grid of marks, usually out of 100 or 10.",
      ["Risk communication", "A share a public audience must feel"],
      ["More than two or three classes", "Precise audit values"],
      ["A grid whose total is not obvious"])
    g("voronoi-treemap", "Voronoi Treemap", "Composition", "Part-to-whole", "Chart", ["Polygon"], ["hierarchical-cat", "composition"], ["medium"], "Advanced", ["area"],
      "A Voronoi treemap fills a shape with cells whose area encodes a value, without a rectangular treemap's aspect ratios.",
      ["Hierarchical magnitudes in an analytical view"],
      ["Precise comparison of close values"],
      ["Cells the reader must compare by area alone with no labels"])
    g("icicle-chart", "Icicle Chart", "Composition", "Part-to-whole", "Chart", ["Bar"], ["hierarchical-cat"], ["medium"], "Intermediate", ["length", "position"],
      "An icicle chart shows a hierarchy as stacked rows. Width is the value. Reading order is the parent-child path.",
      ["File systems, org cost, or any nested magnitude"],
      ["A flat category list"],
      ["Color as a second magnitude"])
    g("circle-packing", "Circle Packing", "Composition", "Part-to-whole", "Chart", ["Circle"], ["hierarchical-cat", "composition"], ["medium"], "Intermediate", ["area"],
      "Circle packing nests circles whose area encodes value. It is distinct from a packed bubble that has no containment.",
      ["A hierarchy when containment is the message"],
      ["Precise rank of close values", "The existing packed-circle card when there is no nesting"],
      ["Radius used instead of area"])
    g("scatter-marginals", "Scatter with Marginals", "Relationship", "Correlation", "Plot", ["Dot"], ["xy-simple"], ["medium", "large"], "Intermediate", ["position"],
      "A scatter with marginal histograms or densities shows the joint pattern and each axis distribution.",
      ["A data science notebook checking two continuous measures"],
      ["A dashboard tile with no room for the margins"],
      ["Margins on a transformed scale the points do not use"])
    g("radviz", "RadViz", "Relationship", "Correlation", "Plot", ["Dot"], ["cat-multi-value"], ["medium"], "Advanced", ["position"],
      "RadViz places features around a circle and pulls each point toward the features where it is high.",
      ["A multivariate exploratory view"],
      ["A claim about a precise distance"],
      ["Feature order that silently changes the picture"])
    g("andrews-curves", "Andrews Curves", "Relationship", "Correlation", "Chart", ["Line"], ["cat-multi-value"], ["medium"], "Advanced", ["position", "color-hue"],
      "Andrews curves turn each multivariate row into a Fourier curve so similar rows bundle.",
      ["Exploratory clustering in a notebook"],
      ["An executive comparison"],
      ["Reading a peak as a single original variable"])
    g("hierarchical-edge-bundling", "Hierarchical Edge Bundling", "Relationship", "Flow", "Diagram", ["Line"], ["hierarchical-cat", "matrix-grid"], ["large"], "Advanced", ["position", "color-hue"],
      "Hierarchical edge bundling groups links that share an ancestor so a dense network becomes a set of bundles.",
      ["Large adjacency structures in a technical review"],
      ["A small network a node-link diagram can show", "A precise path reading"],
      ["Bundles that look like volume they do not encode"])
    g("upset-plot", "UpSet Plot", "Relationship", "Part-to-whole", "Chart", ["Bar", "Dot"], ["demo-grouped", "matrix-grid"], ["medium"], "Intermediate", ["position", "length"],
      "An UpSet plot shows intersection sizes of many sets. Dots mark which sets are in each intersection. Bars show the size.",
      ["More than three sets, where a Venn diagram fails", "Research and product analytics"],
      ["Two or three sets a bar can show"],
      ["Unsorted intersections", "A Venn of six sets"])
    g("kpi-tree", "KPI Tree", "Specialized", "Concept-viz", "Diagram", ["Line"], ["hierarchical-cat"], ["small-N", "medium"], "Basic", ["position"],
      "A KPI tree decomposes an outcome into the inputs of its formula. It is a model of the measure, not a chart of a time series.",
      ["Explaining a formula to any audience", "From contribution margin down to hours and rate"],
      ["A decorative org chart of departments"],
      ["Nodes that are not actually in the formula"])
    g("dupont-tree", "DuPont Tree", "Specialized", "Concept-viz", "Diagram", ["Line"], ["hierarchical-cat"], ["small-N"], "Intermediate", ["position"],
      "A DuPont tree splits return on equity into margin, turnover, and leverage, or an analogous identity the business actually uses.",
      ["Finance analysis and an executive bridge from a ratio to its drivers"],
      ["A tree of unrelated KPIs"],
      ["A DuPont identity the ledger does not support"])
    g("strategy-map", "Strategy Map", "Specialized", "Concept-viz", "Diagram", ["Line"], ["hierarchical-cat"], ["small-N"], "Basic", ["position"],
      "A strategy map links objectives across perspectives (capability, process, customer, financial) with arrows that claim cause.",
      ["Showing how an OKR portfolio is supposed to connect"],
      ["A data chart", "Arrows with no evidence labeled as fact"],
      ["Dozens of boxes", "Causes that are only hopes"])
    g("journey-map", "Journey Map", "Specialized", "Concept-viz", "Diagram", ["Line"], ["event-time"], ["small-N", "medium"], "Basic", ["position"],
      "A journey map lays stages of an experience and the evidence at each stage.",
      ["Customer, employee, or patient journeys for research and service design"],
      ["A funnel of unrelated bars"],
      ["Stages the person does not actually pass through"])
    g("service-blueprint", "Service Blueprint", "Specialized", "Concept-viz", "Diagram", ["Line"], ["event-time", "hierarchical-cat"], ["medium"], "Intermediate", ["position"],
      "A service blueprint shows the customer journey, the frontstage, the backstage, and the support process on one time axis.",
      ["Operations and service design"],
      ["A single KPI"],
      ["Swimlanes that do not match the real organization"])
    g("value-stream-map", "Value Stream Map", "Specialized", "Concept-viz", "Diagram", ["Line"], ["event-time"], ["small-N", "medium"], "Intermediate", ["position"],
      "A value stream map shows process steps, waits, and information flow so lead time can be seen as waiting plus work.",
      ["Operations and development flow reviews"],
      ["A Gantt of a project plan"],
      ["Times that are targets presented as observations"])
    g("decision-tree", "Decision Tree", "Specialized", "Concept-viz", "Diagram", ["Line"], ["hierarchical-cat"], ["small-N", "medium"], "Intermediate", ["position"],
      "A decision tree splits on conditions. A statistical tree shows model splits. A management tree shows choices. The card must say which.",
      ["Model explanation for a data scientist", "A documented decision path"],
      ["A hierarchy of departments"],
      ["Splits with no criterion"])
    g("causal-loop", "Causal Loop Diagram", "Specialized", "Concept-viz", "Diagram", ["Line"], ["matrix-grid"], ["small-N", "medium"], "Intermediate", ["position"],
      "A causal loop diagram shows reinforcing and balancing feedback with signed arrows. It is a theory, not a measured flow.",
      ["Systems conversations in strategy or R&D"],
      ["A Sankey of real quantities"],
      ["Arrows labeled as data when they are hypotheses"])
    g("sipoc", "SIPOC Diagram", "Specialized", "Concept-viz", "Diagram", ["Bar"], ["cat-multi-value"], ["small-N"], "Basic", ["position"],
      "A SIPOC names suppliers, inputs, process steps, outputs, and customers for one process.",
      ["Scoping a process before choosing KPIs"],
      ["A performance result"],
      ["A SIPOC so detailed it becomes a procedure"])
    g("dorling-cartogram", "Dorling Cartogram", "Geospatial", "Geographical", "Map", ["Circle"], ["cat-value"], ["medium"], "Intermediate", ["position", "area"],
      "A Dorling cartogram replaces regions with sized circles that keep roughly geographic neighbors.",
      ["When land area would dominate a choropleth", "Analytics and public communication"],
      ["A reader who needs real geography to navigate"],
      ["Circle area that is not the value"])
    g("hex-cartogram", "Hex Cartogram", "Geospatial", "Geographical", "Map", ["Polygon"], ["cat-value"], ["medium"], "Intermediate", ["color-value", "position"],
      "A hex cartogram gives each region an equal hex so a choropleth is not ruled by large rural areas.",
      ["Comparing regions with very different land area"],
      ["A geographic task such as routing"],
      ["Hexes that invent adjacency"])
    g("bivariate-choropleth", "Bivariate Choropleth", "Geospatial", "Geographical", "Map", ["Polygon"], ["cat-multi-value"], ["medium"], "Advanced", ["color-hue", "color-value"],
      "A bivariate choropleth encodes two variables with a two-dimensional color legend.",
      ["An analyst who will read the legend", "Research maps"],
      ["An executive glance", "Two variables that are not both rates or both comparable"],
      ["A legend the reader cannot decode"])
    g("dasymetric-map", "Dasymetric Map", "Geospatial", "Geographical", "Map", ["Polygon"], ["cat-value"], ["medium", "large"], "Advanced", ["color-value"],
      "A dasymetric map redistributes a value using a related land or population layer so the shade follows where the phenomenon can exist.",
      ["Analyst and researcher maps of rates that official boundaries distort"],
      ["A quick executive choropleth"],
      ["A redistribution with no stated layer"])
    g("spike-map", "Spike Map", "Geospatial", "Geographical", "Map", ["Line"], ["cat-value"], ["medium"], "Intermediate", ["length", "position"],
      "A spike map draws a bar rising from each place. Height is the value. Occlusion is the risk.",
      ["A few sites with very different magnitudes"],
      ["Hundreds of spikes", "A precise reading of hidden spikes"],
      ["3D perspective that changes apparent height"])
    g("data-table", "Data Table", "Specialized", "Comparison", "Table", ["Square"], ["cat-multi-value", "matrix-grid"], ["medium", "large"], "Basic", ["position"],
      "A data table shows entities in rows and measures in columns. It is the right chart when the reader must look up a value.",
      ["Detail zones", "Any audience that needs the number itself", "The most common scraped dashboard mark"],
      ["A pattern that a bar would show faster, when lookup is not the job"],
      ["Too many decimals", "No unit in the column header", "Color as the only encoding of a variance"])
    g("ibcs-variance-table", "IBCS Variance Table", "Specialized", "Deviation", "Table", ["Bar", "Line"], ["cat-multi-value"], ["medium", "large"], "Intermediate", ["position", "length"],
      "An IBCS-style variance table puts the entity, actual, plan, absolute variance, percent variance, and a sparkline or bullet on one row.",
      ["Finance, operations, and any actual-versus-plan communication", "Executive and analyst reviews"],
      ["A table of unrelated metrics with traffic lights"],
      ["Variances with inconsistent signs", "A sparkline on a different scale per row without a note"])


load_gap()


SKIP = {
    "about", "index", "home", "home-list", "choosing-the-right-chart",
    "source-https-chart-guide-design", "title-how-to-choose-the-right-chart",
    "favicon", "wp-content", "wp-includes", "site", "xmlrpc",
}


def catalogue_slugs() -> dict[str, str]:
    found: dict[str, str] = {}
    dt = REF / "datavizproject.com" / "data-type"
    if dt.exists():
        for p in dt.iterdir():
            name = p.name[2:] if p.name.startswith("._") else p.name
            if not name or name.startswith(".") or name == "DS_Store":
                continue
            found.setdefault(slugify(name), "datavizproject")
    for base, source in (
        (REF / "datavizcatalogue.com", "datavizcatalogue"),
        (REF / "www.data-to-viz.com", "data-to-viz"),
        (REF / "chartmaker.visualisingdata.com", "chartmaker"),
    ):
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if p.suffix.lower() not in {".html", ".md"}:
                continue
            if p.name.startswith("._"):
                continue
            found.setdefault(slugify(p.stem), source)
    for slug in GAP:
        found.setdefault(slug, "gap-list")
    # Chart.Guide names from the local notes
    guide = REF / "MD_Pages"
    if guide.exists():
        for p in guide.glob("*.md"):
            text = p.read_text(encoding="utf-8", errors="replace")
            for line in text.splitlines():
                line = line.strip()
                if not line or line.startswith("!") or line.startswith("#") or len(line) > 40:
                    continue
                if re.search(r"chart|plot|map|diagram|graph|bar|table", line, re.I):
                    found.setdefault(slugify(line), "chart.guide")
    return found


def existing_index() -> dict[str, Path]:
    out = {}
    for p in CHARTS.rglob("*.md"):
        text = p.read_text(encoding="utf-8", errors="replace")
        fm, _ = split_doc(text)
        name = fm_get(fm, "name") or p.stem
        out[slugify(name)] = p
        out[p.stem] = p
    return out


def infer_meta(slug: str) -> dict:
    if slug in GAP:
        return GAP[slug]
    title = slug.replace("-", " ").title()
    function = "Comparison"
    category = "Comparison"
    family = "Chart"
    inputs = ["cat-value"]
    if any(k in slug for k in ("map", "choropleth", "cartogram")):
        function, category, family, inputs = "Geographical", "Geospatial", "Map", ["cat-value"]
    elif any(k in slug for k in ("scatter", "bubble", "correlation", "parallel", "radviz")):
        function, category, family, inputs = "Correlation", "Relationship", "Plot", ["xy-simple"]
    elif any(k in slug for k in ("histogram", "box", "violin", "density", "distribution")):
        function, category, family, inputs = "Distribution", "Distribution", "Plot", ["xy-simple"]
    elif any(k in slug for k in ("sankey", "alluvial", "chord", "flow", "funnel")):
        function, category, family, inputs = "Flow", "Relationship", "Diagram", ["cat-multi-value"]
    elif any(k in slug for k in ("pie", "donut", "treemap", "stack", "waffle", "share")):
        function, category, family, inputs = "Part-to-whole", "Composition", "Chart", ["composition"]
    elif any(k in slug for k in ("line", "area", "time", "gantt", "spark", "candle")):
        function, category, family, inputs = "Trend-over-time", "Temporal", "Chart", ["time-series"]
    elif any(k in slug for k in ("diagram", "tree", "map-", "org", "mind", "flow-chart")):
        function, category, family, inputs = "Concept-viz", "Specialized", "Diagram", ["hierarchical-cat"]
    elif "table" in slug:
        function, category, family, inputs = "Comparison", "Specialized", "Table", ["cat-multi-value"]
    complexity = "Advanced" if any(k in slug for k in ("3d", "radviz", "hex", "contour", "chernoff")) else "Intermediate"
    return {
        "name": title,
        "category": category,
        "function": function,
        "family": family,
        "shape": ["Line"] if family == "Chart" else ["Dot"],
        "inputs": inputs,
        "cardinality": ["small-N", "medium"],
        "complexity": complexity,
        "channels": ["position"],
        "purpose": (
            f"{title} is the chart type catalogued under this name. "
            f"Use it for a {function.lower()} question when the data match {', '.join(inputs)}. "
            f"On an analysis surface (notebook, pandas, or matplotlib) it can stay technical. "
            f"On an executive or client surface, prefer a simpler cousin if this encoding is hard to read."
        ),
        "use": [f"A {function.lower()} question with data shaped as {inputs[0]}", "Confirm the encoding against the audience before it leaves a notebook"],
        "avoid": ["A different analytical question than " + function, "An audience that cannot read the encoding, unless a simpler chart carries the message"],
        "mistakes": ["Choosing it because the tool defaults to it", "Using it on an executive page when a bar, line, or table would answer the question"],
        "ibcs": ibcs_for(title, complexity),
    }


def render_card(slug: str, meta: dict, source: str) -> str:
    its = []
    for i in meta["inputs"]:
        if i in IT_FOR and IT_FOR[i] not in its:
            its.append(IT_FOR[i])
    ibcs = meta["ibcs"]
    alts = ["bar-chart", "line-chart", "data-table"]
    q = questions_for(meta["function"], meta["name"])
    fm = f"""---
name: {meta['name']}
category: {meta['category']}
input_type: {yaml_list(meta['inputs'])}
it_variants: {yaml_list(its)}
analytical_function: {meta['function']}
visual_family: {meta['family']}
ft_family: {FT_FOR.get(meta['function'], 'magnitude')}
shape_primitive: {yaml_list(meta['shape'])}
cardinality_fit: {yaml_list(meta['cardinality'])}
audience: [Executive, Analytics, Technical, Public]
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
complexity: {meta['complexity']}
encoding_channels: {yaml_list(meta['channels'])}
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: []
alternatives: {yaml_list(alts)}
ibcs_status: {ibcs}
questions: ["{q[0]}", "{q[1]}"]
related_kpis: []
analysis_surface: notebook
communication_surface: dashboard
source: [{source}]
implementations:
  matplotlib: {{status: stub, source_file: null, last_iterated: null}}
  plotly: {{status: stub, source_file: null, last_iterated: null}}
  altair: {{status: stub, source_file: null, last_iterated: null}}
  d3: {{status: stub, source_file: null, last_iterated: null}}
  tableau: {{status: stub, source_file: null, last_iterated: null}}
  powerbi: {{status: stub, source_file: null, last_iterated: null}}
  excel: {{status: stub, source_file: null, last_iterated: null}}
---
"""
    use = "\n".join(f"- {u}" for u in meta["use"])
    avoid = "\n".join(f"- {u}" for u in meta["avoid"])
    mistakes = "\n".join(f"- {u}" for u in meta["mistakes"])
    body = f"""
# {meta['name']}

## Description
{meta['purpose']}

## When to Use
{use}

## When NOT to Use
{avoid}

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | {", ".join(meta['inputs'])} | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
{mistakes}

{dashboard_section(meta['name'], meta['function'], meta['complexity'], ibcs, alts)}

## Implementation Notes

### matplotlib
```python
# Stub. Map columns to the input type {meta['inputs'][0]} before rendering.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_title("{meta['name']}")
```

### pandas
A technical audience can stay in a notebook: prepare the frame for `{meta['inputs'][0]}`, then plot with pandas or matplotlib. Do not assume the same figure is the executive dashboard.

### plotly / altair / excel / tableau
Use the tool's mark that encodes {", ".join(meta['channels'])}. If the tool defaults to a pie, gauge, or dual axis, switch marks unless that default is truly the question.
"""
    return fm + body


def enrich_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, body = split_doc(text)
    if not fm:
        return
    name = fm_get(fm, "name") or path.stem
    function = fm_get(fm, "analytical_function") or "Comparison"
    complexity = fm_get(fm, "complexity") or "Basic"
    inputs = parse_list(fm_get(fm, "input_type") or "[cat-value]")
    alts = parse_list(fm_get(fm, "alternatives") or "[]")
    # alternatives may be list of names not slugs; keep as-is
    additions = []
    if not fm_has(fm, "ft_family"):
        additions.append(f"ft_family: {FT_FOR.get(function, 'magnitude')}")
    if not fm_has(fm, "ibcs_status"):
        additions.append(f"ibcs_status: {ibcs_for(name, complexity)}")
    if not fm_has(fm, "questions"):
        q = questions_for(function, name)
        additions.append(f'questions: ["{q[0]}", "{q[1]}"]')
    if not fm_has(fm, "related_kpis"):
        additions.append("related_kpis: []")
    if not fm_has(fm, "analysis_surface"):
        ibcs = ibcs_for(name, complexity)
        additions.append("analysis_surface: notebook" if ibcs != "preferred" or complexity == "Advanced" else "analysis_surface: plot")
        additions.append("communication_surface: dashboard")
    if not fm_has(fm, "audience_roles"):
        additions.append("audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]")
    variants = fm_get(fm, "it_variants")
    if variants.strip() in {"", "[]"}:
        its = []
        for i in inputs:
            if i in IT_FOR and IT_FOR[i] not in its:
                its.append(IT_FOR[i])
        if its:
            fm = re.sub(r"(?m)^it_variants:.*$", "it_variants: " + yaml_list(its), fm, count=1)
    if additions:
        fm = fm.rstrip() + "\n" + "\n".join(additions) + "\n"
    if "## Dashboard" not in body and "## Dashboard and other surfaces" not in body:
        ibcs = ibcs_for(name, complexity)
        alt_names = alts if alts else ["bar-chart", "line-chart"]
        block = dashboard_section(name, function, complexity, ibcs, alt_names)
        if "## Implementation Notes" in body:
            body = body.replace("## Implementation Notes", block + "\n## Implementation Notes", 1)
        else:
            body = body.rstrip() + "\n" + block
    path.write_text("---\n" + fm.strip() + "\n---\n" + body.lstrip("\n"), encoding="utf-8")


def write_indexes(cards: list[dict], alias_rows: list[tuple[str, str]]) -> None:
    INDEX.mkdir(parents=True, exist_ok=True)
    by_fn: dict[str, list[str]] = {}
    by_in: dict[str, list[str]] = {}
    by_card: dict[str, list[str]] = {}
    by_fam: dict[str, list[str]] = {}
    by_ft: dict[str, list[str]] = {}
    by_ibcs: dict[str, list[str]] = {}
    by_aud: dict[str, list[str]] = {}
    by_cx: dict[str, list[str]] = {}
    for c in cards:
        by_fn.setdefault(c["function"], []).append(f"- {c['name']} → `{c['rel']}`")
        by_fam.setdefault(c["family"], []).append(f"- {c['name']} → `{c['rel']}`")
        by_ft.setdefault(c["ft"], []).append(f"- {c['name']} → `{c['rel']}`")
        by_ibcs.setdefault(c["ibcs"], []).append(f"- {c['name']} → `{c['rel']}`")
        by_cx.setdefault(c["complexity"], []).append(f"- {c['name']} → `{c['rel']}`")
        for i in c["inputs"]:
            by_in.setdefault(i, []).append(f"- {c['name']} → `{c['rel']}`")
        for cd in c["cardinality"]:
            by_card.setdefault(cd, []).append(f"- {c['name']} → `{c['rel']}`")
        for a in c["audience"]:
            by_aud.setdefault(a, []).append(f"- {c['name']} → `{c['rel']}`")

    def dump(title, groups):
        lines = [f"# Index: {title}", ""]
        for k in sorted(groups):
            lines.append(f"## {k}")
            lines.extend(sorted(set(groups[k])))
            lines.append("")
        return "\n".join(lines)

    (INDEX / "by-function.md").write_text(dump("Charts by Analytical Function", by_fn), encoding="utf-8")
    (INDEX / "by-input-type.md").write_text(dump("Charts by Input Type", by_in), encoding="utf-8")
    (INDEX / "by-cardinality.md").write_text(dump("Charts by Cardinality", by_card), encoding="utf-8")
    (INDEX / "by-visual-family.md").write_text(dump("Charts by Visual Family", by_fam), encoding="utf-8")
    (INDEX / "by-ft-family.md").write_text(dump("Charts by FT Family", by_ft), encoding="utf-8")
    (INDEX / "by-ibcs.md").write_text(dump("Charts by IBCS Status", by_ibcs), encoding="utf-8")
    (INDEX / "by-audience.md").write_text(dump("Charts by Audience Tolerance", by_aud), encoding="utf-8")
    (INDEX / "by-complexity.md").write_text(dump("Charts by Complexity", by_cx), encoding="utf-8")
    (INDEX / "aliases.md").write_text(
        "# Chart aliases\n\nCatalogue names that point at one canonical card.\n\n"
        + "\n".join(f"- `{a}` → `{b}`" for a, b in sorted(alias_rows)),
        encoding="utf-8",
    )
    counts: dict[str, int] = {}
    for c in cards:
        counts[c["category"]] = counts.get(c["category"], 0) + 1
    lines = [
        f"# Chart Library Index",
        f"Total: {len(cards)} canonical charts",
        f"Last updated: {date.today().isoformat()}",
        "",
        "## Chart Count by Category",
    ]
    for k in sorted(counts):
        lines.append(f"- {k}: {counts[k]}")
    lines += ["", "| Chart Name | Category | Visual Family | FT Family | IBCS | Complexity | Audience | File | Function | Input Types |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    for c in sorted(cards, key=lambda x: (x["category"], x["name"])):
        lines.append(
            f"| {c['name']} | {c['category']} | {c['family']} | {c['ft']} | {c['ibcs']} | {c['complexity']} | {', '.join(c['audience'])} | `{c['rel']}` | {c['function']} | {', '.join(c['inputs'])} |"
        )
    lines += ["", "## Aliases", "", "See `library/_INDICES/aliases.md`.", ""]
    LIBINDEX.write_text("\n".join(lines), encoding="utf-8")


def collect_cards() -> list[dict]:
    # one canonical path per name: prefer the file whose folder matches category
    by_name: dict[str, list[Path]] = {}
    for p in CHARTS.rglob("*.md"):
        fm, _ = split_doc(p.read_text(encoding="utf-8", errors="replace"))
        name = fm_get(fm, "name") or p.stem
        by_name.setdefault(name, []).append(p)
    cards = []
    for name, paths in by_name.items():
        def score(p: Path) -> int:
            fm, _ = split_doc(p.read_text(encoding="utf-8", errors="replace"))
            cat = fm_get(fm, "category")
            return 0 if p.parent.name == cat else 1
        path = sorted(paths, key=score)[0]
        fm, _ = split_doc(path.read_text(encoding="utf-8", errors="replace"))
        cards.append({
            "name": name,
            "category": fm_get(fm, "category") or path.parent.name,
            "family": fm_get(fm, "visual_family") or "Chart",
            "ft": fm_get(fm, "ft_family") or "magnitude",
            "ibcs": fm_get(fm, "ibcs_status") or "preferred",
            "complexity": fm_get(fm, "complexity") or "Basic",
            "audience": parse_list(fm_get(fm, "audience") or "[Executive, Analytics, Technical, Public]"),
            "function": fm_get(fm, "analytical_function") or "Comparison",
            "inputs": parse_list(fm_get(fm, "input_type") or "[]"),
            "cardinality": parse_list(fm_get(fm, "cardinality_fit") or "[]"),
            "rel": str(path.relative_to(ROOT / "library")).replace("\\", "/"),
            "stem": path.stem,
        })
    return cards


def main() -> None:
    for p in CHARTS.rglob("*.md"):
        enrich_file(p)
    have = existing_index()
    stems = {p.stem for p in CHARTS.rglob("*.md")}
    catalogue = catalogue_slugs()
    alias_rows = []
    added = 0
    for slug, source in sorted(catalogue.items()):
        if not slug or len(slug) < 3 or slug in SKIP:
            continue
        target = ALIASES.get(slug, slug)
        if target in stems or target in have or slug in stems or slug in have:
            if target != slug and (target in stems or target in have):
                alias_rows.append((slug, target))
            continue
        # fuzzy: if slug is a known stem
        if slug in GAP and slug not in stems:
            meta = GAP[slug]
            folder = CHARTS / meta["category"]
            folder.mkdir(parents=True, exist_ok=True)
            path = folder / f"{slug}.md"
            path.write_text(render_card(slug, meta, source if slug not in GAP else "gap-list"), encoding="utf-8")
            stems.add(slug)
            have[slug] = path
            added += 1
            continue
        if slug in stems or slug in have:
            continue
        meta = infer_meta(slug)
        # skip junk slugs from chart.guide sentences
        if slug.count("-") > 8 or len(slug) > 60:
            alias_rows.append((slug, "skipped-noise"))
            continue
        folder = CHARTS / meta["category"]
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / f"{slug}.md"
        if path.exists():
            stems.add(slug)
            continue
        path.write_text(render_card(slug, meta, source), encoding="utf-8")
        stems.add(slug)
        added += 1
    cards = collect_cards()
    # aliases for duplicate files
    seen = {}
    for c in cards:
        seen.setdefault(slugify(c["name"]), c["stem"])
    for a, b in ALIASES.items():
        if b in stems:
            alias_rows.append((a, b))
    write_indexes(cards, alias_rows)
    print(f"canonical={len(cards)} added={added} aliases={len(alias_rows)}")


if __name__ == "__main__":
    main()
