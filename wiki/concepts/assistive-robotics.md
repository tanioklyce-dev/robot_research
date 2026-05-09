---
title: Assistive Robotics
type: concept
created: 2026-05-09
updated: 2026-05-09
sources: 7
tags: [assistive-robotics, disability, rehabilitation, exoskeleton, social-robot, accessibility]
---

**Assistive robotics** — the design and deployment of robot systems to help people with disabilities, older adults, or rehabilitation patients regain or extend physical and social capabilities. Distinct from industrial/research robotics in that the primary performance metric is *quality of life and autonomy* for a human user, not task throughput.

## Key categories (from wiki sources)

### Mobile manipulation for daily tasks
- [Stretch](../entities/stretch.md) ([Hello Robot](../entities/hello-robot.md)) — the most documented example in this wiki. $20k; single-arm mobile manipulator; used by Henry Evans (quadriplegic) for scratching, meal assistance, laundry, social play ([IEEE Spectrum, 2023](../sources/ieee-spectrum-stretch-assistive.md)).
- The concept of **"assistive autonomy"** — user directs the robot via a GUI + camera view, rather than full autonomy — is the practical operating model for current-generation assistive manipulation.

### Wearable assistive devices
- **RELab tenoexo** (ETH Zurich) — robotic hand orthosis; <150g hand module; 5N per finger; immediate functional benefit in spinal cord injury adults and children ([RELab tenoexo](../sources/relab-ethz-tenoexo.md)). Parallel to soft robotics / exoskeleton work at Virginia Tech ([Assistive Robotics Lab](../sources/virginia-tech-assistive-robotics-lab.md)).

### Social and educational assistive robots
- **Furhat**, **Social Robot Haru**, **QT Robot**, **Buddy** — robots supporting older adults' social connection, children's educational tasks, and emotional wellbeing ([ITU AI for Good, 2023](../sources/itu-aiforgood-assistive-robots.md)).

## Why this matters for the broader wiki

Assistive robotics is the **end-use case that motivates most mobile-manipulation research** in this wiki — [Robot Utility Models](../entities/robot-utility-models.md), [OK-Robot](../entities/ok-robot.md), and [HomeRobot / OVMM](../sources/ovmm-homerobot.md) are all motivated by the same underlying goal: a robot that can help a person in their home without per-environment training.

The gap between the research benchmark (58.5% success on pick-and-drop, OK-Robot) and clinical deployment readiness remains large. Assistive deployments require reliability far exceeding current zero-shot benchmarks.

## Real-world household task performance (2025 data)

The [Stanford HAI AI Index 2026](../sources/stanford-hai-ai-index-2026.md) provides the best independent data point on where robots actually stand on household tasks:

- **RLBench** (controlled simulation, short-horizon tasks): EquAct achieves **89.4% success** — a controlled benchmark that has progressed from ~48% in 2022. This is the "lab ceiling."
- **BEHAVIOR-1K** (realistic household environments, human-centered tasks from surveys): 2025 Challenge top team full task success rate: **12.4%**. Q-score (partial credit): ~26%. The report's verdict: "Reliably executing household tasks in realistic environments is still beyond current capabilities."

The 89.4% vs. 12.4% gap is the canonical quantification of the sim-to-real gap for household tasks as of 2025. See also [Sim-to-real transfer](sim-to-real-transfer.md).

## SDG alignment ([ITU AI for Good](../sources/itu-aiforgood-assistive-robots.md))
- SDG 3 (Health): recovery acceleration, healthcare burden reduction
- SDG 4 (Education): interactive learning support
- SDG 10 (Reduced Inequalities): inclusive participation

## Autonomy and agency

A key finding from the [HCR Lab](../entities/hcrlab.md) ([Maya Cakmak](../entities/maya-cakmak.md), UW) challenges the assumption that more autonomy is always better: **people with severe motor impairments do NOT always prefer more autonomous robots** (HRI 2020). Autonomy preference is context- and person-specific. This motivates:

- **"Assistive autonomy"** as a practical model — user stays in the loop via GUI/camera; the robot executes sub-tasks but the user retains control.
- **[End-user robot programming (EUP)](end-user-robot-programming.md)** — tools that let users without programming skills customize robot behavior for their individual needs. HCR Lab's EUP tools have been transferred to the commercial Hello Robot Stretch SE2. A prototype tool was built specifically for Henry Evans in summer 2022.

The 2025 RO-MAN paper "Preserving Sense of Agency: User Preferences for Robot Autonomy and User Control across Household Tasks" ([HCR Lab publications](../sources/hcrlab-publications.md)) is the most recent work in this line.

## Related concepts
- [LLM-agent architecture](llm-agent-architecture.md) — the control pattern most current assistive robots use (user → LLM → robot actions)
- [End-user robot programming](end-user-robot-programming.md) — enabling non-expert users to customize robot behavior; directly addresses the per-user personalization gap
- [Imitation learning](imitation-learning.md) — policy training approach for manipulation tasks
- [World model](world-model.md) — longer-term: world models could enable robots to plan assistive actions without per-task teleoperation

## Key references
- [IEEE Spectrum — Stretch assistive robot](../sources/ieee-spectrum-stretch-assistive.md) (2023)
- [ITU AI for Good — assistive robots](../sources/itu-aiforgood-assistive-robots.md) (2023)
- [RELab tenoexo](../sources/relab-ethz-tenoexo.md) (ETH Zurich)
- [Virginia Tech Assistive Robotics Lab](../sources/virginia-tech-assistive-robotics-lab.md)

## Mentioned in
- [IEEE Spectrum — Stretch assistive robot](../sources/ieee-spectrum-stretch-assistive.md)
- [ITU AI for Good — assistive robots](../sources/itu-aiforgood-assistive-robots.md)
- [RELab tenoexo](../sources/relab-ethz-tenoexo.md)
- [Virginia Tech Assistive Robotics Lab](../sources/virginia-tech-assistive-robotics-lab.md)
- [Stanford HAI — AI Index Report 2026](../sources/stanford-hai-ai-index-2026.md)
- [HCR Lab Publications](../sources/hcrlab-publications.md)
- [Maya Cakmak — Research Overview](../sources/maya-cakmak-research.md)
