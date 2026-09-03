---
title: VTAM (Video-Tactile-Action Model)
type: entity
subtype: model
created: 2026-09-02
updated: 2026-09-02
sources: 1
tags: [vtam, tactile, world-action-model, vla-models, contact-rich, manipulation, data-efficiency, uiuc]
---

**VTAM — Video-Tactile-Action Model** — adapts a pretrained video-action model into a **predictive backbone that ingests tactile images and predicts visual *and* tactile dynamics before acting**. From Ismini Lourentzou's group at the **University of Illinois Urbana-Champaign** (Haoran Yuan, Weigang Yi, Zhenyu Zhang et al.), presented at [Day 2 of the Chicago Booth world-modeling workshop](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) as *"VTAM: Video-Tactile-Action Models for Complex Physical Interaction Beyond VLAs."*

## The distinction it draws

Contact-aware manipulation has split into two branches, and VTAM belongs to the second:

| Branch | Shape | Failure |
|---|---|---|
| **Tactile-conditioned VLAs** | reactive policy with touch added as another observation | still weak state tracking |
| **Tactile world-action models** | jointly *predict* how tactile, visual and physical state will evolve, then act | VTAM |

The motivating failures are the ones cameras cannot see: a robot that misses the bowl and pours the ingredients onto the table anyway, and wiping that depends on contact pressure and slip. *"Those kinds of signals are weakly observable from cameras."*

## What is claimed

- **~10 minutes of teleoperated demonstrations per task**, with **no separately trained tactile encoder** and **no external wrist-mounted force sensor**.
- Predicts future tactile signals *"as faithfully as future video."*
- Tasks chosen for contact dependence: a crushable chip (delicate force) and whiteboard wiping (stable contact on a slippery surface).
- Vision-only baselines fail; reactive tactile methods reach ~50% on wiping. VTAM reports a higher **stable-contact ratio** — smoother contact dynamics, no excessive pressure.

## Why it matters here

This is the wiki's first instance of tactile sensing entering a [world-action model](../concepts/world-models/world-action-model.md) rather than a policy's observation vector. The wiki's [VLA](../concepts/learning/vla-models.md) coverage repeatedly hits the same wall — policies that look right and fail on contact — and the wiki's [dexterous tool manipulation](../concepts/robotics/dexterous-tool-manipulation.md) page records [SimToolReal](../sources/simtoolreal-paper.md) attributing **43.7% of real failures to pose-tracking loss**, i.e. perception rather than control. VTAM attacks that from the touch side, and does it with a data budget (10 min/task) that is plausible for a home-robot project.

## Related
- [World action model](../concepts/world-models/world-action-model.md) — the family.
- [VLA models](../concepts/learning/vla-models.md) — what it argues past.
- [Dexterous tool manipulation](../concepts/robotics/dexterous-tool-manipulation.md).

## Mentioned in
- [Third World Modeling Workshop — Day 2](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — lightning talk, session 3.

> [!note] Thin entity
> Five-minute talk, no paper ingested, no absolute success rates given for VTAM itself — only relative statements and the baseline's ~50%. Treat the numbers as indicative.
