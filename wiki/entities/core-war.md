---
title: Core War
type: entity
subtype: software
created: 2026-05-31
updated: 2026-05-31
sources: 3
tags: [core-war, programming-game, self-replication, redcode, mars, artificial-life, alife, von-neumann, digital-evolution, retro]
---

**Core War** is a 1984 **programming game** in which two or more programs — **"warriors"** written in an assembly language called **Redcode** — are loaded into a shared **circular memory** and **execute concurrently** inside a virtual machine. Each warrior tries to crash the others (force them onto a non-executable `DAT` instruction) while surviving; the last one still running wins. Created by **[A. K. Dewdney](ak-dewdney.md)** and **David Jones** at the University of Western Ontario, and introduced to the public in Dewdney's May 1984 [*Scientific American* "Computer Recreations" column](../sources/dewdney-1984-core-war-scientific-american.md).

## How it works
- **Circular core.** A ring of (classically) **8,000 addresses**; warriors use **relative addressing only**.
- **MARS** (Memory Array Redcode Simulator) time-shares execution, running one instruction per warrior in alternation. **[pMARS](../sources/pmars-koth.md)** is the de-facto standard portable simulator.
- **Redcode** instructions: `MOV`, `ADD`/`SUB`, `JMP`, `JMZ`/`JMG`, `DJZ`, `CMP`, `DAT`; addressing modes direct / indirect (`@`) / immediate (`#`). Standardized later as **ICWS '88** and **ICWS '94**.

## Why it matters for this wiki
- **The self-replicating programming game.** Its canonical warrior, the **Imp** (`MOV 0 1`), is a one-instruction **self-replicator** that copies itself through memory — making Core War the **self-replication-relevant** member of the programming-game family, vs. the non-replicating [CRobots](../sources/crobots-github.md).
- **A cultural ancestor of the wiki's [self-replicating-code branch](../concepts/alife/artificial-life-and-self-replication.md).** The lineage runs from von Neumann's self-replicating-machine theory → **[Darwin](../sources/darwin-1961-bell-labs-game.md)** (Bell Labs, 1961 — Core War's direct ancestor) / Worm (Shoch) / Core War (hand-written replicators, 1984) → **[Tierra](tierra.md) / [Avida](avida.md)** (evolved digital replicators, 1990s) → **[Computational Life / BFF](../sources/computational-life-self-replicating-programs-paper.md)** (replicators that *emerge* from a self-modifying-code soup with no fitness function).
- **Warriors are hand-written, not evolved** — the contrast that makes Tierra/Avida and Computational Life the natural "and then it evolves / emerges" successors.

## Warrior archetypes (from Dewdney 1984)
- **Imp** — minimal self-replicator (crawls forward copying itself).
- **Dwarf** — stationary bomber dropping zeros at fixed intervals.
- **Gemini / Juggernaut / Bigfoot** — self-copying relocators (prime-interval evasion).
- **Raidar / Scanner** — self-repairing programs with redundant copies.

## People
- [A. K. Dewdney](ak-dewdney.md) — co-creator; *Scientific American* columnist who popularized it.
- David Jones — co-creator (University of Western Ontario). *(No standalone page.)*

## Mentioned in
- [Dewdney 1984 — Core War (Scientific American)](../sources/dewdney-1984-core-war-scientific-american.md)
- [pMARS — Portable Redcode Simulator (KOTH.org)](../sources/pmars-koth.md)
- [corewars.org — community hub](../sources/corewars-org.md)
- [CRobots (troglobit/crobots)](../sources/crobots-github.md) — non-replicating programming-game cousin.
