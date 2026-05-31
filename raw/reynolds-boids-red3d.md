# Boids (Craig Reynolds) — red3d.com/cwr/boids/

> Raw capture (markdown extraction via WebFetch) of https://www.red3d.com/cwr/boids/
> Fetched 2026-05-31. Author: Craig Reynolds. Page is continuously maintained.

## Creator and Origin
Craig Reynolds developed the boids model in 1986 as "a computer model of coordinated
animal motion such as bird flocks and fish schools."

## What Are Boids?
Boids are "the generic simulated flocking creatures" based on three-dimensional
computational geometry. The model demonstrates how complex group behavior emerges
from simple individual rules.

## Three Core Steering Behaviors
1. **Separation**: "steer to avoid crowding local flockmates"
2. **Alignment**: "steer towards the average heading of local flockmates"
3. **Cohesion**: "steer to move toward the average position of local flockmates"

Each boid only responds to neighbors within a defined distance and angle range,
creating a limited perception neighborhood.

## Historical Development
The foundational work was published as "Flocks, Herds, and Schools: a Distributed
Behavioral Model" at SIGGRAPH '87. Reynolds collaborated with colleagues at Symbolics
Graphics Division and Whitney/Demos Productions to create the animated short
*Stanley and Stella in: Breaking the Ice*, first shown at SIGGRAPH '87's Electronic
Theater.

## Film and Media Applications
**Batman Returns** (1992) became the first major film using modified boids software for
bat swarms and penguin flocks. Andy Kopra created realistic bat imagery while Andrea
Losch and Paul Ashdown produced penguin animations.

## Key Concepts
Reynolds notes that boids demonstrate "emergence: where complex global behavior can
arise from the interaction of simple local rules." The model exhibits unpredictable
moderate-term behavior while remaining predictable at short timescales — characteristic
of systems "poised at the edge of chaos," as Chris Langton observed.

## Technical Notes
The straightforward algorithm carries O(n^2) complexity; spatial data structures can
reduce this to nearly O(n), enabling real-time simulations of large flocks.
