---
name: blog-linter
description: Lints blog posts for broken footnotes, orphaned references, malformed links (especially in blockquotes), and author TODO notes. Highlights issues with Obsidian syntax and creates a detailed report.
---

<objective>
Lint blog posts to identify and highlight formatting issues that break rendering, particularly:
- Broken footnotes (references without definitions, definitions without references)
- Malformed links in blockquotes and pullquotes
- Author TODO notes in brackets (e.g., [FIX THIS], [FIND SOURCE])
- Inconsistent footnote numbering
- Other markdown formatting issues that cause rendering problems

Creates a lint report and optionally highlights issues directly in the source file.
</objective>

<common_issues>
The most frequent problems in Obsidian markdown blog posts:

1. **Orphaned footnote references**: `[^5]` in text but no `[^5]: definition` at bottom
2. **Orphaned footnote definitions**: `[^3]: definition` at bottom but no `[^3]` reference in text
3. **Malformed links in blockquotes**: When you indent (pullquote) and include a link, it renders as:
   ```
   > "quoted thing" [Foo bar](https://website.com)
   ```
   Instead of properly rendering the HTML link
4. **Author TODO notes**: Bracketed reminders like `[FIX THIS]`, `[FIND SOURCE FOR THIS]`, `[CUT????]`, `[VERIFY]`, etc.
5. **Inconsistent footnote numbering**: Gaps in sequence (1, 2, 5, 7 instead of 1, 2, 3, 4)
6. **Duplicate footnote numbers**: Multiple `[^3]` references or definitions
7. **Broken wikilinks**: `[[Page That Doesn't Exist]]`
8. **Unclosed formatting**: Unclosed bold `**text`, italics `*text`, or code blocks
</common_issues>

<process>
## Step 1: Get the File

If args provided:
- First arg is the path to the blog post file
- If path doesn't include full vault path, prepend: `/mnt/c/Users/carey/Documents/SyncVaultC/Blog Ideas and Posts/`

If no args:
- Ask user for the file path

Use Read tool to read the entire file.

## Step 2: Analyze for Issues

Scan the file and identify:

### A. Footnote Issues

**Find all footnote references** in the text (format: `[^number]` or `[^label]`)
- Extract the number/label
- Note line numbers where they appear

**Find all footnote definitions** at bottom (format: `[^number]: text`)
- Extract the number/label
- Note line numbers where they appear

**Compare and identify:**
1. **Orphaned references**: References in text with no definition at bottom
2. **Orphaned definitions**: Definitions at bottom with no reference in text
3. **Duplicate references**: Same `[^n]` appears multiple times in text
4. **Duplicate definitions**: Same `[^n]:` appears multiple times at bottom
5. **Numbering gaps**: Non-sequential numbering (e.g., 1, 2, 5, 8)

### B. Author TODO Notes

**Find bracketed notes** that are reminders to fix/verify/cut content:
- Pattern: `\[([A-Z\s?!]+)\]` - matches things like:
  - `[FIX THIS]`
  - `[FIND SOURCE FOR THIS]`
  - `[CUT????]`
  - `[VERIFY]`
  - `[TODO]`
  - `[CHECK THIS]`
  - `[NEEDS WORK]`
- Note line numbers
- Extract the note text

**Exclude false positives:**
- Don't flag markdown links: `[text](url)` - has parentheses after
- Don't flag footnote references: `[^1]` - starts with caret
- Don't flag wikilinks: `[[Page]]` - double brackets
- Don't flag normal bracketed text that isn't all-caps or doesn't contain question marks

### C. Link Issues

**Find malformed links in blockquotes:**
- Pattern: `> ` followed by text and `[text](url)` on same line or next line
- These often don't render properly when the blockquote is indented
- Check if link is inside quotes or immediately after closing quote

**Find potentially broken wikilinks:**
- Pattern: `[[Page Name]]`
- Optional: Check if target file exists in vault (low priority)

### D. Other Formatting Issues

- Unclosed bold: `**text` without closing `**`
- Unclosed italics: `*text` without closing `*`
- Unclosed code blocks: ` ``` ` without closing ` ``` `

## Step 3: Create Lint Report

