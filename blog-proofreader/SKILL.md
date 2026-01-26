---
name: blog-proofreader
description: Comprehensive proofreading for blog posts - checks voice consistency, SEO, clarity, flow, and flags AI-y language. Creates detailed proofreading report with actionable suggestions.
---

<objective>
Proofread blog posts for publication readiness, focusing on:
1. Voice consistency (preserving author's edge and style)
2. Eliminating AI-y language (hedging, generic praise, excessive enthusiasm)
3. SEO optimization (headlines, structure, keywords, meta descriptions)
4. Clarity and flow (transitions, repetition, logical structure)
5. Publication checklist items

Creates a comprehensive proofreading report with specific, actionable feedback.
</objective>

<author_voice_guidelines>
The author writes with:
- Sharp, unapologetic critique (direct, doesn't pull punches)
- Technical precision (GDPR, AI, data protection expertise)
- Evidence-driven arguments (extensive sourcing, original research)
- Conversational but authoritative tone
- Personal investment in topics
- Strategic use of sarcasm/irony

**Red Flags for AI-y Language:**
- Excessive hedging: "It's worth noting that...", "It's important to understand...", "One might argue..."
- Generic enthusiasm: "incredibly", "absolutely", "truly remarkable"
- Overuse of qualifiers: "very", "quite", "rather", "somewhat"
- Passive constructions where active is better
- Corporate-speak: "leverage", "synergy", "ecosystem" (unless mocking)
- Saying the same thing twice: "quick and easy", "each and every", "first and foremost"
</author_voice_guidelines>

<process>
## Step 1: Get the File

If args provided:
- First arg is the path to the blog post file
- If path doesn't include full vault path, prepend: `/mnt/c/Users/carey/Documents/SyncVaultC/Blog Ideas and Posts/`

If no args:
- Ask user for the file path

Use Read tool to read the entire file.

## Step 2: Analyze the Post

Perform comprehensive analysis across these dimensions:

### A. Voice & Style Analysis

**Check for AI-y language patterns:**
- Excessive hedging phrases
- Generic superlatives ("incredibly powerful", "truly amazing")
- Unnecessary qualifiers ("very", "quite", "rather")
- Overly formal or corporate language
- Repetitive sentence structures
- Saying things twice unnecessarily

**Verify voice consistency:**
- Does it sound like the author's authentic voice?
- Any sections that feel "smoothed over" or generic?
- Is the edge/sarcasm landing or does it feel forced?
- Technical precision maintained throughout?

### B. SEO & Structure Analysis

**Headline/Title:**
- Is it compelling and clear?
- Does it accurately represent the content?
- Optimal length (50-60 characters for SEO)?
- Does it have a hook?

**Subheadings (H2, H3):**
- Clear hierarchical structure?
- Descriptive and keyword-rich?
- Break up long sections?
- Help with skimmability?

**Meta Description (if present in frontmatter):**
- 150-160 characters?
- Compelling summary?
- Includes target keywords?

**Content Structure:**
- Clear introduction that hooks reader?
- Logical flow between sections?
- Conclusion that reinforces main points?
- Post length appropriate for topic?

**Keywords:**
- Are main keywords used naturally throughout?
- Good keyword density without stuffing?
- Variations of main terms?

### C. Clarity & Readability

**Paragraph length:**
- Are paragraphs too long (> 4-5 sentences)?
- Do they each focus on one idea?
- Good mix of short and medium paragraphs?

**Sentence variety:**
- Mix of short and long sentences?
- Avoid too many sentences starting the same way?
- Active voice where appropriate?

**Transitions:**
- Smooth flow between paragraphs?
- Clear logical connections?
- Signposting for reader orientation?

**Repetition:**
- Same words/phrases overused?
- Same point made multiple times without adding value?
- Redundant modifiers?

**Jargon & Accessibility:**
- Technical terms explained where needed?
- Balance between expertise and accessibility?
- Acronyms defined on first use?

### D. Argument Strength (Light Check)

**Not a deep critique** (that's the blog-critique skill), but flag:
- Claims that need support
- Weak transitions in logic
- Sections that drag or could be tightened

### E. Publication Checklist

- Title/headline present?
- Author/date in frontmatter?
- All links working (no broken [[wikilinks]])?
- Images referenced are present?
- Proper formatting throughout?
- No placeholder text ([TK], [INSERT], etc.)?
- Consistent voice throughout?

## Step 3: Create Proofreading Report

Create report at:
```
/mnt/c/Users/carey/Documents/SyncVaultC/Blog Ideas and Posts/YYYY-MM-DD - TITLE/[post-name]-proofread.md
```

If folder doesn't exist, save to same directory as source:
```
[post-name]-proofread.md
```

Use this format:

```markdown
---
title: Proofread Report
date: YYYY-MM-DD
source: [filename]
status: Ready for Review
---

# Proofread Report: [Post Title]

**Source:** `[path]`
**Word Count:** [count]
**Reviewed:** YYYY-MM-DD

## Overall Assessment

[2-3 sentence summary of the post's readiness for publication]

**Strengths:**
- [What's working well]
- [Strong elements]

**Areas for Improvement:**
- [Main issues to address]
- [Priority fixes]

---

## Voice & Style

### AI-y Language to Remove

#### Line [X]: [Phrase]
```
[Context around the phrase]
```
**Issue:** [What makes this sound AI-y]
**Suggestion:** [How to rephrase in author's voice]

#### Line [Y]: Hedging language
```
It's worth noting that privacy regulations...
```
**Issue:** Unnecessary hedging - makes point weaker
**Suggestion:** "Privacy regulations..." (just state it directly)

### Voice Consistency

[Overall assessment of whether voice is consistent throughout. Flag any sections that feel off.]

**Sections that need attention:**
- Lines [X-Y]: Feels too formal/corporate
- Lines [A-B]: Lost the edge/sarcasm here

---

## SEO & Structure

### Headline
**Current:** [headline]
**Assessment:** [strength/weaknesses]
**Character count:** [count] (optimal: 50-60)
**Suggestions:**
- [Alternative if needed]

### Subheadings
**Current structure:**
```
H1: [title]
H2: [subhead 1]
H3: [subhead 1.1]
H2: [subhead 2]
...
```

**Issues:**
- [Any hierarchy problems]
- [Missing subheadings in long sections]
- [Unclear or generic subheads]

**Suggestions:**
- Line [X]: Add H2 subheading here to break up long section
- Line [Y]: Current H2 "[title]" could be more descriptive

### Meta Description
**Current:** [if present]
**Status:** [Missing / Too short / Too long / Good]
**Character count:** [count] (optimal: 150-160)
**Suggestion:** [If needed]

### Keywords & Topics
**Main keywords identified:** [list]
**Usage:** [Natural / Forced / Missing opportunities]
**Suggestions:** [If any]

---

## Clarity & Readability

### Long Paragraphs
**Lines [X-Y]:** [number] sentences - consider breaking up
**Lines [A-B]:** [number] sentences - consider breaking up

### Weak Transitions
**Between sections [X] and [Y]:**
```
[Show the transition]
```
**Issue:** Abrupt jump between topics
**Suggestion:** Add transition sentence that connects [previous concept] to [new concept]

### Repetition
**Word/phrase "[term]" used [X] times**
Lines: [line numbers]
**Suggestion:** Vary with synonyms: [alternatives]

**Concept repeated:**
Lines [X] and [Y] both make the same point about [topic]
**Suggestion:** Consolidate or cut one

### Sentence Structure Issues

#### Passive voice (where active is better)
**Line [X]:**
```
The data was collected by OpenAI...
```
**Suggestion:** "OpenAI collected the data..."

#### Starting sentences the same way
Lines [X-Z] all start with "The [thing]..."
**Suggestion:** Vary sentence openings for better flow

---

## Argument & Logic

### Weak Claims Needing Support
[Only flag obvious ones - full critique is separate skill]

**Line [X]:** Claim needs evidence
```
[The claim]
```
**Suggestion:** Add source or data

### Sections That Could Be Tightened
**Lines [X-Y]:** [Section name]
**Issue:** This section meanders / is repetitive / loses focus
**Suggestion:** [How to tighten]

---

## Publication Checklist

- [x] Title present
- [x] Author/date in frontmatter
- [ ] All images referenced exist
- [x] Links functional
- [x] No placeholder text
- [ ] Consistent voice throughout
- [x] No obvious typos

**Items needing attention:**
1. [Item]
2. [Item]

---

## Priority Fixes (Do These First)

1. **[Highest priority issue]** - Lines [X-Y]
2. **[Second priority]** - Line [X]
3. **[Third priority]** - Throughout

## Polish Fixes (Optional)

- [Nice-to-have improvements]
- [Minor style tweaks]

---

## Suggested Edits

[If there are specific line edits that would improve the piece, include them here]

**Line [X]:**
```
Current: [text]
Suggested: [improved text]
Reason: [why this is better]
```

---

## Notes

[Any additional observations, patterns noticed, or general feedback about the piece]
```

## Step 4: Report to User

Tell the user:
```
Proofreading complete! Report saved to: [path]

Summary:
- [X] voice/style issues flagged
- [Y] SEO improvements suggested
- [Z] clarity fixes needed

Priority: [High/Medium/Low priority fixes needed]
```

</process>

<specific_checks>

## AI-y Language Red Flags

Search for these patterns (case insensitive):

**Hedging phrases:**
- "it's worth noting"
- "it's important to"
- "one might argue"
- "it could be said"
- "in some ways"
- "to some extent"

**Generic enthusiasm:**
- "incredibly" (unless used sarcastically)
- "absolutely amazing/powerful/critical"
- "truly remarkable"
- "extremely important"

**Overused qualifiers:**
- "very" (usually unnecessary)
- "quite"
- "rather"
- "somewhat"

**Corporate speak:**
- "leverage" (unless mocking)
- "synergy"
- "paradigm shift"
- "best practices" (unless in quotes/mocking)

**Redundant pairs:**
- "first and foremost"
- "each and every"
- "hopes and dreams"
- "quick and easy"

## SEO Best Practices

**Title:**
- 50-60 characters for Google SERP
- Front-load important keywords
- Make it compelling, not just descriptive

**Meta description:**
- 150-160 characters
- Include target keyword
- Call to action or hook
- Avoid truncation

**Headings:**
- H1: One per page (the title)
- H2: Main sections
- H3: Subsections
- Don't skip levels (no H1 -> H3)
- Use keywords naturally

**Content:**
- Target keyword in first 100 words
- Use variations throughout
- Internal/external links to authoritative sources
- Break up text with lists, quotes, images

</specific_checks>

<style_notes>

- Be specific: Always cite line numbers and show context
- Be actionable: Don't just say "improve this", suggest how
- Respect the voice: Don't smooth out the edge
- Prioritize: Separate "must fix" from "nice to have"
- Stay practical: Focus on changes that matter for publication

</style_notes>

<key_reminders>

1. **Preserve the edge** - Don't suggest softening strong language
2. **Flag AI-y patterns** - These undermine authenticity
3. **SEO matters** - But not at the expense of voice
4. **Be thorough** - This is the final check before publishing
5. **Give context** - Explain WHY something should change
6. **Prioritize** - Help author focus on what matters most

</key_reminders>
