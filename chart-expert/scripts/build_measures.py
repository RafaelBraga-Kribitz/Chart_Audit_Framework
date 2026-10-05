# -*- coding: utf-8 -*-
"""Inventory KPI names, author original entries, metrics, OKRs, dashboards."""
from __future__ import annotations

import html
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(r"C:\Users\Benutzer1\Documents\doing\Chart_Audit_Framework\chart-expert")
LIB = ROOT / "library"
INV = LIB / "KPIS" / "_inventory"
CAT = LIB / "KPIS" / "_catalog"
PAGES = Path(r"C:\Users\Benutzer1\Dev\dashboard-library\the-kpi-compendium\ocr\pages")
PDF = Path(r"C:\Users\Benutzer1\Dev\dashboard-library\the-kpi-compendium\the-kpi-compendium.pdf")
VAULT = Path(r"C:\Users\Benutzer1\Dev\dashboard-library\vault\Dashboards")
BBOOK = Path(r"C:\Users\Benutzer1\Documents\__mktds_2nd_brain\extracted_markdown\Big_Book_of_Dashboards")
CHARTS = LIB / "CHARTS"

HEADER_RE = re.compile(r"key performance indicator", re.I)
PAIR_RE = re.compile(r"<td[^>]*>(.*?)</td>\s*<td[^>]*>(.*?)</td>", re.I | re.S)
ID_RE = re.compile(r"^[A-Za-z▲∆#sSkK0-9][A-Za-z▲∆0-9./-]{1,18}$")

CATEGORIES = [
    ("organizational", "functional", "Accounting"),
    ("organizational", "functional", "Corporate Services"),
    ("organizational", "functional", "CSR"),
    ("organizational", "functional", "Finance"),
    ("organizational", "functional", "Governance, Compliance and Risk"),
    ("organizational", "functional", "Human Resources"),
    ("organizational", "functional", "Information Technology"),
    ("organizational", "functional", "Knowledge and Innovation"),
    ("organizational", "functional", "Management"),
    ("organizational", "functional", "Marketing and Communications"),
    ("organizational", "functional", "Online Presence"),
    ("organizational", "functional", "Portfolio and Project Management"),
    ("organizational", "functional", "Production and Quality"),
    ("organizational", "functional", "Sales and Customer Service"),
    ("organizational", "functional", "Supply Chain"),
    ("organizational", "industries", "Agriculture"),
    ("organizational", "industries", "Arts and Culture"),
    ("organizational", "industries", "Construction"),
    ("organizational", "industries", "Education and Training"),
    ("organizational", "industries", "Financial Institutions"),
    ("organizational", "industries", "Government Local"),
    ("organizational", "industries", "Government"),
    ("organizational", "industries", "Healthcare"),
    ("organizational", "industries", "Hospitality and Tourism"),
    ("organizational", "industries", "Infrastructure"),
    ("organizational", "industries", "Manufacturing"),
    ("organizational", "industries", "Media"),
    ("organizational", "industries", "Non-profit"),
    ("organizational", "industries", "Postal and Courier"),
    ("organizational", "industries", "Professional Services"),
    ("organizational", "industries", "Publishing"),
    ("organizational", "industries", "Real Estate"),
    ("organizational", "industries", "Resources"),
    ("organizational", "industries", "Retail"),
    ("organizational", "industries", "Sport"),
    ("organizational", "industries", "Telecommunications"),
    ("organizational", "industries", "Transportation"),
    ("organizational", "industries", "Utilities"),
    ("global", "human-development", "Administration"),
    ("global", "human-development", "Economics"),
    ("global", "human-development", "Health"),
    ("global", "human-development", "Information Society"),
    ("global", "human-development", "Labor and Social Protection"),
    ("global", "human-development", "Peace and Justice"),
    ("global", "human-development", "Population"),
    ("global", "human-development", "Quality of Life"),
    ("global", "human-development", "Transportation and Infrastructure"),
    ("global", "environment", "Biodiversity"),
    ("global", "environment", "Environment and Pollution"),
    ("global", "environment", "Natural Resources"),
    ("personal", "productivity", "Finances"),
    ("personal", "productivity", "Home Economics"),
    ("personal", "productivity", "Personal Development"),
    ("personal", "productivity", "Planning"),
    ("personal", "productivity", "Process Management"),
    ("personal", "well-being", "Fitness"),
    ("personal", "well-being", "Health"),
    ("personal", "well-being", "Nutrition"),
    ("personal", "well-being", "Relationship"),
    ("personal", "well-being", "Work-life Balance"),
]


def slug(text: str, limit: int = 72) -> str:
    s = text.lower()
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return (s[:limit] or "item").strip("-")


def strip_cell(raw: str) -> str:
    raw = re.sub(r"<[^>]+>", " ", raw)
    raw = html.unescape(raw)
    return re.sub(r"\s+", " ", raw).strip(" |")


def is_id(text: str) -> bool:
    text = text.strip()
    if not text or HEADER_RE.search(text) or len(text) > 22:
        return False
    digits = sum(ch.isdigit() for ch in text)
    if digits < 2:
        return False
    letters = sum(ch.isalpha() for ch in text)
    if letters > 6 and digits < 3:
        return False
    return bool(ID_RE.match(text.replace(" ", ""))) or digits >= 3 and len(text) <= 16


def parse_name(raw: str) -> tuple[str, str] | None:
    text = raw.strip(" .:;-")
    if HEADER_RE.search(text) or len(text) < 4 or len(text) > 160:
        return None
    unit = "number"
    prefix = ""
    m = re.match(r"^([$%#])\s*", text)
    if m:
        prefix = m.group(1)
        text = text[m.end():].strip()
        unit = {"$": "currency", "%": "percent", "#": "count"}[prefix]
    letters = sum(ch.isalpha() for ch in text)
    if letters < 4 or letters / max(len(text), 1) < 0.5:
        return None
    if text.lower() in {"name", "key performance indicator name"}:
        return None
    return unit, text


def norm_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()


def match_category(text: str) -> tuple[str, str, str] | None:
    low = text.lower()
    hits = []
    for ctx, group, cat in CATEGORIES:
        if cat.lower() in low and len(cat) > 4:
            hits.append((len(cat), ctx, group, cat))
    if not hits:
        return None
    hits.sort(reverse=True)
    _, ctx, group, cat = hits[0]
    return ctx, group, cat


def context_from_header(text: str, state: dict) -> None:
    low = text.lower()
    if "organizational" in low and "functional" in low:
        state["context"], state["group"] = "organizational", "functional"
    elif "organizational" in low and "industr" in low:
        state["context"], state["group"] = "organizational", "industries"
    elif "global" in low and "human" in low:
        state["context"], state["group"] = "global", "human-development"
    elif "global" in low and "environment" in low:
        state["context"], state["group"] = "global", "environment"
    elif "personal" in low and "well" in low:
        state["context"], state["group"] = "personal", "well-being"
    elif "personal" in low:
        state["context"], state["group"] = "personal", "productivity"


def heading_sub(line: str, category: str) -> str | None:
    line = strip_cell(line)
    if not line or len(line) > 80 or len(line) < 3:
        return None
    if line.startswith("<") or line.startswith("<!--") or "KPI INSTITUTE" in line:
        return None
    words = line.split()
    if not 1 <= len(words) <= 8:
        return None
    if is_id(line) or parse_name(line) and line[:1] in "$%#":
        return None
    if category and category.lower() in line.lower() and len(words) <= 4:
        return None
    if not line[0].isalpha():
        return None
    return line


def parse_markdown_pages() -> list[dict]:
    rows = []
    state = {"context": "organizational", "group": "functional", "category": "Accounting", "sub": "General"}
    files = sorted(PAGES.glob("page_*.md"))
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        page = path.stem
        context_from_header(text[:500], state)
        # walk blocks split by tables
        parts = re.split(r"(<table[\s\S]*?</table>)", text, flags=re.I)
        for part in parts:
            if part.lower().startswith("<table"):
                for a, b in PAIR_RE.findall(part):
                    left, right = strip_cell(a), strip_cell(b)
                    # either order
                    pairs = []
                    if is_id(left):
                        pairs.append((left, right))
                    if is_id(right) and not is_id(left):
                        pairs.append((right, left))
                    for ident, raw_name in pairs:
                        parsed = parse_name(raw_name)
                        if not parsed:
                            rows.append({"status": "exception", "reason": "unreadable name", "source_label": ident, "raw": raw_name, "page": page,
                                         "context": state["context"], "group": state["group"], "category": state["category"], "subcategory": state["sub"]})
                            continue
                        unit, name = parsed
                        rows.append({
                            "status": "ok", "source_label": ident, "unit": unit, "name": name, "page": page,
                            "context": state["context"], "group": state["group"], "category": state["category"], "subcategory": state["sub"],
                        })
                continue
            for line in part.splitlines():
                hit = match_category(line)
                if hit and len(line) < 120:
                    state["context"], state["group"], state["category"] = hit
                    state["sub"] = "General"
                    continue
                sub = heading_sub(line, state["category"])
                if sub:
                    state["sub"] = sub
    return rows


def cluster_columns(words: list[dict]) -> list[list[dict]]:
    body = [w for w in words if w["y"] > 70]
    if not body:
        return []
    xs = sorted({w["x"] for w in body})
    breaks = [0]
    for i in range(1, len(xs)):
        if xs[i] - xs[i - 1] > 28:
            breaks.append(i)
    ranges = []
    for i, b in enumerate(breaks):
        start = xs[b]
        end = xs[breaks[i + 1] - 1] if i + 1 < len(breaks) else xs[-1]
        ranges.append((start - 8, end + 36))
    cols = []
    for a, b in ranges:
        col = [w for w in body if a <= w["x"] <= b]
        if col:
            cols.append(col)
    return cols


