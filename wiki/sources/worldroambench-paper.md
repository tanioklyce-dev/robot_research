---
title: "WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models"
type: source
url: https://arxiv.org/abs/2606.31672
local_path: raw/2606.31672.pdf
sha256: ed184e7662911fee1505ced355e196967920adac102658efc05508778c5c7d9a
author: Ting-Bing Xu, Jiacheng Sui, Zhe Gao, Kewei Shi, Wenjin Yang, Zhicheng Liu, Zhaoxu Sun, Mingchao Sun, Hongyu Pan, Fan Jiang, Mu Xu, Qi Fan, Yang Gao, Yong Li, Baoquan Chen
venue: Preprint (arXiv 2606.31672v3)
published: 2026-07-06
ingested: 2026-08-08
license: CC BY 4.0
tags: [benchmark, world-model, evaluation, genie-3, long-horizon, memory, interaction-physics, interactive-world-models]
---

## Summary

**The first hard numbers on [Genie 3](../entities/genie-3.md) in this wiki, and they come from a competitor's lab.** AMAP CV Lab (Alibaba) with Nanjing University, Tsinghua (Yong Li, also on [WorldArena](worldarena-paper.md)), and Peking University benchmark **10+ interactive world models** — including the two closed-source frontier systems, **Genie 3** and Alibaba's own **Happy Oyster** — on *long-horizon stability* under 10–60 seconds of continuous WASD/IJKL keyboard interaction across 600+ test cases in Nature, Urban, and Indoor scenes, first- and third-person.

Its organizing insight is that short clips hide everything that matters. Existing benchmarks evaluate ~5–10 s and score action-following at the *trajectory* level; WorldRoamBench shows that a model can post a trajectory score above 85 while getting **below 65% per-frame strict action accuracy** — following the right path while missing individual keystrokes.

Genie 3 takes first place in first-person view (73.81) and second in third-person, **winning on memory and physics while ranking mid-pack on action following.** No model is strong on all four dimensions.

## Key claims

### The four dimensions, and why each needed a new metric

| Dimension | Problem with prior practice | WorldRoamBench's fix |
|---|---|---|
| **Action** | Trajectory-level RPE/ATE suffers *cross-model semantic scale disparity* (models move different distances for the same keystroke) and masks per-frame failures (ignore a keystroke, then over-compensate) | **Per-frame keystroke-level accuracy**, strict and partial |
| **Vision** | Average quality scores miss *temporal degradation*; start-vs-end comparisons miss non-monotonic mid-sequence collapse | **Segment-based drift metric** over imaging and aesthetic scores |
| **Physics** | Studied for passive video generation, not adapted to interactive control | **Controllability-gated** scoring over mechanics (collision, clipping, deformation, terrain following, gravity), optics (reflection, shadow occlusion), and 3D consistency — plausibility counted *only under faithful action execution* |
| **Memory** | Symmetric revisit tests (compare frame *t* and *T−t*) assume perfect action execution; cumulative drift offsets the "return" frame | **Action-decoupled dual-track**: scene memory via *transition-localized 3D point-cloud reconstruction*, subject memory via SAM2 tracking + Qwen3-VL reasoning |

The memory protocol is the important one. It is the rigorous form of the "leave the scene and return" probe the [HAI brief](hai-world-model-spatial-intelligence-brief.md) offered informally and that this wiki filed under [spatial intelligence](../concepts/world-models/spatial-intelligence.md) — and its central methodological point is that **you cannot measure memory without first decoupling it from action error**, because models rarely hit the turning point exactly.

### First-person view leaderboard

| Rank | Model | Overall | Action | Visual | Physics | Memory |
|---:|---|---:|---:|---:|---:|---:|
| 1 | **Genie 3** (closed) | **73.81** | 84.78 | 68.28 | 68.95 | **73.24** |
| 2 | Happy Oyster (closed) | 71.06 | 87.32 | 69.16 | **72.33** | 55.42 |
| 3 | Lyra 2.0 | 70.32 | 91.41 | 71.61 | 56.99 | 61.26 |
| 4 | HY-World 1.5 | 70.29 | **91.61** | 72.52 | 47.42 | 69.60 |
| 5 | LingBot-World | 64.25 | 91.31 | 67.98 | 47.32 | 50.39 |
| 6 | Matrix-Game 3.0 | 63.31 | 88.82 | 70.56 | 41.25 | 52.60 |
| 7 | SANA-WM | 62.16 | 83.95 | **73.08** | 36.29 | 55.32 |
| 8 | Matrix-Game 2.0 | 56.67 | 84.97 | 61.54 | 34.50 | 45.65 |
| 9 | Yume 1.5 | 56.21 | 71.45 | 70.29 | 44.05 | 39.06 |
| 10 | minWM | 49.47 | 64.20 | 60.55 | 20.74 | 52.41 |

