---
title: "Task-Agnostic and Interface-Aware Handling of Unintended Interface Operation for Robot Arm Teleoperation (Nejati Javaremi, Loke, Argall, IJRR 2025)"
type: source
url: https://www.argallab.northwestern.edu/publications/
fetch_url: https://www.argallab.northwestern.edu/files/2026/08/25ijrr_nejati_javaremi.pdf
local_path: raw/25ijrr_nejati_javaremi.pdf
sha256: 93176a49fea3e82a0169da8dbef3d70521eac73b60d995cc3521d952bdd4e8e3
author: "Mahdieh Nejati Javaremi, Larisa Y.C. Loke, Brenna D. Argall (Northwestern University; Shirley Ryan AbilityLab)"
published: 2025
ingested: 2026-11-16
venue: "International Journal of Robotics Research (IJRR), 2025 (author manuscript, 19 pp)"
format: paper (19 pp)
tags: [interface-aware, shared-control, teleoperation, assistive-robot-arm, kinova-jaco, sip-and-puff, spinal-cord-injury, transfer-learning, lstm, personalization, argallab, case-study]
---

# Task-Agnostic and Interface-Aware Handling of Unintended Interface Operation

## Summary

The [argallab](../entities/argallab.md)'s fullest statement of **interface awareness**. A person with a high spinal cord injury may control a 7-DoF [Kinova Jaco](../entities/kinova-jaco.md) arm through a **sip/puff** device: a one-dimensional interface with four actions (hard and soft sips and puffs), where hard ones switch control mode and soft ones move the arm along one dimension. Spasticity, fatigue and the difficulty of the device mean the signal the robot receives is often not what the person meant. Standard shared control treats the received command as the intent. This system models how each person actually operates the interface, estimates the intended interface action, checks it for safety, and corrects it, without knowing the task. The paper reports two iterations (V1 and V2), each tested as case studies with people with spinal cord injuries.

## Key claims

- **The problem** (§1): constrained interfaces force *modal* control, where one input drives different robot dimensions depending on the current mode. That adds mode switches, and an unintended mode switch is costly. The sip/puff is *"commonly the only interface accessible to people with high levels of motor impairment"* and hard to master.
- **V1:** a per-person statistical model of interface use built by histogram binning, from data gathered in abstract training tasks. Two participants.
- **V2:** an **LSTM** model of interface use that captures timing, built with transfer learning and artificially generated expert data to cope with how little data can be collected from each person. Training was redesigned to happen directly on the robot, with audio and visual cues. Three participants.
- **Baselines:** no assistance in V1; in V2 a task-agnostic version of the Maxwell's Demon safety assistance from earlier shared-control work.
- **Safety:** *"All collisions were prevented under both V1 and V2 interface-aware assistance"*; three collisions occurred under the Maxwell's Demon baseline in V2. Collisions were common without assistance in V1.
- **Mode switches:** the LSTM model *"measurably decreased the number of mode switches"*, which allowed a harder manipulation task in V2.
- **What went wrong in V1:** the data-collection tasks did not resemble real use of the arm, which confused participants when they moved from training to the evaluation task. The authors' lesson is that training and testing must mirror real device operation.
- **Remaining limit:** the safety measures are conservative in both versions, which the authors say can frustrate users.
- The abstract's summary claim: improved safety and reduced cognitive load (NASA-TLX) *"with minimal training data requirements."*

## Analysis

- **Where the uncertainty sits.** Most shared-autonomy methods model uncertainty about the user's *goal*. This work models uncertainty one step earlier, in the *channel* between the person and the robot. The two are complementary: goal inference built on a corrupted command inherits the corruption.
- **Data scarcity is the binding constraint.** Each participant can supply only a little data, in sessions that tire them. The move to transfer learning and synthetic expert data is a response to that, and it is the same constraint any personalized assistive policy will meet.
- **Relevance beyond this interface.** A teleoperation interface that is low-dimensional, modal and noisy also describes switch, gaze and head-array control of a mobile manipulator ([levels of autonomy in assistive robotics](../syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md)).
- **Evidence weight.** Case studies with two and then three participants. This page records the paper's qualitative findings; the per-participant tables were not transcribed here.

## Entities mentioned

- [argallab](../entities/argallab.md), [Shirley Ryan AbilityLab](../entities/shirley-ryan-abilitylab.md)
- [Kinova Jaco](../entities/kinova-jaco.md) — the arm used in every case study

## Concepts touched

- [Assistive robotics](../concepts/robotics/assistive-robotics.md)

## Open questions

- How large are the workload and task-time effects per participant? Transcribe the tables before quoting numbers.
- Does a model of interface use learned for one person transfer to another with the same interface?
- Can the conservative safety behaviour be relaxed without losing the zero-collision result?
