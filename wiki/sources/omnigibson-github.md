---
title: OmniGibson (GitHub — BIT-PIE fork of StanfordVL) codebase
type: source
url: https://github.com/BIT-PIE/OmniGibson
upstream: https://github.com/StanfordVL/OmniGibson (within StanfordVL/BEHAVIOR-1K)
docs: https://behavior.stanford.edu/omnigibson/
author: Stanford Vision & Learning Lab (upstream); BIT-PIE (fork)
published: 2024-10 (fork v1.1.0); upstream ongoing
ingested: 2026-07-04
format: github-repo + docs
license: MIT
tags: [omnigibson, simulator, isaac-sim, omniverse, behavior-1k, gym, robots, deformables, fluids, stanford]
---

## Summary

Dedicated codebase ingest of **[OmniGibson](../entities/omnigibson.md)** — Stanford's Omniverse-based embodied-AI simulator (the engine behind [BEHAVIOR-1K](../entities/behavior-benchmark.md)). Fetched via the user's **[`BIT-PIE/OmniGibson`](https://github.com/BIT-PIE/OmniGibson)** fork (MIT, **v1.1.0 / Oct 2024**, Python 96.8%, OpenAI Gym interface) — a thin fork of `StanfordVL/BEHAVIOR-1K` with no documented distinctive changes; the substantive detail is upstream (docs at behavior.stanford.edu/omnigibson). This page pins the practical specifics the entity was missing: **Isaac Sim dependency, the supported-robot roster, controllers/sensors, and install.**

## Key facts

### Runtime dependency
- **Requires [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md) 4.1.0** installed locally — the currently supported version. OmniGibson ships as a pip/GitHub package; the **`isaacsim-for-omnigibson`** pip package auto-downloads the required Isaac Sim components from NVIDIA's PyPI. Docker install also available. (An RTX GPU is required, inherited from the Isaac Sim / Omniverse RTX-renderer requirement.)
- **OpenAI Gym interface** for RL; YAML-config environments; the [BEHAVIOR-1K](../entities/behavior-benchmark.md) task suite ships as **1,004 pre-sampled tasks across all 50 scenes** (v1.0.0).

### Supported robots (14, four categories)
- **Mobile** (differential-drive base + camera + LiDAR): **Turtlebot** (Kobuki base), **Locobot**, **Husky** (Clearpath, 4-wheel), **Freight** (the base under Fetch).
- **Manipulation** (IK arm + gripper + wrist cam): **[Franka](../entities/franka-panda.md)** (7-DOF Research 3), **VX300S** ([ViperX 300](../entities/viperx-300.md) 6-DOF, Trossen — the ALOHA arm), **A1** (6-DOF + Inspire dexterous hand), **Franka Mounted** (on a cart).
- **Mobile manipulation**: **Fetch** (2-wheel base, trunk, 2-DOF head, 7-DOF arm, gripper; head+wrist cam + LiDAR), **[Tiago](../entities/tiago.md)** (PAL bimanual, holonomic base, dual arms/grippers, dual wrist cams + dual LiDAR), **[Stretch](../entities/stretch.md)** (Hello Robot, 5-DOF arm), **[R1](../entities/galaxea-r1.md)** (Galaxea bimanual, 3-DOF holonomic base, dual 6-DOF arms), **[R1 Pro](../entities/galaxea-r1.md)** (holonomic base + 4-DOF torso + dual 7-DOF arms).
- **Anthropomorphic/VR**: **BehaviorRobot** (hand-designed VR-teleoperation proxy).
- **Controllers**: differential-drive / **holonomic** base, joint head, **inverse-kinematics (IK)** arms, grippers (per-robot modular controller stacks). **Sensors**: RGB / depth / segmentation cameras (head + wrist), LiDAR, proprioception.

### Loop-closing detail
**R1 / R1 Pro in OmniGibson *are* the [Galaxea R1](../entities/galaxea-r1.md).** GR00T N1.6's "simulated Galaxea R1 Pro on the BEHAVIOR suite" ([GR00T N1.6](groot-n1_6.md)) is literally the OmniGibson **R1Pro** robot running BEHAVIOR-1K tasks — the wiki's BEHAVIOR ↔ GR00T ↔ Galaxea references all resolve to this one simulator + robot.

## Entities mentioned
- [OmniGibson](../entities/omnigibson.md) — the simulator (deepened by this page). [BEHAVIOR-1K](../entities/behavior-benchmark.md) — the task suite it ships.
- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md) 4.1.0 — required substrate.
- Robots: [Franka](../entities/franka-panda.md), [ViperX 300](../entities/viperx-300.md) (VX300S), [Tiago](../entities/tiago.md), [Stretch](../entities/stretch.md), [Galaxea R1](../entities/galaxea-r1.md) (R1/R1Pro). Turtlebot ([TurtleBot](../entities/turtlebot.md) family), Husky, Locobot, Freight, A1 — not separately tracked.

## Concepts touched
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — OmniGibson is the environment behind the [12.4% BEHAVIOR-1K](../entities/behavior-benchmark.md) gap number.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — a *physics* sim (deformables/fluids/extended-states), the contrast class to learned/generative-video sims.

## Open questions
- **Fork specifics**: what (if anything) `BIT-PIE/OmniGibson` changes vs upstream is undocumented in the repo — the README mirrors StanfordVL.
- **Exact VRAM/RAM/disk minimums**: inherited from Isaac Sim 4.1.0's requirements; not restated in the OmniGibson README (Isaac Sim typically wants an RTX GPU with ≥8 GB VRAM, but confirm against the Isaac Sim 4.1.0 requirements page).
- **iGibson predecessor** — the Gibson → iGibson → OmniGibson lineage still un-ingested.
