---
title: NeuroMechFly
type: entity
subtype: simulator-body-model
created: 2026-05-08
updated: 2026-05-08
sources: 3
license: Apache-2.0
url: https://neuromechfly.org/
code: https://github.com/NeLy-EPFL/flygym/
tags: [neuromechfly, flygym, drosophila, mujoco, mjwarp, vision, olfaction, biomechanical-simulation, hierarchical-control, gpu, open-source, nely-epfl]
---

**NeuroMechFly** — anatomically detailed digital-twin simulator of the adult *Drosophila melanogaster*, built and maintained by [EPFL's NeLy lab](nely-epfl.md). The current v2 line couples the body model with **vision, olfaction, mechanosensory feedback, and an explicit brain↔VNC hierarchical control architecture** ([website](../sources/neuromechfly-website.md), [GitHub](../sources/flygym-github.md)). Apache-2.0 licensed; the Python package is named `flygym`.

> [!note] The wiki previously labelled this entity as a *predecessor* to flybody. That framing is wrong as of 2026: NeuroMechFly v2 is a **contemporary peer** with **active development** ([flygym v2.0.1 released 2026-04-17](../sources/flygym-github.md)) and a different capability profile (olfaction + brain–VNC; no flight). flybody (HHMI Janelia + DeepMind) and NeuroMechFly v2 (EPFL NeLy) are best read as parallel open-source body sims with complementary strengths.

## Versions

| Version | Year | Reference | Capabilities | Notes |
|---|---|---|---|---|
| v1 | 2022 | Lobato-Rios et al., *Nat. Methods* 19:620–627 | Walking + grooming | Heuristic low-level controller |
| v2 (paper) | 2024 | Wang-Chen et al., *Nat. Methods* 21:2353–2362 | + vision + olfaction + brain–VNC hierarchy + learnt high-level controller | The paper-grade reference for v2 |
| v2.x.x (flygym package) | 2026-03 → present | Codebase rewrite ([flygym GitHub](../sources/flygym-github.md)) | + Warp/MJWarp GPU acceleration, redesigned API | **Not backward-compatible with v1.x.x** |
| v1.x.x (legacy package) | maintained | [`flygym-gymnasium`](https://github.com/NeLy-EPFL/flygym-gymnasium); docs at `gymnasium.neuromechfly.org` | v1 capabilities | Migrated to a separate repo when v2.x.x landed |

## Capabilities (v2)

- **Body model** — anatomically detailed adult female fly from micro-CT.
- **Locomotion** — walking over challenging terrain; leg adhesion enables vertical/overhead locomotion.
- **Vision** — compound eyes; ommatidia on a hexagonal lattice. (The same anatomical motif [flyvis](flyvis.md)'s hex-CNN is built around.)
- **Olfaction** — odor receptors in antennae and maxillary palps. **Unique among open-source fly body sims.**
- **Mechanosensory feedback** — joint angles, actuator forces, contact forces, anatomical positions.
- **Hierarchical control** — Brain ↔ Ventral Nerve Cord with explicit descending/ascending representations.
- **No flight.** Flight is currently the unique reach of [flybody](flybody.md).

## Stack

- **Physics:** [MuJoCo](mujoco.md), with optional **Warp / MJWarp** GPU backend (NVIDIA Warp is the same compute layer the [Newton physics engine](newton-physics-engine.md) is built on).
- **Language:** Python 99%+. Apache-2.0.
- **Distribution:** PyPI `flygym`; install instructions at [neuromechfly.org/installation](https://neuromechfly.org/installation).
- **Documentation:** [neuromechfly.org](https://neuromechfly.org/) for v2; `gymnasium.neuromechfly.org` for v1 legacy.

## Performance (v2 vs v1)

- **CPU:** ~10× speed-up; ~2× real-time throughput.
- **GPU:** ~300× speed-up via Warp/MJWarp; ~60× real-time throughput.

## Position vs flybody

| Axis | NeuroMechFly v2 (NeLy / EPFL) | [flybody](flybody.md) (HHMI Janelia + DeepMind) |
|---|---|---|
| Locomotion | Walking + leg adhesion | Walking + leg adhesion |
| **Flight** | — | **✓ phenomenological aerodynamics + WPG** |
| Vision | Compound eyes (ommatidia hex lattice) | Eye cameras (vision-driven flight) |
| **Olfaction** | **✓ antennae + maxillary palps** | — |
| Mechanosensory | ✓ explicit joint / actuator / contact | Largely idealized |
| **Brain–VNC architecture** | **✓ descending + ascending representations** | Flat MLP/CNN policies |
| RL stack | Not surveyed in this pass | DMPO + Acme + Reverb + Ray |
| GPU backend | ✓ Warp / MJWarp | — (CPU-distributed via Ray) |
| License | Apache-2.0 | Apache-2.0 |
| Lab | NeLy / EPFL (Switzerland) | HHMI Janelia + Google DeepMind (US/UK) |

The two projects are best read as **complementary**, not competitive. A serious whole-organism researcher would likely use NeuroMechFly for sensing-rich, walking-domain experiments and flybody for flight or vision-guided aerial navigation.

## Lineage

Bread-crumb in the **biomechanical-simulation lineage** that runs *C. elegans* (Boyle 2012) → Hydra (Wang 2023) → virtual rodent (Merel 2020) → NeuroMechFly v1/v2 → flybody (Vaxenburg 2025). See [Biomechanical simulation](../concepts/biomechanical-simulation.md).

## Why it matters here

- **Sensing-rich body for whole-organism agentic AI.** NeuroMechFly v2's olfaction + mechanosensory channels open up sensor modalities that flybody can't currently deliver. For brain-side controllers ([Drosophila brain model](drosophila-brain-model.md), [flyvis](flyvis.md)) the practical question becomes: which body do you couple to, given which sensors your controller cares about? See [Whole-organism agentic AI](../syntheses/whole-organism-agentic-ai.md).
- **Cross-domain Newton-stack consumer.** v2's GPU path uses NVIDIA Warp via MJWarp. Newton (NVIDIA + DeepMind + Disney + Linux Foundation) is built on the same Warp substrate — i.e., the GPU compute layer being commoditized for industrial-robotics simulation also benefits non-robotics biology simulation. Reinforces the [Newton + OpenUSD substrate convergence](../syntheses/newton-openusd-substrate-convergence.md) claim that the physics layer is becoming a shared substrate.
- **Active development.** v2.0.1 in April 2026 puts NeuroMechFly in the same "actively maintained ~1.5 years post-publication" bucket as [flyvis](flyvis.md). The brain-side and body-side artifacts are all currently live software, not abandoned demos.

## Open integrations

- **Connectome ↔ NeuroMechFly.** No coupling exists in the codebase to either a [Drosophila brain model](drosophila-brain-model.md)-style LIF connectome simulation or a [flyvis](flyvis.md)-style connectome-constrained DMN. Same gap as flybody.
- **Newton via NewtonSceneAPI.** Uses Warp directly through MJWarp, not Newton's USD-schema layer. A Newton-on-NeuroMechFly experiment would be additional plumbing, not impossible.

## Related

- [flygym GitHub](../sources/flygym-github.md) — code release source page.
- [neuromechfly.org website](../sources/neuromechfly-website.md) — docs / tutorials source page.
- [NeLy-EPFL](nely-epfl.md) — host lab.
- [flybody](flybody.md) — sister fly body sim (different lab, different capabilities).
- [Drosophila melanogaster](drosophila.md) — shared organism.
- [MuJoCo](mujoco.md) — physics backend.
- [Newton physics engine](newton-physics-engine.md) — adjacent (shared NVIDIA Warp compute layer).
- [Biomechanical simulation](../concepts/biomechanical-simulation.md) — concept umbrella.
- [Whole-organism agentic AI](../syntheses/whole-organism-agentic-ai.md) — synthesis.

## Mentioned in

- [flybody Paper](../sources/flybody-paper.md) — cites v1 + v2 as the walking-and-grooming predecessor line.
- [flygym GitHub](../sources/flygym-github.md) — code release.
- [neuromechfly.org website](../sources/neuromechfly-website.md) — project website.

## Open questions / TBD

- Wang-Chen et al. 2024 *Nat. Methods* paper itself — not yet ingested as its own source page.
- Lobato-Rios et al. 2022 *Nat. Methods* paper — same.
- Tutorial-by-tutorial enumeration of demoed behaviours; current entity captures *architecturally supported* sensors and capabilities, not which end-to-end demos exist.
- Whether anyone has wired NeuroMechFly v2 sensory channels into a connectome-driven controller (Drosophila brain model or flyvis style) — not surfaced in this pass.
