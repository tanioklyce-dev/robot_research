---
title: WorldArena
type: entity
subtype: benchmark
created: 2026-08-08
updated: 2026-08-08
sources: 3
tags: [benchmark, world-model, evaluation, ewmscore, robotwin, visuotactile, tsinghua]
---

**WorldArena** — a unified benchmark for **embodied world models**, scoring them on perceptual quality *and* on functional utility in the three roles they actually get deployed in: **data engine**, **policy evaluator**, **action planner**. Led by Yu Shang with Yong Li (Tsinghua) corresponding; eight-to-ten institutions across both versions. Public leaderboard at `world-arena.ai`.

The wiki's answer to "how would you ever know if a world model is any good?" — and the source of its most-cited number on the subject.

## The perception–functionality gap

WorldArena's central result. **EWMScore** — the unweighted mean of 16 video-quality metrics across six sub-dimensions, scaled 0–100 — correlates with:

| Against | Pearson r |
|---|---:|
| Human judgment | **0.825** |
| Data-engine utility | 0.600 |
| **Action-planning performance** | **0.360** |

Visual realism predicts what people *think* of a world model and barely predicts what it is *for*. ([WorldArena paper](../sources/worldarena-paper.md))

## Versions

| | WorldArena (Feb 2026) | WorldArena 2.0 (May 2026) |
|---|---|---|
| Models | 14 | 12 |
| Modality | Vision | **+ visuotactile** (UniVTAC; tactile VAE + two-stream + action diffusion head) |
| Functional roles | Data engine, policy evaluator, action planner | **+ online interactive RL environment** |
| Platforms | [RoboTwin 2.0](robotwin.md) | + [LIBERO](libero.md) + **real AgileX Split-Type [ALOHA](aloha.md)** |
| Source | [paper](../sources/worldarena-paper.md) | [paper](../sources/worldarena-2-paper.md) |

## Headline findings

- **Nobody beats real data as a data engine.** Only RoboMaster and WoW exceed real-data policy training, and only on the easier of two tasks. The gap widens going from simulation to a real robot.
- **A dedicated VLA beats every world model as a planner by 3–4×** — [π0.5](pi-zero-5.md) at 77%/66% against a best-world-model 20%/21%.
- **But as an *RL environment* world models work.** Policies trained inside them reach ~⅔ of the gap to simulator-based RL (WoVR 75.00 vs simulator 87.30) and beat SFT across the board. The role split — learned dynamics are good enough to *shape* a policy, not to *be* one — is the cluster's most useful finding.
- **Learned policy evaluators inflate scores.** Both evaluated models report "consistently higher success rates than those measured in the simulator, suggesting partial overfitting to successful trajectories." Ctrl-World still ranks policies almost perfectly (r = 0.986); Cosmos-Predict 2.5 does not (r = 0.483).
- **Simulation performance is not a proxy for real-world deployment.** Functional rankings correlate between two simulators, then "drop greatly" against a physical ALOHA.
- **General video models win on looks, embodied models win on dynamics.** Veo 3.1 and Wan 2.6 top visual and aesthetic scores but "show limited improvements in embodied-specific metrics"; visually strong models "suffer from semantic drift."

## Position in this wiki

The world-model counterpart to [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) and to [LIBERO-PRO](../sources/libero-pro-paper.md): all three are instruments that make previously-published numbers look worse. It supplies the primary evidence for [world-model evaluation](../concepts/world-models/world-model-evaluation.md) and is the benchmark the [HAI policy brief](../sources/hai-world-model-spatial-intelligence-brief.md) singled out as the only one scored on downstream usefulness.

Built on [RoboTwin 2.0](robotwin.md), which makes it a bimanual counterweight to the wiki's LIBERO-heavy evaluation record.

## Caveats

> [!note] Two tasks carry the functional results
> Video quality uses all 50 RoboTwin scenarios, but the data-engine and action-planner numbers rest on *adjust bottle* and *click bell* at 100 trials each — roughly ±10 pp by the wiki's own [rollout-count standard](../concepts/robotics/robot-policy-evaluation.md). Adequate for the 3–4× gaps; not adequate for ranking adjacent models. The data-engine test also uses only **25 synthetic trajectories** per model.

## Related

- [WorldRoamBench](worldroambench.md) — the sibling instrument for *interactive* world models (roaming, not manipulation); shares Yong Li.
- [Ctrl-World](ctrl-world.md) — the standout performer across both versions.
- [RoboTwin 2.0](robotwin.md) · [LIBERO](libero.md) · [π0.5](pi-zero-5.md) · [Veo](veo.md) · [Genie Envisioner](genie-envisioner.md) · [NVIDIA Cosmos](nvidia-cosmos.md)

## Mentioned in

- [WorldArena paper](../sources/worldarena-paper.md)
- [WorldArena 2.0 paper](../sources/worldarena-2-paper.md)
- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../sources/hai-world-model-spatial-intelligence-brief.md)

## Adopted as a metric component

[Reconstruction or Semantics?](../sources/latent-space-robotic-world-models-paper.md) (Mila, May 2026) uses **WorldArena's perceptual and geometric scores** as part of its own visual-fidelity axis, alongside FID / SSIM / LPIPS / FVD / point-track consistency — the first instance in this wiki of WorldArena being reused as infrastructure rather than cited as a result. Three months from publication to dependency.

## Mentioned in (additional)

- [Reconstruction or Semantics?](../sources/latent-space-robotic-world-models-paper.md)
