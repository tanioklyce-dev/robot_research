---
title: "2025 Embodied AI Hackathon Recap — We Built Home & Cooking Robots! (Seeed × NVIDIA × Hugging Face)"
type: source
url: https://www.seeedstudio.com/blog/2025/11/06/2025-embodied-ai-hackathon-recap-we-built-home-cooking-robot/
mirror_url: https://www.seeed.cc/post/2025-embodied-ai-hackathon-recap
event_dates: 2025-10 (Shenzhen + Mountain View, two-site weekend hackathons)
published: 2025-11-06
ingested: 2026-05-11
author: Seeed Studio (corporate blog)
tags: [hackathon, seeed-studio, nvidia, hugging-face, lerobot, xlerobot, groot, jetson-thor, so-arm101, smolvla, home-robotics, cooking-robot, dual-site, embodied-ai]
---

> [!note] Source access
> The Seeed Studio blog URL is behind Cloudflare bot-protection at fetch time. Content for this ingest was extracted via Seeed's mirror (`seeed.cc/post/2025-embodied-ai-hackathon-recap`) and triangulated against a [Hackster.io contest page](https://www.hackster.io/contests/embodiedAI) (judges, prize structure for the precursor March 2025 event) and a [Hackster.io winners announcement](https://www.hackster.io/news/embodied-ai-hackathon-winners-announced-2dc69c76942e) (precursor March 2024 event). Direct fetch should be re-attempted in a normal browser to verify quotes flagged below.

## Summary

A two-site, **October 2025** weekend hackathon held simultaneously in **Shenzhen, China** and **Mountain View, USA**, co-organized by **[Seeed Studio](../entities/seeed-studio.md), [NVIDIA](../entities/nvidia.md), and [Hugging Face](../entities/hugging-face.md)**. Theme: **"Home Task and Cooking Robots."** **700+ developers registered**, **30+ teams participated** (~15 per site). Every winning project this wiki cares about ran on **[LeRobot](../entities/lerobot.md)** with **SO-ARM101** or **[XLeRobot](../entities/xlerobot.md)** hardware and used a **VLA policy** (GR00T N1.5, SmolVLA, ACT, or π0-class) as its core. **Sister event to the [LeRobot Worldwide Hackathon (June 2025)](lerobot-worldwide-hackathon-2025-winners.md)** — Hugging Face, Seeed, and the LeRobot ecosystem ran *two* major embodied-AI hackathons in 2025; this is the larger-budget, more-corporate-aligned one.

This source is the **first wiki ingest of a hackathon where NVIDIA's GR00T N1.5 and Jetson Thor were the headline platforms** — a useful signal of where the "VLA + small-form-factor robot" stack is being pushed by industry.

## Key claims

