---
source_url: https://news.mit.edu/2025/ai-enabled-control-system-helps-autonomous-drones-uncertain-environments-0609
collected: 2026-05-09
published: 2025-06-09
author: Adam Zewe (reporter); Navid Azizan, Sunbochen Tang, Haoyuan Sun (researchers)
affiliation: MIT
---

# AI-Enabled Control System Helps Autonomous Drones Stay on Target in Uncertain Environments

## Summary
MIT researchers developed a meta-learning + mirror descent adaptive control algorithm for drone trajectory tracking under unpredictable environmental disturbances (wind). Learns from 15 min of flight data; no advance knowledge of disturbance structure required.

## Key results
- 50% less trajectory tracking error than baseline methods (simulation)
- Performance advantage grows as wind intensity increases
- Works on wind speeds not seen during training
- Validated in real-world experiments (not just simulation)

## Technical approach
- Combines meta-learning with adaptive control
- Neural network approximates unknown environmental disturbance from observed data
- Uses mirror descent family (not just gradient descent) — algorithm automatically selects the mirror-descent function best suited to the disturbance geometry
- Neural network and mirror function persist across flights without recomputation

## Innovation
Unlike standard gradient descent, leverages the full mirror descent family to match optimization algorithm to problem geometry. The automatic selection is the key novelty.

## Authors
- Navid Azizan (senior) — Esther and Harold E. Edgerton Assistant Professor, MIT Mechanical Engineering; IDSS; LIDS
- Sunbochen Tang (lead) — MIT Aeronautics and Astronautics grad student
- Haoyuan Sun — MIT EECS grad student

## Paper
"Meta-Learning for Adaptive Control with Automated Mirror Descent" — arXiv (not 2506.08045; separate paper). Presented at Learning for Dynamics and Control Conference.

## Funding
MathWorks, MIT-IBM Watson AI Lab, MIT-Amazon Science Hub, MIT-Google Program for Computing Innovation.

## Future work
- Hardware experiments on real drones
- Multiple simultaneous disturbance sources (wind + payload shifting)
- Continual learning without retraining on historical data
