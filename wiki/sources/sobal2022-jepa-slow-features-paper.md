---
title: Sobal et al. 2022 — Joint Embedding Predictive Architectures Focus on Slow Features (PLDM precursor)
type: source
url: https://arxiv.org/abs/2211.10831
local_path: raw/2211.10831v1.pdf
author: Vlad Sobal, Jyothir S V, Siddhartha Jalagam, Nicolas Carion, Kyunghyun Cho, Yann LeCun
affiliation: NYU (Sobal, Jyothir S V, Jalagam); Meta AI (Carion, LeCun); Prescient Design / Genentech (Cho); CIFAR Fellow (Cho); NYU (LeCun)
published: 2022-11-20 (NeurIPS 2022 SSL Theory and Practice Workshop, short paper)
ingested: 2026-05-10 (deepened from PDF)
tags: [pldm, sobal, jepa, slow-features, representation-learning, vicreg, simclr, lecun, precursor, fixed-distractor-failure]
---

> [!note] Ingest depth
> Deepened ingest based on the **full PDF** (`raw/2211.10831v1.pdf`, 13 pages; abstract + main paper + supplementary). This is a NeurIPS 2022 SSL Theory and Practice Workshop short paper — the main content is sections 1–4 (~5 pages) plus appendix A.

## Summary

**Sobal et al. 2022** — short paper at the NeurIPS 2022 SSL Theory and Practice Workshop. The first paper in the [PLDM](../entities/pldm.md) lineage. Investigates JEPA-style world-model learning from offline `(observation, action)` sequences, using **VICReg-based** and **SimCLR-based** training objectives, and contrasts both against reconstruction-based and inverse-dynamics alternatives.

Setup: a deliberately simple **moving-dot** environment with controlled distractor noise. A single dot moves on a unit square; sequences are 17 frames (16 actions). 1M pretraining sequences, 300k for probing, 10k for evaluation. Two distractor variants: **uniform** background noise and **structured** noise (CIFAR-10 overlays); and two temporal regimes: **changing** noise (resampled per frame) vs **fixed** noise (constant within a sequence, varying across sequences).

The headline finding is **counterintuitive**: JEPA methods *fail when distractor noise is fixed* — and they fail **even worse** with structured (CIFAR-10) noise than with uniform noise. The paper title's "JEPA focuses on slow features" is *not* an unalloyed positive. JEPA preferentially encodes whatever varies most slowly *in the input distribution* — and when distractor noise is fixed, **the noise itself is the slowest feature** (it doesn't change between consecutive frames). The encoder latches onto the noise instead of the dot, and the loss-fully-zeros-out at a trivial solution.

The paper proves this analytically (eq. 1–4) for VICReg-based JEPA and notes that SimCLR-based JEPA has the same failure mode by Wang & Isola's theorem 1 (uniform-on-sphere encoder + perfect alignment minimizes InfoNCE).

This is the **diagnostic paper** that motivates the rest of the PLDM lineage: every later end-to-end JEPA work has to either (a) ensure the distractor distribution varies, or (b) add explicit anti-collapse / temporal-variation mechanisms beyond the basic VICReg/SimCLR setup.

## Abstract (verbatim)

> "Many common methods for learning a world model for pixel-based environments use generative architectures trained with pixel-level reconstruction objectives. Recently proposed Joint Embedding Predictive Architectures (JEPA) [20] offer a reconstruction-free alternative. In this work, we analyze performance of JEPA trained with VICReg and SimCLR objectives in the fully offline setting without access to rewards, and compare the results to the performance of the generative architecture. We test the methods in a simple environment with a moving dot with various background distractors, and probe learned representations for the dot's location. We find that JEPA methods perform on par or better than reconstruction when distractor noise changes every time step, but fail when the noise is fixed. Furthermore, we provide a theoretical explanation for the poor performance of JEPA-based methods with fixed noise, highlighting an important limitation."

## Method (§2)