### Event
- **Dates**: October 2025 (exact day-range not specified in the recap).
- **Format**: two synchronous physical sites — **Shenzhen, China** and **Mountain View, USA** (Circuit Launch venue). Weekend hackathon (~48 hr).
- **Organizers**: **Seeed Studio + NVIDIA + Hugging Face** (tri-host).
- **Mentor / judge / partner roster**: NVIDIA, Hugging Face, **[K-Scale Labs](../entities/k-scale-labs.md)**, **[XLeRobot](../entities/xlerobot.md) (Vector Wang's project)**, **Lightwheel**, **Solo Tech**, **Fashion Star (FashionStar / StarAI)**, **Circuit Launch** (Mountain View venue).
- **Participation**: 700+ developers registered; ~30 teams across both sites (15 per site).
- **Theme statement**: "Design Home Task and Cooking Robots" — operate in **HOME scenes** (manipulation in kitchens, tabletop chores, soft-textile handling).

### Hardware platforms used
- **[SO-ARM101](../entities/so-arm101.md)** (Hugging Face LeRobot 6-DOF arm) — the bulk of single-arm projects.
- **[XLeRobot](../entities/xlerobot.md)** dual-arm mobile manipulator — multiple winning teams.
- **FashionStar StarAI** robot arms — alternative arm vendor.
- **[LeKiwi](../entities/lekiwi.md)**-style mobile bases (via XLeRobot composition).
- **NVIDIA Jetson Thor** developer kit with **JetPack 7 SDK** — the on-robot compute platform for VLA inference. (First Jetson Thor appearance in this wiki.)
- **[NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md)** + [LeRobot](../entities/lerobot.md) framework on the software side.

### Winning projects

**U.S. site (Mountain View / Circuit Launch):**

| Rank | Team / project | Hardware | Policy / approach |
|---|---|---|---|
| 🥇 Champion | **UIUC SIGRobotics — Matcha-making bimanual robot** | [XLeRobot](../entities/xlerobot.md) (dual-arm) | **[GR00T N1.5](../entities/nvidia-groot.md)** fine-tuned via NVIDIA Brev; deployed on Jetson Thor. Task: pour matcha powder, add water, whisk to make matcha tea. |
| 🥈 1st runner-up | **Sprinkle Robot** (Bruce Kim, Joon Kim, Peiqing Xia) | SO-ARM101 | Fine-tuned **SmolVLA** (170 episodes) for sugar-sprinkling automation. |
| 🥉 2nd runner-up | **Cloth Folding Robot** | Dual-arm SO-ARM101 | **ACT** model with **learned reward functions** for T-shirt folding. |

**China site (Shenzhen):**

| Rank | Team / project | Hardware | Policy / approach |
|---|---|---|---|
| 🥇 Champion | **Pick & Place with High Generalization** — desktop tidying | SO-ARM101 (single-arm) | **[GR00T N1.5](../entities/nvidia-groot.md)** fine-tuned on a **300-episode multi-source dataset** (90% real, 10% simulated with domain randomization). |
| 🥈 1st runner-up | **Soft Textiles Folding** — towel-folding | Dual-arm SO-ARM101 | (Policy unspecified in recap.) |
| 🥉 2nd runner-up | **Mate XLeRobot** — optimized dual-arm platform | [XLeRobot](../entities/xlerobot.md) variant | Hardware-modded: added **vertical lift-rail** (addresses XLeRobot's fixed-height limitation); VLA-based autonomy. Team: Ryan, Isaac, Qi, KAHO, Bubbles. |

### Technical signals worth noting
- **GR00T N1.5 was the dominant winning policy** across both sites (both champions). The hackathon is the strongest external signal yet that GR00T N1.5 is reaching the "fine-tunable on weekend-scale data" point.
- **SmolVLA** held up at the 1st-runner-up level with **170 episodes** of data — the data-economy story aligns with the [XLeRobot docs' SmolVLA recipe](xlerobot-docs.md) (~20 episodes for simpler tasks).
- **ACT + learned reward functions** is a notable departure from pure-BC ACT — the cloth-folding team layered RL-style reward shaping on top.
- **Mate XLeRobot's vertical lift-rail** directly addresses the **fixed-height workspace limitation** flagged in the XLeRobot docs (0.5–1.25 m). This is the first wiki-documented hardware modification of XLeRobot in the wild.
- **Datasets cited**: 150+ teleoperation episodes typical; 300-episode multi-source (90% real + 10% sim with DR) on the China champion.

### Relation to other 2025 hackathons in this wiki
- **[LeRobot Worldwide Hackathon (June 14–15, 2025)](lerobot-worldwide-hackathon-2025-winners.md)** — Hugging Face's primary community-wide hackathon: 400+ submissions, 916 registered members, 30 ranked teams. Prizes were *hardware* (Hope Jr Arm, LeKiwi, SO-101) rather than the GR00T / Jetson Thor stack used here.
- **The two events together establish 2025 as the inflection year** for community-scale LeRobot hackathons, with Seeed shifting from co-sponsor to co-organizer (June → October).
- **Embodied AI Hackathon precursor (March 22–23, 2025, Mountain View)** — single-site SO-ARM100-only event hosted by Circuit Launch; Hackster.io winners post lists **Team Firebreathing Rubber Duckies** as winners using **GR00T N1, ACT, and π0**. Same organizer / venue lineage as the October 2025 event but a third of the scale.

## Entities mentioned

- [Seeed Studio](../entities/seeed-studio.md) — primary co-organizer
- [NVIDIA](../entities/nvidia.md) — co-organizer
- [Hugging Face](../entities/hugging-face.md) — co-organizer
- [LeRobot](../entities/lerobot.md) — software framework
- [SO-ARM101](../entities/so-arm101.md) — primary arm
- [XLeRobot](../entities/xlerobot.md) — dual-arm platform (winning entries on both sites)
- [LeKiwi](../entities/lekiwi.md) — mobile base lineage
- [NVIDIA GR00T](../entities/nvidia-groot.md) — winning policy on both sites (N1.5)
- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md) — simulation
- [SIGRobotics-UIUC](../entities/sigrobotics-uiuc.md) — U.S. champion team
- [K-Scale Labs](../entities/k-scale-labs.md) — mentor / partner
- [Vector Wang](../entities/vector-wang.md) — XLeRobot creator; on-site mentor (implied)

## New entities surfaced (not yet broken out)

- **NVIDIA Jetson Thor** + **JetPack 7 SDK** — first appearance; worth a stub entity if the wiki keeps tracking on-robot compute.
- **NVIDIA Brev** — cloud GPU service used for GR00T fine-tuning by winning teams.
- **Lightwheel** — partner; positioning unclear from the recap alone.
- **Solo Tech** — partner.
- **Fashion Star / FashionStar / StarAI** — Chinese robot-arm vendor; alternative to SO-ARM101 at the China site.
- **Circuit Launch** — Mountain View hackerspace; recurring venue (also hosted March 2025 precursor).
- **Mate XLeRobot** — hardware-modded XLeRobot variant with vertical lift-rail. Could become an XLeRobot entity-page subsection rather than a standalone page.

## Concepts touched

- [Imitation learning](../concepts/learning/imitation-learning.md) — every winning project is BC- or VLA-line.
- [VLA models](../concepts/learning/vla-models.md) — GR00T N1.5, SmolVLA, ACT all instantiated.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — China champion used 90/10 real/sim split with domain randomization.
- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — *home robots* as theme positions all entries in the assistive / household-manipulation space the wiki tracks.

## Open questions

- **Exact dates** (which October 2025 weekend?) were not in the recap text accessed.
- **Cash prize amounts** — the recap lists champion / runner-up tiers but not dollar figures. Was the prize hardware-only as in the LeRobot hackathon, or did NVIDIA / Seeed put up cash?
- **Are the China-site winning datasets / repos public?** The recap mentions GitHub links but the specific URLs need direct-fetch verification.
- **Why a separate October hackathon when the June LeRobot one was already running?** The two have different organizational centers of gravity — June was HF-led, community-prize; October was NVIDIA-flavored, GR00T-N1.5-dominated. Worth noting as a structural fact about the ecosystem rather than answered here.

## Links cited in the recap (verification needed)

- UIUC SIGRobotics matcha-bot Hackster project page
- Pick & Place GitHub repo (China champion)
- XLeRobot documentation ([xlerobot.readthedocs.io](https://xlerobot.readthedocs.io))
- Hugging Face GR00T N1.5 tuning blog
- Two YouTube highlight videos (`youtube.com/watch` URLs not extracted)
- Sprinkle Robot Google Docs presentation
- Mate XLeRobot LinkedIn post
- SO-ARM101 setup wiki, GR00T fine-tuning wiki, Isaac Sim integration wiki, Diffusion Policy paper
