---
title: H-JEPA (Hierarchical JEPA)
type: entity
subtype: method
created: 2026-10-13
updated: 2026-10-22
sources: 4
tags: [h-jepa, hierarchical-world-model, jepa, hierarchical-planning, leworldmodel, sigreg, inverse-dynamics, lecun, balestriero]
---

**H-JEPA** names two things in this wiki: LeCun's 2022 *proposal* for a hierarchy of JEPAs, and the 2026 *method* that implements it end to end. In the method, each level has its own encoder and latent space and predicts farther ahead than the level below, and planning runs top-down through subgoals ([Zhang, Terver et al., Oct 2026](../sources/h-jepa-hierarchical-world-models-paper.md)).

> [!note] Disambiguation
> - **The proposal**: [A Path Towards Autonomous Machine Intelligence](../sources/lecun2022-path-towards-ami.md) (2022). Low levels make detailed short-range predictions; high levels make abstract long-range ones.
> - **[HWM](hwm.md)** (April 2026): the first implementation of the *temporal* half, with two planning timescales over **one shared latent space**, wrapping frozen world models with CEM.
> - **H-JEPA** (October 2026, this page): **distinct latent spaces per level**, trained jointly from pixels, gradient-descent planning. The first implementation of the *representational* half as well.
> - Unrelated: [HP-JEPA](../sources/hp-jepa-paper.md), multi-resolution JEPA on graphs.
> - **Also unrelated, and confusingly abbreviated "H-JEPA" in its own paper:** [Hamiltonian JEPA](hamiltonian-jepa.md) (Zoabi, Ali, Wolf, Sept 2026), a port-Hamiltonian predictor with an orthonormal action port. Not hierarchical.

## How it works
- Level 1 is [LeWorldModel](leworldmodel.md) (ViT encoder, causal-transformer predictor, [SIGReg](../concepts/world-models/sigreg.md)). Each higher level encodes every s-th lower latent (s = 2 in simulation, 3 on DROID) and pools the intervening action embeddings into a macro-action. Each level has its own predictor and SIGReg term, and everything trains end to end.
- Planning: the top level minimises the distance from its final predicted latent to the goal. Each lower level matches the upper level's first predicted latent by re-encoding its own rollout upward. Gradient descent at every level; upper-level search is clipped to the range of macro-actions seen in training.
- On scenes that change between episodes (DROID), an **inverse-dynamics loss** is required at every level to avoid [slow-feature collapse](../concepts/world-models/slow-feature-collapse.md).

## Results ([paper](../sources/h-jepa-hierarchical-world-models-paper.md))
| Setting | Flat LeWM | H-JEPA | Notes |
|---|---|---|---|
| Visual AntMaze, 50 tasks | 18.0% | **73.3%** (3 levels) | less planner compute; ~2× HWM-style baseline |
| FourRoom / Cube | — | better Pareto front up to 3 levels | ties HWM on FourRoom |
| Push-T | — | 2 levels ≥ flat; **3 levels fails** | short episodes starve deep levels of clips |
| DROID offline, 16 clips (Fréchet fidelity) | 34% (with IDM) | **~40%** (2 levels) | HWM-style ~35%; no closed-loop test |

**When abstraction emerges:** only if the data's fast and slow factors differ in timescale by more than about 2×. Navigation clears that; tabletop manipulation datasets mostly don't.

## Same week, opposite bet
[RoboJEPA](robojepa.md) (Meta FAIR, 2026-10-07) keeps the encoder **frozen** (V-JEPA 2.1) and scales a flat predictor to 8B on 2.87M multi-embodiment episodes, with **closed-loop** real-robot results. H-JEPA trains small encoders **end to end** and scales in hierarchy depth, with real-robot results offline only. Comparison table on the [RoboJEPA source page](../sources/robojepa-scaling-robotic-latent-world-models-paper.md#relation-to-the-h-jepa-paper-also-ingested-2026-10-13).

## Related
- [Three ways to scale a JEPA world model](../syntheses/world-models/three-ways-to-scale-a-jepa-world-model.md) — the synthesis comparing this with the other two autumn-2026 scaling bets.
- [HWM](hwm.md) — the shared-latent predecessor, same first author.
- [JEPA](../concepts/world-models/jepa.md) · [Gradient-based planning](../concepts/world-models/gradient-based-planning.md) · [PLDM](pldm.md) · [WorldDP](worlddp.md) (hierarchy with a diffusion-policy low level).
- [Yann LeCun](yann-lecun.md) · [Randall Balestriero](randall-balestriero.md) · [Basile Terver](basile-terver.md).

## Mentioned in
- [H-JEPA paper (Zhang, Terver et al., 2026)](../sources/h-jepa-hierarchical-world-models-paper.md) — primary.
- [A Path Towards Autonomous Machine Intelligence](../sources/lecun2022-path-towards-ami.md) — the proposal.
- [Hierarchical Planning with Latent World Models (HWM)](../sources/hwm-paper.md) — the temporal-only predecessor.
- [RoboJEPA paper](../sources/robojepa-scaling-robotic-latent-world-models-paper.md) — the frozen-encoder contrast case.
- Synthesis: [What the latent throws away](../syntheses/world-models/jepa-dynamics-collapse-fixes.md)
