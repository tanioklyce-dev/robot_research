---
title: argallab (Assistive & Rehabilitation Robotics Lab, Shirley Ryan AbilityLab / Northwestern)
type: entity
subtype: lab
created: 2026-11-16
updated: 2026-11-17
sources: 6
tags: [argallab, brenna-argall, shared-control, shared-autonomy, interface-aware, assistive-robotics, powered-wheelchair, assistive-robot-arm, robot-learning, northwestern, shirley-ryan-abilitylab]
---

**argallab** — the assistive & rehabilitation robotics laboratory directed by Brenna Argall, a Northwestern University group located inside the [Shirley Ryan AbilityLab](shirley-ryan-abilitylab.md) in Chicago. It adds robotics autonomy to assistive machines for people with motor impairments ([lab pages](../sources/shirley-ryan-abilitylab-research-labs.md)).

## The problem it works on

*"As need increases, access decreases."* The more severe a person's motor impairment, the harder it is to operate the machine meant to help. A robot arm needs 6-D control; a joystick gives 2-D, and a sip-and-puff or head-array interface gives less. The lab's approach is to make the machine partly control itself and to study how control should be divided ([lab pages](../sources/shirley-ryan-abilitylab-research-labs.md)).

## Research lines

- **Shared-control powered wheelchairs.** Obstacle avoidance, doorway traversal, docking, and incline and drop-off detection, built as modular add-ons for existing commercial chairs so that cost outside insurance stays low. The stated goal is that partial autonomy becomes a standard fitting option.
- **Assistive robot arms.** Making a wheelchair-mounted arm usable through limited interfaces. Work covers intent inference, mode-switch assistance and user-customized control sharing.
- **Interface-aware autonomy.** Modelling how a particular person actually operates their interface, including unintended signals, before inferring what they want.
- **Robots learning from motor-impaired teachers**, and people learning to control robots through high-dimensional body-machine interfaces.

Source for all four: [lab pages](../sources/shirley-ryan-abilitylab-research-labs.md).

Two of these lines are stated more fully on Northwestern's [topic pages](../sources/northwestern-robotics-assistive-topic-pages.md). In the motor-learning project, autonomy handles part of the control at first and hands dimensions back to the person as they learn, with machine learning deciding when. In the learning-from-impaired-teachers project, the lab hypothesizes that noisy, sparse demonstrations can be exploited by the learning algorithm.

## Positions worth holding

- **Users want to stay in the control loop.** Argall: *"most people don't want a 100%-driverless car solution for their wheelchairs"*, and autonomy that steps in at the wrong time takes agency away.
- **Test with the real users.** The lab says it always runs studies with people who have impairments, where many robotics groups treat a wheelchair as another mobile base.
- **Clinical grounding changes the research agenda.** Argall argues that claims of assistive relevance in robotics papers are often not grounded in clinical practice.

Source: [lab pages](../sources/shirley-ryan-abilitylab-research-labs.md) (a 2023 institutional news article).

## Facts

- **Director:** Brenna Argall, professor of Computer Science, Mechanical Engineering, and Physical Medicine and Rehabilitation at Northwestern. PhD in Robotics, Carnegie Mellon (2009); postdoc at EPFL. NSF CAREER 2016; AIMBE Fellow 2023.
- **Output:** 71 listed publications through 2026, at venues including RSS, IJRR, HRI and ICORR.
- **Collaborators named:** Todd Murphey and Sandro Mussa-Ivaldi (grants), LUCI (wheelchair safety systems), Innovative Design Labs (NIH SBIR).
- **Project DRIVE:** led by the lab, a participant in the NSF Convergence Accelerator program.
- **HAND ERC:** Argall leads the Intelligent Dexterity thrust of the [HAND ERC](hand-erc.md), an NSF center on dexterous robot hands headquartered at Northwestern ([site](../sources/hand-erc-site.md)). Within it she leads a project on a grasp-affordance taxonomy and levels-of-dexterity benchmarks ([project pages](../sources/hand-erc-projects.md)).

Source: [lab pages](../sources/shirley-ryan-abilitylab-research-labs.md).

## How it relates to the rest of the wiki

Most assistive work here puts a general-purpose mobile manipulator in the home ([Stretch as an assistive platform](../syntheses/assistive/stretch-as-assistive-platform.md)). This lab improves devices that are already prescribed and paid for. Its shared-control work sits in the middle rows of the [levels of autonomy](../syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md) framing, and its agency argument matches the sense-of-agency study discussed on the [source page](../sources/shirley-ryan-abilitylab-research-labs.md).

## Ingested papers

| Paper | What it shows |
|---|---|
| [REACT shared control for wheelchairs](../sources/react-shared-control-wheelchair-paper.md) (RSS 2026) | A deliberately minimal method on top of the commercial LUCI safety system: redirect only when safety throttling is substantial, with no intent or task inference. Case studies with four users over five sessions. Safe trials for a sip/puff driver rose from 72% to 92%; a skilled joystick driver saw no change. One user rated the assistance best and said they would use it least. |
| [Interface-aware arm teleoperation](../sources/interface-aware-arm-teleoperation-sci-paper.md) (IJRR 2025) | Models how each person actually operates a sip/puff interface, then corrects unintended commands to a Kinova Jaco arm without knowing the task. Two iterations with people with spinal cord injuries; all collisions prevented in both; an LSTM model with transfer learning reduced mode switches. |

Both are case studies with two to four participants and no inferential statistics. They show direction for individuals, not effect sizes.

> [!note] Coverage
> Two of the lab's 71 listed papers are ingested. The rest of this page rests on lab and institutional web pages.

## Related

- [Shirley Ryan AbilityLab](shirley-ryan-abilitylab.md)
- [Assistive robotics](../concepts/robotics/assistive-robotics.md)
- [Kinova Jaco](kinova-jaco.md) — the class of wheelchair-mounted arm this work targets

## Mentioned in

- [Shirley Ryan AbilityLab research labs and the argallab](../sources/shirley-ryan-abilitylab-research-labs.md)
- [REACT shared control for powered wheelchairs (RSS 2026)](../sources/react-shared-control-wheelchair-paper.md)
- [Interface-aware handling of unintended interface operation (IJRR 2025)](../sources/interface-aware-arm-teleoperation-sci-paper.md)
- [NSF HAND Engineering Research Center (site)](../sources/hand-erc-site.md)
- [Northwestern robotics topic pages](../sources/northwestern-robotics-assistive-topic-pages.md)
- [HAND ERC project list and project pages](../sources/hand-erc-projects.md)
