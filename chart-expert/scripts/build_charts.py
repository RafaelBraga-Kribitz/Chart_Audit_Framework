# -*- coding: utf-8 -*-
"""Enrich chart cards, add the curated catalogue types, and regenerate the chart indices.

    python chart-expert/scripts/build_charts.py            # write
    python chart-expert/scripts/build_charts.py --check    # exit 1 if anything would change

Paths resolve from this file, so the script runs from any checkout. The scraped
catalogue mirrors default to the repo-local
`Deterministic_Data_Visualization_Framework/references/` (override with `--ref`).

What the script owns:
- Missing derived keys on every card (ft_family, ibcs_status, questions,
  related_kpis, analysis_surface, communication_surface). Keys already present
  are never rewritten, so hand edits survive.
- New cards for GAP entries (original text, below) and for curated catalogue
  types. A catalogue page that is neither curated, aliased, nor skipped is
  reported as unclassified and does not become a card.
- Every file under `library/_INDICES/` except `priority-forms.md`, plus
  `references/chart-library-index.md`.

It never touches `implementations:` stanzas or Implementation Notes, so verified
statuses (see `references/verification-protocol.md`) survive a rebuild.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
LIB = ROOT / "library"
CHARTS = LIB / "CHARTS"
INDEX = LIB / "_INDICES"
LIBINDEX = ROOT / "references" / "chart-library-index.md"
DEFAULT_REF = REPO / "Deterministic_Data_Visualization_Framework" / "references"

TOOLS = ["matplotlib", "plotly", "altair", "d3", "tableau", "powerbi", "excel"]
AUDIENCES = ["Executive", "Analytics", "Technical", "Public"]

# Input-type tag -> inventory ids (references/input-type-inventory.md). The schema
# defines tags and the inventory defines IT ids; this is the crosswalk between them.
IT_FOR = {
    "xy-simple": ["IT001", "IT034"],
    "xy-dual-series": ["IT013"],
    "xyz-trivariate": ["IT012"],
    "cat-value": ["IT026", "IT005"],
    "cat-multi-value": ["IT029", "IT031"],
    "time-series": ["IT018"],
    "interval-range": ["IT040", "IT017"],
    "demo-grouped": ["IT011"],
    "composition": ["IT007", "IT016", "IT020", "IT023"],
    "hierarchical-cat": ["IT024", "IT037"],
    "matrix-grid": ["IT021", "IT028"],
    "event-time": ["IT009", "IT014", "IT036"],
}
# Analytical function -> Financial Times Visual Vocabulary family. Concept diagrams
# have no FT family.
FT_FOR = {
    "Comparison": "magnitude",
    "Correlation": "correlation",
    "Distribution": "distribution",
    "Part-to-whole": "part-to-whole",
    "Trend-over-time": "change-over-time",
    "Geographical": "spatial",
    "Flow": "flow",
    "Ranking": "ranking",
    "Deviation": "deviation",
    "Concept-viz": "none",
}
# Slug tokens, matched whole. Substring matching tagged "Langauge Menu" as a gauge.
AVOID_TOKENS = {"pie", "donut", "doughnut", "gauge", "radar", "spider", "3d", "speedometer", "traffic"}
CONDITIONAL_TOKENS = {
    "bubble", "dual", "combo", "tag", "word", "wordcloud", "horizon", "sankey", "chord", "alluvial",
    "stream", "streamgraph", "polar", "radial", "circular", "nightingale", "rose", "sunburst", "spiral", "proportional",
}
QUESTIONS = {
    "Comparison": "Which category is larger, and by how much?",
    "Correlation": "Do the two measures move together, and where do they not?",
    "Distribution": "What is the shape and the tail, not only the average?",
    "Part-to-whole": "How is the whole split, and which part matters?",
    "Trend-over-time": "How has the series changed over time?",
    "Geographical": "Where is the measure concentrated?",
    "Flow": "How does quantity move between states?",
    "Ranking": "What is the order of the entities, and what changed it?",
    "Deviation": "How far is the result from the reference, and in which direction?",
    "Concept-viz": "What structure or process does the diagram explain?",
}
SURFACE_QUESTION = "Who is the audience, and is this the analysis surface or the communication surface?"
ALTERNATIVES = {
    "Comparison": ["bar-chart", "dot-plot", "data-table"],
    "Correlation": ["scatter-plot", "connected-scatter-plot", "data-table"],
    "Distribution": ["histogram", "box-plot", "strip-plot"],
    "Part-to-whole": ["stacked-bar-chart", "waffle-chart", "data-table"],
    "Trend-over-time": ["line-chart", "sparkline", "area-chart"],
    "Geographical": ["choropleth-map", "bubble-map", "data-table"],
    "Flow": ["sankey-diagram", "flow-chart", "data-table"],
    "Ranking": ["horizontal-bar-chart", "bump-chart", "lollipop-chart"],
    "Deviation": ["diverging-bar", "bullet-graph", "waterfall-chart"],
    "Concept-viz": ["flow-chart", "data-table"],
}
DEFAULT_AUDIENCE = {
    "Basic": ["Executive", "Analytics", "Public"],
    "Intermediate": ["Analytics", "Technical"],
    "Advanced": ["Analytics", "Technical"],
}

# Twelve names exist as two or three hand-written cards in different family
# folders. The canonical copy is the one the original indices listed; the other
# copies stay on disk and are listed as non-canonical in aliases.md.
CANONICAL = {
    "bullet-graph": "Comparison",
    "bump-chart": "Temporal",
    "dumbbell-plot": "Comparison",
    "gantt-chart": "Specialized",
    "hive-plot": "Relationship",
    "lollipop-chart": "Comparison",
    "network-diagram": "Specialized",
    "parallel-coordinates": "Relationship",
    "pareto-chart": "Comparison",
    "radar-chart": "Specialized",
    "slope-chart": "Temporal",
    "waterfall-chart": "Comparison",
}

# Catalogue slug (or a common name) -> canonical card stem.
ALIASES = {
    # datavizproject.com
    "3d-scatterplot": "3d-scatter-plot",
    "angular-gauge-chart": "angular-gauge",
    "angular-index-gauge": "angular-gauge",
    "bar-chart-horizontal": "horizontal-bar-chart",
    "beeswarm-blot": "beeswarm-plot",
    "bubble-based-heat-map": "bubble-heatmap",
    "bubble-map-chart": "bubble-map",
    "bump-chart-2": "bump-chart",
    "choropleth-map-2": "choropleth-map",
    "circular-bubble-chart": "bubble-chart",
    "clustered-force-layout": "packed-circle-chart",
    "column-sparkline": "sparkline",
    "comparison-chart": "data-table",
    "convex-treemap": "voronoi-treemap",
    "curved-bar-chart": "circular-bar-chart",
    "fraction-of-pictograms": "icon-array",
    "icon-count": "pictogram",
    "layered-proportional-area-chart": "proportional-area-chart",
    "linear-process-diagram": "flow-chart",
    "map-bar-chart": "spike-map",
    "matrix-diagram-y-shaped": "matrix-diagram",
    "matrix-diagramroof-shaped": "matrix-diagram",
    "multilevel-pie-chart": "multi-level-donut-chart",
    "network-visualisation": "network-diagram",
    "non-ribbon-chord-diagram": "chord-diagram",
    "number": "big-number",
    "partition-layer-chart": "partition-chart",
    "percentage-grid": "waffle-chart",
    "pictorial-bar-chart": "pictogram",
    "pictorial-fraction-chart": "icon-array",
    "pictorial-stacked-chart": "pictogram",
    "pictorial-unit-chart": "pictogram",
    "polar-area-chart": "nightingale-rose",
    "polar-chart": "radar-chart",
    "population-pyramid-2": "population-pyramid",
    "process-diagram-circle": "cycle-diagram",
    "proportional-area-chart-circle": "proportional-area-chart",
    "proportional-area-chart-half-circle": "proportional-area-chart",
    "proportional-area-chart-icon": "proportional-area-chart",
    "pyramid-diagram": "pyramid-chart",
    "radar-diagram": "radar-chart",
    "radial-area-chart": "radar-chart",
    "radial-convergences": "chord-diagram",
    "radical-histogram": "radial-histogram",
    "radical-line-graph": "radial-line-graph",
    "scaled-timeline": "timeline",
    "scaled-up-number-with-icon": "big-number",
    "spiral-heat-map": "radial-heatmap",
    "stacked-ordered-area-chart": "stacked-area-chart",
    "swimlane-flow-chart": "swimlane-chart",
    "ternary-contour-plot": "ternary-plot",
    "three-dimensional-stream-graph": "stream-graph",
    "triangle-bar-chart": "bar-chart",
    "fan-chart-geneaology": "fan-chart-genealogy",
    "compound-bubble-and-pie-chart": "compound-bubble-pie-chart",
    # datavizcatalogue.com
    "area-graph": "area-chart",
    "brainstorm": "mind-map",
    "calendar": "calendar-heatmap",
    "choropleth": "choropleth-map",
    "dot-map": "dot-density-map",
    "dot-matrix-chart": "waffle-chart",
    "line-graph": "line-chart",
    "multiset-barchart": "grouped-bar-chart",
    "nightingale-rose-chart": "nightingale-rose",
    "point-and-figure-chart": "point-and-figure",
    "radial-column-chart": "circular-bar-chart",
    "stacked-area-graph": "stacked-area-chart",
    "stacked-bar-graph": "stacked-bar-chart",
    "stem-and-leaf-plot": "stem-and-leaf",
    "wordcloud": "tag-cloud",
    # data-to-viz.com
    "arc": "arc-diagram",
    "area": "area-chart",
    "barplot": "bar-chart",
    "boxplot": "box-plot",
    "bubble": "bubble-chart",
    "bubblemap": "bubble-map",
    "chord": "chord-diagram",
    "circularbarplot": "circular-bar-chart",
    "circularpacking": "circle-packing",
    "connectedscatter": "connected-scatter-plot",
    "correlogram": "correlation-matrix",
    "density": "density-plot",
    "density2d": "contour-plot",
    "donut": "donut-chart",
    "edge-bundling": "hierarchical-edge-bundling",
    "heatmap": "heat-map",
    "hexbinmap": "hex-cartogram",
    "line": "line-chart",
    "network": "network-diagram",
    "parallel": "parallel-coordinates",
    "pie": "pie-chart",
    "sankey": "sankey-diagram",
    "scatter": "scatter-plot",
    "stackedarea": "stacked-area-chart",
    "streamgraph": "stream-graph",
    "sunburst": "sunburst-diagram",
    "venn": "venn-diagram",
    "violin": "violin-plot",
    # chart.guide vocabulary and common spellings
    "100-bar-chart": "stacked-bar-100pct",
    "100-stacked-bar": "stacked-bar-100pct",
    "barchart": "bar-chart",
    "bullet-chart": "bullet-graph",
    "bulletgraph": "bullet-graph",
    "chloropeth-map": "choropleth-map",
    "column": "bar-chart",
    "column-chart": "bar-chart",
    "connected-scatterplot": "connected-scatter-plot",
    "contour-map": "isoline-map",
    "coxcomb": "nightingale-rose",
    "deviation-barchart": "diverging-bar",
    "deviation-column-chart": "diverging-bar",
    "deviation-line-chart": "surplus-deficit-filled-line",
    "diverging-bar-chart": "diverging-bar",
    "dot-chart": "dot-plot",
    "dot-line-chart": "line-chart",
    "doughnut-chart": "donut-chart",
    "dumbbell": "dumbbell-plot",
    "dumbbell-chart": "dumbbell-plot",
    "fan-chart": "fan-chart-time-series",
    "filled-surplus-deficit-line-chart": "surplus-deficit-filled-line",
    "floating-bar-chart": "column-range",
    "gannt-chart": "gantt-chart",
    "gantt": "gantt-chart",
    "grid-plot": "waffle-chart",
    "grouped-bar": "grouped-bar-chart",
    "hexbin-map": "hex-cartogram",
    "isopleth-map": "isoline-map",
    "isotype": "pictogram",
    "joy-plot": "ridgeline",
    "joyplot": "ridgeline",
    "league-tables": "data-table",
    "line-column-chart": "combo-chart",
    "lollipop": "lollipop-chart",
    "mekko": "marimekko-chart",
    "mosaic-plot": "marimekko-chart",
    "ordered-bar-chart": "bar-chart",
    "ordered-column-chart": "bar-chart",
    "organizational-chart": "organisational-chart",
    "packed-circle": "packed-circle-chart",
    "pictograph": "pictogram",
    "piechart": "pie-chart",
    "q-q-plot": "qq-plot",
    "radial-bar": "radial-bar-chart",
    "ridgeplot": "ridgeline",
    "rose-chart": "nightingale-rose",
    "scatterplot": "scatter-plot",
    "slopegraph": "slope-chart",
    "stacked-bar": "stacked-bar-chart",
    "stacked-column-chart": "stacked-bar-chart",
    "stacked-diverging-bar": "diverging-stacked-bar",
    "stock-price-chart": "candlestick-chart",
    "swot-analysis": "swot-diagram",
    "symbol-map": "bubble-map",
    "table-chart": "data-table",
    "vertical-bar": "bar-chart",
    "waterfall-plot": "waterfall-chart",
    "x-y-coordinate-plot": "scatter-plot",
    "xy-heatmap": "heat-map",
}

# Catalogue pages that are not chart types: illustrations, overlays, and a
# generic background map.
SKIP = {
    "development-causes", "exploded-view-drawing", "illustration-diagram", "illustration-explanation",
    "step-step-illustration", "trendline", "map",
}


def slugify(name: str) -> str:
    s = name.lower().strip().replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def yaml_scalar(value: str) -> str:
    return json.dumps(value, ensure_ascii=False) if re.search(r"[:#\[\]{},\"'&*!|>%@`]", value) else value


def yaml_list(items: list[str]) -> str:
    return "[" + ", ".join(yaml_scalar(i) for i in items) + "]"


def ibcs_for(slug: str, complexity: str) -> str:
    tokens = set(slug.split("-"))
    if tokens & AVOID_TOKENS:
        return "avoid"
    if tokens & CONDITIONAL_TOKENS or complexity == "Advanced":
        return "conditional"
    return "preferred"


def surfaces_for(ibcs: str, complexity: str) -> tuple[str, str]:
    """(analysis_surface, communication_surface). `none` means retell the finding with an alternative."""
    analysis = "notebook" if ibcs != "preferred" or complexity == "Advanced" else "plot"
    communication = "none" if ibcs == "avoid" or complexity == "Advanced" else "dashboard"
    return analysis, communication


def it_variants_for(inputs: list[str]) -> list[str]:
    out: list[str] = []
    for i in inputs:
        for it in IT_FOR.get(i, []):
            if it not in out:
                out.append(it)
    return out


def split_doc(text: str) -> tuple[str, str]:
    text = text.lstrip("﻿")
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
        return [p.strip().strip("'\"") for p in inner.split(",") if p.strip()] if inner else []
    return [raw] if raw else []


def card_paths() -> list[Path]:
    """Every chart card, sorted, ignoring dot files (macOS ._* forks, .DS_Store)."""
    return sorted(p for p in CHARTS.rglob("*.md") if not p.name.startswith("."))


def vault_type(function: str, slug: str) -> str:
    tokens = set(slug.split("-"))
    if "table" in tokens:
        return "Table"
    if "bubble" in tokens:
        return "Bubble"
    if "scatter" in tokens:
        return "Scatter"
    if "funnel" in tokens:
        return "Funnel"
    if tokens & {"heat", "heatmap"}:
        return "Heatmap"
    if "waterfall" in tokens:
        return "Waterfall"
    if "gauge" in tokens:
        return "Gauge"
    if "bullet" in tokens:
        return "Bullet"
    if tokens & {"spark", "sparkline"}:
        return "Sparkline"
    if "area" in tokens:
        return "Area"
    if "stacked" in tokens:
        return "Stacked bar"
    if tokens & {"donut", "doughnut", "pie"}:
        return "Donut"
    if "line" in tokens or function == "Trend-over-time":
        return "Line"
    if function in {"Comparison", "Ranking", "Deviation", "Part-to-whole"}:
        return "Bar"
    return "Number"


def surface_note(name: str, complexity: str, ibcs: str, alternatives: list[str]) -> str:
    alt = ", ".join(f"`{a}`" for a in alternatives[:3]) if alternatives else "a sorted bar or a table"
    if ibcs == "avoid" or complexity == "Advanced":
        return (
            f"{name} is a valid analysis chart for a data scientist, researcher, R&D, or development notebook "
            f"(matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. "
            f"Communication surface: retell the finding with {alt}. "
            f"`ibcs_status: {ibcs}` applies to that communication surface only."
        )
    return (
        f"{name} can sit on a dashboard, in a report, or in a notebook. "
        f"Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. "
        f"If the page is only a score, pair it with {alt}."
    )


# Marks that hold one number against its comparison: the dashboard score zone.
SCORE_MARKS = {"big-number", "bullet-graph", "thermometer", "progress-bar", "angular-gauge", "semi-circle-donut-chart"}


def dashboard_section(name: str, slug: str, function: str, complexity: str, ibcs: str, alternatives: list[str]) -> str:
    zone = "score" if slug in SCORE_MARKS else {
        "Comparison": "breakdown",
        "Trend-over-time": "trend",
        "Deviation": "variance",
        "Distribution": "breakdown",
        "Part-to-whole": "breakdown",
        "Ranking": "breakdown",
        "Flow": "breakdown",
        "Geographical": "breakdown",
        "Correlation": "breakdown",
        "Concept-viz": "detail",
    }.get(function, "breakdown")
    return f"""
