---
title: Swarm intelligence
type: concept
created: 2026-05-31
updated: 2026-05-31
sources: 1
tags: [swarm-intelligence, swarm-robotics, swarm, uav, drone, emergence, flocking, boids, pso, aco, agentic-uavs, multi-agent, anti-drone]
---

**Swarm intelligence** is the study and engineering of **decentralized collectives whose useful global behavior emerges from many simple agents following local rules** — no central brain, no single point of failure. The biological archetypes are ant colonies, bee swarms, and bird flocks; the canonical computational archetype is [boids](../alife/flocking-and-boids.md). This page is the bridge between the wiki's **artificial-life / emergence** branch (where the idea originates) and its **aerial-robotics** branch ([agentic UAVs](agentic-uavs.md), where it is now being engineered at scale).

## From flocking to swarms

[**Boids**](../alife/flocking-and-boids.md) showed that three local steering rules (separation / alignment / cohesion) produce realistic collective motion with no leader. Swarm intelligence generalizes that insight into **decentralized control + decentralized optimization**: the same "complex global order from simple local interaction" thesis that anchors [artificial life and emergence](../alife/artificial-life-and-self-replication.md). The foundational text is **Bonabeau, Dorigo & Theraulaz, *Swarm Intelligence: From Natural to Artificial Systems* (1999)** ([Raj & Kos 2026](../../sources/raj-kos-drone-swarm-review-2026.md)).

> [!note] "Swarm" vs. "flood"
> [Raj & Kos (2026)](../../sources/raj-kos-drone-swarm-review-2026.md): "A multitude of uncoordinated unoccupied systems does not constitute a 'swarm'; it represents a flood." A swarm's members *synchronize and adjust* into a unified, emergent entity — coordination, not just quantity, is the defining property.

## Command-and-control taxonomy

Engineered swarms span a centralization spectrum ([Raj & Kos 2026](../../sources/raj-kos-drone-swarm-review-2026.md)):

| Model | Coordination mechanism |
|---|---|
| **Coordination by consensus** | Members agree via voting / auction (e.g. CBAA) |
| **Centralized control** | One controller assigns each member's task |
| **Emergent coordination** | Arises from local interaction — the [boids](../alife/flocking-and-boids.md) regime, "as in animal swarms" |
| **Hierarchical control** | Squad-agents under superior controllers |

Tradeoff: decentralized swarms find good solutions but converge slowly (ant-colony-like); centralized/hierarchical are faster but bandwidth-hungry. Under poor comms, swarms fall back on consensus voting or **stigmergy** (indirect coordination by modifying the shared environment).

## Swarm-intelligence optimization (metaheuristics)

A distinct lineage uses swarm metaphors as **optimizers** rather than controllers — population-based search where simple agents + local update rules find good solutions. Surveyed in [Raj & Kos (2026)](../../sources/raj-kos-drone-swarm-review-2026.md) for UAV path planning and 6G/IoT problems:
- **Particle Swarm Optimization (PSO)**, **Ant Colony Optimization (ACO)**, **Artificial Bee Colony (ABC)**, plus Cuckoo Search, Grey Wolf, Elephant Herd, Salp Swarm, Monarch Butterfly, Fruit Fly.

## Aerial swarms (the current engineering frontier)

UAV swarms are where swarm intelligence is being industrialized — see [agentic UAVs](agentic-uavs.md) for the per-vehicle autonomy stack. Notable results from [Raj & Kos (2026)](../../sources/raj-kos-drone-swarm-review-2026.md):
- **Scalable guidance:** an MDPI-style Markov interacting-pattern controller steers **1000 drones at 99.95% accuracy with only 5% informed agents** (validated on Crazyflie micro-quadrotors) — a direct demonstration that sparse leadership suffices for emergent coordination.
- **Learned prediction:** graph/sequence DL (DynGN, EvolveGCN+DMPC, graph-attention transformers, LSTM) for trajectory/intention prediction.
- **LLM interfaces:** **LEVIOSA** (language→multi-UAV 3D trajectories) and **SwarmGPT** (music→drone-light-show choreography with a safety filter).
- **Counter-swarm (anti-drone):** auction-based target allocation, offense-defense decision-making (ODCDM/CBAA), evolutionary air-defense placement, "loyal wingman" human-AI teaming. As offensive swarms mature, **defense against them becomes a co-equal research problem** — with explicit dual-use / lethal-autonomous-weapons concerns.

## Related concepts
- [Flocking and boids](../alife/flocking-and-boids.md) — the canonical computational archetype; emergent-coordination regime.
- [Artificial life and the emergence of self-replication](../alife/artificial-life-and-self-replication.md) — the broader "order from local interaction" branch.
- [Agentic UAVs](agentic-uavs.md) — the per-vehicle autonomy substrate that aerial swarms are built on.
- [LLM-agent architecture](../agents/llm-agent-architecture.md) — multi-agent coordination as the collective analog of single-agent loops.

## Mentioned in
- [Recent Developments and Applications of Drone Swarm (Raj & Kos, 2026)](../../sources/raj-kos-drone-swarm-review-2026.md)
