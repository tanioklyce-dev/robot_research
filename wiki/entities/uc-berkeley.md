---
title: UC Berkeley
type: entity
subtype: university
created: 2026-11-16
updated: 2026-11-16
sources: 31
tags: [uc-berkeley, hybrid-robotics, berkeley-humanoid, cassie, hiperlab, koushil-sreenath, mark-mueller, roberto-horowitz, berkeley, bair, rail, autolab, sergey-levine, pieter-abbeel, ken-goldberg, jitendra-malik, trevor-darrell, shankar-sastry, michael-i-jordan, real-world-rl, visual-navigation, diffusion, code-as-policy, nvidia-gear, academic-lab]
---

**UC Berkeley** (University of California, Berkeley) — the academic institution that appears most often across this wiki's robot-learning sources, on about 70 pages. Its labs originated several of the field's default tools: SAC, RLPD and the SERL line in real-world RL, DDPM in generative modelling, the GNM → ViNT → NoMaD → OmniVLA navigation line, and RMA in sim-to-real locomotion. In 2026 it is also **[NVIDIA GEAR](nvidia-gear.md)'s most frequent academic co-author**.

This page is a map of where Berkeley shows up in the wiki, by lab. It is not an institutional profile: no ingested source covers the university itself, and lab names and group memberships below are as the sources give them.

## Labs and groups, as they appear here

