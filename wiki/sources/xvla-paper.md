---
title: "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model (Zheng, Li et al., Oct 2025)"
type: source
url: https://arxiv.org/abs/2510.10274
local_path: raw/2510.10274v1-xvla.pdf
author: "Jinliang Zheng*, Jianxiong Li*, Zhihao Wang, Dongxiu Liu, Xirui Kang, Yuchun Feng, Yinan Zheng, Jiayin Zou, Yilun Chen, Jia Zeng, Ya-Qin Zhang, Jiangmiao Pang, Jingjing Liu, Tai Wang†, Xianyuan Zhan†"
affiliations: Institute for AI Industry Research (AIR) Tsinghua University; Shanghai AI Lab; Peking University
published: 2025-10-11
ingested: 2026-08-13
tags: [xvla, vla, vision-language-action, soft-prompt, cross-embodiment, flow-matching, florence-2, peft, lora, cloth-folding, libero, simplerenv, robotwin, calvin, vlabench, navsim, primary-source]
---

## Summary

**X-VLA** is a 0.9 B-parameter generalist [VLA](../concepts/learning/vla-models.md) whose single architectural idea is **[soft prompts](../concepts/learning/soft-prompt-cross-embodiment.md)**: one small set of learnable embeddings *per data source*, injected early into a stack of plain self-attention Transformer blocks, that absorb everything heterogeneous about an embodiment — arm kinematics, camera rig, control frequency, task distribution — rather than only its action space. Everything else in the model is deliberately vanilla: a pretrained [Florence-2](../entities/florence-2.md)-Large vision-language encoder, 24 standard Transformer encoder layers at hidden size 1024, and a [flow-matching](../concepts/learning/flow-matching.md) action objective. No DiT, no AdaLN, no cross-attention, no mixture-of-experts.

The headline is that this beats much larger models on almost everything it is pointed at. **X-VLA-0.9B sets a new SOTA on five of six benchmarks** — Simpler-WidowX 95.8 (prior best 71.9), LIBERO 98.1, RoboTwin-2.0 70.0 easy / 39.0 hard (prior best 46.4 / 16.4), VLABench 51.1, NAVSIM PDMS 87.3 — while being 3–8× smaller than the [π0](../entities/pi-zero.md) / OpenVLA / UniVLA models it displaces. Under LoRA it tunes **9 M parameters (1%)** to reach 93% LIBERO and 54% Simpler-WidowX, matching fully-finetuned π0's 3 B.

For this wiki the paper matters twice over. It is the strongest published argument that **cross-embodiment heterogeneity is a conditioning problem, not an architecture problem** — and it is the model that [Vulcan Robotics](../entities/vulcan-robotics.md) ships as the starting policy on [Sourccey](../entities/sourccey.md), the first consumer product in this wiki to arrive with a named research VLA preinstalled.

## The central argument: four ways to absorb heterogeneity

The paper's §3 is an unusually clean empirical bake-off. Fix the backbone (Florence-Base + DiT-Base), fix the data mixture (290 K episodes, 7 hardware setups), fix the recipe, and vary only how embodiment differences are handled:

| Strategy | Where it acts | Verdict |
|---|---|---|
| **(a) Domain-specific action projection** | output head only | The industry default ([π0](../entities/pi-zero.md), [GR00T N1](groot-n1-paper.md), UniAct, RDT). Acts too late to shape perception or proprioceptive reasoning; ignores camera-rig and task-distribution heterogeneity entirely. |
| **(b) HPT-style projection** | input side, per-domain resamplers | "Frequently alters feature distributions and is prone to corrupting pretrained VLM representations" → unstable training. |
| **(c) Language prompts** | text stream, hand-written | e.g. `"Embodiment: Single Franka, Camera Setup: Left View / Wrist View, Freq: 15Hz"`. Works, but requires handcrafted templates per domain — "greatly hinder adaptability and scalability." |
| **(d) Soft prompts (theirs)** | early, learned, per-source | Randomly initialised, optimised end-to-end. Stable training curves, best asymptotic error. |

> [!note] Why this framing is the contribution
> Nearly every prior cross-embodiment VLA treats "different robot" as "different action dimensionality" and solves it with a per-robot output head. X-VLA's claim is that the action space is the *least* of it: camera placement, control rate, and task distribution shift the representation the model needs at *every* layer, and a head at the end can't fix a backbone that was never told which robot it was looking at.

