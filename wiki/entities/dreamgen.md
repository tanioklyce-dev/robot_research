---
title: DreamGen
type: entity
subtype: method
created: 2026-07-04
updated: 2026-08-27
sources: 3
tags: [dreamgen, neural-trajectories, video-world-model, synthetic-data, nvidia, gear, vla, dream-star]
---

**DreamGen** — NVIDIA GEAR's method for turning image-to-video generative models into **synthetic data generators for robot policy training**, producing "neural trajectories" (synthetic video + pseudo-action pairs). The **root of the [GEAR](nvidia-gear.md) Dream\* world-model line** (DreamGen → DreamZero → [DreamDojo](../sources/dreamdojo-paper.md)) and the source of the neural-trajectory data layer in the [GR00T](nvidia-groot.md) data pyramid. Primary source: [DreamGen Paper](../sources/dreamgen-paper.md) (arXiv 2505.12705, June 2025); co-led by [Joel Jang](joel-jang.md), advised by [Yuke Zhu](yuke-zhu.md) + [Jim Fan](jim-fan.md).

## The 4-stage pipeline
1. Fine-tune a video world model (primarily **WAN 2.1**; also tests [Cosmos](nvidia-cosmos.md)) on a small amount of teleop from a *single* behavior in a *single* environment (LoRA).
2. Roll it out with new initial frames + language instructions to generate photorealistic robot videos (only *initial frames* needed for new environments — no physical data collection).
3. Recover pseudo-action labels via an **IDM** (flow-matching inverse dynamics) or a **LAPA latent-action model**.
4. Train visuomotor policies ([Diffusion Policy](diffusion-policy.md), [π0](pi-zero.md), [GR00T N1](nvidia-groot.md)) on the resulting **neural trajectories**.

## Why it matters
- **Video generation as a data-scaling axis for VLAs.** Neural trajectories are the "middle-of-the-pyramid" synthetic layer that [GR00T N1](../sources/groot-n1-paper.md) (827 h of WAN2.1-generated video) and [GR00T N1.5](../sources/groot-n1_5.md) both consume. DreamGen is the named method behind that layer.
- **Zero-to-one generalization.** A humanoid learns 22 new behaviors with zero teleop for those verbs (behavior gen 11.2%→43.2%; environment gen 0%→28.5%) — see [paper](../sources/dreamgen-paper.md).
- **DreamGen Bench** gives video-model researchers a robot-free proxy (Instruction Following + Physics Alignment) that correlates with downstream policy success.

## Related
- [DreamDojo](../sources/dreamdojo-paper.md) — the later Dream\* entry (foundation generative-video WM); DreamGen is the origin of the line.
- [NVIDIA GEAR](nvidia-gear.md) — originating lab. [Joel Jang](joel-jang.md) — co-lead.
- [NVIDIA Cosmos](nvidia-cosmos.md) — one of the video WMs benchmarked in DreamGen Bench.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — DreamGen is the "WM-as-data-generator" instance.
- [GR00T N1](nvidia-groot.md) — largest downstream gains among the three tested policies.

## Mentioned in
- [DreamGen Paper](../sources/dreamgen-paper.md) — **primary source**
- [GR00T N1.5 research page](../sources/groot-n1_5.md) — DreamGen neural trajectories in the N1.5 training mix
- [NVIDIA GEAR Lab — Publications](../sources/nvidia-gear-publications.md) — lists DreamGen in the Dream\* pillar
- [Introducing Index (Figure AI)](../sources/figure-index-announcement.md) — Cited as one of the wiki's published answers to the human→robot label problem ([IDM pseudo-labelling](../concepts/learning/crowdsourced-robot-training-data.md)) that the Index announcement never addresses.

## Open questions
- **DreamZero** — the middle Dream\* entry (between DreamGen and [DreamDojo](../sources/dreamdojo-paper.md)) has no source page yet.
- The DreamGen paper references [GR00T N1](../sources/groot-n1-paper.md) only, not N1.5 — the N1.5 link is via the N1.5 page, not the DreamGen paper (both are mid-June 2025).
