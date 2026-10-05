---
id: IMP-F04
title: "Repository hygiene: delete superseded trees, single-source duplicated references, index design history"
absorbs: [CF6, CF7]
overlaps_triage: []
priority: P2
effort: low
depends_on: []
soft_depends_on: []
queue: issues
target_repo: Chart_Audit_Framework
issue: 4
status: filed
---

# IMP-F04 — Repository Hygiene

The repo carries three generations of the same material side by side, plus
crawl debris:

1. **Byte-identical superseded trees (CF6).** `OLD-chart-audit/` and
   `_legacy/` are the pre-reorg archive, archived twice: every file `_legacy`
   contains is byte-identical to its `OLD-chart-audit` counterpart
   (`_legacy` merely lacks `code-smells.md`), and `code-smells.md` itself is
   byte-identical between `OLD-chart-audit/` and the live
   `chart-audit/references/`. Nothing in the active skills references either
   directory (repo history: 4 commits; the latest reorganized legacy docs
   into the current `chart-audit/` + `chart-expert/` layout).
2. **Duplicated reference pair (CF6).**
   `Deterministic_Data_Visualization_Framework/Chart_library/DataInputTypes_Schema.md`
   and `Complete_Input_Type_Inventory.md` are byte-identical to
   `chart-expert/references/input-type-schema.md` and
   `input-type-inventory.md` (431/447 lines). No symlink or generation
   script ties the copies together — editing one silently strands the other.
   The `Deterministic_Data_Visualization_Framework/` prototype's delivery
   mechanism (Obsidian vault per its `SETUP_GUIDE.md`) is superseded by the
   skill layout.
3. **Crawl debris (CF6).** The scraped site mirrors under
   `Deterministic_Data_Visualization_Framework/references/` include
   indiscriminate WordPress internals (woocommerce assets,
   cleantalk-spam-protect and stop-user-enumeration JS) with zero
   chart-methodology content, plus a stray binary macOS alias file
   (`Deterministic_Data_Visualization_Framework/AI alias`).
4. **Orphaned design history (CF7).** `OLD-chart-audit/GPT Chart Audit
   Mode.md` (477 lines, the original bottom-up monolithic prompt) and
   `OLD-chart-audit/Reverse_order.md` (371 lines — the design note that
   diagnosed bottom-up auditing as backwards and motivated today's
   top-down gate ordering) explain *why* the current methodology is shaped
   as it is, but no active `SKILL.md` points to them.

## 1. Define the Scope (The Data Guardrails)

**In-Scope:**
- Deletion of `OLD-chart-audit/` and `_legacy/` in full — with the two
  design-history documents (`GPT Chart Audit Mode.md`, `Reverse_order.md`)
  relocated first to `docs/design-history/`, and a "why the gates are
  ordered top-down" pointer added to `chart-audit/SKILL.md`.
- Single-sourcing the duplicated reference pair: the
  `Deterministic_Data_Visualization_Framework/Chart_library/` copies of the
  two byte-identical files are deleted; `chart-expert/references/` remains
  the only copy. The rest of `Chart_library/` (catalogue template, setup
  guide, catalogue docs) is either retained with a header note marking it
  as the historical prototype or moved under `docs/design-history/` — one
  decision, applied consistently and recorded in the PR.
- Deletion of the non-content crawl paths (WordPress plugin/theme/commerce
  assets) under the four site mirrors, and of the `AI alias` binary. The
  actual chart-content pages (the ~130 per-chart pages the library was
  generated from, plus curated images/PDFs) are retained.
- A hygiene invariant documented in the PR: zero byte-identical duplicate
  file pairs across the repo; no binary alias files; no scraped
  plugin/theme assets.

**Out-of-Scope:**
- Any change to the live `chart-audit/` and `chart-expert/` skill content
  (IMP-F01/F02 own those).
- The chart library's verification statuses (IMP-F02).
- Git-history rewriting — deletions are ordinary commits; history retains
  the old trees.

## 2. Data-Driven "Given-When-Then" Scenarios

**Scenario: Post-cleanup tree (Happy Path)**
- **Given** the cleanup commit,
- **When** the repo tree is listed,
- **Then** `OLD-chart-audit/` and `_legacy/` do not exist,
  `docs/design-history/` contains the two relocated documents, and
  `chart-audit/SKILL.md` contains a working relative link to the
  design-history rationale.

