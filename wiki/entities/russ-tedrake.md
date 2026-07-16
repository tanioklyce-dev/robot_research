---
title: Russ Tedrake
type: entity
subtype: person
created: 2026-07-08
updated: 2026-07-15
sources: 7
tags: [russ-tedrake, mit, csail, tri, lbm, drake, underactuated-robotics, locomotion, manipulation, physical-ai, walden-robotics]
---

# Russ Tedrake

MIT roboticist and industry research leader — **Toyota Professor at MIT** (EECS / Mechanical Engineering / Aero-Astro, CSAIL) and the architect of [TRI](tri.md)'s **[Large Behavior Models](../concepts/learning/large-behavior-models.md)** program (title reported as Senior VP of Large Behavior Models, earlier VP of Robotics Research). As of **2026-07-15**, **co-founder & CEO of [Walden Robotics](walden-robotics.md)** — the physical-AI startup previously tracked here as "still-stealth" ([Automated Podcast, 2026-07-01](../sources/automated-podcast-tedrake-rocket-ship.md)), revealed as a manufacturing-robotics company spun out of TRI. One of the field's rare model-based-control ↔ learning bridges: the same person behind the optimization/dynamics stack (Drake, underactuated robotics) and one of the leading generalist-manipulation-policy programs.

## Career

