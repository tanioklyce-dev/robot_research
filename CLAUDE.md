# Robot Research Wiki

This directory uses the **LLM Wiki pattern**: an LLM-maintained, persistent knowledge base built incrementally from raw sources. The wiki is a compounding artifact — every ingested source enriches it, and answers are synthesized from the wiki rather than re-derived from raw documents each query.

## Three layers

1. **`raw/`** — Source documents. Immutable. Articles, papers, transcripts, images, data files. Read-only for Claude.
   - `raw/assets/` — Local copies of images referenced in sources.
2. **`wiki/`** — Claude-maintained markdown. Summaries, entity pages, concept pages, source pages, syntheses. Claude owns this entirely; the user reads it.
3. **`CLAUDE.md`** (this file) — Schema and conventions. Co-evolves with usage. When workflows or conventions change, update this file.

### User-owned exception: `wiki/notes/`

`wiki/notes/` is the **user's personal notes directory**. **Read-only for Claude — never edit files in this directory unless the user explicitly asks.** It's fine to read these notes for context if relevant to a question. When running lint, treat orphaned pages under `wiki/notes/` as expected (the user's notes don't need to be cross-linked into the rest of the wiki).

## Wiki structure

```
wiki/
├── index.md          # always-current catalog of every page
├── log.md            # append-only chronological record of events
├── sources/          # one page per ingested source
├── entities/         # companies, robots, products, people, labs
├── concepts/         # technical concepts, methods, trends
│   ├── learning/         # imitation, sim-to-real, scaling laws, VLAs, CoT
│   ├── world-models/     # JEPA, latent-space, world-model, siamese, ...
│   ├── agents/           # LLM-agent architecture
│   ├── safety/           # alignment, corrigibility, mech-interp
│   ├── robotics/         # assistive, EUP, optimal control, AprilTags, UAVs, ...
│   └── bio/              # biomechanical simulation, connectomes
└── syntheses/        # cross-cutting analyses, comparisons, original thinking
    ├── curriculum/       # the 14-module robot-learning curriculum
    ├── platforms/        # platform comparisons & buying decisions
    ├── projects/         # concrete project scoping (Stretch, ROSOrin Pro)
    ├── world-models/     # JEPA / LeWM / video-WM analysis
    ├── simulators/       # sim stack landscape (Newton, OpenUSD, FRC, ...)
    ├── assistive/        # in-home / PAR / autonomy levels
    ├── agents/           # agentic-AI architecture
    └── rl/               # RL history & lineage
```

Subfolders are organizational only — links use relative paths across them (e.g. `[JEPA](../concepts/world-models/jepa.md)` from `wiki/sources/`, `[JEPA](../world-models/jepa.md)` from a sibling concept folder). When ingesting a new source, place new concept/synthesis pages in the appropriate subfolder; create a new subfolder only if the topic clearly doesn't fit any existing group.

## Page conventions

All wiki pages start with YAML frontmatter:

```yaml
---
title: <Page Title>
type: source | entity | concept | synthesis
created: 2026-05-06
updated: 2026-05-06
sources: 3              # for entity/concept: count of sources referencing this
tags: [robotics, manipulation]
---
```

- **Filenames** — kebab-case slugs (e.g. `nvidia-isaac-sim.md`). No spaces, no special characters. The `title` frontmatter field carries the human-readable version.
- **Links** — Use **standard markdown links with relative paths**, e.g. `[JEPA](../concepts/jepa.md)` from a sibling folder, `[Atlas](atlas.md)` from the same folder. Never use Obsidian `[[wikilinks]]` — GitHub does not resolve them and they render as literal text. Standard markdown links work in both GitHub and Obsidian.
- **Citations** — Every factual claim derived from a source links to the source page (not the raw file): `Atlas can perform parkour ([Boston Dynamics Atlas Demo 2024](../sources/boston-dynamics-atlas-demo-2024.md))`.
- **Contradictions** — When sources disagree, present both with citations and flag with an Obsidian callout: `> [!warning] Contradiction`.
- **Confidence** — For uncertain or hedged claims use `> [!note]` callouts or explicit hedging language.
- **Updates** — When updating a page, bump the `updated` date and `sources` count if relevant.

### Source pages (`sources/`)

One page per ingested source. Filename is a slug of the title (kebab-case). Frontmatter includes `url`, `author`, `published`, `ingested`. Body sections:

- **Summary** — One paragraph capturing the thesis/main contribution.
- **Key claims** — Bulleted, with timestamp/page/section references where possible.
- **Entities mentioned** — Links to entity pages.
- **Concepts touched** — Links to concept pages.
- **Open questions** — Things this source raises that aren't answered yet.

