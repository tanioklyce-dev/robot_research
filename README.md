# Robot Research

A personal knowledge base on **agentic robotics** — robots controlled by AI agents (LLMs, VLAs, world models) — built using the LLM Wiki pattern.

The wiki is maintained by [Claude Code](https://claude.ai/code); the human curates sources and asks questions. As of the initial commit, 50 wiki pages cover NVIDIA's Physical AI stack (Isaac Sim/Lab, Newton, Cosmos, GR00T), AGIBOT's Genie Sim 3.0 + Genie Envisioner, MuJoCo Playground, Genesis, RoboCasa365, ManiSkill, Hello Robot's Stretch + stretch_ai, Robot Utility Models, and the JEPA line (V-JEPA 2, LeWorldModel).

## Structure

```
.
├── CLAUDE.md       # Wiki schema + ingest/query/lint workflows.
│                   # Loaded automatically by Claude Code in this directory.
├── raw/            # Immutable source documents (PDFs, articles, transcripts).
│                   # Read-only for the LLM.
└── wiki/           # LLM-maintained markdown — the knowledge base itself.
    ├── index.md            # always-current catalog
    ├── log.md              # append-only chronological record
    ├── sources/            # one page per ingested source
    ├── entities/           # companies, simulators, robots, products
    ├── concepts/           # technical concepts (VLA, JEPA, sim-to-real, ...)
    └── syntheses/          # cross-cutting analyses
```

## Where to start

- **[`wiki/index.md`](wiki/index.md)** — catalog of every page; the **Highlights** section at the top of the index is the curated entry-point list.
- **[`wiki/log.md`](wiki/log.md)** — chronological record of ingests, queries, and lint passes.
- **[`CLAUDE.md`](CLAUDE.md)** — wiki schema and ingest/query/lint workflows.

Best read in [Obsidian](https://obsidian.md/) — the `wiki/` directory is configured as a vault. Wikilinks use `[[slug|Display]]` form (kebab-case filenames + human-readable display text), so they also render correctly in any plain markdown viewer.

## Working with the wiki

Run **Claude Code** in the project root:

- **Ingest a source** — drop a file into `raw/` (or hand Claude a URL), then ask it to ingest. Claude writes a source page, updates or creates relevant entity/concept pages, refreshes the index, and appends to the log.
- **Ask a question** — Claude reads the index first, navigates relevant pages, and answers with citations. Non-trivial syntheses can be filed back as new wiki pages.
- **Lint** — ask Claude to lint the wiki and it'll surface orphan pages, broken wikilinks, source-count drift, contradictions, and coverage gaps.

Full schema, page conventions, and workflows are in [`CLAUDE.md`](CLAUDE.md).

## What is this pattern?

The **LLM Wiki pattern**: instead of treating LLMs as RAG over raw documents, build and maintain a structured wiki *between* you and the sources. The LLM does the bookkeeping — cross-references, summaries, contradiction-flagging — that humans typically abandon wikis over. The wiki is a compounding artifact: every ingested source enriches it, and answers come from the wiki rather than being re-derived from raw documents on every query.

This repository is one specific instance, focused on robotics research.