def words_to_rows(page: str, words: list[dict], state: dict) -> list[dict]:
    header = " ".join(w["t"] for w in words if w["y"] < 80)
    context_from_header(header, state)
    hit = match_category(header)
    if hit:
        state["context"], state["group"], state["category"] = hit
        state["sub"] = "General"
    cols = cluster_columns(words)
    rows = []
    for i, col in enumerate(cols):
        idish = sum(1 for w in col if is_id(w["t"]))
        if idish < max(3, len(col) // 5):
            # possible subcategory label: tall isolated words
            text = " ".join(w["t"] for w in sorted(col, key=lambda z: (z["y"], z["x"]))[:6])
            sub = heading_sub(text, state["category"])
            if sub and idish == 0:
                state["sub"] = sub
            continue
        name_col = cols[i + 1] if i + 1 < len(cols) else []
        for ident in col:
            if not is_id(ident["t"]):
                continue
            near = [w for w in name_col if abs(w["y"] - ident["y"]) <= 10]
            near.sort(key=lambda z: z["x"])
            raw = " ".join(w["t"] for w in near)
            parsed = parse_name(raw)
            if not parsed:
                rows.append({"status": "exception", "reason": "unreadable name", "source_label": ident["t"], "raw": raw, "page": page,
                             "context": state["context"], "group": state["group"], "category": state["category"], "subcategory": state["sub"]})
                continue
            unit, name = parsed
            rows.append({"status": "ok", "source_label": ident["t"], "unit": unit, "name": name, "page": page,
                         "context": state["context"], "group": state["group"], "category": state["category"], "subcategory": state["sub"]})
    return rows


def ensure_ocr() -> None:
    img_dir = INV / "page_images"
    out_dir = INV / "winocr"
    img_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)
    from pypdf import PdfReader
    reader = PdfReader(str(PDF))
    missing_img = []
    for n in range(210, min(len(reader.pages), 299) + 1):
        dest = img_dir / f"page_{n:04d}.jpg"
        if not dest.exists():
            missing_img.append(n)
    if missing_img:
        for n in missing_img:
            page = reader.pages[n - 1]
            xo = page["/Resources"]["/XObject"].get_object()
            data = None
            for v in xo.values():
                data = v.get_object().get_data()
                break
            if data:
                (img_dir / f"page_{n:04d}.jpg").write_bytes(data)
    subprocess.run([
        "powershell", "-NoProfile", "-File",
        str(ROOT / "scripts" / "ocr_pages.ps1"),
        "-ImageDir", str(img_dir),
        "-OutDir", str(out_dir),
    ], check=True)


def parse_winocr(state: dict) -> list[dict]:
    rows = []
    folder = INV / "winocr"
    if not folder.exists():
        return rows
    for path in sorted(folder.glob("page_*.json")):
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        rows.extend(words_to_rows(path.stem, data.get("words", []), state))
    return rows


KRI_WORDS = ("spill", "incident", "downtime", "breach", "non-compliance", "noncompliance", "fatality", "injury", "accident", "complaint", "defect", "arrear", "default", "outage", "violation", "hazard", "loss event")
DOWN_WORDS = ("cost", "expense", "churn", "time", "days", "cycle", "error", "complaint", "defect", "waste", "turnover", "attrition", "downtime", "incident", "accident")
LEAD_WORDS = ("pipeline", "backlog", "scheduled", "application", "training", "lead", "demo", "engagement", "vacancy", "onboarding", "forecast", "queue")
CORRIDOR_WORDS = ("utilization", "utilisation", "mix", "buffer", "coverage ratio", "load factor")

SEEDS = {
    "days sales outstanding": ("percent", "(A / B) * Days", ["credit sales", "accounts receivable", "days in period"], "ratio", "down", "lagging",
                              "Average number of days to collect credit sales. A is accounts receivable, B is credit sales."),
    "dso": ("count", "(A / B) * C", ["accounts receivable", "credit sales", "days in period"], "ratio", "down", "lagging",
            "Days sales outstanding. Receivables divided by credit sales, times the days in the period."),
    "customer acquisition cost": ("currency", "A / B", ["sales and marketing cost", "new customers acquired"], "ratio", "down", "lagging",
                                  "Cost to acquire one new customer."),
    "cost per acquisition": ("currency", "A / B", ["acquisition cost", "acquisitions"], "ratio", "down", "lagging",
                             "Same family as customer acquisition cost. Use one canonical name when the numerator and the acquired unit match."),
    "monthly recurring revenue": ("currency", "A", ["sum of recurring charges for the month"], "count", "up", "lagging",
                                  "Contracted recurring revenue normalized to one month."),
    "customer churn rate": ("percent", "(A / B) * 100", ["customers lost in the period", "customers at the start of the period"], "ratio", "down", "lagging",
                            "Share of starting customers lost during the period. Logo churn, not revenue churn, unless the name says revenue."),
    "gross profit margin": ("percent", "(A / B) * 100", ["gross profit", "revenue"], "ratio", "up", "lagging",
                            "Share of revenue left after direct cost."),
    "profit margin": ("percent", "(A / B) * 100", ["profit", "revenue"], "ratio", "up", "lagging",
                      "Profit divided by revenue. The name must say which profit (gross, operating, net)."),
    "utilization rate": ("percent", "(A / B) * 100", ["billable hours", "available hours"], "ratio", "corridor", "leading",
                         "Share of available hours that are billable. Too low and too high are both failures."),
    "labour efficiency ratio": ("number", "A / B", ["gross profit", "labor cost"], "ratio", "up", "lagging",
                                "Gross profit earned per unit of labor cost."),
    "labor efficiency ratio": ("number", "A / B", ["gross profit", "labor cost"], "ratio", "up", "lagging",
                               "Gross profit earned per unit of labor cost."),
}


def kind_for(name: str) -> str:
    low = name.lower()
    return "kri" if any(w in low for w in KRI_WORDS) else "kpi"


def direction_for(name: str, unit: str) -> str:
    low = name.lower()
    if any(w in low for w in CORRIDOR_WORDS):
        return "corridor"
    if any(w in low for w in DOWN_WORDS):
        return "down"
    return "up"


def timing_for(name: str) -> str:
    low = name.lower()
    if any(w in low for w in LEAD_WORDS):
        return "leading"
    return "lagging"


def formula_for(name: str, unit: str) -> tuple[str, list[str], str, str]:
    key = norm_name(name)
    if key in SEEDS:
        unit_s, formula, inputs, ftype, direction, timing, _defn = SEEDS[key]
        return formula, inputs, ftype, SEEDS[key][6]
    low = name.lower()
    per = re.split(r"\bper\b", name, maxsplit=1, flags=re.I)
    if len(per) == 2 and per[0].strip() and per[1].strip():
        return "A / B", [per[0].strip(), per[1].strip()], "ratio", ""
    if "margin" in low:
        return "(A / B) * 100", [name.replace("margin", "profit").strip(), "revenue"], "ratio", ""
    m = re.search(r"(.+?)\s+(from|of|to)\s+(.+)", name, re.I)
    if unit == "percent" and m:
        return "(A / B) * 100", [m.group(1).strip(), m.group(3).strip()], "ratio", ""
    if unit == "percent" and any(w in low for w in ("rate", "ratio", "share", "percent")):
        return "(A / B) * 100", [f"numerator of {name}", f"base of {name}"], "ratio", ""
    if "versus" in low or " vs " in low or "variance" in low:
        parts = re.split(r"\bversus\b|\bvs\.?\b", name, maxsplit=1, flags=re.I)
        if len(parts) == 2:
            return "(A / B) * 100", [parts[0].strip(), parts[1].strip()], "ratio", ""
        return "A - B", [f"actual {name}", f"reference {name}"], "difference", ""
    if unit == "percent":
        return "(A / B) * 100", [f"part named by {name}", f"whole named by {name}"], "ratio", ""
    if any(w in low for w in ("average", "avg", "mean")):
        return "A / B", [f"sum underlying {name}", "count of observations"], "average", ""
    if "index" in low:
        return "(A / B) * 100", [f"current {name}", f"base-period {name}"], "index", ""
    if any(w in low for w in ("satisfaction", "nps", "pulse", "score")):
        return "A", [name], "survey", ""
    if unit == "currency":
        return "A", [name], "count", ""
    return "A", [name], "count", ""


def definition_for(name: str, unit: str, category: str, sub: str, formula: str, inputs: list[str]) -> str:
    key = norm_name(name)
    if key in SEEDS:
        return SEEDS[key][6] + f" Placed under {category} / {sub}."
    base = (
        f"{name} measures that result inside {category}, subcategory {sub}. "
        f"The unit is {unit}. The formula is {formula}, where "
        + ", ".join(f"{letter} is {inp}" for letter, inp in zip("ABCDEFG", inputs))
        + ". Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed."
    )
    return base


def charts_for(name: str, unit: str) -> tuple[str, str]:
    low = name.lower()
    if any(w in low for w in ("distribution", "variance of", "histogram")):
        analysis = "histogram"
    elif "versus" in low or " vs " in low:
        analysis = "scatter-plot"
    elif unit == "percent":
        analysis = "diverging-bar"
    else:
        analysis = "bar-chart"
    if any(w in low for w in ("month", "daily", "trend", "over time", "ytd")):
        comm = "line-chart"
    elif unit == "percent" or "margin" in low or "rate" in low:
        comm = "bullet-graph"
    elif "versus" in low or "variance" in low or "bridge" in low:
        comm = "waterfall-chart"
    elif "per " in low:
        comm = "horizontal-bar-chart"
    else:
        comm = "bar-chart"
    return analysis, comm


def audiences_for(category: str) -> list[str]:
    low = category.lower()
    roles = ["Executive", "Data Analytics"]
    if any(k in low for k in ("human", "labor", "work-life", "fitness")):
        roles.append("HR")
    if any(k in low for k in ("market", "online", "media", "retail", "ecommerce")):
        roles.append("Marketing Analytics")
    if any(k in low for k in ("information technology", "telecom", "production")):
        roles.extend(["Development", "Data Scientist"])
    if any(k in low for k in ("health", "education", "biodivers", "environment", "science", "research")):
        roles.extend(["Researcher", "R&D"])
    if "professional" in low or "finance" in low or "account" in low:
        roles.append("Data Analytics")
    # unique preserve
    out = []
    for r in roles:
        if r not in out:
            out.append(r)
    return out


def level_for(category: str, name: str) -> str:
    low = name.lower()
    if any(w in low for w in ("per employee", "ticket", "queue", "cycle time", "daily")):
        return "operational"
    if category in {"Management", "Finance", "Economics"}:
        return "strategic"
    return "tactical"


