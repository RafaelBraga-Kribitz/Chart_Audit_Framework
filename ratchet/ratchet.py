#!/usr/bin/env python3
"""Cross-repo audit ratchet (IMP-F03 / issue #3).

Reads a decision-analytics-reconstruction checkout's FIGURE_MANIFEST.yaml and
findings state, then routes every chart id to one of:

  skip         unchanged generator, previously clean — no work
  verify-only  covered by a closed finding — its verification_script is the
               authority; run it (regression check) instead of re-auditing
  full-audit   new chart or generator content changed since the last run —
               needs a fresh audit pass (rule engine where detectors exist,
               chart-adversary LLM layers otherwise; no detectors are
               implemented yet, so rows carry the ``llm-judged`` marker)

The ratchet is strictly read-only against the target checkout. State lives in
``ratchet/state.json`` (per chart: generator hash, verdict, rule-versions
hash, target commit) so consecutive runs are incremental. A run against a
target commit that is an ancestor of the recorded one aborts unless
``--rewind`` is passed.

Exit codes: 0 = ran, no regressions; 1 = >=1 closed-finding REGRESSION;
2 = input/manifest error (unsupported schema_version, missing manifest,
mapping-table schema violation, backwards run without --rewind).

Usage:
  python3 ratchet/ratchet.py <target_checkout> [--state PATH] [--report PATH]
                             [--no-verify] [--rewind]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover
    sys.stderr.write("ratchet: pyyaml is required (pip install pyyaml)\n")
    sys.exit(2)

SUPPORTED_SCHEMA_VERSIONS = {1}
HERE = Path(__file__).resolve().parent
DEFAULT_STATE = HERE / "state.json"
DEFAULT_MAP = HERE / "finding_chart_map.yaml"
RULES_MANIFEST = HERE.parent / "rules" / "manifest.yaml"


def _fail(msg: str) -> "NoReturn":  # type: ignore[name-defined]
    sys.stderr.write(f"ratchet: {msg}\n")
    sys.exit(2)


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _git_head(target: Path) -> str:
    out = subprocess.run(
        ["git", "-C", str(target), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=False,
    )
    return out.stdout.strip() if out.returncode == 0 else "unknown"


def _is_ancestor(target: Path, maybe_ancestor: str, of: str) -> bool:
    out = subprocess.run(
        ["git", "-C", str(target), "merge-base", "--is-ancestor", maybe_ancestor, of],
        capture_output=True,
        check=False,
    )
    return out.returncode == 0


def load_manifest(target: Path) -> dict:
    path = target / "governance" / "FIGURE_MANIFEST.yaml"
    if not path.is_file():
        _fail(f"manifest not found: {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    version = data.get("schema_version")
    if version not in SUPPORTED_SCHEMA_VERSIONS:
        _fail(
            f"unsupported/absent FIGURE_MANIFEST schema_version {version!r} "
            f"(supported: {sorted(SUPPORTED_SCHEMA_VERSIONS)}) — refusing a "
            "possibly-misparsed partial audit"
        )
    return data


def load_findings_state(target: Path) -> dict[str, dict]:
    findings = {}
    for f in sorted((target / "governance" / "findings").glob("F-*.yaml")):
        if f.name == "F-TEMPLATE.yaml":
            continue
        d = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        if d.get("id"):
            findings[d["id"]] = d
    if not findings:
        _fail("no findings found in target checkout")
    return findings


def load_mapping(findings: dict[str, dict]) -> dict[str, list[str]]:
    """chart_id -> [finding ids]; schema-checked against the target's findings."""
    if not DEFAULT_MAP.is_file():
        _fail(f"mapping table missing: {DEFAULT_MAP}")
    raw = yaml.safe_load(DEFAULT_MAP.read_text(encoding="utf-8")) or {}
    mapping: dict[str, list[str]] = raw.get("charts", {})
    for chart_id, fids in mapping.items():
        for fid in fids:
            if fid not in findings:
                _fail(
                    f"mapping table names {fid} (chart {chart_id}) which does "
                    "not exist in the target checkout — fix the table, do not guess"
                )
    return mapping


def rule_versions_hash() -> str:
    if RULES_MANIFEST.is_file():
        return _sha256_file(RULES_MANIFEST)[:12]
    return "no-rules-manifest"


_VERIFY_CACHE: dict[str, tuple[bool, str]] = {}


