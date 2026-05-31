---
title: Tierra
type: entity
subtype: software
created: 2026-05-31
updated: 2026-05-31
sources: 1
tags: [tierra, artificial-life, alife, digital-evolution, self-replication, open-ended-evolution, parasitism, thomas-ray]
---

**Tierra** is a **digital-evolution system** (1991) created by **[Thomas Ray](thomas-ray.md)**: a virtual computer whose memory ("the soup") is seeded with a hand-written **self-replicating machine-code "ancestor,"** which then undergoes **open-ended evolution by natural selection**. It is the canonical demonstration that **a rich ecology can evolve from a single self-replicating program** — the evolved-digital-replicator landmark between [Core War](core-war.md)'s hand-written warriors and [Computational Life](../sources/computational-life-self-replicating-programs-paper.md)'s from-scratch emergence.

## How it works
- **Soup + ancestor.** A block of RAM holds creatures whose **genome is a sequence of machine instructions**; the prototype ancestor is **80 instructions** ([Ray 1991](../sources/ray-1991-tierra-synthesis-of-life.md)).
- **Address by template** (molecular-biology-inspired): jumps target the nearest complementary `NOP` pattern, not a numeric address.
- **Write-protected, read/execute-open memory** — the asymmetry that enables **parasitism** (a parasite executes a host's copy routine).
- **Reaper** (kills creatures as the soup fills) + **slicer** (time-shares CPU via a circular queue); a **genebanker** tracks genotypes/phylogeny (`80aaa`, `45aaa`, …).

## Why it matters for this wiki
- **Open-ended digital evolution.** From one ancestor, Tierra spontaneously evolves **parasites, immunity, hyper-parasites, sociality, and cheaters** — a digital "Cambrian explosion." Ray's definition of life (**self-replicating + open-endedly evolving**) explicitly rules out non-evolving [Core War](core-war.md)/viruses and pre-defined-fitness simulations.
- **Lineage position:** von Neumann → [Darwin](../sources/darwin-1961-bell-labs-game.md) (1961) → [Core War](core-war.md) (1984) → **Tierra (1991)** / [Avida](avida.md) (1994) → [Computational Life](../sources/computational-life-self-replicating-programs-paper.md). Tierra adds **evolution** to hand-written replicators; Computational Life later removes the need for a designed ancestor *or* fitness. See [artificial life and the emergence of self-replication](../concepts/alife/artificial-life-and-self-replication.md).

## Related
- [Avida](avida.md) — the explicitly **tierra-inspired** spatial successor.

## Mentioned in
- [An Approach to the Synthesis of Life (Ray, 1991)](../sources/ray-1991-tierra-synthesis-of-life.md)
- [Evolutionary Learning in … 'Avida' (Adami & Brown, 1994)](../sources/adami-brown-1994-avida.md) — cites Tierra as its inspiration.
