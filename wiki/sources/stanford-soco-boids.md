---
title: "Boids — Stanford SoCo student project (Wong, 2008)"
type: source
url: https://cs.stanford.edu/people/eroberts/courses/soco/projects/2008-09/modeling-natural-systems/boids.html
local_path: raw/stanford-soco-boids-2008.md
author: Timmie Wong
published: 2008-09
ingested: 2026-05-31
format: web
tags: [artificial-life, alife, emergence, flocking, boids, swarm-intelligence, ant-colony-optimization, swarm-robotics, agent-based-model]
---

## Summary

A Stanford "Sociology of Computing" (SoCo) **student write-up of boids** (Timmie Wong, Sept 2008) in Eric Roberts' course. It restates Craig Reynolds' three flocking rules and frames boids explicitly as an **artificial-life** example whose value is pedagogical: simple local rules → emergent group complexity. Its distinctive contribution to the wiki is **placing boids inside the broader swarm-intelligence family** — connecting it forward to ant colony optimization and swarm robotics.

## Key claims

- **Boids = ALife flocking model by Craig Reynolds.** The system specifies simple *individual* rules rather than choreographing the whole flock; realistic group dynamics emerge, suitable for computer animation.
- **The three rules** (as stated on the page):
  - **Separation** — each bird maintains a reasonable distance from nearby birds to prevent overcrowding.
  - **Alignment** — birds match their heading to the average direction of neighbors.
  - **Cohesion** — each bird moves toward the average position of nearby birds.
- **Per-boid state** = position, velocity, orientation; the three rules are applied algorithmically each step. **Obstacle avoidance** is a common extension.
- **Emergence framing.** Short-term motion is orderly/predictable; long-term flock behavior is unpredictable — the recurring "complexity from simple rules" lesson.
- **Swarm-intelligence connections** (the page's added breadth):
  - **Swarm intelligence** — decentralized systems where units follow local rules with no central control.
  - **Ant colony optimization** — pheromone trails + positive feedback to find optimal paths.
  - **Swarm robotics** — small robot groups using swarm-intelligence rules for mapping, foraging, etc.

## Entities mentioned
- [Craig Reynolds](../entities/craig-reynolds.md) — creator of boids.
- Timmie Wong — page author (student).

## Concepts touched
- [Flocking and boids](../concepts/alife/flocking-and-boids.md) — the concept this source anchors; this source supplies the swarm-intelligence / swarm-robotics framing.
- [Agentic UAVs](../concepts/robotics/agentic-uavs.md) — swarm robotics is the applied-robotics neighbor of boids.

## Open questions
- Secondary student source — no novel claims beyond Reynolds; treat as corroborating + framing, not authoritative on implementation detail. For the authoritative version see the primary source: [Reynolds 1987](reynolds-flocks-herds-schools-1987.md).
- The page references pseudocode it doesn't fully reproduce; a concrete reference implementation (e.g. for a curriculum demo) is not yet captured in the wiki.
