---
title: "A scalable pipeline for designing reconfigurable organisms (Kriegman et al. 2020)"
type: source
url: https://www.pnas.org/doi/10.1073/pnas.1910837117
local_path: raw/kriegman-et-al-2020-a-scalable-pipeline-for-designing-reconfigurable-organisms.pdf
sha256: a8f69d619780b94e18117f47ea5c7df6a04aea1ed23404a4d017c49343d271e9
code: https://github.com/skriegman/reconfigurable_organisms
author: Sam Kriegman, Douglas Blackiston, Michael Levin, Josh Bongard
affiliations: University of Vermont (CS); Tufts University (Biology / Allen Discovery Center); Wyss Institute, Harvard
venue: PNAS 117(4):1853–1859
published: 2020-01-13
ingested: 2026-05-31
format: pdf
license: CC BY 4.0
tags: [artificial-life, alife, evolutionary-computation, xenobots, reconfigurable-organisms, bioengineering, self-organization, emergence, morphogenesis, soft-robotics, sim-to-real]
---

## Summary

The **original Xenobots paper**. Kriegman, Blackiston, Levin & Bongard demonstrate a **scalable pipeline that designs novel living machines in silico and builds them out of frog cells in vivo**. An **evolutionary algorithm** searches over arrangements of two cell types — passive (epidermal) and contractile (cardiac) "voxels" — inside a soft-body physics simulator to achieve a target behavior (e.g. locomotion); the best, **noise-robust, buildable** designs are then manufactured by harvesting and microsurgically shaping pluripotent stem cells from *Xenopus laevis* embryos. The resulting **"reconfigurable organisms"** (later dubbed **Xenobots**) self-locomote, manipulate/transport objects, exhibit collective behavior, and **self-repair** — despite having no nervous system and bearing little resemblance to any existing organism. It's a concrete demonstration of **AI-designed, biologically-instantiated artificial life**.

## Key claims

- **Generator-and-filter pipeline.** (1) Evolutionary algorithm generates diverse candidate body designs in a soft-body physics sim, scored on a behavioral goal; (2) **robustness filter** keeps only designs whose behavior survives random actuation noise (noise-resistance in sim predicts real-world transfer); (3) **build filter** removes designs that can't be physically realized (minimal concavity size) or won't scale (proportion of passive tissue). Discrepancies between in-silico and in-vivo behavior are fed **back as constraints** to the next evolutionary round.
- **Evolved, not learned, morphology.** Evolutionary search (not gradient learning) is used precisely because it can **co-design physical structure *and* behavior** — and produces a *diversity* of solutions, useful because some are more buildable than others. 100 independent EA trials per goal, with lineage-competition diversity pressure.
- **Manufacture from frog cells.** Pluripotent stem cells harvested from blastula-stage *Xenopus laevis* embryos, pooled, incubated, then **manually sculpted** with forceps + a 13-μm cautery electrode into a 3D approximation of the evolved design; contractile cardiac-progenitor tissue is layered in to provide actuation. Organisms move for **days–weeks with no added nutrients** (maternal energy stores).
- **Four behaviors realized:** locomotion, object manipulation (spontaneous debris aggregation), object transport (an evolved drag-reducing hole exapted into a payload pouch), and collective behavior (organisms collide, bond, orbit, entangle).
- **Cilia suppressed** in vivo (via Notch-ICD mRNA microinjection) so that displacement comes only from modeled cardiac contraction — simplifying the sim-to-real comparison. Successful directional transfer confirmed for upright (but not inverted) designs (P < 0.01).
- **Emergent self-organization aids the design.** Cardiomyocytes spontaneously phase-match their contractions (not enforced in sim); organisms **self-repair lacerations**; morphology evolves to "derandomize" the random per-cell actuation into coherent global motion.
- **Proposed applications:** targeted drug delivery, internal microsurgery, environmental remediation, sensing — with a built-in **safety feature**: no metabolic engineering ⇒ naturally limited lifespan.

## Entities mentioned
- [Xenobots / reconfigurable organisms](../entities/xenobots.md) — the artifact this paper introduces.
- [Sam Kriegman](../entities/sam-kriegman.md) — co-first author (then UVM PhD; evolutionary design + AI).
- Douglas Blackiston — co-first author (Tufts developmental biologist; did the in-vivo construction).
- [Michael Levin](../entities/michael-levin.md) — Tufts/Allen Discovery Center; morphogenesis & bioelectricity.
- [Josh Bongard](../entities/josh-bongard.md) — UVM; evolutionary robotics; senior author.

## Concepts touched
- [Artificial life and the emergence of self-replication](../concepts/alife/artificial-life-and-self-replication.md) — the wiki branch this anchors on the *biological* side.
- [Evolutionary computation](../concepts/alife/evolutionary-computation.md) — the search method that designs the organisms.
- Sim-to-real transfer, soft-body simulation, self-organization, morphogenesis.

## Open questions
- How far can the pipeline be **fully automated** (the construction step is still manual microsurgery)?
- The 2020 paper notes "if equipped with reproductive systems … they may be capable of [scaling]" — directly set up by the [2021 self-replication paper](kriegman-2021-kinematic-self-replication.md).
- Generality beyond *Xenopus laevis* cells and the four demonstrated behaviors is "as of yet unknown."
