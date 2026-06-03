---
title: Conway's Game of Life
type: entity
subtype: system
created: 2026-06-02
updated: 2026-06-02
sources: 1
tags: [game-of-life, cellular-automata, conway, emergence, universality, alife, class-4]
---

The **Game of Life** is a 2D, two-state [cellular automaton](../concepts/alife/cellular-automata.md) invented by mathematician [John Conway](john-conway.md) in **1970** (popularized via Martin Gardner's *Scientific American* column). Despite a single trivial rule it is **Turing-complete** and supports a 50-year engineering subculture — the canonical example of complex behavior from a simple local rule.

## The rule
On an infinite grid of live/dead cells, all updated simultaneously by neighbor count (8-cell Moore neighborhood):
- A **live** cell with **2 or 3** live neighbors survives; otherwise it dies (under/overpopulation).
- A **dead** cell with **exactly 3** live neighbors becomes alive (birth).

## Emergent structures (the engineering vocabulary)
- **Still lifes** — static (block, beehive, the **"eater"** — the most-reused part in later constructions).
- **Oscillators** — periodic (blinker P2, pentadecathlon P15); by **2023** every period is achievable ("omniperiodic").
- **Gliders / spaceships** — patterns that translate across the grid; the glider (period 4) is the workhorse.
- **Glider guns** — emit endless glider streams; the first (period-30) was found by [Bill Gosper](bill-gosper.md) in 1970.
- **Universality** — gliders can be composed into logic gates, a Turing machine, even a [Game of Life running inside the Game of Life](../sources/wolfram-2025-game-of-life-engineering.md) (499×499 cells per meta-cell).

## Why it matters
- The archetypal **Class 4** CA (between order and chaos) — see [cellular automata](../concepts/alife/cellular-automata.md).
- [Stephen Wolfram](stephen-wolfram.md)'s [2025 retrospective](../sources/wolfram-2025-game-of-life-engineering.md) uses its 50-year pattern-discovery record as a clean dataset for studying **innovation itself** — the **construction-vs-search** axis (engineering modular parts vs mining the computational universe).
- Sits in the wiki's [ALife / emergence branch](../concepts/alife/artificial-life-and-self-replication.md) alongside [Tierra](tierra.md), [Avida](avida.md), and [Computational Life](../sources/computational-life-self-replicating-programs-paper.md).

## Related
- [Cellular automata](../concepts/alife/cellular-automata.md) — the general concept.
- [John Conway](john-conway.md) — inventor. [Bill Gosper](bill-gosper.md) — glider gun + Hashlife. [Stephen Wolfram](stephen-wolfram.md) — analyst.
- [Neural Cellular Automata](../concepts/alife/neural-cellular-automata.md) — learned-rule descendant.

## Mentioned in
- [Game of Life engineering essay (Wolfram, 2025)](../sources/wolfram-2025-game-of-life-engineering.md)
