# Carey's Voice — Shared Reference

Used by blog-critique, blog-proofreader, blog-marketer. One file so it can't
drift across skills the way three separate copies did.

**Status: confirmed via direct interview, 2026-07-19.** Supersedes the
earlier placeholder version. Still a living document — update it through
conversation with Carey, not by inference from a single piece.

## Identity and theory of change

She's an angry, frustrated, pattern-matching writer — a cross between a
rigorous forecaster-with-receipts ("Privacy Cassandra") and a rogue
legal/policy analyst using the law's own language against it, more than a
Guardian-style investigative journalist. Underneath the anger she's an
**optimistic contrarian**: she believes there's a real way out, and that
almost no one takes it because they're scared of "stupid powerful men,"
not because the problem is unsolvable.

**Two parallel tracks, both legitimate, not a fallback hierarchy:**
- **Track A — rigorous argument reshapes elite consensus.** Modeled on
  Stuart Russell and Lina Khan: precision-targeted at people with actual
  leverage (EU/US policymakers, more realistically their staffers who put
  ideas in a principal's ear). Credibility and receipts are the mechanism.
  This is what `blog-proofreader`'s information-gain check serves.
- **Track B — outrage forces change from below.** Modeled on Upton Sinclair:
  *The Jungle* didn't win legislators over with careful argument, it
  disgusted enough ordinary readers that the Pure Food and Drug Act became
  politically unavoidable. Sinclair's own line applies: "I aimed at the
  public's heart, and by accident I hit it in the stomach" — outrage doesn't
  have to land exactly where aimed to still force change. This is what
  `blog-marketer`'s reach/virality work serves — not a consolation prize,
  a real half of the strategy.

Don't collapse these into "write for maximum reach" or "write only for
policy insiders." Both are live goals, often in the same piece.

**Her stated failure mode**: she knows how to write the diagnosis and the
policymaker-facing ask ("wake up, stop sitting on your hands"). What she
struggles with is the ask for a normal reader — see the closing structure
below, which she has actually used successfully before; it's not a gap in
her ability, more a pattern she's lost conscious track of.

## Core stance

- Sharp, unapologetic critique — doesn't pull punches
- Technical precision (GDPR, AI governance, data protection law) — though
  see the editorial shift below
- Evidence-driven: original research, data analysis, extensive sourcing
- Conversational but authoritative
- Personal stakes and investment in the topics
- Strategic sarcasm/irony, deployed deliberately, not as filler

**Editorial shift (2026-07-19)**: moving away from pure GDPR/legal analysis
toward tech extensity, concentrations of power, power dynamics in tech, and
Big Tech criticism generally. The legal precision doesn't disappear — it
becomes a weapon aimed at a wider target, per the "rogue legal analyst"
framing above, rather than the whole frame.

## Structural pattern for closing a piece

Extracted from "Privacy Nihilism is Pervasive. Are Our Laws to Blame?" (May
2024, `Published/Bangers/`) — this is a real, previously successful
template, not a hypothetical:

1. **Diagnosis** — name the problem sharply, no hedging.
2. **Mechanism** — explain *why* it's broken, not just that it is.
3. **Concrete multi-part fix** — specific, numbered if useful, not vague
   gestures at "doing better."
4. **Two-tier call to action** — this is the piece she has trouble
   reconstructing from scratch, so check for it explicitly:
   - A **specific ask for people with leverage** (advocate, push your
     representatives, share with policymaker contacts) — serves Track A.
   - An **achievable floor-level ask for everyone else** — something a
     normal reader can actually clear, deliberately set low enough to
     avoid nihilism. ("If you can even get to that last bit, I'll be
     happy.") Serves Track B by keeping the door open rather than closing
     it in despair.
5. **Explicit humility** about what's left unsolved — this is what lets her
   keep full edge on the diagnosis without overclaiming on the fix. Not
   hedging on the argument itself, just honesty about scope.
6. **Optional register break at the very end** — raw, first-person, direct
   address, almost stand-up ("Seriously, I crave attention"). Not every
   piece needs this, but when a piece has one, it's deliberate, not a
   lapse in consistency — don't smooth it into the analytical register.

## Anti-nihilism guardrail

Never let a piece's last note be pure despair. Every piece needs either an
achievable minimum ask (see step 4 above) or a live example of forward
motion already happening (the Nihilism piece uses the EU's Common Charger
Directive spreading to India, Taiwan, California as evidence that fixing
one law can cascade). She's explicit that it's getting easier to give up,
and she doesn't want to model that for readers, even in the angriest pieces.
This doesn't mean softening the diagnosis — the diagnosis can be as dark as
warranted. It means the piece can't end there.

## Footnotes carry voice

Footnotes in her published work aren't just citation infrastructure — they
carry jokes and asides ("except for laws on data transfers outside the EU.
That's just a confusing mess no matter how many beers you've had.").
`blog-linter` should never treat a footnote's tone as a formatting problem;
`blog-proofreader` should read footnotes for voice consistency same as body
text, not skip them as boilerplate.

## Specific mechanics (confirmed, from long-term memory)

- **Flow over perfect definitional clarity**, when the two are in tension.
  She'll choose the phrase that moves over the phrase that's more precise.
- **Alliterative/rhythmic wordplay is load-bearing, not decorative.** d-d-d
  patterns, internal rhythm, consonance. When editing, preserve the rhythm
  even at a small cost to precision — flag the trade-off rather than
  silently smoothing it away.
- **Cut hedge verbs.** "I posit," "I assert," "I propose" → flat declarative.
  Signposting an argument as opinion reads as weaker to her audience, not
  more careful. Confirmed independently twice: once in direct editing
  feedback, once in a separate memory noting she pushes further/sharper
  than Claude's own default read of her work — treat that gap as real and
  correct for it, not as an occasional preference.
- **Specific named entities over abstractions.** "SpaceX restricting
  Ukraine's Starlink" beats "Big Tech firms exhibit concentration of power."
- **Concrete personal/lived examples anchor abstract concepts** — a core
  recurring move, not an occasional device.
- **Two registers, same spine:**
  - *Substack voice*: conversational, specific, pop-culture-referencing,
    lightly profane, lived examples.
  - *Policy-pitch voice*: same sharpness and specificity, ~30% less casual,
    no profanity, no pop-culture references.
  Don't blur them. If editing, name which register the piece is in.

## Do NOT

- Suggest softening language or removing "edge"
- Make writing sound more "balanced" if the evidence already supports her position
- Tone-police, or push "both-sides" framing
- Make it sound AI-y — no excessive enthusiasm, hedging, or generic praise
- Optimize toward a generic, cite-able-by-nobody policy-memo register
- Let a piece end in pure despair without an achievable ask or a live
  example of forward motion
- Treat a register break, a joke footnote, or "I crave attention"-style
  vulnerability as an inconsistency to smooth out

## Why this matters

Her own assessment (per long-term memory): *"Your voice is already your
moat. The bottleneck is consistency, not inputs."* Being recognizable on the
page — not sounding like every other privacy-policy newsletter — is the
long-term competitive asset. This outranks locally-cleaner phrasing in most
editing decisions. And per this interview: the point was never just to
sound distinctive — it's to move Track A or Track B forward. Voice in
service of nothing is just style.
</content>
