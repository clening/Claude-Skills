# Blog Writing Skills for Claude Code

A collection of Claude Code skills for privacy/tech blog writing workflow.

## Vault layout

```
/mnt/c/Users/carey/Documents/SyncVaultC/05-Blog-Pipeline/
├── Ideas/                — unstarted concepts (+ Ideas/Research/)
├── Drafting/              — posts in progress
├── Published/             — live posts
├── Dead/                  — abandoned
└── _Editorial-Dashboard.md
```

Every post lives in its own folder, named after the post (date-prefixed
title), containing the source `.md` and every artifact these skills
generate (`-critique.md`, `-lint-report.md`, `-proofread.md`,
`-marketing.md`). This is so a finished post can move from `Drafting/` to
`Published/` as one folder. Full rules — path resolution, lazy migration for
stray loose files — live in
`_shared/references/vault-conventions.md`, shared by all four skills.

## Shared references

- `_shared/references/vault-conventions.md` — path/folder rules, read by all four skills.
- `_shared/references/voice.md` — Carey's writing voice, read by blog-critique, blog-proofreader, blog-marketer. One file, so voice guidance can't drift between skills the way three separate copies used to.

## Skills, and how they divide the work

Each skill owns a lane and defers to the others rather than duplicating
checks. Running one first doesn't require running the others, but if a skill
notices something outside its lane, it flags it in one line under
"Out of Scope" instead of auditing it.

### 1. blog-critique — argument
Iterative dialogue: evidence gaps, steelmanned counterarguments, logical
weaknesses. Doesn't touch tone, formatting, or "edginess."

**Output:** `<post-folder>/<post-slug>-critique.md`

### 2. blog-linter — formatting
Runs a script (`scripts/lint_checks.py`) for the deterministic parts —
orphaned/duplicate footnotes, numbering gaps, TODO-bracket candidates,
blockquote links, unclosed formatting — then applies judgment to what the
script can't decide (is this bracket really a TODO? will this link actually
break rendering?).

**Output:** `<post-folder>/<post-slug>-lint-report.md`

### 3. blog-proofreader — prose, voice, discoverability
Voice consistency, AI-y language, clarity/flow, and a Tier 1/Tier 2
discoverability check calibrated to how Google AI Overviews and AI answer
engines (ChatGPT, Perplexity) actually retrieve content in 2026 — see
`references/discoverability-notes.md` for the research behind it. Only
flags the most obvious argument gaps; defers real argument work to
blog-critique.

**Output:** `<post-folder>/<post-slug>-proofread.md`

### 4. blog-marketer — distribution
Generates Substack Notes, a LinkedIn carousel outline (the priority format —
~3x the engagement of text-only), two labeled LinkedIn text variants, pull
quotes, and thread starters — calibrated to how Substack's and LinkedIn's
2026 algorithms actually distribute content (see
`references/platform-research.md`). Bluesky is optional, generated only on
request. Every run closes with a reminder that Substack Recommendations and
restacking/replying to other Notes are the two highest-leverage growth
levers, and this skill can't do either one for her.

**Output:** `<post-folder>/<post-slug>-marketing.md`

---

## Typical workflow

1. **Draft** — write the post in `Drafting/<post-title>/`
2. **Critique** — `/blog-critique` for evidence gaps and counterarguments
3. **Revise** — incorporate feedback
4. **Lint** — `/blog-linter` to catch footnote/link/formatting issues
5. **Fix** — resolve linting issues
6. **Proofread** — `/blog-proofreader` for voice, clarity, and discoverability
7. **Publish** — move the whole post folder to `Published/`
8. **Market** — `/blog-marketer` to generate promotional content, then
   actually restack a few other people's Notes before posting

## Author style

Tuned for posts about tech extensity and concentrations of power, power
dynamics in tech, Big Tech criticism, AI, privacy and data protection,
technology policy, AI governance, and GDPR/CCPA and data protection law.
Carey's focus is moving away from pure GDPR/legal analysis toward the
extensity/power-concentration framing — see `_shared/references/voice.md`
for the full profile. It's a living document, being refined through direct
conversation with Carey, not a fixed spec.

## Installation

Skills live in `~/.claude/skills/`. Use `/skill-name` to invoke, or describe
what you want — each skill's description lists the phrases that trigger it.

## License

MIT
</content>
