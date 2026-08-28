# Wiki overview

A reader's introduction to this wiki — what it is, what's in it, where to start.

## What this is

A **persistent, LLM-maintained knowledge base** built incrementally from raw sources. The pattern is described in `raw/llm-wiki.md` and the operating conventions are in [`CLAUDE.md`](../CLAUDE.md). Three layers:

1. **`raw/`** — source documents (papers, articles, transcripts, datasets). Immutable.
2. **`wiki/`** — Claude-maintained markdown that sits between you and the raw sources. Summaries, entity pages, concept pages, and synthesis pages. Cross-linked.
3. **`CLAUDE.md`** — schema and conventions (page formats, ingest workflow, lint workflow). Co-evolves with usage.

The wiki is a **compounding artifact**. Each new source ingest enriches the cross-references; each new query may produce a new synthesis page. Over time the wiki becomes more useful, not less.

## Robots for Education and Research

A starter shortlist — eleven platforms across the spectrum from "$399 RL biped" and "tabletop arm under $500" to "research-grade mobile manipulator" and "bipedal humanoid." Each entity page links to a vendor or GitHub product page near the top so you can dig into specs and pricing.

| Platform | Form | Price tier | Why it's on this list |
| --- | --- | --- | --- |
| [Microduck](entities/microduck.md) | bipedal walker (no arm) | **$399** | [Pollen](entities/pollen-robotics.md)/[Hugging Face](entities/hugging-face.md)'s 25 cm, sub-800 g RL biped (pre-orders 2026-08-27). The **only platform on this list aimed at reinforcement learning rather than imitation learning**, and the cheapest legged robot in the wiki. Ships seven trained policies plus the whole recipe that made them — [mjlab](entities/mjlab.md)/PPO training envs, a voltage-level [actuator model](concepts/learning/actuator-fidelity-sim2real.md), and an [Apache-2.0 onboard runtime](sources/microduck-runtime-repo.md) whose design docs are worth reading on their own. Learned fall-recovery makes unattended desk iteration practical. Limits: **RK3566 / 1 GB RAM** (no [VLA](concepts/learning/vla-models.md) will ever run on it), an 8×8 ToF rather than the advertised "LiDAR", no [LeRobot](entities/lerobot.md) integration, and **not** open-source *hardware*. |
| [SO-ARM101](entities/so-arm101.md) | tabletop arm | sub-$500 | Open-source low-cost arm; default manipulator across the [LeRobot](entities/lerobot.md) ecosystem. Cheapest entry to imitation-learning data collection. |
| [LeKiwi](entities/lekiwi.md) | mobile manipulator | sub-$1k | Open-source 3-wheel holonomic mobile manipulator from SIGRobotics-UIUC; commercial kits via [Seeed Studio](entities/seeed-studio.md). Pairs with SO-ARM101. |
| [XLeRobot](entities/xlerobot.md) | dual-arm mobile manipulator | $660 | $660 dual-arm household robot built from two SO-ARM101s on a [LeKiwi](entities/lekiwi.md)-style base; 90% 3D-printed. Won two Embodied AI Hackathon 2025 prizes. |
| [reBot Arm B601-DM](entities/rebot-arm-b601.md) | benchtop arm | **$1,499** arm / $7,057 with Jetson Thor | [Seeed](entities/seeed-studio.md)'s fully open 6+1-DOF **CAN-bus** arm on [Damiao](entities/damiao.md) quasi-direct-drive actuators — 767 mm reach, 1.5 kg payload, 0.2 mm repeatability, ROS 1/2 + MoveIt + [LeRobot](entities/lerobot.md) + [Isaac Sim](entities/nvidia-isaac-sim.md). Fills the gap between the FeeTech-servo hobby tier and $20k research arms. Comes with a free 19-module [NVIDIA DLI sim-to-real course](sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) (LeRobot → Isaac Sim → [Cosmos](entities/nvidia-cosmos.md) augmentation → [GR00T 1.7](entities/nvidia-groot.md) → TensorRT on Jetson). The [B601-RS](entities/rebot-arm-b601.md) sibling swaps in [Robstride](entities/robstride.md) motors for 2.5 kg / <0.1 mm at 48 V. |
| [ROSOrin Pro](entities/rosorin-pro.md) | educational mobile manipulator | educational tier | Hiwonder's 6-DOF arm + mobile base kit on a Jetson Orin Nano; ships upstream [OpenClaw](entities/openclaw.md) plus Hiwonder's [`openclaw_controller`](entities/openclaw-controller.md) ROS 2 bridge as the LLM-agent curriculum. The most curriculum-bundled starting kit on this list. |
| [TurtleBot 4](entities/turtlebot.md) | mobile-only (no arm) | ~$1,895 | Canonical ROS 2 educational mobile robot; iRobot Create 3 base + Raspberry Pi 4B. Best starting point if you want a navigation-first platform. |
| [myBuddy 280](entities/mybuddy-280.md) | dual-arm desktop | $1,619 | Elephant Robotics 13-DOF dual-arm tabletop robot with touchscreen + ROS 1 / MoveIt. Lower-ceiling, more polished alternative to XLeRobot. |
| [Stretch 4](entities/stretch.md) | research-grade mobile manipulator | **$29,950** | Hello Robot's fourth-generation mobile manipulator (launched 2026-05-12) — new 3-wheel omnidirectional holonomic base, dual hemispherical 3D LiDAR, 8 redundant DOF + gripper, Intel Ultra 5 NUC, optional Jetson Orin NX ($2,495 add-on). The de-facto research platform behind [Robot Utility Models](entities/robot-utility-models.md), [OK-Robot](entities/ok-robot.md), [stretch_ai](entities/stretch-ai.md), and most academic in-home deployments tracked in this wiki (those policies were trained on Stretch 2 / 3 — Stretch 4 transfer is an open question). |
| [Reachy 2](entities/reachy.md) | bimanual mobile manipulator (humanoid form) | higher tier | Pollen Robotics' open-source bimanual mobile manipulator; ROS 2; positioned explicitly as an embodied-AI development platform. |
| [Unitree G1 EDU Plus](entities/unitree-g1.md) | bipedal humanoid | ~$16k EDU base; **~$30–45k** as EDU+ | The cheapest credible research humanoid, in its extra-DOF/dexterous-hand configuration. Now the **de-facto benchmark platform for learned [whole-body control](concepts/robotics/whole-body-control.md)** — [SONIC](sources/sonic-paper.md), MotionBricks and BumbleBee all evaluate on it, and it is [GR00T](entities/nvidia-groot.md)'s main non-GR-1 humanoid target. **EDU+ pricing is opaque and configuration-dependent**; see [Stretch vs G1](syntheses/platforms/household-robot-decision-stretch-vs-g1.md) before assuming the $16k headline applies. |

