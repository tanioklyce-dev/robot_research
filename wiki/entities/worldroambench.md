---
title: WorldRoamBench
type: entity
subtype: benchmark
created: 2026-08-08
updated: 2026-08-08
tags: [benchmark, world-model, evaluation, long-horizon, memory, interaction-physics, genie-3, alibaba]
sources: 2
---

**WorldRoamBench** — an open-world benchmark for the **long-horizon stability** of *interactive* world models: systems you drive with WASD/IJKL keystrokes that generate frames autoregressively in real time. From AMAP CV Lab (Alibaba Group) with Nanjing University, Tsinghua, and Peking University. 600+ test cases across Nature, Urban, and Indoor scenes, first- and third-person, **10–60 s of continuous interaction** — against the ~5–10 s clips prior benchmarks used.

**The wiki's only source of measured numbers on [Genie 3](genie-3.md).**

## Four dimensions, four new metrics

The contribution is less the leaderboard than the observation that every prior metric was measuring the wrong thing over short clips:

- **Action** — per-frame keystroke accuracy, replacing trajectory-level RPE/ATE. Trajectory metrics suffer *cross-model semantic scale disparity* (models travel different distances per keystroke, so the comparison is unfair) and mask per-step failures where a model ignores a key then over-compensates.
- **Vision** — segment-based *drift*, catching non-monotonic mid-sequence collapse that start-vs-end comparison misses.
- **Physics** — **controllability-gated** scoring over mechanics (collision, clipping, deformation, terrain following, gravity), optics (reflection, shadow occlusion), and 3D consistency. Plausibility counts only when the action was faithfully executed.
- **Memory** — action-decoupled dual track: **scene memory** via transition-localized 3D point-cloud reconstruction, **subject memory** via SAM2 tracking plus Qwen3-VL reasoning.

> [!note] The memory protocol is the rigorous form of a famous informal test
> The [HAI brief](../sources/hai-world-model-spatial-intelligence-brief.md) proposed "move an object, leave the scene, and return to find it where it was left" as the cheap probe of [spatial intelligence](../concepts/world-models/spatial-intelligence.md). WorldRoamBench's contribution is showing that the naive version *doesn't work*: symmetric revisit tests assume perfect action execution, and cumulative drift means the model rarely returns to the same spot, so you measure action error and call it memory failure.

## Leaderboard (first-person, overall)

Genie 3 **73.81** > Happy Oyster 71.06 > Lyra 2.0 70.32 > HY-World 1.5 70.29 > LingBot-World 64.25 > Matrix-Game 3.0 63.31 > SANA-WM 62.16 > Matrix-Game 2.0 56.67 > Yume 1.5 56.21 > minWM 49.47.

Third-person (4 models): Happy Oyster 60.24 > Genie 3 57.04 > LingBot-World 32.19 > HY-World 1.5 15.75.

Closed-source: Genie 3 ([Google DeepMind](google-deepmind.md)) and **Happy Oyster** (Alibaba). Everything else is open.

## The four findings worth carrying

1. **Trajectory score ≠ per-frame correctness** — above 85 on trajectory with below 65% strict per-frame accuracy.
2. **High visual quality ≠ good action following** — "largely independent." The [WorldArena](worldarena.md) perception–functionality gap, found again in a completely different task domain by a different lab.
3. **Stricter physics adherence may compromise action following.** A model that refuses to clip through a wall must deviate from the prescribed trajectory. The honest behavior is scored as an error.
4. **Memory evaluation is confounded by action imprecision** unless explicitly decoupled.

## Position in this wiki

Scores the **renderer** row of the [functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md), where [WorldArena](worldarena.md) scores simulator and planner. The two share an author (Yong Li) and share no models — so the wiki now has both halves of the world-model evaluation picture with no bridge between them.

## Related

- [Genie 3](genie-3.md) — the top-ranked model; this is its only quantitative record here.
- [WorldArena](worldarena.md) · [world-model evaluation](../concepts/world-models/world-model-evaluation.md) · [spatial intelligence](../concepts/world-models/spatial-intelligence.md)

## Mentioned in

- [WorldRoamBench paper](../sources/worldroambench-paper.md)
