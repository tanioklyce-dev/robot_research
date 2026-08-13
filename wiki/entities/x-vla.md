---
title: X-VLA
type: entity
subtype: model
created: 2026-08-13
updated: 2026-08-13
sources: 3
tags: [xvla, vla, soft-prompt, cross-embodiment, flow-matching, florence-2, lerobot, air-tsinghua, shanghai-ai-lab, cloth-folding]
---

**X-VLA** — a 0.9 B-parameter cross-embodiment [VLA](../concepts/learning/vla-models.md) from AIR (Tsinghua) + Shanghai AI Lab, built on one idea: **per-data-source learnable embeddings ("[soft prompts](../concepts/learning/soft-prompt-cross-embodiment.md)") absorb embodiment heterogeneity**, letting an otherwise plain stack of self-attention Transformer blocks serve as the whole policy. Primary source: [X-VLA paper](../sources/xvla-paper.md) (arXiv 2510.10274, Oct 2025).

Notable in this wiki for three reasons: it is the **smallest model holding SOTA on the most benchmarks** as of ingest; it is available as a first-class [LeRobot](lerobot.md) policy (`xvla`); and it is the **first named research VLA shipped preinstalled on a consumer robot product** in this wiki's coverage — [Sourccey](sourccey.md) from [Vulcan Robotics](vulcan-robotics.md).

## Architecture

| Component | Choice |
|---|---|
| VLM encoder | [Florence-2](florence-2.md)-Large (main view + language only) |
| Auxiliary views | shared ViT, **bypassing the VLM** |
| Backbone | 24 standard self-attention Transformer encoder blocks, hidden 1024 |
| Action head | [flow matching](../concepts/learning/flow-matching.md), OT/rectified-flow path, `t ~ U(0,1)` |
| Action space | absolute EEF pose: xyz + **Rot6D** + binary gripper (MSE + BCE) |
| Conditioning | soft prompt tokens queried by dataset ID |
| Domain-specific params | **0.04%** of total (prompts + action-token in/out projections) |
| Params | **0.9 B** |

Deliberately *not* used: DiT/AdaLN, cross-attention, mixture-of-experts, autoregressive action tokens. The paper's ablation shows swapping DiT for a plain Transformer encoder cost 2.1 pts of success on its own but enabled the encoding-pipeline and soft-prompt gains worth +26 pts together.

## Training

- **Pretraining** — 290 K episodes / 7 hardware setups / 5 robot types from [AgiBot](agibot.md)-Beta (48.8%), [DROID](droid.md) (31.6% across two camera views), RoboMind (19.9% across Franka / UR-5 / [AgileX](agilex-piper.md) / dual-Franka). 64 × A100, ~4 days, 200 K iters, batch 1024, 224×224 images.
- **Adaptation** — two-step: prompt warm-up with backbone frozen, then joint finetune. Or LoRA at **9 M tunable params (1%)**.
- **Intention abstraction** — predicts **30 anchor points over 4 s** rather than dense timesteps.

## Results

| Benchmark | X-VLA-0.9B | Prior best (params) |
|---|---|---|
| [Simpler](simplerenv.md)-WidowX | **95.8** | 71.9 (MemoryVLA 7B) |
| Simpler VM / VA (Google Robot) | **80.4 / 75.7** | 78.0 / 72.7 |
| [LIBERO](libero.md) avg | **98.1** | 97.1 ([OpenVLA-OFT](openvla-oft.md) 7B) |
| [RoboTwin-2.0](robotwin.md) easy / hard | **70.0 / 39.0** | 46.4 / 16.4 ([π0](pi-zero.md) 3B) |
| VLABench PS | **51.1** | 39.7 ([GR00T-N1](nvidia-groot.md) 3B) |
| NAVSIM PDMS | **87.3** | 81.7 (UniVLA 9B) |
| CALVIN ABC→D | 4.43 | **4.53** (FLOWER 1B) |

Real-world: WidowX/Bridge pick-and-place (beats all baselines on 5/5 tasks); **bimanual [AgileX](agilex-piper.md) cloth folding at ~100% success / 33 folds per hour** from 1,200 curated demonstrations (the **Soft-Fold** dataset, release promised); AIRBOT LoRA adaptation from 200 demonstrations on an embodiment unseen in pretraining.

Under LoRA (9 M params) it reaches 93% LIBERO / 54% Simpler-WidowX — within ~1.5 pts of fully-finetuned π0 at **300× fewer tuned parameters**.

## In LeRobot

X-VLA is upstreamed into [LeRobot](lerobot.md) as the `xvla` policy (`src/lerobot/policies/xvla/`), shipping `modeling_xvla.py`, `soft_transformer.py`, `processor_xvla.py`, and a vendored `modeling_florence2.py` — confirmed present in both `huggingface/lerobot` and Vulcan's `lerobot-vulcan` fork (verified 2026-08-13). This is how it reaches [Sourccey](sourccey.md).

## Deployment on Sourccey

[Vulcan Robotics](vulcan-robotics.md) lists **"XVLA with 4 micromodels: folding T-shirts, shorts, jeans/pants, and long shirts"** as [Sourccey](sourccey.md)'s starting AI ([Vulcan site](../sources/vulcan-robotics-sourccey-site.md)). The choice is legible — X-VLA's flagship real-world demo *is* cloth folding — but the transfer is unproven:

> [!warning] Two open mismatches between X-VLA's pretraining and Sourccey's embodiment
> **1. Kinematic deficiency.** Every X-VLA pretraining embodiment has ≥6 DOF (Franka 7, UR5 6, AgileX 6, AGIBOT 7) and the aligned action space is full SE(3) EEF pose. Sourccey's arms are **5 DOF + gripper** — they cannot realize arbitrary orientations, so their reachable poses form a lower-dimensional manifold inside the pretrained action space. Soft prompts are exactly the mechanism that *should* absorb this, and no published result tests it.
> **2. Where inference runs.** 0.9 B params + Florence-2-Large will not run at control rate on Sourccey's [Raspberry Pi 5](raspberry-pi-5.md). Vulcan's own spec page concedes the point obliquely — "capabilities scale with the host computer. Rented compute is planned" — so the deployment model is the same off-board-inference arrangement as [XLeRobot](xlerobot.md), not onboard autonomy. The paper gives no inference latency figures at all.

## Related

- [Soft-prompt cross-embodiment conditioning](../concepts/learning/soft-prompt-cross-embodiment.md) — the mechanism
- [π0](pi-zero.md) — the model X-VLA benchmarks against most directly
- [SmolVLA](smolvla.md) — the other "small model beats large model" result in this wiki; SmolVLA wins on *data efficiency*, X-VLA on *heterogeneity handling*
- [Florence-2](florence-2.md) — the VLM backbone
- [Sourccey](sourccey.md), [Vulcan Robotics](vulcan-robotics.md) — first product deployment

## Mentioned in

- [X-VLA paper](../sources/xvla-paper.md)
- [Vulcan Robotics / Sourccey site](../sources/vulcan-robotics-sourccey-site.md)
- [Sourccey vs XLeRobot](../syntheses/platforms/sourccey-vs-xlerobot.md)