## Dashboard and other surfaces

status: placeholder

{surface_note(name, complexity, ibcs, alternatives)}

Suggested communication placement: **{zone}** zone. Coarse template type, when a Databox or Zebra template is the layout: **{vault_type(function, slug)}**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.
"""


# Full cards for types the original 129 cards miss. Purpose text is original.
GAP: dict[str, dict] = {}


def g(slug, name, category, function, family, shape, inputs, card, complexity, channels, purpose, use, avoid, mistakes,
      ibcs=None, audience=None, source="gap-list"):
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
        "ibcs": ibcs or ibcs_for(slug, complexity),
        "audience": audience or DEFAULT_AUDIENCE[complexity],
        "source": source,
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
    g("letter-value-plot", "Letter-Value Plot", "Distribution", "Distribution", "Plot", ["Bar"], ["cat-value"], ["medium", "large"], "Advanced", ["position", "length"],
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
    g("small-multiples", "Small Multiples", "Specialized", "Comparison", "Chart", ["Line", "Bar"], ["cat-multi-value", "time-series"], ["medium"], "Intermediate", ["position"],
      "Small multiples repeat one simple chart per group on a shared scale, so the reader compares shapes across panels instead of decoding one crowded chart.",
      ["The same measure across regions, segments, or products", "Replacing a spaghetti of overlapping lines"],
      ["Panels that need different scales to be readable", "A single series"],
      ["Free y-scales that make small panels look as large as big ones", "Panel order that is alphabetical when the message is rank"],
      audience=["Executive", "Analytics", "Technical"])
    g("surplus-deficit-filled-line", "Surplus-Deficit Filled Line", "Temporal", "Deviation", "Chart", ["Line", "Area"], ["time-series"], ["medium", "large"], "Intermediate", ["position", "color-hue"],
      "A filled line shades the area between a series and its reference, one color above and another below, so surplus and deficit periods read at a glance.",
      ["Balance of trade, budget versus actual over time, temperature against a normal"],
      ["A reference that changes definition mid-series"],
      ["Color as the only sign of the direction", "A reference line that is not drawn"],
      audience=["Executive", "Analytics", "Public"], source="chart.guide")
    # Curated catalogue types. Purpose text is original; the catalogue only supplied the name.
    g("3d-bar-chart", "3D Bar Chart", "Comparison", "Comparison", "Chart", ["Bar"], ["cat-value"], ["small-N", "medium"], "Intermediate", ["position", "length"],
      "A 3D bar chart extrudes bars into perspective depth. The depth carries no data and the perspective distorts the heights the reader must compare.",
      ["Recognizing the form when auditing a legacy report"],
      ["Any comparison where the reader must read the heights"],
      ["Perspective that hides short bars behind tall ones", "Reading the front face instead of the top"],
      source="datavizproject")
    g("cluster-analysis", "Cluster Analysis Plot", "Relationship", "Correlation", "Plot", ["Dot"], ["xy-simple"], ["medium", "large"], "Advanced", ["position", "color-hue"],
      "A cluster plot draws observations in two dimensions (raw or reduced) and colors or hulls them by the cluster a model assigned.",
      ["Checking whether model clusters separate in a data science notebook"],
      ["Proving that the clusters are real", "An executive summary"],
      ["Treating separation in a 2D projection as separation in the full space"],
      source="datavizproject")
    g("compound-bubble-pie-chart", "Compound Bubble and Pie Chart", "Relationship", "Correlation", "Chart", ["Circle"], ["xyz-trivariate", "composition"], ["small-N"], "Advanced", ["position", "area", "angle"],
      "Each bubble is itself a pie, so position, area, and angle all carry data at once.",
      ["Recognizing the form when auditing a legacy report"],
      ["Any decision page", "Precise reading of any of the three encodings"],
      ["Comparing slice angles across bubbles of different size"],
      source="datavizproject")
    g("fan-chart-genealogy", "Fan Chart (Genealogy)", "Specialized", "Concept-viz", "Diagram", ["Line"], ["hierarchical-cat"], ["medium"], "Intermediate", ["position"],
      "A genealogy fan chart places ancestors on concentric half-rings, one generation per ring. It is not the forecast fan chart.",
      ["Family or lineage trees that double with each level"],
      ["Uncertainty bands around a forecast (use the time-series fan chart)"],
      ["Rings so thin the outer labels cannot be read"],
      source="datavizproject")
    g("proportional-area-chart", "Proportional Area Chart", "Comparison", "Comparison", "Chart", ["Square", "Circle"], ["cat-value"], ["small-N"], "Basic", ["area"],
      "A proportional area chart sizes one square, circle, or icon per value. Area, not side length, must carry the value.",
      ["A few magnitudes that differ by an order of magnitude", "A public piece where scale contrast is the message"],
      ["Close values the reader must rank"],
      ["Scaling the radius or side instead of the area", "No value labels"],
      audience=["Executive", "Public"], source="datavizproject")
    g("radial-bar-chart", "Radial Bar Chart", "Comparison", "Comparison", "Chart", ["Bar"], ["cat-value"], ["small-N"], "Intermediate", ["angle", "length"],
      "A radial bar chart bends each bar into a concentric arc. Outer arcs look longer than inner arcs with the same value.",
      ["A decorative summary of a handful of categories"],
      ["Precise comparison", "More than a handful of categories"],
      ["Sorting so the largest value sits on the inner ring"],
      source="datavizcatalogue")
    g("radial-histogram", "Radial Histogram", "Distribution", "Distribution", "Chart", ["Bar"], ["xy-simple"], ["medium", "large"], "Advanced", ["length", "angle"],
      "A radial histogram bins a cyclic variable (hour of day, compass direction, month) around a circle so the wrap-around is visible.",
      ["Wind direction, time-of-day activity, seasonal counts in a notebook"],
      ["A variable that is not cyclic"],
      ["Bar area that grows with radius and overstates the outer bins"],
      source="datavizproject")
    g("radial-line-graph", "Radial Line Graph", "Temporal", "Trend-over-time", "Chart", ["Line"], ["time-series"], ["medium"], "Advanced", ["position", "angle"],
      "A radial line graph wraps a series around a circle, one turn per cycle, so seasons line up across years.",
      ["Seasonality across several years in an analysis notebook"],
      ["A trend that is not cyclic", "An executive page"],
      ["Reading distance from the center as a linear scale"],
      source="datavizproject")
    g("spiral-plot", "Spiral Plot", "Temporal", "Trend-over-time", "Chart", ["Line"], ["time-series"], ["large"], "Advanced", ["position", "color-value"],
      "A spiral plot lays a long series along an Archimedean spiral so periodic patterns line up on the same angle.",
      ["Long daily series with a weekly or yearly cycle"],
      ["Short series", "Reading exact values"],
      ["A period that does not match the real cycle"],
      source="datavizcatalogue")
    g("tally-chart", "Tally Chart", "Distribution", "Distribution", "Glyph", ["Line"], ["cat-value"], ["small-N"], "Basic", ["position"],
      "A tally chart counts occurrences with grouped strokes, one stroke per observation.",
      ["Field counts and classroom data collection"],
      ["Large counts", "A finished report"],
      ["Groups of five drawn inconsistently"],
      audience=["Public", "Analytics"], source="datavizproject")
    g("target-diagram", "Target Diagram", "Specialized", "Concept-viz", "Diagram", ["Circle"], ["hierarchical-cat"], ["small-N"], "Basic", ["position"],
      "A target diagram places items on concentric rings by closeness to a goal or by priority. The rings are categories, not a scale.",
      ["Prioritization workshops", "Stakeholder closeness"],
      ["Measured distances"],
      ["Rings read as equal-interval values"],
      audience=["Executive", "Public"], source="datavizproject")
    g("taylor-diagram", "Taylor Diagram", "Relationship", "Correlation", "Plot", ["Dot"], ["xyz-trivariate"], ["small-N", "medium"], "Advanced", ["position", "angle"],
      "A Taylor diagram places each model by its correlation with observations (angle) and its standard deviation (radius), so centered RMS error is the distance to the reference point.",
      ["Comparing several models against one observed series"],
      ["A business audience"],
      ["Comparing models scored on different reference data"],
      source="datavizproject")
    g("timetable", "Timetable", "Specialized", "Trend-over-time", "Table", ["Square"], ["event-time"], ["medium"], "Basic", ["position"],
      "A timetable lists events against times in a grid so a reader can look up when something happens.",
      ["Schedules, rotas, transport departures"],
      ["Showing a trend"],
      ["Mixed time zones with no note"],
      audience=["Executive", "Analytics", "Public"], source="datavizcatalogue")
    g("tree-diagram", "Tree Diagram", "Specialized", "Concept-viz", "Diagram", ["Line"], ["hierarchical-cat"], ["small-N", "medium"], "Basic", ["position"],
      "A tree diagram draws a hierarchy as nodes joined by parent-child links.",
      ["Taxonomies, reporting lines, decomposition of a measure"],
      ["Magnitudes (use a treemap or icicle)"],
      ["Depth so large the leaves cannot be labeled"],
      source="datavizcatalogue")


# Communication charts that executives and the public read, whatever their complexity.
AUDIENCE_OVERRIDES = {
    "arrow-plot": ["Executive", "Analytics", "Public"],
    "big-number": ["Executive", "Analytics", "Public"],
    "burndown-chart": ["Executive", "Analytics"],
    "burnup-chart": ["Executive", "Analytics"],
    "calendar-heatmap": ["Executive", "Analytics", "Public"],
    "combo-chart": ["Analytics", "Executive"],
    "data-table": AUDIENCES,
    "diverging-bar": ["Executive", "Analytics", "Public"],
    "diverging-stacked-bar": ["Executive", "Analytics", "Public"],
    "dorling-cartogram": ["Analytics", "Public"],
    "dupont-tree": ["Executive", "Analytics"],
    "hex-cartogram": ["Analytics", "Public"],
    "ibcs-variance-table": ["Executive", "Analytics"],
    "icon-array": ["Public", "Executive"],
    "journey-map": ["Executive", "Analytics"],
    "kpi-tree": ["Executive", "Analytics"],
    "pictogram": ["Public", "Executive"],
    "progress-bar": ["Executive", "Public"],
    "run-chart": ["Executive", "Analytics"],
    "service-blueprint": ["Executive", "Analytics"],
    "sipoc": ["Executive", "Analytics"],
    "spine-chart": ["Executive", "Analytics"],
    "strategy-map": ["Executive"],
    "thermometer": ["Executive", "Public"],
    "value-stream-map": ["Executive", "Analytics"],
    "win-loss-sparkline": ["Executive", "Analytics"],
}


load_gap()
for _slug, _aud in AUDIENCE_OVERRIDES.items():
    GAP[_slug]["audience"] = _aud


def catalogue_slugs(ref: Path) -> dict[str, str]:
    """Chart-type pages in the scraped catalogues: slug -> source. Only method directories are read."""
    found: dict[str, str] = {}
    dt = ref / "datavizproject.com" / "data-type"
    if dt.is_dir():
        for p in sorted(dt.iterdir()):
            if p.is_dir() and not p.name.startswith("."):
                found.setdefault(slugify(p.name), "datavizproject")
    for base, source in (
        (ref / "datavizcatalogue.com" / "methods", "datavizcatalogue"),
        (ref / "www.data-to-viz.com" / "graph", "data-to-viz"),
    ):
        if base.is_dir():
            for p in sorted(base.glob("*.html")):
                if not p.name.startswith("."):
                    found.setdefault(slugify(p.stem), source)
    return found


def render_card(slug: str, meta: dict) -> str:
    ibcs = meta["ibcs"]
    alts = [a for a in ALTERNATIVES.get(meta["function"], []) if a != slug]
    analysis, communication = surfaces_for(ibcs, meta["complexity"])
    stanzas = "\n".join(f"  {t}: {{status: stub, source_file: null, last_iterated: null}}" for t in TOOLS)
    questions = [QUESTIONS.get(meta["function"], "What does the chart show?"), SURFACE_QUESTION]
    fm = f"""---
