---
title: Long-term in-home robot deployments — what we know
type: synthesis
created: 2026-05-09
updated: 2026-07-09
tags: [in-home, deployment, longitudinal, henry-evans, stretch, hcrlab, rum, ok-robot, hello-robot, assistive-robotics]
---

What does the wiki actually know about deploying mobile manipulators in real homes for sustained periods? Most robot-learning papers report controlled-lab evaluation. A small set of sources cross into actual home environments — sometimes for hours, sometimes for years. This synthesis pulls them together, sorts them by deployment depth, and surfaces what the longitudinal evidence does and does not say.

> [!note] TL;DR
> There are two distinct deployment shapes in the wiki: **broad-and-shallow** (RUM, OK-Robot — many homes, brief visits) and **narrow-and-deep** (HCR Lab Henry Evans — three summers in one home, expanding task set; Nanavati 2025 — five days in-home with one community researcher). Together they cover ~50 unique homes in evaluation, but only **one home has ≥1 month of deployment data**: Henry and Jane Evans's, with Stretch.

---

## The deployments, sorted by depth

| Depth | Source | Platform | Homes | Duration | Tasks | Outcome |
|---|---|---|---|---|---|---|
| **Years (longitudinal)** | [HCR Lab + Hello Robot Henry Evans deployments](../../sources/maya-cakmak-research.md) | [Stretch](../../entities/stretch.md) | 1 | Summers 2021, 2022, 2023 — ~4 weeks each, 3 years recurring | Self-feeding, face wiping, scratching, lotion, percussion vest, printer, card games with granddaughter, handing a rose to wife Jane. EUP tool prototyped specifically for Henry in summer 2022. | Restored agency; reduced caregiver burden; expanding task set each year. Continuing under NIH grant. |
| **Days (in-home)** | [Nanavati et al. 2025](../../sources/nanavati2025-feeding-out-of-lab.md) | [Kinova JACO](../../entities/kinova-jaco.md) 6-DOF + custom F/T fork (~$50k) | 1 | 5 days, 10 meals | Self-feeding in real home contexts — multiple meals, multiple environments within the home. | CR2 fed himself across diverse contexts; HRI 2025 Best Systems Paper Finalist. Earliest in-home deployment of an open-source feeding system. |
| **Day** | [IEEE Spectrum — Stretch assistive](../../sources/ieee-spectrum-stretch-assistive.md) (2023) | [Stretch](../../entities/stretch.md) | 1 (Henry Evans) | Snapshot reporting | Scratching, blanket moves, retrieving items, transporting laundry, cards, meals, delivering flowers. | Public narrative documentation of the assistive use case; predates the HCR Lab summer-deployment papers. |
| **Hours per home (broad)** | [Robot Utility Models Paper (Etukuru et al. 2024)](../../sources/robot-utility-models-paper.md) | [Stretch](../../entities/stretch.md) | 25 evaluation homes (5 per task × 5 tasks) | Hours each (10 trials/env, 1.31 avg retries) | Door opening, drawer opening, reorientation, tissue pickup, bag pickup. | 90% average success (74.4% raw + 15.6% mLLM-retry). Cross-embodiment to xArm 7: −10pt drop. |
| **Hours per home (broad)** | [OK-Robot project page](../../sources/ok-robot-project-page.md) | [Stretch](../../entities/stretch.md) | 10 NYC homes | Hours per home; 171 pick-and-drop tasks total | Open-vocabulary pick-and-drop. | 58.5% overall; 82% in uncluttered homes. Top failure: semantic memory retrieval, manipulation poses, hardware. |
| **Studio environment (single-shot)** | [HomeRobot / OVMM](../../sources/ovmm-homerobot.md) | [Stretch](../../entities/stretch.md) | Single-platform real eval | Per-rollout | "Move [object] from [start] to [goal]." | 20% real-world baseline. Predecessor benchmark to OK-Robot. |
| **Lab + simulated homes** | [BEHAVIOR-1K Challenge 2025](../../sources/stanford-hai-ai-index-2026.md) | Various | Simulated only | — | 1,000 household tasks | 12.4% top team full success; 26% Q-score (partial credit). |

---

## Five things the longitudinal evidence shows

### 1. The same robot does very different things across years
Henry Evans's deployment progresses from basic fetch / hand-to-mouth in 2021, through user-specific EUP tooling in 2022, to broader social tasks (granddaughter, student visitor) in 2023 ([Maya Cakmak Research](../../sources/maya-cakmak-research.md)). The capability frontier expanded *because* the platform was the same; the engineering effort accumulates. This is the strongest argument in the wiki for the value of long-term partnerships over multi-home cross-sectional studies.

### 2. Off-nominals dominate real-world deployment
[Nanavati et al. 2025](../../sources/nanavati2025-feeding-out-of-lab.md) Lesson 2 is direct: *"off-nominals will arise."* Five days, ten meals, one user, and the variable-LoC interface earned its keep — the user could escalate to teleoperation when the autonomous mode hit something unexpected, rather than ending the session. Lab evaluations of feeding systems do not surface these because the lab doesn't have unexpected events. This is an under-quantified phenomenon: every hour of in-home deployment generates more off-nominals than every hour of lab eval.

### 3. Reliability degrades from controlled to real, and again from short to long
The reliability gradient across the wiki (within a single platform — Stretch — and adjacent task families):

- RLBench (controlled sim, short-horizon): 89.4% ([Stanford HAI](../../sources/stanford-hai-ai-index-2026.md))
- RUM evaluation (25 novel homes, hours each, with mLLM retry): 90% ([Etukuru et al. 2024](../../sources/robot-utility-models-paper.md))
- RUM raw (no retry): 74.4%
- OK-Robot, 10 homes: 58.5%; in uncluttered homes alone: 82%
- BEHAVIOR-1K (1,000 realistic household tasks): 12.4%
- HomeRobot/OVMM (open-vocabulary pick-and-place): 20%

