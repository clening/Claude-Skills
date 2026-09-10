---
name: blog-marketer
description: Generate platform-specific promotional content (Substack Notes, LinkedIn posts and carousels, pull quotes) from a blog post, calibrated to how Substack's and LinkedIn's 2026 algorithms actually distribute content. Use when the user asks to promote a post, write a Substack Note, draft a LinkedIn post, make a carousel/slide breakdown, generate pull quotes, or mentions "market this", "promote this post", "social content for this".
---

<objective>
Generate marketing content for a blog post, calibrated to what actually
drives distribution on Substack and LinkedIn in 2026 — not generic
social-media-manager folklore. Preserve the author's voice. Create multiple
variations so she has real choices, not one guess to accept or reject.

Bluesky is explicitly deprioritized per her direction ("almost useless") —
don't give it equal billing with Substack/LinkedIn.
</objective>

<scope>
This skill owns DISTRIBUTION content and channel strategy, not the post
itself:

- On-page discoverability (the post's own SEO/GEO — headings, entities,
  information gain) → `blog-proofreader` owns this.
- Argument quality → `blog-critique` owns this.

If the post hasn't been through `blog-proofreader` yet, mention that once —
the two skills are complementary: proofreader makes the post itself easier
to find/cite; this skill promotes a post that's already good.
</scope>

<vault_conventions>
Read `~/.claude/skills/_shared/references/vault-conventions.md`
before Step 1. Shared across all four blog skills.
</vault_conventions>

<author_voice>
Read `~/Obsidian/SyncVaultC/05-Blog-Pipeline/_shared/voice.md` before
Step 3. Shared across blog-critique, blog-proofreader, and blog-marketer.

**Adapt to platform, don't lose the edge:**
- LinkedIn: more professional but still direct.
- Substack Notes: conversational, can be more casual/edgy.
</author_voice>

<platform_reality_2026>
Read this before generating anything — it determines what "effective"
content looks like on each platform right now. Detail and sourcing in
`references/platform-research.md`; this is the operative summary.

**Substack — primary channel:**
- The Notes feed stopped prioritizing followed accounts in late 2025. Most
  of what a subscriber now sees comes from creators they've never followed,
  matched by audience-overlap signals. Posting alone doesn't reach people;
  being visibly *in conversation* does.
- **Restacking and replying to other people's Notes is the best-evidenced
  growth lever** — confirmed by Substack's own ML lead, not a growth-hack
  claim. A publication that only posts outward and never engages is largely
  invisible to this mechanism, regardless of how good the writing is. This
  isn't content this skill generates — flag it as a standing habit in
  Step 5, every time.
- Links do **not** suppress reach on Substack (unlike LinkedIn/X) — no need
  to hide or delay the link.
- No confirmed ideal Note length — Substack states the algorithm has no
  format preference. Treat any character-count target below as a
  practitioner heuristic, not an evidenced rule.
- Visual Notes (photo/video) are a rising share (~1/3) and anecdotally
  outperform text-only. Flag pull quotes that would work well as an
  image-quote — this skill can't generate the image, but can flag the
  candidate.
- **The single highest-leverage lever specific to Substack is
  Recommendations** — publications using them grow roughly 2.75x faster,
  and most new subscribers to a recommended pub arrive via another
  Substack's recommendation. This skill doesn't set that up; Step 5 always
  reminds her to check it.

**LinkedIn:**
- External links in a normal post cut reach by roughly 60%. Real and current.
- **"Link in first comment" is dead as of 2026** — the algorithm now detects
  that bridge pattern and penalizes it too. Do not generate this pattern; if
  you've seen it recommended elsewhere, it's stale.
- Real workaround: LinkedIn's native Article/Newsletter format avoids the
  link penalty by keeping the reader on-platform — trade-off is the reader
  never lands on the actual post or subscribes there. Offer both options,
  labeled honestly, and let her choose.
- Document/carousel posts (5-10 slide PDF breakdowns) get roughly 3x the
  engagement of plain-text posts — the single biggest format lever on this
  platform. For an argument-driven writer, a slide breakdown of the post's
  core argument usually beats another paragraph of status-update text.
  **Generate a carousel outline by default, not just a text post.**
