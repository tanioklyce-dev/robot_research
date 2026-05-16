---
title: "neuromechfly.org (project website)"
type: source
subtype: project-website
created: 2026-05-08
updated: 2026-05-08
url: https://neuromechfly.org/
author: Neuroengineering Laboratory (NeLy), EPFL
published: 2024-onwards
ingested: 2026-05-08
tags: [neuromechfly, flygym, drosophila, mujoco, vision, olfaction, biomechanical-simulation, project-website, tutorials]
---

## Summary

Project website for [NeuroMechFly](../entities/neuromechfly.md) — the *Drosophila melanogaster* digital-twin simulator from EPFL's [NeLy lab](../entities/nely-epfl.md). Hosts the documentation, tutorials, paper links, and installation guide for the [flygym](../sources/flygym-github.md) Python library. Tagline: *"can see, smell, walk over challenging terrain, and interact with the environment."*

## Key surfaces on the site

### Versioning landscape
- **v2.x.x** — current. Launched **March 2026** as a complete rewrite. Improved scene composition, interactive viewer, simplified dependencies, GPU acceleration. Documentation lives at the main `neuromechfly.org` domain.
- **v1.x.x** — legacy. Migrated to a separate package [`flygym-gymnasium`](https://github.com/NeLy-EPFL/flygym-gymnasium); documentation at `gymnasium.neuromechfly.org`.

### Capability claims
The model "can see, smell, walk over challenging terrain, and interact with the environment." Concretely this expands into:
- **Locomotion:** walking over challenging terrain.
- **Vision:** compound eyes; ommatidia on hexagonal lattice.
- **Olfaction:** odor receptors in antennae and maxillary palps.
- **Leg adhesion:** vertical / overhead surfaces.
- **Mechanosensory feedback:** joint angles, actuator forces, contact forces.
- **Hierarchical control:** explicit Brain–VNC architecture with descending/ascending representations.

### Performance benchmarks
- CPU: ~10× speed-up over v1 → ~2× real-time throughput.
- GPU (Warp / MJWarp): ~300× speed-up → ~60× real-time throughput.

### Resources surfaced
- **Primary paper:** NeuroMechFly v2 in *Nature Methods* (2024) — referenced from the website.
- **Tutorials:** model composition, experimental replay, GPU acceleration, interactive viewer.
- **Installation guide** at `neuromechfly.org/installation`.
- **Code:** [NeLy-EPFL/flygym](https://github.com/NeLy-EPFL/flygym) — see [companion source page](flygym-github.md).

## Companion papers (referenced via the site, not yet ingested as their own source pages)

- **Lobato-Rios et al. 2022** *Nat. Methods* 19:620–627 — NeuroMechFly v1.
- **Wang-Chen et al. 2024** *Nat. Methods* 21:2353–2362 — NeuroMechFly v2.

## What this source uniquely adds vs the GitHub readme

- **Versioning narrative** — that v1 was migrated out to a separate package, not deprecated. Two live URLs (`neuromechfly.org` for v2, `gymnasium.neuromechfly.org` for v1).
- **Curriculum framing** — the tutorial set tells you what NeLy thinks the platform is *for*, beyond just the README's feature list.
- **Capability tagline** — "see, smell, walk, interact" is the project's own one-line summary; useful as a citation source.

## Entities mentioned

- [NeuroMechFly](../entities/neuromechfly.md) — the platform.
- [NeLy-EPFL](../entities/nely-epfl.md) — host laboratory.
- [Drosophila melanogaster](../entities/drosophila.md) — model organism.
- [MuJoCo](../entities/mujoco.md) — physics engine.

## Concepts touched

- [Biomechanical simulation](../concepts/bio/biomechanical-simulation.md) — most-actively-developed *Drosophila* sim in this lineage.

## Open questions

- **Tutorial details** — content fetched here was the home page. A targeted ingest of the tutorials index would let the wiki claim concretely what behaviours are demoed end-to-end vs. only architecturally supported.
- **Wang-Chen 2024 *Nature Methods* paper itself** — referenced but not ingested. Worth filing if this thread continues.