## Open-source robot AI research projects
If you want to explore the open-source landscape: [Open-source robot AI research projects](syntheses/platforms/open-source-robot-ai-projects.md) — grouped catalog (LeRobot ecosystem, JEPA code, open VLAs, simulators, RL benchmarks, open robot platforms, and more).

## Onboard compute — the Jetson ladder
If you're picking the computer that rides *on* the robot: [Jetson module ladder — performance and power](syntheses/platforms/jetson-module-ladder-power-performance.md) — every SKU from Orin Nano 4 GB to AGX Thor T5000 in one table (specs, price, TOPS/W, merged `nvpmodel` power modes), the measured on-Jetson VLA rates that exist, and the Orin→Thor platform breaks (no RT cores, no MIPI-CSI). For the buying decision on a battery robot, [Onboard compute for XLeRobot](syntheses/platforms/jetson-onboard-compute-xlerobot.md) narrows it to one pick per tier.

## NVIDIA GPU rental landscape
If you need GPU compute for training, fine-tuning, or running policies and world models: [NVIDIA GPU rental landscape](syntheses/platforms/nvidia-gpu-rental-landscape.md) — providers, pricing, and how to choose (Brev / RunPod / Lambda Labs / CoreWeave / Vast.ai / DGX Cloud / DGX Spark rentals at $0.48/hr).

