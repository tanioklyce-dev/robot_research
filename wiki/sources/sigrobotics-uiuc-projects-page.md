---
title: "SIGRobotics (ACM @ UIUC) — Projects page"
type: source
url: https://sigrobotics.acm.illinois.edu/projects
github_org: https://github.com/SIGRobotics-UIUC
author: SIGRobotics-UIUC (student org)
published: rolling (website continuously updated)
ingested: 2026-05-11
tags: [sigrobotics, uiuc, student-organization, lekiwi, lerobot, k-scale-labs, hugging-face, neuralink, frodobots, micro-sim, mini-humanoid, koch-arms, turtlebot3, f1tenth]
---

> [!note] Source extraction note
> `sigrobotics.acm.illinois.edu` is a React single-page app hosted on GitHub Pages with a `CNAME` from the `SIGRobotics-UIUC` org. The `/projects` path returns HTTP 404 from the static host because GitHub Pages doesn't know about SPA client-side routes — but the project, sponsor, and team data is hard-coded into the JS bundle (`/static/js/main.e69055b8.js`). Content below was extracted from the JS bundle directly. Bundle hash may change as the site is rebuilt; re-check on the next ingest.

## Summary

The official projects page of **[SIGRobotics-UIUC](../entities/sigrobotics-uiuc.md)**, the student-run robotics SIG within ACM @ UIUC. Lists **four ongoing flagship projects** and **seven sponsoring organizations**. The page complements but doesn't fully reflect the GitHub org — the public repos at `github.com/SIGRobotics-UIUC` include ~10 additional projects (matcha-bot from the October 2025 hackathon, F1Tenth racing, climbing robot, Earth Rover Mini integration, etc.) that aren't surfaced on the projects page.

This is the **first wiki ingest of a research / student-org institutional landing page** — useful for grounding the group's actual scope beyond the [LeKiwi](../entities/lekiwi.md) work the wiki had already filed.

## Projects (per the website)

| Project | Description | Status | Notes |
|---|---|---|---|
| **[LeKiwi](../entities/lekiwi.md)** | Open-source, low-cost mobile manipulator. "A SIGRobotics × Hugging Face LeRobot collaboration." | Ongoing | The org's flagship — [github.com/SIGRobotics-UIUC/LeKiwi](https://github.com/SIGRobotics-UIUC/LeKiwi). Already extensively covered in the wiki. |
| **Robot Arms (Koch arms)** | 3D-printed Koch arms for table-top manipulation via [imitation learning](../concepts/imitation-learning.md). | Ongoing | No public repo linked from the projects page. Koch arms are an open-hardware lineage that pre-dates SO-100. |
| **Mini Humanoid** | Training locomotion policies on the org's own 3D-printed humanoid. **Sponsored by [K-Scale Labs](../entities/k-scale-labs.md).** | Ongoing | Repo: [github.com/SIGRobotics-UIUC/micro-sim](https://github.com/SIGRobotics-UIUC/micro-sim) ("Training in simulation"). The K-Scale Labs sponsorship is **a new fact** for the wiki — K-Scale was funding UIUC humanoid-policy work even as it ran out of Series-A runway in late 2025. |
| **TB3 Mobile Manipulator** | "Get a Turtlebot3 to get us a cup of coffee." **Sponsored by UIUC CDS.** | Ongoing | No public repo. UIUC CDS = (best guess) Coordinated Science Lab or Computational Data Sciences, not stated explicitly. |

## Sponsors (per the website)

Tiered visually as "big" or "normal" in the bundle:

**Big sponsors (top tier):**
- **FrodoBots** (`frodobots.ai`) — explains the cluster of `earth-rover-mini-OpenSource`, `earthrover-lerobot-sdk`, `Earthrover-OpenSource-SDK`, `earth_rover_mini_sdk`, and `LeRobot_Earth_Rover_Mini` repos in the GitHub org. The relationship is "SIG-as-SDK-builder for FrodoBots' rover platform."
- **BitRobot Foundation** (`bitrobot.ai`)
- **Saronic** (`saronic.com`) — autonomous-maritime startup

**Normal sponsors:**
- **Hugging Face LeRobot** — confirms the wiki's existing understanding that SIGRobotics is a deliberate LeRobot-ecosystem partner
- **Neuralink** — surprising; not an obvious match. Possibly tied to the `silent_speech` (EMG-from-silent-speech) work in the GitHub org
- **ROBOTIS** (`en.robotis.com`) — Dynamixel-servo manufacturer; consistent with the `DynamixelLeKiwi` LeKiwi variant in the repo
- **UIUC CS / Siebel School of Computing & Data Science** — university-level institutional sponsor

## Tagline

> "We are a student-run robotics special-interest group."
> — SIGRobotics homepage hero (`/`)

ACM Open House is mentioned as a recruiting venue.

## Additional projects visible in the GitHub org (not on the projects page)

The website lists 4 active projects; the GitHub org has **~25 public repos**. The most wiki-relevant ones *not* surfaced on the projects page:

- **[`seeed-hack-interface`](https://github.com/SIGRobotics-UIUC/seeed-hack-interface)** — "Web interface to interact with the **Matcha bot**" — i.e., the **frontend for the U.S.-site-champion matcha-making bimanual XLeRobot** at the [October 2025 Seeed × NVIDIA × HF Embodied AI Hackathon](seeed-embodied-ai-hackathon-2025-recap.md). Concrete artifact from the hackathon win.
- **[`Isaac-GR00T-UIUC`](https://github.com/SIGRobotics-UIUC/Isaac-GR00T-UIUC)** — their fork / fine-tune of [NVIDIA Isaac GR00T N1.5](../entities/nvidia-groot.md). Likely the codebase behind the matcha-bot win.
- **[`Climbing-Robot`](https://github.com/SIGRobotics-UIUC/Climbing-Robot)** / **`ClimbingRobot`** — "defy the laws of gravity by being able to achieve a [climbing motion]." (Two repos, possibly fork + variant.)
- **[`F1Tenth`](https://github.com/SIGRobotics-UIUC/F1Tenth)** — "autonomous racing stack for the SIGRobotics F1TENTH team at UIUC." — a *third* major project not represented on the projects page (alongside LeKiwi, Mini Humanoid, Koch arms, TB3, Earth Rover Mini, Matcha bot).
- **[`silent_speech`](https://github.com/SIGRobotics-UIUC/silent_speech)** — "Code for voicing silent speech from EMG. Official repository for the papers [EMNLP 2020 / ACL 2021]." Suggests an HCI / accessibility thread at the SIG predating their robotics focus.
- **`Physical-AI-Hackathon-Food-Team`** — another hackathon team's code; a separate hackathon thread from the matcha-bot one.
- **[`lerobot_robot_bi_so101_follower`](https://github.com/SIGRobotics-UIUC/lerobot_robot_bi_so101_follower)** + **[`lerobot_teleoperator_bi_so101_leader`](https://github.com/SIGRobotics-UIUC/lerobot_teleoperator_bi_so101_leader)** — the bimanual SO-101 leader/follower setup used at the hackathon.

The gap between the website's 4-project view and the GitHub org's 25-repo reality is itself informative: the website is a curated **flagship + sponsor pitch**, not a complete project catalog.

## Entities mentioned

- [SIGRobotics-UIUC](../entities/sigrobotics-uiuc.md) — the org itself
- [LeKiwi](../entities/lekiwi.md) — flagship project
- [LeRobot](../entities/lerobot.md) — software framework
- [Hugging Face](../entities/hugging-face.md) — sponsor
- [K-Scale Labs](../entities/k-scale-labs.md) — Mini Humanoid sponsor (**new sponsorship fact**)
- [NVIDIA GR00T](../entities/nvidia-groot.md) — `Isaac-GR00T-UIUC` repo lineage
- [Seeed × NVIDIA × HF Embodied AI Hackathon 2025 recap](seeed-embodied-ai-hackathon-2025-recap.md) — the matcha-bot context

## New entities surfaced (parked)

- **FrodoBots / Earth Rover Mini** — top-tier sponsor; SIG has ~5 repos around the Earth Rover platform. Worth a stub entity if the wiki picks up consumer / educational rover hardware as a thread.
- **BitRobot Foundation** — top-tier sponsor; unclear positioning at the moment.
- **Saronic** — autonomous maritime; unrelated to the wiki's current threads (home robotics, JEPA) — probably skip.
- **ROBOTIS / Dynamixel** — referenced via the `DynamixelLeKiwi` variant; could justify a stub if Dynamixel servos appear as a recurring component (they already do — SO-100 / SO-101 vs. Feetech STS3215 vs. Dynamixel is the basic actuator-choice axis).
- **Neuralink as SIGRobotics sponsor** — surprising; flagged but no clear action item.
- **Koch arms** — open-hardware arm lineage that precedes SO-100/SO-101. If the wiki ever does an arm-lineage timeline, Koch is a node.

## Concepts touched

- [Imitation learning](../concepts/imitation-learning.md) — Koch arms project framing.
- [Sim-to-real transfer](../concepts/sim-to-real-transfer.md) — implicit in Mini Humanoid (training in `micro-sim`).

## Open questions

- **What does "UIUC CDS" stand for?** Most likely the **Coordinated Science Laboratory (CSL)** or **Computational Data Sciences**, but the projects page doesn't expand it.
- **Why is Neuralink sponsoring SIGRobotics?** The `silent_speech` (EMG decoding) repo is a plausible technical bridge — Neuralink's BCI program overlaps with sub-vocal speech decoding — but the sponsorship isn't explained on the page.
- **Status of the climbing-robot project** — two repos exist; the projects page lists neither. Active or shelved?
- **Did SIGRobotics participate in the [LeRobot Worldwide Hackathon (June 2025)](lerobot-worldwide-hackathon-2025-winners.md) in addition to the October Embodied AI Hackathon?** Not visible from this page.