def author(rows: list[dict]) -> tuple[list[dict], list[dict], list[dict]]:
    canon: dict[str, dict] = {}
    exceptions = [r for r in rows if r["status"] != "ok"]
    for row in rows:
        if row["status"] != "ok":
            continue
        key = norm_name(row["name"])
        if key in canon:
            place = {"context": row["context"], "group": row["group"], "category": row["category"], "subcategory": row["subcategory"], "source_label": row["source_label"], "page": row["page"]}
            if place not in canon[key]["placements"]:
                canon[key]["placements"].append(place)
            continue
        formula, inputs, ftype, defn_extra = formula_for(row["name"], row["unit"])
        if not defn_extra:
            definition = definition_for(row["name"], row["unit"], row["category"], row["subcategory"], formula, inputs)
        else:
            definition = defn_extra if defn_extra.endswith(".") else definition_for(row["name"], row["unit"], row["category"], row["subcategory"], formula, inputs)
            if key in SEEDS:
                definition = SEEDS[key][6] + f" Placed under {row['category']} / {row['subcategory']}."
        analysis, comm = charts_for(row["name"], row["unit"])
        metric_ids = []
        metric_objs = []
        for inp in inputs:
            mid = "metric." + slug(inp)
            metric_ids.append(mid)
            metric_objs.append(inp)
        cat_slug = slug(row["category"])
        kid = f"kpi.{cat_slug}.{slug(row['name'])}"
        dash = f"dash.{cat_slug}.{slug(row['subcategory'])}"
        notes = []
        if "gross profit" in key and "head" in key or "per employee" in key and "gross profit" in key:
            notes.append("Published agency rule of thumb, not a universal target: about 135,000 AUD / 75,000 GBP / 95,000 USD gross profit per head per year.")
        if "team cost" in key or ("staff" in key and "cost" in key and "profit" in key):
            notes.append("Published agency rule of thumb: team cost at most 60 percent of gross profit.")
        if "marketing" in key and ("spend" in key or "cost" in key) and "profit" in key:
            notes.append("Published agency rule of thumb: marketing spend around 5 to 10 percent of gross profit.")
        canon[key] = {
            "id": kid,
            "name": row["name"],
            "measure_kind": kind_for(row["name"]),
            "unit": row["unit"],
            "definition": definition,
            "formula": formula,
            "formula_inputs": metric_ids,
            "input_names": metric_objs,
            "formula_type": ftype,
            "direction": direction_for(row["name"], row["unit"]),
            "leading_lagging": timing_for(row["name"]),
            "level": level_for(row["category"], row["name"]),
            "audience": audiences_for(row["category"]),
            "questions": [
                f"Is {row['name']} on the desired side of its target for this period?",
                f"Which input in the formula moved {row['name']}?",
            ],
            "related_charts": [comm, analysis] if comm != analysis else [comm],
            "analysis_surface": "notebook",
            "analysis_chart": analysis,
            "communication_surface": "dashboard",
            "communication_chart": comm,
            "dashboard": dash,
            "pitfalls": "Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.",
            "target_notes": notes,
            "provenance": "authored",
            "placements": [{"context": row["context"], "group": row["group"], "category": row["category"], "subcategory": row["subcategory"], "source_label": row["source_label"], "page": row["page"]}],
        }
    # ensure user-facing seeds exist
    for key, spec in SEEDS.items():
        if key not in canon and len(key) > 3:
            unit, formula, inputs, ftype, direction, timing, defn = spec
            name = key.title() if key != "dso" else "Days sales outstanding"
            if key == "dso":
                continue
            cat, sub = "Finance", "General"
            canon[key] = {
                "id": f"kpi.{slug(cat)}.{slug(name)}",
                "name": name,
                "measure_kind": "kpi",
                "unit": {"currency": "currency", "percent": "percent", "count": "count", "number": "number"}.get(unit, unit),
                "definition": defn,
                "formula": formula,
                "formula_inputs": ["metric." + slug(i) for i in inputs],
                "input_names": inputs,
                "formula_type": ftype,
                "direction": direction,
                "leading_lagging": timing,
                "level": "tactical",
                "audience": ["Executive", "Data Analytics"],
                "questions": [f"Is {name} on the desired side of its target?"],
                "related_charts": ["bullet-graph", "waterfall-chart"],
                "analysis_surface": "notebook",
                "analysis_chart": "waterfall-chart",
                "communication_surface": "dashboard",
                "communication_chart": "bullet-graph",
                "dashboard": f"dash.{slug(cat)}.{slug(sub)}",
                "pitfalls": "Confirm the inputs match the contract or the ledger before the number is briefed.",
                "target_notes": [],
                "provenance": "authored",
                "placements": [{"context": "organizational", "group": "functional", "category": cat, "subcategory": sub, "source_label": "user-note", "page": "note"}],
            }
    named = [
        ("Days sales outstanding", "Finance", "Cash Management", "count", "(A / B) * C", ["accounts receivable", "credit sales", "days in period"], "ratio", "down", "lagging", "Average days to collect credit sales."),
        ("Accounts receivable aging", "Finance", "Cash Management", "currency", "A", ["receivables grouped by age bucket"], "count", "down", "lagging", "Receivables split by how long they have been outstanding."),
        ("Revenue per employee", "Finance", "Profitability", "currency", "A / B", ["revenue", "employees"], "ratio", "up", "lagging", "Revenue divided by headcount."),
        ("Customer acquisition cost", "Marketing and Communications", "Acquisition", "currency", "A / B", ["sales and marketing cost", "new customers acquired"], "ratio", "down", "lagging", "Cost to acquire one new customer. Cost per acquisition is the same measure when the unit acquired is a customer."),
        ("Net revenue minus CAC", "Finance", "Profitability", "currency", "A - B", ["net revenue", "customer acquisition cost"], "difference", "up", "lagging", "Net revenue left after acquisition cost."),
        ("Profit margin", "Finance", "Profitability", "percent", "(A / B) * 100", ["profit", "revenue"], "ratio", "up", "lagging", "Profit divided by revenue. Say which profit."),
        ("LTV to CAC ratio", "Finance", "Profitability", "number", "A / B", ["customer lifetime value", "customer acquisition cost"], "ratio", "up", "lagging", "How many times acquisition cost is covered by lifetime value."),
        ("Lead to client conversion rate", "Professional Services", "Business Development", "percent", "(A / B) * 100", ["clients won", "leads"], "ratio", "up", "lagging", "Share of leads that become clients."),
        ("Billed versus expected", "Portfolio and Project Management", "Delivery", "percent", "(A / B) * 100", ["amount billed", "amount expected"], "ratio", "corridor", "lagging", "What was billed divided by what the plan said would be billed."),
        ("Project contribution margin", "Portfolio and Project Management", "Delivery", "percent", "(A / B) * 100", ["project revenue minus direct cost", "project revenue"], "ratio", "up", "lagging", "Share of project revenue left after direct delivery cost."),
        ("Labor efficiency ratio", "Professional Services", "Delivery", "number", "A / B", ["gross profit", "labor cost"], "ratio", "up", "lagging", "Gross profit per unit of labor cost."),
        ("Net profit", "Finance", "Profitability", "currency", "A - B", ["revenue", "total costs"], "difference", "up", "lagging", "What remains after costs."),
        ("Monthly recurring profit", "Finance", "Profitability", "currency", "A", ["recurring profit for the month"], "count", "up", "lagging", "Recurring profit normalized to one month."),
        ("Monthly recurring revenue", "Sales and Customer Service", "Revenue", "currency", "A", ["sum of recurring charges for the month"], "count", "up", "lagging", "Contracted recurring revenue for one month."),
        ("Customer churn rate", "Sales and Customer Service", "Retention", "percent", "(A / B) * 100", ["customers lost in the period", "customers at the start of the period"], "ratio", "down", "lagging", "Share of starting customers lost. Not revenue churn unless the name says revenue."),
        ("Upsell rate", "Sales and Customer Service", "Expansion", "percent", "(A / B) * 100", ["customers who bought more", "customers eligible"], "ratio", "up", "lagging", "Share of customers who expanded."),
        ("Operating cash flow", "Finance", "Cash Management", "currency", "A", ["cash from operations"], "count", "up", "lagging", "Cash generated by operations."),
        ("Client breakeven", "Professional Services", "Clients", "count", "A", ["months or revenue until client contribution turns positive"], "count", "down", "lagging", "How long until the client covers the cost to serve and acquire them."),
        ("Client ROI", "Professional Services", "Clients", "percent", "(A / B) * 100", ["client profit", "cost to serve the client"], "ratio", "up", "lagging", "Profit from the client divided by the cost to serve them."),
        ("Wins by lead source", "Marketing and Communications", "Acquisition", "count", "A", ["wins coded to a lead source"], "count", "up", "lagging", "Closed work split by the source of the lead."),
        ("Email click through rate", "Marketing and Communications", "Content", "percent", "(A / B) * 100", ["clicks", "emails delivered"], "ratio", "up", "lagging", "Clicks divided by emails delivered."),
        ("Estimated versus actual project time", "Portfolio and Project Management", "Delivery", "percent", "(A / B) * 100", ["estimated hours", "actual hours"], "ratio", "corridor", "lagging", "Estimated hours divided by actual hours. Above 100 means the work took fewer hours than estimated."),
        ("Estimated versus actual project cost", "Portfolio and Project Management", "Delivery", "percent", "(A / B) * 100", ["estimated cost", "actual cost"], "ratio", "corridor", "lagging", "Estimated cost divided by actual cost."),
        ("Lead time per project", "Portfolio and Project Management", "Delivery", "count", "A", ["elapsed time from start to finish"], "count", "down", "lagging", "Calendar time a project takes."),
        ("Utilization rate", "Professional Services", "Delivery", "percent", "(A / B) * 100", ["billable hours", "available hours"], "ratio", "corridor", "leading", "Billable hours divided by available hours. A corridor, not a maximum."),
        ("Gross profit per head", "Professional Services", "Profitability", "currency", "A / B", ["gross profit", "fee earners"], "ratio", "up", "lagging", "Gross profit per fee earner. Published agency rules of thumb exist and are target notes, not laws."),
        ("Team cost to gross profit", "Professional Services", "Profitability", "percent", "(A / B) * 100", ["team cost", "gross profit"], "ratio", "down", "lagging", "Team cost as a share of gross profit."),
        ("Marketing spend to gross profit", "Marketing and Communications", "Spend", "percent", "(A / B) * 100", ["marketing spend", "gross profit"], "ratio", "corridor", "lagging", "Marketing spend as a share of gross profit."),
        ("Closed won rate", "Sales and Customer Service", "Pipeline", "percent", "(A / B) * 100", ["deals won", "deals closed"], "ratio", "up", "lagging", "Wins divided by decisions."),
        ("Pipeline coverage", "Sales and Customer Service", "Pipeline", "number", "A / B", ["open pipeline", "quota"], "ratio", "corridor", "leading", "Open pipeline divided by the remaining quota."),
        ("Net promoter score", "Sales and Customer Service", "Customers", "number", "A", ["survey promoter share minus detractor share"], "survey", "up", "lagging", "Promoters minus detractors on the stated survey scale."),
        ("Website visitors", "Online Presence", "Traffic", "count", "A", ["sessions or users in the period"], "count", "up", "leading", "People or sessions on the site. A leading input, not the outcome."),
        ("Landing page conversion rate", "Online Presence", "Conversion", "percent", "(A / B) * 100", ["conversions", "landing page visits"], "ratio", "up", "lagging", "Conversions divided by visits to the page."),
        ("Cost per lead", "Marketing and Communications", "Acquisition", "currency", "A / B", ["campaign cost", "leads"], "ratio", "down", "lagging", "Spend divided by leads."),
        ("Click through rate", "Marketing and Communications", "Acquisition", "percent", "(A / B) * 100", ["clicks", "impressions"], "ratio", "up", "leading", "Clicks divided by impressions."),
    ]
    for name, cat, sub, unit, formula, inputs, ftype, direction, timing, defn in named:
        key = norm_name(name)
        if key in canon:
            canon[key]["target_notes"] = canon[key].get("target_notes") or []
            if "gross profit per head" in key:
                canon[key]["target_notes"].append("Published agency rule of thumb, not a law: about 135,000 AUD, 75,000 GBP, or 95,000 USD gross profit per head per year, and about 20,000 AUD, 10,000 GBP, or 13,000 USD per month per fee earner.")
            if "team cost" in key:
                canon[key]["target_notes"].append("Published agency rule of thumb: team cost at most 60 percent of gross profit.")
            if "marketing spend" in key:
                canon[key]["target_notes"].append("Published agency rule of thumb: marketing spend around 5 to 10 percent of gross profit.")
            continue
        analysis, comm = charts_for(name, "percent" if unit == "percent" else "currency")
        canon[key] = {
            "id": f"kpi.{slug(cat)}.{slug(name)}",
            "name": name,
            "measure_kind": "kpi",
            "unit": unit,
            "definition": defn + f" Placed under {cat} / {sub}.",
            "formula": formula,
            "formula_inputs": ["metric." + slug(i) for i in inputs],
            "input_names": inputs,
            "formula_type": ftype,
            "direction": direction,
            "leading_lagging": timing,
            "level": "tactical",
            "audience": audiences_for(cat),
            "questions": [f"Is {name} on the desired side of its target for this period?", f"Which input moved {name}?"],
            "related_charts": [comm, analysis] if comm != analysis else [comm],
            "analysis_surface": "notebook",
            "analysis_chart": analysis,
            "communication_surface": "dashboard",
            "communication_chart": comm,
            "dashboard": f"dash.{slug(cat)}.{slug(sub)}",
            "pitfalls": "Do not brief the analysis chart to an executive if the communication chart already answers the decision.",
            "target_notes": [],
            "provenance": "authored",
            "placements": [{"context": "organizational", "group": "functional", "category": cat, "subcategory": sub, "source_label": "user-note", "page": "note"}],
        }
        if "gross profit per head" in key:
            canon[key]["target_notes"].append("Published agency rule of thumb, not a law: about 135,000 AUD, 75,000 GBP, or 95,000 USD gross profit per head per year.")
        if "team cost" in key:
            canon[key]["target_notes"].append("Published agency rule of thumb: team cost at most 60 percent of gross profit.")
        if "marketing spend" in key:
            canon[key]["target_notes"].append("Published agency rule of thumb: marketing spend around 5 to 10 percent of gross profit.")
    # Measures named by the OKR notes. Exact titles so a key result does not bind to a longer lookalike.
    note_measures = [
        ("Revenue", "Sales and Customer Service", "Revenue", "currency", "A", ["recognized revenue"], "count", "up", "lagging", "Revenue recognized in the period on the stated basis."),
        ("Sales growth", "Sales and Customer Service", "Revenue", "percent", "(A / B) * 100", ["revenue this period", "revenue in the comparison period"], "ratio", "up", "lagging", "This period's revenue divided by the comparison period, minus the base if the result is stated as growth rather than an index. Say the region and the comparison."),
        ("Average deal size", "Sales and Customer Service", "Pipeline", "currency", "A / B", ["closed-won revenue", "closed-won deals"], "ratio", "up", "lagging", "Closed-won revenue divided by closed-won deals."),
        ("Customer interviews", "Sales and Customer Service", "Customers", "count", "A", ["customer interviews completed"], "count", "up", "leading", "Completed interviews with customers in the period. An activity count; pair it with an outcome such as retention or NPS."),
        ("Customer retention", "Sales and Customer Service", "Retention", "percent", "(A / B) * 100", ["customers retained", "customers at the start of the period"], "ratio", "up", "lagging", "Share of starting customers still active at the end of the period."),
        ("Weekly active users", "Sales and Customer Service", "Customers", "percent", "(A / B) * 100", ["customers active in the week", "customers"], "ratio", "up", "leading", "Share of customers who used the product in the week."),
        ("Employee pulse score", "Human Resources", "Engagement", "number", "A", ["mean pulse response"], "survey", "up", "leading", "Mean response on the stated pulse scale."),
        ("Town hall held", "Human Resources", "Engagement", "count", "A", ["town halls held"], "count", "up", "leading", "Count of town halls held. A task count; the outcome is the pulse or retention that follows."),
        ("Marketing qualified leads", "Marketing and Communications", "Acquisition", "count", "A", ["leads meeting the qualification rule"], "count", "up", "leading", "Leads that meet the written qualification rule. Say the channel when the result is channel-specific."),
        ("Referring domains", "Online Presence", "Traffic", "count", "A", ["new referring domains"], "count", "up", "leading", "Distinct sites that newly link to the property in the period."),
        ("Pages meeting speed budget", "Online Presence", "Conversion", "count", "A", ["pages inside the speed budget"], "count", "up", "leading", "Pages whose measured speed is inside the agreed budget."),
        ("Newsletters published", "Marketing and Communications", "Content", "count", "A", ["newsletter issues published"], "count", "up", "leading", "Issues actually sent. A task count; pair it with click-through or pipeline."),
        ("Blog posts published", "Marketing and Communications", "Content", "count", "A", ["posts published"], "count", "up", "leading", "Posts published in the period."),
        ("Expert interviews", "Marketing and Communications", "Content", "count", "A", ["expert interviews published"], "count", "up", "leading", "Interviews published, not conversations merely scheduled."),
        ("Blog subscribers", "Marketing and Communications", "Content", "count", "A", ["subscribers"], "count", "up", "lagging", "People subscribed to the blog at period end."),
        ("Media meetings", "Marketing and Communications", "Awareness", "count", "A", ["media meetings held"], "count", "up", "leading", "Meetings held with media. Pair with a reach or pipeline outcome."),
        ("Influencer meetings", "Marketing and Communications", "Awareness", "count", "A", ["influencer meetings held"], "count", "up", "leading", "Meetings held with influencers."),
        ("Speaking slots", "Marketing and Communications", "Awareness", "count", "A", ["accepted speaking slots"], "count", "up", "leading", "Conference talks accepted, not talks merely submitted."),
        ("Analyst briefings", "Marketing and Communications", "Awareness", "count", "A", ["analyst briefings held"], "count", "up", "leading", "Briefings held with analysts."),
        ("Analyst webinars", "Marketing and Communications", "Awareness", "count", "A", ["webinars with an analyst"], "count", "up", "leading", "Webinars that included an analyst."),
        ("Community page visits", "Marketing and Communications", "Community", "count", "A", ["community page visits"], "count", "up", "leading", "Visits to community pages in the period."),
        ("Community participation rate", "Marketing and Communications", "Community", "percent", "(A / B) * 100", ["customers who participated", "customers"], "ratio", "up", "lagging", "Share of customers who did something in the community beyond a visit."),
        ("Experts contacted", "Marketing and Communications", "Community", "count", "A", ["experts contacted"], "count", "up", "leading", "Experts contacted. Contact is an activity; publication is the result."),
        ("Product pages shipped", "Marketing and Communications", "Enablement", "count", "A", ["product pages updated"], "count", "up", "leading", "Product pages updated to the agreed standard."),
        ("Sales enablement assets", "Marketing and Communications", "Enablement", "count", "A", ["enablement assets finished"], "count", "up", "leading", "Datasheets, briefs, and packs finished for sales."),
        ("Partner whitepapers", "Sales and Customer Service", "Partners", "count", "A", ["partner papers published"], "count", "up", "leading", "Partner papers published."),
        ("Partner webinars", "Sales and Customer Service", "Partners", "count", "A", ["partner webinars held"], "count", "up", "leading", "Webinars held with or for partners."),
        ("Partner events", "Sales and Customer Service", "Partners", "count", "A", ["partner events held"], "count", "up", "leading", "Partner events held."),
        ("Pipeline created", "Sales and Customer Service", "Pipeline", "currency", "A", ["new pipeline value"], "count", "up", "leading", "Value of opportunities created in the period, on the stated stage rule."),
        ("Product demos", "Sales and Customer Service", "Pipeline", "count", "A", ["demos delivered"], "count", "up", "leading", "Demos delivered, not demos scheduled."),
        ("Account executives hired", "Human Resources", "Hiring", "count", "A", ["account executives who started"], "count", "up", "lagging", "Account executives who started in the period."),
        ("Sales development hires", "Human Resources", "Hiring", "count", "A", ["sales development representatives who started"], "count", "up", "lagging", "Sales development hires who started."),
        ("Interview to offer ratio", "Human Resources", "Hiring", "number", "A / B", ["interviews", "offers"], "ratio", "corridor", "leading", "Interviews divided by offers. A corridor: too low and too high both mean the process is off."),
        ("Coaching sessions", "Sales and Customer Service", "Pipeline", "count", "A", ["coaching sessions held"], "count", "up", "leading", "Coaching sessions held. Pair with a pipeline or win-rate outcome."),
        ("New accounts", "Sales and Customer Service", "Pipeline", "count", "A", ["new named accounts"], "count", "up", "lagging", "Named accounts opened in the period."),
        ("Resellers onboarded", "Sales and Customer Service", "Partners", "count", "A", ["resellers onboarded"], "count", "up", "lagging", "Resellers who completed onboarding."),
        ("Sales qualified leads", "Sales and Customer Service", "Pipeline", "count", "A", ["leads accepted by sales"], "count", "up", "leading", "Leads sales accepted under the written qualification rule."),
        ("SDRs trained", "Human Resources", "Hiring", "count", "A", ["sales development representatives who finished training"], "count", "up", "leading", "SDRs who finished the named training."),
        ("Expansion revenue", "Sales and Customer Service", "Expansion", "currency", "A", ["revenue from upsell and cross-sell"], "count", "up", "lagging", "Revenue from existing customers buying more."),
        ("Accounts with health score", "Sales and Customer Service", "Customers", "percent", "(A / B) * 100", ["accounts with a current health score", "active accounts"], "ratio", "up", "leading", "Share of active accounts with a health score inside the freshness window."),
        ("At risk accounts contacted", "Sales and Customer Service", "Customers", "percent", "(A / B) * 100", ["flagged accounts contacted", "accounts flagged at risk"], "ratio", "up", "leading", "Share of accounts flagged at risk that were contacted in the window."),
        ("First response time", "Sales and Customer Service", "Support", "count", "A", ["elapsed time to first response"], "count", "down", "lagging", "Elapsed time from ticket open to first response. State the percentile, not only the mean."),
        ("Resolution time", "Sales and Customer Service", "Support", "count", "A", ["elapsed time to resolution"], "count", "down", "lagging", "Elapsed time from open to resolution."),
        ("Days to close", "Finance", "Close", "count", "A", ["business days from period end to close"], "count", "down", "lagging", "Business days from period end until the books are closed."),
        ("Budgets reviewed", "Finance", "Planning", "count", "A", ["function budgets reviewed"], "count", "up", "leading", "Function budgets reviewed against the request. A process count, not the financial outcome."),
        ("Unplanned downtime", "Information Technology", "Reliability", "count", "A", ["unplanned downtime duration"], "count", "down", "lagging", "Duration of unplanned unavailability in the period."),
        ("Restore tests passed", "Information Technology", "Reliability", "count", "A", ["restore tests passed"], "count", "up", "leading", "Backup restore tests that passed the agreed check."),
        ("Critical defects", "Information Technology", "Quality", "count", "A", ["critical defects found after release"], "count", "down", "lagging", "Critical defects found after the release, on the stated severity rule."),
        ("Regressions", "Information Technology", "Quality", "count", "A", ["regressions found after release"], "count", "down", "lagging", "Behaviors that worked before the release and failed after it."),
        ("Usability score", "Management", "Discovery", "number", "A", ["mean usability score"], "survey", "up", "leading", "Mean score on the stated usability scale for the prototype or release."),
    ]
    for name, cat, sub, unit, formula, inputs, ftype, direction, timing, defn in note_measures:
        key = norm_name(name)
        generic = key in canon and any("named by" in n for n in canon[key].get("input_names", []))
        if key in canon and not generic:
            continue
        analysis, comm = charts_for(name, unit if unit in {"percent", "currency", "count", "number"} else "number")
        if generic:
            kept = canon[key]["placements"]
            canon[key].update({
                "unit": unit,
                "definition": defn + f" Placed under {cat} / {sub}.",
                "formula": formula,
                "formula_inputs": ["metric." + slug(i) for i in inputs],
                "input_names": inputs,
                "formula_type": ftype,
                "direction": direction,
                "leading_lagging": timing,
                "analysis_chart": analysis,
                "communication_chart": comm,
                "related_charts": [comm, analysis] if comm != analysis else [comm],
            })
            canon[key]["placements"] = kept
            continue
        canon[key] = {
            "id": f"kpi.{slug(cat)}.{slug(name)}",
            "name": name,
            "measure_kind": "kpi",
            "unit": unit,
            "definition": defn + f" Placed under {cat} / {sub}.",
            "formula": formula,
            "formula_inputs": ["metric." + slug(i) for i in inputs],
            "input_names": inputs,
            "formula_type": ftype,
            "direction": direction,
            "leading_lagging": timing,
            "level": "tactical",
            "audience": audiences_for(cat),
            "questions": [f"Is {name} on the desired side of its target for this period?", f"Which input moved {name}?"],
            "related_charts": [comm, analysis] if comm != analysis else [comm],
            "analysis_surface": "notebook",
            "analysis_chart": analysis,
            "communication_surface": "dashboard",
            "communication_chart": comm,
            "dashboard": f"dash.{slug(cat)}.{slug(sub)}",
            "pitfalls": "An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.",
            "target_notes": [],
            "provenance": "authored",
            "placements": [{"context": "organizational", "group": "functional", "category": cat, "subcategory": sub, "source_label": "user-note", "page": "note"}],
        }
    kpis = list(canon.values())
    metrics = {}
    for k in kpis:
        for mid, inp in zip(k["formula_inputs"], k["input_names"]):
            metrics.setdefault(mid, {"id": mid, "name": inp, "definition": f"Input used by one or more KPI formulas. {inp} is the quantity as named, with its own unit and period, before it is combined.", "unit": "as named"})
    return kpis, list(metrics.values()), exceptions


