---
title: Neural Cellular Automata (NCA)
type: concept
created: 2026-05-31
updated: 2026-05-31
sources: 1
tags: [neural-cellular-automata, nca, self-organization, morphogenesis, cellular-automata, regeneration, emergence, alife, neural-fields, mordvintsev]
---

**Neural Cellular Automata (NCA)** are cellular automata whose **local update rule is a small learned neural network**, shared identically across all cells. Starting from a seed (or noise), cells repeatedly read their neighborhood and update their own state; over many steps the grid **self-organizes** into a target pattern — an image, a 3D shape, or a texture. Because an NCA learns an **iterative self-organizing process** rather than a one-shot input→output mapping, it naturally exhibits **regeneration** (regrow after damage), **robustness**, and **spontaneous dynamics** — making it the **learnable** member of the wiki's self-organization / morphogenesis family.

## Definition / mechanics
- **Shared local rule.** Every cell runs the same neural update; there is **no central controller** — global structure is the emergent result of countless simple local interactions ([Pajouheshgar et al. 2025](../../sources/pajouheshgar-2025-nca-cells-to-pixels.md)).
- **Trained by backprop through time.** The update rule is optimized (e.g. toward a target image or texture) by unrolling many CA steps and differentiating — bridging gradient learning and CA-style emergence.
- **Known limits & a fix.** Classic NCAs were stuck at ≈64²–256² (quadratic training cost; one-neighborhood-hop-per-step long-range coupling). [Pajouheshgar et al. 2025](../../sources/pajouheshgar-2025-nca-cells-to-pixels.md) **decouple dynamics from appearance** — evolve the NCA on a coarse grid, render arbitrary-resolution output with a local coordinate-based decoder (LPPN) — for real-time high-res 2D/3D/mesh outputs.

## Key references
- [Neural Cellular Automata: From Cells to Pixels (Pajouheshgar et al., 2025)](../../sources/pajouheshgar-2025-nca-cells-to-pixels.md) — high-resolution NCA via implicit decoding (the ingested source).
- Lineage (not separately ingested): Mordvintsev et al., "Growing Neural Cellular Automata" (Distill, 2020); Niklasson et al. texture NCA (2021); Pajouheshgar et al. DyNCA / mesh NCA (2023–24).

## Related concepts
- [Cellular automata](cellular-automata.md) — the **parent concept**: NCA is a classical CA whose hand-written local rule is replaced by a learned neural net. Conway's [Game of Life](../../entities/game-of-life.md) is the hand-designed-rule reference point.
- **Synthesis:** [Local rules, global complexity: learned vs. evolved vs. emergent self-organization](../../syntheses/alife/local-rules-global-complexity.md) — situates NCA (the *learned* corner) against evolved (Tierra/Avida) and emergent (Computational Life) self-organization.
- [Artificial life and the emergence of self-replication](artificial-life-and-self-replication.md) — NCA is the **learnable self-organization** wing; contrast the digital-evolution line (Tierra/Avida) which *evolves* rules and the Computational Life soup where replicators *emerge*. NCA instead *learns* a local rule toward a target.
- [Evolutionary computation](evolutionary-computation.md) — alternative (gradient-free) route to designing self-organizing/embodied systems.
- [Flocking and boids](flocking-and-boids.md) — hand-designed local rules → emergence; NCA is the learned-rule counterpart.

## Current state
NCAs are an active niche spanning ALife, generative graphics, and morphogenesis. The [2025 "Cells to Pixels" paper](../../sources/pajouheshgar-2025-nca-cells-to-pixels.md) removes the resolution ceiling. A notable wiki connection: **[Alexander Mordvintsev](../../entities/alexander-mordvintsev.md)** originated NCA *and* co-authored [Computational Life](../../sources/computational-life-self-replicating-programs-paper.md), tying the learnable-self-organization and emergent-self-replication threads to one researcher.

## Mentioned in
- [Neural Cellular Automata: From Cells to Pixels (Pajouheshgar et al., 2025)](../../sources/pajouheshgar-2025-nca-cells-to-pixels.md)
