---
title: Assistive Robotics
type: concept
created: 2026-05-09
updated: 2026-08-26
sources: 32
tags: [assistive-robotics, disability, rehabilitation, exoskeleton, social-robot, accessibility]
---

**Assistive robotics** — the design and deployment of robot systems to help people with disabilities, older adults, or rehabilitation patients regain or extend physical and social capabilities. Distinct from industrial/research robotics in that the primary performance metric is *quality of life and autonomy* for a human user, not task throughput.

## Key categories (from wiki sources)

### Mobile manipulation for daily tasks
- [Stretch](../../entities/stretch.md) ([Hello Robot](../../entities/hello-robot.md)) — the most documented example in this wiki. $20k; single-arm mobile manipulator; used by Henry Evans (quadriplegic) for scratching, meal assistance, laundry, social play ([IEEE Spectrum, 2023](../../sources/ieee-spectrum-stretch-assistive.md)).
- [Kinova Jaco](../../entities/kinova-jaco.md) ([Kinova](../../entities/kinova.md)) — the **commercial** wheelchair-mounted arm (launched 2010, ~$35k): marketed as a medical device, Cartesian control through the wheelchair's own drive controls, insurance-reimbursed in Germany/Netherlands. The field's longest-standing shipped manipulation product; research editions carry the academic feeding work ([Kinova Jaco product page + user guide](../../sources/kinova-jaco-assistive-arm.md)).
- The concept of **"assistive autonomy"** — user directs the robot via a GUI + camera view, rather than full autonomy — is the practical operating model for current-generation assistive manipulation.

### Wearable assistive devices
- **RELab tenoexo** (ETH Zurich) — robotic hand orthosis; <150g hand module; 5N per finger; immediate functional benefit in spinal cord injury adults and children ([RELab tenoexo](../../sources/relab-ethz-tenoexo.md)). Parallel to soft robotics / exoskeleton work at Virginia Tech ([Assistive Robotics Lab](../../sources/virginia-tech-assistive-robotics-lab.md)).

### Social and educational assistive robots
- **Furhat**, **Social Robot Haru**, **QT Robot**, **Buddy** — robots supporting older adults' social connection, children's educational tasks, and emotional wellbeing ([ITU AI for Good, 2023](../../sources/itu-aiforgood-assistive-robots.md)).
- **[Zeroth M1](../../entities/zeroth-m1.md)** (2026, **$2,499**) — a consumer entrant advertising "gentle fall detection," safety checks, child learning and pet monitoring in a 494 mm, 2.8 kg biped/wheeled body ([product page](../../sources/zeroth-m1-product-page.md)). It belongs in **this** category rather than the mobile-manipulation one above: no payload, reach or manipulation capability is published, and its advertised value is sensing, conversation and alerting. Notable mainly for **testing a price floor an order of magnitude below [Stretch](../../entities/stretch.md)** — with correspondingly little evidence: no compute spec, no privacy statement, no accuracy figure for the safety features, and no independent review.

## The demand-side: aging in place

The human need this field serves is captured by **[aging in place](aging-in-place.md)** — most older adults want to stay in their own homes and turn to caregivers only when needed ([NIA](../../sources/nia-aging-in-place.md)). The NIA's taxonomy of "help you can receive at home" (personal care / chores / meals / money management / health care / transportation / safety) is effectively the target list for physically-assistive robots. Two things stand out: (1) mainstream 2023 elder-care guidance names **no assistive robots** at all — only wearable emergency alert systems — showing how far the research frontier sits from deployed practice; and (2) the intimate **ADLs** NIA lists (bathing, dressing, toileting) are precisely the [underserved PAR domains](../../syntheses/assistive/underserved-par-domains.md), while robotics attention concentrates on the IADLs (fetch, tidy, pick-and-place).

## Why this matters for the broader wiki

Assistive robotics is the **end-use case that motivates most mobile-manipulation research** in this wiki — [Robot Utility Models](../../entities/robot-utility-models.md), [OK-Robot](../../entities/ok-robot.md), and [HomeRobot / OVMM](../../sources/ovmm-homerobot.md) are all motivated by the same underlying goal: a robot that can help a person in their home without per-environment training.

The gap between the research benchmark (58.5% success on pick-and-drop, OK-Robot) and clinical deployment readiness remains large. Assistive deployments require reliability far exceeding current zero-shot benchmarks.

## Literature landscape (systematic review)

The [Nanavati, Ranganeni & Cakmak 2024](../../sources/nanavati2024-physically-assistive-robots-review.md) systematic review (*Annual Review of Control, Robotics, and Autonomous Systems*) is the canonical literature map for this field. From 1,981 screened papers, 87 met inclusion criteria (PAR + user study + mobile/manipulator robot for PwD):

