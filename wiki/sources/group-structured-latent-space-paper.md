---
title: "Learning Abstract World Models with a Group-Structured Latent Space"
type: source
url: https://arxiv.org/abs/2506.01529
local_path: raw/group-structured-latent-space_2506.01529.pdf
sha256: aed0bdfcfb522bddf32a7f9c2d8d85d3acba5ede81b803a20c4a4c333308e16d
author: Thomas Delliaux, Nguyen-Khanh Vu, Vincent François-Lavet, Elise van der Pol, Emmanuel Rachelson
published: 2025-06-02
ingested: 2026-09-07
venue: "arXiv preprint; read at v2 (2026-05-19). Code: github.com/khanhvu207/world-models-group-latents"
format: paper (20 pp incl. appendices)
tags: [world-model, geometric-prior, symmetry, group-action, equivariance, mdp-homomorphism, latent-space, contrastive, infonce, disentanglement, minigrid, vizdoom, abstract-mdp, van-der-pol, isae-supaero]
---

# Learning Abstract World Models with a Group-Structured Latent Space

ISAE-SUPAERO (Toulouse) + ETH Zürich + VU Amsterdam + Microsoft Research AI for Science. **[Elise van der Pol](../entities/elise-van-der-pol.md)** — first author of *MDP Homomorphic Networks* — is a co-author, which places this paper as that line's answer to *"do you need an equivariant network to get the benefit of a known symmetry?"* Their answer: no, put the symmetry in the **topology of the latent space** and leave the architecture alone. This is the paper behind the "geometric priors" paragraph in the [Nicolas JEPA tour](../syntheses/world-models/generative-video-vs-jepa-world-models.md); the wording there is lifted from this abstract.

## Summary

An *abstract world model* here is the decoder-free triple (encoder φ, latent transition τ, reward r) trained with a contrastive predictive objective — the [C-SWM / PRAE](../concepts/learning/contrastive-learning.md) tradition, not the VAE one. The contribution is to **choose the latent space Z to have the symmetry group of the environment built in**, and to implement the transition as an **additive group action** on that space: `ẑ_{t+1} = z_t ⊕ Δ(z_t, a)`. For a cyclic symmetry (turning in place returns you to where you started) Z is the circle **R/kZ** and ⊕ is addition mod k; for two of them, a torus; for rotation-plus-position, the product **R/2πZ × R²** with modular addition on the first coordinate and ordinary addition on the rest. What is *learned* is how far each action moves you (Δ) and everything unstructured; what is *assumed* is the group's *type* (cyclic), not its order. A **sparsity mask** on Δ forces each action to touch only its own coordinates — turning cannot change position — which is where the disentanglement comes from. Against an unstructured latent of the same dimension, this predicts held-out transitions far better on a torus gridworld, a top-down MiniGrid, and 64×64 first-person **VizDoom** frames, and improves a downstream DDQN agent trained on the frozen model.

## Key claims

- **Objective (§2.3, §3.1).** Predictive loss + entropy term ≈ **InfoNCE** (Eq. 5), plus reward L2, plus a hinge loss bounding the latent's volume (Eq. 7). No decoder. The InfoNCE negatives are the collapse defence — this is the contrastive branch of the [anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md), and the paper's Eq. 9 (`τ(φ(s), a) = φ(s′)`) is the [MDP-homomorphism](../concepts/learning/geometric-priors-and-equivariance.md) condition stated as a training target.
- **The prior is the manifold, not the network (§3.2).** *"These improvements come without altering the training objectives or network architectures."* Explicit contrast with equivariant architectures (weight-tying à la MDP Homomorphic Networks, Park et al. 2022, Wang et al. 2022) which *"come with additional computational overhead."* Only a cyclic-group *structure* is assumed, not the number of elements — Passage learns 2π/7 per step from a 7-cycle without being told 7.
- **Disentanglement by masking + action-conditioned negatives (§3.3).** `L_disent = |Δ(z,a)_σ(a)|` zeroes the coordinates action a must not affect; the σ(a) subspaces are disjoint across actions. InfoNCE negatives are drawn **from transitions with the same action**, so the contrast is *where you were* rather than *what you did*. Both are needed for the orientation/position split to emerge cleanly (Fig. 5, Fig. 6).
- **Environments (§4).** Passage (7-cycle, Z = R/2πZ); Torus 5×5 (Z/nZ × Z/nZ, Z = torus, homeomorphic to R³ for plotting); MiniGrid 5×5 top-down with {forward, turn-right}, Z = R/2πZ × R²; **VizDoom** custom single textured room, 64×64 RGB, rotation fixed at δ = 36°, 100k random-policy transitions, actions {forward, nothing, left, right}, **3-D latent**. Models are tiny: 2×32-unit MLPs, a 4-conv CNN for VizDoom; Apple M3 / one RTX 3090.
- **Held-out transition prediction (Table 1; H@1 / H@5 / MRR ×100).**

  | Env | AWM + geometric priors | AWM, same latent dim | PRAE (van der Pol 2020a) | Rotation matrix (Quessard 2020) |
  |---|---|---|---|---|
  | MiniGrid 5×5 | **85.6 / 97.8 / 91.1** | 13.3 / 70.0 / 37.7 | 24.4 / 77.8 / 24.4 | 83.3 / 98.2 / 90.0 |
  | Torus 5×5 | 96.0 / 100 / 98.0 | 56.0 / 100 / 70.4 | 12.0 / 100 / 42.5 | **100 / 100 / 100** |
  | VizDoom | **81.0 / 93.7 / 86.8** | 59.3 / 79.1 / 68.6 | 42.4 / 71.7 / 55.7 | 17.6 / 27.2 / 23.7 |

  Standard deviations are large on MiniGrid (±14 on H@1). Fig. 4: with 10% of state-action pairs withheld, the unstructured model *"fails to predict the unseen transitions"* and the structured one gets them.
