# -*- coding: utf-8 -*-
"""chart-audit-rules: the deterministic rule layer's single CI entry point (IMP-F01).

    python rules/chart_audit_rules.py <chart_path> <code_path>
        [--manifest rules/manifest.yaml]
        [--data table.csv --group-col G --metric-col M]          # Smell B
        [--interval-labels labels.yaml]                           # Smell C
        [--expected-categories exp.txt --plotted-categories plot.txt]  # Smell J
        [--json]

    python rules/chart_audit_rules.py --check-manifest

Exit codes (rules/cli-spec.md): 0 = every executed detector clean (skips are
reported, never counted as clean); 1 = at least one detector fired; 2 = input
or manifest error. LLM-judged rules are out of scope for this process.
Requires PyYAML.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Callable

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from detectors import DETECTORS, DetectorInputError, Finding  # noqa: E402

RULES = Path(__file__).resolve().parent
REPO = RULES.parent
ENFORCEMENT = {"detector-backed", "llm-judged-only"}


class ManifestError(ValueError):
    """rules/manifest.yaml (or the coverage matrix) is inconsistent (exit code 2)."""


def load_manifest(path: Path) -> list[dict]:
    """Load and validate the rule registry; raise ManifestError on any defect."""
    rules = (yaml.safe_load(path.read_text(encoding="utf-8")) or {}).get("rules") or []
    ids = [r.get("id") for r in rules]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        raise ManifestError(f"duplicate rule ids: {dupes}")
    for rule in rules:
        if rule.get("enforcement") not in ENFORCEMENT:
            raise ManifestError(f"{rule.get('id')}: unknown enforcement {rule.get('enforcement')!r}")
        if rule["enforcement"] != "detector-backed":
            continue
        detector = rule.get("detector") or {}
        spec = REPO / str(detector.get("spec", ""))
        if not detector.get("spec") or not spec.is_file():
            raise ManifestError(f"{rule['id']}: detector spec {detector.get('spec')!r} missing")
        if detector.get("function") not in DETECTORS:
            raise ManifestError(f"{rule['id']}: detector {detector.get('function')!r} is not implemented")
    return rules


def check_coverage_matrix(rules: list[dict], matrix: Path) -> None:
    """The coverage matrix must list exactly the manifest's ids with the same enforcement."""
    rows = re.findall(r"^\| ((?:SMELL|GATE)-[A-Z]) \|[^|]*\| ([a-z-]+) \|", matrix.read_text(encoding="utf-8"), re.M)
    in_matrix = dict(rows)
    in_manifest = {r["id"]: r["enforcement"] for r in rules}
    if in_matrix != in_manifest:
        drift = sorted(set(in_matrix.items()) ^ set(in_manifest.items()))
        raise ManifestError(f"COVERAGE_MATRIX.md disagrees with manifest.yaml: {drift}")


def _read_lines(path: str) -> list[str]:
    return [ln.strip() for ln in Path(path).read_text(encoding="utf-8").splitlines() if ln.strip()]


def _run_b(args: argparse.Namespace) -> list[Finding] | None:
    if not args.data:
        return None
    if not (args.group_col and args.metric_col):
        raise DetectorInputError("--data requires --group-col and --metric-col")
    with open(args.data, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return [DETECTORS["detect_flat_distribution"](rows, args.group_col, args.metric_col)]


def _run_c(args: argparse.Namespace) -> list[Finding] | None:
    if not args.interval_labels:
        return None
    entries = yaml.safe_load(Path(args.interval_labels).read_text(encoding="utf-8")) or []
    if not isinstance(entries, list) or not entries:
        raise DetectorInputError("--interval-labels must be a non-empty YAML/JSON list")
    keys = ("declared_label", "computed_low", "computed_high", "quantile_low", "quantile_high")
    out = []
    for e in entries:
        missing = [k for k in keys if k not in e]
        if missing:
            raise DetectorInputError(f"interval entry missing {missing}: {e!r}")
        out.append(DETECTORS["detect_interval_mislabel"](str(e["declared_label"]), *(float(e[k]) for k in keys[1:])))
    return out


def _run_j(args: argparse.Namespace) -> list[Finding] | None:
    if not args.expected_categories:
        return None
    if not args.plotted_categories:
        raise DetectorInputError("--expected-categories requires --plotted-categories")
    expected, plotted = _read_lines(args.expected_categories), _read_lines(args.plotted_categories)
    return [DETECTORS["detect_dropped_categories"](expected, plotted)]


RUNNERS: dict[str, Callable[[argparse.Namespace], list[Finding] | None]] = {
    "detect_flat_distribution": _run_b,
    "detect_interval_mislabel": _run_c,
    "detect_dropped_categories": _run_j,
}


def _parse(argv: list[str] | None) -> argparse.Namespace:
    p = argparse.ArgumentParser(prog="chart-audit-rules", description=__doc__.split("\n")[0])
    p.add_argument("chart_path", nargs="?")
    p.add_argument("code_path", nargs="?")
    p.add_argument("--manifest", default=str(RULES / "manifest.yaml"))
    p.add_argument("--check-manifest", action="store_true", help="validate manifest + coverage matrix only")
    p.add_argument("--data")
    p.add_argument("--group-col")
    p.add_argument("--metric-col")
    p.add_argument("--interval-labels")
    p.add_argument("--expected-categories")
    p.add_argument("--plotted-categories")
    p.add_argument("--json", action="store_true", help="emit findings as JSON lines")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse(argv)
    try:
        rules = load_manifest(Path(args.manifest))
        check_coverage_matrix(rules, RULES / "COVERAGE_MATRIX.md")
    except (ManifestError, OSError, yaml.YAMLError) as exc:
        print(f"[ERROR] manifest: {exc}", file=sys.stderr)
        return 2
    if args.check_manifest:
        backed = sum(r["enforcement"] == "detector-backed" for r in rules)
        print(f"[PASS] manifest: {len(rules)} rules, {backed} detector-backed, all implemented")
        return 0
    for name in ("chart_path", "code_path"):
        value = getattr(args, name)
        if not value or not Path(value).exists():
            print(f"[ERROR] {name} {value!r} does not exist", file=sys.stderr)
            return 2
    ran = fired = skipped = 0
    for rule in (r for r in rules if r["enforcement"] == "detector-backed"):
        try:
            findings = RUNNERS[rule["detector"]["function"]](args)
        except (DetectorInputError, OSError, yaml.YAMLError, ValueError) as exc:
            print(f"[ERROR] {rule['id']}: {exc}", file=sys.stderr)
            return 2
        if findings is None:
            skipped += 1
            print(f"[SKIP] {rule['id']}: required inputs not supplied")
            continue
        for f in findings:
            ran += 1
            fired += f.fired
            if args.json:
                print(json.dumps({"rule": rule["id"], **f.as_dict()}, sort_keys=True))
            else:
                print(f"[{'FIRED' if f.fired else 'CLEAN'}] {rule['id']}: {f.evidence}")
    print(f"ran={ran} fired={fired} skipped={skipped}")
    return 1 if fired else 0


if __name__ == "__main__":
    sys.exit(main())
