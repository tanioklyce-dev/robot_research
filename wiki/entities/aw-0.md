---
title: AW-0 (Agentic World Action Model)
type: entity
subtype: model
created: 2026-10-27
updated: 2026-10-27
sources: 1
tags: [aw-0, world-action-model, code-as-policy, mixture-of-transformers, masked-diffusion, nvidia-gear, uc-berkeley, yam, sharpa-wave, skill-library]
---

**AW-0** is a UC Berkeley / NVIDIA / U. Penn [world-action model](../concepts/world-models/world-action-model.md) (October 2026) that adds a **code expert** to a video+action WAM. It jointly denoises a skill-program slice, future video and a 64-D action chunk ([AW-0 paper](../sources/agentic-world-action-models-aw0-paper.md)).

## Architecture
- Three-expert mixture-of-transformers, attention order **code → video → action** ([paper §2.1](../sources/agentic-world-action-models-aw0-paper.md)).
- Code: masked discrete diffusion on a mostly frozen SDAR-1.7B + frozen Qwen3-VL-2B ViT. Video: flow matching on a [Cosmos-Predict2.5-2B](nvidia-cosmos.md) DiT with a Wan2.2 VAE. Action: flow-matching DiT, horizon 32.
- 0.23 s per inference on one RTX 5090 (4 joint denoising steps); the code expert adds 0.04 s.
- Two execution modes. **Default**: the code is never executed and only conditions the actions. **Hybrid**: a decoded slice runs against a skill/primitive namespace if it passes stage, dependency, syntax and whitelist gates; otherwise the action chunk drives the robot.

## Data
- Pretrained on 2,913 h: 1,919 h [YAM](yam.md) bimanual teleop + 994 h egocentric human video retargeted to 22-DoF hands.
- Program labels come from an agentic pipeline (Gemini 3.1 Pro writer + Claude Code/Opus 4.8 coordinator) that distills a frozen **50-skill library** (23 YAM, 27 human).

## Results
- [RoboTwin 2.0](robotwin.md): 80.8% clean (best baseline 64.8%). Randomized: 20.6%, below π0.5 at 27.7%; the hybrid mode reaches 29.2%.
- Real world, 8 tasks on YAM grippers and Tianji + [Sharpa Wave](sharpa-wave.md) hands: 71.1 average rubric score against 46.0 for DreamZero and 43.6 for π0.5.

## Why it matters in this wiki
It is the first system in the wiki to put [code-as-policy](../concepts/agents/code-as-policy.md) **inside** a learned policy rather than around one. Its group is the [NVIDIA GEAR](nvidia-gear.md)/Berkeley one behind [CaP-X](cap-x.md) and [ASPIRE](aspire.md), so the two halves of the agentic-vs-end-to-end debate now come from the same authors.

## Related
- [Cosmos 3](nvidia-cosmos.md): the other MoT WAM. [EgoScale](../sources/egoscale-paper.md) is a baseline here.
- People: [Jim Fan](jim-fan.md), [Yuke Zhu](yuke-zhu.md), [Guanzhi Wang](guanzhi-wang.md), [Ken Goldberg](ken-goldberg.md).

## Mentioned in
- [Agentic World Action Models (AW-0) paper](../sources/agentic-world-action-models-aw0-paper.md): primary source.