- **Downstream RL (§4.5, App. E).** DDQN on frozen abstract states, with the transition model used to **synthesise one-step transitions for every action** from each stored state (no extra environment interaction). With-priors beats no-priors beats vanilla DDQN on all three environments (Fig. 8, 5 seeds; curves only, no table).
- **Limitations, stated (App. A).** Translations and rotations only; **group structure assumed known a priori**; **deterministic MDPs and exact symmetries**; no stochastic dynamics, no continuous control, no real-world data — *"which often present a messy mix of group-structured actions and unstructured dynamics."*

## The wiki's read

- **Read Table 1 for the mixed case, not the pure one.** Quessard's rotation-matrix latent *wins* on the torus and ties on MiniGrid — a fully symmetric latent is fine when the world is fully symmetric. It falls to 17.6 on VizDoom. The paper's real claim is narrower and better than its abstract: **structured + unstructured coordinates side by side is what survives a first-person camera.** That is also the case a robot is in.
- **This is a declared-axis machine.** The [abstraction-tax](../syntheses/world-models/abstraction-tax.md) page argues a latent world model generalises along an axis only if something at training time *declared* that axis. Here the declaration is the topology: orientation *is* a circle, so a 350° turn and a −10° turn land in the same place by construction, and the model never has to learn it from data it did not see. The mask then declares which action owns which axis. It is the cleanest instance in the wiki of manufacturing an [inductive bias](../concepts/learning/inductive-bias.md) at the representation level rather than the architecture level.
- **The hedge that matters for a home robot: exact symmetry.** A real base does not turn exactly δ per command, and the symmetry is broken by wheel slip, cable drag, and a room that is not a torus. The formulation assumes exact symmetry and deterministic dynamics; the authors say so. The obvious next experiment — a soft version, where Δ's modular coordinate carries a learned per-step noise — is not in the paper. Neither is any comparison to a JEPA on the same frames, so how this interacts with a frozen DINOv2 encoder is unknown.
- **What the numbers measure.** H@k on a static random-policy dataset is *transition retrieval*: rank the true next latent among candidates. It says the representation is predictable, not that it is controllable; the RL result is the only control evidence and it is a reach-the-goal gridworld with curves only.
- **Compute.** Everything here runs on a laptop. If the [declared-axis experiment](../syntheses/world-models/declared-axis-experiment.md) ever runs, adding a circle-topology orientation coordinate to LeWM's latent is a one-afternoon variant.

## Entities mentioned

- [Elise van der Pol](../entities/elise-van-der-pol.md) — co-author; MDP Homomorphic Networks, PRAE (the baseline), C-SWM (with Kipf).
- Thomas Delliaux, Nguyen-Khanh Vu (equal contribution); Vincent François-Lavet (VU Amsterdam; *Combined RL via abstract representations*, 2019); Emmanuel Rachelson (ISAE-SUPAERO).

## Concepts touched

- [Geometric priors and equivariance](../concepts/learning/geometric-priors-and-equivariance.md) — the concept page this source creates: geometric prior, MDP homomorphism, equivariant network, group-structured latent.
- [Inductive bias](../concepts/learning/inductive-bias.md) — the prior lives in the manifold.
- [Contrastive learning](../concepts/learning/contrastive-learning.md) — InfoNCE as a world-model objective; the same-action-negatives trick.
- [World model](../concepts/world-models/world-model.md) — the C-SWM / PRAE "abstract MDP" branch.
- [Latent space](../concepts/world-models/latent-space.md) — a latent that is a torus, not R^d.

## Open questions

- Soft / approximate symmetry: what happens to Table 1 when δ is jittered per step, or when the room has an obstacle that breaks translation?
- Continuous actions and SE(2) for a wheeled base — the natural extension the limitations section names.
- Same frames, DINOv2 features in, circle coordinate out: does the prior still help once the encoder is a foundation model?
- The un-ingested primaries behind this: [MDP Homomorphic Networks](https://proceedings.neurips.cc/paper/2020/file/2be5f9c2e3620eb73c2972d7552b6cb5-Paper.pdf) (NeurIPS 2020), Quessard et al. 2020, Kipf et al. C-SWM 2019, Park et al. 2022 — listed in the backlog.
