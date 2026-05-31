---
title: "Computational Life: How Well-formed, Self-replicating Programs Emerge from Simple Interaction"
type: source
url: https://arxiv.org/abs/2406.19108
local_path: raw/2406.19108v2.pdf
code: https://github.com/paradigms-of-intelligence/cubff
author: Blaise Agüera y Arcas, Jyrki Alakuijala, James Evans, Ben Laurie, Alexander Mordvintsev, Eyvind Niklasson, Ettore Randazzo, Luca Versari
affiliations: Google (Paradigms of Intelligence Team); University of Chicago (Evans)
published: 2024-06-27
revised: 2024
ingested: 2026-05-31
format: pdf
tags: [artificial-life, alife, self-replication, origins-of-life, emergence, complexity, brainfuck, bff, forth, subleq, z80, kolmogorov-complexity, aguera-y-arcas, paradigms-of-intelligence]
---

## Summary

When **random, non-self-replicating programs** are dropped into a soup with **no explicit fitness function, no selection, and no reward**, **self-replicators reliably emerge on their own** — purely from random interactions and self-modification, with or without background mutation. Once they appear there's a sharp **state transition** from "pre-life" to "life," after which **increasingly complex dynamics keep emerging**. The [Google Paradigms of Intelligence Team](../entities/blaise-aguera-y-arcas.md) (+ U. Chicago) demonstrate this across several computational substrates and even **real CPU instruction sets**, and give one **counterexample** substrate (SUBLEQ) where it doesn't happen. It's an Artificial-Life / Origins-of-Life argument that **self-replication and open-ended complexity are generic, near-inevitable outcomes of simple interacting code** — not rare accidents requiring fine-tuned conditions.

## Key claims

- **Spontaneous emergence without selection.** In an environment "lacking any explicit fitness landscape," self-replicators tend to arise from random interactions + **self-modification**; happens **both with and without background random mutation**.
- **Primordial-soup setup** (an isolated-system variant of Fontana's *Turing gas*): a fixed population of byte "tapes"; each **epoch** picks random ordered pairs of programs, **concatenates** them, and **executes the combined code** for a fixed number of steps. **No programs are added or removed** — all change comes from self-modification or background mutation. Programs read/write on the **same shared tape**, which is what lets one program rewrite another (the mechanism behind replication).
- **Sharp state transition, detectable.** The pre-life → life shift shows up as a **rapid drop in unique tokens** + dominance by a few popular tokens. They introduce a novel metric, **"high-order entropy"** = (Shannon entropy over bytes) − (normalized Kolmogorov complexity, i.e. Kolmogorov complexity / n), plus tracer tokens, to detect it.
- **Substrate generality.** Demonstrated on:
  - **BFF** — their extension of the esoteric minimal language **Brainfuck** (8 commands), modified so programs share one read/write tape. Primordial-soup, **spatial** (self-replicators compete for space), and **long-tape** variants.
  - **Forth** — stack-based language; also produces self-replicators (soup + long-tape).
  - **Real-world instruction sets** — a **Zilog Z80** emulator and the **Intel 8080**: self-replication emerges here too, showing the result isn't an artifact of toy languages.
- **Counterexample — SUBLEQ.** In the minimalist one-instruction-set language **SUBLEQ** (and RSUBLEQ4), the pre-life→life transition is **not observed to arise spontaneously**, even though hand-crafted self-replicators exist — and the **shortest hand-crafted SUBLEQ self-replicator is much longer** than in the other substrates. Suggests the *reachability* of short replicators by random walk is what gates emergence.
- **Code released**: [`paradigms-of-intelligence/cubff`](cubff-github.md) ("cubff") — ingested as its own source page; SUBLEQ variants via `--lang subleq` / `--lang rsubleq4`, BFF variants via `--lang bff_noheads` etc.
- **Independently reproduced**: [Jonas Werner's BFF reproduction (2026)](jonas-werner-bff-emergent-complexity.md) reimplements the BFF soup from scratch (C+OpenMP, no relation to cubff) and confirms spontaneous self-replicators + the sharp phase transition on a commodity desktop.

## Entities mentioned
- [Blaise Agüera y Arcas](../entities/blaise-aguera-y-arcas.md) — lead author; leads Google's Paradigms of Intelligence Team.
- Co-authors: Alakuijala, James Evans (U. Chicago), Ben Laurie, **Alexander Mordvintsev** (of Neural Cellular Automata / "Growing CA" fame), Niklasson, Randazzo, Versari.

## Concepts touched
- [Artificial life and the emergence of self-replication](../concepts/alife/artificial-life-and-self-replication.md) — the concept this source anchors.
- High-order entropy / Kolmogorov complexity — complexity metrics (covered on the concept page).

## Why this matters for the wiki
- **Opens a new branch: Artificial Life / emergence / complexity** (new `concepts/alife/` area). Distinct from the wiki's learning / world-model / robotics threads, but intellectually adjacent to the **"what is intelligence, and is LLM-scaling the right paradigm?"** debate the wiki already tracks.
- **A third "paradigm of intelligence" voice.** Where [LeCun](../entities/yann-lecun.md) bets on world models and [Michael I. Jordan](../entities/michael-i-jordan.md) on collectives/economics, **Agüera y Arcas's "Paradigms of Intelligence" framing** treats intelligence/life as **emergent from simple interacting computation** — a complement to the [critiques of the intelligence north star](../syntheses/society/critiques-of-the-intelligence-north-star.md) synthesis.
- **Methodologically resonant with the JEPA thread**: both reject hand-designed objectives — JEPA learns without pixel reconstruction; this work gets complexity **without any fitness function at all**.

## Open questions
- What *exactly* gates emergence? SUBLEQ's failure points at **replicator reachability / minimum description length** under random self-modification, but the paper leaves the precise condition open.
- Relationship to **open-endedness** research and to Mordvintsev's **Neural Cellular Automata** line — a natural next ingest to build out `concepts/alife/`.
- Any connection drawn by the authors between this and large-model "emergence" claims? (The "Paradigms of Intelligence" team framing invites it, but the paper stays within ALife.)
