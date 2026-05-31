---
title: "BFF — Emergent Complexity experiment (Jonas Werner)"
type: source
url: https://jonamiki.com/posts/bff-emergent-complexity-experiment/
code: https://github.com/jonas-werner/bff-emergent-complexity
author: Jonas Werner
published: 2026-03-07
ingested: 2026-05-31
format: blog
license: CC BY 4.0
tags: [artificial-life, alife, self-replication, emergence, complexity, brainfuck, bff, reproduction, primordial-soup, xenobots, kolmogorov-complexity]
---

## Summary

An **independent, from-scratch reproduction** of the BFF "primordial soup" experiment from ["Computational Life" (Agüera y Arcas et al., 2024)](computational-life-self-replicating-programs-paper.md). Jonas Werner reimplements the self-modifying Brainfuck-variant soup (C + OpenMP engine, Python orchestration) and **independently confirms the headline result**: with **no fitness function, no selection, no design**, self-replicating programs spontaneously emerge from random data and trigger a sharp **"gelation" phase transition**. The post is a hands-on corroboration — runnable on a 12-thread desktop in minutes — plus the author's own metrics (operations/interaction, lineage diversity, compressibility) and a more speculative philosophical coda (primordial-soup abiogenesis, Xenobots, Hoffman's "Fitness Beats Truth").

## Key claims

- **Setup replicates the paper's BFF soup.** 1,024 programs × 64 bytes, random init. Each interaction: pick 2 programs at random → **concatenate into a 128-byte tape** → run the BFF interpreter → **split back into two 64-byte programs** replacing the originals. 50,000 epochs = **51.2 M interactions per seed**. No fitness/selection/guidance.
- **BFF = extended Brainfuck.** Only **10 of 256** byte values are valid instructions (rest are no-ops): `.`/`,` copy data between read/write heads, `[`/`]` loop control, plus head-movement operators. Copying is *possible* but not required — matching the paper's shared read/write-tape mechanism.
- **The "gelation" phase transition** (his term for the paper's pre-life→life transition): after thousands of quiet epochs, self-replicators spontaneously appear. Signatures:
  - **Operations/interaction** jump from **~700 (baseline noise) to 6,000–12,000** (active replication).
  - **Program diversity collapses** from tens of thousands of unique lineages to a handful.
  - **Compressibility rises** once near-identical replicators dominate — his stand-in for the paper's high-order-entropy / Kolmogorov signal.
- **Consistent across random seeds** without intervention. Two illustrative runs:
  - **Seed 5 — "crash, compete, rebuild":** stable replication for ~15 M interactions → catastrophic collapse at ~20 M when the dominant replicator corrupted → recovery → final **three competing lineages**: BEC0 (977/1,024), 3800 (21), 2BA4 (21).
  - **Seed 3 — "total domination":** smooth uncontested rise → **monoculture**, lineage BEC0 in 1,023/1,024 programs; unique tokens reduced to **209** (from 65,536).
- **Implementation.** Core engine in **C with OpenMP**; orchestration in **Python 3.10+**; static + interactive charts for operations/compressibility/lineage. 51.2 M interactions/seed in *minutes* on a 12-thread desktop — a useful CPU-only reproducibility data point (cf. cubff's CUDA-or-CPU engine).
- **Code released:** [`jonas-werner/bff-emergent-complexity`](https://github.com/jonas-werner/bff-emergent-complexity) — reproducible with a C compiler + Python 3.10+ on standard hardware.

## Entities mentioned
- [Blaise Agüera y Arcas](../entities/blaise-aguera-y-arcas.md) — author of the [Computational Life paper](computational-life-self-replicating-programs-paper.md) this reproduces (via the Google Paradigms of Intelligence Team).
- Jonas Werner — author of the post and reproduction code.
- **Xenobots** (Tufts / U. Vermont, 2021) — referenced as a biological cousin: frog-embryo cells that self-organize into novel forms with unexpected reproductive strategies. *Not yet an entity page.*
- **Donald Hoffman** — "Fitness Beats Truth" theorem, invoked in the philosophical coda. *Not yet a page.*

## Concepts touched
- [Artificial life and the emergence of self-replication](../concepts/alife/artificial-life-and-self-replication.md) — this is an independent reproduction of that concept's anchor result.
- High-order entropy / Kolmogorov complexity / compressibility — the author uses compressibility as a practical proxy for the paper's high-order-entropy transition signal.

## Why this matters for the wiki
- **First independent reproduction of the Computational Life BFF result in the wiki.** Corroborates the central "self-replication emerges with no fitness function" claim across an *independent codebase* — strengthening it from single-source to replicated.
- **Reproducibility data point.** Demonstrates the headline emergence is reachable on a **commodity multi-core CPU in minutes** (C+OpenMP), not requiring the GPU path of [cubff](cubff-github.md) — echoing the wiki's recurring interest in single-machine reproducibility (cf. [LeWM reproduction](onchain-ai-garage-lewm-reproduction.md)).

## Open questions
- The author measures **compressibility** rather than the paper's exact **high-order entropy** (Shannon − normalized Kolmogorov) — how closely the two signals track across the transition isn't quantified here.
- Only the BFF substrate is reproduced; the paper's substrate-generality (Forth, Z80, 8080) and the **SUBLEQ counterexample** are not re-tested in this post.
- The philosophical coda (Hoffman's Fitness-Beats-Truth, "reality as interface," intelligence as a substrate feature) is the author's editorializing, **not** a claim from the Computational Life paper — flagged here to keep the reproduction (solid) separate from the speculation (the author's own).
