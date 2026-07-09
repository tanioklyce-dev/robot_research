---
title: Russ Tedrake
type: entity
subtype: person
created: 2026-07-08
updated: 2026-07-08
sources: 4
tags: [russ-tedrake, mit, csail, tri, lbm, drake, underactuated-robotics, locomotion, manipulation, physical-ai]
---

# Russ Tedrake

MIT roboticist and industry research leader — **Toyota Professor at MIT** (EECS / Mechanical Engineering / Aero-Astro, CSAIL) and the architect of [TRI](tri.md)'s **[Large Behavior Models](../concepts/learning/large-behavior-models.md)** program (title reported as Senior VP of Large Behavior Models, earlier VP of Robotics Research). As of mid-2026, **founder of a still-stealth physical AI startup** ([Automated Podcast, 2026-07-01](../sources/automated-podcast-tedrake-rocket-ship.md)). One of the field's rare model-based-control ↔ learning bridges: the same person behind the optimization/dynamics stack (Drake, underactuated robotics) and one of the leading generalist-manipulation-policy programs.

## Career

- **Education**: B.S.E. Computer Engineering, U. Michigan (1999); Ph.D. EECS, MIT (2004), advised by Sebastian Seung (web bio: [MIT Robot Locomotion Group](https://locomotion.csail.mit.edu/russt.html) — live-web fact, not an ingested source).
- **Formative path** ([podcast](../sources/automated-podcast-tedrake-rocket-ship.md)): Detroit-area childhood (GM father); Ford Wayne Assembly paint-shop internship in high school (the fan-shutdown/82 °F walk-off story — his stated first hard lesson in automation-meets-labor); video-game AI with John Laird at Michigan + Microsoft Research summers; MIT Leg Lab basement (Troody, M2) as the gateway to bipeds.
- **Thesis line**: passive dynamic walkers + RL — the "Toddler" robot **learned to walk in ~20 minutes** (2004), contemporary with Abbeel's helicopters; "RL before it was cool" ([podcast](../sources/automated-podcast-tedrake-rocket-ship.md)).
- **MIT**: leads the Robot Locomotion Group; led **Team MIT in the DARPA Robotics Challenge**; teaches the canonical **Underactuated Robotics** and **Robot Manipulation** courses/textbooks (live-web facts: [CSAIL](https://www.csail.mit.edu/person/russ-tedrake), [Quest](https://quest.mit.edu/about/people/russ-tedrake)). Multiple MIT teaching awards (2021 Jamieson, 2023 Teaching with Digital Technology, 2024 Distinguished Educator).
- **TRI**: built the LBM program ("the science of LBMs — the initial scaling laws... at a level a startup wouldn't be motivated to do and academia couldn't resource"); previously VP of Robotics Research — the affiliation on the [UMI paper](../sources/umi-paper.md) and the TRI cohort around [Diffusion Policy](diffusion-policy.md) ([TRI website](../sources/tri-website.md)).
- **Startup (2026, stealth)**: confirmed on the [Automated Podcast](../sources/automated-podcast-tedrake-rocket-ship.md); the name apparently references LBMs ("it's in the company name"); claimed differentiation across data / deployments / operations / business; founding motivation explicitly includes steering physical AI toward **"amplifying, not replacing people."** Advisor to CarbonSix Inc. (live-web fact; separate from the startup).

## Positions he argues (from ingested sources)

- **LBM ⊃ VLA**: an LBM is any image-sequences→actions model; a VLA is the uptrained-VLM architectural choice; video/world-model backbones are the alternative (better for long context) — see [Large behavior models](../concepts/learning/large-behavior-models.md).
- **Robot data scarcity is misframed**: you start from a pretrained base model's common sense and "build a bridge" to one new output (actions); data strategy = bridge-building across modalities, not corpus-size races ([podcast](../sources/automated-podcast-tedrake-rocket-ship.md)).
- **ML has outrun theory**: roboticists are becoming "behavioral scientists" probing systems they built; scaling has headroom; theory still matters for data curricula/robustness.
- **Deployment is the next milestone** — the virtuous cycle (robots fielded → data → capability) has to be earned.
- **Escape velocity**: this robotics moment differs from prior hype cycles via talent influx + investment + manufacturing (China) + demographic demand — "I would rather be on the rocket ship."

## Drake

Open-source **model-based design and simulation/dynamics library** from his MIT group + TRI ([drake.mit.edu](https://drake.mit.edu/)) — multibody dynamics, optimization-based planning/control (the GCS motion-planning line is his group's — [State of Robot Motion Generation](../sources/state-of-robot-motion-generation-2024.md)). Tedrake calls it "my horcrux... I still contribute production code" ([podcast](../sources/automated-podcast-tedrake-rocket-ship.md)). The wiki's model-based counterweight to its mostly-learning stack; no dedicated entity page yet (this section is the anchor).

## Related

- [TRI](tri.md) — institutional home of the LBM program.
- [Large behavior models](../concepts/learning/large-behavior-models.md) — his coined-at-TRI model class.
- [Diffusion Policy](diffusion-policy.md) — the single-task ancestor of LBMs ("LBM = multitask diffusion policy, in my vernacular").
- [UMI](umi.md) — co-author; the TRI/Stanford data-collection line.
- [VLA models](../concepts/learning/vla-models.md) — the adjacent (subtype) model class.

## Mentioned in

- [Automated Podcast — Robotics Is Finally on a Rocket Ship](../sources/automated-podcast-tedrake-rocket-ship.md) — **primary ingest**; career + LBM taxonomy + startup.
- [TRI Website](../sources/tri-website.md) — TRI role, cohort.
- [UMI Paper](../sources/umi-paper.md) — co-author (TRI).
- [State of Robot Motion Generation 2024](../sources/state-of-robot-motion-generation-2024.md) — GCS (his group) among named classical methods; [Kober RL survey](../sources/kober-rl-robotics-survey-2013.md) — early Tedrake biped RL cited.
