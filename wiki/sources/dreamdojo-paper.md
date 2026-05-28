---
title: DreamDojo — A Generalist Robot World Model from Large-Scale Human Videos
type: source
url: https://arxiv.org/abs/2602.06949
arxiv_id: 2602.06949v1
local_path: raw/2602.06949v1.pdf
project_page: https://dreamdojo-world.github.io/
doi: https://doi.org/10.48550/arXiv.2602.06949
license: CC BY 4.0
author: Shenyuan Gao, William Liang, Kaiyuan Zheng, Ayaan Malik, Seonghyeon Ye, Sihyun Yu, Wei-Cheng Tseng, Yuzhu Dong, Kaichun Mo, Chen-Hsuan Lin, Qianli Ma, Seungjun Nah, Loic Magne, Jiannan Xiang, Yuqi Xie, Ruijie Zheng, Dantong Niu, You Liang Tan, K. R. Zentner, George Kurian, Suneel Indupuru, Pooya Jannaty, Jinwei Gu, Jun Zhang, Jitendra Malik, Pieter Abbeel, Ming-Yu Liu, Yuke Zhu, Joel Jang, Linxi (Jim) Fan
affiliations: NVIDIA; HKUST; UC Berkeley; UW; Stanford; KAIST; UofT; UCSD; UT Austin
venue: ICML 2026 (Spotlight)
published: 2026-02-06 (arXiv v1; cover date 2026-02-09)
ingested: 2026-05-15
tags: [dreamdojo, nvidia-gear, world-model, generative-video, cosmos, latent-action, self-forcing, distillation, human-video-pretraining, fourier-gr1, agibot, unitree-g1, yam, foundation-model]
---

> [!note] Project leads + co-firsts
> Three project leads (‡): **Yuke Zhu, Joel Jang, Linxi "Jim" Fan**. Two co-first authors (†): **Shenyuan Gao** (HKUST) and **William Liang** (UC Berkeley). 28 total authors across 9 institutions. Notable academic co-authors: **Pieter Abbeel** (Berkeley) and **Jitendra Malik** (Berkeley); senior NVIDIA generative-AI scientist **Ming-Yu Liu** is also on the list.

## Summary

**DreamDojo** is NVIDIA GEAR's foundation **generative-video world model** for robotics — a video diffusion model that predicts future RGB frames conditioned on robot actions, pretrained on **44,711 hours of egocentric human video** (the **largest video dataset for world model training to date**, 15× the longest prior corpus and 2,000× the most scene-diverse). The model is the latest, most ambitious data point on the *generative-video* side of the world-model paradigm split — the direct counterpoint to FAIR's JEPA program ([LeWorldModel](../entities/leworldmodel.md), [DINO-WM](../entities/dino-wm.md), [V-JEPA 2](../entities/v-jepa-2.md)) — and the destination paper of NVIDIA's **Dream*** triplet (**DreamGen → DreamZero → DreamDojo**).

Two technical ideas carry the paper:

1. **Continuous latent actions as unified proxy labels.** Most internet human video is unlabeled. DreamDojo trains a VAE with an information bottleneck on consecutive frame pairs `(f_t, f_{t+1})` to extract a continuous low-dim embedding that captures the *action* between frames — self-supervised, cross-embodiment. Used as the action condition during world-model pretraining; the model is post-trained on real robot action spaces afterward.
2. **Self-Forcing distillation** from a bidirectional, 35-step diffusion teacher to a causal, **4-step autoregressive student**, hitting **10.81 FPS at 640×480** for arbitrary-horizon real-time interaction. This is what makes live teleoperation, online model-based planning, and large-scale policy evaluation tractable.

Built on **[NVIDIA Cosmos-Predict2.5](../entities/nvidia-cosmos.md)** (latent video diffusion w/ DiT + WAN2.2 tokenizer + [flow-matching](../concepts/learning/flow-matching.md)). Two variants: **2B** and **14B** parameters. Pretrained 140k steps on **256 NVIDIA H100 GPUs**.

## Key claims