def kpi_md(k: dict) -> str:
    places = "\n".join(f"- {p['context']} / {p['group']} / {p['category']} / {p['subcategory']} ({p['source_label']}, {p['page']})" for p in k["placements"][:12])
    notes = "\n".join(f"- {n}" for n in k["target_notes"]) or "- None."
    inputs = "\n".join(f"- `{mid}` ({name})" for mid, name in zip(k["formula_inputs"], k["input_names"]))
    return f"""### {k['name']}

- id: `{k['id']}`
- kind: {k['measure_kind']}
- unit: {k['unit']}
- direction: {k['direction']}
- timing: {k['leading_lagging']}
- level: {k['level']}
- formula: `{k['formula']}`
- formula type: {k['formula_type']}
- dashboard: `{k['dashboard']}`
- analysis chart: `{k['analysis_chart']}` ({k['analysis_surface']})
- communication chart: `{k['communication_chart']}` ({k['communication_surface']})
- audiences: {", ".join(k['audience'])}
- provenance: {k['provenance']}

{k['definition']}

Questions: {k['questions'][0]}

Inputs:

{inputs}

Placements:

{places}

Target notes:

{notes}

Pitfall: {k['pitfalls']}
"""


def write_catalog(kpis: list[dict], metrics: list[dict], exceptions: list[dict]) -> None:
    CAT.mkdir(parents=True, exist_ok=True)
    with (CAT / "kpis.jsonl").open("w", encoding="utf-8") as fh:
        for k in kpis:
            fh.write(json.dumps(k, ensure_ascii=False) + "\n")
    with (CAT / "metrics.jsonl").open("w", encoding="utf-8") as fh:
        for m in metrics:
            fh.write(json.dumps(m, ensure_ascii=False) + "\n")
    grouped: dict[tuple, list] = defaultdict(list)
    for k in kpis:
        for p in k["placements"]:
            grouped[(p["context"], p["group"], p["category"], p["subcategory"])].append(k)
    for (ctx, group, cat, sub), items in grouped.items():
        # unique by id
        seen = set()
        uniq = []
        for k in items:
            if k["id"] in seen:
                continue
            seen.add(k["id"])
            uniq.append(k)
        path = LIB / "KPIS" / slug(ctx) / slug(group) / slug(cat) / f"{slug(sub)}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        body = [f"# {cat} / {sub}", "", f"Context: {ctx}. Group: {group}. KPIs: {len(uniq)}.", ""]
        body.append("Each entry is an original definition. The source label is a crosswalk, not the public id.")
        body.append("The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.")
        body.append("")
        for k in uniq:
            body.append(kpi_md(k))
        path.write_text("\n".join(body), encoding="utf-8")
    # metrics: one file per metric, grouped by first letter to keep paths short
    for m in metrics:
        letter = m["id"].split(".")[-1][:1] or "x"
        path = LIB / "METRICS" / letter / f"{m['id'].split('.',1)[1]}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"---\nid: {m['id']}\ntype: metric\n---\n\n# {m['name']}\n\n{m['definition']}\n\nUnit: {m['unit']}.\n", encoding="utf-8")
    kris = [k for k in kpis if k["measure_kind"] == "kri"]
    lines = ["# Key risk indicators", "", f"{len(kris)} indicators use `measure_kind: kri`. They are not success targets.", ""]
    for k in kris[:5000]:
        lines.append(f"- `{k['id']}` {k['name']}")
    (LIB / "KRIS" / "index.md").parent.mkdir(parents=True, exist_ok=True)
    (LIB / "KRIS" / "index.md").write_text("\n".join(lines), encoding="utf-8")
    ex_lines = ["# Inventory exceptions", "", f"Count: {len(exceptions)}.", "", "These rows were not given a formula because the name could not be read honestly.", ""]
    for e in exceptions[:2000]:
        ex_lines.append(f"- {e.get('page')} `{e.get('source_label')}` {e.get('raw','')[:80]} ({e.get('reason')})")
    if len(exceptions) > 2000:
        ex_lines.append(f"\n... {len(exceptions) - 2000} more in exceptions.jsonl")
    (INV / "exceptions.md").write_text("\n".join(ex_lines), encoding="utf-8")
    with (INV / "exceptions.jsonl").open("w", encoding="utf-8") as fh:
        for e in exceptions:
            fh.write(json.dumps(e, ensure_ascii=False) + "\n")
    (INV / "summary.md").write_text(
        f"# Inventory summary\n\nCanonical KPIs: {len(kpis)}\nMetrics: {len(metrics)}\nExceptions: {len(exceptions)}\n",
        encoding="utf-8",
    )


