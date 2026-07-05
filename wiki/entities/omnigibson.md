---
title: OmniGibson
type: entity
subtype: simulator
created: 2026-07-04
updated: 2026-07-04
sources: 1
tags: [omnigibson, simulator, behavior-1k, omniverse, physx, isaac-sim, deformables, fluids, extended-states, stanford, igibson]
---

**OmniGibson** — Stanford Vision & Learning Lab's **physics + rendering simulator for embodied AI**, built on **NVIDIA Omniverse + PhysX 5**. The simulator underneath [BEHAVIOR-1K](behavior-benchmark.md), and the successor to **iGibson**. Its distinguishing capability is simulating what most robot-learning sims can't: **rigid + deformable bodies + fluids**, plus **continuous extended object states** (temperature, toggled, soaked, dirtiness, sliced) via a **Transition Machine** — the physics that "over half of BEHAVIOR-1K activities" require ([BEHAVIOR-1K paper](../sources/behavior-1k-paper.md)). Exposes an **OpenAI Gym interface** for RL.

## Capabilities
- **Omniverse + PhysX 5** substrate ([NVIDIA Isaac Sim](nvidia-isaac-sim.md) / [OpenUSD](openusd.md) stack); ray/path-traced photorealistic rendering.
- Rigid bodies, **deformables/cloth**, **fluids**; extended states (temperature/toggled/soaked/dirtiness/sliced) + Transition Machine (dough + oven → pie); thermal effects (fire/steam/smoke).
- **Highest visual realism** among embodied sims in the BEHAVIOR-1K user study: **3.20±1.23** vs Habitat 2.0 1.74, AI2-THOR 1.73, iGibson 2.0 1.69.
- **~60 fps** for a ~60-object house scene (trades speed for realism vs iGibson 2.0's ~100 fps — a scaling caveat for large RL runs).
- Mobile-manipulator robots with modular controllers; BDDL logical predicates as checking + sampling functions.

## Why it matters in this wiki
- **The physics engine behind the wiki's hardest benchmark.** Whenever [BEHAVIOR-1K](behavior-benchmark.md) or the [12.4% sim-to-real number](../concepts/learning/sim-to-real-transfer.md) is cited, OmniGibson is the environment.
- **The fluid/deformable/extended-state frontier.** It's the reference for what *learned* [world-model simulators](../concepts/world-models/world-model-simulators.md) still can't do — cooking, soaking, slicing, pouring — a useful contrast to the generative-video sim line ([Cosmos](nvidia-cosmos.md), [Genie Envisioner](genie-envisioner.md)).
- Part of the Omniverse-based robotics-sim cluster alongside [Isaac Sim](nvidia-isaac-sim.md) / [Isaac Lab](nvidia-isaac-lab.md) / [RoboCasa](robocasa.md), all sharing the PhysX/USD substrate.

## Code
- **Upstream**: `StanfordVL/OmniGibson` (now within the `StanfordVL/BEHAVIOR-1K` monorepo, ~1.5k★).
- **Fork tracked here**: [`BIT-PIE/OmniGibson`](https://github.com/BIT-PIE/OmniGibson) — MIT; **v1.1.0 (Oct 2024)**; OpenAI Gym interface; Docker install; ships 1,004 pre-sampled tasks + all 50 scenes. A thin fork of the StanfordVL platform (no distinctive documented changes vs upstream).

## Related
- [BEHAVIOR-1K](behavior-benchmark.md) — the benchmark it simulates.
- [NVIDIA Isaac Sim](nvidia-isaac-sim.md) / [OpenUSD](openusd.md) — the Omniverse/PhysX/USD substrate.
- [RoboCasa](robocasa.md), [Habitat](habitat.md) — peer household/embodied sims (RoboCasa also Omniverse-adjacent; Habitat is the Meta counterpart).
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — OmniGibson is the environment where the hard gap is measured.

## Mentioned in
- [BEHAVIOR-1K Paper](../sources/behavior-1k-paper.md) — introduces + describes OmniGibson.

## Open questions
- **No standalone OmniGibson paper ingested** — it's described in the BEHAVIOR-1K paper; a dedicated OmniGibson doc/repo ingest would pin the exact Isaac Sim version, VRAM/RTX requirements, and the full supported-robot list (Fetch/Franka/Tiago/Turtlebot/R1…).
- What the **BIT-PIE fork** changes vs upstream (undocumented in the repo excerpt).
- **iGibson** predecessor — not ingested; would anchor the Gibson → iGibson → OmniGibson lineage.
