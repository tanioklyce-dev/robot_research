---
title: Metaworld
type: entity
subtype: benchmark
created: 2026-05-07
updated: 2026-05-07
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
- **Physics engine** (per the original paper): [[mujoco|MuJoCo]].

## Why it matters in this wiki
Metaworld functions as a **lightweight, standardized manipulation testbed** that shows up across multiple paradigms:

- **[[mujoco-playground-paper|MuJoCo Playground]]** — DeepMind's MJX framework includes Metaworld envs as one of its eval suites.
- **[[jepa-wms-paper|JEPA-WMs]] (Terver et al., FAIR Dec 2025)** — uses **42 Metaworld tasks (100 episodes each)** as training/eval data alongside RoboCasa + Push-T + DROID + real Franka. This is the load-bearing JEPA-for-robotics use of Metaworld in the wiki.
- Earlier benchmark-zoo references in [[leworldmodel-paper|LeWorldModel]] and [[dino-wm-paper|DINO-WM]] for context.

## Position in the benchmark landscape
- **Lighter than [[robocasa|RoboCasa]] / [[maniskill|ManiSkill]]** — single Sawyer arm + simple kitchens/desks; no large-scene context.
- **Heavier than [[pusht|PushT]]** — 50 distinct manipulation tasks with proper rewards, vs. one 2D pushing test.
- **Meta-/multi-task framing is unusual** — Metaworld is one of the few benchmarks explicitly designed for *generalization across tasks*, not just policy quality on one task.

## Related
- [[mujoco|MuJoCo]] — physics backend.
- [[mujoco-playground|MuJoCo Playground]] — DeepMind framework that includes Metaworld envs.
- [[jepa-wms|JEPA-WMs]] — primary JEPA-line consumer.
- [[robocasa|RoboCasa]] — heavier-sim manipulation cousin.
- [[pusht|PushT]] — lightweight-sim cousin.

## Mentioned in
- [[jepa-wms-paper|JEPA-WMs Paper]]
- [[mujoco-playground-paper|MuJoCo Playground Paper]] (referenced as eval suite)
- [[farama-projects-page|Farama Foundation Projects Page]] (listed as deferred ingest)

## Open questions / TBD
- License of the Metaworld code/assets — not surfaced from project page.
- Real-robot correspondence — none claimed; Metaworld is sim-only.
- The Metaworld paper itself (arxiv 1910.10897) is not yet a source page; would let us cite design rationale (e.g. why 50 tasks, why Sawyer).