Third-person view (4 models): Happy Oyster **60.24** > Genie 3 57.04 > LingBot-World 32.19 > HY-World 1.5 15.75. TPV overall is weighted by control rate, where Genie 3 manages 77.36 against Happy Oyster's 84.43.

### What the shape of that table says

**Genie 3 wins overall while placing 7th of 10 on action following** (84.78; strict accuracy 75.19 against HY-World 1.5's 89.82 and Lyra 2.0's 87.62). It wins because it is far ahead on **memory** — retention 71.63, hallucination 25.07, both best in class — and strong on physics. The open models that beat it on keystroke fidelity collapse on physics (HY-World 1.5: 47.42; LingBot-World: 47.32) and memory.

Four cross-cutting findings, quoted in substance:

1. **Trajectory score ≠ per-frame correctness.** Models with trajectory scores above 85 can have below 65% strict per-frame action accuracy.
2. **High visual quality ≠ good action following** — the two are "largely independent."
3. **Stricter physics adherence may compromise action following.** Models that refuse to clip through obstacles necessarily deviate from the prescribed trajectory. This is a real tension, not a bug: an honest world model *should* disobey a keystroke that would drive you through a wall.
4. **Memory evaluation is confounded by action imprecision** unless you decouple them — the motivation for the point-cloud protocol.

### Genie 3, specified

The paper's model table gives the wiki its first architecture-adjacent facts, such as they are:

| | Genie 3 |
|---|---|
| Type | Closed |
| Params | **not disclosed** |
| Year | 2025 |
| Views | FPV / TPV |
| Resolution | **1280×704** |
| FPS | **20** |
| Chunk / inference speed / MPPS | not disclosed |

Sharper than the "720p, 20–24 fps" of DeepMind's own materials, and it confirms that no parameter count or throughput figure is public.

## Entities mentioned

- [Genie 3](../entities/genie-3.md) · [Google DeepMind](../entities/google-deepmind.md) · [WorldRoamBench](../entities/worldroambench.md)
- Happy Oyster (Alibaba), Matrix-Game 2.0/3.0, HY-World 1.5, Yume 1.5, LingBot-World, Lyra 2.0, SANA-WM, minWM — no wiki pages
- AMAP CV Lab (Alibaba Group) — no wiki page

## Concepts touched

- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) · [spatial intelligence](../concepts/world-models/spatial-intelligence.md) (the memory protocol) · [world model](../concepts/world-models/world-model.md)
- [World-model functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md) — this benchmark scores the **renderer** row, where WorldArena scores simulator and planner.

## Open questions

- **Everything here is open-world roaming, not manipulation.** WorldRoamBench and WorldArena barely overlap in models or tasks — one benchmarks camera-controlled world *exploration*, the other robot *manipulation*. They are complementary, and no model appears in both, so there is no bridge between "good world to walk through" and "good world to train a robot in."
- **A competitor benchmarked Genie 3.** Alibaba's lab ranks Genie 3 first in FPV and its own Happy Oyster second — which is evidence *against* thumb-on-scale, but the evaluation of closed models runs through whatever public interface those products expose, and the paper notes inputs are mapped "into the closest supported control format for each model."
- **The physics-vs-action tension is unresolved.** If refusing to clip through a wall costs action-following points, the aggregate Overall Score is penalizing correct behavior. Nobody has proposed the right scoring rule.
- **How does the "few minutes of coherence" claim relate to these scores?** The [HAI brief](hai-world-model-spatial-intelligence-brief.md) says Genie 3 stayed coherent a few minutes at its 2025 release; this benchmark runs 10–60 s. The regime where the coherence limit actually bites is longer than anything measured here.
