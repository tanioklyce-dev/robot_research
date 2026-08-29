---
title: "MotionBricks: Scalable Real-Time Motions with Modular Latent Generative Model and Smart Primitives"
type: source
url: https://arxiv.org/abs/2604.24833
project_page: https://nvlabs.github.io/motionbricks/
author: Tingwu Wang, Olivier Dionne (joint first), Michael De Ruyter, David Minor, Davis Rempe, Kaifeng Zhao, Mathis Petrovich, Ye Yuan, Chenran Li, Zhengyi Luo, Brian Robison, Xavier Blackwell, Bernardo Antoniazzi, Xue Bin Peng, Yuke Zhu, Simon Yuen (NVIDIA + collaborators)
published: 2026-04-27
ingested: 2026-07-15
local_path: raw/2604.24833v1.pdf
sha256: 44c4baabb047642d8968f53205a0d585bb169f5bbb2de6e6539ea0f0f85a40fc
venue: ACM Transactions on Graphics 45(4), SIGGRAPH 2026 (arXiv 2604.24833 v1)
license: CC-BY 4.0
format: pdf (22 pp.)
tags: [motionbricks, nvidia, gear, xue-bin-peng, yuke-zhu, whole-body-control, humanoid, unitree-g1, motion-generation, latent-generative-model, character-animation, real-time, tokenizer, siggraph]
---

# MotionBricks: Scalable Real-Time Motions with Modular Latent Generative Model and Smart Primitives

## Summary

**MotionBricks** is a **large-scale, real-time generative motion framework** from [NVIDIA](../entities/nvidia.md) (the [GEAR](../entities/nvidia-gear.md)/animation orbit; [Xue Bin Peng](../entities/xue-bin-peng.md), [Yuke Zhu](../entities/yuke-zhu.md) senior). It targets the gap between generative-motion *research* and *production*: existing text/tag-driven diffusion or token models degrade in quality/scale under real-time constraints and lack fine-grained multi-modal control. MotionBricks answers with **(1)** a **modular latent generative backbone** — a structured multi-head tokenizer + root/pose modules — that models **>350,000 motion clips in a single model**, and **(2)** **"smart primitives,"** a plug-and-play authoring interface for navigation and object interaction that needs **no fine-tuning or task-specific tags** (zero-shot to new downstream tasks). It hits **15,000 FPS at 2 ms latency**, drives a **production-grade UE5 animation demo**, and — the wiki-relevant part — is **deployed on the [Unitree G1](../entities/unitree-g1.md) humanoid for real-time whole-body robotic control**, positioning one model across *both* character animation and robotics. Published at **SIGGRAPH 2026 (ACM TOG 45(4))**; CC-BY 4.0; code/data/videos on the project page. **Code** ships as the `motionbricks/` dir of [`NVlabs/GR00T-WholeBodyControl`](gr00t-wholebodycontrol-github.md) — a preview release with a keyboard-driven interactive G1 demo (VQVAE tokenizer + pose + root models, ~2.2 GB checkpoints); the 350k-clip production dataset is the **BONES** corpus (`bones.studio/datasets`), the same lineage as SONIC's BONES-SEED.

## Key claims

**Two challenges it targets (bridging research → production)**
1. **Real-time scalability** — industry needs a vast motion repertoire generated in real time; generative methods degrade under real-time compute.
2. **Integration** — industry needs fine-grained multi-modal control (velocity commands, style selection, precise keyframes) plus a *systematic design interface* — largely unmet by text/tag-driven models.

**Architecture — 4-stage inference pipeline (Fig. 2, Alg. 1)**
- **Stage 0 — Smart primitives**: `Smart Locomotion` + `Smart Object` modules turn user commands / game events into **keyframe constraints** `T` (walk/crouch/crawl/run; pick-up/vault/parkour/door-open). Navigation needs only 1–2 keyframes; object interaction needs denser hand-position specs.
- **Stage 1 — Root module** `F`: predicts frame count `T` and root trajectory `{r}`.
- **Stage 2 — Pose module** `P`: models the distribution of **multi-head latent pose tokens** `{z_q}` conditioned on root + constraints.
- **Stage 3 — Token decoder**: produces continuous motion `{r,p,q,v,c}`.
- **Structured multi-head tokenizer** is the cornerstone: **root–pose disentanglement** + a flexible conditioning mechanism. **Any subset of constraints** is accepted — missing constraints are replaced by a **learnable mask embedding** (consistent masking across root/pose/decoder). In-betweening segments **12–64 frames @ 30 FPS**.

**Results**
- **SOTA motion quality** on open-source *and* proprietary datasets of varied scale.
- **15,000 FPS throughput, 2 ms latency** — real-time by a wide margin.
- **Zero-shot** to new downstream tasks (no fine-tuning / tagging); "assemble applications like bricks" without expert animation knowledge.
- **UE5 production demo** across locomotion styles, acrobatics, and object–scene interaction with one unified model.
- **Unitree G1 deployment** — same backbone for real-world humanoid whole-body control (animation → robotics transfer).

**Relation to [SONIC](sonic-paper.md)** (explicit, §2): MotionBricks notes SONIC "adopts a similar token-based latent generation approach for humanoid robot control, though with a different tokenizer and network architecture, and is **limited to locomotion without support for object interaction**." MotionBricks' smart primitives add the object-interaction axis SONIC lacks — the two are sibling GEAR-orbit token-latent motion models.

## Entities mentioned

- [NVIDIA](../entities/nvidia.md) / [NVIDIA GEAR](../entities/nvidia-gear.md) — authoring lab orbit; listed on the [GEAR publications page](nvidia-gear-publications.md).
- [Xue Bin Peng](../entities/xue-bin-peng.md), [Yuke Zhu](../entities/yuke-zhu.md) — senior authors.
- [Unitree G1](../entities/unitree-g1.md) — the deployed humanoid.

## Concepts touched

- [Whole-body control](../concepts/robotics/whole-body-control.md) — the robotics half of the system.
- **Latent generative motion models / vector-quantized tokenizers** — a discrete-token motion cousin of [VQ-BeT](../entities/vq-bet.md) and of [SONIC](sonic-paper.md)'s FSQ token space.
- [Generative modeling](../syntheses/curriculum/curriculum-05-generative-models.md) — the diffusion/token family MotionBricks argues it outperforms on the quality-vs-speed trade-off.

## Open questions

- **How deep is the robot transfer?** The G1 deployment is a demonstration; no head-to-head WBC benchmark (SR/MPJPE) against [SONIC](sonic-paper.md) or [BumbleBee](bumblebee-experts-to-generalist-wbc.md) is given — animation is the paper's primary evaluation axis.
- **Data provenance** — the >350k-clip corpus mixes open-source + proprietary; licensing of the proprietary half unstated.
