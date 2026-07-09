# Library verification protocol

How a chart-library entry earns `status: verified` (IMP-F02). The curator
(`chart-expert/agents/library-curator.md`) executes this; no other path may
flip a status field.

1. **Render with a fixture.** Build a small inline fixture dataset matching
   the entry's `input_type` (no external files) and run the tool-specific
   snippet end-to-end.
2. **Confirm the artifact.** The render must complete without an exception
   AND produce a non-empty output file (size > 0). A render that raises, or
   produces a 0-byte artifact, must NOT flip status — report the failure
   instead.
3. **Capture the snippet.** Commit the exact script that ran under
   `chart-expert/library/_SNIPPETS/<entry>_<tool>.py` (generalized column
   names, inline fixture, self-contained). Align the entry's
   `Implementation Notes.<tool>` section with the committed snippet so the
   two never diverge.
4. **Flip the stanza.** Set the entry's front-matter stanza for that tool to
   `{status: verified, source_file: "<snippet path>", last_iterated: <ISO date>}`.
   Other tools' stanzas are untouched.
5. **Regenerate the index.** Update
   `chart-expert/library/_INDICES/verification-index.md` (per-tool
   verified/total counts) in the same change as any status flip — a flip
   without an index regeneration is an inconsistent state.

Verification order follows `chart-expert/library/_INDICES/priority-forms.md`
(the chart forms actually used by decision-analytics-reconstruction,
matplotlib first).
