---
name: blog-linter
description: Lint a blog post for broken footnotes, orphaned references, malformed blockquote links, and leftover author TODO notes before publishing. Use when the user asks to lint a post, check formatting, find broken links or footnotes, run a pre-publish check, or mentions "lint this", "check my footnotes", "is this ready to publish formatting-wise".
---

<objective>
Lint blog posts to identify and highlight formatting issues that break rendering, particularly:
- Broken footnotes (references without definitions, definitions without references)
- Malformed links in blockquotes and pullquotes
- Author TODO notes in brackets (e.g., `[FIX THIS]`, `[FIND SOURCE]`, `[DATE]`)
- Inconsistent footnote numbering
- Unclosed bold/italic/code formatting

Creates a lint report and optionally highlights issues directly in the source file.
</objective>

<scope>
This skill owns FORMATTING — things that break rendering or signal the post
isn't publish-ready mechanically. Stay in that lane:

- Argument quality, evidence gaps, counterarguments → `blog-critique` owns these.
- Prose polish, voice, AI-y language, SEO → `blog-proofreader` owns these.

If something in another skill's lane catches your eye, note it in one line
under "Out of Scope" in the report and move on — don't audit it here.
</scope>

<vault_conventions>
Read `~/.claude/skills/_shared/references/vault-conventions.md`
before Step 1. Shared across all four blog skills.
</vault_conventions>

<process>
## Step 1: Resolve the Post

Resolve the input path per `<vault_conventions>`.

## Step 2: Run the Deterministic Script

The set-arithmetic parts of this skill (matching every reference to its
definition, finding gaps in a numbering sequence, scanning for bracket
patterns) are exact, mechanical work — a script does this correctly every
time; doing it by eye on a 40-footnote post risks a miscount. Run it:

```bash
python3 ~/.claude/skills/blog-linter/scripts/lint_checks.py "<resolved-path>"
```

This returns JSON with:
- `footnotes.orphan_references` / `orphan_definitions` — real errors
- `footnotes.duplicate_definitions` — real error (same label defined twice)
- `footnotes.reused_references_info` — NOT an error, see Step 3
- `footnotes.numbering_gaps` — warning, may be intentional
- `todo_note_candidates` — candidate author TODO notes, needs your judgment
- `wikilinks` — informational list, no existence checking
- `blockquote_link_candidates` — candidate rendering issues, needs your judgment
- `formatting_issues` — unclosed bold/italic/code fence (best-effort; italics
  detection in particular is low-confidence — the script says so per-item)

## Step 3: Apply Judgment to the Candidates

This is the part regex can't decide — this is your actual job on this skill:

- **`todo_note_candidates`**: almost always real TODO notes, but confirm each
  isn't legitimate bracketed content the regex couldn't distinguish (rare —
  the script already excludes wikilinks, markdown links, and footnote refs).
- **`blockquote_link_candidates`**: decide whether each will actually break
  in Obsidian rendering vs. render fine. Say "check in preview" rather than
  asserting certainty either way — you can't render Markdown to verify.
- **`reused_references_info`**: same footnote cited more than once in the
  text is valid Markdown. Mention as FYI only, never list it as an error.
- **HTML-commented-out footnote syntax** (`<!-- [^1] -->`): the script
  doesn't exclude these. If you see one in the surrounding context, don't
  flag it — it's intentionally disabled, not broken.
- **Footnote labels that are words, not numbers** (`[^note1]`): valid. The
  script's numbering-gap check only looks at purely numeric labels, so
  these never trigger a false gap — no action needed from you here.
- **Caps-marker-plus-colon brackets** (e.g. `[TOD: fix this later]`,
  `[NOTE: check with source]`): intentionally NOT flagged. Carey uses this
  notation deliberately and manages these notes herself — the script's
  narrow all-caps-only TODO regex is a design decision she confirmed
  (2026-07-19), not a gap. Don't flag them manually and don't widen the regex.
- **Bare Substack URLs in parens on their own line** (e.g.
  `(https://insights.priva.cat/p/...)`, no `[text](...)` wrapper): this is
  an intentional artifact of the Obsidian→Substack conversion — Substack
  auto-handles links to its own hosted content on import. Do not flag as a
  malformed link. Links to non-Substack sources still need proper Markdown
  form and should still be checked normally.

## Step 4: Create Lint Report

Write to `<post-folder>/<post-slug>-lint-report.md` per `<vault_conventions>`.

Use the structure in `references/lint-report-template.md`. Read that file
when you reach this step — not before. Fill it from the script's JSON plus
your Step 3 judgment calls. Only include sections that actually have
findings — don't pad the report with empty categories.

## Step 5: Optional — Highlight Issues in Source

Ask: "Want a copy with issues highlighted using `==highlight==` syntax?"

If yes:
- Create `<post-slug>-highlighted.md` in the same post folder
- Wrap TODO notes: `==[FIX THIS]==`
- Wrap problematic footnote references: `==[^5]==`
- Wrap problematic links: `==[Link text](url)==`
- Add inline comments: `<!-- LINT: Missing footnote definition -->`

Report both file paths to the user.
</process>

<key_reminders>
1. **Run the script before doing anything else** — don't hand-count footnotes.
2. **The script gives candidates, not verdicts** — Step 3 is real work, not a formality.
3. **Distinguish errors vs warnings** — orphaned footnotes are errors, numbering gaps are warnings, reused references are FYI.
4. **Don't auto-fix without permission** — ask before modifying the source file.
5. **TODO notes are high priority** — surface these first in the report; they mean "not ready to publish."
6. **Stay in your lane** — formatting only; see `<scope>`.
</key_reminders>
</content>
