---
title: Avida
type: entity
subtype: software
created: 2026-05-31
updated: 2026-05-31
sources: 2
tags: [avida, tierra, artificial-life, alife, digital-evolution, self-replication, open-ended-evolution, cellular-automata, chris-adami, charles-ofria]
---

**Avida** is a **digital-evolution platform** (1994, **[Chris Adami](chris-adami.md)** & C. Titus Brown, Caltech) — a **tierra-inspired** system in which **self-replicating machine-code organisms** live on a **2D spatial grid** with **local, cellular-automaton-style interactions**, evolving under mutation and selection. It became the **most widely used digital-evolution research tool** (long maintained by **Charles Ofria**'s lab, later Michigan State), notably for studying how **computational complexity evolves**.

## How it works
- **Spatial, local.** Organisms occupy cells on an **N×M torus**; on cell division the **oldest neighbor is replaced** — births affect only the local neighborhood. Updates are **K=1 cellular-automaton-like** ([Adami & Brown 1994](../sources/adami-brown-1994-avida.md)).
- **Genomes** are strings of instructions on a configurable virtual CPU (instruction set similar to [Tierra](tierra.md)'s set #4). **Poisson-random point mutation**; insertions/deletions/doublings emerge from the copy process.
- **Task rewards.** Bonus CPU time is granted for performing computations (e.g. **reading and summing integers**) — a fitness landscape "specified only by information," letting complexity evolve from a bare self-replicator.

## Why it matters for this wiki
- **Locality improves evolvability.** Genotype-age power-law exponent **D ≈ 1.14 (Avida) vs. ≈ 1.6 (Tierra)**: local interaction sustains **near-maximal diversity** and avoids Tierra's global-reaper **metastable traps / premature homogenization**. Also distributes across processors near-linearly.
- **Evolving computation.** Demonstrates **evolution of arithmetic** from non-arithmetic replicators — the seed of Avida's famous result on the **evolution of complex features** ([Lenski, Ofria, Pennock & Adami, *Nature* 2003](../sources/lenski-2003-evolutionary-origin-complex-features.md)): the complex EQU function evolves **only when simpler functions are also rewarded** (0/50 vs 23/50).
- **Lineage position:** the spatial successor to [Tierra](tierra.md) in the digital-evolution line (von Neumann → [Darwin](../sources/darwin-1961-bell-labs-game.md) → [Core War](core-war.md) → Tierra/**Avida** → [Computational Life](../sources/computational-life-self-replicating-programs-paper.md)). Unlike Computational Life, Avida still uses an **externally specified reward**. See [artificial life and the emergence of self-replication](../concepts/alife/artificial-life-and-self-replication.md).

## Related
- [Tierra](tierra.md) — the direct inspiration.

## Mentioned in
- [Evolutionary Learning in the 2D Artificial Life System 'Avida' (Adami & Brown, 1994)](../sources/adami-brown-1994-avida.md)
- [The evolutionary origin of complex features (Lenski, Ofria, Pennock & Adami, 2003)](../sources/lenski-2003-evolutionary-origin-complex-features.md)