- **Scale of need**: 1.3 billion people globally experience significant disability (WHO).
- **Domains most studied**: Navigation, eating/feeding, and pick-and-place/housework dominate. Three spikes against an otherwise thin distribution.
- **Underserved domains**: Dressing, bathing/grooming, and managing medications have high user need relative to the proportion of PAR papers addressing them — the clearest research gaps.
- **Participant inclusion**: ~half of PAR papers involve no participants with the target disability. All formative studies involved PwD; most summative evaluations did not.
- **Three research themes**: (1) Interaction interfaces; (2) Levels of autonomy; (3) Adaptation.

## What "safe near a person" costs, numerically

The wiki's assistive coverage argues about autonomy levels and interfaces; [PACS](../../sources/pacs-paper.md) supplies the physical-safety number underneath all of it. Its **FEEDING** task — put a fork of food into a person's mouth — is run under **ISO/TS 15066 power-and-force limiting** with a formally identified impact-energy threshold for the **head/eye** of **0.001 J**, against **0.014 J** for a constrained hand contact and **0.265 J** unconstrained. Two orders of magnitude between "bumping a hand" and "a fork near an eye," and the feeding case is the tightest constraint in the paper.

The result that matters for this page: an unsafeguarded diffusion policy performing that task **violated its safety constraint in 85% of timesteps** while succeeding 63% of the time. With a path-consistent safety filter, success was unchanged (0.63) and violations went to zero. Assistive manipulation near the face is exactly the regime where **task success and safety are separate measurements** — see [safety filters for learned policies](safety-filters.md). (Caveat: the quantitative feeding runs use a printed face with a cut-out mouth; the real human appears only in qualitative tests.)

Compare [Nanavati et al. 2025](../../sources/nanavati2025-feeding-out-of-lab.md), the wiki's out-of-lab feeding study, which reaches the same domain from the user-study side.

## Real-world household task performance (2025 data)

The [Stanford HAI AI Index 2026](../../sources/stanford-hai-ai-index-2026.md) provides the best independent data point on where robots actually stand on household tasks:

- **RLBench** (controlled simulation, short-horizon tasks): EquAct achieves **89.4% success** — a controlled benchmark that has progressed from ~48% in 2022. This is the "lab ceiling."
- **BEHAVIOR-1K** (realistic household environments, human-centered tasks from surveys): 2025 Challenge top team full task success rate: **12.4%**. Q-score (partial credit): ~26%. The report's verdict: "Reliably executing household tasks in realistic environments is still beyond current capabilities."

The 89.4% vs. 12.4% gap is the canonical quantification of the sim-to-real gap for household tasks as of 2025. See also [Sim-to-real transfer](../learning/sim-to-real-transfer.md).

## SDG alignment ([ITU AI for Good](../../sources/itu-aiforgood-assistive-robots.md))
- SDG 3 (Health): recovery acceleration, healthcare burden reduction
- SDG 4 (Education): interactive learning support
- SDG 10 (Reduced Inequalities): inclusive participation

## Autonomy and agency

A key finding from the [HCR Lab](../../entities/hcrlab.md) ([Maya Cakmak](../../entities/maya-cakmak.md), UW) challenges the assumption that more autonomy is always better: **people with severe motor impairments do NOT always prefer more autonomous robots** (HRI 2020). Autonomy preference is context- and person-specific. This motivates:

- **"Assistive autonomy"** as a practical model — user stays in the loop via GUI/camera; the robot executes sub-tasks but the user retains control.
- **[End-user robot programming (EUP)](end-user-robot-programming.md)** — tools that let users without programming skills customize robot behavior for their individual needs. HCR Lab's EUP tools have been transferred to the commercial Hello Robot Stretch SE2. A prototype tool was built specifically for Henry Evans in summer 2022.

The 2025 RO-MAN paper "Preserving Sense of Agency: User Preferences for Robot Autonomy and User Control across Household Tasks" ([HCR Lab publications](../../sources/hcrlab-publications.md)) is the most recent work in this line.

## Communication and the output-interface gap

The [PAR review](../../sources/nanavati2024-physically-assistive-robots-review.md) §6.1.3 flags **output interfaces** — how the robot communicates state and intent back to the user — as comparatively under-researched. [Huh et al. 2026](../../sources/huh2026-accessible-robot-comm.md) is the direct response for blind users: it shows that blind users systematically overestimate their situational awareness during silent autonomous execution (avg 7.5 inaccuracies per task) and overwhelmingly prefer **mixed-initiative narration** (proactive + question answering) over reactive answer-only modes. The full body of findings is summarized in the [Accessible robot communication](accessible-robot-communication.md) concept page.

The navigation-domain counterpart is [DRAGON (Liu et al. 2024)](../../sources/dragon-assistive-nav-2024.md), which pairs verbal output (CLIP-grounded scene description + VQA + dialogue) with kinesthetic guidance via a T-shaped handle for persons with visual impairments.

