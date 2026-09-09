# Critique Output Template

Write the critique file using this structure. Replace bracketed placeholders
with real content from the dialogue. Omit any section that had no findings —
do not include empty headers or invented filler.

```markdown
---
title: Critique - [Original Post Title]
date: [YYYY-MM-DD from `date +%Y-%m-%d`]
original-file: [full path to the source post]
status: Draft
---

# Critique: [Original Post Title]

## Summary
[Brief overview of the critique session and the main points strengthened.]

## Evidence Gaps Identified

### [Short name for the gap]
- **Claim**: [The claim needing support, quoted from the post]
- **Location**: Line [N]
- **Issue**: [Why more evidence is needed]
- **Addressed**: [How it was resolved in dialogue, or "Pending"]
- **Suggestions**: [Specific sourcing or data to add]

## Counterarguments Considered

### [Short name for the counterargument]
- **Opposing View**: [The strongest version of what critics would say]
- **Who makes it**: [Which constituency — industry, academics, skeptics]
- **Response**: [How to address it]
- **Strength**: [Honest assessment of how well the response holds]

## Logical Weaknesses

### [Short name]
- **Location**: Line [N]
- **Issue**: [The logical gap]
- **Impact**: [How it affects the overall argument]
- **Resolution**: [How to fix it]

## Additional Sourcing Suggestions
- [Specific source, with why it helps]

## Remaining Items to Address
- [ ] [Concrete action]

## Notes from Dialogue
[Key insights, clarifications, or context that emerged in conversation —
especially things the author knows but hadn't written down.]

## Out of Scope (noted, not audited)
[One line each, if anything came up: formatting issues → run blog-linter;
prose/voice issues → run blog-proofreader.]
```
</content>