| Group | People in the wiki | What it contributed here |
|---|---|---|
| **RAIL** (the lab's site uses both "Robotic AI & Learning Lab" and "Robotics and AI Lab @ BAIR"; [site](https://rail.eecs.berkeley.edu/)) | [Sergey Levine](sergey-levine.md), [Jianlan Luo](jianlan-luo.md), [Dhruv Shah](dhruv-shah.md), [Noriaki Hirose](noriaki-hirose.md) | **Off-policy RL as a robot tool:** [SAC](../sources/sac-paper.md) and its [applications paper](../sources/sac-applications-paper.md) → [RLPD](rlpd.md) → [SERL](serl.md) → [HIL-SERL](../sources/hil-serl-paper.md), 100% success in 1–2.5 h of real training ([real-world robot RL](../concepts/learning/real-world-robot-rl.md)). **The open navigation line:** [GNM](../sources/gnm-paper.md) → [ViNT](../sources/vint-paper.md) → [NoMaD](../sources/nomad-paper.md) → [MBRA](../sources/mbra-paper.md) → [OmniVLA](../sources/omnivla-paper.md) ([visual navigation policies](../concepts/robotics/visual-navigation-policies.md)). Also [Meta-World](metaworld.md) (with Stanford). |
| **Robot Learning Lab** (Abbeel; [site](https://rll.berkeley.edu/)) | Pieter Abbeel (no page), [Danijar Hafner](danijar-hafner.md) (collaborations) | [DDPM](ddpm.md), the diffusion-model foundation; [Decision Transformer](decision-transformer.md); [DayDreamer](../sources/daydreamer-paper.md) (Dreamer on real robots); [EfficientZero](../sources/efficientzero-paper.md); [RPG](rpg.md) (with Amazon FAR, 2026) |
| **AUTOLab** ([site](https://autolab.berkeley.edu/)) | [Ken Goldberg](ken-goldberg.md) (director), [Letian Fu](letian-fu.md) | [Code-as-policy](../concepts/agents/code-as-policy.md) measurement and harnesses with NVIDIA: [CaP-X](cap-x.md), [Graph-as-Policy](graph-as-policy.md). **VABAR**, a [variational automation](../concepts/robotics/variational-automation.md) benchmark with NVIDIA ([CoRL 2026 blog](../sources/nvidia-corl-2026-robotics-simulation-blog.md)) |
| **Malik group** | Jitendra Malik (no page), [Ashish Kumar](ashish-kumar.md) | [RMA](../sources/rma-paper.md) rapid motor adaptation and [egocentric-vision locomotion](../sources/egocentric-vision-locomotion-paper.md) (with CMU), the teacher–student [sim-to-real](../concepts/learning/sim-to-real-transfer.md) recipe; co-author on [DreamDojo](dreamdojo.md) |
| **Others in the wiki** | Trevor Darrell, Shankar Sastry (no pages); [Michael I. Jordan](michael-i-jordan.md); [Amy Pavel](amy-pavel.md), [Mina Huh](mina-huh.md) | [EgoScale](../sources/egoscale-paper.md) (Darrell); CaP-X and RPG (Sastry); [collectivist economic AI](../sources/jordan-collectivist-economic-ai.md) (Jordan, with Inria); [accessible robot communication](../sources/huh2026-accessible-robot-comm.md) (Pavel, Huh); the laptop [fly-brain simulation](../sources/shiu-fly-brain-paper.md) from Kristin Scott's lab ([Phil Shiu](phil-shiu.md)). Berkeley is also among the listed affiliations of [RoboDojo](robodojo.md) and [WorldModelBench](../sources/worldmodelbench-paper.md); those sources don't map authors to institutions. |

## Robotics labs with no ingested source yet (checked 2026-11-16)

A user-supplied list (a search-engine summary) named these labs. Each line below was checked against the lab's own page; none has an ingested paper in this wiki yet, so they are leads, not coverage.

| Lab | Director (per lab page) | Focus | Status |
|---|---|---|---|
| **Hybrid Robotics** ([site](https://hybrid-robotics.berkeley.edu/)) | Koushil Sreenath, Assoc. Professor, Mechanical Engineering | Dynamic legged locomotion: the site lists bipedal work on **Cassie** (RL locomotion, jumping, ball juggling) and quadrupeds | Confirmed |
| **Berkeley Humanoid** ([project](https://berkeley-humanoid.com/)) | from Hybrid Robotics: Liao, Zhang, Huang, Huang, Li, Sreenath | *"A Research Platform for Learning-based Control"* | Confirmed. The obvious paper to ingest for the [humanoid](../concepts/robotics/whole-body-control.md) thread. |
| **High Performance Robotics Lab (HiPeRLab)** ([site](https://hiperlab.berkeley.edu/)) | Mark W. Mueller, Mechanical Engineering. Per the Berkeley ME lab page and his members-page entry; the homepage itself names no director, and he is on every listed publication. | *"Low-level research on fundamental robotics capabilities, especially for Unmanned Aerial Systems. Areas of particular focus are safety, localization, and design"*, with *"a strong focus on experimental validation"*. Listed areas: vehicle design, safety, firefighting and challenging environments, energy efficiency, state estimation, motion planning. Recent work includes Duawlfin (a wheeled and flying drone, RA-L 2025), Mueller's book *Dynamics and Control of Autonomous Flight* (Springer, 2025), and 2026 preprints on occlusion-aware MPPI and on interpreting control latents with conditional [flow matching](../concepts/learning/flow-matching.md). | Confirmed. The homepage and publications page were read directly on 2026-11-16 (a plain curl had hit a Cloudflare challenge). Relevant to [agentic UAVs](../concepts/robotics/agentic-uavs.md). **Video:** the lab's [YouTube channel](https://www.youtube.com/channel/UCJnDtux5GS1WRogCBfLTsfA/videos), linked from its homepage, has 42 videos (paper demos plus conference talks; listed 2026-11-16). The most viewed are in-flight battery switching (~34k) and a mid-air reconfigurable quadcopter (~27k). The leads for this wiki's learning thread are *ProxFly* (residual-RL close-proximity flight), *A Learning-based Quadcopter Controller with Extreme Adaptation* and *A Zero-shot Adaptive Quadcopter Controller*. |
| *"Autonomy, Robotics, and Controls (ARC) Lab"* | Roberto Horowitz, Mechanical Engineering (Etcheverry Hall) | Robot-manipulator control; recent SE(3)-equivariant, contact-rich manipulation learning | **Lab name not confirmed.** Horowitz's homepage, bio and ME page give his office (5138 Etcheverry), his manipulation work and that he teaches EECS C106A, but name no "ARC Lab". Treat the name as unverified. |

Not on that list but central here: **AUTOLab** (Goldberg), the most active Berkeley robotics lab in this wiki's sources (see above).

## The NVIDIA GEAR pattern

Across 2024–2026, Berkeley is the academic partner on a large share of NVIDIA GEAR's robotics papers in this wiki:

- [HOVER](../sources/hover-paper.md) — whole-body control distillation (2024)
- [EgoScale](../sources/egoscale-paper.md) and [DreamDojo](../sources/dreamdojo-paper.md) — human-video data and world models (2026)
- [CaP-X](../sources/cap-x-paper.md) and [ASPIRE](../sources/aspire-paper.md) — code-as-policy (2026)
- [Graph-as-Policy](../sources/gap-graph-as-policy-paper.md) (CoRL 2026 spotlight) and VABAR
- [AW-0](../sources/agentic-world-action-models-aw0-paper.md) — a code expert inside a world-action model (October 2026)

The recurring names are [Ken Goldberg](ken-goldberg.md) and [Letian Fu](letian-fu.md) on the Berkeley side and [Jim Fan](jim-fan.md) and [Yuke Zhu](yuke-zhu.md) on NVIDIA's. For a reader tracking the code-as-policy and agentic-robotics thread, this Berkeley × GEAR axis is where most of the primary results come from.

## Alumni and diaspora in the wiki

- [Physical Intelligence](physical-intelligence.md) counts Sergey Levine among its founders, and its [FAST](../sources/fast-paper.md) paper carries a joint PI / Berkeley / Stanford affiliation.
- [Deepak Pathak](deepak-pathak.md) did his PhD at Berkeley before CMU and [Skild AI](skild-ai.md).
- [Dhruv Shah](dhruv-shah.md) moved from RAIL to Princeton faculty.
- [Phil Shiu](phil-shiu.md) moved from Kristin Scott's lab to Eon Systems.
- [Mahi Shafiullah](mahi-shafiullah.md) moved from NYU / Hello Robot to a Berkeley postdoc on robotic hands as of June 2026 ([TechCrunch](../sources/techcrunch-hello-robot-homes-2026.md)).

## Data and benchmarks with Berkeley involvement

- [DROID](droid.md) — a 13-institution dataset; co-lead [Karl Pertsch](karl-pertsch.md) spans Berkeley and Stanford.
- The [FrodoBots](frodobots.md) navigation data relabelled by RAIL as Berkeley-FrodoBots-7K ([MBRA](../sources/mbra-paper.md); [BitRobot](bitrobot.md)).
- [OpenVLA](openvla.md) — Stanford / TRI / Berkeley / Google DeepMind / MIT.
- [Meta-World](metaworld.md), VABAR, and [RoboDojo](robodojo.md) (Berkeley among many affiliations).

## Related

- [Sergey Levine](sergey-levine.md), [Ken Goldberg](ken-goldberg.md), [Michael I. Jordan](michael-i-jordan.md)
- [NVIDIA GEAR](nvidia-gear.md) — the most frequent industry co-author
- [Physical Intelligence](physical-intelligence.md), [Skild AI](skild-ai.md) — companies with Berkeley-trained founders
- [Real-world robot RL](../concepts/learning/real-world-robot-rl.md), [Visual navigation policies](../concepts/robotics/visual-navigation-policies.md), [Code as policy](../concepts/agents/code-as-policy.md)

## Open questions

- **Ingest a Berkeley Humanoid or Hybrid Robotics paper.** Sreenath's lab is Berkeley's legged and humanoid group, and the wiki has nothing from it.
- **Pieter Abbeel, Jitendra Malik, Trevor Darrell and Shankar Sastry have no person pages**, despite each appearing across several sources here. Abbeel is the biggest gap: DDPM, Decision Transformer, DayDreamer, EfficientZero, SAC and RPG.
- **Lab boundaries are inferred from authorship.** No source lays out BAIR or its labs, so a group listed here is the one its sources' authors belong to, not an official roster.

## Mentioned in

> [!note] Curated list — about 70 wiki pages mention UC Berkeley; the source pages below shaped this one.

- [HIL-SERL](../sources/hil-serl-paper.md), [SERL](../sources/serl-paper.md), [RLPD](../sources/rlpd-paper.md), [SAC](../sources/sac-paper.md) — the RAIL real-world-RL line
- [GNM](../sources/gnm-paper.md), [MBRA](../sources/mbra-paper.md) — the RAIL navigation line
- [DDPM](../sources/ddpm-paper.md), [Decision Transformer](../sources/decision-transformer-paper.md), [DayDreamer](../sources/daydreamer-paper.md) — the Abbeel lab
- [CaP-X](../sources/cap-x-paper.md), [Graph-as-Policy](../sources/gap-graph-as-policy-paper.md), [AW-0](../sources/agentic-world-action-models-aw0-paper.md), [NVIDIA CoRL 2026 blog](../sources/nvidia-corl-2026-robotics-simulation-blog.md) — the Berkeley × NVIDIA GEAR axis
- [RMA](../sources/rma-paper.md), [Egocentric-vision locomotion](../sources/egocentric-vision-locomotion-paper.md) — the Malik group
- [Shiu fly-brain paper](../sources/shiu-fly-brain-paper.md), [Berkeley News](../sources/berkeley-fly-brain-news.md) — the connectome simulation
