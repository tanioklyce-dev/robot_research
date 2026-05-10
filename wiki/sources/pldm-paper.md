---
title: PLDM Paper — Stress-Testing Offline Reward-Free RL: A Case for Planning with Latent Dynamics Models (Sobal et al., WRL @ ICLR 2025)
type: source
url: https://openreview.net/forum?id=jON7H6A9UU
pdf: https://openreview.net/pdf?id=jON7H6A9UU
author: Vlad Sobal, Wancong Zhang, Kyunghyun Cho, Randall Balestriero, Tim G. J. Rudner, Yann LeCun
affiliation: NYU (Sobal, Zhang, Cho); Brown / FAIR (Balestriero); NYU / Oxford (Rudner); NYU / Meta FAIR (LeCun) — affiliations inferred from co-author cross-references
published: 2025-02-28 (WRL @ ICLR 2025 Workshop)
ingested: 2026-05-10
created: 2026-05-10
updated: 2026-05-10
tags: [pldm, planning-with-latent-dynamics-models, jepa, end-to-end, offline-rl, reward-free-rl, sobal, lecun, vicreg, mpc, mppi]
---

> [!note] Ingest depth
> This source page is **based on the OpenReview workshop PDF** extracted via pypdf. The full paper has 21 pages with detailed appendix; this ingest reads pages 1–5 (abstract + method + setup) and the headline results table (Table 1 / Table 2). Appendix E.1.1 has the full anti-collapse loss-term breakdown that's referenced but not unpacked here. Filed primarily to close cross-module TBDs in the curriculum (Modules 10, 11, 12).
>
> Predecessor paper: [Sobal et al. 2022](sobal2022-jepa-slow-features-paper.md) ("Joint embedding predictive architectures focus on slow features") — the 2022 paper introduces the slow-features representational claim that motivates JEPA-as-WM; the 2025 paper is the planning-and-stress-test followup. The pair is collectively referenced as **PLDM** across the wiki.

## Summary

**PLDM** ("Planning with Latent Dynamics Models") — Sobal, Zhang, Cho, Balestriero, Rudner, LeCun (NYU + FAIR, ICLR 2025 Workshop on Reinforcement Learning). The 2025 paper that introduces and extensively stress-tests the **end-to-end JEPA-style world model** that subsequent work (notably [LeWorldModel](../entities/leworldmodel.md)) compares against and critiques.

The contribution is **methodological**: across **23 carefully-controlled offline reward-free datasets** spanning two top-down navigation environments, PLDM is shown to be **the only method (out of 6 tested — HILP, HIQL, GCIQL, CRL, GCBC, PLDM) that does not completely fail in any of six generalization properties** (transfer to new environments, transfer to new tasks, data efficiency, best-case performance, learning from random trajectories, stitching suboptimal trajectories).

PLDM's architecture: an **encoder + predictor pair** trained end-to-end on offline `(state, action, next-state)` data, with a **multi-term anti-collapse objective** combining a similarity loss, a **VICReg-inspired** regularizer, and an **inverse-dynamics auxiliary** ("for more details see Appendix E.1.1"). At test time, latent-space MPC with **MPPI** sampling against an image-goal cost.

The high anti-collapse-hyperparameter count (cited downstream as "6 hyperparameters" by [LeWM](../sources/leworldmodel-paper.md), or "7 training-loss terms" via the VICReg + inverse-dynamics + similarity decomposition) is exactly what LeWM's [SIGReg](../glossary.md#sigreg) is designed to reduce to a single regularizer.

## Abstract (verbatim)

> "Reinforcement learning (RL) has enabled significant progress in controlling embodied agents. While online RL can learn complex behaviors, it is usually costly and limiting as it requires direct interactions between an agent and its environment. On the other hand, offline RL has promised to use pre-collected data to solve tasks without any direct environment interaction. In particular, zero-shot and goal-conditioned offline RL methods are even able to handle reward-free data. However, how the properties of the offline dataset influence the performance of offline RL for reward-free data remains unclear. In this work, we study how well offline RL methods for reward-free data generalize using controlled offline datasets of varying quality. We find that when given a large amount of high-quality data, model-free approaches excel but that model-based planning achieves superior performance when there is variability in the environment layouts, when solving the task requires stitching suboptimal trajectories, or when the dataset is small. Given the scarcity of high-quality, task-specific data and the abundance of suboptimal, task-agnostic trajectories in real-world scenarios, our results suggest that planning with a dynamics model is an appealing choice for zero-shot generalization from suboptimal data."

