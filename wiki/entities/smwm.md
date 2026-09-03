---
title: SMWM (Sensorimotor World Model)
type: entity
subtype: model
created: 2026-07-26
updated: 2026-08-30
sources: 4
tags: [smwm, sensorimotor-world-model, jepa, inverse-dynamics, representation-collapse, world-model, causality, controllable-degrees-of-freedom, balestriero, scholkopf]
---

# SMWM (Sensorimotor World Model)

**SMWM** ([Ivashkov, Balestriero, Schölkopf 2026](../sources/sensorimotor-world-models-paper.md), arXiv 2606.20104) is an end-to-end-from-pixels [JEPA](../concepts/world-models/jepa.md) latent world model that uses **inverse dynamics regularization as its sole anti-collapse mechanism**. It is co-authored by [Randall Balestriero](randall-balestriero.md) but led by **Petr Ivashkov** and senior-authored by **Bernhard Schölkopf** (MPI for Intelligent Systems) — a **causality-side** entry into the JEPA-world-model line, not a [LeCun](yann-lecun.md) paper.

## Why it matters in this wiki

SMWM adds a **fourth entry to the wiki's JEPA anti-collapse taxonomy**, and the most principled one: where [DINO-WM](dino-wm.md) freezes the encoder, [PLDM](pldm.md) adds variance-covariance terms, [LeWorldModel](leworldmodel.md) matches an isotropic Gaussian (SIGReg), and [V-JEPA 2](v-jepa-2.md) uses EMA stop-gradient targets, SMWM prevents collapse with a **single inverse-dynamics head** and one hyperparameter. Its deeper claim is conceptual — "**perception for action**": a world model's representation should be shaped by what the agent can *control*, not by visual fidelity. This grounds the JEPA program in **causal representation learning** (Schölkopf): the representation should encode actions and their effects (interventions), biasing toward controllable degrees of freedom and **filtering uncontrollable distractors**. It's the clearest bridge in the wiki between the LeCun/JEPA and Schölkopf/causality research programs.

## Method

Objective `L = L_fwd + λ·L_inv`:
- **Forward loss** `‖g(z_t, a_t) − z_{t+1}‖²` — next-embedding prediction (the JEPA objective).
- **Inverse loss** `‖h(z_t, z_{t+1}) − a_t‖²` — recover the action from a pair of embeddings.

Recovering the action forces the encoder to preserve action-relevant information, ruling out the constant-embedding collapse; unlike distributional priors it **does not prescribe latent geometry**, only that the representation stay action-informative. Trained on offline, reward-free `(o_t, a_t, o_{t+1})` transitions with no frozen encoder, EMA, or complex regularizer.

## Key findings

- **Recovers controllable structure:** on a controlled "dot world," the encoder recovers the **true intrinsic dimension = controllable action dimension**, is spatially faithful, and represents **actions as latent translations** `g_a(z) ≈ z + ρ(a)` — an emergent equivariance/homomorphism (**Theorem 1**), not enforced by any loss.
- **Filters distractors:** a randomly-moving (uncontrolled) object is ignored by the encoder — encoding it would inflate the forward loss without reducing the inverse loss.
- **Planning** (CEM + MPC in latent space, [LeWM](leworldmodel.md) setup): **matches** the SIGReg baseline on 2D tasks (TwoRoom 99 vs 94, Reacher 66 vs 67, Push-T 83 vs 87) and **clearly beats it on 3D OGBench-Cube (84 vs 59)**; both dominate a forward-only ablation.

## Related

- [SIGReg](../concepts/world-models/sigreg.md) — the distributional regularizer this replaces; SMWM beats it 84 vs 59 on OGBench-Cube and ties on the 2D tasks.
- [Randall Balestriero](randall-balestriero.md) — co-author; SIGReg (its main baseline) is his [LeWorldModel](leworldmodel.md) regularizer.
- [LeWorldModel](leworldmodel.md) / [DINO-WM](dino-wm.md) / [PLDM](pldm.md) / [V-JEPA 2](v-jepa-2.md) — the other anti-collapse approaches in the taxonomy.
- [JEPA](../concepts/world-models/jepa.md) — the family; SMWM's inverse-dynamics regularizer is a new anti-collapse option.
- [Identifiability](../concepts/world-models/identifiability.md) — sibling theme (recovering controllable latent structure).

## Open questions

- Only simple 2D/3D control shown — no high-DoF or real-robot results. The single-step inverse objective's guarantees don't transfer to the continuous setting (used as [inductive bias](../concepts/learning/inductive-bias.md), not proof). Is inverse dynamics complementary to, or redundant with, SIGReg/EMA?

## Mentioned in

- [Sensorimotor World Models paper (Ivashkov, Balestriero, Schölkopf 2026)](../sources/sensorimotor-world-models-paper.md) — the primary source.
