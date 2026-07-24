---
title: Flocking and boids
type: concept
created: 2026-05-31
updated: 2026-05-31
sources: 6
tags: [artificial-life, alife, emergence, flocking, boids, swarm-intelligence, swarm-robotics, ant-colony-optimization, agent-based-model, edge-of-chaos, behavioral-animation, particle-system, actor-model]
---

**Boids** is Craig Reynolds' agent-based model of coordinated animal motion (bird flocks, fish schools), first published at **SIGGRAPH '87** ([Reynolds 1987](../../sources/reynolds-flocks-herds-schools-1987.md); model dated 1986). It is the canonical demonstration that **realistic, complex group motion emerges from each individual following a few simple local rules** — with no leader, no global plan, and no central choreography. "boids" = **bird-oid objects**; each is a generalization of a **particle system** (an oriented sub-object) implemented as an **actor** ([Reynolds 1987](../../sources/reynolds-flocks-herds-schools-1987.md)). It sits in the wiki's [ALife / emergence branch](artificial-life-and-self-replication.md) as the "continuous steering" sibling of the "self-modifying code" emergence shown in [Computational Life](../../sources/computational-life-self-replicating-programs-paper.md).

## The three rules

Each boid is an autonomous agent with **position, velocity, and orientation**, steering each step by three behaviors computed only over *local* flockmates (neighbors within a distance/view-angle). The popular names come from Reynolds' later [web page](../../sources/reynolds-boids-page.md); the original 1987 paper named them differently and — crucially — ordered them by **strict precedence** ([Reynolds 1987](../../sources/reynolds-flocks-herds-schools-1987.md)):

| Popular name (web/later) | Original 1987 name | What it does |
|---|---|---|
| **Separation** | **Collision Avoidance** (highest precedence) | steer to avoid crowding local flockmates (static, position-based) |
| **Alignment** | **Velocity Matching** | match heading + speed of local flockmates (dynamic; predictive collision avoidance) |
| **Cohesion** | **Flock Centering** (lowest precedence) | steer toward the centroid of local flockmates |

> [!note] Priority, not equal averaging
> The three-co-equal-rules framing is a simplification. The 1987 paper uses **prioritized acceleration allocation**: requests are summed in priority order until a per-boid max-acceleration budget is spent, and lower-priority urges (flock centering) are dropped in emergencies. Naive weighted averaging fails — opposing avoidance vectors cancel (crash), and "fly north" + "fly east" wrongly averages to "fly northeast" ([Reynolds 1987](../../sources/reynolds-flocks-herds-schools-1987.md)).

**Localized perception is essential** — the paper's key finding: flocking *depends on* a limited, local view. A global **central-force model fails** (the whole scattered flock collapses to one point and cannot bifurcate around obstacles). Neighbor influence falls off as **inverse-square distance** (a linear "spring-like" law gave an unrealistically bouncy flock). Common extensions: **obstacle avoidance** (force-field vs. the preferred vision-like *steer-to-avoid*) and a scriptable **migratory urge** (global goal point) for directing the flock ([Reynolds 1987](../../sources/reynolds-flocks-herds-schools-1987.md), [Stanford SoCo](../../sources/stanford-soco-boids.md)).

## Emergence and dynamics

Boids is a textbook case of **emergence: complex global behavior arising from the interaction of simple local rules** ([Reynolds page](../../sources/reynolds-boids-page.md)). Motion is **predictable short-term but unpredictable over the moderate term** — Reynolds characterizes flocks as "poised at the **edge of chaos**," citing Chris Langton. This is the same "structure without a designer" theme as the broader [ALife self-replication](artificial-life-and-self-replication.md) work — there from random self-modifying code, here from continuous local steering.

## Computational cost

Naively **O(n²)** — every boid queries every other for neighbors — but **spatial data structures** (grids/bins, k-d trees) bring it to nearly **O(n)**, enabling real-time large flocks ([Reynolds page](../../sources/reynolds-boids-page.md)). Reynolds argues real animals run a near **constant-time** algorithm (aware only of self + 2–3 nearest neighbors + "the rest"), which is why natural flocks show no upper size bound ([Reynolds 1987](../../sources/reynolds-flocks-herds-schools-1987.md)). For scale: his 1987 Lisp-Machine implementation ran 80 boids at ~95 s/frame.

## Key references
- [Reynolds 1987 — "Flocks, Herds, and Schools: A Distributed Behavioral Model" (SIGGRAPH '87)](../../sources/reynolds-flocks-herds-schools-1987.md) — **the seminal primary source**; original rule names, priority arbitration, localized perception, geometric flight.
- [Boids (Craig Reynolds) — red3d.com](../../sources/reynolds-boids-page.md) — Reynolds' own later overview page (separation/alignment/cohesion framing, history, applications).
- [Boids — Stanford SoCo (Wong, 2008)](../../sources/stanford-soco-boids.md) — secondary write-up; supplies the swarm-intelligence framing.

## Applications
- **Computer animation / VFX** — *Stanley and Stella* (1987); ***Batman Returns*** (1992, first feature film) used modified boids for bats and penguins; standard in films and games for crowds/flocks since ([Reynolds page](../../sources/reynolds-boids-page.md)).
- **Swarm intelligence & robotics** — boids is a foundational instance of decentralized, local-rule control; the [Stanford source](../../sources/stanford-soco-boids.md) links it to **ant colony optimization** and **swarm robotics** (mapping, foraging). This generalizes into the [swarm intelligence](../robotics/swarm-intelligence.md) concept, whose current engineering frontier is aerial swarms — see [agentic UAVs](../robotics/agentic-uavs.md), where 1000-drone coordination from 5% informed agents echoes the same local-rule logic ([Raj & Kos 2026](../../sources/raj-kos-drone-swarm-review-2026.md)).

## Related concepts
- [Artificial life and the emergence of self-replication](artificial-life-and-self-replication.md) — parent branch; boids = emergence in continuous steering, Computational Life = emergence in self-modifying code.
- [Swarm intelligence](../robotics/swarm-intelligence.md) — the generalization of boids into decentralized control + optimization.
- [Agentic UAVs](../robotics/agentic-uavs.md) — swarm/multi-agent robotics as the engineering descendant.
- Cellular automata, open-endedness, self-organization — adjacent ALife topics flagged but **not yet covered**.

## Mentioned in
- [Reynolds 1987 — Flocks, Herds, and Schools (SIGGRAPH '87)](../../sources/reynolds-flocks-herds-schools-1987.md)
- [Boids (Craig Reynolds) — red3d.com](../../sources/reynolds-boids-page.md)
- [Boids — Stanford SoCo (Wong, 2008)](../../sources/stanford-soco-boids.md)
