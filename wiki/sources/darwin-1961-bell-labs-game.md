---
title: "Darwin, a Game of Survival of the Fittest among Programs (Bell Labs, 1961; McIlroy transcript)"
type: source
local_path: raw/darwin.pdf
author: M. D. McIlroy, R. Morris, V. A. Vyssotsky (1971 letter); flyer by V. A. Vyssotsky et al. (1961)
affiliations: Bell Telephone Laboratories, Murray Hill, NJ
published: 1961-08
ingested: 2026-05-31
format: pdf
tags: [darwin, core-war, self-replication, artificial-life, alife, bell-labs, ibm-7090, mcilroy, morris, vyssotsky, programming-game, digital-evolution, history]
---

## Summary

The **primary-source origin of the self-reproducing-program game** — and the direct ancestor of [Core War](../entities/core-war.md). **Darwin** was invented at **Bell Labs in August 1961** by **Victor Vyssotsky**, with **Doug McIlroy** coding the "umpire" overnight and **Robert Morris** soon writing the "ultimately lethal" competitor that ended the game. Programs ("organisms" of a "species") live in a shared **arena** in core memory, where the one in control tries to **replicate itself** into free space and **kill** members of other species. This PDF is **McIlroy's transcript of a 1971 letter** (the basis for the first public description, by "Aleph-Null," in *Software—Practice & Experience* Vol. 2, 1972, pp. 91–96), bundled with the **original 1961 rules flyer**. Dewdney's 1984 *Scientific American* column later rechristened the updated game as [Core War](dewdney-1984-core-war-scientific-american.md).

## Key claims / content

- **Provenance.** Conceived by **Vyssotsky** (Aug 1961); **McIlroy** coded the umpire that night; **Morris** invented the lethal competitor ~2 weeks later. First public description by "Aleph-Null" in *SP&E* 1972 (the document notes **Aleph-Null ≠ C. A. Lang**, the journal editor the letter was addressed to). Played on the **IBM 7090**.
- **Umpire-mediated, not self-modifying-by-default.** Unlike Core War's shared-tape free-for-all, Darwin runs through an **umpire** with three calls: `probe(loc, myno)` (must precede the others), `kill(loc, myno)` (kills any individual regardless of species), `claim(loc, myno)` (specifies the origin of a newly reproduced individual). **Probing a *protected* cell silently transfers control** to the probed program; any unreasonable umpire request **exterminates the offending species**.
- **Reproduction required relocation, not just copying.** "The code of an individual could not simply be copied but had to be **correctly relocated**." Vyssotsky's **5-instruction move-and-relocate loop** became the standard idiom. The smallest creature doing probe+kill+reproduce was ~**30 IBM-7090 instructions**.
- **McIlroy's "hard-shelled virus."** A **15-cell** creature that could only probe and kill won a few early rounds — so dominant they had to cut the protected-cell limit (from 20) "lest it be immortal."
- **Morris's adaptive killer (44 cells)** ended the game: on finding the boundary of an unknown opponent it would **poke a small integer** into it; on success it reused the increment on the next individual; on losing control it **changed its poking increment**; offspring inherited successful increments. An **adaptive search** that tuned itself to each opponent's protection pattern — "the more thickly memory was inhabited by the enemy, the more virulent the attack."
- **Emergent ecology.** Observed **population oscillation / rock-paper-scissors dynamics**: species A swelling at B's expense becomes vulnerable to C, in rotation. A failed **"bisexualism" experiment** (separate search-and-destroy vs. reproducer individuals) — the division of labor gained no viability and added a fatal weakness.
- **Implementation lore.** Arena usually **10,000 locations**; rounds ran in **under a minute** because organisms were **executed, not interpreted** (an "honesty rule" — all programs circulated to all players after each round — replaced interpretive enforcement and ran 20–30× faster). Getting many copies loaded at random origins abused the "scatter loader."
- **1961 rules flyer ("Darwin: A Game of Survival and (Hopefully) Evolution," Vyssotsky et al.):** a species = number N, size S(N) < 2000, origin O(N), and **20 protected locations**; organisms occupy S(N) contiguous cells with a single entry point, may not inspect the umpire or anything outside the arena, must notify the umpire before writing outside their own block, no I/O; the umpire scatters organisms at pseudo-random origins; **win by destroying all other species** (or surviving when time runs out). A wild transfer, infinite loop, or illegal write loses the game.

## Entities mentioned
- [Core War](../entities/core-war.md) — the 1984 descendant ([Dewdney column](dewdney-1984-core-war-scientific-american.md)).
- [Doug McIlroy](../entities/doug-mcilroy.md) — coded the umpire; transcriber of this document (later of Unix-pipes / `diff` fame).
- [Victor Vyssotsky](../entities/victor-vyssotsky.md) — inventor of Darwin (later Multics, Bell Labs/DEC).
- [Robert Morris](../entities/robert-morris.md) — author of the winning adaptive species (later NSA chief scientist; father of Morris-worm author R. T. Morris).

## Concepts touched
- [Artificial life and the emergence of self-replication](../concepts/alife/artificial-life-and-self-replication.md) — Darwin is the **earliest** entry in the wiki's digital-replicator lineage (1961), predating Core War (1984).
- Self-replication, code relocation, adaptive search, emergent ecological dynamics (precursor framing to digital evolution / Tierra / Avida — not yet ingested).

## Open questions
- **Umpire-mediated (Darwin) vs. shared-tape (Core War / [Computational Life](computational-life-self-replicating-programs-paper.md)) substrates** differ in *how* one program can affect another — a clean axis for a future cross-substrate synthesis of the self-replication branch.
- Darwin had **adaptation within a round** (Morris's self-tuning increment) but no across-generation *evolution* of code — the flyer's "(Hopefully) Evolution" went largely unrealized; the evolved-replicator step is **Tierra/Avida** (still un-ingested).
- Exact canonical URL of this McIlroy transcript not captured (local PDF; widely mirrored from McIlroy's pages).
