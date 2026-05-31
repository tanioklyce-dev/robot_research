---
title: "Flocks, Herds, and Schools: A Distributed Behavioral Model (Reynolds, 1987)"
type: source
url: https://www.red3d.com/cwr/papers/1987/boids.html
local_path: raw/SIGGRAPH87.pdf
author: Craig W. Reynolds
affiliation: Symbolics Graphics Division
published: 1987-07
ingested: 2026-05-31
venue: "SIGGRAPH '87 — Computer Graphics 21(4), July 1987, pp. 25–34 (ed. Maureen C. Stone)"
format: pdf
note: "raw PDF is the 1995 OCR reprint; no illustrations, minor OCR errors"
tags: [artificial-life, alife, emergence, flocking, boids, swarm, agent-based-model, behavioral-animation, particle-system, actor-model, computer-animation, distributed-systems, craig-reynolds]
---

## Summary

The **seminal boids paper** — Reynolds' original SIGGRAPH '87 publication introducing a **distributed behavioral model** for "polarized, non-colliding aggregate motion" (flocks, herds, schools). Rather than scripting each bird's path, the animator instantiates many autonomous **"boids"** (bird-oid objects) that each navigate by **local perception + simple behaviors + simulated flight physics**; realistic flock motion is the *emergent* result of their dense interaction. This is the primary source behind the [Reynolds web page](reynolds-boids-page.md) and the [Stanford write-up](stanford-soco-boids.md), and it is richer and more precise than either — especially on the **original rule names, their strict priority ordering, the arbitration scheme, and the centrality of localized perception**.

## Key claims

- **"boids" = "bird-oid objects"** (explicit footnote etymology) — used generically even for fish/other creatures. A boid is a generalization of a **particle system** (Reeves): a particle replaced by an oriented geometric object ("subobject system"), with its own local coordinate frame. Each boid is an **actor** (Hewitt actor model) — a virtual computer passing messages — implemented in Symbolics Common Lisp **Flavors** (OOP).
- **The three original flocking behaviors, stated "in order of decreasing precedence":**
  1. **Collision Avoidance** — avoid collisions with nearby flockmates (*static*, position-based). → later renamed **separation**.
  2. **Velocity Matching** — match velocity (heading + speed) with nearby flockmates (*dynamic*); "a predictive version of collision avoidance." → later **alignment**.
  3. **Flock Centering** — steer toward the centroid of *nearby* flockmates. → later **cohesion**.
  > [!note] Refinement vs. the popular framing
  > Secondary sources (and Reynolds' own later web page) present these as three co-equal "steering behaviors" named **separation / alignment / cohesion**. The 1987 original gives them a **strict precedence ordering** and explicitly rejects naive equal averaging — see arbitration below. The popular three-rule version is a simplification of this.
- **Arbitration = "prioritized acceleration allocation," not weighted averaging.** Each behavior emits an acceleration request (unit-truncated 3D vector + a [0,1] "strength"). Simple weighted averaging fails: opposing collision-avoidance requests cancel (→ crash into the wall dead ahead), and "fly north" + "fly east" wrongly averages to "fly northeast." Instead, requests are summed **in priority order** into an accumulator until a per-boid **maximum acceleration** budget is spent; the last request is trimmed. Lower-priority urges (e.g. flock centering) go temporarily unsatisfied in emergencies.
- **Localized perception is essential — the paper's key scientific finding.** "The aggregate motion that we intuitively recognize as 'flocking' … *depends upon* a limited, localized view of the world." A **central-force (global) model fails** (whole scattered flock converges to one centroid; can't bifurcate around obstacles). Neighborhood = a spherical **zone of sensitivity** (radius + inverse-exponential falloff); influence weighted by **inverse-square distance** (gravity-like; linear "spring-like" weighting gave an unrealistic bouncy flock). Matches Partridge's fish-school measurements.
- **Constant-time hypothesis.** Natural flocks show **no upper size bound** (herring schools ~17 miles, millions of fish), implying each bird runs a roughly **constant-time** algorithm — aware only of itself, its 2–3 nearest neighbors, and "the rest." A bird is "much more strongly influenced by its near neighbors."
- **Geometric flight.** Incremental translation along local +Z + steering rotations (pitch/yaw); **banking** via roll (coordinated turn); conservation of momentum, viscous speed damping, max-speed/max-acceleration limits. Equivalent to 3D **Logo turtle** geometry.
- **Obstacle avoidance — two methods.** (1) **Force field** (repulsion field): simple but flawed — fails on exact head-on approach, too strong up close / too weak far away. (2) **Steer-to-avoid** (vision-like, preferred): considers only obstacles intersecting the forward axis, aims one body-length past the nearest silhouette edge; implemented for spheres, cylinders, planes, boxes.
- **Scripted vs. impromptu flocking.** A **migratory urge** (global goal point/direction) lets an animator "lead" the flock by animating a goal point ahead of it; momentum smooths abrupt changes. Left alone, boids show **flash expansion**, coalesce into "flockettes," and **bifurcate** around obstacles (which leader/central-force models can't do).
- **Performance (1987).** Symbolics 3600 Lisp Machine; 80 boids = 6,400 comparisons ≈ **95 s/frame**; a 300-frame test ≈ **8 hours**. Naive algorithm is **O(N²)**; proposed fixes = spatial bin partitioning + incremental collision detection toward O(N)/constant time. First version built in **10 days** before SIGGRAPH 86.
- **Predecessors ("Our Foreflocks").** Amkraut/Girard/Karl's *Eurythmy* (SIGGRAPH '85, "force field animation system") and Karl Sims' behavioral animation.
- **Proposed applications.** Fish schools, herds (2D + terrain-following), **traffic flow**, film crowds/"extras," and — notably — **controlled, repeatable scientific study of real flocks** by comparing simulated vs. natural aggregate motion.

## Entities mentioned
- [Craig W. Reynolds](../entities/craig-reynolds.md) — author (Symbolics Graphics Division).
- W. T. Reeves (particle systems), C. Hewitt (actor model), B. L. Partridge / Wayne Potts (fish-school & flock-coordination zoology), Amkraut/Girard/Karl, Karl Sims (predecessor animation).

## Concepts touched
- [Flocking and boids](../concepts/alife/flocking-and-boids.md) — the concept this source primarily anchors (now upgraded from web-page-level to primary-source detail).
- [Artificial life and the emergence of self-replication](../concepts/alife/artificial-life-and-self-replication.md) — emergence from local interaction.
- [Swarm intelligence](../concepts/robotics/swarm-intelligence.md) — boids as the canonical decentralized-collective archetype.

## Open questions
- Reynolds' later, broader **steering-behaviors** taxonomy (seek/flee/pursue/wander/path-following/etc., GDC 1999) generalizes boids to game-AI character navigation — still not ingested.
- The paper proposes **forward-weighted perception** and **vision-based path planning** as future work; modern boids variants and their relationship to learned perception aren't covered in the wiki.
