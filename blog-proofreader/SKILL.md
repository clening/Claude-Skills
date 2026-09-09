---
name: blog-proofreader
description: Comprehensive pre-publish proofread of a blog post - voice consistency, AI-y language, clarity/flow, discoverability (Google + AI-answer-engine citation), and a publication checklist. Use when the user asks to proofread, polish, or do a final pass on a post; asks if a post is ready to publish; asks about SEO, discoverability, or getting cited by ChatGPT/Perplexity/AI Overviews; or mentions "proofread this", "final check", "pre-publish".
---

<objective>
Proofread blog posts for publication readiness, focusing on:
1. Voice consistency (preserving author's edge and style)
2. Eliminating AI-y language (hedging, generic praise, excessive enthusiasm)
3. Discoverability — on-page choices that help both classic Google ranking
   and citation by AI answer engines (ChatGPT, Perplexity, Google AI Mode)
4. Clarity and flow (transitions, repetition, logical structure)
5. Publication checklist items

Creates a comprehensive proofreading report with specific, actionable feedback.
</objective>

<scope>
This skill owns PROSE, VOICE, and DISCOVERABILITY. Stay in that lane:

- Argument quality, evidence gaps, counterarguments → `blog-critique` owns these.
  Flag only the most obvious unsupported claims in passing (Section D below);
  don't do a deep pass — that's a separate skill and a separate dialogue.
- Broken footnotes, malformed links, formatting that breaks rendering →
  `blog-linter` owns these.

If something in another skill's lane catches your eye, note it in one line
under "Out of Scope" and move on.
</scope>

<vault_conventions>
Read `/home/privacat/.claude/skills/_shared/references/vault-conventions.md`
before Step 1. Shared across all four blog skills.
</vault_conventions>

<author_voice_guidelines>
Read `/home/privacat/.claude/skills/_shared/references/voice.md` before
Step 2. Shared across blog-critique, blog-proofreader, and blog-marketer.

**Red Flags for AI-y Language** (this skill's own responsibility, not covered
in the shared voice file):
- Excessive hedging: "It's worth noting that...", "It's important to understand...", "One might argue..."
- Generic enthusiasm: "incredibly", "absolutely", "truly remarkable"
- Overuse of qualifiers: "very", "quite", "rather", "somewhat"
- Passive constructions where active is better
- Corporate-speak: "leverage", "synergy", "ecosystem" (unless mocking)
- Saying the same thing twice: "quick and easy", "each and every", "first and foremost"
</author_voice_guidelines>

<process>
## Step 1: Get the File

Resolve the input path per `<vault_conventions>`.

## Step 2: Analyze the Post

Perform comprehensive analysis across these dimensions:

### A. Voice & Style Analysis

Check for AI-y language patterns (see `<author_voice_guidelines>`), and
verify voice consistency against `voice.md`:
- Does it sound like her authentic voice — both registers are valid, but
  don't blur them within one piece?
- Any sections that feel "smoothed over" or generic?
- Is rhythm/alliteration preserved where it's clearly intentional, or has
  editing (hers or otherwise) flattened it?
- Technical precision maintained throughout?

**Originality & Honesty Check:**
- Is this recycling common takes or providing fresh analysis?
- What unique insight can't a reader generate in 30 seconds elsewhere? (This
  doubles as the "information gain" check in Section B — genuinely original
  synthesis is now the single biggest lever for both Google ranking and AI
  citation post-2026, see below.)
- Clichés: flag as "missed opportunities" for original phrasing, not errors.

### B. Discoverability — Google + AI Answer Engines

**Frame this correctly before doing anything else:** as of 2026, "SEO" and
"GEO" (getting cited by ChatGPT/Perplexity/Claude/Google AI Mode) are
converging, not separate disciplines. Google's own guidance says AI Overviews
and AI Mode use no separate crawl — they rerank the existing Google index.
ChatGPT's search layer sits on Bing. **Getting retrieved at all (classic
ranking/authority) is the dominant factor; text-level rewriting for AI is a
much smaller, less reliable lever than the SEO industry claims.** Multiple
2026 replications of the original "GEO" research found near-zero effect from
formatting-only tweaks — see `references/discoverability-notes.md` for the
underlying research if you want the detail.

Given that, split checks into two tiers:

