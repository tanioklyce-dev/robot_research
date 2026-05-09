---
source_url: https://ovmm.github.io/
collected: 2026-05-09
published: Unknown (2024 era)
author: Yenamandra, Ramachandran, Yadav et al.
affiliation: Georgia Tech, Meta AI, CMU, Simon Fraser University
---

# HomeRobot: Open Vocabulary Mobile Manipulation (OVMM)

## What is OVMM
"Picking any object in any unseen environment, and placing it in a commanded location." Integrates perception, language understanding, navigation, and manipulation for household tasks specified in natural language.

## Hardware
Hello Robot Stretch (affordable, compliant mobile manipulator).

## Task format
"Move the [object] from the [start receptacle] to the [goal receptacle]"

## Benchmark
- Simulation: 50 initial scenes, thousands of episodes, multi-room home environments. Seen vs. unseen objects.
- Real world: deployed on Hello Robot Stretch.

## Results
- 20% success rate in real world (baseline)
- Demonstrates sim-to-real transfer via both RL and heuristic model-based approaches.

## Framing
"A foundational challenge for robots to be useful assistants in human environments" — simultaneously addresses perception, language, navigation, and manipulation.
