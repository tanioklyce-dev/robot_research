---
title: HAND ERC (NSF Human AugmentatioN via Dexterity Engineering Research Center)
type: entity
subtype: lab
created: 2026-11-17
updated: 2026-11-17
sources: 3
tags: [hand-erc, dexterous-manipulation, robot-hands, tactile-sensing, nsf, northwestern, skill-library, testbed, assistive-robotics]
---

**HAND ERC** — a US National Science Foundation Engineering Research Center on dexterous robot hands, headquartered at Northwestern University. It was announced on 21 August 2024 with **$26 million over five years, renewable for a further $26 million and five years** ([announcement](../sources/northwestern-hand-erc-announcement.md)). The center's site states this as *"up to $52M and 10-years"* ([site](../sources/hand-erc-site.md)).

## Goal

Dexterous manipulation *"out of the box"* by 2035: a non-specialist sets up a two-armed robot and within a day it performs dexterous skills from a library, such as twisting a cap on a jar or using hand tools; within a week it does whole tasks for that user's application ([site](../sources/hand-erc-site.md)).

## Structure

| Part | Lead | Content |
|---|---|---|
| Director | J. Edward Colgate (Northwestern) | Named in the [announcement](../sources/northwestern-hand-erc-announcement.md) |
| Research director | Kevin Lynch (Northwestern) | |
| Thrust 1: Hands | Carmel Majidi (Carnegie Mellon) | Hand designs revised every two years; soft tactile skin; tendons, electrostatic clutches, fiber actuators |
| Thrust 2: Intelligent Dexterity | Brenna Argall ([argallab](argallab.md)) | Skill library; behavior cloning, reinforcement learning, sim-to-real; tactile simulation |
| Thrust 3: Human Interface | Julie Shah (MIT) | Haptic, VR and language interfaces; low-code programming; social, legal and industrial studies |

Source: [site](../sources/hand-erc-site.md). The research team listed there also includes [Russ Tedrake](russ-tedrake.md), Todd Murphey, Oliver Kroemer and Nancy Pollard.

## Testbeds

- **DexNex** at Northwestern, the integration and research testbed.
- High-mix manufacturing (Berkshire Innovation Center), assembly and disassembly (Carnegie Mellon), **assistance and caregiving ([Shirley Ryan AbilityLab](shirley-ryan-abilitylab.md))**, high-consequence material handling (Texas A&M), dexterity education (Florida A&M).

Source: [site](../sources/hand-erc-site.md).

## Ecosystem

About 45 dues-paying industry members, among them Meta, [DeepMind](google-deepmind.md), Amazon Robotics, Analog Devices, the Bosch Center for AI and the Robotics and AI Institute, plus many small makers of tactile sensors, actuators and hands. Partners include NIST, ASTM, NASA and several national laboratories ([site](../sources/hand-erc-site.md)).

## Projects (2025–2026)

31 projects are listed, 15 with a one-paragraph page ([project pages](../sources/hand-erc-projects.md)):

- **Hands:** electrostatic artificial muscle fibers, a stretchable tactile sensing layer, a textile sensing glove, durable skin and tissue.
- **Intelligent dexterity:** a grasp-affordance taxonomy with levels-of-dexterity benchmarks (led by Argall), a representation for dexterous skills, a [Drake](drake.md) simulation of the DexNex teleoperation system, [Diffusion Policy](diffusion-policy.md) trained from teleoperation, and two soft-hand learning projects.
- **Human interface:** haptic cue studies, a haptic glove, interfaces that map intent to dexterous primitives, and steering a pre-trained diffusion policy at deployment.
- **Integration:** a "bones, joints and tendons" project described as a precursor to the hand design, with remotized actuators. Mechanical design, skin, electronics, software and benchmarking are 2026 projects.

**Status as of the capture:** the center is still before its first hand. The learning methods are the ones common across this wiki; the new work is in actuators, skins and tendons.

> [!note] Coverage
> Known here from the center's website and a university announcement. The pages state aims, structure and plans. No hand design, benchmark or result has been ingested.

## Related

- [Tactile sensing](../concepts/robotics/tactile-sensing.md), [Dexterous tool manipulation](../concepts/robotics/dexterous-tool-manipulation.md)
- [Assistive robotics](../concepts/robotics/assistive-robotics.md)

## Mentioned in

- [NSF HAND Engineering Research Center (site)](../sources/hand-erc-site.md)
- [Northwestern announcement of the HAND award (2024-08-21)](../sources/northwestern-hand-erc-announcement.md)
- [HAND ERC project list and project pages](../sources/hand-erc-projects.md)
