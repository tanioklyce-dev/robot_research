---
title: Xenobots (reconfigurable organisms)
type: entity
subtype: robot
created: 2026-05-31
updated: 2026-05-31
sources: 5
tags: [xenobots, reconfigurable-organisms, artificial-life, biohybrid, soft-robotics, self-replication, evolutionary-computation, morphogenesis]
---

**Xenobots** (the authors' own term is **"reconfigurable organisms"**) are **AI-designed living machines** built from the pluripotent stem cells of the African clawed frog *Xenopus laevis* (hence "Xeno-"). They are neither traditional robots (no metal/electronics) nor standard organisms (they bear little resemblance above the cellular level to any frog) — a novel **biohybrid / artificial-life** category: bodies designed *in silico* by an evolutionary algorithm and instantiated *in vivo* from frog cells.

## What they are
- **Two generations.** *(2020)* AI-designed, **manually sculpted** bodies actuated by layered **cardiac (cardiomyocyte)** muscle pushing against the surface ([Kriegman 2020](../sources/kriegman-2020-reconfigurable-organisms.md)). *(2021 "2.0")* **self-assembling** explants that locomote via **surface cilia** — no sculpting or muscle needed ([Blackiston 2021](../sources/blackiston-2021-cellular-platform-synthetic-living-machines.md)). The cilia-driven spheroids are the substrate used in the self-replication study.
- **Cell types:** passive **epidermal** tissue + contractile **cardiac** tissue (2020), or cilia-driven epidermal **spheroids** (2021). No nervous system, no genetic modification of behavior.
- **Construction:** harvest pluripotent cells from blastula-stage *Xenopus* embryos → pool/incubate → **manually sculpt** with microsurgery forceps + a 13-μm cautery electrode into the evolved shape ([Kriegman 2020](../sources/kriegman-2020-reconfigurable-organisms.md)).
- **Lifespan:** self-locomote for days–weeks on maternal energy stores; **naturally self-limiting** (no metabolic engineering) — framed as a built-in safety feature.

## Capabilities
- **Locomotion, object manipulation, object transport, collective behavior** ([Kriegman 2020](../sources/kriegman-2020-reconfigurable-organisms.md)).
- **Cilia-driven coordinated locomotion via emergent self-organization** (no sculpted muscle actuator) ([Blackiston 2021](../sources/blackiston-2021-cellular-platform-synthetic-living-machines.md)).
- **Self-repair** — spontaneously close lacerations ([Kriegman 2020](../sources/kriegman-2020-reconfigurable-organisms.md)).
- **Kinematic self-replication** — swarms push loose dissociated stem cells into piles that mature into new organisms; **arises spontaneously, not by selection**; AI-designed **C-shaped semitorus** progenitors amplify it from ~2 to up to 4 generations ([Kriegman 2021](../sources/kriegman-2021-kinematic-self-replication.md)).

## Why they matter for this wiki
- The **biological counterpart** to the wiki's code-based self-replication results: where [Computational Life](../sources/computational-life-self-replicating-programs-paper.md) shows self-replicators emerging in a soup of self-modifying programs with no fitness function, Xenobots show **multicellular kinematic self-replication arising spontaneously** in living matter. Both live under [artificial life and the emergence of self-replication](../concepts/alife/artificial-life-and-self-replication.md).
- A concrete instance of **[evolutionary computation](../concepts/alife/evolutionary-computation.md) co-designing morphology + behavior** and transferring sim→bio.
- Referenced as a biological cousin in [Jonas Werner's BFF reproduction post](../sources/jonas-werner-bff-emergent-complexity.md).

## People
- [Sam Kriegman](sam-kriegman.md) & Douglas Blackiston — co-first authors (design/AI; in-vivo construction).
- [Michael Levin](michael-levin.md) — morphogenesis/bioelectricity (Tufts).
- [Josh Bongard](josh-bongard.md) — evolutionary robotics (UVM); senior author.
- Emma Lederer, Simon Garnier (NJIT; collective behavior) — co-authors on the [2021 cellular-platform paper](../sources/blackiston-2021-cellular-platform-synthetic-living-machines.md).

## Mentioned in
- [Kriegman et al. 2020 — A scalable pipeline for designing reconfigurable organisms](../sources/kriegman-2020-reconfigurable-organisms.md)
- [Blackiston et al. 2021 — A cellular platform for synthetic living machines](../sources/blackiston-2021-cellular-platform-synthetic-living-machines.md) (cilia-driven "Xenobots 2.0")
- [Kriegman et al. 2021 — Kinematic self-replication in reconfigurable organisms](../sources/kriegman-2021-kinematic-self-replication.md)
- [AI-Designed Living Robots Can Self-Replicate (IEEE EMBS feature)](../sources/embs-xenobots-self-replicate-feature.md)
- [BFF — Emergent Complexity experiment (Jonas Werner)](../sources/jonas-werner-bff-emergent-complexity.md) — cites Xenobots as a biological emergence cousin.
