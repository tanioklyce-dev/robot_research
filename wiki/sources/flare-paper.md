---
title: FLARE — Robot Learning with Implicit World Modeling (paper)
type: source
url: https://arxiv.org/abs/2505.15659
project_page: https://research.nvidia.com/labs/gear/flare
author: Ruijie Zheng, Jing Wang, Scott Reed (co-first), … Jan Kautz, Furong Huang, Yuke Zhu, Jim Fan (NVIDIA GEAR + UMD + NTU + UT Austin)
published: 2025-05-21 (arXiv 2505.15659v1)
ingested: 2026-07-04
local_path: raw/FLARE_2505.15659v1.pdf
format: pdf (14 pp.)
tags: [flare, implicit-world-model, latent-alignment, jepa-adjacent, nvidia, gear, vla, flow-matching, auxiliary-loss, human-video]
---

## Summary

Primary source for **[FLARE](../concepts/world-models/flare.md)** (**F**uture **LA**tent **RE**presentation Alignment) — NVIDIA GEAR's method for adding **implicit latent world modeling to a flow-matching robot policy through a lightweight auxiliary loss** rather than pixel-level future prediction. It augments a [GR00T N1](groot-n1-paper.md)-style DiT policy with a few learnable "future tokens"; at an intermediate DiT layer, their projected activations are aligned (cosine similarity) to the embedding of a *future* observation. This forces the policy to implicitly anticipate future states while predicting actions, requires minimal architectural change, beats prior baselines by **up to 26%**, and — crucially — lets **action-less human egocentric video** contribute to manipulation learning. **This is the auxiliary loss that [GR00T N1.5](groot-n1_5.md) adopts at coefficient λ=0.2.** Co-first authors Ruijie Zheng, Jing Wang, Scott Reed; advised by [Yuke Zhu](../entities/yuke-zhu.md) + [Jim Fan](../entities/jim-fan.md).

## Key claims

### The FLARE objective (§3)
- Base objective is **flow matching** (following [π0](../entities/pi-zero.md) / [GR00T N1](../entities/nvidia-groot.md)): `L_fm` predicts the denoising direction of a noised action chunk; DiT backbone with alternating cross-attention (to VL embedding) + self-attention; K=4 Euler steps at inference.
- **FLARE mechanism**: add **M learnable future-token embeddings** to the input sequence (alongside proprioceptive state + noised action chunk). At internal DiT **layer L** (layer 6 of 8 best), slice out the future-token activations, project via MLP, and align to the embedding of the future observation `φ_{t+H}`.
- **Alignment loss** `L_align = −cos(f_θ(future tokens), g(φ_{t+H}))`; **total `L = L_fm + λ·L_align`, λ=0.2 optimal** (robust across 0.1–0.5).
- **REPA lineage, JEPA-adjacent**: analogous to Representation Alignment (REPA) from text-to-image diffusion, with two differences — it aligns to *future* embeddings (not current), and uses dedicated future tokens so action-prediction and alignment are separate streams interacting via self-attention. An **implicit latent world model** that bypasses future-frame/latent reconstruction (contrasts with UWM, UVA, [DINO-WM](../entities/dino-wm.md)).

### Action-aware future embedding target (§3.2)
- Target encoder = compact **action-aware vision-language embedding model**: SigLIP-2 vision+text → 4 self-attention layers → **Q-former** compressing to **M=32 query tokens**. "Action-awareness" trained by attaching 8 DiT blocks + flow-matching objective.
- **EMA target** (not fully frozen; ρ=0.995 best) to mitigate pretrain/downstream distribution shift — the same EMA-teacher pattern as JEPA. Pretrained on ~2,000 h cross-embodiment data (GR00T sim/real + 7 [Open X-Embodiment](../entities/open-x-embodiment.md) datasets).

### Results (hard numbers)
- **Multitask sim (Table 1)**: 24 RoboCasa avg **70.1%** (vs policy-only 61.9, UWM 60.8, GR00T-N1-scratch 60.6, Diffusion Policy 51.7); 24 GR-1 humanoid avg **55.0%** (vs 44.0 / 29.5 / 45.1 / 40.9). The "up to 26%" headline is FLARE 55.0 vs UWM 29.5 on GR-1.
- **Data-efficient post-training** with cross-embodiment pretrained embedding: real GR-1 4-task avg **81.2%→95.3%** with only 100 trajectories/task.
- **Human-video co-training (§4.3)**: 150 action-less human GoPro demos/object + 10 robot demos/object; **10 traj/object 42.5%→80.0%** (roughly doubling); even with 1 robot demo, 37.5%→60.0%. Human videos use *only* the alignment loss (no actions).
- **Ablations**: action-aware target 55.0% vs raw SigLIP-2 49.6% vs no-FLARE 43.9% (even a generic teacher gives +7%); layer 6/8 best; λ=0.2 best.

## Entities mentioned
- [NVIDIA GEAR](../entities/nvidia-gear.md); advisors [Yuke Zhu](../entities/yuke-zhu.md) + [Jim Fan](../entities/jim-fan.md); [Joel Jang](../entities/joel-jang.md) among authors.
- [GR00T N1](../entities/nvidia-groot.md) (architecture base + backbone), [π0](../entities/pi-zero.md), [Diffusion Policy](../entities/diffusion-policy.md), UWM / UVA / [DINO-WM](../entities/dino-wm.md) (reconstruction-WM baselines).
- [Fourier GR-1](../entities/fourier-gr-1.md), [Franka Panda](../entities/franka-panda.md) (RoboCasa). SigLIP-2 (target encoder), Q-former, [Eagle VLM](../entities/eagle-vlm.md) (GR00T N1 backbone), REPA.

## Concepts touched
- [FLARE](../concepts/world-models/flare.md) — the concept page derived from this paper.
- [JEPA](../concepts/world-models/jepa.md) — FLARE is a JEPA-adjacent latent future-prediction with an EMA target; [world model](../concepts/world-models/world-model.md) (implicit vs reconstruction-based).
- [VLA models](../concepts/learning/vla-models.md), [Flow matching](../concepts/learning/flow-matching.md) (base objective), [imitation learning](../concepts/learning/imitation-learning.md).
- [VLA-JEPA](../sources/vla-jepa-paper.md) — the closest wiki analogue (JEPA-as-auxiliary inside a VLA).

## Open questions
- Focuses on imitation learning + pick-and-place on a real humanoid; dexterous manipulation + **RL integration** are future work.
- Human egocentric videos collected in controlled settings (head-mounted GoPros); in-the-wild scaling is open.
- Using FLARE for **planning** (like [DINO-WM](../entities/dino-wm.md)) rather than only policy co-training is flagged as a valuable extension.