### Setup
- **MDP** `M = (O, A, P, R)`. The agent has *no access* to rewards `R` during training; only `(observation, action)` sequences.
- Encoder `g_φ: O → ℝ^D` maps observations to `D`-dimensional latents.
- Forward model `f_θ: ℝ^D × A → ℝ^D` predicts the next latent given current latent + action.
- Auto-regressive rollout: `s̃_1 = g_φ(o_1)`, `s̃_t = f_θ(s̃_{t-1}, a_{t-1})`.
- Probing: a single linear layer trained with **frozen** encoder and predictor to recover dot position from `s̃_t`. Probes both encoder and predictor outputs.

### Methods compared
- **VICReg-JEPA** — variance + covariance regularization at each step + L2 prediction loss between forward-model output and encoder output.
- **SimCLR-JEPA** — InfoNCE loss treating forward-model output and encoder output for the same time step as positive pairs.
- **Reconstruction** — adds a decoder `d_ξ`, reconstruction loss `L = (1/T) Σ ‖o_t − õ_t‖²`.
- **Inverse Dynamics Modeling (IDM)** — linear layer predicts action from `(g_φ(o_t), g_φ(o_{t+1}))`; forward model trained via next-step prediction.
- **Supervised** — end-to-end gradient from probe to encoder + predictor (lower bound on probe error).
- **Random** — frozen random weights (upper bound, near-trivial baseline).

## The fixed-distractor failure proof (§2)

The paper's clearest analytical result. Assume the encoder collapses to *the persistent background noise* and the forward model converges to the identity. Then for VICReg-JEPA:

```
L_prediction = (1/TN) Σ_t Σ_i ‖f_θ(S_{t,i}, A_{t,i}) − g_φ(O_{t+1,i})‖²
             = (1/TN) Σ_t Σ_i ‖S_{t,i} − S_{t+1,i}‖²
             = 0                                                    (eq. 1)
```

— because `g_φ(o_t) = g_φ(o_{t+1}) = s` (encoder ignores the foreground; persistent background gives constant per-sequence `s`) and `f_θ(s, a) = s` (forward model is identity).

```
Var(s_t) = (1/N-1) Σ_i (s_i − s̄)² = σ²       (s ~ 𝒩(0, σ²I))      (eq. 2)
L_variance = max(0, γ − √(Var(S_{t,:,j}) + ε)) = 0  for large enough σ   (eq. 3)
L_covariance = (1/(T+1)(N-1)) Σ_t Σ_i Σ_{j>i} (S_t S_t^T)_{i,j} = 0     (eq. 4)
```

— because the noise variables are *independent across episodes*, so the encoder's per-episode-constant outputs have non-collapsed batch variance and decorrelated covariance entries. **All three loss terms reach zero at the trivial solution**, so VICReg-JEPA has nothing to push the encoder back toward the actual signal.

For SimCLR-JEPA: by [Wang & Isola 2020] theorem 1, InfoNCE is minimized in the infinite-negatives limit when (a) positive pairs are perfectly aligned and (b) the encoder output is uniformly distributed on the unit sphere. **Both conditions are satisfied** by the trivial solution above, so SimCLR-JEPA suffers the same failure.

This is one of the cleanest demonstrations in the SSL literature that **the slow-features inductive bias has a specific failure mode**: the *slowest* feature wins, even if it's not the *useful* feature.

## Empirical results (§3)

Dataset: 17-frame sequences of a moving dot on a unit square. Background distractor types:

- **Uniform noise** at brightness coefficient `α ∈ [0, 3]`.
- **Structured noise** — CIFAR-10 image overlay at brightness `α`.

Each combined with **changing** (resampled per frame) or **fixed** (constant per sequence) regimes. Prober trained with frozen encoder + predictor. RMSE metric on dot-position recovery, averaged over 17 timesteps. 3 random seeds.

Headline results (Figure 3):