name: {yaml_scalar(meta['name'])}
category: {meta['category']}
input_type: {yaml_list(meta['inputs'])}
it_variants: {yaml_list(it_variants_for(meta['inputs']))}
analytical_function: {meta['function']}
visual_family: {meta['family']}
shape_primitive: {yaml_list(meta['shape'])}
cardinality_fit: {yaml_list(meta['cardinality'])}
audience: {yaml_list(meta['audience'])}
complexity: {meta['complexity']}
encoding_channels: {yaml_list(meta['channels'])}
tool_support: {yaml_list(TOOLS)}
failure_modes: []
alternatives: {yaml_list(alts)}
source: [{meta['source']}]
implementations:
{stanzas}
ft_family: {FT_FOR[meta['function']]}
ibcs_status: {ibcs}
questions: {json.dumps(questions, ensure_ascii=False)}
related_kpis: []
analysis_surface: {analysis}
communication_surface: {communication}
---
"""
    bullets = lambda items: "\n".join(f"- {u}" for u in items)  # noqa: E731
    body = f"""
# {meta['name']}

## Description
{meta['purpose']}

## When to Use
{bullets(meta['use'])}

## When NOT to Use
{bullets(meta['avoid'])}

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| as input type | {", ".join(meta['inputs'])} | See `references/input-type-schema.md` |

