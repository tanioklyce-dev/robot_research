---
title: "Cosmos 3 Edge — NVIDIA's 4B on-device world model (Hugging Face blog)"
type: source
url: https://huggingface.co/blog/nvidia/cosmos3edge
author: Pranjali Joshi, Saeed Babamohamadi (NVIDIA), with Hugging Face contributors
affiliations: NVIDIA; Hugging Face
published: 2026-07-20
ingested: 2026-07-27
tags: [nvidia, cosmos, cosmos3-edge, world-model, world-action-model, edge-ai, jetson-thor, droid, distillation, vla, huggingface]
---

## Summary

The launch of **Cosmos 3 Edge**, the **4B-parameter** member of the [Cosmos 3](../entities/nvidia-cosmos.md) family, aimed at running a world model *on the robot* rather than in a datacenter. The wiki had been tracking this variant as announced-but-undelivered; this is the delivery. The headline deployment number is **15 Hz real-time control on [Jetson Thor](../entities/jetson-thor.md)**, emitting **32 actions per inference at 640×360** — which puts a 4B omnimodal world-action model squarely in the reactive-control band on edge hardware, something no VLA in this wiki had achieved on Jetson. It ships alongside a DROID-finetuned policy variant and two **step-distilled 64B Super** models claiming **25× faster inference** (50 → 4 denoising steps).

## What shipped

| Model | Params | What it is |
|---|---|---|
| **Cosmos3-Edge** | 4B | Base on-device world model |
| **Cosmos3-Edge-Policy-DROID** | 4B | Manipulation policy fine-tuned on [DROID](../entities/droid.md) |
| **Cosmos3-Super-Image2Video-4Step** | 64B | Step-distilled I2V — **25×** faster |
| **Cosmos3-Super-Text2Image-4Step** | 64B | Step-distilled T2I |

Available on Hugging Face under `nvidia/Cosmos3-Edge`; frameworks and tooling via `github.com/NVIDIA/cosmos`. **vLLM integration is stated as forthcoming.**

## Architecture

**Dual-transformer design** (consistent with the [Cosmos 3 technical report](cosmos-3-technical-report.md)'s omnimodal framing):

- An **autoregressive tower** for vision/text understanding and reasoning.
- A **diffusion tower** for video, audio, and action prediction/generation.
- **Shared multimodal attention layers** aligning information across the two.

**Unified action representation** — one encoding covering translation, rotation, and manipulation state across embodiments: vehicle ego-pose, camera motion, end-effector pose, gripper state. This is the [world-action model](../concepts/world-models/world-action-model.md) claim made concrete: the same action space spans driving and manipulation.

**Bidirectional action flow** — the model can predict the *effects* of actions **or** infer the actions that explain an observed visual change. Inverse and forward dynamics in one model.

## Hardware and performance

**Targets:** [Jetson Thor](../entities/jetson-thor.md) (**15 Hz**, 32 actions/inference @ 640×360), Jetson **T2000 / T3000**, RTX PRO, GeForce RTX, DGX.

**Benchmarks as claimed:**
- **#1 among 4B models on VANTAGE-Bench** (vision analytics).
- SOTA claimed for robot policy learning and smart infrastructure.
- The distilled **I2V** model **#1 on the Artificial Analysis Image-to-Video leaderboard** (2026-07-23).
- The distilled **T2I** model **#2 among open-weight models**.
- Step distillation: **50 → 4 denoising steps, ~25× faster, "minimal quality loss."**

> [!note] The 15 Hz figure is the wiki-relevant one
> Placed on the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md): 15 Hz on Thor sits **above** GR00T N1.6's 10.9 Hz official TensorRT on the same board and near the community-optimized 22–24 Hz — from a model that is also a *world* model, not just a policy. It is the first 2026-class edge number the wiki has for anything in this class. Caveats: it is a **vendor self-report**, the resolution (640×360) is low, and "32 actions per inference" means the *control* rate depends on chunk consumption — 15 Hz is inference rate, not necessarily closed-loop rate.

## Post-training and extensibility

NVIDIA ships distillation recipes and training scripts so developers can fine-tune on H100/DGX Station clusters, adapt to domain-specific workloads before deployment, and **distill their own Cosmos3 checkpoints** for application-specific latency targets. The distillation recipe being released — not just the distilled weights — is the more consequential half.

## Capabilities as described

- **World modeling** — predicts environment changes, object relationships, and action effects.
- **Policy mode** — generates actions together with their expected visual consequences.
- **On-device reasoning** — no datacenter dependency.

## Entities mentioned

- [NVIDIA Cosmos](../entities/nvidia-cosmos.md) — the family; this is its edge tier.
- [Jetson Thor](../entities/jetson-thor.md) — the flagship deployment target.
- [DROID](../entities/droid.md) — the policy variant's fine-tuning dataset.
- [NVIDIA](../entities/nvidia.md), [Hugging Face](../entities/hugging-face.md) — publisher and host.

## Concepts touched

- [World-action model](../concepts/world-models/world-action-model.md) — unified action representation across embodiments; bidirectional action flow.
- [World models](../concepts/world-models/world-model.md).
- [VLA models](../concepts/learning/vla-models.md) — Cosmos3-Edge-Policy-DROID competes directly with the wiki's VLA table.
- [Control-rate ladder](../syntheses/platforms/control-rate-ladder.md) — the 15 Hz Thor datapoint.

## Open questions

- **No RoboLab-120 or LIBERO number for Cosmos3-Edge-Policy-DROID.** The [Cosmos entity](../entities/nvidia-cosmos.md) carries **Cosmos3-Nano-Policy-DROID (16B) at 39.7% vs π0.5's 28.1%** on [RoboLab-120](../entities/nvidia-robolab.md); the 4B **Edge** policy's score is unpublished. Without it there is no way to price the 16B→4B drop.
- **What is VANTAGE-Bench?** Named as the vision-analytics benchmark Cosmos3-Edge tops among 4B models; no wiki page, no description given, and "#1 among 4B models" is a narrow field.
- **Is 15 Hz measured under the full pipeline?** Camera-to-action end-to-end, or model forward only? The [Cutting the Cord](cutting-the-cord-untethered-xlerobot.md) numbers this would be compared against are explicitly end-to-end camera→action.
- **Power draw on Thor at 15 Hz** is not given — the [Jetson ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md) shows Thor's sub-120 W modes cost ~40% of GPU throughput, so 15 Hz likely assumes the full envelope.
- **License** for the Edge variants is not stated in the blog. Nano/Super were released under **OpenMDW-1.1**; whether Edge matches is unconfirmed.
- **T2000/T3000 numbers** — named as targets with no measurements.