### Dataset — DreamDojo-HV (the headline data scale)
- **44,711 hours total** across three sources: **In-lab** (55 hr, in-house Manus + Vive precise hand-pose collection), **[EgoDex](../entities/egodex.md)** (829 hr, Apple Vision Pro), **DreamDojo-HV** (43,827 hr, in-house crowdsourced).
- **9,869 scenes, 6,015 tasks, 43,237 objects** in the in-house corpus.
- Comparison table (Table 1 in the paper) vs prior WM datasets:

| Dataset | Type | # Hours | # Trajectories | # Skills | # Scenes |
|---|---|---:|---:|---:|---:|
| Language-Table | Robot | 2,700 | 442k | — | — |
| RT-1 | Robot | 900 | 130k | 8 | 2 |
| AgiBot-World | Robot | 2,900 | 1,000k | 87 | 106 |
| DROID | Robot | 350 | 76k | 86 | 564 |
| EgoDex | Human | 829 | 30k | 194 | 5 |
| Nymeria | Human | 300 | 1.2k | — | 50 |
| **DreamDojo-HV** | Human | **43,827** | 1,135k | **6,015†** | **1,135k** |
| **Total mixture** | Human | **44,711** | 1,179k | ≥6,015† | ≥1,135k |

(† Estimated by GPT from per-clip language annotations.)

Per the paper, this is **15× longer**, **96× more skills**, and **2,000× more scenes** than the previously largest WM-pretraining dataset.

> [!note] DreamDojo-HV vs EgoScale's corpus
> The 6,015-task / 43,237-object / 9,869-scene figures match **exactly** the in-the-wild portion of [EgoScale](egoscale-paper.md)'s 20,854-hour pretraining corpus. DreamDojo-HV is *more than twice the size* (43,827 hr vs ~20k hr in-the-wild) and uses the same task/scene/object metadata. The two GEAR papers (Feb 2026) appear to share a data collection pipeline and grow it from EgoScale's 20K-hr regime to DreamDojo-HV's 43.8K-hr regime — EgoScale is the VLA scaling-law analysis on the smaller cut; DreamDojo is the world-model training on the larger cut.

### Architecture
- **Backbone**: [Cosmos-Predict2.5](../entities/nvidia-cosmos.md). Latent video diffusion model operating in WAN2.2 tokenizer's continuous latent space (4× temporal compression). DiT blocks with cross-attention for text and adaptive-layer-norm modulation for timestep.
- **Action conditioning** (two architectural deltas from base Cosmos-Predict2.5):
  1. **Relative actions** — rebaseline robot joint poses to the start of each latent frame (every 4 timesteps). Concentrates action distribution into a narrower shared space → better generalization.
  2. **Chunked, per-latent-frame action injection** — instead of conditioning every latent frame on the full action sequence (which would break causality), inject only the **4 consecutive actions** corresponding to that latent frame. Added to timestep embedding inside each DiT block's adaptive-layer-norm. Ablations (Table 5) show ~+1 PSNR from these two changes alone.
- **Variants**: 2B and 14B parameter models, both pretrained 140k steps with effective batch 1024 on **256 NVIDIA H100 GPUs**.

### Continuous latent action model
- 700M-parameter **spatiotemporal Transformer** (24 encoder blocks + 24 decoder blocks) trained as a VAE.
- Encoder: takes `(f_t, f_{t+1})`, projects spatiotemporal features to a **32-dim latent**.
- Decoder: receives the latent + `f_t`, predicts `f_{t+1}`.
- Loss: reconstruction + KL with `β = 10⁻⁶`. Information-bottleneck design forces the latent to capture only what's needed to explain motion between frames.
- Trained for 400k steps with batch 256 on a mixture of three human datasets + four in-house robot datasets (Unitree G1, **Fourier GR-1**, AgiBot, YAM).
- Empirical finding: latent actions retrieved across embodiments correspond to *semantically similar motions* (Fig. 3) — i.e., the latent action space generalizes across human/robot embodiments without supervision.