### Entity pages (`entities/`)

People, companies, robots, products, labs. Body:

- One-line definition at the top.
- Sections organized by topic (e.g. **Capabilities**, **History**, **Funding**, **People**).
- Each claim links to a source page.
- **Mentioned in** section at the bottom: bulleted list of source pages referencing this entity.

### Concept pages (`concepts/`)

Technical ideas (VLA models, sim-to-real, RLHF, whole-body control, etc.). Body:

- Definition.
- **Key references** — seminal sources/papers.
- **Related concepts** — links to other concept pages.
- **Current state** — short paragraph on where the field stands, citing sources.
- **Mentioned in** section.

### Synthesis pages (`syntheses/`)

Cross-cutting analyses created in response to queries (e.g. comparisons, trend analyses, market maps). When a query produces a useful synthesis, offer to file it here so the work compounds rather than disappearing into chat history.

## Workflows

### Ingest

Triggered when the user adds a file to `raw/` and asks to process it.

1. Read the source carefully (and view referenced images if downloaded locally).
2. Briefly surface key takeaways and confirm with the user what to emphasize.
3. Create `wiki/sources/<slug>.md` with the source-page structure above.
4. For every entity mentioned: update an existing entity page or create a new one. Add citations.
5. For every concept touched: update or create a concept page.
6. Update `wiki/index.md` with new pages and bumped source counts.
7. Append an entry to `wiki/log.md`.
8. Flag contradictions with prior knowledge. Surface open questions.

A single ingest typically touches 5–15 wiki pages. That's normal — that's the point.

### Query

Triggered when the user asks a question against the wiki.

1. Read `wiki/index.md` first to find relevant pages.
2. Read those pages and any linked pages they reference.
3. Answer with citations to source pages (not raw sources). Hedge where the wiki is thin or sources disagree.
4. If the answer represents non-trivial synthesis, offer to file it as a `wiki/syntheses/<slug>.md` page and log it.

### Lint

Triggered when the user asks for a health check.

- Contradictions across pages.
- Stale claims (older sources superseded by newer ones — check `updated` dates and source frontmatter).
- Orphan pages (no inbound links).
- Concepts/entities frequently mentioned but lacking their own page.
- Broken links.
- Knowledge gaps that could be filled with a new source or targeted web search.

Report findings as a punch list. Don't auto-fix without user direction.

## index.md format

Catalog organized by category. Each entry: link, one-line summary, source count or date.

```markdown
# Index

## Sources (chronological)
- [Boston Dynamics Atlas Demo 2024](sources/boston-dynamics-atlas-demo-2024.md) — YouTube demo of Atlas parkour. (2024-08-15)

## Entities
### Companies
- [Boston Dynamics](entities/boston-dynamics.md) — Robotics company, owned by Hyundai. (12 sources)
### Robots
- [Atlas](entities/atlas.md) — Humanoid robot from Boston Dynamics. (8 sources)
### People
- [Marc Raibert](entities/marc-raibert.md) — Founder of Boston Dynamics. (4 sources)

## Concepts
- [Whole-body control](concepts/whole-body-control.md) — Coordinating full-body motion for humanoids. (5 sources)

## Syntheses
- [Humanoid form factor tradeoffs](syntheses/humanoid-form-factor-tradeoffs.md) — Cross-player comparison. (2026-04-10)
```

## log.md format

Append-only. Each entry starts with `## [YYYY-MM-DD] <action> | <subject>` so it's grep-able with `grep "^## \[" wiki/log.md | tail -10`.

```markdown
## [2026-05-06] bootstrap | Wiki initialized
## [2026-05-06] ingest | Boston Dynamics Atlas Demo 2024
- Created [Boston Dynamics Atlas Demo 2024](sources/boston-dynamics-atlas-demo-2024.md)
- Updated [Atlas](entities/atlas.md), [Boston Dynamics](entities/boston-dynamics.md)
- New concept: [Whole-body control](concepts/whole-body-control.md)
## [2026-05-06] query | "How do humanoids handle uneven terrain?"
- Synthesized from [Atlas](entities/atlas.md), [Digit](entities/digit.md), [Optimus](entities/tesla-optimus.md)
- Filed as [Humanoid terrain handling](syntheses/humanoid-terrain-handling.md)
```

## Roles

- **User** — curates sources, asks questions, directs the analysis, judges what matters, evolves this schema.
- **Claude** — reads, summarizes, cross-references, files, maintains. Does the bookkeeping so the wiki stays current and consistent. Never modifies `raw/`.
