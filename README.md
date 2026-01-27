# Blog Writing Skills for Claude Code

A collection of Claude Code skills for privacy/tech blog writing workflow.

## Skills

### 1. blog-critique (`/blog-critique`)
Engages in iterative dialogue to critique blog posts, focusing on evidence gaps and counterarguments. Preserves the author's voice and edge while strengthening argumentation.

**Usage:**
```
/blog-critique <path-to-blog-post>
```

**What it does:**
- Identifies evidence gaps and weak points
- Steelmans counterarguments
- Tests logical connections
- Creates organized critique file in dated folder structure

**Output:** `Blog Ideas and Posts/YYYY-MM-DD - TITLE/[post-name]-critique.md`

---

### 2. blog-linter (`/blog-linter`)
Lints blog posts for broken footnotes, orphaned references, malformed links, and author TODO notes. Highlights issues and creates detailed report.

**Usage:**
```
/blog-linter <path-to-blog-post>
```

**What it checks:**
- Orphaned footnote references (refs without definitions)
- Orphaned footnote definitions (definitions without refs)
- Malformed links in blockquotes
- Author TODO notes in brackets (`[FIX THIS]`, `[FIND SOURCE]`, etc.)
- Inconsistent footnote numbering
- Unclosed formatting

**Output:** `[post-name]-lint-report.md`

---

### 3. blog-proofreader (`/blog-proofreader`)
Comprehensive proofreading for publication readiness - checks voice consistency, SEO, clarity, flow, and flags AI-y language.

**Usage:**
```
/blog-proofreader <path-to-blog-post>
```

**What it checks:**
- Voice consistency (flags AI-y language, hedging, generic enthusiasm)
- SEO optimization (headlines, subheadings, meta descriptions, keywords)
- Clarity and readability (paragraph length, transitions, repetition)
- Publication checklist (frontmatter, links, images, formatting)

**Output:** `[post-name]-proofread.md`

---

### 4. blog-marketer (`/blog-marketer`)
Generates platform-specific promotional content (Substack Notes, LinkedIn, Bluesky) from published blog posts. Creates multiple variations to choose from while preserving author voice.

**Usage:**
```
/blog-marketer <path-to-blog-post>
```

**What it generates:**
- Substack Notes (3-5 variations, 200-300 chars each)
- LinkedIn posts (2-3 variations, professional but conversational)
- Bluesky threads (1-2 complete threads, casual/edgy)
- Pull quotes (3-5 quotable excerpts, 280 chars max)
- Thread starters (2-3 engagement prompts)

**Output:** `[post-name]-marketing.md`

---

## Workflow

Typical blog post workflow using these skills:

1. **Draft** - Write initial blog post
2. **Critique** - `/blog-critique` for evidence gaps and counterarguments
3. **Revise** - Incorporate feedback, strengthen arguments
4. **Lint** - `/blog-linter` to catch footnote/link issues
5. **Fix** - Resolve linting issues
6. **Proofread** - `/blog-proofreader` for final polish
7. **Publish** - Post is ready!
8. **Market** - `/blog-marketer` to generate promotional content

## Author Style

These skills are tuned for blog posts about:
- Privacy and data protection
- Technology policy
- AI governance
- GDPR/CCPA and data protection law

**Voice characteristics:**
- Sharp, unapologetic critique
- Technical precision
- Evidence-driven arguments
- Conversational but authoritative
- Strategic sarcasm/irony

## Installation

1. Copy skill directories to `~/.claude/skills/`
2. Skills should be automatically available in Claude Code
3. Use `/skill-name` to invoke

## Version Control

Skills are organized in dated folder structures to avoid overwriting:
```
Blog Ideas and Posts/
├── YYYY-MM-DD - Post Title/
│   ├── post.md
│   ├── post-critique.md
│   ├── post-lint-report.md
│   ├── post-proofread.md
│   └── post-marketing.md
```

## License

MIT
