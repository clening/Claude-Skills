# Lint Report Template

Fill from the script's JSON plus your Step 3 judgment calls. Omit sections
with no findings — don't include empty headers.

```markdown
---
title: Lint Report
date: [YYYY-MM-DD from `date +%Y-%m-%d`]
source: [filename]
issues: [count]
---

# Lint Report: [Post Title]

**Source:** `[path]`
**Total Issues:** [count]

## Summary
- 🔴 [X] footnote issues
- 🔴 [X] author TODO notes remaining
- 🟡 [X] blockquote links to check in preview
- 🟡 [X] formatting warnings

---

## Author TODO Notes (Remove Before Publishing!)

#### Line [N]: `[TEXT]`
```
[context from the script]
```

---

## Footnote Issues

### Orphaned References (in text, no definition)
#### `[^N]` — Line [N]
**Fix:** Add footnote definition or remove reference.

### Orphaned Definitions (defined but not referenced)
#### `[^N]` — Line [N]
**Fix:** Remove definition or add reference in text.

### Duplicate Definitions
#### `[^N]` defined [X] times — Lines [...]
**Fix:** Keep one, remove the other(s).

### Numbering Gaps (warning, may be intentional)
**Sequence:** [...] **Missing:** [...]

---

## Blockquote Links to Verify

#### Line [N]
```markdown
[context]
```
**Assessment:** [your judgment — likely fine / check in preview / restructure]

---

## Formatting Warnings
[unclosed bold/italic/code fence, if any — note italics is low-confidence]

---

## Out of Scope (noted, not audited)
[Anything belonging to blog-critique or blog-proofreader — one line each.]

## What You Can Ask Claude Code to Do
- "Highlight all issues with ==syntax==" — creates a highlighted copy
- "Renumber footnotes sequentially" — fixes numbering gaps
- "Remove orphaned footnotes" — deletes unused definitions

These require explicit requests — this report is read-only.
```
</content>
