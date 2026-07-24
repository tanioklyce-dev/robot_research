---
title: Evolutionary computation
type: concept
created: 2026-05-31
updated: 2026-05-31
sources: 3
tags: [evolutionary-computation, evolutionary-algorithms, genetic-algorithms, artificial-life, optimization, morphology, co-design, soft-robotics]
---

**Evolutionary computation (EC)** is a family of population-based, derivative-free optimization methods inspired by biological evolution: maintain a **population** of candidate solutions, **evaluate** each against an objective, **select** the better ones, and produce the next generation by **random mutation / recombination**. Repeat. Unlike gradient-based learning, EC needs no differentiable objective and explores a *diversity* of solutions.

## Why it shows up in this wiki
EC is the design engine behind the [Xenobots](../../entities/xenobots.md) work:
- **It co-designs body *and* behavior.** [Kriegman et al. 2020](../../sources/kriegman-2020-reconfigurable-organisms.md) note that EC is used *instead of* learning methods precisely because it can evolve a machine's **physical structure** alongside its controller — you can't backprop through "what shape should this organism be." Designs are scored in a soft-body physics sim, and **diversity is valuable** because some designs are more physically buildable than others.
- **It optimizes for emergent, hard-to-specify outcomes.** [Kriegman et al. 2021](../../sources/kriegman-2021-kinematic-self-replication.md) evolve progenitor *shape* (and terrain) to **amplify kinematic self-replication** — discovering the C-shaped semitorus that triples replication rounds — even though the replication behavior itself is emergent and un-selected.

## How it differs from the wiki's other optimizers
- vs. **gradient learning** (SGD/Adam, the substrate of [neural nets](../../syntheses/curriculum/curriculum-01-neural-networks.md), BC, VLAs): EC is gradient-free and population-based; it can optimize **non-differentiable, discrete, or structural** design spaces (morphology), at the cost of sample efficiency.
- vs. **reinforcement learning**: both maximize a reward/fitness without labeled targets, but RL learns a *policy's parameters* by exploiting the temporal/credit structure of an MDP, while EC treats the whole solution as a black box and relies on selection over a population. (See [RL vocabulary](../../syntheses/curriculum/curriculum-08-rl-vocabulary.md).)

## Related concepts
- [Artificial life and the emergence of self-replication](artificial-life-and-self-replication.md) — EC is one of the classic ALife tools; "evolutionary computation | artificial life" are the literal keywords of the [2020 paper](../../sources/kriegman-2020-reconfigurable-organisms.md).
- [Flocking and boids](flocking-and-boids.md) — sibling emergence model (hand-designed local rules rather than evolved).

## Current state
In this wiki EC appears specifically as a **morphology/structure co-design** tool for embodied + biohybrid systems (Bongard-lineage evolutionary robotics), distinct from the dominant gradient-learning robot-policy methods. Broader EC (NEAT, CMA-ES, quality-diversity, open-ended evolution) is **not yet covered** — natural neighbors as this branch grows.

## Mentioned in
- [Kriegman et al. 2020 — A scalable pipeline for designing reconfigurable organisms](../../sources/kriegman-2020-reconfigurable-organisms.md)
- [Kriegman et al. 2021 — Kinematic self-replication in reconfigurable organisms](../../sources/kriegman-2021-kinematic-self-replication.md)