**Scenario: Duplicate scan (Happy Path)**
- **Given** the post-cleanup tree,
- **When** a content-hash duplicate scan runs across all tracked text files,
- **Then** it reports zero byte-identical pairs between different
  directories (the CF6 condition), and specifically
  `chart-expert/references/input-type-schema.md` and
  `input-type-inventory.md` each exist exactly once in the repo.

**Scenario: Reference-integrity after deletion (Edge Case)**
- **Given** the deletions,
- **When** every markdown link and path reference in the active skill trees
  (`chart-audit/`, `chart-expert/`) is resolved,
- **Then** none points into a deleted path — the cleanup may not orphan any
  live reference (verified by a link check across the two active trees).

## 3. Specify Undesirable Behaviors (Negative Constraints)

**Scenario: Preventing archive-by-copy recurrence**
- **Given** any future reorganization of the skills,
- **When** content is superseded,
- **Then** it is deleted (git history is the archive) or moved to
  `docs/design-history/` once — never left as a sibling copy of the live
  tree; two directories claiming to be the methodology is the exact
  cross-artifact-contradiction smell (Smell M) this framework audits for in
  others.

**Scenario: Preventing silent loss of the design rationale**
- **Given** the deletion of `OLD-chart-audit/`,
- **When** the cleanup PR is assembled,
- **Then** the two design-history documents must appear at their new path
  in the same commit that deletes the old one (move, not delete-then-maybe-
  restore) — the rationale for the gate ordering is preserved with
  continuity.

**Scenario: Preventing over-deletion of source material**
- **Given** the crawl-debris deletion,
- **When** paths are selected for removal,
- **Then** only asset/plugin/theme paths with no chart content are removed;
  the per-chart content pages the library entries cite as provenance remain
  — IMP-F02's verification loop needs them.

## 4. Detail Data-Specific Non-Functional Requirements

- **Model fairness / bias:** N/A — repository hygiene.
- **Performance & decay:** repo size reduction recorded in the PR
  description (before/after `du` of the deleted trees); clone/checkout time
  is the only performance surface.
- **Data integrity:** the PR description lists every deleted top-level path
  and every moved file with old → new mapping; the link check across active
  trees passes.
- **Reproducibility:** the duplicate scan and link check are re-runnable
  commands documented in the PR so the hygiene condition can be re-verified
  at any later commit.

## 5. Queue Stub (ready to file)

**GitHub issue body:**

> **Title:** Repo hygiene: delete OLD-chart-audit/ and _legacy/, single-source duplicated references, relocate design history, strip crawl debris (IMP-F04)
>
> **Problem.** Three generations of the methodology coexist:
> `OLD-chart-audit/` and `_legacy/` are byte-identical pre-reorg archives
> unreferenced by any active skill;
> `Deterministic_Data_Visualization_Framework/Chart_library/` duplicates two
> `chart-expert/references/` files byte-for-byte with no generation link;
> the site mirrors include WordPress plugin/commerce assets and a stray
> macOS `AI alias` binary. The design-history docs that explain the
> top-down gate ordering (`GPT Chart Audit Mode.md`, `Reverse_order.md`)
> are stranded in the tree slated for deletion.
>
> **Acceptance criteria.**
> 1. `OLD-chart-audit/` and `_legacy/` deleted; the two design-history docs
>    moved to `docs/design-history/` in the same commit; pointer added to
>    `chart-audit/SKILL.md`.
> 2. Duplicated reference pair single-sourced under
>    `chart-expert/references/`; prototype `Chart_library/` retained-with-
>    header or moved to design-history (one decision, recorded).
> 3. Plugin/theme/commerce crawl assets and the `AI alias` binary deleted;
>    per-chart content pages retained.
> 4. Duplicate-pair scan: zero byte-identical cross-directory pairs; link
>    check across `chart-audit/` + `chart-expert/`: zero dangling paths.
> 5. PR lists deleted paths, moves (old→new), and size reduction.
>
> **Spec:** `Chart_Audit_Framework/improvement_plan/IMP-F04_repo-hygiene.md`

Labels: `type:refactor`, `skill:infra`, `effort:low`, `priority:p2`,
`status:claude-ready`
