---
title: NeLy-EPFL (Neuroengineering Laboratory)
type: entity
subtype: research-lab
created: 2026-05-08
updated: 2026-05-08
sources: 2
url: https://www.epfl.ch/labs/nely/
tags: [nely, epfl, switzerland, neuroengineering, drosophila, biomechanics, neuromechfly]
---

**NeLy** — the **Neuroengineering Laboratory** at **EPFL** (École polytechnique fédérale de Lausanne), Switzerland. Maintainer of [NeuroMechFly](neuromechfly.md) and the open-source `flygym` Python library ([GitHub](../sources/flygym-github.md), [website](../sources/neuromechfly-website.md)). The European counterweight to HHMI Janelia in the *Drosophila* whole-body simulation thread.

## Confirmed contributions

- **NeuroMechFly v1** (2022, *Nat. Methods*) — first-generation walking + grooming digital fly with anatomically detailed body.
- **NeuroMechFly v2** (2024, *Nat. Methods*) — vision + olfaction + brain–VNC hierarchical control + learnt high-level controller.
- **`flygym` package** (Apache-2.0; v2.0.1 in April 2026) — actively maintained Python library implementing v2 with Warp/MJWarp GPU acceleration.

## Position in the wiki

The wiki's *Drosophila* whole-body simulation thread now has **two parallel open-source labs** producing complementary platforms:

| Lab | Country | Body sim | Capability split |
|---|---|---|---|
| [HHMI Janelia](hhmi-janelia.md) (Turaga / Tassa) | US / UK | [flybody](flybody.md) | Walking + flight; flat policies |
| **NeLy / EPFL** | Switzerland | [NeuroMechFly](neuromechfly.md) | Walking + olfaction + brain–VNC hierarchy |

Both projects use [MuJoCo](mujoco.md), both are Apache-2.0, both ship in 2024–2026 with active follow-on releases. The "next decade of fly modelling" Vaxenburg et al. invoke in their flybody discussion section is unfolding across two institutions in parallel, not one.

## Related

- [NeuroMechFly](neuromechfly.md) — primary product.
- [flybody](flybody.md) — analogous platform from a different lab.
- [HHMI Janelia](hhmi-janelia.md) — peer institution on the same problem.
- [Drosophila melanogaster](drosophila.md) — shared organism.

## Mentioned in

- [flygym GitHub](../sources/flygym-github.md)
- [neuromechfly.org website](../sources/neuromechfly-website.md)

## Open questions / TBD

- **PI** — the wiki has not confirmed the lab's PI in this pass; commonly listed as Pavan Ramdya, but not surfaced from a primary source ingested here. To be filed if the thread continues.
- **Other NeLy projects** outside the *Drosophila* thread.