- Hashtags are weak and contested since LinkedIn killed hashtag-following in
  2024 — estimates range from "roughly neutral" to a small lift. Use 1-2
  specific, contextual hashtags inline. Don't generate a stacked list of 5.
- Saves and comments outweigh likes as a distribution signal — CTAs should
  prompt saving or a real comment, not just a like.

**Bluesky — deprioritized:**
Generate at most one short thread, and only if she asks for it. Don't
default to producing it or give it a full lettered section alongside
Substack/LinkedIn.

**Why this skill doesn't chase Google/organic search:**
AI Overviews and zero-click search are suppressing publisher referral
traffic broadly (reported 25-38% YoY declines in 2026). Organic search is a
long-tail credibility asset for this newsletter, not a growth engine — hence
the focus on Notes/Recommendations/LinkedIn distribution here. The post's
own on-page discoverability is handled separately, by `blog-proofreader`.
</platform_reality_2026>

<process>
## Step 1: Get the File

Resolve the input path per `<vault_conventions>`.

## Step 2: Analyze the Post

Extract:
- **Title and thesis** — main argument, the "why should I care"
- **Hook elements** — opening lines, counterintuitive takes, controversial
  positions, personal anecdotes
- **Key arguments** — usually 3-5, with supporting evidence
- **Strong quotes** — one-liners, sarcastic observations, technical insight
  made accessible; note which are image-quote candidates
- **Call to action** — what should the reader do next
- **URL** — from frontmatter `url:` field if present, else `[LINK]` placeholder

## Step 3: Generate Platform Content

Read `<author_voice>` first. Then, per `<platform_reality_2026>`:

### A. Substack Notes (3-5 variations)
Hook + insight + link (links are fine, don't hide them). At least one
variation should be framed to invite a reply or restack, not just announce
the post — e.g. ending on a genuine question rather than only a CTA link.
Flag which variation(s) would work as an image-quote Note.

### B. LinkedIn (generate carousel first, then text)
1. **Carousel/document outline** (5-10 slides) — the priority format. Give
   each slide a one-line headline and 1-2 supporting bullets, building the
   post's core argument slide by slide, ending on a CTA slide.
2. **Text post, two labeled variants:**
   - *Native/Article style* — no external link, keeps reader on LinkedIn,
     summarizes the argument in full. Use when the goal is LinkedIn
     presence/authority.
   - *Status-update style* — includes the link, accepts the ~60% reach cost,
     drives traffic to the actual post. Use when the goal is subscribers.
   Label which is which so she picks deliberately, not by default.
3. 1-2 contextual hashtags per post, inline — not a stacked list.

### C. Pull Quotes (3-5)
280 characters or less, standalone impact. Mark any that are strong
image-quote candidates for a visual Substack Note.

### D. Thread Starters (2-3)
Questions or hot takes designed to prompt replies — these double as Notes
engagement bait, which matters more now that replies feed the audience-
overlap algorithm.

### E. Bluesky (only if asked)
One short thread (4-6 posts), 300 chars/post. Skip entirely unless requested.

## Step 4: Create Marketing File

Write to `<post-folder>/<post-slug>-marketing.md` per `<vault_conventions>`.
Use the structure in `references/marketing-template.md` — read it when you
reach this step, not before.

## Step 5: Report to User

Report the path and a one-line content summary. Then, every time, remind her
of the two things this skill can't do for her but that outweigh anything it
generates:
1. **Restack/reply to other people's Notes** — the best-evidenced Substack
   growth lever, and it's a habit, not a one-time task.
2. **Substack Recommendations** — check whether this post's newsletter is
   actively recommending and being recommended by adjacent
   privacy/AI-governance publications; this is the single highest-leverage
   lever available and this skill can't set it up.
</process>

<key_reminders>
1. **Preserve the edge** - platform tone shifts, voice doesn't
2. **Carousel over text-only on LinkedIn** - roughly 3x the engagement
3. **Never generate the link-in-first-comment trick** - dead as of 2026, actively penalized
4. **Links are fine on Substack** - don't hide them, that's a LinkedIn problem not a Substack one
5. **Bluesky is optional, not equal billing** - only on request
6. **Always close with the Recommendations + restacking reminder** - highest-leverage items this skill can't generate
7. **Multiple options** - give her real choices, especially the two LinkedIn text variants
</key_reminders>
</content>