def run_verification(target: Path, script: str) -> tuple[bool, str]:
    if script in _VERIFY_CACHE:
        return _VERIFY_CACHE[script]
    proc = subprocess.run(
        ["poetry", "run", "python", script],
        cwd=str(target),
        capture_output=True,
        text=True,
        check=False,
    )
    tail = (proc.stdout + proc.stderr).strip().splitlines()
    result = (proc.returncode == 0, tail[-1] if tail else "")
    _VERIFY_CACHE[script] = result
    return result


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("target", type=Path)
    ap.add_argument("--state", type=Path, default=DEFAULT_STATE)
    ap.add_argument("--report", type=Path, default=None)
    ap.add_argument(
        "--no-verify",
        action="store_true",
        help="route only; do not execute the target's verification scripts",
    )
    ap.add_argument(
        "--rewind",
        action="store_true",
        help="acknowledge auditing an older target commit than the recorded state",
    )
    args = ap.parse_args()
    target = args.target.resolve()

    manifest = load_manifest(target)
    findings = load_findings_state(target)
    mapping = load_mapping(findings)
    rv_hash = rule_versions_hash()
    head = _git_head(target)

    state = {}
    if args.state.is_file():
        state = json.loads(args.state.read_text(encoding="utf-8"))
        prev = state.get("target_commit")
        if (
            prev
            and prev not in ("unknown", head)
            and head != "unknown"
            and _is_ancestor(target, head, prev)
            and not args.rewind
        ):
            _fail(
                f"target HEAD {head[:12]} is an ancestor of the recorded state "
                f"commit {prev[:12]} — pass --rewind to ratchet backwards deliberately"
            )

    charts = state.get("charts", {})
    rows: list[dict] = []
    regressions = 0
    full_audits = 0

    for fig in manifest.get("figures", []):
        chart_id = fig["chart_id"]
        gen_path = target / fig["generator"]
        gen_hash = _sha256_file(gen_path)[:16] if gen_path.is_file() else "missing-generator"
        prev_entry = charts.get(chart_id, {})
        covering = mapping.get(chart_id, [])
        closed_covering = [
            f for f in covering if findings[f].get("status") in ("closed", "closed_historical")
        ]

        if gen_hash == "missing-generator":
            route, detail = "manifest-defect", f"generator missing: {fig['generator']}"
        elif closed_covering:
            route = "verify-only"
            details = []
            for fid in closed_covering:
                script = findings[fid].get("verification_script")
                if not script:
                    details.append(f"{fid}: closed_historical (no script)")
                    continue
                if args.no_verify:
                    details.append(f"{fid}: {script} (not executed, --no-verify)")
                    continue
                ok, line = run_verification(target, script)
                if ok:
                    details.append(f"{fid}: PASS")
                else:
                    details.append(
                        f"REGRESSION of {fid}: {line} — reopen per the target's "
                        "AUDIT_PROCEDURE.md; the ratchet files no duplicate issue"
                    )
                    regressions += 1
            detail = "; ".join(details)
        elif prev_entry.get("generator_hash") == gen_hash and prev_entry.get(
            "rule_versions"
        ) == rv_hash:
            route, detail = "skip", "unchanged since last ratchet run"
        else:
            route = "full-audit"
            detail = (
                "new or changed generator — audit via chart-adversary "
                "(llm-judged: no detectors implemented yet, rules manifest "
                f"{rv_hash})"
            )
            full_audits += 1

        rows.append(
            {
                "chart_id": chart_id,
                "route": route,
                "generator_hash": gen_hash,
                "rule_ids": closed_covering or ["llm-judged"],
                "detail": detail,
            }
        )
        charts[chart_id] = {
            "generator_hash": gen_hash,
            "verdict": route,
            "rule_versions": rv_hash,
        }

    new_state = {
        "target_commit": head,
        "run_date": str(date.today()),
        "rule_versions": rv_hash,
        "charts": charts,
    }
    args.state.parent.mkdir(parents=True, exist_ok=True)
    args.state.write_text(json.dumps(new_state, indent=2) + "\n", encoding="utf-8")

    n_skip = sum(1 for r in rows if r["route"] == "skip")
    n_verify = sum(1 for r in rows if r["route"] == "verify-only")
    summary = (
        f"charts={len(rows)} skip={n_skip} verify-only={n_verify} "
        f"full-audit={full_audits} regressions={regressions} target={head[:12]}"
    )
    report_lines = [f"# Ratchet report — {date.today()}", "", summary, ""]
    if full_audits == 0 and regressions == 0:
        report_lines.append("No deltas: no full audits required, no regressions.")
    for r in rows:
        if r["route"] != "skip":
            report_lines.append(
                f"- `{r['chart_id']}` [{r['route']}] rules={','.join(r['rule_ids'])}: {r['detail']}"
            )
    report = "\n".join(report_lines) + "\n"
    if args.report:
        args.report.write_text(report, encoding="utf-8")
    print(report)
    return 1 if regressions else 0


if __name__ == "__main__":
    sys.exit(main())
