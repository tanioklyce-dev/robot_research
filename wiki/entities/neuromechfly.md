---
title: NeuroMechFly
type: entity
subtype: simulator-body-model
created: 2026-05-08
updated: 2026-05-08
sources: 1
tags: [neuromechfly, drosophila, biomechanical-simulation, predecessor]
---

**NeuroMechFly** — anatomically detailed neuromechanical model of the adult *Drosophila melanogaster*, focused on **walking and grooming** (no flight). Predecessor to [flybody](flybody.md).

## Versions

- **NeuroMechFly v1** (Lobato-Rios et al. 2022, *Nat. Methods* 19:620–627) — walking + grooming with a heuristically designed low-level walking controller.
- **NeuroMechFly v2** (Wang-Chen et al. 2024, *Nat. Methods* 21:2353–2362) — pairs the heuristic low-level controller with a *learnt* high-level controller for sensory-guided behaviours.

## Position vs flybody

Per the [flybody Paper](../sources/flybody-paper.md):

- **NeuroMechFly:** walking + grooming. Heuristic low-level + learnt high-level controller.
- **flybody:** **flight + walking unified**. End-to-end deep-RL low-level controllers; hierarchical reuse for vision-guided flight.

NeuroMechFly demonstrated the value of an anatomically detailed *Drosophila* body. flybody scales the controller stack and adds aerodynamics + adhesion physics.

## Why it matters here

- Bread-crumb in the **biomechanical-simulation lineage** that runs *C. elegans* → Hydra → virtual rodent → NeuroMechFly → flybody.

## Related

- [flybody](flybody.md) — direct successor.
- [Drosophila melanogaster](drosophila.md) — shared organism.
- [Biomechanical simulation](../concepts/biomechanical-simulation.md) — concept umbrella.

## Mentioned in

- [flybody Paper](../sources/flybody-paper.md) (cited as direct predecessor)

## Open questions / TBD

- The two NeuroMechFly papers are not yet ingested as their own source pages. Stub here is sufficient until referenced more deeply.
- License / open-source status of NeuroMechFly itself — unverified in this wiki.
