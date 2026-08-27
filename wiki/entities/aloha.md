---
title: ALOHA / Mobile ALOHA
type: entity
subtype: product
created: 2026-05-25
updated: 2026-08-26
sources: 15
tags: [aloha, mobile-aloha, bimanual, mobile-manipulation, teleoperation, viperx-300, stanford, low-cost, open-source, act-plus-plus]
---

**ALOHA** ("A Low-cost Open-source HArdware system") — Stanford's **low-cost bimanual puppeteering teleoperation platform**, built around 4× Trossen [ViperX 300](viperx-300.md) arms (2 leaders + 2 followers). Introduced in 2023 by **Zhao, Kumar, Levine, Finn** as the data-collection rig for [ACT](act.md). Defines the academic-budget reference for bimanual robot teleoperation.

**Mobile ALOHA** — 2024 extension that adds an **AgileX Tracer differential-drive wheeled base** + a whole-body teleoperation interface in which the operator is **physically tethered to the base** and backdrives the wheels by walking. **Total system cost: $32k including onboard power + compute** — comparable to a single Franka Panda arm, ~6× cheaper than a PR2 or TIAGo.

## Hardware

| Spec | Mobile ALOHA |
|---|---|
| Arms | 4× [ViperX 300](viperx-300.md) (2 leaders + 2 followers); 6 DOF each |
| DOF (action) | 14 arms + 2 base = **16-dim** |
| Base | AgileX Tracer ($7k; differential drive; 1.6 m/s; 100 kg payload; 10 mm step / 8° slope) |
| Cameras | 3× Logitech C922x RGB (2 wrist + 1 top); 480×640 @ 50 Hz |
| Compute | Intel i7-12800H + RTX 3070 Ti (8 GB VRAM) |
| Battery | 1.26 kWh (14 kg, doubles as ballast); ~12 hr |
| Reach | 65–200 cm vertical; 100 cm horizontal |
| Payload | 750 g/arm; 1.5 kg combined; 100 N pull at 1.5 m |
| Total weight / footprint | 75 kg / 90×135 cm (with leaders) |
| Top base speed (autonomous) | 1.42 m/s |
| Repeatability / accuracy | 1 mm / 5–8 mm |
| Total cost | **$32k** |

## Design contributions ([source](../sources/mobile-aloha-paper.md))

1. **Bimanual puppeteering teleop** — leader-follower kinematic mirroring with two arms; user moves leader arms, followers track in joint space.
2. **Untethered onboard compute + power** — consumer-laptop class, 12 hr battery.
3. **Whole-body teleop via waist tether + wheel backdrive** — both hands are already on the leader arms, so the user walks while controlling arms, and the base follows passively. Tether provides coarse haptic feedback on base collisions. Detachable for autonomous execution.
4. **Forward-facing arm mount** (vs original ALOHA's inward-facing) — expands ergonomic workspace.

## Software / data

- Fully open-source: hardware + software + tutorials (3D printing, assembly, install) at https://mobile-aloha.github.io ([project page source](../sources/mobile-aloha-project-page.md)).
- **Hardware code**: https://github.com/MarkFzp/mobile-aloha (BOM + assembly + drivers).
- **ML code**: https://github.com/MarkFzp/act-plus-plus — named **[ACT++](act-plus-plus.md)**, the mobile-extended successor to the original [ACT](act.md) codebase.
- Static-ALOHA dataset: **825 demonstrations** across ~12 disjoint tabletop tasks; released via the [RT-X embodied dataset collection](../sources/mobile-aloha-paper.md).
- Mobile-ALOHA in-domain datasets: 20–50 demos per task across 7 evaluated tasks. Hosted on Google Drive (link on project page).

## Why it matters in this wiki

- **The bimanual-mobile-manipulation reference platform.** Mobile-manipulation coverage previously consisted of single-arm [Stretch](stretch.md) (lift + telescoping arm), [TurtleBot](turtlebot.md) (no arm), and stationary bimanual [Reachy](reachy.md). Mobile ALOHA is the academic-budget bimanual-mobile reference.
- **Validates the co-training pattern at small scale.** 825 static demos + 20–50 in-domain → +90% absolute on hard mobile-manipulation tasks ([source](../sources/mobile-aloha-paper.md), Table 1). Same compound-the-data pattern as [RUM data-diversity](robot-utility-models.md) and [EgoScale human-video pretraining](../sources/egoscale-paper.md), but at the scale a single lab can actually reproduce.
- **Open-source, $32k, hour-scale teleop session** — the practical reproducibility envelope is wider than most "low-cost" platforms.

## People

- **[Zipeng Fu](zipeng-fu.md)** — Mobile ALOHA co-lead; Stanford CS PhD; Stanford Graduate Fellowship.
- **[Tony Z. Zhao](tony-zhao.md)** — Mobile ALOHA co-lead; **first author on original ALOHA + ACT**.
- **[Chelsea Finn](chelsea-finn.md)** — senior author.

## Downstream projects

- **[Grievous](grievous.md)** ([source](../sources/grievous-github.md)) — Alex Koven's in-progress "cheap, human-like, fully-autonomous testbed" explicitly building on Mobile ALOHA + [XLeRobot](xlerobot.md) + [LeRobot](lerobot.md). First wiki-tracked attempt to cost-reduce Mobile ALOHA from $32k toward the [XLeRobot](xlerobot.md) tier.

## Related
- [ACT (Action Chunking Transformer)](act.md) — the IL method introduced alongside original ALOHA; the platform's default policy class.
- [ACT++](act-plus-plus.md) — the mobile-extended ML codebase shipped with Mobile ALOHA.
- [Diffusion Policy](diffusion-policy.md) — alternative IL method evaluated on Mobile ALOHA.
- [ViperX 300](viperx-300.md) — the underlying 6-DOF arm SKU.
- [Imitation learning](../concepts/learning/imitation-learning.md) — concept the platform is built around.
- [Stretch](stretch.md) — single-arm mobile-manip contrast; cited in Mobile ALOHA's related-work as having no bimanual / whole-body teleop interface.
- [Franka Panda](franka-panda.md) — cost reference (one Mobile ALOHA ≈ one Panda arm).
- [Grievous](grievous.md) — first downstream-of-Mobile-ALOHA cost-reduction effort.

## Mentioned in
- [Mobile ALOHA Paper](../sources/mobile-aloha-paper.md)
- [Mobile ALOHA Project Page](../sources/mobile-aloha-project-page.md)
- [Grievous GitHub](../sources/grievous-github.md) — design ancestor.
- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — **ALOHA-2** (Aldaco et al. 2024) is one of 8 natively-supported [LeRobot](lerobot.md) platforms, listed at **~€21k** (Table 1a) — the premium bimanual tier, ~40× the cost of SO-100 bimanual (€550). ALOHA-2 paper: arxiv 2405.02292.
- [Gemini Robotics 2: Safety Evaluations](../sources/gemini-robotics-2-safety-report.md) — ALOHA tabletop scenes are the visual substrate for ASIMOV-Agentic's safety-constraint-following component.
- [Building Worlds That Train Robots (R2S2R)](../sources/world-labs-r2s2r.md) — World Labs' most-used demo platform: bimanual box packing and elastic cable insertion for [real-to-sim](../concepts/robotics/real-to-sim-to-real.md) reconstruction, and the **bimanual cube-handover task** used for the sim-vs-real policy-ranking result (2,000 simulated / 100 real trials per checkpoint).