## Best Practices
- Match the chart to the audience and the surface. A notebook may keep this encoding. An executive page may need a simpler alternative.
- State the comparison (target, prior, peer, or distribution) in the title when the chart is used to communicate.
- Prefer position and length over area and angle when the reader must compare values precisely.

## Common Mistakes
{bullets(meta['mistakes'])}
{dashboard_section(meta['name'], slug, meta['function'], meta['complexity'], ibcs, alts)}
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


def enrich_text(text: str, slug: str) -> str:
    """Add the derived keys a card is missing. Present keys are left alone."""
    fm, body = split_doc(text)
    if not fm:
        return text
    name = fm_get(fm, "name").strip("\"'") or slug
    function = fm_get(fm, "analytical_function") or "Comparison"
    complexity = fm_get(fm, "complexity") or "Basic"
    inputs = parse_list(fm_get(fm, "input_type") or "[]")
    alts = [a for a in parse_list(fm_get(fm, "alternatives") or "[]") if re.fullmatch(r"[a-z0-9-]+", a)]
    ibcs = fm_get(fm, "ibcs_status") or ibcs_for(slug, complexity)
    analysis, communication = surfaces_for(ibcs, complexity)
    additions = []
    if not fm_has(fm, "ft_family"):
        additions.append(f"ft_family: {FT_FOR.get(function, 'magnitude')}")
    if not fm_has(fm, "ibcs_status"):
        additions.append(f"ibcs_status: {ibcs}")
    if not fm_has(fm, "questions"):
        additions.append("questions: " + json.dumps([QUESTIONS.get(function, "What does the chart show?"), SURFACE_QUESTION]))
    if not fm_has(fm, "related_kpis"):
        additions.append("related_kpis: []")
    if not fm_has(fm, "analysis_surface"):
        additions.append(f"analysis_surface: {analysis}")
    if not fm_has(fm, "communication_surface"):
        additions.append(f"communication_surface: {communication}")
    if fm_get(fm, "it_variants") in {"", "[]"}:
        its = it_variants_for(inputs)
        if its:
            fm = re.sub(r"(?m)^it_variants:.*$", "it_variants: " + yaml_list(its), fm, count=1)
    if additions:
        fm = fm.rstrip() + "\n" + "\n".join(additions)
    if "## Dashboard" not in body:
        block = dashboard_section(name, slug, function, complexity, ibcs, alts or ALTERNATIVES.get(function, []))
        if "## Implementation Notes" in body:
            body = body.replace("## Implementation Notes", block.lstrip("\n") + "\n## Implementation Notes", 1)
        else:
            body = body.rstrip() + "\n" + block
    return "---\n" + fm.strip() + "\n---" + body


