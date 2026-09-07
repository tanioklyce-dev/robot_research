---
title: End-User Robot Programming
type: concept
created: 2026-05-09
updated: 2026-09-07
sources: 13
tags: [eup, robot-programming, hri, accessibility, customization]
---

**End-user robot programming (EUP)** — the practice of enabling non-expert users — including people with disabilities, older adults, and domain specialists — to specify, customize, and extend robot behavior without requiring programming skills. Distinct from developer-facing APIs and from teleoperation: EUP targets people who will use the robot regularly and need it to work their way.

## Rationale

Universal robotic capabilities — a robot that can do everything anyone might need — are computationally and practically infeasible. EUP offers an alternative: a general-purpose robot platform plus user-accessible tools for specifying the specific behaviors each user needs. This:
- Scales to the long tail of individual user needs (especially relevant for assistive robotics)
- Reduces dependence on programmers for small customizations
- Lets users with disabilities participate in designing their own robot's behavior

## Key approaches

- **Visual programming / block-based**: ConCodeIt (HCR Lab) — concurrency-aware blocks for robot programs
- **Programming by demonstration**: synthesis of robot programs from a single observed human demo (Huang, Fox, Cakmak — IROS 2019); Diffusion-PbD (2024)
- **Multimodal specification**: path sketches on tablet + natural language (HRI 2023)
- **Sketch + tunable holes**: expert creates a program sketch with adjustable parameters; end-user tunes variables (RSS 2020)
- **Tangible programming**: figurines on a tabletop to program robot interactions (Figaro, CHI 2021; Situated Tangible Robot Programming, HRI 2017)
- **FLEX-SDK** (UIST 2022) — open-source toolkit for social robots from two tablet screens; deployed across UW and other institutions

## Key findings

- **EUP literature survey** (Cakmak et al.): 45 papers on end-user program specification for robots. EUP tools have been transferred to commercial hardware — including [Hello Robot Stretch SE2](../../entities/stretch.md) — indicating the approach is practically deployable, not just academic.
- **Sense of agency** ([Yang et al., RO-MAN 2025](../../sources/yang2025-sense-of-agency.md)): In a two-part survey study using Hello Robot Stretch 3, **end-user programmed robots highly preserved users' sense of agency** even when acting fully autonomously — because the user is the author of the robot's behavior. Third-party teleoperation reduced sense of agency more than full autonomy alone. In high-risk contexts (e.g., medication preparation), users strongly preferred interfaces that preserved their control. Model: "Sense of agency can be preserved if the robot is programmed by the user, instead of relying on a third party to control the robot." This provides the strongest empirical case for EUP as the preferred autonomy level for in-home assistive robots.
- **Out-of-lab feeding deployment** ([Nanavati et al., HRI 2025](../../sources/nanavati2025-feeding-out-of-lab.md)): The three key design principles for out-of-lab deployment — portability, customizability, and user control — map directly onto EUP's core commitments. Variable autonomy (letting users escalate or de-escalate robot autonomy as off-nominals arise) was cited as essential for real-world viability.

## Connection to assistive robotics

EUP is particularly relevant to [assistive robotics](assistive-robotics.md) because:
1. Users with motor impairments have highly individual needs; a universal policy cannot cover them all.
2. The [HRI 2020 finding](../../sources/maya-cakmak-research.md) that people with severe motor impairments do NOT always prefer more autonomy suggests that giving users control over *how* the robot operates (via EUP) may be more valuable than pushing autonomy higher.
3. [Maya Cakmak](../../entities/maya-cakmak.md)'s lab developed a prototype EUP tool specifically for Henry Evans (quadriplegic) during summer 2022 — the clearest example of per-user customization in the wild.

## Related
- [Assistive robotics](assistive-robotics.md)
- [LLM-agent architecture](../agents/llm-agent-architecture.md) — natural-language task specification is a soft form of EUP
- [HCR Lab](../../entities/hcrlab.md) — primary research group

## A third channel: the non-expert writes the *prior*, not the behavior

The approaches on this page have a person specify **what the robot should do**. [Oriyama et al. 2025](../../sources/hitl-transfer-learning-collision-avoidance.md) have a person specify **what the robot should start out believing**, and then let it learn the rest: a four-branch rule (*move away from whichever sensor reads closest*) labels 100 random-walk observations, that dataset trains a small network, and those weights initialize an online learner.

The authoring cost is trivially low — it is an `if/else` — and the measured result is that it matters **exactly where the environment matches what the author had in mind**, and not otherwise (p = 0.441 in a dynamic environment the rule was not written for). That is a usable design constraint for any end-user programming system whose output feeds a learner rather than an executor: **the user is not specifying behavior, they are specifying a distribution assumption**, and it fails silently when the deployment leaves it.

## Mentioned in

- [Human-in-the-loop transfer learning in collision avoidance](../../sources/hitl-transfer-learning-collision-avoidance.md) — a hand-written rule as the prior, and where it stops paying.
- [HCR Lab Publications](../../sources/hcrlab-publications.md)
- [Maya Cakmak — Research Overview](../../sources/maya-cakmak-research.md)
- [Sense of Agency — Yang et al. 2025](../../sources/yang2025-sense-of-agency.md)
- [Feeding System Out-of-lab — Nanavati et al. 2025](../../sources/nanavati2025-feeding-out-of-lab.md)