### Three-stage training pipeline
1. **Pretrain** on human-video mixture (In-lab : EgoDex : DreamDojo-HV = 1 : 2 : 10 sampling), conditioned on continuous latent actions. 140k steps.
2. **Post-train** on target robot data — reinitialize the action MLP's first layer to match the robot's action dimension; fully fine-tune all pretrained weights. Works at small scale because pretraining already covers the physics.
3. **Distill** to real-time autoregressive student via Self-Forcing — warmup stage (regress to teacher ODE solutions) + distillation stage (distribution matching with student's own previous outputs, simulating long rollouts).

### New training loss — temporal consistency
- Standard Cosmos-Predict2.5 uses flow-matching loss (Eq. 2).
- DreamDojo adds a **temporal-consistency loss** (Eq. 4) that supervises the *velocity differences* between consecutive frames in the predicted vs ground-truth video latent:
  ```
  L_temporal = E[ Σ ‖(z_{i+1} − z_i) − (v_{i+1} − v_i)‖² ]
  ```
- Combined: `L_final = L_flow + λ · L_temporal` with **λ = 0.1**.
- Empirically improves both controllability and object completeness; reduces artifacts.

### Distillation (Self-Forcing)
- **Teacher**: bidirectional attention, 35 denoising steps, **2.72 FPS**, 12-frame prediction horizon.
- **Student**: causal attention (sliding window 12), 4 denoising steps, **10.81 FPS**, 4-frame prediction at a time + 12-frame context.
- Two-stage process:
  - **Warmup**: regress student to teacher ODE solutions (10k ODE trajectories, 10k iters, batch 256).
  - **Distillation**: KL-based distribution matching with student generating from its own previous outputs. Student generates 13–49 frames, loss computed on last 13. 3k iters, batch 64.
- Run on **64 NVIDIA H100 GPUs**.
- Result (Table 6): ~4× speedup, minor quality drop, real-time autoregressive interaction "for more than 1 minute without degradation."

### Results

**Effects of action conditioning** (Table 2, simulation quality on held-out evals):

| Method | In-lab PSNR | EgoDex PSNR |
|---|---:|---:|
| w/o pretrain | 20.576 | 19.952 |
| action-free pretrain | 20.797 | 19.924 |
| **latent action** (default) | **20.913** | **20.344** |
| Retargeted GT action (In-lab) / MANO (EgoDex) — *ideal* | 20.960 | 20.474 |

Latent action conditioning **matches** the ideal ground-truth-action setting *despite* needing no action-capture hardware. This is the load-bearing empirical result for the latent-action thesis.

**Effects of data mixture** (Table 3 — PSNR rises monotonically with more human data; **DreamDojo-14B wins across all four OOD evals**):

| Pretraining | In-lab PSNR | EgoDex PSNR | DreamDojo-HV PSNR | Counterfactual PSNR |
|---|---:|---:|---:|---:|
| Cosmos-Predict2.5 (baseline, no human pretrain) | 20.576 | 19.952 | 18.274 | 20.472 |
| + In-lab | 20.913 | 20.267 | 18.621 | 20.755 |
| + EgoDex | 20.972 | 20.334 | 18.706 | 20.797 |
| + DreamDojo-HV | 21.016 | 20.414 | 18.724 | 20.852 |
| **DreamDojo-2B** | 21.114 | 20.411 | 18.813 | 20.907 |
| **DreamDojo-14B** | **21.413** | **20.525** | **18.924** | **21.087** |

**Human preference** (Table 4 — 12 volunteers, 50 OOD samples):

| Comparison | Physics correctness | Action following |
|---|---:|---:|
| DreamDojo-2B > Cosmos-Predict2.5 | 62.50% | 63.45% |
| DreamDojo-14B > Cosmos-Predict2.5 | **73.50%** | **72.55%** |
| DreamDojo-14B > DreamDojo-2B | 72.50% | 65.53% |

**Distillation** (Table 6): student hits 10.81 FPS vs teacher 2.72 FPS, predict-length 4 vs 12, context-length 12 vs 1 (causal attention enables much longer context).

### Downstream applications demonstrated
- **Policy evaluation** (§4.7): post-trained DreamDojo-2B on AgiBot fruit-packing dataset; evaluates checkpoints of a single-view state-free [GR00T N1.5](../entities/nvidia-groot.md) variant by simulating closed-loop rollouts. Cheaper and faster than real-robot eval.
- **Live teleoperation**: human operator drives the robot's predicted future in real time at 10.81 FPS.
- **Online model-based planning**: planner samples action sequences, rolls out in the world model, picks the best.

### Embodiments tested
- **Fourier GR-1** humanoid — primary eval target for In-lab, EgoDex, DreamDojo-HV, and Counterfactual evals.
- **Unitree G1** humanoid — in-house robot dataset for latent-action training.
- **AgiBot** robot — fruit-packing policy-eval demo + latent-action training.
- **YAM** — in-house robot used in latent-action training.

## Position in the wiki

### The Dream* triplet, completed
NVIDIA GEAR's WM line is the **DreamGen → DreamZero → DreamDojo** triplet — flagged in the [NVIDIA GEAR Lab Publications](nvidia-gear-publications.md) page as the wiki's top WM-side follow-up cluster. DreamDojo is the third and most ambitious. With this ingest, the most-flagged generative-video-WM gap in the wiki is closed.

### Generative-video vs JEPA — DreamDojo is the new high-water mark on the pixel side
The wiki's [generative-video vs JEPA world models](../syntheses/world-models/generative-video-vs-jepa-world-models.md) synthesis now has its largest, most ambitious generative-video data point. Where V-JEPA 2 (1B params, 1M+ hr internet video) had been the largest scale on either side, DreamDojo-14B (14B params, 44.7K hr human video) clearly tops it in compute *and* publishes head-to-head OOD wins vs Cosmos-Predict2.5. The synthesis page needs an update.

### Two parallel data-vs-method bets within NVIDIA GEAR
- **[EgoScale](egoscale-paper.md)** (the *VLA* side): scaling law for action-policy pretraining on 20K hr human video. Output = a VLA.
- **DreamDojo** (the *world-model* side): scaling for video-prediction pretraining on 44K hr human video. Output = a world model.
- Both papers (Feb 2026, NVIDIA GEAR) share project leads ([Yuke Zhu](../entities/yuke-zhu.md), [Jim Fan](../entities/jim-fan.md)) and a near-identical data collection pipeline. They are the two halves of NVIDIA's "what to do with massive human video" thesis.

### The Cosmos-Predict family
The wiki's [NVIDIA Cosmos](../entities/nvidia-cosmos.md) entity already noted **Cosmos-Predict2.5** as a family member. DreamDojo is now the canonical *robot-specific* downstream of Cosmos-Predict2.5 — the architectural cousin of [Genie Envisioner](../entities/genie-envisioner.md) (which is AGIBOT's robot-specific downstream of Cosmos-Predict2.5 / its own VLM).