def card_meta(path: Path) -> dict:
    fm, _ = split_doc(path.read_text(encoding="utf-8"))
    name = fm_get(fm, "name").strip("\"'")
    if not name:
        raise SystemExit(f"{path}: chart card has no frontmatter name")
    stanzas = {}
    for tool in TOOLS:
        m = re.search(rf"(?m)^\s+{tool}:\s*\{{status:\s*(\w+)", fm)
        stanzas[tool] = m.group(1) if m else "stub"
    return {
        "name": name,
        "stem": path.stem,
        "category": fm_get(fm, "category") or path.parent.name,
        "family": fm_get(fm, "visual_family"),
        "ft": fm_get(fm, "ft_family"),
        "ibcs": fm_get(fm, "ibcs_status"),
        "complexity": fm_get(fm, "complexity"),
        "audience": parse_list(fm_get(fm, "audience")),
        "function": fm_get(fm, "analytical_function"),
        "inputs": parse_list(fm_get(fm, "input_type")),
        "cardinality": parse_list(fm_get(fm, "cardinality_fit")),
        "tools": parse_list(fm_get(fm, "tool_support")),
        "stanzas": stanzas,
        "rel": path.relative_to(LIB).as_posix(),
    }


def collect_cards() -> tuple[list[dict], list[tuple[str, str]]]:
    """One canonical card per stem, plus (non-canonical path, canonical path) pairs."""
    by_stem: dict[str, list[Path]] = {}
    for p in card_paths():
        by_stem.setdefault(p.stem, []).append(p)
    cards, extra = [], []
    for stem, paths in sorted(by_stem.items()):
        if len(paths) > 1:
            folder = CANONICAL.get(stem)
            chosen = [p for p in paths if p.parent.name == folder]
            if not chosen:
                raise SystemExit(f"{stem}: {len(paths)} cards and no CANONICAL folder entry")
            canon = chosen[0]
            extra += [(p.relative_to(LIB).as_posix(), canon.relative_to(LIB).as_posix()) for p in paths if p != canon]
        else:
            canon = paths[0]
        cards.append(card_meta(canon))
    return cards, extra


