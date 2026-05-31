---
title: Xenobots (reconfigurable organisms)
type: entity
subtype: robot
created: 2026-05-31
updated: 2026-05-31
sources: 3
tags: [xenobots, reconfigurable-organisms, artificial-life, biohybrid, soft-robotics, self-replication, evolutionary-computation, morphogenesis]
---

**Xenobots** (the authors' own term is **"reconfigurable organisms"**) are **AI-designed living machines** built from the pluripotent stem cells of the African clawed frog *Xenopus laevis* (hence "Xeno-"). They are neither traditional robots (no metal/electronics) nor standard organisms (they bear little resemblance above the cellular level to any frog) — a novel **biohybrid / artificial-life** category: bodies designed *in silico* by an evolutionary algorithm and instantiated *in vivo* from frog cells.

## What they are
- **Cell types:** passive **epidermal** tissue + contractile **cardiac** (cardiomyocyte) tissue, or — in the self-replication work — cilia-driven epidermal **spheroids**. No nervous system, no genetic modification of behavior.
- **Construction:** harvest pluripotent cells from blastula-stage *Xenopus* embryos → pool/incubate → **manually sculpt** with microsurgery forceps + a 13-μm cautery electrode into the evolved shape ([Kriegman 2020](../sources/kriegman-2020-reconfigurable-organisms.md)).
- **Lifespan:** self-locomote for days–weeks on maternal energy stores; **naturally self-limiting** (no metabolic engineering) — framed as a built-in safety feature.

## Capabilities
- **Locomotion, object manipulation, object transport, collective behavior** ([Kriegman 2020](../sources/kriegman-2020-reconfigurable-organisms.md)).
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

## Mentioned in
- [Kriegman et al. 2020 — A scalable pipeline for designing reconfigurable organisms](../sources/kriegman-2020-reconfigurable-organisms.md)
- [Kriegman et al. 2021 — Kinematic self-replication in reconfigurable organisms](../sources/kriegman-2021-kinematic-self-replication.md)
- [BFF — Emergent Complexity experiment (Jonas Werner)](../sources/jonas-werner-bff-emergent-complexity.md) — cites Xenobots as a biological emergence cousin.
