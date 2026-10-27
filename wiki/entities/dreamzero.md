---
title: DreamZero
type: entity
subtype: model
created: 2026-10-27
updated: 2026-10-27
sources: 4
tags: [dreamzero, world-action-model, nvidia-gear, wan2-1, video-diffusion, autoregressive, agibot-g1, droid, open-weights]
---

**DreamZero** is [NVIDIA GEAR](nvidia-gear.md)'s 14B [world-action model](../concepts/world-models/world-action-model.md) (February 2026). It fine-tunes Wan2.1-I2V-14B to generate future video and actions jointly, autoregressively in 1.6 s chunks ([DreamZero paper](../sources/dreamzero-paper.md)).

## Design
- One network, one shared flow-matching timestep for video and action. Actions are effectively inverse dynamics on the imagined video ([paper §3.1](../sources/dreamzero-paper.md)).
- In closed loop, real observations overwrite the predicted frames in the KV cache after each chunk. Visual memory is 6.6 s.
- Inference is 5.7 s → 150 ms per chunk (38×) via CFG parallelism, DiT caching, compile/kernels, NVFP4 and **DreamZero-Flash** (high-noise video, uniform action timesteps). That gives ~7 Hz on 2 × GB200.
- Weights, inference code and eval code are open (github.com/dreamzero0/dreamzero).

## Results
- **Own paper (unseen environments):** AgiBot G1, 62.2% seen / 39.5% unseen-task progress against 27.4% / 16.3% for the best pretrained VLA. On DROID-Franka, 22.5% unseen-task success against 12.5% for GR00T N1.6. 10–20 minutes of video-only YAM or human demos: 38.3 → 55.4 / 54.3%.
- **Independent benchmarks:**
  - [Cosmos 3](../sources/cosmos-3-technical-report.md) RoboLab-120: 25.2% against π0.5 28.1% and Cosmos3-Nano-Policy 39.7%.
  - [AW-0](../sources/agentic-world-action-models-aw0-paper.md), 8 real tasks: 46.0 rubric, against π0.5 43.6 and AW-0 71.1. It is strongest on contact-rich tasks and weaker on semantic ones.
  - [Isaac Lab-Arena](isaac-lab-arena.md) v0.3 ships a DreamZero policy integration.

## Lineage
DreamZero is one of the three Dream* papers, alongside [DreamGen](dreamgen.md) (video model as data generator) and [DreamDojo](../sources/dreamdojo-paper.md) (action-conditioned simulator on human video). DreamZero (2026-02-17) postdates DreamDojo (2026-02-06), so the two are **parallel branches**, not a sequence: DreamDojo *consumes* actions and DreamZero *emits* them.

## Related
- People: [Joel Jang](joel-jang.md), [Jim Fan](jim-fan.md), [Yuke Zhu](yuke-zhu.md) (project leads); [Guanzhi Wang](guanzhi-wang.md).
- Platforms: [AGIBOT](agibot.md) G1, [DROID](droid.md)/[Franka](franka-panda.md), [YAM](yam.md).

## Mentioned in
- [DreamZero paper](../sources/dreamzero-paper.md): primary source.
- [AW-0 paper](../sources/agentic-world-action-models-aw0-paper.md): pure-WAM baseline.
- [Cosmos 3 technical report](../sources/cosmos-3-technical-report.md): RoboLab baseline.
- [Isaac Lab-Arena GitHub](../sources/isaaclab-arena-github.md): policy integration.
- [NVIDIA GEAR publications](../sources/nvidia-gear-publications.md): listed.
