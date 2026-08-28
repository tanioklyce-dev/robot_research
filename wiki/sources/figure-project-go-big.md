---
title: Project Go-Big — Internet-Scale Humanoid Pretraining and Direct Human-to-Robot Transfer (Figure AI)
type: source
url: https://www.figure.ai/news/project-go-big
author: Figure AI
affiliation: Figure AI
published: 2025-09-18
ingested: 2026-08-28
tags: [figure, helix, go-big, brookfield, human-data, egocentric, cross-embodiment, zero-shot, navigation, se2, pretraining, vendor-source]
---

> [!warning] Vendor announcement, no evaluation
> No success rate, no baseline, no dataset size, no method description. The architectural and result claims below are Figure-stated and uncorroborated.

## Summary

**Project Go-Big** — [Figure AI](../entities/figure.md)'s human-video pretraining programme, announced 2025-09-18, one day after the [Brookfield partnership](figure-brookfield-partnership.md) that supplies its collection sites. Two claims: (1) Figure is building "the world's largest and most diverse humanoid pretraining dataset" from **egocentric human video captured in Brookfield's residential, office and logistics properties**; and (2) a first result — **[Helix](../entities/helix.md) trained on 100% human video, with no robot demonstrations whatsoever, performing closed-loop navigation** in cluttered real homes from spoken commands like *"go to the fridge."*

**This is the wiki's answer to the question [Index](../entities/figure-index.md) refuses to address** — how Figure crosses the human→robot gap. It is a real answer, published 11 months before Index. It is also a **navigation-only** answer, which is the easiest possible case, and Figure has never published a manipulation equivalent.

## Key claims

### The dataset programme

- Framing: robotics "lacks a large-scale equivalent — no *'YouTube for robot behaviors'*" to ImageNet / Wikipedia / YouTube.
- The stated structural argument for humanoids specifically: *"their perspectives and kinematics mirror our own, making it possible to transfer knowledge directly from everyday human video."*
- Collection sites come from [Brookfield](../entities/brookfield.md): **100,000+ residential units**, **500M sq ft of commercial office**, **160M sq ft of logistics**, against a $1T asset base.
- *"Figure has already begun data collection efforts in Brookfield environments and will continue to scale this program."*

### The transfer result

- Trained on **100% egocentric human video**, *"collected passively as people do behaviors in real Brookfield homes."*
- **"This approach required no robot demonstrations whatsoever."**
- **Speech-to-nav**: responds to *"Walk to the kitchen table"* / *"Go water the plants"*, "autonomously generating closed-loop control from pixels to navigate complex, cluttered home environments."
- **A single unified model**: "One Helix network now outputs both high rate dexterous manipulation and navigation commands — eliminating the need for separate, task-specific or data source-specific systems."
- The priority claim, quoted exactly: *"To our knowledge, this is the first time a humanoid robot has learned end-to-end — from images and language to **low-level SE(2) velocity commands** — using only human video. No robot-specific data or training was required."*

## Assessment

> [!note] Navigation is the one case where human→robot transfer is nearly free — and the claim is carefully scoped to it
> Read the priority claim's own wording: **"low-level SE(2) velocity commands."** SE(2) is planar position and heading. Two properties make this the cheapest possible instance of cross-embodiment transfer, and neither generalises to manipulation:
>
> 1. **The action space is close to embodiment-invariant.** A person walking to the fridge and a humanoid walking to the fridge trace nearly the same 2D path through the room. There is no morphology gap to bridge — no fingers, no gripper kinematics, no contact forces, no payload dynamics. The target output is a base velocity that means the same thing for both bodies.
> 2. **The action labels are recoverable from the video itself.** Egocentric video contains the camera's own motion; the SE(2) trajectory can in principle be extracted by visual odometry or SLAM, with no annotation and no teleoperation rig. That is very likely *why* "no robot demonstrations whatsoever" was achievable here — see [visual relocalization and mapping](../concepts/robotics/visual-relocalization-and-mapping.md).
>
> **Figure never says which mechanism it used**, so (2) is inference, not reporting. But the scoping is not accidental: a company that had solved human→robot transfer for *manipulation* would not have announced the navigation case.

> [!warning] The unified-model claim and the transfer claim are about different things
> "One Helix network now outputs both manipulation and navigation" is a claim about **architecture**. "Trained on 100% human video with no robot demonstrations" is a claim about the **navigation half only** — Helix's manipulation ability came from ~500 h of teleoperation ([Helix](helix-blog.md)). The post's title, *"Direct Human-to-Robot Transfer"*, invites reading the second claim as covering the first. It does not.

> [!note] Chronology against the literature
> Go-Big (2025-09-18) **predates [EgoScale](egoscale-paper.md)** (NVIDIA GEAR, 2026-02-18) by five months. Figure got a human-video-only transfer result out first; NVIDIA published the **fitted scaling law and the recipe** — on **dexterous manipulation**, the hard case — later. The pair is a clean illustration of the wiki's recurring asymmetry: Figure ships and announces, the labs measure and publish. Anyone wanting to *reproduce* human→robot transfer has EgoScale to work from and nothing usable from Go-Big.

> [!warning] Filming inside homes, mediated by the landlord
> Data is *"collected passively as people do behaviors in real Brookfield homes."* Brookfield is the **owner** of those units, and also an **investor in Figure's Series C** ([partnership post](figure-brookfield-partnership.md)) — so the data supplier is not an arm's-length counterparty. Neither post says whether the units are occupied or vacant, who is being filmed, who consented, on what terms, or what happens to footage of non-participants. This is the same gap the wiki flagged on [Index](../entities/figure-index.md), 11 months earlier and inside dwellings Figure's partner is the landlord of. See [crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md).

> [!warning] Not a single number
> No dataset size (hours, episodes, units covered). No success rate for the navigation policy. No baseline. No comparison against a robot-demo-trained navigation policy — the one experiment that would size what the human video actually bought. No failure modes. Nothing about how a human's eye-height egocentric view is reconciled with Figure 03's camera placement.

## Entities mentioned

- [Figure](../entities/figure.md) · [Helix](../entities/helix.md) · [Brookfield](../entities/brookfield.md) · [Index](../entities/figure-index.md) · [Figure 03](../entities/figure-03.md)

## Concepts touched

- [Scaling laws — VLAs and human data](../concepts/learning/scaling-laws-vla.md) — the thesis; EgoScale is the quantified counterpart.
- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md) — Go-Big is the landlord-mediated precursor to Index's open marketplace.
- [Visual relocalization and mapping](../concepts/robotics/visual-relocalization-and-mapping.md) — the likely (unstated) source of SE(2) labels from raw video.
- [VLA models](../concepts/learning/vla-models.md) — one network emitting both manipulation and navigation.

## Open questions

- **How are the SE(2) action labels obtained from human video?** The single most useful thing the post could have said, and it says nothing.
- **How is the human→robot viewpoint gap handled?** Different eye height, different camera intrinsics, different gait-induced motion.
- **Is there a manipulation equivalent?** As of 2026-08-28, no — and [Index](../entities/figure-index.md), which is overwhelmingly a manipulation corpus, still ships with no transfer story.
- **How much human video?** Never stated, here or in Index.
- **Consent, occupancy and data rights in Brookfield residential units.**
- **Did Go-Big's navigation policy survive into [Helix 02](figure-helix-02.md)?** Helix 02's loco-manipulation is trained differently (System 0 on retargeted motion capture); the relationship to Go-Big's navigation policy is never addressed.
