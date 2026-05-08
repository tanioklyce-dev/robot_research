---
title: DM Control Suite
type: entity
subtype: benchmark
created: 2026-05-08
updated: 2026-05-08
sources: 2
tags: [dm-control, deepmind, mujoco, rl-benchmark, locomotion, manipulation]
---

**DM Control Suite** ("DeepMind Control Suite") — Google DeepMind's open-source benchmark of **continuous-control RL tasks** on top of [[mujoco|MuJoCo]]. The default RL bench for locomotion (`cheetah`, `walker`, `humanoid`, `quadruped`) and simple manipulation (`reacher`, `finger`, `manipulator`). Predates Gymnasium-Robotics by years; now lives alongside it in the broader RL-benchmark ecosystem.

## Position in this wiki
Reference appears across multiple ingested sources:
- **[[stable-worldmodel|stable-worldmodel]]** — exposes 12 DM Control envs in its env zoo (per the canonical README).
- **[[dino-wm|DINO-WM]]** — references **DM Control Reacher** as one of the eval envs.
- **[[farama-projects-page|Farama Foundation Projects Page]]** — DM Control is bridged into the Gymnasium ecosystem via Shimmy.

## Why it matters
- **Standard locomotion bench.** When a paper says "we evaluate on cheetah," DM Control is implied.
- **Pre-Gymnasium-Robotics legacy substrate.** Bridges the OpenAI-Gym era to the modern Farama-curated ecosystem.
- **MuJoCo-coupled.** DM Control specifically uses MuJoCo (originally `mujoco-py`, now the maintained `dm_control` Python bindings) — meaning DM Control is a carrier for the MuJoCo-as-default-RL-physics pattern.

## Related
- [[google-deepmind|Google DeepMind]] — origin lab.
- [[mujoco|MuJoCo]] — physics backend.
- [[mujoco-playground|MuJoCo Playground]] — sibling DeepMind RL-benchmark project (newer, JAX-based).
- [[gymnasium-robotics|Gymnasium-Robotics]] — modern Farama-curated equivalent for robotics-specific tasks.
- [[stable-worldmodel|stable-worldmodel]] — exposes DM Control envs to the LeWM-line.

## Mentioned in
- [[leworldmodel-howto|LeWorldModel — train and run howto]] (referenced via stable-worldmodel env zoo)
- [[dino-wm-paper|DINO-WM Paper]] (DM Control Reacher as eval)
- [[farama-projects-page|Farama Foundation Projects Page]] (Shimmy bridge)

## Open questions / TBD
- DM Control paper / project page not yet ingested as a source.
- License terms — Apache 2.0 expected but not verified in this wiki.
