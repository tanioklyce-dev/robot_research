---
title: "NeLy-EPFL/flygym (GitHub)"
type: source
subtype: code-repository
url: https://github.com/NeLy-EPFL/flygym/
author: Neuroengineering Laboratory (NeLy), EPFL
published: 2026-04-17
ingested: 2026-05-08
license: Apache-2.0
latest_release: v2.0.1 (2026-04-17)
release_count: 18
tags: [neuromechfly, flygym, drosophila, mujoco, mjwarp, nvidia-warp, biomechanical-simulation, vision, olfaction, gpu, open-source]
---

## Summary

Official open-source release of [NeuroMechFly v2](../entities/neuromechfly.md), the *Drosophila melanogaster* digital-twin simulator from EPFL's [Neuroengineering Laboratory (NeLy-EPFL)](../entities/nely-epfl.md). The Python package is named `flygym`; the model and the project are NeuroMechFly. **Apache-2.0 licensed.** **Latest release v2.0.1 on 2026-04-17.** 150 ★ / 23 forks / 18 releases. Repo description: *"A digital twin of the adult fruit fly Drosophila melanogaster that can see, smell, walk over challenging terrain, and interact with the environment."*

The v2.x.x line launched in **March 2026** as a complete rewrite of the v1.x.x library, **not backward-compatible**. The v1.x.x package was migrated to a separate repository, [`NeLy-EPFL/flygym-gymnasium`](https://github.com/NeLy-EPFL/flygym-gymnasium), with documentation at `gymnasium.neuromechfly.org`.

## Key contents (v2)

### Body model
- **Anatomically detailed *Drosophila*** based on micro-CT scan of an adult female fly.
- **Hierarchical control architecture.** Brain ↔ Ventral Nerve Cord (VNC), with explicit **descending and ascending representations** — distinct from flybody's flat MLP-policy approach.
- **Leg adhesion** for vertical-wall and ceiling locomotion (insects need this; mammalian sims don't).

### Sensors
- **Vision.** Compound eyes with ommatidia on a **hexagonal lattice** (the same anatomical motif Lappalainen's [flyvis](../entities/flyvis.md) hex-CNN matches).
- **Olfaction.** Odor receptors in **antennae and maxillary palps**. *No other open-source fly body sim has this — including [flybody](../entities/flybody.md).*
- **Mechanosensory feedback.** Joint angles, actuator forces, contact forces, anatomical positions.

### Performance (v2 vs v1)
- **CPU:** ~10× speed-up over v1, ~2× real-time throughput.
- **GPU:** ~300× speed-up via **Warp/MJWarp**, ~60× real-time throughput. (NVIDIA Warp is the same GPU compute layer that underlies the [Newton physics engine](../entities/newton-physics-engine.md); MJWarp is MuJoCo's Warp-backed implementation.)

### Stack
- **Physics:** [MuJoCo](../entities/mujoco.md), with optional Warp/MJWarp backend for GPU acceleration.
- **Language:** Python (99.4% of repo), Apache-2.0.
- **Distribution:** PyPI package `flygym`. Install instructions at [neuromechfly.org/installation](https://neuromechfly.org/installation).
- **Documentation site:** [neuromechfly.org](https://neuromechfly.org/) — see also [companion source page](neuromechfly-website.md).

### Tutorials (v2)
Per the project website: model composition, experimental replay, GPU acceleration, plus an interactive viewer. (Detailed enumeration deferred — pulled from the website summary, not from a deep tutorial-by-tutorial fetch.)

## What's *not* here

- **No flight.** v2 (and v1) are walking + grooming + sensing platforms. For flight, [flybody](../entities/flybody.md) is the unique open-source choice.
- **No FlyWire/connectome integration in the codebase.** Same situation as flybody and flyvis — the connectome ↔ body coupling is everyone's open problem.
- **No pretrained controllers** mentioned in the README content fetched. (May exist in tutorials; not surfaced here.)
- **No `flygym` ↔ Newton/Isaac Lab integration** — uses MuJoCo + Warp directly, not the Newton wrapper.

## Entities mentioned

- [NeuroMechFly](../entities/neuromechfly.md) — the model/platform.
- [NeLy-EPFL](../entities/nely-epfl.md) — host laboratory.
- [Drosophila melanogaster](../entities/drosophila.md) — model organism.
- [MuJoCo](../entities/mujoco.md) — physics engine.
- [Newton physics engine](../entities/newton-physics-engine.md) — adjacent (shares NVIDIA Warp substrate; not directly used).
- [flybody](../entities/flybody.md) — sister fly body sim (different lab, different capability split).
- [flyvis](../entities/flyvis.md) — adjacent (the optic-lobe DMN whose hex-CNN matches NeuroMechFly's compound-eye anatomy).

## Concepts touched

- [Biomechanical simulation](../concepts/bio/biomechanical-simulation.md) — current state of the art for *Drosophila* with sensing + brain↔VNC architecture.

## Open questions

- **License of v1.** Repo says v1 was migrated to `flygym-gymnasium`; license of that variant not separately verified in this pass.
- **Warp/MJWarp dependency.** The README mentions Warp/MJWarp as the GPU path. Whether v2 ships its own Warp kernels or pulls from MuJoCo's upstream Warp integration was not pulled in this fetch.
- **Connectome coupling.** Has anyone tried driving NeuroMechFly v2 sensory channels (vision, olfaction) into a [Drosophila brain model](../entities/drosophila-brain-model.md)-style LIF brain or a [flyvis](../entities/flyvis.md)-style DMN, and reading motor commands back? Not surfaced anywhere in the wiki yet.
- **Pretrained policies / example datasets** — README content fetched did not enumerate; would benefit from a tutorials/notebooks pass.
