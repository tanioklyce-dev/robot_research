---
title: "AI-Enabled Control System Helps Autonomous Drones Stay on Target in Uncertain Environments"
type: source
url: https://news.mit.edu/2025/ai-enabled-control-system-helps-autonomous-drones-uncertain-environments-0609
author: Adam Zewe (reporter)
affiliations: MIT News
published: 2025-06-09
ingested: 2026-05-09
tags: [drone, adaptive-control, meta-learning, mirror-descent, mit, trajectory-tracking, wind]
---

## Summary
MIT News article covering a meta-learning adaptive control algorithm for drone trajectory tracking under unpredictable wind disturbances. The key innovation is automatic selection of the optimal mirror-descent optimization algorithm for the specific disturbance geometry — rather than assuming gradient descent or a fixed structure. Learns from 15 minutes of flight data. Paper: "Meta-Learning for Adaptive Control with Automated Mirror Descent," presented at Learning for Dynamics and Control Conference.

## Key claims

- **50% less trajectory tracking error** than baseline methods in simulation; advantage grows with wind intensity.
- Handles wind speeds **not seen during training** — generalizes beyond training distribution.
- Learns from **15 minutes of flight data** — minimal data requirement.
- Neural network and mirror function persist across flights; no recomputation needed per flight.
- Validated in real-world experiments, not just simulation.

## Technical approach
- **Meta-learning** — learns how to adapt quickly from minimal observations; no advance knowledge of disturbance structure required.
- **Mirror descent family** — instead of standard gradient descent, automatically selects the mirror-descent function (from a library of options) that best matches the geometry of the specific disturbance encountered.
- **Neural network** — approximates the unknown environmental disturbance from observed flight data.

The mirror-descent selection is the core novelty: different disturbance geometries (e.g., smooth wind vs. turbulent gusts) call for different optimization landscapes; this system identifies and applies the right one automatically.

## Authors
- **Navid Azizan** (senior) — Esther and Harold E. Edgerton Assistant Professor, MIT Mechanical Engineering; IDSS; LIDS
- **Sunbochen Tang** (lead) — MIT Aeronautics and Astronautics PhD student
- **Haoyuan Sun** — MIT EECS PhD student

## Funding
MathWorks, MIT-IBM Watson AI Lab, MIT-Amazon Science Hub, MIT-Google Program for Computing Innovation.

## Future work
- Hardware drone experiments beyond simulation
- Multiple simultaneous disturbance sources (wind + payload shifting)
- Continual learning — adaptation without retraining on historical data

## Related prior work from same group
[Learning Control-Oriented Dynamical Structure from Data](learning-control-oriented-dynamical-structure.md) (Richards, Slotine, Azizan, Pavone — ICML 2023) — Azizan's earlier work on learning SDC factorizations for SDRE-based nonlinear tracking. Complements this paper: that paper addresses model learning; this paper addresses runtime disturbance rejection.

## Entities mentioned
- [Navid Azizan](../entities/navid-azizan.md) — senior author
- [Agentic UAVs](../concepts/agentic-uavs.md) — domain context

## Open questions
- arXiv ID for the underlying paper not provided in the article.
- Performance numbers are simulation-based; real-world quantitative results not yet published.
- Applicable to fixed-wing UAVs or only multirotor?