### Continuous latent actions — a new pattern worth tracking
Not yet a wiki concept page. Appears in:
- Genie (Bruce et al. 2024) — the original latent-action VAE.
- LAPA / Gao et al. 2025 — extends to continuous latent actions.
- DreamDojo (this paper) — adapts the pattern for cross-embodiment WM pretraining.

If V-JEPA-2-AC, π0, or any of the other VLAs adopt this idea, a `concepts/latent-action-models.md` page would be warranted.

## Entities mentioned

**Already in wiki:**
- [NVIDIA GEAR](../entities/nvidia-gear.md) — origin lab.
- [Jim Fan (Linxi Fan)](../entities/jim-fan.md), [Yuke Zhu](../entities/yuke-zhu.md) — project leads.
- [NVIDIA](../entities/nvidia.md) — parent.
- [NVIDIA Cosmos](../entities/nvidia-cosmos.md) — Cosmos-Predict2.5 is the backbone.
- [NVIDIA GR00T](../entities/nvidia-groot.md) — used in DreamDojo's policy-eval demo (GR00T N1.5 variant).
- [EgoDex](../entities/egodex.md) — one of three pretraining data sources.
- [AGIBOT](../entities/agibot.md) — AgiBot fruit-packing dataset used in §4.7 policy-eval demo.

**New entity stubs created with this ingest:**
- [Joel Jang](../entities/joel-jang.md) — third project lead.
- [Fourier GR-1](../entities/fourier-gr-1.md) — humanoid robot, primary OOD eval target.

**Mentioned but not entitied:**
- **Cosmos-Predict2.5** — covered by [NVIDIA Cosmos](../entities/nvidia-cosmos.md). DreamDojo's update to that entity page captures the connection.
- **WAN2.2 tokenizer** (Wan et al. 2025) — 4× temporally-compressing video tokenizer that defines DreamDojo's latent space. Not yet a wiki entity.
- **Self-Forcing** (Huang et al. 2025) — distillation paradigm. Not in the wiki.
- **YAM** — in-house NVIDIA robot embodiment used in latent-action training. Identity not surfaced in the body.
- **Pieter Abbeel** / **Jitendra Malik** (UC Berkeley) — famous academic co-authors. Not yet entitied; would be substantial stubs.
- **Ming-Yu Liu** (NVIDIA) — senior generative-AI scientist. Not entitied.
- **Shenyuan Gao** (HKUST), **William Liang** (UC Berkeley) — co-first authors. Not entitied.