NOTE_OKRS = [
    ("company-grow", "Grow our corporate global business", "internal", "company", "Management", "Executive",
     [("Hit the global sales target", "revenue", "100 million currency units in the year", "up", "year"),
      ("Grow EMEA sales versus last year", "sales growth", "100 percent year over year in EMEA", "up", "year"),
      ("Increase average deal size", "average deal size", "30 percent versus last year", "up", "year"),
      ("Reduce annual churn", "customer churn rate", "under 5 percent", "down", "year")]),
    ("company-delight", "Delight our customers", "internal", "company", "Sales and Customer Service", "Executive",
     [("Interview customers each month", "customer interviews", "20 interviews per month", "up", "month"),
      ("Reach the customer NPS target", "net promoter score", "NPS 9 or the scale equivalent of a 9", "up", "quarter"),
      ("Raise retention", "customer retention", "98 percent", "up", "quarter"),
      ("Raise weekly active use", "weekly active users", "80 percent of customers active weekly", "up", "week")]),
    ("company-culture", "Build a culture people want to stay in", "internal", "company", "Human Resources", "HR",
     [("Run a weekly pulse", "employee pulse score", "8 or higher", "up", "week"),
      ("Hold a monthly town hall with open questions", "town hall held", "1 per month", "up", "month")]),
    ("mkt-mql", "Generate more marketing qualified leads", "internal", "function", "Marketing and Communications", "Marketing Analytics",
     [("MQLs from email", "marketing qualified leads", "150 from email", "up", "quarter"),
      ("MQLs from paid search", "marketing qualified leads", "100 from paid search", "up", "quarter"),
      ("MQLs from organic search", "marketing qualified leads", "50 from organic search", "up", "quarter")]),
    ("mkt-cac", "Lower the cost of acquiring a customer", "internal", "function", "Marketing and Communications", "Marketing Analytics",
     [("Reduce CAC", "customer acquisition cost", "20 percent below the prior quarter", "down", "quarter")]),
    ("mkt-abm", "Make account-based marketing a real source of revenue", "internal", "function", "Marketing and Communications", "Marketing Analytics",
     [("Closed-won sourced from ABM", "closed won rate", "20 percent of closed-won in the quarter", "up", "quarter")]),
    ("web-traffic", "Grow the site and the conversions on it", "client", "function", "Online Presence", "Marketing Analytics",
     [("Grow visitors", "website visitors", "7 percent every month", "up", "month"),
      ("Lift landing-page conversion", "landing page conversion rate", "10 percent in the quarter", "up", "quarter")]),
    ("ppc", "Keep paid search inside its efficiency limits", "client", "function", "Marketing and Communications", "Marketing Analytics",
     [("MQLs from paid search", "marketing qualified leads", "150", "up", "quarter"),
      ("Cost per lead", "cost per lead", "4 currency units or less", "down", "month"),
      ("Click-through rate", "click through rate", "2 percent or higher", "up", "month")]),
    ("seo", "Earn relevant organic demand", "client", "function", "Online Presence", "Marketing Analytics",
     [("New relevant referring domains", "referring domains", "10", "up", "quarter"),
      ("Landing pages meeting the speed budget", "pages meeting speed budget", "the agreed template set", "up", "quarter")]),
    ("newsletter", "Launch the monthly newsletter", "internal", "function", "Marketing and Communications", "Marketing Analytics",
     [("Issues published", "newsletters published", "3 this quarter, 1 per month", "up", "quarter"),
      ("Newsletter click-through", "email click through rate", "3 percent or higher", "up", "month")]),
    ("blog", "Make the blog a subscriber channel", "internal", "function", "Marketing and Communications", "Marketing Analytics",
     [("Posts published", "blog posts published", "50 in the quarter", "up", "quarter"),
      ("Expert interviews published", "expert interviews", "5", "up", "quarter"),
      ("Blog subscribers", "blog subscribers", "5000", "up", "quarter")]),
    ("pr", "Increase brand awareness through earned conversations", "internal", "function", "Marketing and Communications", "Executive",
     [("Media meetings", "media meetings", "30 by end of quarter", "up", "quarter"),
      ("Influencer meetings", "influencer meetings", "15", "up", "quarter"),
      ("Conference talks accepted", "speaking slots", "2", "up", "year")]),
    ("analysts", "Be present in the analyst conversation", "internal", "function", "Marketing and Communications", "Executive",
     [("Analyst briefings", "analyst briefings", "2 in the quarter", "up", "quarter"),
      ("Analysts hosted on webinars", "analyst webinars", "2", "up", "quarter")]),
    ("community", "Launch a customer community people actually use", "internal", "function", "Marketing and Communications", "Marketing Analytics",
     [("Community articles and visits", "community page visits", "60 articles and 6000 visits", "up", "quarter"),
      ("Customers participating", "community participation rate", "30 percent of customers", "up", "quarter")]),
    ("community-experts", "Bring recognized practitioners into the community", "internal", "function", "Marketing and Communications", "Marketing Analytics",
     [("Experts contacted", "experts contacted", "12", "up", "quarter"),
      ("Interviews published", "expert interviews", "the contacted set that agrees", "up", "quarter")]),
    ("product-mkt", "Launch the product with the materials sales can use", "internal", "function", "Marketing and Communications", "Executive",
     [("Product pages updated", "product pages shipped", "the agreed set", "up", "quarter"),
      ("Datasheets and briefs finished", "sales enablement assets", "datasheet, feature brief, and enablement pack", "up", "quarter")]),
    ("partners", "Give partners a reason to learn the product", "internal", "function", "Sales and Customer Service", "Executive",
     [("Partner papers published", "partner whitepapers", "5", "up", "quarter"),
      ("Partner webinars", "partner webinars", "7", "up", "quarter"),
      ("Partner events", "partner events", "5 cities", "up", "quarter")]),
    ("sales-pipeline", "Keep a pipeline that can hit the number", "internal", "function", "Sales and Customer Service", "Executive",
     [("Pipeline created", "pipeline created", "12 million currency units", "up", "quarter"),
      ("Coverage", "pipeline coverage", "at least 5 times quota", "corridor", "week"),
      ("Demos", "product demos", "7 per week", "up", "week")]),
    ("sales-hires", "Hire the sales roles the plan requires", "internal", "function", "Human Resources", "HR",
     [("Account executives hired", "account executives hired", "10", "up", "quarter"),
      ("SDRs hired", "sales development hires", "20", "up", "quarter"),
      ("Interview-to-offer", "interview to offer ratio", "4 to 1", "corridor", "month")]),
    ("sales-coach", "Coach the team every week", "internal", "team", "Sales and Customer Service", "Executive",
     [("Reps with a weekly coaching session", "coaching sessions", "every rep, every week", "up", "week")]),
    ("sales-region", "Grow the named region with local coverage", "internal", "team", "Sales and Customer Service", "Executive",
     [("New named accounts in the region", "new accounts", "50", "up", "quarter"),
      ("Resellers onboarded", "resellers onboarded", "10", "up", "quarter")]),
    ("sdr-sql", "Pass sales-qualified leads the closers accept", "internal", "team", "Sales and Customer Service", "Data Analytics",
     [("SQLs passed", "sales qualified leads", "80", "up", "quarter"),
      ("SDRs trained on the social motion", "sdrs trained", "5", "up", "quarter")]),
    ("upsell", "Grow revenue from customers we already have", "internal", "function", "Sales and Customer Service", "Executive",
     [("Upsell and cross-sell revenue", "expansion revenue", "40 percent above the prior period", "up", "quarter"),
      ("Retention", "customer retention", "98 percent", "up", "quarter")]),
    ("cs", "See risk before the customer leaves", "internal", "function", "Sales and Customer Service", "Data Analytics",
     [("Accounts with a health score", "accounts with health score", "every active account", "up", "week"),
      ("At-risk accounts contacted", "at risk accounts contacted", "every account flagged that week", "up", "week")]),
    ("support", "Resolve support at the standard the customer was promised", "internal", "function", "Sales and Customer Service", "Executive",
     [("Tier-1 CSAT", "customer satisfaction", "90 percent or higher", "up", "week"),
      ("Tier-1 first response", "first response time", "within 1 hour", "down", "week"),
      ("Tier-2 resolved in a day", "resolution time", "95 percent under 24 hours", "up", "week")]),
    ("finance-close", "Close the books on the calendar we promised", "internal", "function", "Finance", "Executive",
     [("Days to close", "days to close", "within 10 business days of quarter end", "down", "quarter")]),
    ("finance-budget", "Finish the budget before the year needs it", "internal", "function", "Finance", "Executive",
     [("Function budgets reviewed", "budgets reviewed", "every requesting function", "up", "quarter")]),
    ("ops-it", "Keep internal systems available", "internal", "function", "Information Technology", "Development",
     [("Unplanned downtime", "unplanned downtime", "none in the quarter", "down", "quarter"),
      ("Restore test passed", "restore tests passed", "the agreed backup test", "up", "quarter")]),
    ("eng-quality", "Ship the release without a critical regression", "internal", "function", "Information Technology", "Development",
     [("Critical bugs after release", "critical defects", "at most 1", "down", "quarter"),
      ("Regressions", "regressions", "zero", "down", "quarter")]),
    ("product-discovery", "Learn from the people who would use the product", "internal", "function", "Management", "Researcher",
     [("Discovery interviews", "customer interviews", "30", "up", "quarter"),
      ("Usability score on the prototype", "usability score", "above 8 out of 10", "up", "quarter")]),
    ("agency-leads", "Keep the agency's own lead flow ahead of the work it needs", "internal", "company", "Professional Services", "Executive",
     [("Lead to client conversion", "lead to client conversion rate", "the quarterly target", "up", "month"),
      ("Wins with a known source", "wins by lead source", "every win coded to a source", "up", "month")]),
    ("agency-delivery", "Deliver projects inside the hours and cost we quoted", "project", "team", "Portfolio and Project Management", "Executive",
     [("Hours versus estimate", "estimated versus actual project time", "at least 100, estimate over actual", "corridor", "project"),
      ("Cost versus estimate", "estimated versus actual project cost", "at least 100, estimate over actual", "corridor", "project"),
      ("Contribution margin", "project contribution margin", "the quoted margin", "up", "project")]),
    ("agency-client", "Show the client the outcome we agreed, in their numbers", "client", "function", "Marketing and Communications", "Marketing Analytics",
     [("Client ROI", "client roi", "above the agreed hurdle", "up", "quarter"),
      ("Client breakeven", "client breakeven", "reached inside the agreed window", "down", "quarter")]),
]


