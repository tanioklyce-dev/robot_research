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
│   ├── bio/              # biomechanical simulation, connectomes
│   ├── economics/        # economics-of-ML: collectivist AI, mechanism design, PPI
│   └── alife/            # artificial life, emergence, self-replication, complexity
└── syntheses/        # cross-cutting analyses, comparisons, original thinking
    ├── curriculum/       # the 14-module robot-learning curriculum
    ├── platforms/        # platform comparisons & buying decisions
    ├── projects/         # concrete project scoping (Stretch, ROSOrin Pro)
    ├── world-models/     # JEPA / LeWM / video-WM analysis
    ├── simulators/       # sim stack landscape (Newton, OpenUSD, FRC, ...)
    ├── assistive/        # in-home / PAR / autonomy levels
    ├── agents/           # agentic-AI architecture
    ├── rl/               # RL history & lineage
    └── society/          # AI-and-society / economics-of-ML cross-cutting analyses
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

> **Source-page exception.** `sources/` pages use **`published` + `ingested`** instead of `created`/`updated` (see the [Source pages](#source-pages-sources) section) — a source's "created" date is its publication date and its "updated" event is the ingest. The `created`/`updated` pair above is the convention for **entity / concept / synthesis** pages. `tags` is universal; `sources:` is entity/concept-only.

- **Filenames** — kebab-case slugs (e.g. `nvidia-isaac-sim.md`). No spaces, no special characters. The `title` frontmatter field carries the human-readable version.
- **Links** — Use **standard markdown links with relative paths**, e.g. `[JEPA](../concepts/jepa.md)` from a sibling folder, `[Atlas](atlas.md)` from the same folder. Never use Obsidian `[[wikilinks]]` — GitHub does not resolve them and they render as literal text. Standard markdown links work in both GitHub and Obsidian.
- **Citations** — Every factual claim derived from a source links to the source page (not the raw file): `Atlas can perform parkour ([Boston Dynamics Atlas Demo 2024](../sources/boston-dynamics-atlas-demo-2024.md))`.
- **Contradictions** — When sources disagree, present both with citations and flag with an Obsidian callout: `> [!warning] Contradiction`.
- **Confidence** — For uncertain or hedged claims use `> [!note]` callouts or explicit hedging language.
- **Updates** — When updating a page, bump the `updated` date and `sources` count if relevant.

### Source pages (`sources/`)

One page per ingested source. Filename is a slug of the title (kebab-case). Frontmatter uses `url`, `author`, `published`, `ingested` (plus `title`, `type`, `tags`, and optionally `local_path`, `venue`, `license`, `format`) — **source pages do not carry `created`/`updated`/`sources`**; `published` is the source's own date and `ingested` is when it entered the wiki. Body sections:

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

> [!note] Hub pages: **Mentioned in** is curated, not exhaustive
> Once a page passes roughly **30 inbound source pages**, a hand-maintained inbound list stops being useful and starts being a chore nobody wins at — `vla-models.md` is cited by 110 sources. For those pages, **Mentioned in** lists the sources that *substantively shaped* the page, and carries a marker line giving the true inbound count so the reader knows the list is a selection:
>
> `> [!note] Curated list — N source pages link here; the ones below are those that shaped this page.`
>
> This codifies what was already happening in practice. Do not try to complete these lists; do add a source to one when it genuinely changes what the page says.

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

#### Primary sources for decision-grade claims

**When a vendor or spec claim will be quoted in a buying, flashing, or build decision, ingest the primary as its own source page — release notes, spec tables, datasheets, the paper itself. Do not cite secondary coverage for it.**

Agreement among secondary sources is not corroboration when they are all paraphrasing the same page: three blog posts, forum threads, or vendor landing pages carrying the same number are **one** source. Count distinct *origins*, not distinct URLs.

Two failure modes, both observed on the JetPack 7.2 correction (see `log.md`, 2026-08-16):

- **Scope loss.** Paraphrase preserves the noun phrase and drops what it was bound to. "CUDA 13.0" appeared verbatim on the vendor landing page — attached to a claim about Arm/SBSA target unification, not the bundle version (which was 13.2.1). So the check is not only *is this number right* but *what was this number about in the original*.
- **Omission, which costs more.** Secondaries compress toward the headline, and the decision-relevant content of a release is precisely the un-headline-able part — a "coming soon" on a component you depend on, a boot-failure fix you have to know to apply, a revised figure that inverts a prior finding.

The trigger is not doubt about the claim. It's the document type: if you are summarizing a document's *contents* rather than quoting one fact from it, go to the primary.

Extraction note: primaries are often docs sites where WebFetch silently returns nav menus — curl and strip the `<article>`/`<main>` tag instead (see [NVIDIA JetPack docs index](wiki/sources/nvidia-jetpack-docs-index.md)).

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

### Git

**Commit ingests (and other wiki edits) directly to `main` when the user asks to commit/push — do not branch or open a PR by default.** This is a solo, append-mostly knowledge wiki with no CI and no collaborators, so the usual "branch off the default branch" habit adds ceremony without benefit; one-commit-per-ingest already gives clean, revertable history.

Switch to a branch-based flow (feature branch → PR → review the rendered diff → squash-merge) only when one of these is true: (1) a **collaborator** joins and wants a review surface, (2) a **large or multi-session ingest** needs to be staged and reviewed as a unit before becoming canonical, or (3) the user wants a **draft buffer** for speculative material they may discard. Absent one of those, prefer direct-to-`main`.

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