## Concepts touched
- [World model](../concepts/world-models/world-model.md) — DreamDojo is a generative-video world model.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — DreamDojo as simulator-substitute for policy evaluation.
- [VLA models](../concepts/learning/vla-models.md) — adjacent paradigm; DreamDojo + a VLA = train+eval pair (the GR00T N1.5 + DreamDojo policy-eval demo is the concrete example).
- [Imitation learning](../concepts/learning/imitation-learning.md) — DreamDojo's pretraining objective is structured imitation from human videos.
- [Scaling laws — VLAs and human data](../concepts/learning/scaling-laws-vla.md) — adjacent: DreamDojo doesn't fit a clean scaling law but shows monotone improvement in OOD physics with data scale (Table 3).

## Open questions

- **Quantitative scaling law for WM pretraining**: DreamDojo shows monotone improvement with data, but doesn't fit a closed-form scaling law (vs EgoScale's `L = a − b·ln(D)`). A WM-side scaling-law paper is the obvious follow-up.
- **Real-robot transfer of DreamDojo-trained policies**: the paper demonstrates *policy evaluation* (DreamDojo simulates rollouts of an existing GR00T N1.5 policy), but does *not* publish results for "policy trained inside DreamDojo, deployed on real robot." The V-JEPA-2-AC-style zero-shot real-robot result is the open question for the generative-video paradigm.
- **Head-to-head vs V-JEPA 2 / LeWorldModel**: no source has compared DreamDojo against the JEPA line on the same benchmark. The wiki's [generative-video vs JEPA](../syntheses/world-models/generative-video-vs-jepa-world-models.md) synthesis has been calling out this gap; it remains open.
- **What is YAM?** Latent-action training uses Unitree G1 + Fourier GR-1 + AgiBot + YAM. The first three are identifiable; YAM is not surfaced in the body.
- **Continuous latent actions across the GEAR program**: DreamDojo cites Gao et al. 2025 for the construct. Does EgoScale also use it? (EgoScale uses *retargeted joint-space hand actions*, not latent actions — so DreamDojo and EgoScale use *different* action representations even though they share the data pipeline.)
- **Compute disclosure**: 256 H100s × 140k steps × two model sizes (2B + 14B) is a substantial training run. The paper doesn't report total GPU-hours.
- **License of DreamDojo-HV**: the in-house crowdsourced corpus. Public release? Currently the paper does not commit.
- **Inference cost on real hardware**: 10.81 FPS on an H100 is good for cloud-side inference but not on-robot. What's the model footprint for on-Jetson deployment?

## Why this is a significant ingest

1. **Closes the wiki's top WM-side gap.** DreamGen → DreamZero → DreamDojo was the most-flagged follow-up cluster from the GEAR publications ingest. DreamDojo (the destination paper) is now filed.
2. **Establishes the largest WM-pretraining corpus to date.** 44.7K hr egocentric human video. Reframes the data-availability story for world models — they no longer need teleop data at scale, just human video.
3. **Validates the latent-action proxy at scale.** The Table 2 result (latent action ≈ ideal action conditioning) is the cleanest published evidence that self-supervised pseudo-action labels can substitute for hardware-captured action labels in WM pretraining.
4. **Real-time autoregressive video WMs become deployable.** The Self-Forcing distillation result (35 steps → 4 steps, 2.72 FPS → 10.81 FPS) is a critical engineering milestone — live teleoperation and online MPC over a generative-video WM were impractical at teacher speed.
5. **The wiki's generative-video-vs-JEPA synthesis page needs DreamDojo.** Until now, the largest generative-video data point in that synthesis was Genie Envisioner / GE-Sim2 (Cosmos-Predict2 backbone, parameter count unstated). DreamDojo-14B is 14B params on 44K hr of human video — a clear upper bound.
