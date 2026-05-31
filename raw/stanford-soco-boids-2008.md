# Boids — Stanford SoCo student project (Timmie Wong, Sept 2008)

> Raw capture (markdown extraction via WebFetch) of
> https://cs.stanford.edu/people/eroberts/courses/soco/projects/2008-09/modeling-natural-systems/boids.html
> Fetched 2026-05-31. Author: Timmie Wong, September 2008. Eric Roberts' SoCo course.

## Overview
This page documents Boids, an artificial life simulation created by Craig Reynolds that
models bird flocking behavior. Rather than controlling entire flocks, the system
specifies simple individual rules that generate complex, realistic group dynamics
suitable for computer animation.

## The Three Core Rules
1. **Separation**: "Each bird attempts to maintain a reasonable amount of distance
   between itself and any nearby birds, to prevent overcrowding."
2. **Alignment**: Birds adjust their heading to match the average direction of
   neighboring birds.
3. **Cohesion**: "Every bird attempts to move towards the average position of other
   nearby birds."

## Technical Implementation
Each boid maintains position, velocity, and orientation. The system implements these
three behavioral rules algorithmically. Pseudocode is referenced but not fully detailed
on this page.

## Emergent Behavior
The simulation demonstrates how simple local rules generate surprising complexity.
Though long-term flock behavior remains unpredictable, short-term motion patterns prove
orderly and predictable. Extensions include obstacle avoidance, allowing boids to
navigate environments while maintaining cohesion.

## Applications & Related Fields
- **Swarm Intelligence**: Decentralized systems where individual units follow local
  rules without central control.
- **Ant Colony Optimization**: Agents finding optimal paths using pheromone trails and
  positive feedback.
- **Swarm Robotics**: Small robot groups programmed with swarm intelligence for tasks
  like mapping and foraging.

## Attribution
Timmie Wong, September 2008.
