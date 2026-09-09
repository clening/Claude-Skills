#!/usr/bin/env python3
"""Deterministic checks for the blog-linter skill. Outputs JSON to stdout.

Handles what regex can decide with certainty: footnote orphans/duplicates/
gaps, candidate TODO-bracket notes, wikilinks, markdown links inside
blockquotes, and unclosed bold/italic/code fences.

Deliberately leaves judgment calls to the caller (an LLM applying this
skill): whether a flagged bracket is really an author TODO vs legitimate
content, whether a flagged blockquote link will actually break rendering,
and footnote-cited-twice is informational, not an error.
"""
import re
import sys
import json


REF_RE = re.compile(r'\[\^([^\]]+)\]')
DEF_RE = re.compile(r'^\[\^([^\]]+)\]:\s*(.*)$')
TODO_RE = re.compile(r'(?<!\[)\[([A-Z][A-Z\s?!]*)\](?!\(|:|\[)')
WIKILINK_RE = re.compile(r'\[\[([^\]]+)\]\]')
MD_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
FENCE_RE = re.compile(r'^\s*```')


def lint(path):
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()

    refs = {}
    defs = {}
    todos = []
    wikilinks = []
    blockquote_links = []

    in_code = False
    open_fence_line = None
    bold_open = False
    bold_flip_line = None
    italic_open = False
    italic_flip_line = None

    for i, raw in enumerate(lines, start=1):
        line = raw.rstrip('\n')

        if FENCE_RE.match(line):
            in_code = not in_code
            open_fence_line = i if in_code else None
            continue

        if in_code:
            continue

        def_match = DEF_RE.match(line)
        if def_match:
            defs.setdefault(def_match.group(1), []).append(i)
        else:
            for m in REF_RE.finditer(line):
                refs.setdefault(m.group(1), []).append(i)

        for m in TODO_RE.finditer(line):
            todos.append({"line": i, "text": m.group(0), "context": line.strip()})

        for m in WIKILINK_RE.finditer(line):
            wikilinks.append({"line": i, "page": m.group(1)})

        if line.lstrip().startswith('>'):
            for m in MD_LINK_RE.finditer(line):
                blockquote_links.append({
                    "line": i, "text": m.group(1), "url": m.group(2),
                    "context": line.strip(),
                })

        # Bold/italic parity — best-effort only, flag as low-confidence.
        if line.count('**') % 2 == 1:
            bold_open = not bold_open
            bold_flip_line = i
        de_bolded = line.replace('**', '')
        if de_bolded.count('*') % 2 == 1:
            italic_open = not italic_open
            italic_flip_line = i

    formatting_issues = []
    if in_code:
        formatting_issues.append({
            "type": "unclosed_code_block", "line": open_fence_line,
            "detail": "Code fence opened here has no matching close.",
        })
    if bold_open:
        formatting_issues.append({
            "type": "unclosed_bold", "line": bold_flip_line,
            "detail": "Odd count of ** markers from this line to EOF — likely unclosed bold.",
        })
    if italic_open:
        formatting_issues.append({
            "type": "unclosed_italic", "line": italic_flip_line,
            "detail": "Odd count of single * markers (after removing **) from this line to EOF. "
                      "Low confidence — verify by eye before flagging.",
        })

    ref_labels = set(refs)
    def_labels = set(defs)

    orphan_refs = sorted(ref_labels - def_labels)
    orphan_defs = sorted(def_labels - ref_labels)
    dup_defs = {l: ln for l, ln in defs.items() if len(ln) > 1}
    reused_refs = {l: ln for l, ln in refs.items() if len(ln) > 1}

    numeric_labels = sorted(int(l) for l in (ref_labels | def_labels) if l.isdigit())
    gaps = []
    if numeric_labels:
        full = range(numeric_labels[0], numeric_labels[-1] + 1)
        gaps = [n for n in full if n not in numeric_labels]

    return {
        "file": path,
        "footnotes": {
            "orphan_references": [{"label": l, "lines": refs[l]} for l in orphan_refs],
            "orphan_definitions": [{"label": l, "lines": defs[l]} for l in orphan_defs],
            "duplicate_definitions": [{"label": l, "lines": ln} for l, ln in dup_defs.items()],
            "reused_references_info": [{"label": l, "lines": ln} for l, ln in reused_refs.items()],
            "numbering_gaps": gaps,
        },
        "todo_note_candidates": todos,
        "wikilinks": wikilinks,
        "blockquote_link_candidates": blockquote_links,
        "formatting_issues": formatting_issues,
    }


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: lint_checks.py <path-to-post.md>", file=sys.stderr)
        sys.exit(1)
    print(json.dumps(lint(sys.argv[1]), indent=2))