## Architecture

- **Vision-language stream** — Florence-2-Large encodes the **main (fixed) view + language instruction only**. Auxiliary views (wrist cameras) go through a **shared ViT, bypassing the VLM**, "as current VLMs have limited multi-view perception." A deliberate disentangling: fixed views carry stable task context, wrist views carry fast noisy contact cues.
- **Proprioceptive-action stream** — joint/EEF state `R_t`, noisy action chunk `A_t`, and flow time `t` are concatenated and projected by one lightweight linear layer, fusing *early* with the multimodal tokens rather than late.
- **Backbone** — 24 standard self-attention Transformer encoder blocks, hidden 1024, fully bidirectional. Soft prompts are prepended as extra tokens, queried by dataset ID.
- **Domain-specific parameters total 0.04% of the model** — the soft prompts plus the input/output linear projections for action tokens. Everything else is shared.

## Training recipe (the part that actually carries the numbers)

The ablation path in Tab. 1 is worth reading as a list of things that matter more than the idea:

| Change | Val error ↓ | Simpler-WidowX ↑ |
|---|---|---|
| Baseline (Florence-base + DiT-base, no pretrain) | — | 4.1 |
| + custom LR (no pretrain) | — | **39.6** (+35.5) |
| + heterogeneous pretraining (naive) | 0.11 | 25.0 (**−14.6**) |
| + action alignment / intention abstraction / balanced sampling | 0.077 | 50.0 (+25.0) |
| + Transformer encoder instead of DiT | 0.071 | 47.9 (−2.1) |
| + disentangled encoding pipeline | 0.053 | 64.6 (+16.7) |
| + **soft prompt** | 0.041 | 73.8 (+9.2) |
| + scaling up | 0.032 | 89.6 (+15.8) |
| + two-step adaptation | 0.032 | **95.8** (+6.2) |

> [!warning] Naive cross-embodiment pretraining made the model *worse*
> Adding 290 K episodes of mixed-robot data to the baseline **dropped** Simpler-WidowX from 39.6 to 25.0. Every point of the eventual 95.8 comes from the machinery that makes heterogeneous data usable — data alignment, encoding, prompts — not from the data itself. This is a direct counterweight to "just add more robot data."

Key recipe components:

- **Custom (reduced) learning rate** on soft prompts and the vision-language modules, to avoid catastrophic drift from pretrained representations — the same instinct as [knowledge insulation](../concepts/learning/knowledge-insulation.md) in the π-line, reached by a cruder route.
- **Aligned action representation** — all embodiments mapped to absolute EEF pose: Cartesian xyz + **Rot6D** rotation (avoiding Euler/quaternion discontinuities) + binary gripper. MSE on pose, BCE on gripper.
- **Intention abstraction by temporal downsampling** — rather than predicting every timestep, predict **30 anchor points spanning the next 4 seconds**. Raw low-level trajectories are "too fine-grained and contain lots of noisy movements due to human randomness."
- **Balanced sampling** — shuffle across domains *and* across trajectories within domains, not round-robin.
- **Two-step adaptation** to a new embodiment: (1) **prompt warm-up** with the backbone frozen, so the new prompt lands in the pretrained feature geometry; (2) **joint finetune** of backbone + prompt.

## Pretraining data

290 K episodes, 7 hardware setups, 5 robot types, drawn from three public corpora:

| Source | Embodiment | Share | Freq | Cameras |
|---|---|---|---|---|
| AgiBot-Beta ([AgiBot World](../entities/agibot.md)) | AGIBOT | 48.8% | 30 Hz | head + wrist |
| [DROID](../entities/droid.md) | [Franka](../entities/franka-panda.md) (left view) | 15.8% | 15 Hz | left + wrist |
| DROID | Franka (right view) | 15.8% | 15 Hz | right + wrist |
| RoboMind | Franka | 6.7% | 30 Hz | top |
| RoboMind | UR-5 | 8.7% | 30 Hz | top |
| RoboMind | [AgileX](../entities/agilex-piper.md) | 3.7% | 30 Hz | front + wrist |
| RoboMind | Dual-Franka | 0.8% | 30 Hz | front + wrist |

