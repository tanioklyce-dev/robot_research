---
title: Physically Assistive Robots — A Systematic Review (Nanavati, Ranganeni, Cakmak 2024)
type: source
url: https://doi.org/10.1146/annurev-control-062823-024352
local_path: raw/nanavati2024physically.pdf (preprint); raw/annurev-control-062823-024352.pdf (published Annual Review version)
author: Amal Nanavati, Vinitha Ranganeni, Maya Cakmak
published: 2024 (Advance online November 21, 2023)
ingested: 2026-05-09
updated: 2026-05-10
tags: [assistive-robotics, systematic-review, par, hcrlab, maya-cakmak, amal-nanavati]
---

## Summary

PRISMA systematic review of mobile and manipulator robots that physically assist people with disabilities. Published in *Annual Review of Control, Robotics, and Autonomous Systems*, Vol. 7, 2024, pp. 123–47. Screened 1,981 papers from top robotics, HCI, and accessible-technology venues; included 87. Organizes the field along three research themes — **interaction interfaces, levels of autonomy, and adaptation** — and identifies systematic gaps in who is studied and which tasks are addressed.

> [!note] On 2026-05-10 we obtained the published Annual Review PDF (`raw/annurev-control-062823-024352.pdf`) in addition to the preprint already on file. The two are the same paper. This source page now incorporates content from the Annual Review §6 (interaction interfaces, levels of autonomy, adaptation) that was previously listed as an open question.

## Key claims — survey & landscape

- **Scale of need**: 1.3 billion people globally experience significant disability (WHO); disabilities can impact ability to independently perform ADLs and IADLs.
- **Literature trend**: PAR papers have increased severalfold over the past decade, yet the field remains siloed by domain of assistance with little cross-domain synthesis.
- **PRISMA pipeline**: 1,981 papers screened → 135 full-text → 87 included. Exclusions: no PAR for PwD (1,275), no user study (337), no mobile/manipulator robot (234), rehabilitation focus (28), other (16).
- **Domains of assistance**: Three spikes in PAR research — navigation, eating/feeding, and pick-and-place / housework. These three domains dominate.
- **Underserved domains**: Dressing, bathing/grooming, and managing medications have high user need (per IADL surveys) but proportionately little PAR research. These are flagged as high-priority gaps.
- **Target populations**: Motor impairment (49 papers, most common), elderly (17), visual impairment (11), children (6), other (4). Drastically different from SAR (Socially Assistive Robot) research, which targets autism, dementia, and older adults.
- **Participant inclusion failure**: ~half of PAR papers involve no participants with target disabilities. All formative studies involve PwD; most summative evaluations involve only people without disabilities — creating a risk that designs miss real user needs.

## Three research themes (§6, Annual Review version)

### 6.1 Interaction interfaces

**Input interfaces** — using the Senses and Sensors Taxonomy:
- *Direct processing* — EMG/EEG converting brain signals to robot commands; mostly pick-and-place teleoperation. Often combined with eye gaze, muscle contraction, or other modalities.
- *Indirect processing* — vision (laser pointers, gaze trackers, mouth-open detection for feeding), audition (speech), touch (force-torque on robot handle, e.g., Ranganeni et al.), kinesthetic (body movements for teleoperation, rotary/pressure sensors on walkers).

**Output interfaces** — comparatively under-explored:
- Vision: display robot's camera feed during teleoperation/interaction.
- Audition: verbalization to greet, provide direction feedback, narrate planned actions.
- Touch: haptic vibrations conveying direction or obstacle distance.
- Kinesthetic: position/force adjustments in walkers; guiding the user's hand to a target.
- Robot motion as an implicit output channel for intent — noted as a category but **not investigated by any PAR paper in the survey**.

**Future work on interfaces**:
- Output interfaces deserve much more attention; users' trust and comfort hinge on transparent state/intent communication ([Huh et al. 2026](huh2026-accessible-robot-comm.md) is the most direct follow-up).
- Many input interfaces require extra devices — users want to minimize the number of assistive devices they manage.

### 6.2 Levels of autonomy

- **Most PAR research operates at a single level of autonomy.** Few works expose autonomy as user-configurable.
- Zhang et al. (cited as ref 38) let users of a navigational aide choose between full and partial autonomy; users preferred **less autonomy in less-controlled environments** (e.g., outdoor). Mirrored by Ranganeni et al. (ref 8).
- This finding aligns with the HCR Lab's broader [autonomy-preference finding](../entities/maya-cakmak.md): more autonomy is *not* universally preferred by people with severe motor impairments.

### 6.3 Adaptation

Three dimensions of adaptation in PAR research:

1. **What gets adapted**: input interface (e.g., screen-reader speed customization), level of autonomy (full vs. partial mode), specific functionalities (e.g., older adults programming a custom skill like "raise tray when microwave is on", customizing follow-policy vs. user-input ratio, customizing robot speed/proximity/speech).
2. **Who does the adaptation**:
   - **User** — exposed knobs, mode selectors, continuous parameters, even an entire domain-specific language for customization (Saunders et al.).
   - **Shared control** — user provides calibration data (sensor sensitivity, mobility level, arm range of motion).
   - **Robot** — observes/predicts user state (distance from body, gaze of other diners) and adapts behavior.
3. **When adaptation happens**: pre-execution calibration, during execution (mode selection, parameter iteration), post-task (data-driven updates between sessions).

**Open guidance gaps**: there are no published guidelines on *who* should do the adaptation or *when* it should happen for a given robot/user/domain. Cross-domain transfer of adaptation insights is also unmapped.

## Summary points (paper's own)

1. Three main PAR domains: navigation, feeding, pick-and-place.
2. Nearly all formative works include PwD; ~half of summative evaluations don't.
3. In-context deployments are systematically under-reported (relegated to short sections).
4. Most summative evaluations use task-specific objective metrics + custom subjective questionnaires.
5. Many input interfaces; comparatively few output interfaces.
6. Most PAR uses a single autonomy level despite known user-by-context preference variation.
7. Adaptation research is fragmented across domains; no guidance on who/when.

## Entities mentioned

- [Maya Cakmak](../entities/maya-cakmak.md)
- [Amal Nanavati](../entities/amal-nanavati.md)
- [HCR Lab](../entities/hcrlab.md)

## Concepts touched

- [Assistive robotics](../concepts/assistive-robotics.md)
- [Accessible robot communication](../concepts/accessible-robot-communication.md) — §6.1.3 output-interface gap is the entry point for [Huh et al. 2026](huh2026-accessible-robot-comm.md)
- [End-user robot programming](../concepts/end-user-robot-programming.md) — levels of autonomy + adaptation themes intersect with EUP

## Mentioned in
- [Assistive robotics — R&D landscape](../syntheses/assistive-robotics-research-landscape.md)
- [Levels of autonomy in assistive robotics](../syntheses/levels-of-autonomy-in-assistive-robotics.md)
- [Underserved PAR domains](../syntheses/underserved-par-domains.md)
- [Designing Accessible Robot Communication for Blind People (Huh et al. 2026)](huh2026-accessible-robot-comm.md) — direct follow-up on §6.1.3 output-interface gap.