**Tier 1 — do these, they're evidenced or free (per-post, check every time):**
- **Self-contained paragraphs.** No orphan pronouns ("this," "as noted
  above") that only resolve if the paragraph is read in full document
  context — AI engines retrieve passages, not always full pages.
- **Specific, descriptive headings** that restate the topic rather than
  being clever or elliptical. Headings carry disproportionate retrieval
  weight and often become the passage boundary.
- **Named entities spelled out**, not pronoun'd away: "GDPR Article 22," not
  "the provision"; full names/acronym pairs on first use per major section.
- **Explicit dates and numbers** over vague temporal language: "In its March
  2026 decision" beats "recently." This has direct empirical support.
- **A definition sentence for each key term** she's introducing or relying
  on: "X is a Y that does Z." Helps both a human skimming and a retrieval
  system matching a definitional query.
- **Front-loaded conclusions** — state the finding, then support it.
- **Visible byline and credentials in the rendered post**, not just
  frontmatter — live crawlers read visible text, not hidden metadata.
- **Genuine information-gain check** (see Section A) — content that merely
  synthesizes what's already in the top results is what Google's 2026 core
  update reportedly targets as "AI slop." Her heavily-footnoted, primary-
  source-driven style is structurally advantaged here; flag if a section
  reads as pure summary of common takes.

**Tier 2 — explicitly low-value or debunked. Don't add these, and flag them
if already present so she stops spending time on them:**
- Keyword density / repeating a target phrase for search purposes — dead;
  keyword stuffing measurably *hurt* in the original GEO study.
- Strict 50–60 character title rule — cosmetic at best; Google rewrites
  titles freely. Keep the underlying instinct only as "make the title
  specific," not a character-count rule.
- Bolted-on FAQ blocks that don't correspond to real reader questions.
- AI-specific schema/structured data — a 2026 study of 1,885 pages found no
  measurable citation lift; live-fetch crawlers read visible text, not
  hidden JSON-LD.
- llms.txt — Google has confirmed it doesn't use it; adoption studies found
  97% of these files receive zero AI-crawler requests.
- Rewriting prose to sound more "authoritative" — the research explicitly
  flags confident tone as a weak, unstable signal; don't recommend it as a
  discoverability tactic, and don't confuse it with the voice work in
  Section A, which is about *her* voice, not a generic authority register.

**One-time site-level items — check only if asked, not every post:**
Custom domain (Substack has been observed serving crawlers a 302 instead of
article HTML on the platform subdomain), robots.txt not blocking
`OAI-SearchBot`/`PerplexityBot`/`ClaudeBot`/`Google-Extended`, Bing Webmaster
Tools submission. Mention once if relevant, don't repeat per report.

**Meta Description (if present in frontmatter):**
- 150-160 characters, compelling, includes the actual topic — this remains
  useful as a click-through lever in search results regardless of the
  AI-citation question.

**Subheadings (H2, H3):**
- Clear hierarchical structure, no skipped levels, break up long sections,
  descriptive rather than generic.

### C. Clarity & Readability

**Paragraph length:**
- Are paragraphs too long (> 4-5 sentences)? Do they each focus on one idea?

**Sentence variety:**
- Mix of short and long sentences? Active voice where it serves the point?
- Are sentences structured around what logically matters most? (e.g.,
  "Giving them money scales sublinearly" not "It scales sublinearly to give
  them money")

**Transitions:**
- Smooth flow between paragraphs? Clear logical connections? Signposting?

**Repetition:**
- Same words/phrases overused? Same point made multiple times without
  adding value? Redundant modifiers?

**Jargon & Accessibility:**
- Technical terms explained where needed? Acronyms defined on first use?

### D. Argument Strength (Light Check Only)

Not a deep critique — that's `blog-critique`. Only flag the most obvious:
claims that clearly need support, weak transitions in logic, sections that
visibly drag. If you find yourself wanting to steelman a counterargument or
go back-and-forth on an evidence gap, stop — note it under "Out of Scope"
and suggest running `blog-critique` instead.

### E. Publication Checklist

- Title/headline present? Author/date in frontmatter?
- All links working (no broken `[[wikilinks]]`)?
- Images referenced are present?
- No placeholder text (`[TK]`, `[INSERT]`, bracketed TODO notes)?
- Consistent voice throughout?

## Step 3: Create Proofreading Report

Write to `<post-folder>/<post-slug>-proofread.md` per `<vault_conventions>`.

Use the structure in `references/proofread-report-template.md`. Read that
file when you reach this step — not before.

## Step 4: Report to User

Tell the user the path, a one-line count of issues by category, and overall
priority (High/Medium/Low fixes needed).
</process>

<style_notes>
- Be specific: cite line numbers and show context.
- Be actionable: don't just say "improve this," suggest how.
- Respect the voice: don't smooth out the edge.
- Prioritize: separate "must fix" from "nice to have."
</style_notes>

<key_reminders>
1. **Preserve the edge** - Don't suggest softening strong language
2. **Flag AI-y patterns** - These undermine authenticity
3. **Discoverability is now mostly "does this get retrieved," not "does this have the right keywords"** - lean on Tier 1, actively flag Tier 2 tactics as not worth her time
4. **Be thorough** - this is the final check before publishing
5. **Give context** - explain WHY something should change
6. **Stay in your lane** - deep argument critique belongs to `blog-critique`; formatting belongs to `blog-linter`
</key_reminders>
</content>