Compute: **64 × A100 for ~4 days**, global batch 1024, 200 K iterations, AdamW, lr 1e-4, bf16, images at 224×224.

## Results

### Simulation (Tab. 2 — X-VLA vs the aggregated best of 20 prior models)

| Benchmark | Prior best (any model) | X-VLA-0.9B |
|---|---|---|
| Simpler Visual Matching (Google Robot) | 78.0 | **80.4** |
| Simpler Visual Aggregation | 72.7 | **75.7** |
| **[Simpler](../entities/simplerenv.md)-WidowX** | 71.9 (MemoryVLA 7B) | **95.8** |
| **[LIBERO](../entities/libero.md)** avg | 97.1 (OpenVLA-OFT 7B) | **98.1** |
| CALVIN ABC→D | 4.53 (FLOWER 1B) | 4.43 |
| **[RoboTwin-2.0](../entities/robotwin.md)** easy / hard | 46.4 / 16.4 (π0 3B) | **70.0 / 39.0** |
| VLABench PS | 39.7 (GR00T-N1 3B) | **51.1** |
| NAVSIM PDMS | 81.7 (UniVLA 9B) | **87.3** |

CALVIN is the one loss, and narrowly. RoboTwin-2.0 hard is the widest margin — **2.4×** the previous best — which is the bimanual, domain-randomized setting.

> [!note] A VLA that also drives a car
> NAVSIM is a closed-loop autonomous-driving benchmark. X-VLA beats Transfuser and UniAD, both purpose-built AV planners, on the aggregate PDM score (87.3 vs 84.0 / 83.4), driven almost entirely by drivable-area compliance (96.5 vs 92.8) and time-to-collision (82.2 vs 79.2). The wiki has no other example of one manipulation policy architecture transferring to driving without modification.

### Real-world (3 embodiments)

- **WidowX / BridgeData-v2** — pick-and-place across four generalization axes (visual, motion, physical, semantic), 10 trials per task; beats all baselines on all five tasks.
- **AgileX bimanual — dexterous cloth folding.** New dataset **Soft-Fold**, 1,200 trajectories, to be released. **~100% success at 33 folds/hour** (≈1.8 min/fold), "comparable to the closed-source π0-folding model, presumably trained on substantially larger and higher-quality datasets." Finetuned π0-base and from-scratch [ACT](../entities/act.md) both failed to match throughput.
- **AIRBOT — PEFT on an unseen embodiment.** 200 demonstrations, cloth-picking, LoRA only.

### How Soft-Fold was collected (Appendix F) — the underrated part

Cloth folding is a multi-modal-demonstration problem: humans fold "in a wide variety of methods in a seemingly random manner," and different strategies are different behavioral modes. The team's answer:

1. **Split the task in two** — (I) smooth the cloth from a disordered state, (II) fold the smoothed cloth. Stage I is the hard one; disordered cloth has "highly random dynamics."
2. **Collect stage I repetitively** until keypoints (two corners, two ends) emerge, then use a **swinging motion** to finish smoothing and hand off to stage II. "Unstructured or randomly collected demonstrations in stage I can entangle policies in inconsistent behaviors."
3. **DAgger-style iteration** — retrain [ACT](../entities/act.md) every 100 episodes, find its failure modes, collect targeted demonstrations against them.

Rate: ~1.5 min/episode, **20–25 episodes per hour** including resets and discards. 1,200 episodes ≈ 50–60 operator-hours.

## Interpretability of the prompts

t-SNE of the seven learned prompts (Fig. 8) clusters by hardware configuration — but **the two DROID-Franka prompts (left-view and right-view) intermingle rather than separate**, because they differ only in which camera is designated main. The prompts are not brute-force dataset IDs; they encode configuration similarity.

The transfer experiment (Fig. 9) follows: adapting to WidowX (unseen), a **frozen pretrained UR5 prompt** beats a random prompt early — partial kinematic similarity transfers — but plateaus below the two-step-adapted prompt. The authors flag the obvious next step: with enough pretraining platforms, **retrieve the nearest prompt for zero/few-shot embodiment transfer**.

## Key claims

