# Blog Pipeline Vault Conventions

Shared by blog-critique, blog-linter, blog-proofreader, blog-marketer.
Read this once, at the point in each skill's process where it says to.

## Publication

Carey's Substack is **insights.priva.cat**. Posts are drafted in Obsidian
and published there; the conversion is imperfect and produces some
recurring artifacts that look like errors but render fine on Substack (see
`blog-linter`'s judgment-call notes for the specific case: bare
Substack-hosted URLs in parens, no `[text](url)` wrapper needed).

## Base path and stages

```

/Obsidian/SyncVaultC/05-Blog-Pipeline/
├── Ideas/              — unstarted concepts
│   └── Research/        — background research for ideas not yet drafted
├── Drafting/            — posts in progress
├── Published/           — live posts
├── Dead/                — abandoned
├── Kudos/                — reader feedback / self-promotion notes
└── _Editorial-Dashboard.md   — dataview board over Drafting/ and Ideas/Research/
```

## Folder-per-post

Every post lives in its own folder, named exactly after the post file
(date-prefixed title, no extension):

```
Drafting/2026-07-13 - Can We Just Throw the Bastards in Jail Already/
├── 2026-07-13 - Can We Just Throw the Bastards in Jail Already.md   (the post)
├── ...-critique.md
├── ...-lint-report.md
├── ...-proofread.md
└── ...-marketing.md
```

This lets Carey move the whole folder from `Drafting/` to `Published/` as one
unit when a post goes live. It also keeps `_Editorial-Dashboard.md`'s
dataview (which lists everything under `Drafting/`) from mistaking a lint
report for a draft in progress.

**Never write a generated artifact directly into `Drafting/`, `Ideas/`, or
`Published/` as a loose file.** It always goes inside the post's own folder.

## Resolving the input post

1. Absolute path given → use it.
2. Bare filename, partial title, or fragment → Glob
   `05-Blog-Pipeline/**/*<fragment>*.md`, checking `Drafting/` first, then
   `Published/`, then `Ideas/`.
3. Multiple matches → list them and ask which one. Never guess.
4. Nothing given → list recent files in `Drafting/` by modified time and ask.
5. Some entries are folders already (the normal case) and some may still be
   loose `.md` files. Handle both — see migration rule below.

## Lazy migration on touch

If the resolved source file is a loose `.md` sitting directly in `Drafting/`
(not already inside a same-named folder), migrate it before doing anything
else:

```bash
mkdir -p "Drafting/<title>"
mv "Drafting/<title>.md" "Drafting/<title>/"
```

Then proceed using the new path inside the folder. Do this silently as part
of the workflow — it's routine housekeeping, not a decision that needs
confirmation, because the destination is unambiguous and the move is a
rename within the same stage. Report the move in one line so Carey knows it
happened.

**Do not** apply this migration logic to `Published/`, `Dead/`, or `Ideas/`
un-asked — those folders were left flat deliberately and mixing conventions
there wasn't part of the agreed scope. If a skill is invoked on a loose file
in one of those folders, ask first.

## Running a skill against an already-published post

If the target post is in `Published/`, confirm the purpose before writing
an artifact: is this feeding a real revision, or is it a one-off test/eval
run (e.g. comparing new skill output against an old report)? For a test/eval
run, present the analysis in conversation and do NOT write a new file into
the post's folder — a published, settled post doesn't need another artifact
accumulating next to it. Only write to disk if she's actually revising the
published post or explicitly asks for a saved copy.

## Writing artifacts

Every generated report/critique/lint-report/marketing file goes inside the
post's own folder, named `<post-slug>-<artifact-type>.md` where `<post-slug>`
is the post filename minus extension.

## Dates

Get today's real date with `date +%Y-%m-%d` before writing any report
frontmatter. Never hardcode or guess a date.

## Orphaned artifacts

If you find a report file with no matching post in the same folder (source
was renamed, moved, or deleted out from under it), do not silently delete or
relocate it. Flag it to Carey and ask what to do — she may want it kept as
history, moved with the post, or removed.
</content>
