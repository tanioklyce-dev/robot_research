---
title: "Sensorimotor World Models: Perception for Action via Inverse Dynamics (Ivashkov, Balestriero, Schölkopf 2026)"
type: source
url: https://arxiv.org/abs/2606.20104
author: Petr Ivashkov, Randall Balestriero, Bernhard Schölkopf (MPI-IS Tübingen / Brown / ELLIS / ETH Zürich)
published: 2026-06-18
ingested: 2026-07-26
local_path: raw/2606.20104.pdf
sha256: 1a366a3764e80702ab9f652d6e1670a662c806f0936377861838301168380862
venue: arXiv preprint (cs.LG)
license: arXiv
format: pdf
tags: [smwm, sensorimotor-world-model, jepa, inverse-dynamics, representation-collapse, world-model, causality, perception-for-action, controllable-degrees-of-freedom, balestriero, scholkopf]
---

# Sensorimotor World Models: Perception for Action via Inverse Dynamics

## Summary

**Sensorimotor World Models (SMWM)** proposes a **single, principled fix** for the central practical problem of end-to-end [JEPA](../concepts/world-models/jepa.md)-style latent world models — **representation collapse** — using **inverse dynamics regularization** as the *sole* anti-collapse mechanism. A forward model predicts the next embedding from the current embedding + action; an **inverse model** predicts the action from a pair of consecutive embeddings. Because recovering the action requires the encoder to preserve action-relevant information, the inverse loss both (a) rules out the trivial collapsed solution and (b) biases the representation toward the environment's **controllable degrees of freedom**, discarding uncontrollable distractors. No frozen encoder, no EMA target, no distributional/variance-covariance regularizer. The paper frames this as "**perception for action**": representations should be judged not by visual fidelity but by their relevance to the actions available to the agent — an idea it ties to **causality** (a causal/interventional world model), enactive perception, common coding, and affordances. It is a [Randall Balestriero](../entities/randall-balestriero.md) co-authored paper, but led by **Petr Ivashkov** and senior-authored by **Bernhard Schölkopf** (Max Planck Institute for Intelligent Systems) — not by [LeCun](../entities/yann-lecun.md).

## Key claims

- **The collapse problem it targets:** when an encoder + latent dynamics model are trained jointly to predict in embedding space, the encoder can map every observation to a constant embedding (forward loss → 0, model useless). Prior JEPA world models each patch this differently — [DINO-WM](../entities/dino-wm.md) **freezes** a pretrained encoder; [PLDM](../entities/pldm.md) adds **variance-covariance** regularizers; [LeWorldModel](../entities/leworldmodel.md) matches embeddings to an **isotropic Gaussian via SIGReg**; [V-JEPA 2](../entities/v-jepa-2.md) uses **stop-gradient + EMA** target encoder.
- **The SMWM mechanism:** objective `L = L_fwd + λ·L_inv`, where `L_fwd = ‖ĝ(z_t,a_t) − z_{t+1}‖²` (forward) and `L_inv = ‖h(z_t,z_{t+1}) − a_t‖²` (inverse). A collapsed encoder makes the inverse model's best guess a constant action; any reduction below that requires `(z_t, z_{t+1})` to be action-informative — so collapse is ruled out. Unlike distributional priors, inverse dynamics **does not prescribe the geometry** of the latent space; it anchors it to a task-grounded quantity (the action). One extra hyperparameter (λ).
- **Learned structure (controlled "dot world" testbed):** the encoder recovers the **true intrinsic dimension = the controllable action dimension** (2D dot → 2 significant PCs in a 64-D latent; the other 62 collapse), is **spatially faithful** (world-state grid → near-square latent grid), and represents **actions as latent translations** `g_a(z) ≈ z + ρ(a)` — an emergent equivariance/homomorphism (**Theorem 1**: if actions form a semigroup and equivariance holds, `a ↦ g_a` is a homomorphism), not enforced by any loss term.
- **Controllable DoF & distractor filtering:** across Independent / Coupled / Distractor / Combined dot configs, the number of significant PCs matches the *controllable* dimension; a randomly-moving **distractor dot is ignored** (encoding it would inflate `L_fwd` without reducing `L_inv`). A post-hoc decoder shows uncontrolled pose variables are averaged out (an uncontrolled rotation → an orientation-averaged blob).
- **Planning results** (goal-conditioned CEM + receding-horizon MPC in latent space, following [LeWM](../entities/leworldmodel.md)'s setup; 50-step budget, goal 25 steps ahead, 5 seeds):
  - **TwoRoom (2D nav):** SMWM **99** vs SIGReg 94, Forward-only 37, Random 30.
  - **Reacher:** SMWM **66** ≈ SIGReg 67 (Forward-only 11, Random 14).
  - **Push-T:** SMWM **83** ≈ SIGReg 87 (Forward-only 2, Random 3).
  - **OGBench-Cube (3D tabletop):** SMWM **84** vs SIGReg **59** (Forward-only 44, Random 43) — SMWM matches SIGReg on the three 2D tasks and **clearly wins on the harder 3D task**.
  - Both regularized variants dominate the Forward-only ablation, confirming an effective anti-collapse mechanism is necessary for usable planning.
- **Theoretical/conceptual framing:** connects to **causal representation learning** (Schölkopf's program) — a useful representation should encode actions and their effects (interventions), not just predictive correlations — and to cognitive-science notions (perception-for-action, common coding, enactive perception, sensorimotor contingencies, Gibson's affordances, von Uexküll's *Umwelt*).

## Entities mentioned

- **[SMWM](../entities/smwm.md)** — the subject of this source.
- [Randall Balestriero](../entities/randall-balestriero.md) — co-author (Brown); the LeJEPA/SIGReg counterpart whose regularizer is the main baseline here.
- [LeWorldModel](../entities/leworldmodel.md) / [DINO-WM](../entities/dino-wm.md) / [PLDM](../entities/pldm.md) / [V-JEPA 2](../entities/v-jepa-2.md) — the anti-collapse approaches SMWM is contrasted against.
- Authors: Petr Ivashkov (MPI-IS Tübingen), Bernhard Schölkopf (MPI-IS / ELLIS / ETH Zürich) — the causality-side senior author.

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) — SMWM is a JEPA-family end-to-end-from-pixels world model; adds inverse dynamics to the anti-collapse design space.
- [World model](../concepts/world-models/world-model.md) — a latent, offline, reward-free world model.
- [Identifiability](../concepts/world-models/identifiability.md) — related theme (recovering controllable latent structure); complements the [Klindt/LeCun/Balestriero identifiability theorems](when-does-lejepa-learn-a-world-model-paper.md).
- [SIGReg](../concepts/world-models/sigreg.md) — inverse-dynamics regularization as the alternative; beats SIGReg 84 vs 59 on OGBench-Cube.

## Open questions

- Evaluated on **simple 2D/3D control** (dot world, TwoRoom, Reacher, Push-T, OGBench-Cube) — no high-DoF or real-robot results. Does inverse-dynamics regularization scale to complex manipulation the way SIGReg/EMA approaches are being pushed?
- The single-step inverse objective's theoretical guarantees (from finite rich-observation settings) **do not transfer** to the continuous setting — the authors use it as inductive bias, not proof. What's the continuous-state identifiability story?
- How does inverse-dynamics regularization compose with the other anti-collapse mechanisms (SIGReg, EMA) — complementary or redundant?
