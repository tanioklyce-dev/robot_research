---
title: Flocking and boids
type: concept
created: 2026-05-31
updated: 2026-05-31
sources: 2
tags: [artificial-life, alife, emergence, flocking, boids, swarm-intelligence, swarm-robotics, ant-colony-optimization, agent-based-model, edge-of-chaos]
---

**Boids** is Craig Reynolds' 1986 agent-based model of coordinated animal motion (bird flocks, fish schools). It is the canonical demonstration that **realistic, complex group motion emerges from each individual following a few simple local rules** — with no leader, no global plan, and no central choreography. It sits in the wiki's [ALife / emergence branch](artificial-life-and-self-replication.md) as the "continuous steering" sibling of the "self-modifying code" emergence shown in [Computational Life](../../sources/computational-life-self-replicating-programs-paper.md).

## The three rules

Each boid is an autonomous agent with **position, velocity, and orientation**, and steers each step by combining three behaviors computed only over *local* flockmates (neighbors within a distance and view-angle) ([Reynolds page](../../sources/reynolds-boids-page.md), [Stanford SoCo](../../sources/stanford-soco-boids.md)):

1. **Separation** — steer to avoid crowding local flockmates (short-range repulsion).
2. **Alignment** — steer toward the average *heading* of local flockmates.
3. **Cohesion** — steer toward the average *position* of local flockmates.

Common extensions: **obstacle avoidance** and goal-seeking, which let boids navigate environments while staying flocked ([Stanford SoCo](../../sources/stanford-soco-boids.md)).

## Emergence and dynamics

Boids is a textbook case of **emergence: complex global behavior arising from the interaction of simple local rules** ([Reynolds page](../../sources/reynolds-boids-page.md)). Motion is **predictable short-term but unpredictable over the moderate term** — Reynolds characterizes flocks as "poised at the **edge of chaos**," citing Chris Langton. This is the same "structure without a designer" theme as the broader [ALife self-replication](artificial-life-and-self-replication.md) work — there from random self-modifying code, here from continuous local steering.

## Computational cost

Naively **O(n²)** — every boid queries every other for neighbors — but **spatial data structures** (grids, k-d trees) bring it to nearly **O(n)**, enabling real-time large flocks ([Reynolds page](../../sources/reynolds-boids-page.md)).

## Key references
- [Boids (Craig Reynolds) — red3d.com](../../sources/reynolds-boids-page.md) — primary source; the model, the three rules, history, complexity.
- Reynolds, "Flocks, Herds, and Schools: a Distributed Behavioral Model," **SIGGRAPH '87** — the seminal paper (not yet ingested in full).
- [Boids — Stanford SoCo (Wong, 2008)](../../sources/stanford-soco-boids.md) — secondary write-up; supplies the swarm-intelligence framing.

## Applications
- **Computer animation / VFX** — *Stanley and Stella* (1987); ***Batman Returns*** (1992, first feature film) used modified boids for bats and penguins; standard in films and games for crowds/flocks since ([Reynolds page](../../sources/reynolds-boids-page.md)).
- **Swarm intelligence & robotics** — boids is a foundational instance of decentralized, local-rule control; the [Stanford source](../../sources/stanford-soco-boids.md) links it to **ant colony optimization** and **swarm robotics** (mapping, foraging). The applied-robotics neighbor in this wiki is [agentic UAVs](../robotics/agentic-uavs.md), where multi-drone coordination echoes the same local-rule logic.

## Related concepts
- [Artificial life and the emergence of self-replication](artificial-life-and-self-replication.md) — parent branch; boids = emergence in continuous steering, Computational Life = emergence in self-modifying code.
- [Agentic UAVs](../robotics/agentic-uavs.md) — swarm/multi-agent robotics as the engineering descendant.
- Cellular automata, open-endedness, self-organization — adjacent ALife topics flagged but **not yet covered**.

## Mentioned in
- [Boids (Craig Reynolds) — red3d.com](../../sources/reynolds-boids-page.md)
- [Boids — Stanford SoCo (Wong, 2008)](../../sources/stanford-soco-boids.md)
