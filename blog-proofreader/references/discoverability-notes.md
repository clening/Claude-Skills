# Discoverability Research Notes (2026)

Background for the Tier 1 / Tier 2 split in the main skill. Load this only
if you want the underlying evidence — the skill body already has the
actionable version.

## Bottom line

The empirical literature has moved against most of what the "GEO" (Generative
Engine Optimization) industry sells. **Getting retrieved is the hard part,
and classic SEO/authority is how you get retrieved. Text-level "GEO tweaks"
have small, unstable, and sometimes negative effects.**

## What the research actually shows

- **Original GEO paper** (Aggarwal et al., KDD '24,
  [arxiv.org/abs/2311.09735](https://arxiv.org/abs/2311.09735)): tested 9
  tactics, found Statistics Addition (+41%) and Quotation Addition (+28%)
  helped, keyword stuffing hurt. Caveat the industry omits: this measured
  citation *conditional on already being in the retrieved context* — not
  organic retrieval, no user study.
- **C-SEO Bench** (Puerto et al., NeurIPS 2025 D&B,
  [arxiv.org/abs/2506.11097](https://arxiv.org/abs/2506.11097)): broad
  replication found C-SEO tactics "mostly ineffective" — near-zero boost;
  none of the tested methods worked for question-answering tasks (closest
  analogue to an answer engine); gains erode toward zero-sum as adoption rises.
- **SAGEO Arena** (Kim et al. 2026): body-only GEO rewriting *reduced*
  retrieval presence 9-16% and final citation ~6%. Optimizing prose for
  quotability can make a page harder to retrieve in the first place.
- **Critical survey 2023-2026**
  ([arxiv.org/html/2607.14035v1](https://arxiv.org/html/2607.14035v1)):
  concludes no reviewed technique shows a stable, cross-platform causal
  effect on organic discoverability; explicitly flags "authoritative tone"
  as a weak, unstable signal.
- **Vishwakarma et al.** (252,000 trials, 6 LLMs, 18 factors): primary
  determinants of citation are query-relevance and context position — both
  outrank any rewrite. Explicit prices/recent dates showed real effects;
  formatting alone was weak.

## Retrieval surface

- ChatGPT search is Bing-backed (~87% overlap with Bing top results per Seer
  Interactive analysis) plus own crawlers (`OAI-SearchBot` for the search
  index — blocking it removes a site from ChatGPT Search).
- Google AI Overviews / AI Mode: no separate index — reranks/synthesizes
  from the existing Google index via query fan-out. Classic Google ranking
  *is* the entry ticket.
- Perplexity has a genuine proprietary index (`PerplexityBot`), heavily
  freshness-weighted.

## Debunked / low-value, with sources

- **llms.txt**: Google's Gary Illyes confirmed non-support (Jul 2025); an
  adoption study across hundreds of thousands of domains found 97% of these
  files never get fetched, zero measurable citation effect
  ([ppc.land](https://ppc.land/llms-txt-adoption-rises-8-8x-but-97-of-files-get-zero-ai-requests/)).
- **AI-specific schema/structured data**: Ahrefs study (May 2026) tracked
  1,885 pages that added JSON-LD, found no meaningful citation lift on any
  platform — live fetches read visible text, skip hidden JSON-LD. Google's
  own guide: "Structured data isn't required for generative AI search."
- **Substack platform-subdomain crawler issue**: observed serving 302
  redirects to AI crawlers instead of article HTML, making the archive
  invisible to live fetches; moving to a custom domain (CNAME) fixed it
  ([digitalapplied.com](https://www.digitalapplied.com/blog/ai-crawler-discoverability-audit-invisible-archive-302-fix)).
  This is the single most concrete, actionable finding for a Substack writer
  specifically.

## Official Google position (May 2026)

[developers.google.com/search/docs/fundamentals/ai-optimization-guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) —
AEO/GEO is "still SEO," no additional requirements to appear in AI Overviews
or AI Mode. Explicitly lists as things to ignore: llms.txt, chunking content
for AI, writing differently for generative AI, AI-specific structured data.
Keyword density and strict title-character rules are also superseded —
Google's guide says the system understands synonyms and rewrites titles
freely regardless.

## Measurement (if she asks how to tell if this is working)

Only ~12-18% of Perplexity citations produce a click (SparkToro, Jan 2026) —
most AI-citation value leaves no analytics trace. Practical tiers, cheapest
first: (1) server/platform logs for `ChatGPT-User`, `PerplexityBot`,
`OAI-SearchBot`, `ClaudeBot` hits — invisible in GA4 since bots skip JS; (2)
GA4 custom channel group regexing AI-referrer domains, noting Google AI Mode
uses `noreferrer` and is structurally untrackable; (3) manual monthly prompt
testing across ChatGPT/Perplexity/Claude/Google AI Mode with a fixed
question list, logged in a spreadsheet — cheapest, most reliable for a solo
writer; (4) Google Search Console's Generative AI performance report.
</content>
