---
title: Artificial life and the emergence of self-replication
type: concept
created: 2026-05-31
updated: 2026-05-31
sources: 3
tags: [artificial-life, alife, self-replication, origins-of-life, emergence, complexity, open-endedness, kolmogorov-complexity, cellular-automata, flocking, boids]
---

**Artificial Life (ALife)** studies "life as it could be" — the general principles of living/complex systems abstracted away from biochemistry. A central question: **how does self-replication, and then open-ended complexity, arise from non-living "pre-life" dynamics?** This concept page anchors the wiki's ALife / emergence / complexity branch.

## Core finding (this wiki's anchor source)
[**"Computational Life" (Agüera y Arcas et al., 2024)**](../../sources/computational-life-self-replicating-programs-paper.md): in a soup of **random, interacting, self-modifying programs with no fitness function and no selection**, **self-replicators reliably emerge on their own**, triggering a sharp **pre-life → life state transition** after which complexity keeps increasing. Key points:
- **No objective required.** Replication is not selected for — it arises from random interaction + self-modification (with or without background mutation). This is the striking part: complexity without a designed reward.
- **Substrate-general.** Shown in **BFF** (an extended Brainfuck where programs share one read/write tape), **Forth**, and **real CPU instruction sets** (Zilog **Z80**, Intel **8080**) — not just toy languages.
- **A counterexample bounds the claim.** In **SUBLEQ** (a one-instruction set) spontaneous emergence is **not** observed, and the shortest hand-crafted self-replicator is much longer — implicating **reachability of short replicators under random self-modification** as the gating condition.
- **Independently reproduced.** [Jonas Werner's BFF reproduction (2026)](../../sources/jonas-werner-bff-emergent-complexity.md) reimplements the BFF soup from scratch (C+OpenMP) and confirms the spontaneous-replicator result and its sharp phase transition (he calls it **"gelation"**) — operations/interaction jumping ~700→6,000–12,000 as diversity collapses — on a commodity desktop in minutes, on multiple random seeds.

## Mechanism
The enabling ingredient is a **shared read/write substrate**: when randomly paired programs are concatenated and executed on a common tape, one program can rewrite another. Self-modification + this shared medium make self-replicating motifs reachable by random walk; once a replicator appears it spreads and **takes over the soup** (the "life" phase). Setup follows an isolated-system variant of **Fontana's Turing gas**.

## Detecting the transition — "high-order entropy"
The paper introduces **high-order entropy** = (Shannon entropy over tokens/bytes) − (**normalized Kolmogorov complexity**, i.e. Kolmogorov complexity ÷ length). Together with **tracer tokens**, it flags the state transition as a **collapse in unique tokens** and dominance by a few motifs — a quantitative signature of emergent order distinct from raw entropy.

## Why it matters
- A concrete, reproducible demonstration that **self-replication and rising complexity are generic outcomes** of simple interacting computation — relevant to Origins-of-Life debates and to "life as it could be."
- **Connects to the wiki's intelligence-paradigms thread.** It's the [Paradigms of Intelligence](../../entities/blaise-aguera-y-arcas.md) view: intelligence/life as **emergent from simple interaction**, a complement to [LeCun](../../entities/yann-lecun.md)'s world-models bet and [Michael I. Jordan](../../entities/michael-i-jordan.md)'s collectivist/economic view — see [critiques of the intelligence north star](../../syntheses/society/critiques-of-the-intelligence-north-star.md).
- **Methodological echo of [JEPA](../world-models/jepa.md)**: both get useful structure *without a hand-designed objective* — JEPA predicts in latent space instead of reconstructing pixels; this gets complexity with **no fitness function at all**.

## Related concepts
- [Flocking and boids](flocking-and-boids.md) — sibling emergence model (continuous steering substrate).
- [JEPA](../world-models/jepa.md) — objective-light learning (different domain, same anti-hand-design spirit).
- Open-endedness, cellular automata, self-organization — **not yet covered**; natural neighbors as this branch grows (e.g. co-author Mordvintsev's Neural Cellular Automata line).

## Mentioned in
- [Computational Life (Agüera y Arcas et al., 2024)](../../sources/computational-life-self-replicating-programs-paper.md)
- [cubff (paradigms-of-intelligence/cubff)](../../sources/cubff-github.md) — the runnable engine for the anchor result.
- [BFF — Emergent Complexity experiment (Jonas Werner)](../../sources/jonas-werner-bff-emergent-complexity.md) — independent CPU reproduction of the BFF result.