def find_kpi(kpis: list[dict], needle: str) -> dict | None:
    n = norm_name(needle)
    exact = [k for k in kpis if norm_name(k["name"]) == n]
    if exact:
        return exact[0]
    hits = [k for k in kpis if n and n in norm_name(k["name"])]
    if not hits:
        return None
    hits.sort(key=lambda k: (len(norm_name(k["name"])), k["id"]))
    return hits[0]


def write_okrs(kpis: list[dict]) -> None:
    by_cat = defaultdict(list)
    by_sub = defaultdict(list)
    for k in kpis:
        for p in k["placements"]:
            by_cat[p["category"]].append(k)
            by_sub[(p["category"], p["subcategory"])].append(k)
    out = LIB / "OKRS"
    index = ["# OKRs", "", "Note objectives are the density reference. Category and subcategory files cover the taxonomy.", ""]
    for oid, objective, ctx, level, function, audience, krs in NOTE_OKRS:
        resolved = []
        initiatives = []
        for statement, needle, target, direction, cadence in krs:
            hit = find_kpi(kpis, needle)
            if hit:
                resolved.append((statement, hit["id"], target, direction, cadence))
            else:
                initiatives.append(f"{statement} (no catalog KPI matched '{needle}' yet; do not treat the task as a key result)")
        if not resolved:
            continue
        path = out / "note" / f"{oid}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "---", f"id: okr.note.{oid}", "type: okr", f"context: {ctx}", f"level: {level}",
            f"function: {function}", f"audience: {audience}", "---", "",
            f"# {objective}", "",
            "Key results:", "",
        ]
        for statement, kid, target, direction, cadence in resolved:
            lines.append(f"- {statement}. KPI `{kid}`. Target: {target}. Direction: {direction}. Cadence: {cadence}.")
        if initiatives:
            lines += ["", "Initiatives (not key results):", ""]
            lines += [f"- {i}" for i in initiatives]
        lines += ["", "Anti-pattern: a key result that is only a task, or a target with no KPI id.", ""]
        path.write_text("\n".join(lines), encoding="utf-8")
        index.append(f"- note / {audience} / {ctx}: [{objective}](note/{oid}.md)")
    for cat, items in sorted(by_cat.items()):
        uniq = []
        seen = set()
        for k in items:
            if k["id"] in seen:
                continue
            seen.add(k["id"])
            uniq.append(k)
        if not uniq:
            continue
        path = out / "category" / f"{slug(cat)}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        chunks = [uniq[:3], uniq[3:6], uniq[6:9]]
        labels = ["Improve the outcome that defines this category", "Build the capability that moves that outcome", "Hold the risk that can cancel the outcome"]
        lines = [f"# {cat}", "", "Three objectives. Key results are KPIs from this category. Analysis charts stay in the notebook. Communication charts go to the dashboard.", ""]
        for i, (label, group) in enumerate(zip(labels, chunks), start=1):
            use = group or uniq[:1]
            lines.append(f"## Objective {i}. {label}")
            lines.append("")
            lines.append(f"- id: `okr.category.{slug(cat)}.{i}`")
            lines.append("- context: internal")
            lines.append("- level: function")
            lines.append(f"- audience: {', '.join(audiences_for(cat))}")
            lines.append("")
            for k in use[:3]:
                lines.append(f"- Key result: move {k['name']} ({k['direction']}). KPI `{k['id']}`. Cadence: month. Communication chart `{k['communication_chart']}`. Analysis chart `{k['analysis_chart']}`.")
            lines.append("")
        path.write_text("\n".join(lines), encoding="utf-8")
        index.append(f"- category: [{cat}](category/{slug(cat)}.md)")
    for (cat, sub), items in sorted(by_sub.items()):
        uniq = []
        seen = set()
        for k in items:
            if k["id"] in seen:
                continue
            seen.add(k["id"])
            uniq.append(k)
        path = out / "subcategory" / slug(cat) / f"{slug(sub)}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            f"# {sub}", "",
            f"Category: {cat}.",
            "",
            f"- id: `okr.sub.{slug(cat)}.{slug(sub)}`",
            "- context: internal",
            "- level: team",
            f"- audience: {', '.join(audiences_for(cat))}",
            "",
            f"## Objective. Make {sub} inside {cat} move the measures that define it",
            "",
        ]
        for k in uniq[:3]:
            lines.append(f"- Key result: {k['name']} ({k['direction']}). KPI `{k['id']}`.")
        path.write_text("\n".join(lines), encoding="utf-8")
    (out / "index.md").write_text("\n".join(index), encoding="utf-8")


