---
title: "A Control-Centric Benchmark for Video Prediction (VP²) — Tian, Finn & Wu, ICLR 2023"
type: source
url: https://arxiv.org/abs/2304.13723
local_path: raw/2304.13723.pdf
code: https://github.com/s-tian/vp2
author: Stephen Tian, Chelsea Finn, Jiajun Wu
affiliations: Stanford University
venue: ICLR 2023
published: 2023-04-26
ingested: 2026-08-08
tags: [benchmark, video-prediction, world-model, evaluation, visual-foresight, mpc, robosuite, robodesk, control-centric]
---

## Summary

**The origin of the finding the whole 2026 world-model evaluation literature is built on, three years early.** Perceptual metrics — FVD, LPIPS, SSIM — are unreliable predictors of whether a video prediction model can actually control a robot. VP² (Video Prediction for Visual Planning) makes that measurable by standardizing *everything* in a model-predictive-control pipeline except the video predictor, then scoring models by **task success rate** instead of pixel similarity.

Everything the wiki filed in 2026 as news — [WorldArena](worldarena-paper.md)'s r = 0.360, the [action-relevance probes](action-relevant-latents-paper.md), the [latent-space study](latent-space-robotic-world-models-paper.md) — is a rediscovery or extension of this paper at larger scale. Both 2026 probe papers cite it as the prior result.

Also worth noting whose names are on it: **Chelsea Finn and Jiajun Wu**. Finn's group later produced [Ctrl-World](../entities/ctrl-world.md), the best-measured policy evaluator in [WorldArena](../entities/worldarena.md); Wu co-authored **WorldScore** and the [HAI policy brief](hai-world-model-spatial-intelligence-brief.md) that told policymakers no adequate benchmark exists. The people who first showed the problem are still working it.

## Key claims

### The mismatch, demonstrated

Six models — FitVid and SVG′, each trained with plain MSE and with an auxiliary LPIPS loss at weights 1 and 10 — scored on perceptual metrics *and* on control success. Selected rows:

| Environment | Model | FVD ↓ | LPIPS ↓ | SSIM ↑ | **Control success** |
|---|---|---:|---:|---:|---:|
| robosuite push | SVG′ MSE | **51.7** (worst) | 5.1 | 82.7 | **80%** (best) |
| robosuite push | FitVid +LPIPS=1 | 18.0 | 2.8 | **89.3** | 67% |
| robosuite push | FitVid +LPIPS=10 | 24.3 | 4.1 | 84.6 | **35%** |
| RoboDesk open slide | SVG′ +LPIPS=1 | **4.9** (best) | 2.06 | 89.7 | **10%** |
| RoboDesk open slide | SVG′ MSE | 22.5 | 1.88 | 90.6 | **58%** |
| RoboDesk red button | FitVid MSE | 9.0 | 0.62 | 97.4 | 58% |
| RoboDesk red button | FitVid +LPIPS=1 | 5.9 | 0.63 | 97.5 | **82%** |
| RoboDesk red button | FitVid +LPIPS=10 | 6.8 | 0.70 | 97.3 | **32%** |

Read the inversions:

- On **robosuite pushing**, the model with the *worst* FVD in the table (51.7) has the *best* control success (80%).
- On **open slide**, the best FVD in the entire study (4.9) scores **10%**; the worst FVD on that task (22.5) scores **58%**.
- On **red button**, SSIM ranges over 0.2 points (97.3–97.5) while success ranges from **32% to 82%**.

The paper's own summary: models improving on these metrics "do not always perform well when used for planning, and the degree to which they are correlated with control performance appears highly task-dependent." On some tasks FVD tracks success well; on others it inverts. **The correlation isn't just weak — its sign is task-dependent**, which is worse, because it means you cannot correct for it with a constant.

The mechanism is illustrated directly: a model can produce crisp, perceptually excellent frames that are *physically infeasible* — in their Figure 1, predicting that a slide moves on its own. Sharpness and physics are separately optimizable.

### What VP² actually is

- **11 task categories, 310 task instances**, two simulated environments: a **robosuite** tabletop (4 push tasks × 25 instances, object textures randomized from a set of 13) and **RoboDesk** (7 tasks: push red/green/blue button, open slide/drawer, push upright/flat block off table).
- **Training datasets included**: 50K scripted-policy trajectories for robosuite, 5K per RoboDesk task (35K total), 35 timesteps at 256×256, with Gaussian action noise so success rates vary.
- **The full control stack is part of the benchmark** — visual foresight with MPPI sampling, 2 context frames, 10 predicted frames, task-specific pretrained classifier cost functions, tuned hyperparameters. Only the predictor is swapped.
- **Interface is one function.** `__call__(context_frames, action_seq) → predictions`. No differentiability requirement, no architecture assumption, no RL expertise needed. A design choice worth copying.
- **A simulator-as-model upper bound.** Running the same planner on ground-truth dynamics separates "the model is bad" from "the planner or cost function is bad." Most benchmarks in this wiki lack this control.

### The scaling results, which have aged well

Five competitive models benchmarked — FitVid, SVG′, MCVD (diffusion), Struct-VRNN, MaskViT:

- **Model capacity doesn't buy control performance.** Across **6M → 300M** parameters there is no strong trend; the authors hypothesize larger FitVid variants *overfit* to action sequences in the dataset.
- **Data quantity plateaus fast.** From 1K to 50K trajectories, gains arrive early and flatten, attributed to the constrained action distribution of a scripted collection policy.
- **Diffusion is prohibitively slow for planning.** Forward pass for 10 frames: FitVid-full (302M) **5.63 s**, SVG′ (325M) 3.58 s, FitVid-mini (2.3M) 0.29 s — **MCVD (56M) 220 s**. Competitive control performance at ~39× the full-FitVid cost and ~758× the mini cost.
- **Uncertainty awareness helps, unevenly.** A 4-model ensemble-disagreement penalty improved one task, was neutral on a second, slightly hurt a third.

## Entities mentioned

- [Chelsea Finn](../entities/chelsea-finn.md) · [robosuite](../entities/robosuite.md) · [Franka Panda](../entities/franka-panda.md) (RoboDesk)
- FitVid, SVG′, MCVD, Struct-VRNN, MaskViT, RoboDesk — no wiki pages

## Concepts touched

- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) — this is the founding source.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) · [world-model simulators](../concepts/world-models/world-model-simulators.md) · [optimal control](../concepts/robotics/optimal-control.md) (MPPI / visual foresight)

## Open questions

- **Why did it take three years to be rediscovered at scale?** VP² is open-source with a one-function interface, and the 2026 benchmarks ([WorldArena](../entities/worldarena.md), WorldRoamBench) built new infrastructure rather than extending it. Neither cites VP² as a design ancestor, though both reach its conclusion.
- **Nobody has run VP² on a modern model.** [Cosmos](../entities/nvidia-cosmos.md), [Genie 3](../entities/genie-3.md), Wan, and Veo did not exist in 2023. The benchmark's whole premise is a one-function interface — running it on a 2026 world model is cheap and nobody has published it.
- **The "capacity doesn't help" result predates the scaling era.** 300M was large in 2023. Whether the plateau survives at 14B (DreamDojo) is untested and matters a great deal for the field's central bet.
- **Simulation only**, 64×64 goal images, scripted data collection — the authors flag the narrowness themselves.
