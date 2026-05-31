---
title: "Neural Cellular Automata: From Cells to Pixels (Pajouheshgar et al., 2025)"
type: source
url: https://arxiv.org/abs/2506.22899
local_path: raw/2506.22899v3.pdf
author: Ehsan Pajouheshgar, Yitao Xu, Ali Abbasi, Alexander Mordvintsev, Wenzel Jakob, Sabine Süsstrunk
affiliations: EPFL; Google Research (Mordvintsev)
venue: "arXiv 2506.22899 (cs.CV); v3 2026-05-01"
published: 2025-06
ingested: 2026-05-31
format: pdf
tags: [neural-cellular-automata, nca, self-organization, morphogenesis, texture-synthesis, mordvintsev, alife, emergence, neural-fields, generative]
---

## Summary

A scaling advance for **Neural Cellular Automata (NCA)** — the learnable-self-organization line originated by co-author **[Alexander Mordvintsev](../entities/alexander-mordvintsev.md)** ("Growing NCA," 2020), who is also a co-author of the wiki's [Computational Life](computational-life-self-replicating-programs-paper.md). NCAs are grids of **identical cells applying a shared, learned local update rule** that self-organize into images/shapes/textures, with built-in **regeneration and robustness**. They had been stuck at low resolution (≈64²–256²). This paper **decouples dynamics from appearance**: run the NCA on a *coarse* grid, then render arbitrary-resolution output with a lightweight **coordinate-based implicit decoder (LPPN)** conditioned on local cell state — keeping everything **local and parallelizable**, and achieving **real-time high-resolution** 2D/3D/mesh morphogenesis and texture synthesis.

## Key claims

- **What NCAs are.** "Bio-inspired dynamical systems in which identical cells iteratively apply a learned local update rule to self-organize into complex patterns, exhibiting regeneration, robustness, and spontaneous dynamics." A small **shared neural update rule** grows images/shapes from a seed and synthesizes textures — learning an *iterative self-organizing process* rather than a direct mapping (hence robustness + regeneration).
- **The resolution problem.** Prior NCAs ran on ≈10⁴–10⁵ cells (64²–256²). Scaling is blocked by (1) **training time/memory growing quadratically** with grid size, (2) **strictly local propagation** (one neighborhood hop/update) impeding long-range coordination, and (3) heavy real-time high-res inference cost.
- **The method — decouple dynamics from appearance.** Evolve the NCA on a **coarse lattice**, but render a continuous high-resolution output via **LPPN**, a lightweight **coordinate-based decoder / neural field** mapping a locally-interpolated cell feature + intra-primitive coordinate → appearance. Same model renders at **arbitrary resolution**; because decoder and NCA updates are both local, inference stays **highly parallelizable**.
- **Training.** Task-specific losses for **morphogenesis** (growth from a seed) and **texture synthesis**, designed for minimal extra memory/compute.
- **Results.** High-resolution, real-time outputs across **2D grids, 3D grids, and mesh domains**, preserving the characteristic self-organizing behavior. Architecture-agnostic (applies to different NCA backbones/targets). Interactive demos at cells2pixels.github.io.
- **Framing.** Opens by situating NCAs in **complex self-organizing systems** — "global structure emerges not from top-down planning but from the collective effect of countless simple local interactions" (particles→molecules→materials; one cell→organism via morphogenesis; neurons→cognition).

## Entities mentioned
- [Alexander Mordvintsev](../entities/alexander-mordvintsev.md) — NCA originator (Google Research); co-author here and on [Computational Life](computational-life-self-replicating-programs-paper.md).
- Ehsan Pajouheshgar, Yitao Xu, Ali Abbasi, **Wenzel Jakob** (Mitsuba renderer), Sabine Süsstrunk — EPFL. *(No standalone pages.)*

## Concepts touched
- [Neural Cellular Automata](../concepts/alife/neural-cellular-automata.md) — the concept this anchors.
- [Artificial life and the emergence of self-replication](../concepts/alife/artificial-life-and-self-replication.md) — NCA is the **learnable** wing of self-organization/morphogenesis (the long-flagged Mordvintsev neighbor of the ALife branch).
- Self-organization, morphogenesis, regeneration, neural fields / implicit decoders, local-rule emergence.

## Open questions
- NCA optimizes a **learned local rule toward a target pattern** (morphogenesis), whereas the wiki's [self-replication](../concepts/alife/artificial-life-and-self-replication.md) line concerns *replication + open-ended evolution*. Mordvintsev bridges both communities (NCA + Computational Life) — whether the two formally connect (e.g. learned vs. evolved vs. emergent local rules) is an open synthesis.
- This is a graphics/CV scaling paper (real-time high-res rendering); the deeper ALife questions (open-endedness, self-replication *within* NCA, e.g. Mordvintsev's self-replicating-NCA work) are referenced but not the focus here.
