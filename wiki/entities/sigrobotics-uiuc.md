---
title: SIGRobotics-UIUC
type: entity
subtype: organization
created: 2026-05-10
updated: 2026-05-11
sources: 4
tags: [sigrobotics, uiuc, student-organization, lekiwi, open-hardware, lerobot, hackathon, mini-humanoid, koch-arms, frodobots]
---

**SIGRobotics-UIUC** — student-run robotics special-interest group within ACM @ UIUC. Website: [sigrobotics.acm.illinois.edu](https://sigrobotics.acm.illinois.edu); GitHub org: [github.com/SIGRobotics-UIUC](https://github.com/SIGRobotics-UIUC) (~25 public repos). Best known in this wiki for designing **[LeKiwi](lekiwi.md)** (1,300+ GitHub stars; Apache 2.0; CAD in Fusion 360) and for **winning the U.S. (Mountain View) site of the [October 2025 Seeed × NVIDIA × Hugging Face Embodied AI Hackathon](../sources/seeed-embodied-ai-hackathon-2025-recap.md)** with a matcha-making bimanual XLeRobot driven by a GR00T-N1.5 policy.

## Projects

### Flagship (listed on the projects page)

- **[LeKiwi](lekiwi.md)** — sub-$1k 3-wheel holonomic Kiwi-drive mobile manipulator platform; default mounting target for the [SO-ARM101](so-arm101.md) arm in the [LeRobot](lerobot.md) ecosystem. Joint with [Hugging Face](hugging-face.md) LeRobot.
- **Robot Arms (Koch arms)** — 3D-printed Koch arms for tabletop manipulation via imitation learning. No public repo linked from the projects page.
- **Mini Humanoid** — locomotion-policy training on a 3D-printed humanoid. **Sponsored by [K-Scale Labs](k-scale-labs.md)** ([micro-sim repo](https://github.com/SIGRobotics-UIUC/micro-sim)). The K-Scale sponsorship is significant — K-Scale was funding SIGRobotics' humanoid work even as it ran out of Series-A runway in late 2025.
- **TB3 Mobile Manipulator** — Turtlebot3-based "get-us-coffee" project. Sponsored by UIUC CDS (exact expansion not given).

### Other active projects (from GitHub org, not on the projects page)

- **Matcha-bot / `seeed-hack-interface`** (Oct 2025) — U.S.-site champion at the Embodied AI Hackathon. Built on [XLeRobot](xlerobot.md); fine-tuned **[NVIDIA GR00T N1.5](nvidia-groot.md)** via NVIDIA Brev; deployed on Jetson Thor. Companion repo: [`Isaac-GR00T-UIUC`](https://github.com/SIGRobotics-UIUC/Isaac-GR00T-UIUC).
- **F1Tenth** — autonomous racing stack; sub-team within SIG.
- **Climbing Robot** — defies gravity (per repo description).
- **Earth Rover Mini SDK** — public Python SDK on PyPI for [FrodoBots](https://www.frodobots.ai/)' Earth Rover Mini+ platform. (FrodoBots is a top-tier sponsor.)
- **Bimanual SO-101 setup** — [`lerobot_robot_bi_so101_follower`](https://github.com/SIGRobotics-UIUC/lerobot_robot_bi_so101_follower) + [`lerobot_teleoperator_bi_so101_leader`](https://github.com/SIGRobotics-UIUC/lerobot_teleoperator_bi_so101_leader). Direct lineage to the matcha-bot.
- **`silent_speech`** — code for the EMG-decoding-of-silent-speech papers (EMNLP 2020 / ACL 2021). Suggests an HCI / accessibility predecessor thread.

## Sponsors

Top tier: **[FrodoBots](https://www.frodobots.ai/)**, **BitRobot Foundation**, **Saronic** (autonomous maritime).
Normal tier: **[Hugging Face](hugging-face.md) LeRobot**, **Neuralink**, **ROBOTIS** (Dynamixel-servo manufacturer), **UIUC CS / Siebel School**.

The **K-Scale Labs sponsorship of Mini Humanoid** is project-tier, not org-tier — i.e., it's named on the Mini Humanoid project card, not in the general sponsor list.

## Core contributors

- **CAD**: Manav Chandaka, Bhargav Chandaka, Pepijn Kooijmans
- **Software**: Pepijn Kooijmans, Gloria Wang, Bhargav Chandaka, Advait Patel

## Distribution

- Hardware sales: [Seeed Studio](seeed-studio.md) bazaar
- Software framework upstream: [LeRobot](lerobot.md) / [Hugging Face](hugging-face.md)
- Community: Discord (LeRobot server, `#mobile-so100-arm`)

## Why it matters in this wiki

UIUC has two assistive-robotics-relevant student/lab efforts now indexed: SIGRobotics (this entity, low-cost mobile manipulation) and the [Katherine Driggs-Campbell](katherine-driggs-campbell.md) lab (assistive navigation, [DRAGON](../sources/dragon-assistive-nav-2024.md)). The two are independent but illustrate UIUC's footprint in accessible / assistive robot platforms.

## Related

- [LeKiwi](lekiwi.md)
- [LeRobot](lerobot.md)
- [Seeed Studio](seeed-studio.md)

## Mentioned in

- [LeKiwi GitHub](../sources/lekiwi-github.md)
- [Seeed Studio LeRobot LeKiwi Wiki](../sources/seeed-lekiwi-wiki.md)
- [Seeed × NVIDIA × HF Embodied AI Hackathon 2025 Recap](../sources/seeed-embodied-ai-hackathon-2025-recap.md)
- [SIGRobotics (ACM @ UIUC) — Projects page](../sources/sigrobotics-uiuc-projects-page.md)

## Open questions / TBD

- Org-level governance / succession plan as core contributors graduate (typical risk for student-run hardware projects).
- Relationship (if any) to Driggs-Campbell's HRI lab at UIUC — possibly none.
- Why does **Neuralink sponsor SIGRobotics?** Plausible technical bridge is the `silent_speech` EMG-decoding repo, but the relationship is not explained on the projects page.
- "UIUC CDS" (Mini Humanoid + TB3 sponsor) — exact expansion not given on the page; best guesses are Coordinated Science Lab or Computational Data Sciences.
