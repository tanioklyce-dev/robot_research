---
title: "UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling"
type: source
url: https://arxiv.org/abs/2604.19734
local_path: raw/2604.19734.pdf
author: Boyu Chen, Yi Chen, Lu Qiu, Jerry Bai, Yuying Ge, Yixiao Ge
venue: arXiv 2604.19734v1 (cs.RO), 21 pp.; XPENG Robotics + Tsinghua + HKU
published: 2026-04-21
ingested: 2026-08-04
format: pdf
tags: [unit, latent-action-tokens, cross-embodiment, humanoid, rq-vae, visual-anchoring, world-model, egodex, robocasa, xpeng, action-representation]
---

# UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling

**Chen, Chen, Qiu, Bai, Ge, Ge** — [XPENG Robotics](../entities/xpeng-robotics.md) + Tsinghua + The University of Hong Kong. Project page: [xpeng-robotics.github.io/unit](https://xpeng-robotics.github.io/unit/).

## Summary

UniT is the **counter-proposal** to a human-readable action language, and it names itself accordingly: *"a unified physical language"* whose vocabulary is a **codebook of discrete latent tokens**, not words. The problem is human-to-humanoid transfer — egocentric human video is abundant and humanoid data is scarce, but the kinematics don't match. UniT's insight: *"while human and humanoid kinematics differ in structural DoFs, the physical outcomes of their intents share a consistent visual representation."* So **vision is used as the universal anchor** to align disparate action spaces.

The mechanism is a **tri-branch cross-reconstruction** tokenizer. A visual branch (inverse dynamics over frozen [DINOv2](../entities/dinov2.md) features), an action branch (state + action chunk, per-embodiment MLPs onto a padded common width), and a fusion branch are each quantized by a **shared RQ-VAE codebook**, and each quantized token must decode **both** the visual transition *and* the action chunk. Forcing actions to predict vision anchors kinematics to physical consequences; forcing vision to predict actions strips away appearance confounders. What survives is the intersection: **embodiment-agnostic physical intent**.

This is the primary source for the [latent action tokens](../concepts/learning/latent-action-tokens.md) concept, and the direct empirical answer to the question in [action representation languages](../syntheses/agents/action-representation-languages.md).

## Key claims

### The architecture argument (§3.2, Fig. 2)

The paper's taxonomy of latent-action designs is itself useful:

| Design | Failure mode |
|---|---|
| **Action-only** (e.g. VQ-BeT-style) | proprioception alone → severe human/robot distribution shift, no external grounding |
| **Vision-only** (e.g. [UniVLA](../entities/univla.md)) | entangles appearance confounders — texture, lighting; misses fine-grained physical detail |
| **Decoupled vision+action** | independent tokenizers → **disjoint vocabularies**, no representational unification |
| **UniT (cross-reconstruction)** | — |

Loss: `Σ_{i∈{v,a,m}} [λ_v·L_cos(f̂ᵢ, f_{t+k}) + λ_a·L_act(âᵢ, a_{t:t+k})] + L_RQ`. The visual decoder is shared across embodiments; the action decoder is embodiment-specific. Tokens capture **relative physical change** rather than absolute configuration — which is what lets different embodiments share transition patterns despite incompatible state spaces.

### Two downstream uses

- **VLA-UniT** — built on [GR00T](../entities/nvidia-groot.md) N1.5 with [Qwen2.5-VL](../entities/qwen.md). The VLM predicts **UniT token indices** via learnable queries (cross-entropy), while a lightweight **flow-matching** head emits embodiment-specific continuous actions from the same vision-language context. So the readable-vs-latent question is sidestepped: the *prediction target* is latent, the *output* is joint angles.
- **WM-UniT** — built on **Cosmos Predict 2.5**; UniT's pre-quantization action features replace raw actions as the conditioning signal for action-conditioned video generation. Notably, the action branch takes only state and action, so this **does not leak future observations** at deployment.

### Results

**RoboCasa GR1 tabletop simulation** — 24 tasks (18 pick-and-place, 6 articulated), **50 episodes each (n = 1,200)**:

| Method | Overall |
|---|---:|
| **VLA-UniT** (Qwen2.5-VL) | **66.7** |
| FLARE | 55.0 |
| OFT (Qwen3-VL) | 48.8 |
| GR00T (Qwen3-VL) | 47.8 |
| GR00T N1.6 | 47.0 |
| π-Qwen3 | 47.6 |
| Diffusion Policy | 29.5 |

The controlled comparison is **VLA-UniT 66.7 vs GR00T-Qwen2.5 47.8** — *same architecture, differing only by UniT token prediction*, so **+18.9 pp is the value of the objective itself**.

**Data efficiency:** with 10% of the data (100 trajectories/task) VLA-UniT reaches **45.5%**, approaching the GR00T baseline's full-data 47.8% — roughly a **10× data reduction**.

**Human co-training** (EgoDex `basic_pick_place`, 27,419 trajectories, few-shot regime): in-domain 45.5 → 50.0; OOD average 34.7 → 38.5.

**Real humanoid** (IRON-R01-1.11, **50-dimensional** action space over arms, hands, waist, head, wrist):

| | GR00T-Qwen2.5 | VLA-UniT w/o human | VLA-UniT w/ human |
|---|---:|---:|---:|
| Pick & Place (n=40) | 30% | 70% | **78%** |
| Pouring (n=20) | 5% | 35% | **75%** |
| Geometry OOD (n=30) | 20.0% | 33.3% | **73.3%** |
| Distractor OOD (n=30) | 10.0% | 26.7% | **60.0%** |
| Target OOD (n=20) | 20.0% | 45.0% | **65.0%** |
| Background OOD (n=30) | 0.0% | 23.3% | **63.3%** |
| Combinatorial (n=10,30) | 10.0% | 20.0% | **70.0%** |

**Zero-shot task transfer** — a stacking task absent from robot data but present in human video: GR00T baseline **0%**, UniT without cross-reconstruction **0%**, VLA-UniT without human data **10%**, VLA-UniT with human co-training **60%**, with *emergent* waist rotation and head turning mirroring the human videos.

> [!note] The real-world gaps are large enough to survive their small N
> Most of these run at n = 20–40, where the wiki's [audit](../syntheses/platforms/vla-success-rate-audit.md) says nothing under ~17–27 pp is detectable. But the headline gaps are **40–63 pp** (Pouring 5 → 75; Background 0 → 63.3), which clear that bar comfortably. The **0% → 60% zero-shot stacking** result is the strongest single claim in the paper and would survive at almost any n. The smaller contrasts — 70 vs 78 on Pick & Place — do not separate and should not be read as ordered.

### Alignment and denoising evidence

- **t-SNE** at three levels: raw actions vs UniT tokens; VLA vision-language hidden states; WM cross-attention outputs. Vanilla baselines show cleanly **separated** human/humanoid clusters; UniT variants show **overlapping** ones. The alignment propagates from the token layer into downstream model internals — the paper's cleanest structural claim.
- **Noise robustness** — inject Gaussian noise at σ = 0.2 of the dataset's action std into EgoDex trajectories: **[FAST](../entities/fast-action-tokenization.md) degrades 10.7×**, an action-only RQ-VAE tokenizer 2.7×, **UniT only 1.7×**. Visual grounding acts as a denoiser by discarding kinematic variation with no visual correspondence. A genuinely useful side effect for messy human motion-capture data.
- **World modeling** (Table 1): on DROID, WM-UniT ≈ raw-action conditioning (PSNR 21.32 vs 21.02). Under **human-humanoid co-training** the gap opens sharply — EgoDex PSNR 28.06 vs 24.84, FVD 130.87 vs 171.37; RoboCasa-GR1 PSNR 17.66 vs 13.45, FVD 166.50 vs 237.13. **The unified interface only pays when embodiments are actually mixed** — which is an honest and clarifying negative result on single-embodiment data.

## Open questions

- **Nothing about these tokens is inspectable.** A codebook index is not auditable, loggable in human terms, or correctable by a human operator mid-episode — the three things [RT-H](rt-h-paper.md)'s language motions buy. Neither paper compares against the other, and no work in the wiki tests a readable and a latent interface on the same robot and task.
- **Vision as anchor assumes visible consequences.** Force-dominant, occluded, or in-hand manipulation has physical intent that a shared *visual* decoder cannot see. Untested here.
- **Human data is pick-and-place-shaped.** EgoDex `basic_pick_place` and `pour` carry the transfer results; whether the shared manifold holds for contact-rich or tool-use behavior is unknown.
- **RoboCasa GR1 numbers are not comparable to the wiki's LIBERO table** — different benchmark, different embodiment, and the leaders sit near 50–67% rather than 97%, which (as the [audit](../syntheses/platforms/vla-success-rate-audit.md) notes for RoboTwin) makes it a *more* discriminating benchmark.

## Entities mentioned
- [UniT](../entities/unit.md) · [XPENG Robotics](../entities/xpeng-robotics.md) · [UniVLA](../entities/univla.md)
- [DINOv2](../entities/dinov2.md) · [Qwen2.5-VL](../entities/qwen.md) · [GR00T](../entities/nvidia-groot.md) · [FAST](../entities/fast-action-tokenization.md) · [Diffusion Policy](../entities/diffusion-policy.md)
- [EgoDex](../entities/egodex.md) · [RoboCasa](../entities/robocasa.md) · [DROID](../entities/droid.md) · [Fourier GR-1](../entities/fourier-gr-1.md)

## Concepts touched
- [Latent action tokens](../concepts/learning/latent-action-tokens.md) — the concept this source founds
- [Action representation languages](../syntheses/agents/action-representation-languages.md) — the unreadable end of the spectrum, argued for on the merits
- [VLA models](../concepts/learning/vla-models.md) · [World-action model](../concepts/world-models/world-action-model.md) — WM-UniT is one
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — human-to-humanoid is a distinct transfer axis
