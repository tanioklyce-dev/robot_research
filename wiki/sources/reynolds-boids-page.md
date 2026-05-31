---
title: "Boids (Craig Reynolds) — red3d.com"
type: source
url: https://www.red3d.com/cwr/boids/
local_path: raw/reynolds-boids-red3d.md
author: Craig Reynolds
published: 1995 (page); model 1986; paper SIGGRAPH '87
ingested: 2026-05-31
format: web
tags: [artificial-life, alife, emergence, flocking, boids, swarm, agent-based-model, computer-animation, edge-of-chaos, craig-reynolds]
---

## Summary

Craig Reynolds' own canonical page for **boids** — his 1986 "computer model of coordinated animal motion such as bird flocks and fish schools." The page is the primary-source definition of the model: each simulated creature ("boid") is an autonomous agent steering by **three simple local rules**, and realistic, complex flock motion **emerges** from their interaction with no central choreography. It is the founding artifact of agent-based flocking and a touchstone example of emergence "from the interaction of simple local rules."

## Key claims

- **Origin.** Reynolds created the boids model in **1986**; "boids" = "the generic simulated flocking creatures," built on 3D computational geometry.
- **The three steering behaviors** (each computed only over *local* flockmates within a distance/angle neighborhood):
  - **Separation** — steer to avoid crowding local flockmates.
  - **Alignment** — steer towards the average heading of local flockmates.
  - **Cohesion** — steer to move toward the average position of local flockmates.
- **Seminal publication.** "**Flocks, Herds, and Schools: a Distributed Behavioral Model**," **SIGGRAPH '87** (*Computer Graphics* 21(4)). The original distributed behavioral model.
- **First animation.** ***Stanley and Stella in: Breaking the Ice***, made with Symbolics Graphics Division + Whitney/Demos Productions, premiered at the **SIGGRAPH '87** Electronic Theater.
- **First feature-film use.** ***Batman Returns* (1992)** used modified boids software for bat swarms and penguin flocks (Andy Kopra — bats; Andrea Losch & Paul Ashdown — penguins).
- **Emergence thesis.** Boids demonstrate "**emergence**: where complex global behavior can arise from the interaction of simple local rules." Behavior is predictable short-term but unpredictable over the moderate term — characteristic of systems "**poised at the edge of chaos**" (citing **Chris Langton**).
- **Computational complexity.** The naive algorithm is **O(n²)** (every boid checks every other); **spatial data structures** reduce it to nearly **O(n)**, enabling real-time large flocks.

## Entities mentioned
- [Craig Reynolds](../entities/craig-reynolds.md) — creator of the boids model.
- Chris Langton — coined "edge of chaos"; cited for the model's dynamical character.
- Symbolics Graphics Division; Whitney/Demos Productions (production collaborators).

## Concepts touched
- [Flocking and boids](../concepts/alife/flocking-and-boids.md) — the concept this source anchors.
- [Artificial life and the emergence of self-replication](../concepts/alife/artificial-life-and-self-replication.md) — the broader ALife/emergence branch.

## Open questions
- The page asserts "edge of chaos" qualitatively; the wiki has no quantitative dynamical-systems analysis of boids parameter regimes yet.
- Reynolds' later **steering-behaviors** taxonomy (seek, flee, pursue, wander, path-following, etc.) extends boids to general autonomous-agent navigation — not yet ingested.