- Heterogeneity in cross-embodiment data is not only action-space heterogeneity; camera setup, control frequency, and task distribution matter and are unaddressed by per-embodiment action heads (§3).
- Soft prompts totalling 0.04% of parameters outperform HPT-style input projection and hand-written language prompts, with more stable training dynamics (§3, Fig. 4).
- Naive heterogeneous pretraining *degrades* downstream success; the data-processing recipe is load-bearing (Tab. 1).
- Scaling holds along **three axes simultaneously** — model size, data diversity, data volume — with **no sign of saturation at 0.9 B / 290 K episodes / 7 sources**; validation ℓ1 error correlates R² = −0.925 with adaptation success (Fig. 5).
- Validation prediction error is a usable **proxy for downstream adaptation success**, which lets the scaling study avoid running full rollouts (Tab. 1).
- 1% LoRA adaptation ≈ full π0 finetuning on LIBERO (95.4/96.6/96.0/84.2 vs 96.8/98.8/95.8/85.2) and Simpler-WidowX (54.2 vs 55.7) (Tab. 3).
- 1,200 well-curated cloth-folding demonstrations suffice to match a closed-source model presumed to be trained on far more (§5.2, App. F).

## Limitations (Appendix N, the authors' own)

- 0.9 B is "modest," constrained by compute and by the scarcity of high-quality robotics data — the interaction between embodiment variability and model capacity is an open scaling question.
- **Low-dimensional action labels are information-poor supervision.** Temporal downsampling is a heuristic that abstracts intention without enriching it. Wanted: 3D spatial cues, physical dynamics, subgoal annotations, self-supervised objectives on raw streams.
- **Deployment still requires embodiment-specific adaptation** — a handful of demonstrations and a finetune. Not plug-and-play. Proposed direction: explicit embodiment-agnostic abstractions (universal kinematic descriptors, physics-informed priors).

## Entities mentioned

- [X-VLA](../entities/x-vla.md) · [Florence-2](../entities/florence-2.md) · [π0](../entities/pi-zero.md) · [GR00T N1](../entities/nvidia-groot.md) · [SmolVLA](../entities/smolvla.md) · [OpenVLA](../entities/openvla.md) / [OpenVLA-OFT](../entities/openvla-oft.md) · [ACT](../entities/act.md)
- [LIBERO](../entities/libero.md) · [SimplerEnv](../entities/simplerenv.md) · [RoboTwin 2.0](../entities/robotwin.md)
- [AgiBot](../entities/agibot.md) · [DROID](../entities/droid.md) · [Franka Panda](../entities/franka-panda.md) · [AgileX PiPER](../entities/agilex-piper.md)
- [Vulcan Robotics](../entities/vulcan-robotics.md) / [Sourccey](../entities/sourccey.md) — downstream adopter, not in the paper
- [LeRobot](../entities/lerobot.md) — X-VLA is upstreamed as the `xvla` policy

## Concepts touched

- [Soft-prompt cross-embodiment conditioning](../concepts/learning/soft-prompt-cross-embodiment.md) (new)
- [VLA models](../concepts/learning/vla-models.md) · [Flow matching](../concepts/learning/flow-matching.md) · [Scaling laws — VLAs](../concepts/learning/scaling-laws-vla.md)
- [Imitation learning](../concepts/learning/imitation-learning.md) · [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md)

## Open questions

- **Every pretraining embodiment has ≥6 DOF** (Franka 7, UR5 6, AgileX 6, AGIBOT 7). The aligned action space is full SE(3) EEF pose. What happens when the target embodiment is **kinematically deficient** — a 5-DOF arm that cannot realize arbitrary orientations? Soft prompts are the obvious mechanism to absorb it, and [Sourccey](../entities/sourccey.md) is about to be the field test. Untested in the paper.
- Prompt *retrieval* for zero-shot embodiment transfer is proposed and never run.
- The Soft-Fold DAgger loop uses ACT as the failure-mode detector. Does the loop still work if the detector is the model being trained?
- No wall-clock inference numbers or deployment hardware are given anywhere in the paper. 0.9 B + Florence-2-Large is not an edge-device model; where it actually runs at control rate is unstated.
- CALVIN is the single loss (4.43 vs FLOWER's 4.53) and goes uncommented.
- Soft-Fold release is promised, not yet confirmed.
