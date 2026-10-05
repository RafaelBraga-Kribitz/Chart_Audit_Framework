# -*- coding: utf-8 -*-
"""Structural completeness checks for the visualization library."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(r"C:\Users\Benutzer1\Documents\doing\Chart_Audit_Framework\chart-expert")
LIB = ROOT / "library"
CHARTS = LIB / "CHARTS"


def slug(text: str, limit: int = 72) -> str:
    s = text.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return (s[:limit] or "item").strip("-")


def stems() -> set[str]:
    return {p.stem for p in CHARTS.rglob("*.md")}


def main() -> None:
    errors: list[str] = []
    chart_stems = stems()
    kpis = []
    catalog = LIB / "KPIS" / "_catalog" / "kpis.jsonl"
    if not catalog.exists():
        errors.append("missing kpis.jsonl")
    else:
        for line in catalog.read_text(encoding="utf-8").splitlines():
            if line.strip():
                kpis.append(json.loads(line))
    metrics = set()
    mpath = LIB / "KPIS" / "_catalog" / "metrics.jsonl"
    if mpath.exists():
        for line in mpath.read_text(encoding="utf-8").splitlines():
            if line.strip():
                metrics.add(json.loads(line)["id"])
    ids = {k["id"] for k in kpis}
    required = ["id", "name", "definition", "formula", "formula_inputs", "leading_lagging", "related_charts", "dashboard", "analysis_chart", "communication_chart", "audience"]
    missing_metric_files = 0
    for k in kpis:
        for field in required:
            if not k.get(field):
                errors.append(f"{k.get('id')} missing {field}")
                break
        for mid in k.get("formula_inputs", []):
            if mid not in metrics:
                errors.append(f"{k['id']} input {mid} not in metric catalog")
                break
        for chart in k.get("related_charts", []):
            if chart not in chart_stems:
                errors.append(f"{k['id']} chart {chart} missing")
                break
        if "ibcs" in k["definition"].lower() and len(k["definition"]) > 400 and "SUCCESS" in k["definition"]:
            errors.append(f"{k['id']} looks like pasted standard text")
    # metric files exist for a sample and for every id used... checking 20k stat calls is ok
    metric_root = LIB / "METRICS"
    have_metric_files = {p.stem for p in metric_root.rglob("*.md")} if metric_root.exists() else set()
    for mid in list(metrics)[:]:
        stem = mid.split(".", 1)[1]
        if stem not in have_metric_files:
            missing_metric_files += 1
            if missing_metric_files > 20:
                break
    if missing_metric_files:
        errors.append(f"metric files missing, first failures {missing_metric_files}")
    # subcategory dashboards
    dash_root = LIB / "DASHBOARDS" / "subcategory"
    dash_files = {p.stem for p in dash_root.rglob("*.md")} if dash_root.exists() else set()
    subs = set()
    for k in kpis:
        for p in k["placements"]:
            subs.add((p["category"], p["subcategory"]))
    missing_dash = 0
    for cat, sub in subs:
        if not (dash_root / slug(cat) / f"{slug(sub)}.md").exists():
            missing_dash += 1
    if missing_dash:
        errors.append(f"subcategories without a dashboard file: {missing_dash}")
    # category okrs
    okr_cats = {p.stem for p in (LIB / "OKRS" / "category").glob("*.md")} if (LIB / "OKRS" / "category").exists() else set()
    cats = {p["category"] for k in kpis for p in k["placements"]}
    missing_okr = 0
    for cat in cats:
        if slug(cat) not in okr_cats:
            missing_okr += 1
    if missing_okr:
        errors.append(f"categories without an OKR portfolio: {missing_okr}")
    # note okrs cite real ids
    note_dir = LIB / "OKRS" / "note"
    note_files = list(note_dir.glob("*.md")) if note_dir.exists() else []
    if len(note_files) < 30:
        errors.append(f"note OKRs too few: {len(note_files)}")
    for path in note_files:
        text = path.read_text(encoding="utf-8")
        for kid in re.findall(r"KPI `([^`]+)`", text):
            if kid not in ids:
                errors.append(f"{path.name} cites missing {kid}")
    # chart index
    index = (ROOT / "references" / "chart-library-index.md").read_text(encoding="utf-8")
    if "ft_family" not in index and "FT Family" not in index:
        errors.append("chart index missing family columns")
    for must in ("horizon-chart", "data-table", "ibcs-variance-table", "qq-plot", "kpi-tree"):
        if must not in chart_stems:
            errors.append(f"missing chart {must}")
    # foundations
    for rel in (
        "library/ONTOLOGY.md",
        "references/selection-playbook.md",
        "library/STANDARDS/ibcs-success.md",
        "library/THEORY/15-key-directions-for-performance-management.md",
        "library/REPORTS/board-pack.md",
        "library/STORIES/diagnostic.md",
        "library/OMTM/agency.md",
    ):
        if not (ROOT / rel).exists():
            errors.append(f"missing {rel}")
    ex = LIB / "KPIS" / "_inventory" / "exceptions.md"
    ex_text = ex.read_text(encoding="utf-8") if ex.exists() else ""
    print(f"kpis={len(kpis)} metrics={len(metrics)} charts={len(chart_stems)} note_okrs={len(note_files)} dashboards~={len(dash_files)}")
    print(ex_text.splitlines()[2] if ex_text else "no exceptions file")
    if errors:
        print("FAIL")
        for e in errors[:40]:
            print(" -", e)
        raise SystemExit(1)
    print("PASS")


if __name__ == "__main__":
    main()