GROUP_NOTES = {
    "function": {
        "Comparison": "Comparing magnitudes across categories or entities.",
        "Correlation": "Relationship between two or more variables.",
        "Distribution": "Spread, shape, and tails of a variable.",
        "Part-to-whole": "Components as fractions of a total.",
        "Trend-over-time": "Change over time.",
        "Geographical": "Spatial or location-based patterns.",
        "Flow": "Movement between states or nodes.",
        "Ranking": "Ordered magnitude with identity.",
        "Deviation": "Departure from a reference or baseline.",
        "Concept-viz": "A concept, structure, or process rather than measured data.",
    },
    "input": {
        "xy-simple": "[numeric, numeric]. Two numeric columns, no explicit time.",
        "xy-dual-series": "[num or cat, num, num]. One x with two series.",
        "xyz-trivariate": "[numeric, numeric, numeric]. Three numeric columns.",
        "cat-value": "[categorical, numeric]. One value per category.",
        "cat-multi-value": "[categorical, num, num, ...]. Several values per category.",
        "time-series": "[datetime, num, ...]. Ordered by time.",
        "interval-range": "[cat, num, num] to [cat, num x4]. Ranges, intervals, OHLC.",
        "demo-grouped": "[cat, cat, num, ...]. Two grouping levels.",
        "composition": "[cat, num, ...] where rows sum to a whole.",
        "hierarchical-cat": "[num or ordered, cat, cat, ...]. Nested categories.",
        "matrix-grid": "Row category x column category -> value.",
        "event-time": "[categorical, datetime]. Events on a timeline.",
    },
    "cardinality": {
        "small-N": "Fewer than 10 items or categories.",
        "medium": "10 to 50 items.",
        "large": "50 to 500 items.",
        "very-large": "More than 500 items.",
    },
    "audience": {
        "Executive": "Needs the message in seconds; basic marks, message title, comparison stated.",
        "Analytics": "Business analyst; comfortable with intermediate charts and filters.",
        "Technical": "Engineer or scientist; reads diagnostic and model plots.",
        "Public": "General audience; accessible design, minimal jargon.",
    },
    "complexity": {
        "Basic": "Readable without a legend lesson.",
        "Intermediate": "Needs one sentence of explanation.",
        "Advanced": "Needs training or a notebook context.",
    },
    "ibcs": {
        "preferred": "Usable on executive, client, and public communication surfaces.",
        "conditional": "Communication use needs a stated reason; analysis surfaces are fine.",
        "avoid": "Not the message mark on executive, public, or client communication surfaces. Analysis surfaces keep it.",
    },
}
ORDER = {
    "cardinality": ["small-N", "medium", "large", "very-large"],
    "audience": AUDIENCES,
    "complexity": ["Basic", "Intermediate", "Advanced"],
    "ibcs": ["preferred", "conditional", "avoid"],
}