## Where else to start (by intent)
- **You're new to this repo entirely:** start with the [repo README](../README.md) for the directory layout, then come back here.
- **You want the broader landscape** (humanoids you can't easily buy, simulators, FRC platforms, etc.): see [index.md](index.md) under **Entities → Robot platforms** and **Humanoids**.
- **You want to set up a home-robot research project:** start with [Assistive robotics R&D landscape](syntheses/assistive/assistive-robotics-research-landscape.md) and [Module 13](syntheses/curriculum/curriculum-13-home-robotics-deployment.md). Then [LeWM-on-Stretch feasibility](syntheses/projects/lewm-on-stretch-feasibility.md) or [DINO-WM-on-Stretch experiment](syntheses/projects/dino-wm-on-stretch-experiment.md) depending on which WM you'd prefer to try.
- **You want to learn the robotics-policy landscape end to end:** start with [the curriculum hub](syntheses/curriculum/robot-learning-curriculum.md). The prereq diagnostic at the top of [Module 1](syntheses/curriculum/curriculum-01-neural-networks.md) tells you whether you can skim Tier 1.
- **You want to understand LeWorldModel specifically:** start with [the curriculum hub](syntheses/curriculum/robot-learning-curriculum.md), then jump to [Module 10](syntheses/curriculum/curriculum-10-world-models.md) → [Module 11](syntheses/curriculum/curriculum-11-jepa-deep.md) → [Module 12](syntheses/curriculum/curriculum-12-lewm-deep-dive.md) (assumes ML basics).
- **You want to actually reproduce LeWorldModel:** [LeWM howto](syntheses/world-models/leworldmodel-howto.md) + [hello-world scope](syntheses/projects/lewm-hello-world-project-scope.md) + [Module 14 capstone](syntheses/curriculum/curriculum-14-capstone.md).
- **You're looking up an acronym:** [glossary.md](glossary.md). Ctrl-F.
- **You want the full catalog:** [index.md](index.md). Every page listed, organized by category.
- **You want to know what was done when:** [log.md](log.md). Append-only chronological record of ingests, syntheses, lint passes, and curriculum-module drafts. Grep with `grep "^## \[" log.md | tail -20` to see recent activity.

## Robot AI curriculum

The single most ambitious artifact in this wiki is a **14-module bottom-up curriculum** for going from neural-network basics to reading the [LeWorldModel paper](sources/leworldmodel-paper.md) and reasoning about home-robotics policy-learning techniques.

**Status: all 14 modules drafted.** Reader-traversable from absolute beginning through the destination and capstone.

- Hub: [Robot-learning curriculum — from neurons to LeWorldModel](syntheses/curriculum/robot-learning-curriculum.md).
- Glossary (cross-linked from every module): [glossary.md](glossary.md) — ~100 acronyms with one-line definitions.

The curriculum has five tiers:

| Tier | Modules | Theme |
| --- | --- | --- |
| **1** | [1](syntheses/curriculum/curriculum-01-neural-networks.md), [2](syntheses/curriculum/curriculum-02-cnns.md), [3](syntheses/curriculum/curriculum-03-attention-and-transformers.md), [4](syntheses/curriculum/curriculum-04-self-supervised-learning.md) | ML foundations: NN basics, CNNs, transformers/ViT, SSL. Brisk-but-rigorous refreshers; each module opens with a prereq diagnostic for self-assessment. |
| **2** | [5](syntheses/curriculum/curriculum-05-generative-models.md) | Generative modeling fundamentals with a full DDPM math walkthrough (ELBO → `L_simple` derivation, KL bounds, classifier-free-guidance derivation). |
| **3** | [6](syntheses/curriculum/curriculum-06-imitation-learning.md), [7](syntheses/curriculum/curriculum-07-bc-lineage-pusht.md), [8](syntheses/curriculum/curriculum-08-rl-vocabulary.md), [9](syntheses/curriculum/curriculum-09-vla.md) | Robot learning paradigms: imitation learning, BC-lineage on PushT (IBC → BeT → Diffusion Policy), RL vocabulary, VLA models. |
| **4** | [10](syntheses/curriculum/curriculum-10-world-models.md), [11](syntheses/curriculum/curriculum-11-jepa-deep.md), [12](syntheses/curriculum/curriculum-12-lewm-deep-dive.md) | World models: four-family taxonomy, JEPA in depth (with the collapse-prevention zoo), the LeWM deep-dive with the full SIGReg derivation. |
| **5** | [13](syntheses/curriculum/curriculum-13-home-robotics-deployment.md), [14](syntheses/curriculum/curriculum-14-capstone.md) | Deployment reality (the 89.4% / 12.4% RLBench-vs-BEHAVIOR-1K gap; Stretch as platform) + capstone (Phase A: reproduce LeWM PushT + experiment-design memo; Phase B: real-Stretch execution if hardware available). |

The **destination** is Module 12 (LeWM deep-dive with full SIGReg math). The reading order is mostly linear, but the [module dependency graph](syntheses/curriculum/robot-learning-curriculum.md) gives readers permission to skip Tier 1 modules they're comfortable with.

### JEPA / LeWorldModel

A long-running thread of this wiki, and the original motivating goal. Primary sources for the entire SIGReg-LeWM-PLDM lineage are filed:

- [LeWorldModel Paper](sources/leworldmodel-paper.md) (Maes et al. 2026) — the destination paper.
- [LeJEPA Paper](sources/lejepa-paper.md) (Balestriero & LeCun 2025) — the SIGReg foundational paper.
- [PLDM Paper](sources/pldm-paper.md) (Sobal et al. 2025) + [Sobal et al. 2022](sources/sobal2022-jepa-slow-features-paper.md) — the end-to-end-JEPA-baseline lineage.
- [V-JEPA 2 Paper](sources/v-jepa-2-paper.md) and [V-JEPA 2.1 Paper](sources/v-jepa-2-1-paper.md) — Meta FAIR's parallel JEPA-at-scale line.
- [DINO-WM Paper](sources/dino-wm-paper.md), [JEPA-WMs Paper](sources/jepa-wms-paper.md) — frozen-feature alternatives.
- [DreamerV3 Paper](sources/dreamer-v3-paper.md), [TD-MPC2 Paper](sources/td-mpc2-paper.md) — the MBRL baselines LeWM benchmarks against.

Concept pages: [Joint-Embedding Predictive Architecture](concepts/world-models/jepa.md), [World model](concepts/world-models/world-model.md), [World-model simulators](concepts/world-models/world-model-simulators.md), [Learned latent space](concepts/world-models/latent-space.md).

Syntheses: [generative-video vs JEPA world models](syntheses/world-models/generative-video-vs-jepa-world-models.md), [LeWM-on-Stretch feasibility](syntheses/projects/lewm-on-stretch-feasibility.md), [LeWM-on-ROSOrin-Pro feasibility](syntheses/projects/lewm-on-rosorin-pro-feasibility.md), [LeWM howto](syntheses/world-models/leworldmodel-howto.md), [LeWM hello-world scope](syntheses/projects/lewm-hello-world-project-scope.md).

> [!note] Still a live question, not a settled destination
> LeWorldModel was the wiki's original organizing target, and the [curriculum](syntheses/curriculum/robot-learning-curriculum.md) above still lands on it. Two things have since complicated the picture. **In its favor:** [When Does LeJEPA Learn a World Model?](sources/when-does-lejepa-learn-a-world-model-paper.md) (May 2026) proves the LeJEPA recipe achieves [linear identifiability](concepts/world-models/identifiability.md) of the world's latents — the strongest formal result the JEPA program has. **Against:** [stable-worldmodel](sources/stable-worldmodel-paper.md) (May 2026, same group) measures LeWM **collapsing to 6–26 % under mild visual perturbation**. Meanwhile the [VLA](concepts/learning/vla-models.md) line the JEPA program dismisses keeps producing real-world results ([π0.7](entities/pi07.md), [MolmoAct2](entities/molmoact2.md)).
>
> Read this section as **one serious bet on how world models should work**, worth understanding deeply — not as the wiki's answer. The broader question is [generative-video vs JEPA](syntheses/world-models/generative-video-vs-jepa-world-models.md), and it is open.


## Other major themes

Beyond the curriculum, the wiki has accumulated content across several clusters. Listed here briefly; full catalog is in [index.md](index.md).

### Behavior cloning lineage

The policy-learning side. Filed end-to-end:

- [IBC Paper](sources/ibc-paper.md), [BET Paper](sources/bet-paper.md), [Diffusion Policy Paper](sources/diffusion-policy-paper.md), [DDPM Paper](sources/ddpm-paper.md), [UMI Project Page](sources/umi-paper.md).
- VLAs: [π0 Paper](sources/pi-zero-paper.md), [Helix (Figure AI blog)](sources/helix-blog.md), [VLA-JEPA Paper](sources/vla-jepa-paper.md), and entities for [GR00T](entities/nvidia-groot.md), [Gemini Robotics](entities/gemini-robotics.md), [Physical Intelligence](entities/physical-intelligence.md), [Figure](entities/figure.md).

Concept pages: [Imitation learning](concepts/learning/imitation-learning.md), [VLA models](concepts/learning/vla-models.md).

### Assistive robotics

A separate research thread feeding into the curriculum's Module 13 (home-robotics deployment).

- [Maya Cakmak](entities/maya-cakmak.md)'s [HCR Lab](entities/hcrlab.md) at UW — long-term in-home deployments with Henry Evans.
- [Amal Nanavati](entities/amal-nanavati.md) — robot-assisted feeding; PAR systematic review.
- [Stretch](entities/stretch.md) (Hello Robot) — the de-facto research platform.
- [Robot Utility Models](entities/robot-utility-models.md), [OK-Robot](entities/ok-robot.md) — the strongest current home-robotics results, both on Stretch, both BC-line.

Syntheses: [Assistive robotics R&D landscape](syntheses/assistive/assistive-robotics-research-landscape.md), [Levels of autonomy in assistive robotics](syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md), [Long-term in-home robot deployments](syntheses/assistive/long-term-in-home-robot-deployments.md), [Stretch as assistive platform](syntheses/assistive/stretch-as-assistive-platform.md), [Underserved PAR domains](syntheses/assistive/underserved-par-domains.md).

### AI safety and alignment

Auxiliary cluster — relevant context for agentic robotics.

- [Claude's Constitution](sources/claudes-constitution.md) — Anthropic's primary specification.
- Concept pages: [AI safety and alignment](concepts/safety/ai-safety-alignment.md), [Corrigibility](concepts/safety/corrigibility.md), [LLM-agent architecture](concepts/agents/llm-agent-architecture.md).
- Entities: [Anthropic](entities/anthropic.md), [Apollo Research](entities/apollo-research.md).

### Simulators and infrastructure

The sim-stack landscape circa 2026.

- [Simulators for agentic robotics — 2026 landscape](syntheses/simulators/simulators-for-agentic-robotics-2026.md) — six-category survey.
- [Newton + OpenUSD substrate convergence](syntheses/simulators/newton-openusd-substrate-convergence.md), [OpenUSD support across simulators](syntheses/simulators/openusd-support-across-simulators.md).
- Entities: [NVIDIA Isaac Sim / Lab](entities/nvidia-isaac-sim.md), [MuJoCo](entities/mujoco.md), [MuJoCo Playground](entities/mujoco-playground.md), [Newton physics engine](entities/newton-physics-engine.md), [Genesis](entities/genesis.md), [AGIBOT Genie Sim](entities/agibot-genie-sim.md), [RoboCasa](entities/robocasa.md), [ManiSkill](entities/maniskill.md).

### Whole-organism agentic AI (fruit fly)

A discrete research thread on biological agent loops.

- [Whole-organism agentic AI](syntheses/agents/whole-organism-agentic-ai.md) — synthesis.
- [flybody](entities/flybody.md), [NeuroMechFly](entities/neuromechfly.md), [FlyWire](entities/flywire.md), [Drosophila brain model](entities/drosophila-brain-model.md), [flyvis](entities/flyvis.md).
- Primary sources: [flybody Paper](sources/flybody-paper.md), [Shiu et al. 2024](sources/shiu-fly-brain-paper.md), [Lappalainen et al. 2024](sources/lappalainen-flyvis-paper.md), [Berkeley News on fly brain](sources/berkeley-fly-brain-news.md).

### FRC (FIRST Robotics Competition)

A separate hobby/competition thread.

- [FRC 2026 Game Manual](sources/frc-2026-game-manual.md), [FRC KitBot 2026](sources/frc-kitbot-2026.md), [Team 254 AI in FRC presentation](sources/team-254-ai-in-frc-presentation.md).
- Entities: [FIRST Robotics Competition](entities/first-robotics-competition.md), [FRC KitBot](entities/frc-kitbot.md), [AndyMark](entities/andymark.md), [Team 254](entities/team-254.md), [roboRIO](entities/roborio.md).
- Synthesis: [FRC simulation & AI landscape](syntheses/simulators/frc-simulation-and-ai-landscape.md).

### ROSOrin Pro project ladder

A practical project sequence for learning JEPA on educational hardware.

- [JEPA project ladder for ROSOrin Pro](syntheses/projects/jepa-project-ladder-rosorin-pro.md) — six-rung ladder.
- [LeWM on ROSOrin Pro — feasibility](syntheses/projects/lewm-on-rosorin-pro-feasibility.md).
- Entities: [ROSOrin / ROSOrin Pro](entities/rosorin.md), [Hiwonder](entities/hiwonder.md), [OpenClaw](entities/openclaw.md), [openclaw_controller](entities/openclaw-controller.md).

### Agentic UAVs (drones)

If your interest is in the air rather than the ground: [Agentic UAVs](concepts/robotics/agentic-uavs.md) — four-layer architecture (perception / cognition / control / communication), key enabling technologies, and how learned-controller research connects to the open-source [PX4 Autopilot](entities/px4-autopilot.md) flight stack on [Pixhawk](entities/pixhawk.md) hardware.

**Start here for the open-source UAV stack: [dronecode.org](https://dronecode.org/)** — the Linux Foundation Collaborative Project that stewards PX4, [MAVLink](entities/mavlink.md), Pixhawk, QGroundControl, and MAVSDK under one vendor-neutral umbrella. See the wiki's [Dronecode Foundation entity](entities/dronecode-foundation.md) for governance context.


## How this wiki discriminates — its ten strongest axes

The sections above describe *what* is here. This one describes *how it judges* — the recurring analytical axes that do the work of separating things vendor language conflates. If you read only one section before using the wiki to make a decision, read this one.

An axis earns a place by four tests: it **recurs across many pages**, it **discriminates between things that otherwise look alike**, it is **anchored in numbers rather than opinion**, and it has **changed at least one conclusion here**.

| # | Axis | Home page | What anchors it |
| --- | --- | --- | --- |
| 1 | **Control abstraction level** | [control abstraction levels](concepts/robotics/control-abstraction-levels.md) | Four levels (torques → controller → policy commands → RL setup), Level 2 subdividing into eight ([CaP-X](sources/cap-x-paper.md)); 11 models × 4 levels × 3 robots ([Anthropic](sources/anthropic-how-claude-performs-on-robotics-tasks.md)) |
| 2 | **Statistical power / N** | [success-rate audit](syntheses/platforms/vla-success-rate-audit.md) | ±2 pp needs ~1,030–2,450 rollouts; the top of the LIBERO table is a **statistical tie** |
| 3 | **Control rate (Hz)** | [control-rate ladder](syntheses/platforms/control-rate-ladder.md) | ~30 rows, 0.2 Hz LLMs → 1 kHz servo loops, REQ/MEAS/CAP tagged; the **83 Hz vs 0.2–0.4 Hz** gap |
| 4 | **Benchmark vs deployment** | [AI Index 2026](sources/stanford-hai-ai-index-2026.md), [LIBERO-PRO](sources/libero-pro-paper.md) | RLBench **89.4%** vs BEHAVIOR-1K **12.4%**; >90% models collapse to **0.0%** under perturbation |
| 5 | **Power envelope (W, Wh)** | [module ladder](syntheses/platforms/jetson-module-ladder-power-performance.md), [onboard compute](syntheses/platforms/jetson-onboard-compute-xlerobot.md) | 7–25 W Orin Nano → 40–130 W Thor against a 288 Wh pack; TOPS/W |
| 6 | **Cost ladder** | [platform comparison](syntheses/platforms/robot-platforms-comparison.md), [value chain](syntheses/society/consumer-robotics-value-chain.md) | $660 → $2,499 → $29,950 → $89,999; **86% of [UME](entities/ume.md)'s BOM is actuators** |
| 7 | **Code-as-policy vs end-to-end policy** | [code as policy](concepts/agents/code-as-policy.md) | *Code agents degrade gracefully where trained policies fall off a cliff — and lose to them in-distribution.* Constant since 2022 |
| 8 | **Compute placement** | [where the compute lives](syntheses/agents/on-device-and-on-robot-agents.md) | On-robot / local server / cloud; "the split-brain pattern is the norm" |
| 9 | **Prevention / detection / intervention** | [prevention-detection-intervention](syntheses/platforms/prevention-detection-intervention.md) | [PACS](sources/pacs-paper.md): a CBF filter drops success to **0.04**, path-consistent braking holds **0.72** |
| 10 | **Readability vs embodiment-agnosticism** | [action representation languages](syntheses/agents/action-representation-languages.md) | [RT-H](sources/rt-h-paper.md): relabel the same phrases as integers and performance drops — *the grammar ports, the lexicon cannot* |

Three of these are worth understanding before the others, because they change how you read everything else:

- **Axis 1 is non-monotonic.** Capability *inverts* across abstraction levels, so "model X can/can't control a robot" is not a claim — "model X at level 1 can't and at level 3 can" is. Its corollary, **access level is part of the system**, is also the wiki's core safety thesis.
- **Axis 2 is retroactive.** It re-scores every policy comparison already in the wiki. Applying it demoted one product announcement to anecdote-grade and found that a buried [TurboVLA](sources/turbovla-paper.md) bimanual result survives (p=0.0012) while its headline number does not.
- **Axis 3 explains structure, not just speed.** The ~100× gap between what real-time control demands and what inference delivers is not closed by faster models; it is bridged **architecturally**, by making the model *write* the controller rather than *be* it.

> [!warning] The axes that are weak here — where this wiki will mislead you
> - **Anything economic.** No revenue, unit-volume, market-sizing or supply-chain data. The two pages that reason about markets ([value chain](syntheses/society/consumer-robotics-value-chain.md), [home AI platform](syntheses/agents/home-ai-platform-trust-and-authority.md)) carry that warning at the top and infer from the technology stack instead.
> - **Human factors and multi-tenancy.** Per-person authority in a shared home — guests, children, elderly relatives — has **no ingested source at all**. That is a literature gap, not merely a wiki gap.
> - **Long-horizon reliability.** Almost everything here is measured in single sessions. The [long-term in-home deployments](syntheses/assistive/long-term-in-home-robot-deployments.md) thread is the only counterweight.
> - **Safety certification.** [ISO 13482](concepts/robotics/robot-safety-standards.md) is documented as a pathway with essentially nothing measured against it.
> - **Home automation.** One ingested source ([Matter 1.4](sources/matter-1-4-core-specification.md)) and nothing on Thread, HomeKit, SmartThings, Alexa, Nest or Ring.

## Conventions in one paragraph

Pages use YAML frontmatter (`title`, `type`, `created`, `updated`, `sources`, `tags`). Every factual claim links to a source page (not a raw file). Filenames are kebab-case slugs. Links are standard markdown relative paths (no Obsidian `[[wikilinks]]`). Source-page conventions: `## Summary`, `## Key claims`, `## Entities mentioned`, `## Concepts touched`, `## Open questions`. Entity/concept pages end with a `## Mentioned in` section listing inbound sources. Contradictions across sources are flagged with `> [!warning] Contradiction` callouts. Full conventions are in [`CLAUDE.md`](../CLAUDE.md).

## Quick stats (as of 2026-08-17)

| Layer | Count | Was 2026-05-17 |
| --- | --- | --- |
| Source pages (`wiki/sources/`) | **414** | 145 |
| Entity pages (`wiki/entities/`) | **412** | 164 |
| Concept pages (`wiki/concepts/`) | **86** | 26 |
| Synthesis pages (`wiki/syntheses/`) | **83** (incl. the 14 curriculum modules + hub) | 44 |
| Top-level (`index.md`, `log.md`, `glossary.md`, `overview.md`, `backlog.md`) | **5** | 4 |
| **Total wiki pages** | **1,000** | 383 |

Plus `wiki/notes/` — the user's own notes directory, not maintained by Claude and excluded from the count above.

**Roughly 2.6× in three months**, with entity and source pages growing in step — the ingest pattern is holding (a single ingest touches 5–15 pages, so sources and entities compound together rather than one outrunning the other).

## What's not here

A few things this wiki deliberately doesn't cover:

- **Classical robotics** (kinematics, dynamics, control theory, ROS plumbing, SLAM, segmentation pipelines) — out of scope for the curriculum, by design.
- **Implementation details** of any specific algorithm beyond what's pedagogically useful.
- **A literature-survey treatment** of the field — the wiki is curated around what's relevant to the curriculum's destination (LeWM on home robotics), not exhaustive.

## Provenance

This wiki is part of the `robot-research` repository. Built incrementally starting 2026-05-06; actively maintained. The curriculum is the principal artifact; the surrounding entity / concept / source pages exist either as direct curriculum dependencies or as accumulated context from prior research threads (FRC, fruit-fly simulation, AI safety, assistive robotics).