def write_dashboards(kpis: list[dict]) -> None:
    grouped = defaultdict(list)
    for k in kpis:
        for p in k["placements"]:
            grouped[(p["category"], p["subcategory"], p["context"])].append(k)
    # vault templates
    vault_rows = []
    if VAULT.exists():
        for path in VAULT.rglob("*.md"):
            text = path.read_text(encoding="utf-8", errors="replace")
            if not text.startswith("---"):
                continue
            end = text.find("\n---", 3)
            fm = text[4:end] if end > 0 else ""
            title = ""
            m = re.search(r"(?m)^title:\s*[\"']?(.*?)[\"']?\s*$", fm)
            if m:
                title = m.group(1).strip()
            cat_m = re.search(r"(?m)^category:\s*(.*)$", fm)
            charts_m = re.search(r"(?m)^chart_types:\s*(.*)$", fm)
            vault_rows.append({
                "title": title or path.stem,
                "path": str(path),
                "category": cat_m.group(1).strip() if cat_m else path.parent.name,
                "charts": charts_m.group(1).strip() if charts_m else "",
            })
    by_cat_vault = defaultdict(list)
    for row in vault_rows:
        by_cat_vault[row["category"].lower()].append(row)
    dash_root = LIB / "DASHBOARDS"
    for (cat, sub, ctx), items in grouped.items():
        seen = set()
        uniq = []
        for k in items:
            if k["id"] in seen:
                continue
            seen.add(k["id"])
            uniq.append(k)
        links = []
        for row in by_cat_vault.get(cat.lower(), [])[:3]:
            links.append(f"- `{row['path']}` ({row['title']})")
        status = "linked" if links else "placeholder"
        path = dash_root / "subcategory" / slug(cat) / f"{slug(sub)}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "---",
            f"id: dash.{slug(cat)}.{slug(sub)}",
            "type: dashboard",
            f"status: {status}",
            f"category: {cat}",
            f"subcategory: {sub}",
            f"context: {ctx}",
            f"audiences: [{', '.join(audiences_for(cat))}]",
            "---",
            "",
            f"# {cat} / {sub}",
            "",
            "This card is a specification, not a claim that a live executive dashboard exists.",
            "",
            "## Questions",
            "",
            f"- Are the few outcomes in {sub} on the right side of their targets?",
            "- Which input moved, and is that a signal or a tail?",
            "",
            "## Audiences and surfaces",
            "",
            "- Communication (executive, client, HR business partner): dashboard or report. Use each KPI's communication chart.",
            "- Analysis (data scientist, researcher, R&D, marketing analytics, development): notebook or pandas/matplotlib plot. Use each KPI's analysis chart. Do not paste that figure onto the executive page unchanged.",
            "",
            "## Zones (communication)",
            "",
            "| Zone | What goes here |",
            "|---|---|",
            "| Score | Big number or bullet versus target for the OMTM of this subcategory |",
            "| Trend | Line of that KPI |",
            "| Breakdown | Sorted bar of the entities |",
            "| Variance | Waterfall or diverging bar versus plan |",
            "| Detail | Data table of the rows a person can act on |",
            "",
            "## KPIs",
            "",
        ]
        for k in uniq[:40]:
            lines.append(f"- `{k['id']}` {k['name']}. Communication `{k['communication_chart']}`. Analysis `{k['analysis_chart']}`.")
        if len(uniq) > 40:
            lines.append(f"- ... {len(uniq) - 40} more in the subcategory KPI page.")
        lines += ["", "## Vault templates", ""]
        lines += links or ["- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey)."]
        lines.append("")
        path.write_text("\n".join(lines), encoding="utf-8")
    # vault index
    vlines = ["# Vault template index", "", f"Templates indexed: {len(vault_rows)}.", "", "These are links, not copies.", ""]
    for row in vault_rows:
        vlines.append(f"- {row['category']}: {row['title']} — `{row['path']}` charts: {row['charts'][:120]}")
    (dash_root / "vault-index.md").write_text("\n".join(vlines), encoding="utf-8")
    # big book patterns
    scenarios = [
        (2, "Course metrics", "Is the cohort learning, and where is the drop?", "line-chart, bar-chart", "A small set of rates over the term, not a gallery."),
        (3, "Individual versus peers", "Where does this person sit among peers?", "dot-plot, box-plot", "Show the distribution. A rank without the spread flatters or shames."),
        (4, "What-if", "What happens to the result if one driver moves?", "kpi-tree, waterfall-chart", "The tree is the model. The waterfall is the result of one change."),
        (5, "Executive sales", "Are we on pace, and which segment explains the gap?", "line-chart, bar-chart, waterfall-chart", "Score, trend, then one breakdown."),
        (6, "Now versus then", "What changed rank since the comparison period?", "slope-chart, bump-chart", "Two times. Not a spaghetti of every month."),
        (7, "Pace to goal", "Will we land on the target if the recent rate holds?", "line-chart, bullet-graph", "Path plus target. A gauge throws the path away."),
        (8, "Several KPIs at once", "Are the few key results healthy together?", "ibcs-variance-table, bullet-graph", "A scorecard, not forty tiles."),
        (9, "Operations monitoring", "Is the process inside its corridor right now?", "run-chart, control-chart", "Technical audience may use the control chart. The shift lead may only need the run and the exceptions."),
        (10, "YTD and year ago", "How does this year compare with last year, to date?", "line-chart, diverging-bar", "Two explicit series. Do not make the reader remember."),
        (11, "Player performance", "Who is extreme, and on which measure?", "scatter-plot, bar-chart", "Analytics surface can be the scatter. Communication can be the sorted bar."),
        (12, "Match performance", "What changed during the event?", "timeline, bar-chart", "Time order of events, then the totals."),
        (13, "Web analytics", "Where does traffic become a lead?", "line-chart, funnel-chart", "Funnel only if the steps are a real sequence."),
        (14, "Patient history", "What happened to this person over time?", "timeline, line-chart", "One patient is not a population average."),
        (15, "Hotel operations", "Are occupancy, rate, and service inside plan tonight?", "bullet-graph, line-chart", "Tonight's exceptions, then the month."),
        (16, "Sentiment distribution", "Is the average hiding an angry tail?", "diverging-stacked-bar, histogram", "Show the distribution. The mean is not the story."),
        (17, "NPS with the distribution", "What sits behind the single NPS figure?", "diverging-stacked-bar, big-number", "The score for the executive, the distribution for the researcher."),
        (18, "Server monitoring", "Which process is away from its corridor?", "run-chart, horizon-chart", "Horizon is a notebook or an operator wall, not a board slide."),
        (19, "Index comparison", "How does a price compare across places?", "bar-chart, choropleth-map", "Say the base of the index."),
        (20, "Complaints", "What do people complain about, and is it growing?", "bar-chart, line-chart", "Pareto of reasons, trend of volume."),
        (21, "Utilization versus potential", "Where is capacity unused?", "bullet-graph, bar-chart", "Utilization is a corridor."),
        (22, "Rank and magnitude", "Who is first, and by how much?", "horizontal-bar-chart, lollipop-chart", "Sort by the value."),
        (23, "Many measures, many dimensions", "Which slice is different on more than one measure?", "ibcs-variance-table, heatmap", "A table with marks. Not a radar."),
        (24, "Churn", "Who left, and was it logos or revenue?", "waterfall-chart, line-chart", "Do not mix the two definitions."),
        (25, "Actual versus potential", "How far is actual from the ceiling we believe?", "bullet-graph, diverging-bar", "State what potential means."),
        (26, "Productivity", "Output per person, with the mix visible?", "bar-chart, scatter-plot", "Scatter for the analyst. Bar of the outliers for the manager."),
        (27, "Executive telecom", "Are growth, service, and network risk all visible?", "line-chart, big-number, kri list", "A KRI beside the growth KPI."),
        (28, "Economy at a glance", "What moved in the handful of macro series?", "line-chart, sparkline", "Small multiples, shared time."),
        (29, "Call center", "Are we answering, and is the queue aging?", "run-chart, bar-chart", "Service level and aging, not a gauge."),
        (30, "Personal scope", "Does this page show the viewer's own work?", "data-table, big-number", "Impersonal walls do not get action."),
        (31, "Time as time", "Is time an axis?", "line-chart", "Do not encode time only as color or a pie slice."),
        (32, "No dead end", "Can the reader reach the entity they must change?", "bar-chart, data-table", "Score without a detail zone is a dead end."),
        (33, "Not only red and green", "Can the variance be read without color?", "diverging-bar", "Sign and position carry the message."),
        (34, "Not a pie", "Is a part-to-whole being shown with angles?", "stacked-bar-chart", "Bars or a table of shares."),
        (35, "Not a cloud of bubbles", "Is area pretending to be a precise magnitude?", "scatter-plot, bar-chart", "Bubbles only when a third variable is real and the audience is analytical."),
        (36, "Unknown data", "Do we know the shape before we pick the chart?", "histogram, scatter-plot", "Look first. A dashboard template is not a finding."),
    ]
    for num, title, question, charts, why in scenarios:
        path = dash_root / "patterns" / f"{num:02d}-{slug(title)}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        kind = "practice" if num >= 30 else "scenario"
        path.write_text(
            f"---\nid: pattern.{num}\ntype: {kind}\n---\n\n# {num}. {title}\n\nQuestion: {question}\n\nCharts: {charts}.\n\nWhy: {why}\n\n"
            f"Local extract, not quoted: `{BBOOK}`.\n\n"
            "Audience split: the analytical form may be a notebook plot. The communication form is the simpler chart in the list.\n",
            encoding="utf-8",
        )
    (dash_root / "index.md").write_text(
        "# Dashboards\n\nOne specification per KPI subcategory under `subcategory/`. "
        "Pattern cards under `patterns/`. Vault links in `vault-index.md`.\n\n"
        "A dashboard is the communication surface. It is not the only output. "
        "Technical audiences keep the analysis chart in a notebook or a pandas plot.\n",
        encoding="utf-8",
    )


