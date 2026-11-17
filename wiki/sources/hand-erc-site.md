---
title: "NSF HAND Engineering Research Center — Human AugmentatioN via Dexterity (site, retrieved 2026-11-16)"
type: source
url: https://hand-erc.org/
local_path: raw/2026-11-16-hand-erc-site.md
sha256: ddcd71dfe8ebbfa7d0487928bc055fdce49e5b85e9b6bc135481be09452b4d31
capture: bundle
author: NSF HAND Engineering Research Center (headquartered at Northwestern University)
published: Unknown (retrieved 2026-11-16)
ingested: 2026-11-17
format: text extracted from 6 pages of the center's website
tags: [hand-erc, dexterous-manipulation, robot-hands, tactile-sensing, nsf, engineering-research-center, northwestern, skill-library, sim-to-real, low-code, testbed, assistive-robotics, shirley-ryan-abilitylab]
---

# NSF HAND Engineering Research Center

## Summary

**HAND** (Human AugmentatioN via Dexterity) is a US National Science Foundation Engineering Research Center headquartered at Northwestern University, funded *"for up to $52M and 10-years"*. The [award announcement](northwestern-hand-erc-announcement.md) shows that this is $26 million for five years with a renewal option for the same again. Its target is a dexterous robot hand that works **"out of the box"**: hardware that mounts on commercial arms and humanoids, a growing library of AI-driven dexterous skills, and an interface a trained worker can use without a robotics specialist. It states a dated goal for 2035. One of its five application testbeds, for assistance and caregiving, is at the [Shirley Ryan AbilityLab](../entities/shirley-ryan-abilitylab.md), and Brenna Argall of the [argallab](../entities/argallab.md) leads its intelligent-dexterity thrust. This capture is the center's own website: it states aims and structure, not results.

## Key claims

- **The 2035 goal** (research page): *"A non-specialist will be able to set up a bimanual robot system and, within a day, have it robustly perform tactile-and-vision-based dexterous skills included in the skill library, such as twisting a cap on a jar or using hand tools. By the end of a week, the robot will productively perform entire dexterous tasks for the user's particular application."*
- **The engineered system has four parts:** (1) end-effectors with vision and tactile sensing that integrate with commercial arms and humanoids and can use human tools; (2) high-fidelity simulation, including soft skins and tactile sensors, for digital twins and sim-to-real; (3) an open, extensible library of *"robust, composable, error-correcting dexterous skills"*; (4) a low-code interface and training materials for non-specialists.
- **Three research thrusts:**
  - **Hands** (lead: Carmel Majidi, Carnegie Mellon): hand designs *"upgraded every two years"*, soft multimodal tactile skin, tendons, electrostatic clutches and liquid-crystal-elastomer fiber actuators.
  - **Intelligent Dexterity** (lead: Brenna Argall): the skill library, training by behavior cloning, reinforcement learning and sim-to-real, sensor-based control, and simulation of tactile skin.
  - **Human Interface** (lead: Julie Shah, MIT): haptic, virtual-reality and natural-language interfaces, low-code programming, and social, legal and industrial studies.
- **Research director:** Kevin Lynch, Northwestern.
- **Testbeds:** a research testbed at Northwestern called the Dexterity Nexus (DexNex), and five application testbeds: high-mix manufacturing (Berkshire Innovation Center, Massachusetts), assembly and disassembly (Carnegie Mellon), **assistance and caregiving (Shirley Ryan AbilityLab)**, high-consequence material handling (Texas A&M), and dexterity education (Florida A&M).
- **Partners:** core university partners are Texas A&M, Florida A&M and Carnegie Mellon, with faculty from MIT, Syracuse and Wisconsin–Madison.
- **Industry members:** about 45 are listed, paying dues in four tiers by company size in return for an advisory-board seat, IP rights and a vote on project priorities. They include Meta, DeepMind, Amazon Robotics, Analog Devices, the Bosch Center for AI and the Robotics and AI Institute, and many small tactile-sensor, actuator and hand makers.
- **Center partners** include NIST and ASTM (standards), NASA, several national laboratories, the ARM Institute and the Federal Reserve Bank of Chicago's economic mobility project.
- **Stated impact:** making robot manipulation accessible to small firms as well as large ones, and enabling *"individuals with motor impairments to live fuller lives"*.

## Analysis

- **A dated, checkable goal.** "A day to set up, a week to be productive, by 2035" is specific enough to score, which is unusual for a research center. It sits close to the 2035 column of this wiki's [home robot forecast](../syntheses/society/home-robot-forecast-2026-2028.md), which was written without it.
- **The bet is on the hand and on touch.** The center treats the end-effector and tactile sensing as the limiting factor, where most learned-policy work in this wiki uses parallel grippers and vision ([tactile sensing](../concepts/robotics/tactile-sensing.md), [dexterous tool manipulation](../concepts/robotics/dexterous-tool-manipulation.md)).
- **A skill library, not one end-to-end policy.** "Composable, error-correcting skills" is a modular position, in contrast with the single-policy approach of [VLA models](../concepts/learning/vla-models.md).
- **Assistance is one of five testbeds**, and it is hosted in a hospital. That gives the center a route to testing with people who have motor impairments.
- **Evidence weight.** A website. No hand, benchmark or result is described on the captured pages; the project list page was not captured.

## Entities mentioned

- [HAND ERC](../entities/hand-erc.md)
- [Shirley Ryan AbilityLab](../entities/shirley-ryan-abilitylab.md) — hosts the assistance and caregiving testbed
- [argallab](../entities/argallab.md) — its director leads Thrust 2
- [Google DeepMind](../entities/google-deepmind.md) — listed industry member
- [Russ Tedrake](../entities/russ-tedrake.md) — listed on the research team

## Concepts touched

- [Tactile sensing](../concepts/robotics/tactile-sensing.md)
- [Dexterous tool manipulation](../concepts/robotics/dexterous-tool-manipulation.md)
- [Assistive robotics](../concepts/robotics/assistive-robotics.md)

## Open questions

- What has the center built so far? The [project pages](hand-erc-projects.md) show plans through 2026 and no finished hand.
- ~~When did the award start?~~ Answered by the [announcement](northwestern-hand-erc-announcement.md): 21 August 2024, $26 million for five years, renewable for another $26 million.
- What does the assistance testbed at the Shirley Ryan AbilityLab actually test?