Create a detailed report file at:
```
/mnt/c/Users/carey/Documents/SyncVaultC/Blog Ideas and Posts/YYYY-MM-DD - TITLE/[post-name]-lint-report.md
```

If the folder doesn't exist (post isn't in dated folder yet), save to same directory as source file:
```
[post-name]-lint-report.md
```

Use this format:

```markdown
---
title: Lint Report
date: YYYY-MM-DD
source: [filename without path]
issues: [count]
---

# Lint Report: [Original Post Title]

**Source:** `[path]`
**Scanned:** YYYY-MM-DD HH:MM
**Total Issues:** [count]

## Summary

- 🔴 [X] Footnote issues
- 🔴 [X] Author TODO notes remaining
- 🔴 [X] Link formatting issues
- 🟡 [X] Formatting warnings
- 🟢 No issues found

---

## Author TODO Notes (Remove Before Publishing!)

These are bracketed notes you left for yourself. Remove or resolve before publishing:

#### Line 45: `[FIX THIS]`
```
...surrounding text [FIX THIS] more text...
```

#### Line 127: `[FIND SOURCE FOR THIS]`
```
The study showed that 73% [FIND SOURCE FOR THIS] of users...
```

#### Line 289: `[CUT????]`
```
This entire paragraph might not be needed [CUT????]
```

**Total TODO notes found:** [X]

---

## Footnote Issues

### Orphaned References (in text, no definition)

#### `[^5]` - Line 87
```
...surrounding text with [^5] reference...
```
**Issue:** No corresponding `[^5]: definition` found at bottom of file.
**Fix:** Add footnote definition or remove reference.

### Orphaned Definitions (defined but not referenced)

#### `[^12]` - Line 456
```
[^12]: This is an orphaned footnote definition.
```
**Issue:** No `[^12]` reference found in text.
**Fix:** Remove definition or add reference in text.

### Duplicate References

#### `[^3]` appears 3 times
- Line 45
- Line 89
- Line 112

**Issue:** Same footnote reference used multiple times.
**Fix:** Either this is intentional (same footnote cited multiple times) or you meant different numbers.

### Duplicate Definitions

#### `[^7]` defined 2 times
- Line 389
- Line 412

**Issue:** Footnote defined multiple times.
**Fix:** Keep one definition, remove the other.

### Numbering Gaps

**Sequence:** 1, 2, 3, 6, 8, 9, 10, 14, 15...
**Missing:** 4, 5, 7, 11, 12, 13

**Note:** Gaps might be intentional if you removed content. If renumbering, update both references and definitions.

---

## Link Formatting Issues

### Malformed Links in Blockquotes

#### Line 134
```markdown
> "This is a quote with a link" [source](https://example.com)
```
**Issue:** Link immediately after quote in blockquote may not render properly.
**Fix:** Consider moving link outside blockquote or restructuring.

#### Line 256
```markdown
> Indented pullquote text
[Link text](https://website.com)
```
**Issue:** Link on line after blockquote may not render as expected.
**Fix:** Either include link fully inside blockquote or move it outside with proper spacing.

---

## Other Formatting Issues

### Unclosed Bold/Italics

#### Line 89
```markdown
This text has **unclosed bold formatting
```
**Fix:** Add closing `**`

### Unclosed Code Blocks

#### Line 234
` ``` ` opened but never closed
**Fix:** Add closing ` ``` `

---

## Recommendations

1. **TODO Notes:** [X] author notes to remove/resolve before publishing
2. **Footnotes:** [X] issues to fix - see details above
3. **Links:** [X] potential rendering issues - test in preview
4. **Formatting:** [X] unclosed elements - will break rendering

## What You Can Ask Claude Code to Do

If you want automated fixes, come back to Claude Code terminal and ask for:
- "Highlight all issues with ==syntax==" - Creates highlighted copy
- "Renumber footnotes sequentially" - Fixes numbering gaps
- "Remove orphaned footnotes" - Deletes unused definitions

These require explicit requests - this report is read-only.
```

## Step 4: Optional - Highlight Issues in Source

Ask user: "Would you like me to create a version with issues highlighted using `==highlight==` syntax?"

If yes:
- Create a copy: `[filename]-highlighted.md`
- Wrap TODO notes: `==[FIX THIS]==`
- Wrap problematic footnote references: `==[^5]==`
- Wrap problematic links: `==[Link text](url)==`
- Add inline comments: `<!-- LINT: Missing footnote definition -->`
- Save to same directory as lint report

Report both file paths to user.

## Step 5: Suggest Fixes

Based on the issues found, provide actionable suggestions:

**For TODO notes:**
- "You left [X] reminder notes in brackets. Review and remove before publishing."

**For orphaned references:**
- "Add footnote definition at bottom, or remove reference if not needed"

**For orphaned definitions:**
- "Either add reference in text where you mention this, or delete the footnote"

**For malformed blockquote links:**
- Show the problematic pattern
- Suggest: "Move link outside blockquote, or restructure as: `> "quote" ([source](url))`"

**For numbering gaps:**
- "If you removed content, renumber footnotes sequentially to avoid confusion"

</process>

<technical_notes>

**Author TODO Note Regex:**
- Pattern: `\[([A-Z][A-Z\s?!]*)\](?!\(|:|\[)` - matches bracketed all-caps text
- Examples matched: `[FIX THIS]`, `[VERIFY]`, `[FIND SOURCE]`, `[CUT????]`
- Excludes:
  - Links: `[text](url)` - has `(` after `]`
  - Footnote defs: `[^1]:` - has `:` after `]`
  - Wikilinks: `[[Page]]` - has `[` before or after
  - Footnote refs: `[^1]` - handled separately

**Footnote Reference Regex:**
- Pattern: `\[\^(\w+)\](?!:)` - matches `[^1]`, `[^note]` but not `[^1]:`
- Capture group gets the number/label

**Footnote Definition Regex:**
- Pattern: `^\[\^(\w+)\]:\s*(.+)` - matches `[^1]: text` at start of line
- First capture: number/label
- Second capture: definition text

**Link in Blockquote Pattern:**
- Pattern: `^>\s*.*\[.+\]\(.+\)` - blockquote line containing markdown link
- Need to check context (is it properly inside quote or hanging outside?)

**Wikilink Pattern:**
- Pattern: `\[\[([^\]]+)\]\]` - matches `[[Page Name]]`

</technical_notes>

<edge_cases>

1. **Footnotes intentionally referenced multiple times**: This is valid markdown - same `[^3]` can appear multiple times pointing to single definition. Flag as "FYI" not error.

2. **Footnotes with labels not numbers**: `[^note1]` is valid. Support both.

3. **Links inside code blocks**: Don't flag these as issues, they're examples.

4. **HTML comments with footnote syntax**: `<!-- [^1] -->` shouldn't be flagged.

5. **Links in nested blockquotes**: `> > [text](url)` - even more likely to break.

6. **TODO notes that are legitimate content**: If bracket text contains lowercase or isn't clearly a note (e.g., `[via email]`, `[emphasis mine]`), don't flag it. Focus on all-caps or question-mark-heavy brackets.

7. **False positive TODO detection**: `[1]`, `[2]` - numbered references should not be flagged as TODOs. Check that content is actually letters/words.

</edge_cases>

<output_style>

- Use clear, actionable language
- Show line numbers for all issues
- Include surrounding context (3 lines before/after) so user can locate issue
- Use emoji indicators: 🔴 Error, 🟡 Warning, 🟢 OK, ℹ️ Info
- Don't be alarmist - frame as "here's what might break" not "this is garbage"
- Group similar issues together (all orphaned refs, then all orphaned defs)
- **Prioritize TODO notes at top** - these are most urgent for pre-publish check

</output_style>

<key_reminders>

1. **Read entire file** - footnotes are often at the very end
2. **Check line numbers** - user needs to know where to look
3. **Distinguish errors vs warnings** - orphaned footnotes are errors, numbering gaps are warnings
4. **Test in context** - blockquote links might render fine, flag as "check in preview"
5. **Don't auto-fix without permission** - ask first before modifying source file
6. **TODO notes are high priority** - these mean "not ready to publish"

</key_reminders>