- **Education**: B.S.E. Computer Engineering, U. Michigan (1999); Ph.D. EECS, MIT (2004), advised by Sebastian Seung (web bio: [MIT Robot Locomotion Group](https://locomotion.csail.mit.edu/russt.html) — live-web fact, not an ingested source).
- **Formative path** ([podcast](../sources/automated-podcast-tedrake-rocket-ship.md)): Detroit-area childhood (GM father); Ford Wayne Assembly paint-shop internship in high school (the fan-shutdown/82 °F walk-off story — his stated first hard lesson in automation-meets-labor); video-game AI with John Laird at Michigan + Microsoft Research summers; MIT Leg Lab basement (Troody, M2) as the gateway to bipeds.
- **Thesis line**: passive dynamic walkers + RL — the "Toddler" robot **learned to walk in ~20 minutes** (2004), contemporary with Abbeel's helicopters; "RL before it was cool" ([podcast](../sources/automated-podcast-tedrake-rocket-ship.md)).
- **MIT**: leads the Robot Locomotion Group; led **Team MIT in the DARPA Robotics Challenge**; teaches the canonical **Underactuated Robotics** and **Robot Manipulation** courses/textbooks (live-web facts: [CSAIL](https://www.csail.mit.edu/person/russ-tedrake), [Quest](https://quest.mit.edu/about/people/russ-tedrake)). Multiple MIT teaching awards (2021 Jamieson, 2023 Teaching with Digital Technology, 2024 Distinguished Educator).
- **TRI**: built the LBM program ("the science of LBMs — the initial scaling laws... at a level a startup wouldn't be motivated to do and academia couldn't resource"); senior author on the **[TRI LBM paper](../sources/tri-lbm-paper.md)** (82 authors, Science Robotics 2026 — the program's primary source, with Drake as its simulator); previously VP of Robotics Research — the affiliation on the [UMI paper](../sources/umi-paper.md) and the TRI cohort around [Diffusion Policy](diffusion-policy.md) ([TRI website](../sources/tri-website.md)).
- **[Walden Robotics](walden-robotics.md) (co-founder & CEO, revealed 2026-07-15)**: the startup confirmed-but-unnamed on the [Automated Podcast](../sources/automated-podcast-tedrake-rocket-ship.md). Cambridge, MA; **spun out of TRI in Jan 2026**; **$300M seed at $1.1B**; builds general-purpose manufacturing robots on **[LBMs](../concepts/learning/large-behavior-models.md) + [Diffusion Policy](diffusion-policy.md)** with a human-remote-assist deployment model; already in production at a Toyota NC plant since Feb 2026. Brought along TRI robot-learning leadership ([Ben Burchfiel](ben-burchfiel.md) CTO, [Siyuan Feng](siyuan-feng.md) Principal Architect, Adrien Gaidon CSO, Rares Ambrus Head of AI). Note the earlier "name references LBMs" hint did **not** pan out literally — the name references **Thoreau's *Walden*** ([launch](../sources/walden-robotics-launch.md)). Advisor to CarbonSix Inc. (live-web fact; separate from Walden).

- **MIT video-diffusion line**: senior author (with Vincent Sitzmann) on **[History-Guided Video Diffusion / DFoT](../sources/history-guided-video-diffusion-paper.md)** (ICML 2025) and its ancestor Diffusion Forcing — his group's evidence base for the "video backbones win for long context" position from the [podcast](../sources/automated-podcast-tedrake-rocket-ship.md); includes a physical-robot result (83% on a memory+reactivity task via sampling-time score composition).

## Positions he argues (from ingested sources)

- **LBM ⊃ VLA**: an LBM is any image-sequences→actions model; a VLA is the uptrained-VLM architectural choice; video/world-model backbones are the alternative (better for long context) — see [Large behavior models](../concepts/learning/large-behavior-models.md).
- **Robot data scarcity is misframed**: you start from a pretrained base model's common sense and "build a bridge" to one new output (actions); data strategy = bridge-building across modalities, not corpus-size races ([podcast](../sources/automated-podcast-tedrake-rocket-ship.md)).
- **ML has outrun theory**: roboticists are becoming "behavioral scientists" probing systems they built; scaling has headroom; theory still matters for data curricula/robustness.
- **Deployment is the next milestone** — the virtuous cycle (robots fielded → data → capability) has to be earned.
- **Escape velocity**: this robotics moment differs from prior hype cycles via talent influx + investment + manufacturing (China) + demographic demand — "I would rather be on the rocket ship."

## Drake

Open-source **model-based design and simulation/dynamics library** from his MIT group + TRI ([drake.mit.edu](https://drake.mit.edu/)) — multibody dynamics, optimization-based planning/control (the GCS motion-planning line is his group's — [State of Robot Motion Generation](../sources/state-of-robot-motion-generation-2024.md)). Tedrake calls it "my horcrux... I still contribute production code" ([podcast](../sources/automated-podcast-tedrake-rocket-ship.md)). The wiki's model-based counterweight to its mostly-learning stack; no dedicated entity page yet (this section is the anchor).

## Related

- [Walden Robotics](walden-robotics.md) — his company (CEO); the commercialization of the LBM line.
- [TRI](tri.md) — institutional home of the LBM program.
- [Large behavior models](../concepts/learning/large-behavior-models.md) — his coined-at-TRI model class.
- [Diffusion Policy](diffusion-policy.md) — the single-task ancestor of LBMs ("LBM = multitask diffusion policy, in my vernacular").
- [UMI](umi.md) — co-author; the TRI/Stanford data-collection line.
- [VLA models](../concepts/learning/vla-models.md) — the adjacent (subtype) model class.

## Mentioned in

- [Walden Robotics — Launch from Stealth](../sources/walden-robotics-launch.md) — co-founder & CEO; the startup reveal.
- [Automated Podcast — Robotics Is Finally on a Rocket Ship](../sources/automated-podcast-tedrake-rocket-ship.md) — **primary ingest**; career + LBM taxonomy + startup.
- [TRI LBM paper](../sources/tri-lbm-paper.md) — senior author; the LBM program's primary source (Drake as simulator).
- [History-Guided Video Diffusion (DFoT)](../sources/history-guided-video-diffusion-paper.md) — senior author; MIT-side video-diffusion/world-model line.
- [TRI Website](../sources/tri-website.md) — TRI role, cohort.
- [UMI Paper](../sources/umi-paper.md) — co-author (TRI).
- [State of Robot Motion Generation 2024](../sources/state-of-robot-motion-generation-2024.md) — GCS (his group) among named classical methods; [Kober RL survey](../sources/kober-rl-robotics-survey-2013.md) — early Tedrake biped RL cited.