| Setting | Reconstruction | VICReg-JEPA | SimCLR-JEPA | IDM | Supervised | Random |
| --- | --- | --- | --- | --- | --- | --- |
| **Changing uniform** (`α ≤ 3`) | OK | OK / good | OK / good | OK | OK (lower bound) | bad (upper bound) |
| **Changing structured** | OK (`α ≤ 1.5`) | OK | OK | OK | OK | bad |
| **Fixed uniform** (any `α > 0`) | OK (`α ≤ 1.5`) | **fails** | **fails** | OK | OK | bad |
| **Fixed structured** (any `α > 0`) | OK (`α ≤ 1.5`) | **fails** | **fails** | OK | OK | bad |

Key observations:

- **JEPA-based methods fail on fixed noise** at any nonzero brightness, both uniform and structured.
- **Reconstruction works for α ≤ 1.5** in all four settings — but degrades at higher brightness because the reconstruction loss pulls the encoder toward representing the bright noise too.
- **IDM works in all settings** — but only because it specifically targets the agent. With multiple agents (3-dot variant in appendix A.6), IDM also fails: it captures the *first* dot and ignores the others.
- JEPA does *not* require hyperparameter tuning to handle higher levels of changing noise; reconstruction *does* (per appendix A.5). So when noise is changing, JEPA is robust; when noise is fixed, JEPA is broken.

## Conclusion (§4)

> "We demonstrate that JEPA-based methods offer a possible way forward for reconstruction-free forward model learning and are capable of ignoring unpredictable noise well even without additional hyperparameter tuning. However, these methods fail when slow features are present, even with a large pre-training dataset and hyperparameter tuning."

The paper's suggested fixes:

- **Image differences or optical flow as input** — would force the encoder to ignore static backgrounds. (But would lose static information that may be useful elsewhere.)
- **Hierarchical JEPA (HJEPA)** — per [LeCun 2022, A Path Towards Autonomous Machine Intelligence].
- **Temporal-constancy regularization** — explicitly penalize representations that are constant across time.

The third option is essentially the direction the rest of the JEPA program took — ensuring the encoder doesn't collapse to a temporally-constant solution becomes the central engineering problem. [LeJEPA](lejepa-paper.md)'s SIGReg is a much later answer to this question: enforce isotropic-Gaussian latent distribution (which rules out *all* low-rank or constant solutions, not just temporally-constant ones).

## How this paper relates to LeWM / LeJEPA / PLDM

- **The "slow features" framing** is the *positive* claim that motivates JEPA-as-WM: a JEPA preferentially captures slowly-varying features, which is exactly what's useful for control. [Module 11](../syntheses/curriculum/curriculum-11-jepa-deep.md) §2 ("What 'joint embedding' means") draws on this representational argument.
- **The fixed-distractor failure mode** is the *negative* claim that motivates everything else in the JEPA program: VICReg + SimCLR are not enough. You need *additional* mechanisms (temporal-constancy regularization, EMA, frozen encoders, or [SIGReg](../glossary.md#sigreg)) to prevent the slowest-feature-wins collapse.
- **PLDM 2025** ([source](pldm-paper.md)) is the planning-and-stress-test followup. The 2022 paper's diagnostic motivates the 2025 paper's choice of multi-term anti-collapse loss (VICReg-inspired + inverse-dynamics + similarity).

## Entities mentioned

- [PLDM](../entities/pldm.md) — the family entity; this paper is the 2022 predecessor.
- [Yann LeCun](../entities/yann-lecun.md) — senior author.

## Concepts touched

- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — this paper's central diagnosis.
- [Learned latent space](../concepts/world-models/latent-space.md) — what the slow-features framing is about.

## Open questions / TBD

- **Vlad Sobal author entity page** — would anchor the lead-author thread of the PLDM lineage and the 2025 followup.
- **Connection to neuroscience's "slow feature analysis"** (Wiskott & Sejnowski 2002) — the term "slow features" precedes this paper. The 2022 paper doesn't explicitly cite SFA but the conceptual lineage is direct. Worth flagging if the curriculum picks up neuroscience-connection threads.
- **HJEPA** (LeCun's hierarchical-JEPA proposal from "A Path Towards Autonomous Machine Intelligence") — referenced as a possible fix; would be a useful concept page if the curriculum picks up hierarchical-JEPA threads.
