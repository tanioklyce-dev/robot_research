---
title: "A cellular platform for the development of synthetic living machines (Blackiston et al. 2021)"
type: source
url: https://www.science.org/doi/10.1126/scirobotics.abf1571
author: Douglas Blackiston, Emma Lederer, Sam Kriegman, Simon Garnier, Josh Bongard, Michael Levin
affiliations: Tufts University (Allen Discovery Center); Wyss Institute, Harvard; New Jersey Institute of Technology (Garnier); University of Vermont (Kriegman, Bongard)
venue: Science Robotics 6(52):eabf1571
published: 2021-03-31
ingested: 2026-05-31
format: gated-html
license: subscription (Science Robotics)
tags: [artificial-life, alife, xenobots, reconfigurable-organisms, cilia, self-organization, biohybrid, soft-robotics, voxcraft, emergence]
---

> [!note] Gated source — abstract-level ingest
> The full text is paywalled (Science Robotics; HTTP 403 on the article + ePDF). This page is built from the **abstract, citation metadata, and the companion [IEEE EMBS feature](embs-xenobots-self-replicate-feature.md)** — not the full methods/results. Treat specifics as provisional pending full-text access.

## Summary

The **"Xenobots 2.0"** paper. Where the [original 2020 pipeline](kriegman-2020-reconfigurable-organisms.md) built reconfigurable organisms by **manually sculpting** frog tissue and adding **cardiac (contractile) muscle** for actuation, this paper introduces a **cellular platform** in which **amphibian embryonic explants self-assemble into motile living machines that locomote via surface cilia** — no sculpting of a muscle actuator required. The result is a more **self-organizing, plastic** route to xenobots, exploiting *emergent* self-organization and functional plasticity rather than imposed structure. These cilia-driven spheroids are the substrate later shown to **[kinematically self-replicate](kriegman-2021-kinematic-self-replication.md)**.

## Key claims (from abstract + secondary coverage)

- **Motivation.** Robot swarms have to date been built from artificial materials, and prior motile biological constructs relied on **muscle cells grown on precisely shaped scaffolds**; exploiting **emergent self-organization + functional plasticity** in a self-directed living machine had remained an open challenge.
- **Method.** A method to generate **in vitro biological robots from frog (*Xenopus laevis*) cells** via embryonic explants that self-assemble.
- **Locomotion mechanism.** These xenobots exhibit **coordinated locomotion via cilia** present on their surface — a shift from the cardiomyocyte-pushing actuation of the 2020 organisms. (Cilia were the feature *suppressed* in the 2020 study; here they are the motor.)
- **Tooling.** Associated computational modeling used the **Voxcraft-sim** GPU soft-body physics engine (per the reference list).
- **Significance.** Establishes the **self-organizing, cilia-driven xenobot** as a reusable platform — the bridge between the AI-designed-and-sculpted 2020 organisms and the 2021 self-replication result.

## Entities mentioned
- [Xenobots / reconfigurable organisms](../entities/xenobots.md) — this paper's cilia-driven self-assembling variant ("2.0").
- [Sam Kriegman](../entities/sam-kriegman.md), [Josh Bongard](../entities/josh-bongard.md), [Michael Levin](../entities/michael-levin.md) — recurring author team.
- Douglas Blackiston (lead), Emma Lederer, **Simon Garnier** (NJIT; collective-behavior / swarm researcher). *(No standalone pages.)*

## Concepts touched
- [Artificial life and the emergence of self-replication](../concepts/alife/artificial-life-and-self-replication.md) — the self-organization / emergence side.
- Self-organization, functional plasticity, cilia-driven locomotion, soft-body simulation (Voxcraft).

## Open questions
- Full methods/results not captured (gated): exact lifespan, payload, self-repair quantification, and how robustly the self-assembled forms transfer from sim.
- Relationship of Garnier's **collective-behavior/swarm** expertise to the multi-organism dynamics — would connect to the wiki's [swarm intelligence](../concepts/robotics/swarm-intelligence.md) and [flocking/boids](../concepts/alife/flocking-and-boids.md) pages if the full text were accessible.
