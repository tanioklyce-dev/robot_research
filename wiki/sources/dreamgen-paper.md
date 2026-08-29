---
title: DreamGen — Unlocking Generalization in Robot Learning through Video World Models (paper)
type: source
url: https://arxiv.org/abs/2505.12705
project_page: https://research.nvidia.com/labs/gear/dreamgen
author: Joel Jang, Seonghyeon Ye, Zongyu Lin, Jiannan Xiang, … Ming-Yu Liu, Jan Kautz, Dieter Fox, Scott Reed; advisors Yuke Zhu & Jim Fan (NVIDIA GEAR + 8 universities)
published: 2025-06-17 (arXiv 2505.12705v2)
ingested: 2026-07-04
local_path: raw/dreamgen_2505.12705v2.pdf
sha256: e4e2c5c9e664d9331adb49c230053a76cf5bb4c3501341f4d9b372ecc585684c
format: pdf (18 pp.)
tags: [dreamgen, neural-trajectories, video-world-model, synthetic-data, nvidia, gear, vla, latent-actions, idm, generalization]
---

## Summary

The primary paper for **[DreamGen](../entities/dreamgen.md)** — NVIDIA GEAR's method for turning image-to-video generative models into **synthetic data generators for robot policy training**. A 4-stage pipeline: fine-tune a video world model on a *single* behavior in a *single* environment, prompt it with new initial frames + language to generate photorealistic robot videos, extract pseudo-action labels (via IDM or LAPA latent actions), and train visuomotor policies on the resulting **"neural trajectories."** This is the source of the "neural trajectory" data layer in the [GR00T N1](groot-n1-paper.md) data pyramid and the [GR00T N1.5](groot-n1_5.md) training mix. Headline: a humanoid learns **22 new behaviors** in seen *and* unseen environments with **zero teleop data for those verbs** (behavior generalization 11.2%→43.2%; environment generalization 0%→28.5%). Co-led by [Joel Jang](../entities/joel-jang.md); advised by [Yuke Zhu](../entities/yuke-zhu.md) + [Jim Fan](../entities/jim-fan.md).

## Key claims

### The 4-stage pipeline (§2)
1. **Video world model fine-tuning (§2.1)** — fine-tune an image-to-video model (primarily **WAN 2.1**; also tests [Cosmos](../entities/nvidia-cosmos.md)) on human teleop to adapt it to the target embodiment. **LoRA** (rank 4, α 4, lr 1e-4). Multiview datasets tiled into a 2×2 grid before fine-tuning.
2. **Rollout (§2.2)** — prompt with new initial frames + language instructions; randomize object/environment positions. For environment generalization, only *initial frames* of new environments are captured — **no physical data collection** (zero-shot transfer).
3. **Pseudo-action labeling (§2.3)** — generated videos lack actions, recovered two ways: an **IDM** (diffusion transformer + SigLIP-2, flow-matching, conditioned on two frames, sliding window) or a **LAPA latent-action model** (VQ-VAE visual-delta over current + 1s-ahead frames; pre-quantized continuous embedding following GR00T N1; LAPA training mix = 438.1M frames across 10 datasets).
4. **Policy training (§2.4)** — train visuomotor policies (state zeroed) on neural trajectories, either co-trained with real trajectories (1:1) or *solely* on neural trajectories. Validated on **[Diffusion Policy](../entities/diffusion-policy.md), [π0](../entities/pi-zero.md), and [GR00T N1](../entities/nvidia-groot.md)**.

