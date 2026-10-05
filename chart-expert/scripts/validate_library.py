# -*- coding: utf-8 -*-
"""Structural checks for the chart-expert library.

    python chart-expert/scripts/validate_library.py

Exit 0 and print PASS when every check holds; otherwise print each failure and exit 1.
Generated files are checked for freshness separately, by running each generator with
--check (build_charts.py, build_measures.py, write_foundations.py); CI runs all four.
Requires PyYAML.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]  # chart-expert/
REPO = ROOT.parent
LIB = ROOT / "library"
CHARTS = LIB / "CHARTS"

TOOLS = ["matplotlib", "plotly", "altair", "d3", "tableau", "powerbi", "excel"]
VOCAB = {
    "category": {"Comparison", "Composition", "Distribution", "Geospatial", "Relationship", "Specialized", "Temporal"},
    "analytical_function": {"Comparison", "Correlation", "Distribution", "Part-to-whole", "Trend-over-time", "Geographical",
                            "Flow", "Ranking", "Deviation", "Concept-viz"},
    "visual_family": {"Chart", "Diagram", "Plot", "Map", "Table", "Glyph"},
    "shape_primitive": {"Area", "Bar", "Circle", "Dot", "Icon", "Line", "Polygon", "Pyramid", "Square"},
    "input_type": {"xy-simple", "xy-dual-series", "xyz-trivariate", "cat-value", "cat-multi-value", "time-series",
                   "interval-range", "demo-grouped", "composition", "hierarchical-cat", "matrix-grid", "event-time"},
    "cardinality_fit": {"small-N", "medium", "large", "very-large"},
    "audience": {"Executive", "Analytics", "Technical", "Public"},
    "complexity": {"Basic", "Intermediate", "Advanced"},
    "encoding_channels": {"position", "length", "angle", "area", "color-hue", "color-value", "shape", "texture", "motion"},
    "tool_support": set(TOOLS) | {"r-ggplot2"},
    "source": {"datavizproject", "datavizcatalogue", "data-to-viz", "depictdatastudio", "chartmaker", "chart.guide", "gap-list"},
    "ft_family": {"magnitude", "correlation", "distribution", "part-to-whole", "change-over-time", "spatial", "flow",
                  "ranking", "deviation", "none"},
    "ibcs_status": {"preferred", "conditional", "avoid"},
    "analysis_surface": {"plot", "notebook"},
    "communication_surface": {"dashboard", "none"},
}
CARD_KEYS = list(VOCAB) + ["name", "it_variants", "failure_modes", "alternatives", "implementations", "questions", "related_kpis"]
KPI_KEYS = ["id", "name", "measure_kind", "function", "area", "unit", "definition", "formula", "formula_inputs", "input_names",
            "direction", "leading_lagging", "level", "audience_roles", "questions", "related_charts", "analysis_chart",
            "communication_chart", "dashboard", "provenance"]
KPI_VOCAB = {
    "measure_kind": {"kpi", "kri"},
    "unit": {"currency", "percent", "count", "number", "days", "hours", "months"},
    "direction": {"up", "down", "corridor"},
    "leading_lagging": {"leading", "lagging"},
    "level": {"strategic", "tactical", "operational"},
    "provenance": {"authored"},
}
ROLES = {"Executive", "Client", "HR business partner", "Marketing lead", "Marketing analytics", "Data analytics",
         "Data scientist", "Researcher", "R&D", "Development", "Public"}
LOCAL_PATH = re.compile(r"[A-Za-z]:[\\/]+Users[\\/]|/Users/[A-Za-z]|/home/[a-z]")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def __call__(self, msg: str) -> None:
        self.errors.append(msg)


def frontmatter(path: Path, err: Report) -> dict | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        err(f"{rel(path)}: no frontmatter")
        return None
    end = text.find("\n---", 4)
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        err(f"{rel(path)}: frontmatter is not valid YAML ({str(exc).splitlines()[0]})")
        return None
    return data if isinstance(data, dict) else None


def rel(path: Path) -> str:
    return path.relative_to(REPO).as_posix()


def as_list(value) -> list:
    return value if isinstance(value, list) else [] if value is None else [value]


def check_cards(err: Report) -> tuple[set[str], dict[str, Path]]:
    stems: dict[str, list[Path]] = {}
    for path in sorted(CHARTS.rglob("*")):
        if path.name.startswith("."):
            err(f"{rel(path)}: dot file inside the chart library")
            continue
        if path.suffix != ".md":
            continue
        stems.setdefault(path.stem, []).append(path)
        fm = frontmatter(path, err)
        if fm is None:
            continue
        for key in CARD_KEYS:
            if key not in fm:
                err(f"{rel(path)}: missing key {key}")
        if fm.get("category") != path.parent.name:
            err(f"{rel(path)}: category {fm.get('category')!r} but folder {path.parent.name!r}")
        for key, allowed in VOCAB.items():
            for value in as_list(fm.get(key)):
                if value not in allowed:
                    err(f"{rel(path)}: {key} value {value!r} not in retrieval-dimensions vocabulary")
        impl = fm.get("implementations") or {}
        for tool in TOOLS:
            stanza = impl.get(tool)
            if not isinstance(stanza, dict) or stanza.get("status") not in {"stub", "verified"}:
                err(f"{rel(path)}: implementations.{tool} missing or with an unknown status")
            elif stanza["status"] == "verified" and not (REPO / str(stanza.get("source_file") or "")).is_file():
                err(f"{rel(path)}: implementations.{tool} is verified but source_file {stanza.get('source_file')!r} does not exist")
        if fm.get("complexity") == "Advanced" and "Executive" in as_list(fm.get("audience")):
            err(f"{rel(path)}: Advanced chart tagged for an Executive audience")
    aliases = (LIB / "_INDICES" / "aliases.md").read_text(encoding="utf-8")
    canonical: dict[str, Path] = {}
    for stem, paths in stems.items():
        if len(paths) == 1:
            canonical[stem] = paths[0]
            continue
        listed = [p for p in paths if f"`{p.relative_to(LIB).as_posix()}` →" not in aliases]
        if len(listed) != 1:
            err(f"{stem}: {len(paths)} cards but {len(listed)} canonical (non-canonical copies must be listed in aliases.md)")
        canonical[stem] = listed[0] if listed else paths[0]
    return set(stems), canonical


def check_indices(canonical: dict[str, Path], err: Report) -> None:
    for path in sorted((LIB / "_INDICES").glob("*.md")) + [ROOT / "references" / "chart-library-index.md"]:
        for target in re.findall(r"`(CHARTS/[^`]+\.md)`", path.read_text(encoding="utf-8")):
            if not (LIB / target).is_file():
                err(f"{rel(path)}: points at missing {target}")
    index = (ROOT / "references" / "chart-library-index.md").read_text(encoding="utf-8")
    rows = Counter(re.findall(r"\| `(CHARTS/[^`]+\.md)` \|", index))
    for stem, path in canonical.items():
        n = rows.get(path.relative_to(LIB).as_posix(), 0)
        if n != 1:
            err(f"chart-library-index.md: {stem} listed {n} times")
    m = re.search(r"Total: (\d+) canonical charts", index)
    if not m or int(m.group(1)) != len(canonical):
        err(f"chart-library-index.md: total {m.group(1) if m else '?'} != {len(canonical)} canonical cards")


def load_jsonl(path: Path, err: Report) -> list[dict]:
    if not path.is_file():
        err(f"missing {rel(path)}")
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def check_measures(stems: set[str], err: Report) -> set[str]:
    kpis = load_jsonl(LIB / "KPIS" / "_catalog" / "kpis.jsonl", err)
    metrics = load_jsonl(LIB / "KPIS" / "_catalog" / "metrics.jsonl", err)
    for kid, n in Counter(k.get("id") for k in kpis).items():
        if n > 1:
            err(f"kpis.jsonl: id {kid} appears {n} times")
    for mid, n in Counter(m.get("id") for m in metrics).items():
        if n > 1:
            err(f"metrics.jsonl: id {mid} appears {n} times")
    ids = {k["id"] for k in kpis if "id" in k}
    metric_ids = {m["id"]: m for m in metrics}
    dashboards = {}
    for path in (LIB / "DASHBOARDS").rglob("*.md"):
        if path.parent.name != "patterns" and path.name != "index.md":
            fm = frontmatter(path, err) or {}
            dashboards[fm.get("id")] = path
    for k in kpis:
        kid = k.get("id", "?")
        for key in KPI_KEYS:
            if key not in k or k[key] in ("", None, []):
                err(f"{kid}: missing {key}")
        for key, allowed in KPI_VOCAB.items():
            if k.get(key) not in allowed:
                err(f"{kid}: {key} {k.get(key)!r} not in {sorted(allowed)}")
        for role in k.get("audience_roles", []):
            if role not in ROLES:
                err(f"{kid}: audience role {role!r} not in ONTOLOGY roles")
        inputs = k.get("formula_inputs", [])
        letters = set(re.findall(r"\b[A-G]\b", k.get("formula", "")))
        if letters != set("ABCDEFG"[: len(inputs)]):
            err(f"{kid}: formula {k.get('formula')!r} does not use its {len(inputs)} inputs")
        if k.get("unit") in {"percent", "number"} and len(inputs) == 1 and \
                metric_ids.get(inputs[0], {}).get("name", "").lower() == k.get("name", "").lower():
            err(f"{kid}: a rate or ratio whose only formula input is the KPI itself")
        for mid in inputs:
            if mid not in metric_ids:
                err(f"{kid}: input {mid} not in metrics.jsonl")
            elif kid not in metric_ids[mid].get("used_by", []):
                err(f"{mid}: used_by does not list {kid}")
        for chart in set(k.get("related_charts", [])) | {k.get("analysis_chart"), k.get("communication_chart")}:
            if chart not in stems:
                err(f"{kid}: chart {chart!r} has no card")
        if k.get("dashboard") not in dashboards:
            err(f"{kid}: dashboard {k.get('dashboard')!r} has no specification under library/DASHBOARDS/")
    for path in sorted((LIB / "OKRS").rglob("*.md")) + sorted((LIB / "DASHBOARDS").rglob("*.md")) + sorted((LIB / "KRIS").rglob("*.md")):
        for kid in re.findall(r"`(kpi\.[a-z0-9.-]+)`", path.read_text(encoding="utf-8")):
            if kid not in ids:
                err(f"{rel(path)}: cites missing KPI {kid}")
    for path in sorted((LIB / "OMTM").glob("*.md")):
        if path.name != "index.md" and (frontmatter(path, err) or {}).get("kpi") not in ids:
            err(f"{rel(path)}: kpi does not resolve")
    for path in sorted(CHARTS.rglob("*.md")):
        fm = frontmatter(path, err) or {}
        for kid in as_list(fm.get("related_kpis")):
            if kid not in ids:
                err(f"{rel(path)}: related_kpis cites missing {kid}")
    return ids


def check_doc_paths(err: Report) -> None:
    """Backticked paths and markdown links in the hand-written and generated prose must resolve."""
    docs = [ROOT / "SKILL.md", *sorted((ROOT / "references").glob("*.md")), *sorted((ROOT / "agents").glob("*.md"))]
    for sub in ("ONTOLOGY.md", "THEORY", "STANDARDS", "REPORTS", "STORIES", "OMTM", "OKRS", "DASHBOARDS", "KPIS", "KRIS", "_INDICES"):
        p = LIB / sub
        docs += sorted(p.rglob("*.md")) if p.is_dir() else [p]
    for path in docs:
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"`((?:chart-expert/)?(?:library|references|scripts|agents)/[^`*<>\s]+)`", text):
            target = target.rstrip("/")
            base = REPO if target.startswith("chart-expert/") else ROOT
            if not (base / target).exists():
                err(f"{rel(path)}: refers to missing {target}")
        for target in re.findall(r"\]\(([^)#:\s]+\.md)\)", text):
            if not (path.parent / target).exists():
                err(f"{rel(path)}: broken link {target}")


def check_hygiene(err: Report) -> None:
    try:
        tracked = subprocess.run(["git", "-C", str(REPO), "ls-files", "-z"], capture_output=True, check=True).stdout.decode().split("\0")
    except (OSError, subprocess.CalledProcessError):
        tracked = [p.relative_to(REPO).as_posix() for p in REPO.rglob("*") if p.is_file() and ".git" not in p.parts]
    for name in tracked:
        base = name.rsplit("/", 1)[-1]
        if base == ".DS_Store" or base.startswith("._"):
            err(f"{name}: macOS metadata file is tracked")
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and path.suffix in {".md", ".py", ".jsonl", ".json", ".yml", ".yaml"}:
            if LOCAL_PATH.search(path.read_text(encoding="utf-8", errors="replace")) and path.name != "validate_library.py":
                err(f"{rel(path)}: contains an absolute local path")


def main() -> int:
    err = Report()
    stems, canonical = check_cards(err)
    check_indices(canonical, err)
    ids = check_measures(stems, err)
    check_doc_paths(err)
    check_hygiene(err)
    print(f"chart cards={sum(1 for _ in CHARTS.rglob('*.md'))} canonical={len(canonical)} kpis={len(ids)}")
    if err.errors:
        print("FAIL")
        for e in err.errors:
            print(" -", e)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