The 90% RUM number is the wiki's high-water mark for **broad real-home deployment**. It is real — and it is also the result of (a) restricting to five well-shaped pick-and-place-like tasks and (b) adding an mLLM retry loop. The longitudinal Henry Evans deployments do not have a comparable reliability number because the metric category isn't well-defined for "uses Stretch over a summer."

### 4. Diversity of homes generalizes; depth of deployment surfaces what generalization missed
RUM's "diversity > quantity" finding (25 demos × 40 environments beats 200 × 5; [RUM paper §ablations](../../sources/robot-utility-models-paper.md)) is the strongest evidence for breadth. But the HCR Lab summers and the Nanavati 2025 in-home study are where you see what *broad-trained policies still don't handle*: a particular kitchen layout, a particular caregiver routine, a particular user's preferred object positions, environments with specific lighting and clutter. These are the regimes where personalization (per-user EUP, per-home tuning) starts to matter more than per-task generalization.

### 5. The deployments cluster around Stretch
Of the seven deployment-shape rows in the table above, **six use Stretch**. The seventh (Nanavati 2025 feeding) is on Kinova JACO because the form factor — a single arm at face height — fits the feeding task better. The pattern is unambiguous: *if you want to do real-home work in 2024–2026, you use Stretch.* Discussed at length in [Stretch as the de-facto assistive-robotics platform](stretch-as-assistive-platform.md).

---

## What's missing from the longitudinal record

- **Demographics.** Henry Evans's case is well-documented and influential. We have one person × one home × one disability profile (C4–C5 quadriplegia from stroke). The longitudinal record is one data point. Even Nanavati 2025's in-home study is one community researcher.
- **Failure mode taxonomy across years.** The HCR Lab summer deployments are described narratively, not analytically. There is no published taxonomy of what failed across summer 2021 → 2022 → 2023, what improved, what didn't, and why. This is a gap a future paper could fill from the existing data.
- **Caregiver-side measurements.** The IEEE Spectrum story documents caregiver burden (Jane Evans) qualitatively. Quantified caregiver-time-saved data across the three summers would be high-value.
- **Cross-platform comparisons.** Every long deployment is on Stretch (or Kinova JACO for Nanavati 2025). The wiki has no multi-month deployment data on Reachy 2, 1X NEO, Unitree G1, or any humanoid. The longitudinal robot-deployment landscape is currently single-platform.

---

## What an independent researcher could do

1. **Document a second long-term deployment.** A different user, different disability profile, different home, on Stretch (since the platform is open and supported). Even a four-week deployment with a structured weekly diary would double the longitudinal record. The HCR Lab CBPR methodology ([Nanavati et al. 2024 — Multiple Ways](../../sources/nanavati2024-multiple-ways-par.md)) is an explicit guide.
2. **Build a longitudinal failure taxonomy from existing data.** Henry Evans's summers 2021–2023 are documented across narrative pages, IEEE Spectrum, and likely internal HCR Lab notes. Surfacing a structured "what failed when" taxonomy would surface generalizable engineering lessons.
3. **Caregiver-time instrument.** Lightweight self-report or sensor-based instrument to measure caregiver intervention frequency across robot-active and robot-inactive periods. Currently no published study uses one.
4. **Cross-platform short-deployment comparison.** Two weeks each on Stretch and Reachy 2 in the same home, same user, same task list. Would surface platform-specific failure modes that single-platform deployments hide.

---

## Sources used in this synthesis

- [Maya Cakmak — Research Overview](../../sources/maya-cakmak-research.md) — Henry Evans summers 2021–2023.
- [HCR Lab Publications](../../sources/hcrlab-publications.md) — corroborating publication record.
- [IEEE Spectrum — Stretch assistive robot](../../sources/ieee-spectrum-stretch-assistive.md) — Henry Evans narrative documentation.
- [Feeding System Out-of-lab (Nanavati et al. 2025)](../../sources/nanavati2025-feeding-out-of-lab.md) — five days in-home.
- [Robot Utility Models Paper (Etukuru et al. 2024)](../../sources/robot-utility-models-paper.md) — 25 evaluation homes; cross-embodiment.
- [OK-Robot Project Page](../../sources/ok-robot-project-page.md) — 10 NYC homes.
- [HomeRobot / OVMM](../../sources/ovmm-homerobot.md) — 20% baseline.
- [Stanford HAI AI Index 2026](../../sources/stanford-hai-ai-index-2026.md) — RLBench / BEHAVIOR-1K reference points.
- [Multiple Ways of Working with Users (Nanavati et al. 2024)](../../sources/nanavati2024-multiple-ways-par.md) — CBPR methodology.

## Related

- [Stretch as the de-facto assistive-robotics platform](stretch-as-assistive-platform.md) — why every long deployment uses Stretch.
- [Levels of autonomy in assistive robotics](levels-of-autonomy-in-assistive-robotics.md) — the autonomy design pattern these deployments converge on.
- [Assistive robotics — R&D landscape and JEPA applicability](assistive-robotics-research-landscape.md) — broader R&D context.
- [Assistive robotics](../../concepts/robotics/assistive-robotics.md) — concept overview.
- [Robot safety standards](../../concepts/robotics/robot-safety-standards.md) — ISO 13482 ("mobile servant robot") is the certification/CE pathway an in-home deployment would face, and its deterministic-safety-function machinery is unresolved for learned policies.
