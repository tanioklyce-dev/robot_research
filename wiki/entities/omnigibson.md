---
title: OmniGibson
type: entity
subtype: simulator
created: 2026-07-04
updated: 2026-07-04
sources: 2
tags: [omnigibson, simulator, behavior-1k, omniverse, physx, isaac-sim, deformables, fluids, extended-states, stanford, igibson]
---

**OmniGibson** — Stanford Vision & Learning Lab's **physics + rendering simulator for embodied AI**, built on **NVIDIA Omniverse + PhysX 5**. The simulator underneath [BEHAVIOR-1K](behavior-benchmark.md), and the successor to **iGibson**. Its distinguishing capability is simulating what most robot-learning sims can't: **rigid + deformable bodies + fluids**, plus **continuous extended object states** (temperature, toggled, soaked, dirtiness, sliced) via a **Transition Machine** — the physics that "over half of BEHAVIOR-1K activities" require ([BEHAVIOR-1K paper](../sources/behavior-1k-paper.md)). Exposes an **OpenAI Gym interface** for RL.

## Capabilities
- **Omniverse + PhysX 5** substrate ([NVIDIA Isaac Sim](nvidia-isaac-sim.md) / [OpenUSD](openusd.md) stack); ray/path-traced photorealistic rendering.
- Rigid bodies, **deformables/cloth**, **fluids**; extended states (temperature/toggled/soaked/dirtiness/sliced) + Transition Machine (dough + oven → pie); thermal effects (fire/steam/smoke).
- **Highest visual realism** among embodied sims in the BEHAVIOR-1K user study: **3.20±1.23** vs Habitat 2.0 1.74, AI2-THOR 1.73, iGibson 2.0 1.69.
- **~60 fps** for a ~60-object house scene (trades speed for realism vs iGibson 2.0's ~100 fps — a scaling caveat for large RL runs).
- Mobile-manipulator robots with modular controllers; BDDL logical predicates as checking + sampling functions.
- **Requires [Isaac Sim](nvidia-isaac-sim.md) 4.1.0** (via the `isaacsim-for-omnigibson` pip package); OpenAI **Gym** interface; RTX GPU required. See the [codebase ingest](../sources/omnigibson-github.md) for install + the full spec.

## Supported robots (14)
From the [OmniGibson docs / codebase](../sources/omnigibson-github.md), four categories:
- **Mobile**: Turtlebot, Locobot, Husky, Freight (diff-drive + camera + LiDAR).
- **Manipulation**: [Franka](franka-panda.md) (7-DOF Research 3), VX300S ([ViperX 300](viperx-300.md), the ALOHA arm), A1 (+ Inspire hand), Franka Mounted (IK arm + gripper + wrist cam).
- **Mobile manipulation**: Fetch, [Tiago](tiago.md) (PAL bimanual holonomic), [Stretch](stretch.md) (Hello Robot), **[R1 / R1 Pro](galaxea-r1.md)** (Galaxea bimanual holonomic).
- **VR proxy**: BehaviorRobot (teleoperation).
Controllers: differential-drive / holonomic base, joint head, IK arms, grippers. Sensors: RGB/depth/segmentation, LiDAR, proprioception.

> [!note] R1/R1Pro = the Galaxea R1
> The wiki's BEHAVIOR ↔ GR00T ↔ Galaxea references resolve here: [GR00T N1.6](../sources/groot-n1_6.md)'s "simulated [Galaxea R1 Pro](galaxea-r1.md) on the BEHAVIOR suite" is the OmniGibson **R1Pro** robot running [BEHAVIOR-1K](behavior-benchmark.md) tasks.

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
- [OmniGibson GitHub (BIT-PIE fork) codebase](../sources/omnigibson-github.md) — the repo/docs ingest (Isaac Sim 4.1.0, 14 robots, install, Gym API).

## Open questions
- ~~Standalone repo/doc ingest~~ — filed 2026-07-04: [OmniGibson codebase](../sources/omnigibson-github.md) (Isaac Sim 4.1.0, 14-robot roster, install). Residual: exact **VRAM/RAM/disk** minimums (inherited from Isaac Sim 4.1.0) not restated in the README.
- What the **BIT-PIE fork** changes vs upstream StanfordVL (undocumented — README mirrors upstream).
- **iGibson** predecessor — not ingested; would anchor the Gibson → iGibson → OmniGibson lineage.
