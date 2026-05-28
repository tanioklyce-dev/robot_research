---
title: Metaworld
type: entity
subtype: benchmark
created: 2026-05-07
updated: 2026-05-28
sources: 3
tags: [metaworld, meta-rl, multi-task-rl, benchmark, mujoco, sawyer, stanford, berkeley]
---

**Metaworld** — "A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning." 50 simulated manipulation tasks on a single robot platform, designed to test **multi-task** and **meta-learning** generalization. Lead authors **Tianhe Yu, Deirdre Quillen, Sergey Levine, Chelsea Finn** at Stanford + UC Berkeley. arxiv 1910.10897 (2019), CoRL 2019. Code: https://github.com/rlworkgroup/metaworld. Project page: https://meta-world.github.io/.

## Composition
- **50 manipulation environments** spanning pick-and-place, push, drawer-open, peg-insert, hammer, button-press, etc.
- **Six evaluation modes**:
  - **ML1** — single task with variable goals (meta-learning within one task).
  - **MT1** — single task, no generalization testing.
  - **ML10** — 10 training tasks + 5 held-out test tasks (meta-RL).
  - **MT10** — 10 tasks, no generalization (multi-task RL).
  - **ML45** — 45 training + 5 held-out test (large-scale meta-RL).
  - **MT50** — all 50 environments (large-scale multi-task RL).
- **Robot platform** (per the original paper, not landing page): simulated **Sawyer** arm.
- **Physics engine** (per the original paper): [MuJoCo](mujoco.md).

## Why it matters in this wiki
Metaworld functions as a **lightweight, standardized manipulation testbed** that shows up across multiple paradigms:

- **[MuJoCo Playground](../sources/mujoco-playground-paper.md)** — DeepMind's MJX framework includes Metaworld envs as one of its eval suites.
- **[JEPA-WMs](../sources/jepa-wms-paper.md) (Terver et al., FAIR Dec 2025)** — uses **42 Metaworld tasks (100 episodes each)** as training/eval data alongside RoboCasa + Push-T + DROID + real Franka. This is the load-bearing JEPA-for-robotics use of Metaworld in the wiki.
- Earlier benchmark-zoo references in [LeWorldModel](../sources/leworldmodel-paper.md) and [DINO-WM](../sources/dino-wm-paper.md) for context.

## Position in the benchmark landscape
- **Lighter than [RoboCasa](robocasa.md) / [ManiSkill](maniskill.md)** — single Sawyer arm + simple kitchens/desks; no large-scene context.
- **Heavier than [PushT](pusht.md)** — 50 distinct manipulation tasks with proper rewards, vs. one 2D pushing test.
- **Meta-/multi-task framing is unusual** — Metaworld is one of the few benchmarks explicitly designed for *generalization across tasks*, not just policy quality on one task.

## Related
- [MuJoCo](mujoco.md) — physics backend.
- [MuJoCo Playground](mujoco-playground.md) — DeepMind framework that includes Metaworld envs.
- [JEPA-WMs](jepa-wms.md) — primary JEPA-line consumer.
- [RoboCasa](robocasa.md) — heavier-sim manipulation cousin.
- [PushT](pusht.md) — lightweight-sim cousin.

## Mentioned in
- [Metaworld Paper](../sources/metaworld-paper.md)
- [JEPA-WMs Paper](../sources/jepa-wms-paper.md)
- [MuJoCo Playground Paper](../sources/mujoco-playground-paper.md) (referenced as eval suite)
- [Farama Foundation Projects Page](../sources/farama-projects-page.md) (listed as deferred ingest)
- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — **natively integrated** as one of two simulation benchmarks (alongside [LIBERO](libero.md)). Used because of the shared-robot / shared-skill structure, useful for transfer evaluation.

## Open questions / TBD
- License of the Metaworld code/assets — not surfaced from project page.
- Real-robot correspondence — none claimed; Metaworld is sim-only.
- The [Metaworld Paper](../sources/metaworld-paper.md) (arxiv 1910.10897) is now filed (2026-05-16). The 10-task multi-task-RL failure is the load-bearing 2019 result; whether it's been overturned by post-VLA scaling is open.
