---
title: awesome-physical-ai (GitHub curated list)
type: source
url: https://github.com/natnew/awesome-physical-ai
author: natnew (solo curator; community PRs)
published: rolling (52 commits; snapshot 2026-07-08)
ingested: 2026-07-08
format: web (GitHub README / docs site — MDX+JS)
license: MIT
tags: [awesome-list, physical-ai, embodied-ai, catalog, curation, robotics, learning-resources]
---

# awesome-physical-ai (GitHub curated list)

## Summary

A solo-curated (111★ / 11 forks, MIT) "awesome list" spanning the whole Physical-AI stack: simulators → datasets → benchmarks → evaluation → foundation models → world models → manipulation/locomotion → sim-to-real → **safety/governance** → production (ROS 2) → courses/companies/hardware/people. Its suggested on-ramp is Gymnasium CartPole → MuJoCo → [LeRobot](../entities/lerobot.md) → [OpenVLA](../entities/openvla.md). For this wiki the value is less the entries themselves (most core items are already covered here in more depth) than the **taxonomy and the gap-mining**: it surfaces several whole categories the wiki deliberately or accidentally lacks. Treat as a directory/second-opinion source, not a claims source.

## Coverage vs this wiki

**Heavy overlap (the wiki is deeper):** LeRobot ecosystem + SO-ARM100 hardware, [GR00T](../entities/nvidia-groot.md), [π0](../entities/pi-zero.md)/Helix/[Gemini Robotics](../entities/gemini-robotics.md), [V-JEPA 2](../entities/v-jepa-2.md)/I-JEPA/[Cosmos](../entities/nvidia-cosmos.md), [Diffusion Policy](../entities/diffusion-policy.md)/[ACT](../entities/act.md)/[Mobile ALOHA](../entities/aloha.md), [Isaac Sim](../entities/nvidia-isaac-sim.md)/[Isaac Lab](../entities/nvidia-isaac-lab.md)/Genesis, [OXE](../entities/open-x-embodiment.md)/[DROID](../entities/droid.md), [LIBERO](../entities/libero.md)/[Metaworld](../entities/metaworld.md)/[SimplerEnv](../entities/simplerenv.md), ROS 2/[Nav2](../entities/nav2.md)/Zenoh/MCAP, [Reachy 2](../entities/reachy.md)/[Stretch](../entities/stretch.md)/[Unitree G1](../entities/unitree-g1.md), [Tedrake](../entities/russ-tedrake.md) (People to Follow; Drake among simulators; MIT 6.4210 = his Robot Manipulation course).

**Categories the wiki lacks or is thin on (gap-mine):**
- **Safety & robustness tooling** — Safety Gym(nasium), OmniSafe, Constrained Policy Optimization, **Control Barrier Functions**, RSS, VerifAI. The wiki's safety folder is alignment/mech-interp-oriented; *robot control safety* is a real gap.
- **Governance & standards** — ISO 10218/15066 (collaborative robots), **ISO 13482** (personal-care robots), UL 4600, ISO 26262, EU AI Act / Machinery Regulation. ~~Nothing in the wiki covers robot standards~~ — [Robot safety standards](../concepts/robotics/robot-safety-standards.md) created 2026-07-08 from this gap.
- **Model-based-RL world-model line** — DreamerV3/DayDreamer, TD-MPC2, PlaNet, MuZero, Genie 2, GAIA-1, UniSim: the wiki's world-model coverage is JEPA-vs-generative-video; the *MBRL* lineage is mostly absent.
- **Locomotion corpus** — RMA, legged_gym/RSL-RL, ANYmal Parkour, HumanPlus/OmniH2O/H2O/ASAP/HOVER, Walk These Ways. The wiki tracks locomotion only via GR00T-adjacent whole-body work ([SONIC](../entities/gear-sonic.md)).
- **Sim-to-real classics** — Eureka, DeXtreme, Automatic Domain Randomization, BayesSim — would deepen [sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md)'s historical spine.
- **Evaluation methodology as a category** — robomimic, rliable, RoboArena (wiki knows it only via [Cosmos 3](cosmos-3-technical-report.md)); pairs naturally with the [TRI LBM paper](tri-lbm-paper.md)'s statistical-rigor argument.
- Misc notable absences: Octo, RT-2/RT-X, SayCan/Code-as-Policies, Habitat, CARLA/AV stack, Gello, Dex-UMI.

> [!note] Curation-quality caveats
> Solo-curated and uneven: e.g. "Stanford CS 336 (Robot Learning)" appears mislabeled (CS 336 is Percy Liang's language-modeling course; Stanford's robot-learning course is CS 224R), and some entries are idiosyncratic picks (DreamZero, Sunday Robotics, Chipstrat). 111 stars ≈ small-community list, not a field-consensus artifact like Awesome-LLM-Robotics. Verify before citing entries as facts.

## Entities mentioned

Directory-style — hundreds; only wiki-linked ones enumerated above. Companies section aligns with the wiki's humanoid coverage ([Figure](../entities/figure.md), [Boston Dynamics](../entities/boston-dynamics.md), [Physical Intelligence](../entities/physical-intelligence.md), [Pollen Robotics](../entities/pollen-robotics.md), [Apptronik](../entities/apptronik-apollo.md), 1X, Agility).

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md), [world-model simulators](../concepts/world-models/world-model-simulators.md), [imitation learning](../concepts/learning/imitation-learning.md), [sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — as catalog categories.

## Open questions

- Which gap categories are worth wiki investment: ~~robot-safety standards~~ (done — [robot safety standards](../concepts/robotics/robot-safety-standards.md)), **MBRL world models (Dreamer/TD-MPC2)** and **evaluation methodology (rliable/robomimic/RoboArena)** remain.
- Whether a bigger-community awesome list (Awesome LLM Robotics, Awesome World Models — both in its "Related lists") would be a better recurring directory source than this one.