### Results (hard numbers)
- **RoboCasa sim scaling (§3.1)**: synthetic data scaled up to **333×** original human demos; **log-linear** policy-success improvement up to 240K neural trajectories (LAPA high-GT 49.6→**58.21%** avg over 24 tasks; low-GT 17.4→**22.07%**). Generating the 240K set took **54 hours on 1,500 L40 GPUs**. Training *solely* on IDM-labeled neural trajectories (no GT actions) still reaches ~20.6% — neural-trajectory quality approaches ground truth.
- **Real-world augmentation (§3.1)** — low-data (10 demos/task) + neural trajectories: **GR1 humanoid 22.5%→37% (DP), →46.4% (GR00T N1)**; **Franka 21%→45.5%**; **SO-100 23%→37%** (strawberry pick-and-place 25→65 with GR00T N1). Tasks are contact-rich/deformable (towel folding, liquid wiping, hammering, M&M scooping) — hard to simulate.
- **Generalization (§3.2)**, video WM trained on ~2,884 pick-and-place trajectories: **behavior generalization 11.2%→43.2%** (14 novel-verb tasks, seen envs); **environment generalization 0%→28.5%** (novel env + novel behavior — a true zero-to-one; the pick-and-place-only baseline scores 0%). 22 total new behaviors.
- **DreamGen Bench (§4)** — a video-generation benchmark for robotics scoring **Instruction Following (IF)** + **Physics Alignment (PA)** (rated by GPT-4o / Qwen2.5-VL / human). Benchmarks Hunyuan, CogVideoX, WAN 2.1, [Cosmos](../entities/nvidia-cosmos.md); **DreamGen Bench score positively correlates with downstream RoboCasa policy success** (Fig. 6) — a robot-free proxy for video-model researchers. GR00T N1 gets the largest downstream gains among the three policy classes (its separate action encoder/decoder pairs well with zero-state neural trajectories).

## Entities mentioned
- [DreamGen](../entities/dreamgen.md) — this is its primary source. [NVIDIA GEAR](../entities/nvidia-gear.md); co-leads incl. [Joel Jang](../entities/joel-jang.md); advisors [Yuke Zhu](../entities/yuke-zhu.md) + [Jim Fan](../entities/jim-fan.md).
- Video world models: WAN 2.1 (primary), [NVIDIA Cosmos](../entities/nvidia-cosmos.md), CogVideoX, HunyuanVideo.
- Policies: [GR00T N1](../entities/nvidia-groot.md) (largest gains), [π0](../entities/pi-zero.md), [Diffusion Policy](../entities/diffusion-policy.md).
- Robots: [Fourier GR-1](../entities/fourier-gr-1.md), [Franka Panda](../entities/franka-panda.md), [SO-ARM101](../entities/so-arm101.md) (SO-100).
- Data: [RoboCasa](../entities/robocasa.md), [DROID](../entities/droid.md), [Open X-Embodiment](../entities/open-x-embodiment.md) (RT-1, Bridge-v2, Language Table), [MimicGen](../entities/mimicgen.md) (DexMG), [AgiBot](../entities/agibot.md), Ego4D. Aux: LAPA, SigLIP-2.

## Concepts touched
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — video world models used as **synthetic data generators** rather than real-time planners; "neural trajectories" is the key term.
- [Scaling laws — VLAs and human data](../concepts/learning/scaling-laws-vla.md) — video generation as a new data-scaling axis beyond manual teleop; log-linear scaling to 240K trajectories.
- [Imitation learning](../concepts/learning/imitation-learning.md) — pseudo-action-labeled synthetic demos; IDM + latent-action (LAPA) labeling.
- [VLA models](../concepts/learning/vla-models.md), [Flow matching](../concepts/learning/flow-matching.md) (IDM objective).

## Open questions
> [!note] Dream* line attribution
> This v2 (June 2025) references **[GR00T N1](groot-n1-paper.md) only** — it does **not** mention N1.5, "DreamZero", or "DreamDojo". The "DreamGen → DreamZero → DreamDojo" triplet framing comes from the [GEAR publications](nvidia-gear-publications.md) page, not this paper. DreamGen and [GR00T N1.5](groot-n1_5.md) are contemporaneous (both mid-June 2025); N1.5's use of "DreamGen neural trajectories" is stated on the N1.5 page.

- High compute: 240K trajectories = 54 h on 1,500 L40 GPUs; cost reduction is open.
- Relies on **manually provided initial frames**; automating them (img2img inpainting) is future work.
- Zero-shot generalization with **zero ground-truth data for a new embodiment** remains open (paper's own footnote).
- Most neural-trajectory quality loss comes from the **video model**, not the IDM (App. A) — better instruction/physics following would lift downstream results.
- [DreamZero / DreamDojo](dreamdojo-paper.md) — the later Dream* entries; [DreamDojo](dreamdojo-paper.md) is filed, DreamZero is not.