## Domestic-robot precursors

**Institutional precursor:** the [CMU/Pitt Quality of Life Technology Center](../../entities/cmu-qolt-center.md) (NSF ERC, 2006 – mid-2010s) ran the first large-scale systems-level program in this space — PerMMA (two-armed robotic wheelchair with user/remote-assistant blended control) and HERB — and its clinician-partnered, user-in-the-loop methodology prefigures current PAR practice.

[Schneiders et al. 2021](../../sources/schneiders2021-domestic-robots-automation.md) — the only ingested study of the *consumer-deployed* domestic-robot category (vacuum, lawnmower, hybrid). Identifies **task fragmentation** (one-task-becomes-many-sub-tasks) and **under-trust → co-located monitoring** patterns that recur in PAR deployments and accessible-communication research.

## Related concepts
- [Aging in place](aging-in-place.md) — the demand-side / human-needs context that motivates in-home assistive robotics
- [Accessible robot communication](accessible-robot-communication.md) — output-interface side of HRI for non-visual users
- [LLM-agent architecture](../agents/llm-agent-architecture.md) — the control pattern most current assistive robots use (user → LLM → robot actions)
- [End-user robot programming](end-user-robot-programming.md) — enabling non-expert users to customize robot behavior; directly addresses the per-user personalization gap
- [Imitation learning](../learning/imitation-learning.md) — policy training approach for manipulation tasks
- [World model](../world-models/world-model.md) — longer-term: world models could enable robots to plan assistive actions without per-task teleoperation
- [Robot safety standards](robot-safety-standards.md) — ISO 13482 is the certification pathway for in-home/assistive deployment ("mobile servant robot" category); the [Fosch-Villaronga critique](../../sources/fosch-villaronga-iso13482-exoskeletons.md) documents its gaps (incl. cognitive accessibility as a safety issue)

## Key references
- [Kinova Jaco product page + user guide](../../sources/kinova-jaco-assistive-arm.md) (2021)
- [IEEE Spectrum — Stretch assistive robot](../../sources/ieee-spectrum-stretch-assistive.md) (2023)
- [ITU AI for Good — assistive robots](../../sources/itu-aiforgood-assistive-robots.md) (2023)
- [RELab tenoexo](../../sources/relab-ethz-tenoexo.md) (ETH Zurich)
- [Virginia Tech Assistive Robotics Lab](../../sources/virginia-tech-assistive-robotics-lab.md)

## Mentioned in

> [!note] Curated list — **32** source pages link here; the ones below are those that shaped this page.

- [IEEE Spectrum — Stretch assistive robot](../../sources/ieee-spectrum-stretch-assistive.md)
- [ITU AI for Good — assistive robots](../../sources/itu-aiforgood-assistive-robots.md)
- [RELab tenoexo](../../sources/relab-ethz-tenoexo.md)
- [Virginia Tech Assistive Robotics Lab](../../sources/virginia-tech-assistive-robotics-lab.md)
- [Stanford HAI — AI Index Report 2026](../../sources/stanford-hai-ai-index-2026.md)
- [HCR Lab Publications](../../sources/hcrlab-publications.md)
- [Maya Cakmak — Research Overview](../../sources/maya-cakmak-research.md)
- [Physically Assistive Robots — Systematic Review](../../sources/nanavati2024-physically-assistive-robots-review.md)
- [Kinova Jaco product page + user guide](../../sources/kinova-jaco-assistive-arm.md)
- [Sense of Agency — Yang et al. 2025](../../sources/yang2025-sense-of-agency.md)
- [Feeding System Out-of-lab — Nanavati et al. 2025](../../sources/nanavati2025-feeding-out-of-lab.md)
- [Explicit-Input Teleoperation — Walker et al. 2024](../../sources/walker2024-explicit-input-teleoperation.md)
- [Grasping in Clutter IVFP — Murray et al. 2024](../../sources/murray2024-grasping-clutter-ivfp.md)
- [Multiple Ways of Working with Users — Nanavati et al. 2024](../../sources/nanavati2024-multiple-ways-par.md)
- [DRAGON Paper (Liu et al. 2024)](../../sources/dragon-assistive-nav-2024.md)
- [Designing Accessible Robot Communication for Blind People (Huh et al. 2026)](../../sources/huh2026-accessible-robot-comm.md)
- [Domestic Robots and the Dream of Automation (Schneiders et al. 2021)](../../sources/schneiders2021-domestic-robots-automation.md)
- [Aging in Place: Growing Older at Home (NIA)](../../sources/nia-aging-in-place.md)
- [Zeroth M1 — product page](../../sources/zeroth-m1-product-page.md)
