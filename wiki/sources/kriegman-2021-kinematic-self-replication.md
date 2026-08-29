---
title: "Kinematic self-replication in reconfigurable organisms (Kriegman et al. 2021)"
type: source
url: https://www.pnas.org/doi/10.1073/pnas.2112672118
local_path: raw/kriegman-et-al-2021-kinematic-self-replication-in-reconfigurable-organisms.pdf
sha256: f0dda5783023b197e34f57a0862653405afc35a649e3667f04f0cf59959527c6
author: Sam Kriegman, Douglas Blackiston, Michael Levin, Josh Bongard
affiliations: Tufts University (Allen Discovery Center); Wyss Institute, Harvard; University of Vermont (CS)
venue: PNAS 118(49):e2112672118
published: 2021-11-29
ingested: 2026-05-31
format: pdf
license: CC BY-NC-ND 4.0
tags: [artificial-life, alife, self-replication, kinematic-self-replication, xenobots, reconfigurable-organisms, evolutionary-computation, von-neumann, origins-of-life, emergence, morphogenesis]
---

## Summary

The **Xenobot self-replication paper**. The same team shows that swarms of *Xenopus*-cell "reconfigurable organisms" can **replicate *kinematically*** — not by growing and budding (as every known plant/animal does) but by **moving through their environment and pushing loose dissociated stem cells into piles** that mature into new motile organisms, which then do the same. This is a form of replication **previously unseen at the multicellular level** (it had only been known at the molecular/subcellular scale), and it **arises spontaneously over ~5 days without selection or genetic engineering**. An **evolutionary algorithm** then designs progenitor *shapes* (and terrains) that dramatically amplify how many replication rounds occur — the famous **C-shaped / "Pac-Man" semitorus** beats the natural spheroid.

## Key claims

- **Kinematic (motion-based) self-replication.** Wild-type spheroid organisms placed amid ~60,000 dissociated stem cells use their collective ciliary motion to **aggregate loose cells into piles**; piles ≥ ~50 cells adhere, compact, and over 5 d develop into ciliated, self-propelled **offspring** — which, given fresh feedstock, build the next generation. Progenitors (p) build offspring (o) which become progenitors.
- **Spontaneous, not evolved.** This behavior is "not only absent from the donating organism but from every other known plant or animal," and it **does not evolve in response to selection** — it arises from appropriate initial/environmental conditions. *(Distinct from the [Computational Life](computational-life-self-replicating-programs-paper.md) sense: there the soup is selection-free too, but here AI is used only to **amplify**, not to produce, the base behavior.)*
- **Control: no progenitors ⇒ no replication.** With only dissociated cells and no progenitor organisms, **no offspring self-assembled** at any tested density — confirming offspring are built by the kinematics of the parents, not mere fluid dynamics.
- **AI amplification via shape.** An evolutionary algorithm + physics sim searched progenitor body shapes to maximize **filial generations before halting**. Best discovered + manufacturable shape = an asymmetric **semitorus (C-shape)** with a "mouth" that captures/transports/aggregates cells. In vivo: semitoroids increased offspring diameter **+149%** and replication rounds **+250%** (spheroids ~1.2 rounds avg / max 2; semitoroids ~3 avg / max 4). 49 independent EA trials yielded 49 diverse high-performing shapes.
- **Terrain & clutter can also be optimized.** Evolving dish-floor walls increased replication rounds for wild-type spheroids; the EA could also confer replication ability in cluttered environments (elevating ventral surfaces above the clutter).
- **Exponential / superlinear utility.** Building on **von Neumann's** kinematic self-replicator theory: a self-replicator that does useful work *as a side effect* yields superlinear utility from a small seed investment. A simulation of **microcircuit assembly** (swarms randomly closing circuits between power supplies and light emitters while also building offspring, recursively bifurcated across dishes) shows utility growing **quadratically** vs. linearly for k non-replicative robots — eventually surpassing any fixed k.
- **No constructor/copier/controller/blueprint.** Unlike von Neumann's classical 4-part machine, these organisms have **no identifiable morphological or genetic structures** mapping to those roles, and no nervous system — making them a clue to how self-amplifying processes can emerge spontaneously in abiotic/cellular/biohybrid systems.
- **Origins-of-life relevance.** Connects to the **amyloid-world hypothesis** (self-assembling peptides forming variably-sized seeded "offspring") as a possible pre-RNA, kinematic-replication stage — though the authors stress Xenobots are *not* an origin-of-life model.

## Entities mentioned
- [Xenobots / reconfigurable organisms](../entities/xenobots.md) — the self-replicating artifact.
- [Sam Kriegman](../entities/sam-kriegman.md), Douglas Blackiston (co-first authors); [Michael Levin](../entities/michael-levin.md), [Josh Bongard](../entities/josh-bongard.md).
- **John von Neumann** — kinematic self-replicator theory invoked throughout. *(Not yet a page.)*

## Concepts touched
- [Artificial life and the emergence of self-replication](../concepts/alife/artificial-life-and-self-replication.md) — the biological-substrate counterpart to the wiki's code-substrate self-replication results.
- [Evolutionary computation](../concepts/alife/evolutionary-computation.md) — used here to amplify (not originate) self-replication.
- Kinematic self-replication, von Neumann replicators, exponential utility, origins of life.

## Open questions
- Replication **halts after ≤4 rounds** (offspring shrink each generation) — what conditions would sustain it indefinitely?
- The exponential-utility forecast is a **simulation**, not yet empirically tested for in-situ circuit assembly.
- How does "spontaneous, un-selected" kinematic replication here relate to the **selection-free emergence** in [Computational Life](computational-life-self-replicating-programs-paper.md)? Both reject designed fitness, but the mechanisms (cell mechanics vs. self-modifying code) differ — a cross-substrate comparison the wiki could synthesize.
