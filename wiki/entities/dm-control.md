---
title: DM Control Suite
type: entity
subtype: benchmark
created: 2026-05-08
updated: 2026-05-08
sources: 4
tags: [dm-control, deepmind, mujoco, rl-benchmark, locomotion, manipulation, biomechanics]
---

**DM Control Suite** ("DeepMind Control Suite") — Google DeepMind's open-source benchmark of **continuous-control RL tasks** on top of [MuJoCo](mujoco.md). The default RL bench for locomotion (`cheetah`, `walker`, `humanoid`, `quadruped`) and simple manipulation (`reacher`, `finger`, `manipulator`). Predates Gymnasium-Robotics by years; now lives alongside it in the broader RL-benchmark ecosystem.

## Position in this wiki
Reference appears across multiple ingested sources:
- **[stable-worldmodel](stable-worldmodel.md)** — exposes 12 DM Control envs in its env zoo (per the canonical README).
- **[DINO-WM](dino-wm.md)** — references **DM Control Reacher** as one of the eval envs.
- **[Farama Foundation Projects Page](../sources/farama-projects-page.md)** — DM Control is bridged into the Gymnasium ecosystem via Shimmy.
- **[flybody](flybody.md)** — uses `dm_control` as the env / control API for the *Drosophila* whole-body simulator ([flybody Paper](../sources/flybody-paper.md), [GitHub](../sources/flybody-github.md)).

## Why it matters
- **Standard locomotion bench.** When a paper says "we evaluate on cheetah," DM Control is implied.
- **Pre-Gymnasium-Robotics legacy substrate.** Bridges the OpenAI-Gym era to the modern Farama-curated ecosystem.
- **MuJoCo-coupled.** DM Control specifically uses MuJoCo (originally `mujoco-py`, now the maintained `dm_control` Python bindings) — meaning DM Control is a carrier for the MuJoCo-as-default-RL-physics pattern.

## Related
- [Google DeepMind](google-deepmind.md) — origin lab.
- [MuJoCo](mujoco.md) — physics backend.
- [MuJoCo Playground](mujoco-playground.md) — sibling DeepMind RL-benchmark project (newer, JAX-based).
- [Gymnasium-Robotics](gymnasium-robotics.md) — modern Farama-curated equivalent for robotics-specific tasks.
- [stable-worldmodel](stable-worldmodel.md) — exposes DM Control envs to the LeWM-line.

## Mentioned in
- [LeWorldModel — train and run howto](../syntheses/leworldmodel-howto.md) (referenced via stable-worldmodel env zoo)
- [DINO-WM Paper](../sources/dino-wm-paper.md) (DM Control Reacher as eval)
- [Farama Foundation Projects Page](../sources/farama-projects-page.md) (Shimmy bridge)
- [flybody Paper](../sources/flybody-paper.md) (`dm_control` env API for *Drosophila* sim)
- [flybody GitHub](../sources/flybody-github.md)

## Open questions / TBD
- DM Control paper / project page not yet ingested as a source.
- License terms — Apache 2.0 expected but not verified in this wiki.
