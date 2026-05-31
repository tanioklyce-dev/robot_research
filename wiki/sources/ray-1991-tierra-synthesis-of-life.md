---
title: "An Approach to the Synthesis of Life (Ray, 1991) — Tierra"
type: source
local_path: raw/Ray1991AnApproachToTheSynthesisOfLife.pdf
author: Thomas S. Ray
affiliations: School of Life & Health Sciences, University of Delaware
venue: "Artificial Life II (SFI Studies in the Sciences of Complexity, vol. X; eds. Langton, Taylor, Farmer, Rasmussen), Addison-Wesley, p. 371"
published: 1991
ingested: 2026-05-31
format: pdf
tags: [tierra, artificial-life, alife, self-replication, digital-evolution, open-ended-evolution, parasitism, thomas-ray, emergence, complexity, cambrian]
---

## Summary

The **founding Tierra paper** — the work that put **evolving self-replicating programs** on the map. Thomas Ray argues for **synthesizing** (not simulating) life: seed a virtual computer's memory ("the soup") with a single **hand-written 80-instruction self-replicating "ancestor,"** add mutation + a reaper, and let **open-ended evolution by natural selection** run. From that one ancestor, a whole **ecology emerges spontaneously** — parasites, immunity, hyper-parasites, sociality, and cheaters — in a digital parallel to the **Cambrian explosion**. This is the **evolved-digital-replicator** step the wiki's [self-replication lineage](../concepts/alife/artificial-life-and-self-replication.md) had been missing: more than [Darwin](darwin-1961-bell-labs-game.md)/[Core War](dewdney-1984-core-war-scientific-american.md)'s hand-written warriors, less than [Computational Life](computational-life-self-replicating-programs-paper.md)'s from-scratch emergence.

## Key claims

- **Synthesis, not simulation.** Ray's definition of life: a system that is **self-replicating and capable of open-ended evolution**. The aim is to evolve "structures or processes that were not designed-in or preconceived by the creator," paralleling the Cambrian explosion of diversity.
- **Explicitly beyond Core Wars / viruses / worms.** Ray notes those are self-replicating *but not evolving*, and that typical evolutionary simulations are **dead-ended** because they bolt on **pre-defined genes, alleles, and fitness functions** — the simulator copies survivors rather than the organisms containing their own replication machinery. Self-replication is critical precisely so that **selection is not pre-determined**: free creatures **invent their own implicit fitness functions** (e.g. mutual exploitation) the designer would never think of.
- **The Tierra virtual computer.** A block of RAM = the **"soup,"** inoculated with creatures whose **genome is a sequence of machine instructions**. The prototype **ancestor = 80 instructions** (named `80aaa`).
- **Address by template** (borrowed from molecular biology): a `JMP` is followed by a `NOP` pattern, and the CPU searches for the **nearest complementary template** rather than a numeric address — making code robust to relocation/insertion.
- **Memory protection asymmetry → parasitism.** Each creature has **exclusive *write* privileges** in its block, but **read and execute are *not* protected** — others can read and even *execute* your code. This is the mechanism that lets parasites borrow a host's copy routine.
- **Reaper + Slicer (the "operating system").** A **reaper** kills creatures (deallocating memory) once the soup fills (~80%), working off a queue; a **slicer** time-shares CPU across all living creatures via a circular queue (slice size/scaling determines whether selection favors large or small genomes). Dead code is left in the soup.
- **Genebanker.** Names genotypes by **size class + label** (`80aaa`, first size-45 parasite `45aaa`), recording ancestry/phylogeny, birth time, and "metabolic" stats.
- **Emergent ecology from one ancestor** (within ~100M instructions, ~a dozen+ genotypes):
  - **Parasites** (~45 instructions) that lack a copy procedure and execute the host's instead.
  - **Immunity** in hosts; **parasites that circumvent** immunity.
  - **Facultative hyper-parasites** that replicate alone but, when parasitized, **subvert the parasite's energy/control** to replicate themselves.
  - **Sociality** — high genetic relatedness in hyper-parasite communities yields creatures that **only replicate in aggregations**.
  - **Cheaters** — hyper-hyper-parasites that invade those social aggregations.
  - **Size optimization** — selection for smaller/faster replicators; runaway mutation can also bloat genomes or drive a community to **sterile offspring and extinction**.

## Entities mentioned
- [Tierra](../entities/tierra.md) — the system introduced here.
- [Thomas Ray](../entities/thomas-ray.md) — author/creator.
- [Core War](../entities/core-war.md) — cited as self-replicating-but-not-evolving (the predecessor Tierra surpasses).

## Concepts touched
- [Artificial life and the emergence of self-replication](../concepts/alife/artificial-life-and-self-replication.md) — Tierra is the canonical **open-ended digital evolution** system.
- Open-ended evolution, implicit fitness, parasite/host coevolution, digital natural selection.

## Open questions
- Tierra evolves *from a hand-written ancestor*; [Computational Life](computational-life-self-replicating-programs-paper.md) gets replicators *from random code with no ancestor and no fitness*. The axis "designed ancestor + selection → evolution" vs. "no ancestor, no fitness → emergence" is the cleanest framing for the wiki's [self-replication branch](../concepts/alife/artificial-life-and-self-replication.md).
- Later Tierra work (Physica D; network Tierra; the "digital Cambrian" / parallel Tierra) is not ingested here — this is the 1991 foundational paper only.
