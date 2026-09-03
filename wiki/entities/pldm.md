---
title: PLDM (Planning with Latent Dynamics Models)
type: entity
subtype: method
created: 2026-05-10
updated: 2026-07-26
sources: 8
tags: [pldm, planning-with-latent-dynamics-models, jepa, end-to-end-jepa, sobal, lecun, vicreg, mpc, mppi]
---

**PLDM** — **Planning with Latent Dynamics Models**. End-to-end JEPA-style world-model family from Vlad Sobal and Yann LeCun's group at NYU (with Cho, Balestriero, Rudner, etc.). The pre-LeWM reference for "what an end-to-end JEPA WM looks like when you do it carefully with the standard tools." Cited heavily as a comparison baseline in the broader JEPA-WM literature.

## Family lineage

- **PLDM-2022** (Sobal, Jyothir S V, Jalagam, Carion, Cho, LeCun) — [source page](../sources/sobal2022-jepa-slow-features-paper.md). "Joint embedding predictive architectures focus on slow features." Establishes the representational framing: JEPA latents preferentially encode slowly-varying features, which is exactly what's useful for planning. NeurIPS 2022 SSL workshop (short paper).
- **PLDM-2025** (Sobal, Zhang, Cho, Balestriero, Rudner, LeCun) — [source page](../sources/pldm-paper.md). "Stress-Testing Offline Reward-Free Reinforcement Learning: A Case for Planning with Latent Dynamics Models." The planning-and-stress-test followup; the canonical PLDM reference. WRL @ ICLR 2025 Workshop.

## Architecture (per [PLDM Paper 2025](../sources/pldm-paper.md))

- **Encoder + predictor**, end-to-end-trained on offline `(state, action, next-state)` data.
- **Multi-term anti-collapse loss:** similarity (next-embedding MSE) + VICReg-inspired regularization (variance + invariance + covariance) + inverse-dynamics auxiliary. At least 5 loss terms; ~6 anti-collapse hyperparameters per the [LeWM paper](../sources/leworldmodel-paper.md)'s critique.
- **Planning:** latent-space MPC with **MPPI** sampling. Goal-conditioned via image-goal cost `Cost(a) = Σ_t ‖z_g − ẑ_{t+1}‖`. Re-plan every step.

## Why it's in this wiki

- **The end-to-end JEPA baseline that [LeWM](leworldmodel.md) responds to.** LeWM's "6 hyperparameters → 1" headline is calibrated against PLDM specifically.
- **The clearest published example of multi-term anti-collapse in a JEPA-WM setting.** Module 11's collapse-prevention zoo §5 (multi-fix-soup family) points here as the exemplar.
- **The PLDM stress-testing methodology (23 datasets, 6 generalization properties)** is itself a research contribution — the kind of benchmark methodology that would be useful to apply to LeWM and other end-to-end JEPAs.

## Position vs adjacent methods

| Method | Encoder | Anti-collapse | Hyperparameters | Predictor + planning |
| --- | --- | --- | --- | --- |
| **PLDM** | end-to-end | VICReg + inverse-dyn + similarity | ~6 (per LeWM critique) | MPC + MPPI |
| [LeWM](leworldmodel.md) | end-to-end | **single [SIGReg](../glossary.md#sigreg)** | **1** (`λ`) | MPC + CEM (and gradient variants) |
| [DINO-WM](dino-wm.md) | **frozen DINOv2** | encoder can't collapse | 0 (frozen) | MPC + CEM |
| [V-JEPA 2-AC](v-jepa-2.md) | EMA target + stop-grad (V-JEPA 2 frozen, 300M predictor post-trained) | EMA + L1 + augmentation | ~3 | MPC |
| [Dreamer](dreamer.md) | trained, decoder-equipped | (different family — generative WM) | n/a | actor-critic in imagination |
| [TD-MPC](td-mpc.md) | trained, decoder-free | (RL bootstrap) | n/a | MPC + TD-bootstrapped value |

The four-row "JEPA-line" comparison (PLDM, LeWM, DINO-WM, V-JEPA 2-AC) is the substantive Module 11 / Module 12 axis: which collapse-prevention strategy, at what cost in hyperparameters, on what benchmark.

## Where PLDM wins / loses (Table 1 of the 2025 paper)

- **Wins:** transfer to new environments, transfer to new tasks, data efficiency, fail-proof-in-all-settings (the only method without a complete failure mode).
- **Loses (or draws):** best-case performance (HILP/HIQL/GCIQL beat it); random-trajectory and stitching settings (HILP wins outright).
- **Reading:** PLDM trades best-case performance for **robustness across data quality regimes**. That's the kind of property worth having in a deployable world model.

## Related

- [LeWorldModel](leworldmodel.md) — direct response paper (March 2026). LeWM critiques PLDM's hyperparameter complexity.
- [V-JEPA 2](v-jepa-2.md) — Meta FAIR's parallel JEPA-WM line at much larger scale.
- [DINO-WM](dino-wm.md) — frozen-feature alternative; sidesteps PLDM's collapse problem entirely by not training the encoder.
- [Yann LeCun](yann-lecun.md) — senior author.
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — umbrella concept.
- [World model](../concepts/world-models/world-model.md) — umbrella concept; PLDM is a Family-2 (latent-prediction) entity.

## Mentioned in

- [PLDM Paper](../sources/pldm-paper.md) (2025)
- [HWM — Hierarchical Planning with Latent World Models](../sources/hwm-paper.md) — PLDM is the **Diverse Maze base** HWM wraps (+39% zero-shot on unseen layouts)
- [Sobal et al. 2022 — JEPA slow features](../sources/sobal2022-jepa-slow-features-paper.md) (predecessor)
- [LeWorldModel Paper](../sources/leworldmodel-paper.md) (as a baseline)
- [stable-worldmodel paper (Maes et al., 2026)](../sources/stable-worldmodel-paper.md) — implemented as a baseline in the `swm` platform; benchmarked under controlled visual/physical perturbation (quadratic decay under distractors).
- [Sensorimotor World Models paper (Ivashkov et al., 2026)](../sources/sensorimotor-world-models-paper.md) — PLDM cited as the "variance-covariance regularizer" point in the anti-collapse design space (PLDM itself already includes an inverse-dynamics term among its auxiliary losses).

## Open questions / TBD
- **Author entity for Vlad Sobal** — appears as lead author across both papers; could anchor a NYU LeCun-line thread.
- **A direct PLDM-vs-LeWM head-to-head on PushT or Two-Rooms** — would isolate the SIGReg contribution. LeWM reports 78% PushT vs LeWM's 96%; PLDM's own evaluation uses different environments.
