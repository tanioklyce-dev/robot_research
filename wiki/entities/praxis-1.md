---
title: Praxis-1
type: entity
subtype: model
created: 2026-11-12
updated: 2026-11-12
sources: 3
tags: [praxis-1, runway, world-action-model, open-weights, apache-2, mixture-of-experts, diffusion-transformer, video-pretraining, robolab, droid, yam, so-101, nvfp4]
---

# Praxis-1

[Runway](runway.md)'s **open-weight world-action model**. Runway's video generation model (27B-parameter MoE diffusion transformer, about 2.8B active) is made chunk-causal, mid-trained mostly on egocentric human video, and paired with a 314M action expert that reads the backbone while it imagines the next 1.6 s. It was announced in September 2026 and released under **Apache 2.0** on 2026-11-11 ([launch](../sources/runway-praxis-1-launch.md), [technical report](../sources/runway-praxis-1-technical-report.md)).

## How it works

- **Each call** takes an instruction, the latest camera frames and the robot's pose. It returns **predicted video plus 24 action rows (1.6 s at 15 Hz)** from two joint Euler denoising steps. That takes **about 0.55 s on one H100** for the default chunked mode ([report §5](../sources/runway-praxis-1-technical-report.md#inference-5)).
- **Separate action expert, not mixture-of-transformers.** The expert's eight cross-attention layers each tap a different backbone encoder block. Nothing flows back into the backbone in the forward pass. Putting action tokens inside the backbone made no measurable difference and cost more ([report §2.2](../sources/runway-praxis-1-technical-report.md#architecture-2)). Compare [Cosmos 3](nvidia-cosmos.md)'s MoT layout and [FLUX 3](flux-3.md)'s action decoder on a frozen backbone.
- **Thin per-robot projections** around a shared backbone and expert. Released heads: DROID Franka, bimanual [YAM](yam.md), SO-100/SO-101 joint space, plus the base model for new rigs ([README](../sources/praxis-1-oss-github.md)).
- **Training** has four stages: video pretraining, then embodied-video mid-training (58% egocentric human, 20% general, 18% robot), then joint video and action mid-training with about 30% of tasks still video-only, then embodiment fine-tuning with the video loss kept on.

## Results (self-reported)

| Evaluation | Praxis-1 | Comparison |
|---|---|---|
| [RoboLab-120](nvidia-robolab.md) (10 trials × 120 tasks) | **46.2%** | FLUX 3 Action 42.9, Cosmos 3 Nano 36.8, π0.5 28.0, DreamZero 25.7, GR00T N1.6 7.3 |
| Real Franka FR3 (Positronic, FLUX 3 Action's 10 tasks × 10) | **88/100** | FLUX 3 Action 80/100 |
| [SimplerEnv](simplerenv.md) Google robot, visual matching (RT-1 unseen) | **80.0%** | RT-1 52.4; FLUX 3 Action 39.7 (fine-tuned by Runway) |
| YAM pen-cap, sponge and die tasks vs [GPT-6 Astra](gpt-6-astra.md) | 0:16, $0.04/task | 4:13, $1.87/task |

> [!warning] Read the leaderboard claim carefully
> "#1" means #1 among WAMs and open models. Four RoboLab-120 entries score higher: AMP1 86.0%, SenseNova-RoboRSI 57.1%, Lakeside 51.0%, BiMind v0.5 49.2%. The 3.3-point lead over FLUX 3 Action is **not statistically separable** at n = 1,200 (p ≈ 0.10), and neither is the 88-vs-80 real-robot result (p ≈ 0.12). The lead over Cosmos 3 Nano and the open VLAs is clear ([launch analysis](../sources/runway-praxis-1-launch.md#where-the-launch-post-goes-past-its-own-primary)).

## What the report shows about WAMs in general

- **The error is in the imagined future.** Given the true future video, action error is **1.14 cm**. When the model imagines its own, it is **5.71 cm**. Failures on look-alike objects are *"usually already visible in the imagined video"* ([report §10, §12](../sources/runway-praxis-1-technical-report.md#offline-evaluation-10)).
- **More mid-training compute gave better fine-tunes, then leveled off.** RoboLab rose 25.5 → 41.2% over five checkpoints, and the fifth checkpoint added nothing.
- **The predicted future can score itself.** A frozen-feature head predicts real-robot success at AUROC 0.77 after about 6 s, on an earlier model. Runway names this as its path toward a *"self-improving world action model"*.
- **4-bit is nearly free.** NVFP4 routed experts with QAT give 46.5% vs 47.8% and shrink the model from 54.4 to 17.5 GB.

## Availability and hardware

Weights and code are released under Apache 2.0, for commercial use. Distribution is via Hugging Face (`runwayml/praxis-1-*`) with LeRobot support, GitHub `runwayml/praxis-1-oss`, vLLM-Omni, NeMo Automodel tutorials, and hosted inference. The quick start needs **an 80 GB GPU**. The NVFP4 checkpoints (about 23.5 GB with encoders) target Blackwell and [Jetson Thor](jetson-thor.md). RTX 5090 fit is *"not measured yet"* ([README](../sources/praxis-1-oss-github.md)).

## Related

- [Runway](runway.md) · [FLUX 3](flux-3.md) (closest competitor, same video-model origin) · [NVIDIA Cosmos](nvidia-cosmos.md) · [DreamZero](dreamzero.md)
- [World-action model](../concepts/world-models/world-action-model.md) · [Mixture of experts](../concepts/learning/mixture-of-experts.md) · [Cross-embodiment](../concepts/learning/cross-embodiment.md)

## Mentioned in

- [Praxis-1 Is Now Available (launch)](../sources/runway-praxis-1-launch.md)
- [Praxis-1 technical report](../sources/runway-praxis-1-technical-report.md) — the primary.
- [praxis-1-oss GitHub README](../sources/praxis-1-oss-github.md) — the hardware facts.
