---
title: Geometric priors, equivariance, and MDP homomorphisms
type: concept
created: 2026-09-07
updated: 2026-09-07
sources: 1
tags: [geometric-prior, equivariance, invariance, symmetry, group-action, mdp-homomorphism, inductive-bias, latent-space, world-model, reinforcement-learning, geometric-deep-learning]
---

**A geometric prior is an [inductive bias](inductive-bias.md) that encodes a known symmetry of the world into the learner, so the symmetry does not have to be learned from data.** The word comes from *geometric deep learning* (Bronstein et al. 2021), whose organising claim is that the successful architectures are the ones that respect a symmetry group: a CNN's weight sharing makes it translation-equivariant, so a detector learned in one corner works in the other without more examples.

## The vocabulary

- **Invariance** — `f(g·x) = f(x)`: the output ignores the transformation. Right for classification.
- **Equivariance** — `f(g·x) = g·f(x)`: the output transforms *with* the input. Right for anything spatial, and for control: rotate the observation and the correct action rotates too.
- **Group action** — a transformation set with identity, inverses, and composition, acting on states. In an MDP the *dynamics itself* can be a group action: turning in place generates a cyclic group; a wheeled base generates SE(2).
- **Orbit** — everything reachable from a state by the group. A symmetry prior says: learn once per orbit.

## MDP homomorphisms

Ravindran & Barto's formalisation of "these two situations are the same problem." A map `(f, g_s)` from states and actions to abstract states and actions that **preserves reward** and **preserves transition probabilities into each block of equivalent states**. Optimal values and policies lift through it: solve the small MDP, act in the large one. A **bijective** homomorphism is a symmetry of the MDP; the set of them is its symmetry group. Two things people get wrong:

- The action map is **state-dependent** (`g_s`). After a 90° rotation "north" becomes "east," but which action corresponds depends on where you are. One global relabelling assumes more than the definition gives.
- Exact homomorphisms rarely exist on hardware. The approximate version bounds the value error by how badly reward and transition preservation are violated — that bound is the honest number for a robot whose bilateral symmetry is broken by cable routing and wear.

## Three places to put the prior

| Where | How | Cost | Representative |
|---|---|---|---|
| **Architecture** | weight-tying so the network is equivariant by construction | compute overhead; exact group must be known | MDP Homomorphic Networks (van der Pol et al. 2020); equivariant Q-learning / grasping (Wang, Walters, Platt 2022) |
| **Loss** | augmentation or a consistency penalty | soft — encourages, does not guarantee | most "symmetry-aware" RL |
| **Latent topology** | choose Z with the group built in (a circle, a torus, R/2πZ × R²) and make the transition an additive group action | no architecture change; assumes group *type*, not order; assumes exact symmetry | [Group-Structured Latent Space](../../sources/group-structured-latent-space-paper.md) (2025); Quessard et al. 2020 |

The third row is the one the wiki has a primary for. Its finding, read carefully: a **fully** symmetric latent (rotation matrices) is best when the world is fully symmetric and collapses on a first-person camera; **structured + unstructured coordinates side by side** is what survives VizDoom (H@1 81 vs 59 unstructured vs 18 fully-symmetric). Disentanglement comes from a sparsity mask saying which action owns which coordinate, plus InfoNCE negatives drawn from same-action transitions.

## Why this page exists in a robot wiki

- **It is the declared-axis mechanism made explicit.** The [abstraction tax](../../syntheses/world-models/abstraction-tax.md) says a latent world model generalises along an axis only if training declared it. Topology is the strongest possible declaration: orientation *is* a circle, so a −10° turn and a 350° turn coincide by construction. The [declared-axis experiment](../../syntheses/world-models/declared-axis-experiment.md) could test this with a one-coordinate change to LeWM.
- **A wheeled base is SE(2), and MiniGrid's R/2πZ × R² is the discrete cartoon of it.** The 2025 paper stops at deterministic, exact symmetry. Wheel slip, an obstacle, and a room that is not a torus break the assumptions in exactly the ways a home does.
- **The JEPA programme barely uses it.** Collapse prevention, not symmetry, is where the [anti-collapse lineage](../../syntheses/world-models/ssl-anti-collapse-lineage.md) spends its effort; equivariance appears in the wiki mainly as the CNN story in the [curriculum](../../syntheses/curriculum/curriculum-02-cnns.md). A geometric reading of JEPA (as in the Nicolas Substack tour) is a commentator's lens, not the field's self-description.

## Related concepts

- [Inductive bias](inductive-bias.md) — the general case.
- [Contrastive learning](contrastive-learning.md) — InfoNCE is the objective in the group-structured paper.
- [Latent space](../world-models/latent-space.md) — a latent that is a manifold with a group action, not R^d.
- [World model](../world-models/world-model.md) — the abstract-MDP branch (C-SWM, PRAE, DeepMDP).
- [Identifiability](../world-models/identifiability.md) — a topological prior is one route to a latent that recovers the true factors.

## Key references

- [Group-Structured Latent Space](../../sources/group-structured-latent-space-paper.md) — the ingested primary.
- **Un-ingested:** MDP Homomorphic Networks (van der Pol, Worrall, van Hoof, Oliehoek, Welling, NeurIPS 2020); Ravindran & Barto 2004; Quessard, Barrett & Clements 2020; Kipf, van der Pol & Welling, C-SWM 2019; Park et al. 2022 (symmetric embeddings); Rezaei-Shoshtari et al. 2022 (continuous MDP homomorphisms); Bronstein et al. 2021 (geometric deep learning).

## Current state

Well-developed for gridworlds and known finite groups; thin for continuous control and approximate symmetry, which is where a robot lives. The group-structured paper's own limitations section names the gap.

## Mentioned in

- [Group-Structured Latent Space](../../sources/group-structured-latent-space-paper.md)
