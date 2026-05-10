---
title: Maya Cakmak
type: entity
subtype: person
created: 2026-05-09
updated: 2026-05-10
sources: 9
tags: [maya-cakmak, assistive-robotics, eup, hcrlab, uw, hri]
---

**Maya Cakmak** — Associate Professor, Paul G. Allen School of Computer Science & Engineering, University of Washington. Director of the [Human-Centered Robotics Lab (HCR Lab)](hcrlab.md). Research goal: "make personal robot assistants in the home a reality" for persons with motor limitations and older adults.

## Research tracks

### Physically assistive robots
Long-running work on mobile manipulators helping people with severe motor impairments — feeding, grooming, handover of objects, teleoperation for low-bandwidth users. Primary platform: [Hello Robot Stretch](stretch.md).

Key results:
- **Henry Evans long-term deployments** (quadriplegic, stroke): summers 2021–2023 using Stretch; achieved self-feeding, face wiping, scratching, lotion, medical device operation, card games, and handing objects to family. NIH grant secured for continued work ([Maya Cakmak Research](../sources/maya-cakmak-research.md)).
- **Autonomy preference finding** (HRI 2020): people with severe motor impairments do NOT always prefer more autonomous robots. Autonomy–control tradeoff is user-specific and context-specific — an important design constraint often overlooked in the autonomy literature.
- **Sense of agency** ([Yang et al., RO-MAN 2025](../sources/yang2025-sense-of-agency.md)): end-user programmed robots preserve sense of agency even when acting autonomously; third-party involvement reduces agency more than autonomy alone; high-risk tasks drive preference for user control.
- **Robot-assisted feeding**: decade-long collaboration with UW Personal Robotics Lab (Siddhartha Srinivasa); HRI 2023 Best Design Paper Award for feeding in social contexts; [HRI 2025 out-of-lab deployment lessons](../sources/nanavati2025-feeding-out-of-lab.md) (Best Systems Paper Finalist) — open-source Kinova JACO system co-designed with two community researchers with SCI quadriplegia.
- **Handovers**: ICRA 2021 Best HRI Paper Award; affordance-aware pose selection for users with arm mobility constraints.
- **Systematic review**: "[Physically Assistive Robots](../sources/nanavati2024-physically-assistive-robots-review.md)" in *Annual Review of Control, Robotics, and Autonomous Systems* (2024, with Nanavati and Ranganeni) — 87 papers; three themes; dressing/bathing/medication identified as underserved domains.
- **Grasping in clutter**: [IVFP](../sources/murray2024-grasping-clutter-ivfp.md) — interactive visual failure prediction on Stretch RE1; autonomous reward signal enabling online policy improvement with less human supervision.
- **Explicit-input teleoperation**: [Walker et al. IROS 2024](../sources/walker2024-explicit-input-teleoperation.md) — pointing-based explicit assistance; NVIDIA collaboration; operators prefer explicit over implicit inference-based assistance.
- **PAR methodology**: [Multiple Ways of Working with Users](../sources/nanavati2024-multiple-ways-par.md) (A3DE @ HRI 2024) — cross-institutional reflection on participatory design for including PwD in PAR research.
- **Accessible communication for blind users**: [Huh et al. CHI 2026 InterAI Workshop](../sources/huh2026-accessible-robot-comm.md) — co-author on a UC Berkeley × UT Austin × UW study deriving six design guidelines for accessible robot task communication; the empirical case for **mixed-initiative narration** as preferred by blind users (vs. reactive for sighted users), directly addressing the output-interface gap in [Nanavati et al. 2024](../sources/nanavati2024-physically-assistive-robots-review.md) §6.1.3.

### End-user robot programming (EUP)
Enabling non-programmers (including users with disabilities) to customize and extend robot behavior for their specific needs.

- **FLEX-SDK** (UIST 2022): open-source social robot toolkit; nine case studies at UW and other institutions over five years.
- EUP tools transferred to commercial hardware: **Hello Robot Stretch SE2**.
- University of Wisconsin collaboration (NRI grant): program verification/synthesis and tabletop figurine-based programming.
- Literature survey: 45 papers on end-user program specification for robots.

## Significance for assistive robotics

Cakmak is the most directly relevant academic researcher to the "accessible HRI for low-motor users" problem identified in the [assistive robotics synthesis](../syntheses/assistive-robotics-research-landscape.md). Her lab is distinguished by:
1. Including PwDs as participants throughout (not just evaluating on them at the end).
2. Long-term deployments rather than controlled lab studies.
3. The finding that more autonomy ≠ better: users want to preserve agency.
4. EUP as a scalable solution to the customization problem.

## Related
- [HCR Lab](hcrlab.md) — her lab
- [Stretch](stretch.md) — primary research platform
- [Assistive robotics](../concepts/assistive-robotics.md)
- [End-user robot programming](../concepts/end-user-robot-programming.md)
- [Assistive robotics R&D landscape](../syntheses/assistive-robotics-research-landscape.md)

## Mentioned in
- [Maya Cakmak — Research Overview](../sources/maya-cakmak-research.md)
- [HCR Lab Publications](../sources/hcrlab-publications.md)
- [Physically Assistive Robots — Systematic Review](../sources/nanavati2024-physically-assistive-robots-review.md)
- [Sense of Agency — Yang et al. 2025](../sources/yang2025-sense-of-agency.md)
- [Feeding System Out-of-lab — Nanavati et al. 2025](../sources/nanavati2025-feeding-out-of-lab.md)
- [Explicit-Input Teleoperation — Walker et al. 2024](../sources/walker2024-explicit-input-teleoperation.md)
- [Grasping in Clutter IVFP — Murray et al. 2024](../sources/murray2024-grasping-clutter-ivfp.md)
- [Multiple Ways of Working with Users — Nanavati et al. 2024](../sources/nanavati2024-multiple-ways-par.md)
- [Designing Accessible Robot Communication for Blind People — Huh et al. 2026](../sources/huh2026-accessible-robot-comm.md)