## Key claims

### Method (PLDM architecture)

- **Encoder + predictor.** Encoder maps observations to latent embeddings; predictor maps `(z_t, a_t) → ẑ_{t+1}`. End-to-end-trained; no frozen pretrained encoder.
- **Similarity loss** (the prediction objective): `L_sim = (1/N) Σ_b ‖ẑ_{t,b} − z_{t,b}‖²`.
- **Anti-collapse via VICReg-inspired objective** (Bardes et al. 2021) — the variance / invariance / covariance regularization family from [Module 11](../syntheses/curriculum-11-jepa-deep.md)'s collapse-prevention zoo §2.
- **Plus inverse-dynamics modeling** (Lesort et al. 2018) — predict the action `a_t` from `(z_t, z_{t+1})` as an auxiliary loss.
- **Net loss-term count.** Multi-term: at minimum (similarity, VICReg-variance, VICReg-covariance, VICReg-invariance, inverse-dynamics) = 5 terms. With the typical sub-decompositions and the VICReg variants used in practice, this reaches ~7 terms / 4–6 anti-collapse hyperparameters that need joint tuning ([LeWM paper](../sources/leworldmodel-paper.md) section 2 critique).

### Planning (test-time)

- Goal-conditioned latent-space MPC. Cost: `Cost(a, s_0, s_g) = Σ_t ‖h_θ(s_g) − f_θ(ẑ_t, a_t)‖`.
- **MPPI** ([Model Predictive Path Integral](https://arxiv.org/abs/1509.01149), Williams et al. 2015) for action-sequence sampling.
- Re-plans every `k = 1` step (i.e. closed-loop MPC).

### Headline empirical claim (Table 1)

PLDM is the only method that scores ≥★★✩ on all 6 generalization properties. Specifically:

| Property | HILP | HIQL | GCIQL | CRL | GCBC | **PLDM** |
| --- | --- | --- | --- | --- | --- | --- |
| Transfer to new environments | ★ | ★ | ★ | ★ | ★ | **★★★** |
| Transfer to new task | ★★ | ★ | ★ | ★ | ★ | **★★★** |
| Data efficiency | ★ | ★★ | ★★ | ★★ | ★★ | **★★★** |
| Best-case performance | ★★★ | ★★★ | ★★★ | ★★★ | ★★ | ★★ |
| Random trajectories | **★★★** | ★ | ★ | ★ | ★ | ★★ |
| Stitching | **★★★** | ★ | ★ | ★ | ★ | ★★ |
| Fail-proof in all settings | ✗ | ✗ | ✗ | ✗ | ✗ | **✓** |

Reading: HILP and PLDM are the strongest methods overall; PLDM is the **only one** that doesn't completely fail in any setting. PLDM trades off best-case performance for robustness across data conditions.

### Two-Rooms specific numbers (Table 2)

| Method | Good-quality data | No door-passing trajectories |
| --- | --- | --- |
| CRL | 0.893 ± 0.012 | 0.147 ± 0.070 |
| GCBC | 0.860 ± 0.045 | 0.084 ± 0.037 |
| GCIQL | 0.936 ± 0.009 | 0.220 ± 0.041 |
| HILP | **1.000 ± 0.000** | **1.000 ± 0.000** |
| HIQL | 0.964 ± 0.030 | 0.263 ± 0.138 |
| **PLDM** | 0.860 ± 0.028 | **0.568 ± 0.031** |

The "no door-passing trajectories" column is the stitching-from-suboptimal-data test. PLDM substantially outperforms all model-free goal-conditioned methods (CRL, GCBC, GCIQL, HIQL) but loses to HILP. Note: HILP is a representation-learning approach (state distances proportional to step count), not a world model — it's an orthogonal point in the design space.

## How this paper relates to LeWM

[LeWM](../entities/leworldmodel.md)'s critique of PLDM (per [LeWM paper](../sources/leworldmodel-paper.md) §2):

- **"6 hyperparameters"** — PLDM's anti-collapse loss is multi-term with several weights to tune; LeWM cites this as 4–6 anti-collapse hyperparameters depending on counting conventions.
- **"Training instabilities and scalability limitations"** — direct quote from the LeWM paper, citing Balestriero & LeCun 2022 ([24] in LeWM bibliography). The argument: VICReg-line objectives are sensitive to hyperparameter ratios, and the multi-term loss is hard to tune jointly.
- **"7-term loss"** — LeWM's counting includes the similarity term, three VICReg sub-terms (variance, covariance, invariance), inverse-dynamics, plus typical regularization (weight decay, etc.). The exact count varies; the substantive claim is "many more knobs than necessary."

LeWM's response: replace the multi-term anti-collapse battery with a single SIGReg regularizer (random-projection + Epps–Pulley test, justified by Cramér–Wold). Module 12's headline claim — "1 hyperparameter, bisection-tunable, vs PLDM's 6 hyperparameters with `O(n^6)` grid search" — is calibrated against this paper.

The PLDM paper itself doesn't dispute LeWM (it predates LeWM); the comparison runs the other direction.

## Why it matters in this wiki

- **The most-flagged TBD across Modules 10, 11, 12** is now closed. Previously the curriculum cited PLDM via secondary cites only.
- **The "end-to-end JEPA with multi-term loss" lineage** has a primary source. Module 11's collapse-prevention zoo §5 (multi-fix-soup family) can now point at the actual paper rather than describing the family generically.
- **The 2022 precursor (Sobal et al. arxiv 2211.10831)** is *not* yet ingested — the predecessor paper introducing JEPA-as-WM via slow-features. Listed in Open questions below.

## Predecessor paper — Sobal et al. 2022

[Source page](sobal2022-jepa-slow-features-paper.md). Sobal, Jyothir S V, Jalagam, Carion, Cho, LeCun (NeurIPS 2022 SSL Theory and Practice Workshop). Establishes that JEPA latents preferentially encode **slowly-varying features** — the representational framing that motivates planning in latent space rather than pixel space. Includes the *fixed-distractor failure mode*: JEPA fails when distractor noise doesn't vary across timesteps. The 2025 paper builds on this representational claim with the planning-and-stress-test methodology.

## Entities mentioned

- [PLDM](../entities/pldm.md) — the algorithm/family entity.
- [LeWorldModel](../entities/leworldmodel.md) — direct response paper; cites PLDM as the "end-to-end JEPA with too many hyperparameters" baseline.
- [DINO-WM](../entities/dino-wm.md) — frozen-feature alternative to PLDM's end-to-end setup.
- [Yann LeCun](../entities/yann-lecun.md) — senior author.

## Concepts touched

- [Joint-Embedding Predictive Architecture](../concepts/jepa.md) — PLDM is an end-to-end JEPA exemplar.
- [World model](../concepts/world-model.md) — Family 2 (latent-prediction); end-to-end variant.
- [Imitation learning](../concepts/imitation-learning.md) — the GCBC baseline shows the BC-vs-WM comparison directly.

## Open questions / TBD

- ~~**Sobal et al. 2022 (arxiv 2211.10831)** as a separate source page~~ — Filed: [Sobal et al. 2022 — JEPA slow features](sobal2022-jepa-slow-features-paper.md) (2026-05-10).
- **Appendix E.1.1 detailed loss decomposition** — the exact hyperparameter count and weight schedule isn't unpacked here. Worth a re-read if Module 12's "6 hyperparameters" framing needs to be sharpened.
- **Author entity pages for Vlad Sobal** — appears as lead author on the PLDM lineage; could anchor the NYU LeCun-line research thread alongside [Lerrel Pinto](../entities/lerrel-pinto.md) and [Mahi Shafiullah](../entities/mahi-shafiullah.md).
- **Comparison with [LeWM](../entities/leworldmodel.md) on PLDM's own benchmarks** — LeWM uses different environments (PushT, Reacher, OGBench-Cube, Two-Room — note: "Two-Room" appears in both papers but the LeWM Two-Room may differ from PLDM's Two-Rooms; worth verifying). A head-to-head on identical setups would isolate the SIGReg contribution.