def dump(title: str, intro: str, groups: dict[str, list[dict]], dimension: str = "") -> str:
    keys = [k for k in ORDER.get(dimension, []) if k in groups] + sorted(k for k in groups if k not in ORDER.get(dimension, []))
    lines = [f"# Index: {title}", "", intro, "", "---", ""]
    for k in keys:
        lines.append(f"## {k}")
        note = GROUP_NOTES.get(dimension, {}).get(k)
        if note:
            lines.append(note)
        lines += [f"- {c['name']} → `{c['rel']}`" for c in sorted(groups[k], key=lambda c: (c["name"].lower(), c["rel"]))]
        lines.append("")
    return "\n".join(lines)


GENERATED = "Generated by `chart-expert/scripts/build_charts.py` from card frontmatter. Do not edit by hand."


def render_indexes(cards: list[dict], alias_rows: list[tuple[str, str]], extra: list[tuple[str, str]]) -> dict[Path, str]:
    def group(key, multi=False):
        out: dict[str, list[dict]] = {}
        for c in cards:
            for v in (c[key] if multi else [c[key]]):
                out.setdefault(v, []).append(c)
        return out

    out = {
        INDEX / "by-function.md": dump("Charts by Analytical Function", GENERATED, group("function"), "function"),
        INDEX / "by-input-type.md": dump("Charts by Data Input Type", GENERATED, group("inputs", True), "input"),
        INDEX / "by-cardinality.md": dump("Charts by Cardinality Fit", GENERATED + " Use it to filter out charts that break at the dataset's N.", group("cardinality", True), "cardinality"),
        INDEX / "by-visual-family.md": dump("Charts by Visual Family", GENERATED, group("family")),
        INDEX / "by-ft-family.md": dump("Charts by FT Visual Vocabulary Family", GENERATED, group("ft")),
        INDEX / "by-ibcs.md": dump("Charts by IBCS Status", GENERATED + " Scope of each status: `library/STANDARDS/ibcs-success.md`.", group("ibcs"), "ibcs"),
        INDEX / "by-audience.md": dump("Charts by Audience Tolerance", GENERATED, group("audience", True), "audience"),
        INDEX / "by-complexity.md": dump("Charts by Complexity", GENERATED, group("complexity"), "complexity"),
    }
    tool_lines = ["# Index: Charts by Tool", "", GENERATED + " `verified` marks an implementation that passed `references/verification-protocol.md`.", "", "---", ""]
    for tool in TOOLS:
        listed = sorted((c for c in cards if tool in c["tools"]), key=lambda c: (c["name"].lower(), c["rel"]))
        tool_lines.append(f"## {tool}")
        tool_lines += [f"- {c['name']} → `{c['rel']}`" + (" (verified)" if c["stanzas"][tool] == "verified" else "") for c in listed]
        tool_lines.append("")
    out[INDEX / "by-tool.md"] = "\n".join(tool_lines)
    ver = [
        "# Verification index", "",
        f"Verified implementations per tool across the {len(cards)} canonical chart cards.",
        "Generated by `chart-expert/scripts/build_charts.py` from each card's `implementations:` stanza; a status flip",
        "(`references/verification-protocol.md` step 4) is followed by a rebuild in the same change (step 5).", "",
        f"| Tool | Verified / {len(cards)} |", "|---|---|",
    ]
    ver += [f"| {tool} | {sum(1 for c in cards if c['stanzas'][tool] == 'verified')} |" for tool in TOOLS]
    out[INDEX / "verification-index.md"] = "\n".join(ver) + "\n"
    alias_lines = ["# Chart aliases", "", "Catalogue names and common spellings that point at one canonical card. " + GENERATED, ""]
    alias_lines += [f"- `{a}` → `{b}`" for a, b in sorted(set(alias_rows))]
    if extra:
        alias_lines += ["", "## Non-canonical copies", "",
                        "These names exist as more than one hand-written card. Retrieval uses the canonical file; merge the others into it.", ""]
        alias_lines += [f"- `{a}` → `{b}`" for a, b in sorted(extra)]
    out[INDEX / "aliases.md"] = "\n".join(alias_lines) + "\n"
    counts: dict[str, int] = {}
    for c in cards:
        counts[c["category"]] = counts.get(c["category"], 0) + 1
    lines = ["# Chart Library Index", "", f"Total: {len(cards)} canonical charts. " + GENERATED, "", "## Chart Count by Category", ""]
    lines += [f"- {k}: {counts[k]}" for k in sorted(counts)]
    lines += ["", "| Chart Name | Category | Visual Family | FT Family | IBCS | Complexity | Audience | File | Function | Input Types |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    for c in sorted(cards, key=lambda x: (x["category"], x["name"].lower(), x["rel"])):
        lines.append(f"| {c['name']} | {c['category']} | {c['family']} | {c['ft']} | {c['ibcs']} | {c['complexity']} | "
                     f"{', '.join(c['audience'])} | `{c['rel']}` | {c['function']} | {', '.join(c['inputs'])} |")
    lines += ["", "## Aliases", "", "See `library/_INDICES/aliases.md`.", ""]
    out[LIBINDEX] = "\n".join(lines)
    return {p: t if t.endswith("\n") else t + "\n" for p, t in out.items()}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--ref", type=Path, default=DEFAULT_REF, help="scraped catalogue mirrors (default: repo-local references/)")
    ap.add_argument("--check", action="store_true", help="write nothing; exit 1 if any file would change")
    args = ap.parse_args()

    for target in set(ALIASES.values()):
        if target not in GAP and not any(p.stem == target for p in card_paths()):
            raise SystemExit(f"alias target {target!r} has no card and no GAP entry")

    pending: dict[Path, str] = {}
    stems = {p.stem for p in card_paths()}
    for slug, meta in sorted(GAP.items()):
        if slug not in stems:
            pending[CHARTS / meta["category"] / f"{slug}.md"] = enrich_text(render_card(slug, meta), slug)
            stems.add(slug)
    for p in card_paths():
        new = enrich_text(p.read_text(encoding="utf-8"), p.stem)
        if new != p.read_text(encoding="utf-8"):
            pending[p] = new

    alias_rows = [(a, b) for a, b in ALIASES.items() if a != b]
    unclassified = []
    for slug in catalogue_slugs(args.ref):
        if slug in stems or slug in SKIP or slug in ALIASES:
            continue
        unclassified.append(slug)

    if args.check:
        changed = [p for p, t in pending.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
    else:
        for p, t in pending.items():
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(t, encoding="utf-8", newline="\n")
        changed = list(pending)

    cards, extra = collect_cards() if not args.check or not pending else (None, None)
    if cards is not None:
        for p, t in render_indexes(cards, alias_rows, extra).items():
            if p.exists() and p.read_text(encoding="utf-8") == t:
                continue
            changed.append(p)
            if not args.check:
                p.write_text(t, encoding="utf-8", newline="\n")

    for slug in unclassified:
        print(f"unclassified catalogue type: {slug} (add it to GAP, ALIASES, or SKIP)", file=sys.stderr)
    for p in sorted(set(changed)):
        print(("would change: " if args.check else "wrote: ") + p.relative_to(REPO).as_posix())
    print(f"cards={len(cards) if cards is not None else '?'} changed={len(set(changed))} unclassified={len(unclassified)}")
    return 1 if args.check and (changed or unclassified) else 0


if __name__ == "__main__":
    sys.exit(main())