def write_omtm(kpis: list[dict]) -> None:
    picks = [
        ("agency", "Professional Services", "project contribution margin", "An agency principal steers on whether delivery earned the profit that was quoted."),
        ("saas", "Sales and Customer Service", "monthly recurring revenue", "A subscription business steers on recurring revenue, with churn beside it as a KRI."),
        ("ecommerce", "Retail", "conversion rate", "A store steers on conversion once traffic is a known input, not on traffic alone."),
        ("marketplace", "Retail", "liquidity", "A marketplace steers on whether both sides of the market are transacting."),
        ("professional-services", "Professional Services", "utilization rate", "Utilization is a corridor: too little and the firm is idle, too much and quality or people break."),
    ]
    out = LIB / "OMTM"
    out.mkdir(parents=True, exist_ok=True)
    lines = ["# OMTM", ""]
    for oid, cat, needle, why in picks:
        hit = find_kpi(kpis, needle)
        kid = hit["id"] if hit else "unresolved"
        path = out / f"{oid}.md"
        path.write_text(f"---\nid: omtm.{oid}\n---\n\n# {oid}\n\n{why}\n\nKPI: `{kid}`.\n\nCommunication surface: dashboard or board pack. Analysis surface: the KPI's analysis chart in a notebook.\n", encoding="utf-8")
        lines.append(f"- [{oid}]({oid}.md) `{kid}`")
    # one per industry category: first kpi
    seen = set()
    for k in kpis:
        for p in k["placements"]:
            if p["group"] != "industries" or p["category"] in seen:
                continue
            seen.add(p["category"])
            name = slug(p["category"])
            path = out / f"industry-{name}.md"
            path.write_text(
                f"---\nid: omtm.industry.{name}\n---\n\n# {p['category']}\n\n"
                f"Steering metric for this industry category: `{k['id']}` ({k['name']}). "
                "It is a starting point for selection, not a claim that every firm in the industry uses it.\n",
                encoding="utf-8",
            )
            lines.append(f"- industry [{p['category']}](industry-{name}.md)")
    (out / "index.md").write_text("\n".join(lines), encoding="utf-8")


def patch_chart_kpis(kpis: list[dict]) -> None:
    by_chart = defaultdict(list)
    for k in kpis:
        for c in k["related_charts"]:
            if len(by_chart[c]) < 8:
                by_chart[c].append(k["id"])
    for path in CHARTS.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        if not text.startswith("---"):
            continue
        ids = by_chart.get(path.stem, [])
        if not ids:
            continue
        repl = "related_kpis: [" + ", ".join(ids) + "]"
        text2, n = re.subn(r"(?m)^related_kpis:.*$", repl, text, count=1)
        if n:
            path.write_text(text2, encoding="utf-8")


def write_category_reports(kpis: list[dict]) -> None:
    cats = sorted({p["category"] for k in kpis for p in k["placements"]})
    base = {
        "Finance": "variance-report.md",
        "Accounting": "variance-report.md",
        "Sales and Customer Service": "pipeline-review.md",
        "Human Resources": "personal-review.md",
        "Information Technology": "operational-review.md",
    }
    for cat in cats:
        path = LIB / "REPORTS" / f"category-{slug(cat)}.md"
        parent = base.get(cat, "monthly-business-review.md")
        path.write_text(
            f"---\ntype: report\ncategory: {cat}\n---\n\n# {cat} review\n\n"
            f"Uses the section order of `{parent}` and the subcategory dashboards under `{cat}`.\n\n"
            "Audience decides the surface. An executive gets the communication charts and the score, trend, and variance zones. "
            "A data scientist, researcher, or developer gets the analysis charts in a notebook and brings back one sentence and one simpler chart.\n\n"
            "IBCS: message title, actual versus plan, no gauge as the message. See `library/STANDARDS/ibcs-success.md`.\n",
            encoding="utf-8",
        )


def main() -> None:
    INV.mkdir(parents=True, exist_ok=True)
    print("ocr")
    ensure_ocr()
    print("parse markdown")
    rows = parse_markdown_pages()
    state = {"context": "global", "group": "human-development", "category": "Economics", "sub": "General"}
    print("parse winocr")
    rows.extend(parse_winocr(state))
    ok = sum(1 for r in rows if r["status"] == "ok")
    print(f"rows={len(rows)} ok={ok}")
    kpis, metrics, exceptions = author(rows)
    print(f"kpis={len(kpis)} metrics={len(metrics)} exceptions={len(exceptions)}")
    write_catalog(kpis, metrics, exceptions)
    write_okrs(kpis)
    write_dashboards(kpis)
    write_omtm(kpis)
    write_category_reports(kpis)
    patch_chart_kpis(kpis)
    img_dir = INV / "page_images"
    if img_dir.exists():
        for p in img_dir.glob("*.jpg"):
            p.unlink()
    print("done")


if __name__ == "__main__":
    main()
