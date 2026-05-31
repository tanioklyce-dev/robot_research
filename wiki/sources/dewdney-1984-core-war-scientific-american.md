---
title: "Computer Recreations: Core War (Dewdney, Scientific American, May 1984)"
type: source
url: https://corewar.co.uk/dewdney/1984-05.htm
author: A. K. Dewdney
venue: Scientific American — "Computer Recreations" column
published: 1984-05
ingested: 2026-05-31
format: web
tags: [core-war, programming-game, self-replication, redcode, mars, artificial-life, alife, von-neumann, digital-evolution, retro]
---

## Summary

The **founding document of Core War** — A. K. Dewdney's May 1984 *Scientific American* "Computer Recreations" column, which introduced the game to the public. Two or more programs, written in an assembly language called **Redcode**, are loaded into a shared circular memory and **execute concurrently inside a virtual machine (MARS)**, each trying to crash the others while surviving. The column is also a small treatise on **self-replicating and self-repairing programs**: its canonical warrior, the **Imp**, is a single self-copying instruction. This is the **self-replication-relevant programming game** the wiki's ALife branch had flagged as missing (the cousin of the non-replicating [CRobots](crobots-github.md)).

## Key claims / content

- **Origin folklore → real implementation.** Inspired by the (apocryphal) **Creeper/Reaper** story of self-replicating programs spreading across a networked lab; Dewdney traces the real lineage to two earlier programs — **[Darwin](darwin-1961-bell-labs-game.md)** (Vyssotsky/McIlroy/Morris, Bell Labs, 1961) and **Worm** (John F. Shoch, Xerox PARC). Dewdney + student **David Jones** built the actual game at the University of Western Ontario.
- **Circular core.** Memory is a ring of **8,000 addresses** (0–7999, where 8000 ≡ 0). Programs use **relative addressing only** — a warrior can't know its absolute position.
- **MARS (Memory Array Redcode Simulator).** Time-shares execution, running **one instruction from each warrior in alternation** until a program hits a non-executable instruction (it then loses).
- **Redcode instruction set** (between high-level language and machine code): `MOV` (copy), `ADD`/`SUB` (arithmetic), `JMP` (jump), `JMZ`/`JMG` (conditional jumps), `DJZ` (decrement-and-jump-if-zero), `CMP` (compare, skip-if-unequal), `DAT` (non-executable data — landing on it kills a process). Addressing modes: **direct**, **indirect (`@`)**, **immediate (`#`)**.
- **Win condition.** Two programs start ≥1,000 addresses apart; you win by forcing every opposing process onto an unexecutable instruction (a `DAT`). Strategies: **offense** (dropping "bombs" of zeros/`DAT` into opponent code), **defense** (repairing damage), **evasion** (relocating).
- **Canonical warriors:**
  - **Imp** — the minimal self-replicator: `MOV 0 1` copies itself one address forward each cycle, crawling through the core leaving a trail of copies.
  - **Dwarf** — a stationary "bomber" that drops zeros every fifth address, eventually sweeping the whole array; "no stationary battle program with more than four instructions can avoid taking a hit from Dwarf."
  - **Gemini** — a template **self-copying** program that relocates itself ~100 addresses ahead (variants: **Juggernaut**, **Bigfoot** using prime-interval steps to evade).
  - **Raidar / Scanner** — **self-repairing** programs that keep redundant copies and scan for corruption, restoring damaged code and transferring execution to the healthy copy.
- **Self-protection musings.** Dewdney ponders a hypothetical `PCT A` instruction that would protect an instruction from alteration until next executed, and frames the game as a demonstration of **evolutionary-like dynamics** (simple aggressors lose to smarter defenders, but all stay vulnerable to chance interactions).

## Entities mentioned
- [Core War](../entities/core-war.md) — the game introduced here.
- [A. K. Dewdney](../entities/ak-dewdney.md) — author; co-creator with **David Jones**.
- [Darwin (Bell Labs, 1961)](darwin-1961-bell-labs-game.md) — the direct ancestor; [McIlroy](../entities/doug-mcilroy.md) / [Vyssotsky](../entities/victor-vyssotsky.md) / [Morris](../entities/robert-morris.md).
- John von Neumann (self-replicating-machine theory, the conceptual backdrop); Shoch (Worm). *(No standalone pages.)*

## Concepts touched
- [Artificial life and the emergence of self-replication](../concepts/alife/artificial-life-and-self-replication.md) — Core War is the **programming-game** ancestor of the self-replicating-code thread; the Imp is a hand-written self-replicator.
- Self-replication, self-repair, von Neumann replicators, digital evolution (precursor to Tierra/Avida — not yet ingested).

## Open questions
- Core War warriors are **hand-written**, not evolved — the bridge to *evolved* self-replicators is **Tierra** (Tom Ray, 1991) and **Avida**, neither yet in the wiki. Natural next ingest to complete the lineage toward [Computational Life](computational-life-self-replicating-programs-paper.md).
- The 1984 column predates the standardized Redcode; later **ICWS '88 / '94** standards (see [pMARS](pmars-koth.md)) tightened the rules — the exact instruction set here is the original, not the modern one.
