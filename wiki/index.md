# Index

## Highlights

Curated entry points across the wiki.

**AI Safety and Alignment**
- [Claude's Constitution](sources/claudes-constitution.md) — Anthropic's primary specification for Claude's values, corrigibility model, principal hierarchy, and hard constraints.
- [AI safety and alignment](concepts/ai-safety-alignment.md) — concept overview; connects to agentic robot deployments.
- [Corrigibility](concepts/corrigibility.md) — the corrigibility dial, asymmetric cost argument, galaxy-brained reasoning risk.
- [Apollo Research](entities/apollo-research.md) — independent safety evaluation institute; red-teamed Claude Opus 4.

**Assistive Robotics**
- [Assistive robotics](concepts/assistive-robotics.md) — concept overview; sim-to-real gap quantified (89.4% RLBench vs 12.4% BEHAVIOR-1K household tasks).
- [Assistive robotics — R&D landscape and JEPA applicability](syntheses/assistive-robotics-research-landscape.md) — seven blocking problems, timeline, active researchers, independent-researcher paths, JEPA fit.
- [OK-Robot](entities/ok-robot.md) — zero-shot pick-and-drop in 10 homes; 58.5% success; state-of-the-art household manipulation.
- [Robot Utility Models](entities/robot-utility-models.md) — NYU/Meta zero-shot BC; data diversity > data quantity insight.
- [Stanford HAI — AI Index Report 2026](sources/stanford-hai-ai-index-2026.md) — 89.4% vs 12.4% gap; humanoid landscape; Physical AI assessment.

**FRC (FIRST Robotics Competition)**
- [FRC 2026 Game Manual — REBUILT](sources/frc-2026-game-manual.md) — deep ingest of the 166-page 2026 REBUILT game manual.
- [FIRST Robotics Competition](entities/first-robotics-competition.md) — competition overview, robot constraints, technical infrastructure.
- [FRC KitBot](entities/frc-kitbot.md) — the beginner-friendly KitBot platform.
- [FRC simulation & AI landscape](syntheses/frc-simulation-and-ai-landscape.md) — what simulation & AI tools FRC teams use (trajectory planners, physics sims, ML frontier).

**JEPA / LeWorldModel**
- [Joint-Embedding Predictive Architecture](concepts/jepa.md) — JEPA concept page.
- [Learned latent space](concepts/latent-space.md) — the substrate JEPAs predict in.
- [LeWorldModel Paper](sources/leworldmodel-paper.md) — LeWM paper ingest.
- [LeWorldModel — train and run howto](syntheses/leworldmodel-howto.md) — how to install, train, and evaluate LeWM on a single GPU.
- [LeWM hello world — Project 1 detailed scope](syntheses/lewm-hello-world-project-scope.md) — reproduce LeWM PushT from scratch.
- [JEPA task capabilities](syntheses/jepa-task-capabilities.md) — what JEPA models can do, mapped per-paper.

**ROSOrin Pro JEPA project ladder**
- [JEPA project ladder for ROSOrin Pro](syntheses/jepa-project-ladder-rosorin-pro.md) — six-rung educational/research project ladder for learning JEPA on ROSOrin Pro hardware.
- [LeWM on ROSOrin Pro — feasibility analysis](syntheses/lewm-on-rosorin-pro-feasibility.md) — feasibility analysis for deploying LeWM on ROSOrin Pro.

**Whole-organism agentic AI (fruit fly)**
- [Whole-organism agentic AI](syntheses/whole-organism-agentic-ai.md) — brain ([FlyWire](entities/flywire.md)) + body ([flybody](entities/flybody.md) / [NeuroMechFly v2](entities/neuromechfly.md)) for *Drosophila*: the first plausible end-to-end animal-scale agent loop.
- [flybody](entities/flybody.md) — HHMI Janelia + DeepMind whole-body fly physics in MuJoCo (walking + flight).
- [NeuroMechFly](entities/neuromechfly.md) — NeLy/EPFL parallel platform (walking + vision + olfaction + brain–VNC); active flygym v2.x.x with GPU acceleration.
- [FlyWire](entities/flywire.md) — complete adult *Drosophila* connectome.
- [Drosophila brain model](entities/drosophila-brain-model.md) and [flyvis](entities/flyvis.md) — open-source brain-side controllers (LIF + connectome-constrained DMN).
- [Biomechanical simulation](concepts/biomechanical-simulation.md) and [Connectome](concepts/connectome.md) — concept pages.

**General**
- [Simulators for agentic robotics — 2026 landscape](syntheses/simulators-for-agentic-robotics-2026.md) — landscape survey across six categories.

## Sources (chronological)
- [OK-Robot Project Page](sources/ok-robot-project-page.md) — zero-shot pick-and-drop in 10 NYC homes; 58.5% success; 1.8× over OVMM. (2024-01)
- [HomeRobot — OVMM](sources/ovmm-homerobot.md) — Open Vocabulary Mobile Manipulation benchmark on Stretch; 20% real-world baseline. (2024)
- [IEEE Spectrum — Stretch Assistive Robot](sources/ieee-spectrum-stretch-assistive.md) — Stretch as assistive device for quadriplegic user Henry Evans. (2023-10-08)
- [TurtleBot 4 — Clearpath Robotics](sources/clearpath-turtlebot-4.md) — ROS 2 educational mobile robot on iRobot Create 3; Raspberry Pi 4B; two variants. (2022 era)
- [Elephant Robotics — myAGV & Compound Collection](sources/elephant-robotics-myagv-compound.md) — affordable compound mobile robot kits; $1,498–$21,999. (Unknown)
- [Elephant Robotics — myBuddy 280](sources/elephant-robotics-mybuddy-280.md) — 13 DOF dual-arm desktop robot; $1,619; ROS1 + MoveIt. (Unknown)
- [Fauna Robotics — Sprout Creator Edition](sources/fauna-robotics-sprout.md) — 107cm, 29 DOF developer humanoid; Jetson AGX Orin 64GB; NYC. (Unknown)
- [1X NEO Product Page](sources/1x-neo-product-page.md) — household humanoid specs; 22 DOF hands; Redwood AI VLM; $200 deposit. (Unknown)
- [Reachy 2 — Pollen Robotics](sources/pollen-robotics-reachy.md) — open-source bimanual mobile manipulator; ROS 2 + Python SDK. (Unknown)
- [ITU AI for Good — Assistive Robots](sources/itu-aiforgood-assistive-robots.md) — survey of 7 assistive robots at 2023 AI for Good Summit. (2023-04-12)
- [Virginia Tech Assistive Robotics Lab](sources/virginia-tech-assistive-robotics-lab.md) — Prof. Alan Asbeck; exoskeletons, soft robotics, haptics. (Unknown)
- [RELab tenoexo — ETH Zurich](sources/relab-ethz-tenoexo.md) — <150g hand orthosis; 5N/finger; benefit in spinal cord injury patients. (Unknown)
- [6 Lessons from a Robotics Startup Failure (K-Scale Labs)](sources/robot-report-kscale-labs-lessons.md) — COO post-mortem; YC humanoid startup shutdown late 2025. (2026-03-02)
- [Robot Utility Models Project Page](sources/robot-utility-models-website.md) — NYU/Meta zero-shot generalist policies for Stretch. (2024-09)
- [Robot Utility Models Paper](sources/robot-utility-models-paper.md) — full RUM paper (arxiv 2409.05865); architecture, ablations, cross-embodiment numbers. (2024-09)
- [ManiSkill-HAB Paper](sources/maniskill-hab-paper.md) — GPU-parallel low-level manipulation chains for HAB. (2024-12)
- [Genesis Project Page](sources/genesis-project-page.md) — generative + ultra-fast physics engine launch. (2024-12)
- [MuJoCo Playground Paper](sources/mujoco-playground-paper.md) — DeepMind's MJX-based robot-learning framework. (2025-02)
- [V-JEPA 2 Paper](sources/v-jepa-2-paper.md) — Meta FAIR's JEPA world model with zero-shot Franka. (2025-06)
- [Genie Envisioner Paper](sources/genie-envisioner-paper.md) — unified world foundation platform for manipulation. (2025-08)
- [Hello Robot Stretch Documentation](sources/hello-robot-stretch-docs.md) — Stretch 3 docs (ROS 2 + Python + MuJoCo/Gazebo). (2025)
- [Stretch AI LLM Agent Documentation](sources/stretch-ai-llm-agent-docs.md) — concrete LLM-agent stack for the Stretch robot. (2024–2025)
- [Hiwonder ROSOrin Documentation](sources/hiwonder-rosorin-docs.md) — educational Jetson Orin Nano kit; Gazebo + cloud/offline LLM-agent curriculum. (2024–2025)
- [Hiwonder ROSOrin Pro User Manual](sources/hiwonder-rosorin-pro-user-manual.md) — hardware spec sheet for the 6-DOF arm + base variant. (2024–2025)
- [Hiwonder OpenClaw Practical Tutorial](sources/hiwonder-openclaw-tutorial.md) — Hiwonder's manipulation-aware LLM-agent framework. (2024–2025)
- [RoboCasa365 Paper](sources/robocasa365-paper.md) — 365-task household manipulation benchmark. (ICLR 2026)
- [AGIBOT Genie Sim 3.0 Announcement](sources/agibot-genie-sim-3-announcement.md) — open simulation platform launch at CES 2026. (2026-01)
- [AGIBOT Genie Envisioner 2.0 Announcement](sources/agibot-genie-envisioner-2-announcement.md) — world model evolved into a "world simulator." (2026)
- [NVIDIA Newton Physics Engine Developer Page](sources/nvidia-newton-physics-engine-developer-page.md) — Newton landing page; Linux-Foundation governance. (2026)
- [NVIDIA Newton Contact-Rich Manipulation Blog](sources/nvidia-newton-contact-rich-manipulation-blog.md) — Newton 1.0 GA at GTC 2026 inside Isaac Lab. (2026)
- [LeWorldModel Paper](sources/leworldmodel-paper.md) — first stable end-to-end JEPA from raw pixels. (2026-03)
- [LeWorldModel GitHub (lucas-maes/le-wm)](sources/lewm-github.md) — MIT-licensed; ViT+AR Predictor+SIGReg; HuggingFace checkpoints for 4 envs; baseline list. (2026)
- [V-JEPA 2 GitHub (facebookresearch/vjepa2)](sources/vjepa2-github.md) — variant family (ViT-B→g, 80M–2B), V-JEPA 2.1 training additions, dual license. (2026)
- [MLWorks — LeWorldModel: Navigate the World from Raw Pixels](sources/medium-lewm-navigate-world.md) — secondary blog post (paywalled). (2026-03-30)
- [Towards Deep Learning — This World Model Learns Physics by Watching Videos](sources/towardsdeeplearning-world-model-physics.md) — secondary blog post (paywalled). (2026-03-24)
- [Towards AI — LeCun / AMI Labs / 3 World Models](sources/towardsai-lecun-ami-labs.md) — secondary journalism; reports LeCun founded AMI Labs with $1.03B (provisional). (2026-04-27)
- [Top 10 Physical AI Models 2026](sources/top-10-physical-ai-models-2026.md) — VLA model survey including GR00T N1.7 EA. (2026-04)
- [New Video Series: What Developers Need to Know About OpenUSD](sources/nvidia-openusd-developer-video-series.md) — NVIDIA blog; four core USD features incl. Hydra pipeline. (2024-04-11)
- [OpenUSD Rigid Body Physics Proposal](sources/openusd-rigid-body-physics-proposal.md) — UsdPhysics whitepaper, robotics schemas in the standard. (2020 / 26.05 docs)
- [Using OpenUSD for Modular and Scalable Robotic Simulation](sources/nvidia-openusd-for-robotic-simulation.md) — NVIDIA's robotics-USD position + roadmap. (2025-03-18)
- [Building CAD-to-USD Workflows with NVIDIA Omniverse](sources/nvidia-cad-to-usd-jt-workflows.md) — JT-to-USD pipeline, OpenUSD Exchange SDK. (2025-07-29)
- [URDF vs MJCF vs USD comparison](sources/source-robotics-urdf-mjcf-usd-comparison.md) — practitioner survey. (2026-03-13)
- [UAVs Meet Agentic AI — Multidomain Survey](sources/uavs-agentic-ai-survey.md) — 4-layer agentic UAV architecture; 8 application domains; Cornell + U. Peloponnese. (2025-06)
- [MIT Drone Adaptive Control](sources/mit-drone-adaptive-control.md) — meta-learning + mirror descent; 50% less tracking error; 15 min training data. (2025-06-09)
- [Learning Control-Oriented Dynamical Structure from Data](sources/learning-control-oriented-dynamical-structure.md) — SD-LQR: learned SDC factorizations for SDRE nonlinear tracking; ICML 2023; Azizan et al. (2023-06)
- [Claude's Constitution](sources/claudes-constitution.md) — Anthropic's 82-page specification of Claude's values, corrigibility model, principal hierarchy, honesty properties, and hard constraints. CC0 1.0. (2026-01-21)
- [Are We Building Skynet? — Medium (2025)](sources/medium-are-we-building-skynet.md) — secondary journalism; MCP (>1,000 connectors), A2A (50+ supporters), Apollo Research Claude Opus 4 safety eval. (2025, date unknown)
- [Stanford HAI — AI Index Report 2026](sources/stanford-hai-ai-index-2026.md) — 9th edition; 89.4% RLBench vs 12.4% BEHAVIOR-1K household tasks; model convergence at frontier; US–China gap 2.7%; $285.9B US AI investment; AI incidents 362. (2026)
- [Arcade Learning Environment — Farama Project Page](sources/ale-farama.md) — Farama's Atari 2600 RL benchmark; 100+ games, 23 multi-agent envs, Gymnasium API. (Unknown)
- [Farama Foundation Projects Page](sources/farama-projects-page.md) — index of 19 RL env / API standards (Gymnasium, PettingZoo, Minari, …). (2026)
- [Gymnasium-Robotics Documentation](sources/gymnasium-robotics-docs.md) — six MuJoCo env families (Fetch, Shadow Hand, Maze, Adroit, Franka Kitchen, MaMuJoCo). (2026)
- [DINO-WM Paper](sources/dino-wm-paper.md) — DINOv2-feature world model + zero-shot planning; lightweight MuJoCo benches. (2024-11)
- [DINO-world Paper](sources/dino-world-paper.md) — FAIR DINOv2-latent video world model ("Back to the Features"). (2025-07)
- [JEPA-WMs Paper](sources/jepa-wms-paper.md) — Terver et al., FAIR; first JEPA paper to use RoboCasa + Metaworld + DROID + real Franka. (2025-12)
- [VLA-JEPA Paper](sources/vla-jepa-paper.md) — JEPA-as-auxiliary inside a VLA; LIBERO + SimplerEnv + real. (2026-02)
- [V-JEPA 2.1 Paper](sources/v-jepa-2-1-paper.md) — direct successor to V-JEPA 2; "dense features" + +20pt real-Franka grasping. (2026-03)
- [FRC 2026 Game Manual — REBUILT](sources/frc-2026-game-manual.md) — 166-page rule book for FIRST Robotics Competition 2026; game mechanics, robot constraints, AprilTag field, scoring. (2026-01-10)
- [FRC KitBot 2026](sources/frc-kitbot-2026.md) — official KitBot resource page; AM14U6 chassis, Java code, CAD, multilingual docs. (2026-01)
- [Team 254: The Next Revolution — AI in FRC](sources/team-254-ai-in-frc-presentation.md) — 2026 Championship Conference presentation; Claude Code, wpilib-agent-tools, closed-loop agent workflows. (2026-05-04)
- [Team 254 Website](sources/team-254-website.md) — official site; robot history, programs, technical resources. (2026)
- [Berkeley News — researchers simulate an entire fly brain on a laptop](sources/berkeley-fly-brain-news.md) — Phil Shiu's leaky-integrate-and-fire simulation of the full FlyWire connectome. (2024-10-02)
- [flybody Paper — Vaxenburg et al. 2025, Nature](sources/flybody-paper.md) — anatomically detailed *Drosophila* whole-body MuJoCo simulator + DMPO-trained walking & vision-guided flight controllers. (2025-04-23)
- [flybody GitHub (TuragaLab/flybody)](sources/flybody-github.md) — Apache-2.0 release: body XML, dm_control tasks, Ray-distributed DMPO training. (2024–2025)
- [Shiu et al. 2024 — A Drosophila computational brain model](sources/shiu-fly-brain-paper.md) — *Nature* paper behind the "fly brain on a laptop" claim; LIF model on the full FlyWire connectome via Brian 2; MIT-licensed code. (2024-10-02)
- [Lappalainen et al. 2024 — Connectome-constrained networks predict fly visual-system activity](sources/lappalainen-flyvis-paper.md) — *Nature* paper; PyTorch deep net with optic-lobe connectome as fixed connectivity mask; 64 cell types / 45k neurons; predicts T4/T5 motion selectivity. (2024-09-11)
- [neuromechfly.org website](sources/neuromechfly-website.md) — project website for NeuroMechFly v2; vision + olfaction + brain–VNC; tutorials + installation; v2 launched March 2026. (2024–2026)
- [flygym GitHub (NeLy-EPFL/flygym)](sources/flygym-github.md) — Apache-2.0 Python library implementing NeuroMechFly v2; v2.0.1 release. (2026-04-17)

## Entities

### Companies
- [NVIDIA](entities/nvidia.md) — owns most of the agentic-robotics simulation substrate. (8 sources)
- [Hiwonder](entities/hiwonder.md) — Chinese educational-robotics vendor; ROSOrin / ROSOrin Pro kits + OpenClaw. (3 sources)
- [AGIBOT](entities/agibot.md) — Shanghai embodied-AI / humanoid company. Open-source-heavy. (3 sources)
- [Hello Robot](entities/hello-robot.md) — Stretch mobile manipulator + stretch_ai stack. (6 sources)
- [Elephant Robotics](entities/elephant-robotics.md) — Chinese edu-robotics vendor; myAGV + myBuddy 280 + arm ecosystem. (2 sources)
- [Pollen Robotics](entities/pollen-robotics.md) — French open-source humanoid maker; Reachy 2. (1 source)
- [Fauna Robotics](entities/fauna-robotics.md) — NYC; Sprout Creator Edition; 107cm, 29 DOF, Jetson AGX Orin. (1 source)
- [K-Scale Labs](entities/k-scale-labs.md) — YC humanoid startup; shut down late 2025; notable post-mortem. (1 source)
- [Meta FAIR](entities/meta-fair.md) — Yann LeCun's lab; JEPA research line. (6 sources)
- [Google DeepMind](entities/google-deepmind.md) — MuJoCo, Newton co-development, MjcPhysics USD plugin. (5 sources)
- [Mila](entities/mila.md) — Quebec AI Institute; frequent JEPA collaborator. (2 sources) _stub_
- [Farama Foundation](entities/farama-foundation.md) — non-profit; took over OpenAI gym → Gymnasium; 19 RL projects. (3 sources)
- [AMI Labs](entities/ami-labs.md) — Yann LeCun's reported post-Meta AI lab; $1.03B seed round (single secondary source, provisional). (1 source)
- [Anthropic](entities/anthropic.md) — developer of Claude; AI safety mission; author of Claude's Constitution; MCP protocol. (1 source)
- [Apollo Research](entities/apollo-research.md) — independent AI safety evaluation institute; red-teamed Claude Opus 4 (2025). (2 sources)
- [Physical Intelligence](entities/physical-intelligence.md) — San Francisco; π0/π0.6 cross-platform generalist VLAs. (1 source)
- [Hillbot](entities/hillbot.md) — UCSD spinoff that maintains ManiSkill. (1 source) _stub_
- [Disney Research](entities/disney-research.md) — Newton co-developer with NVIDIA + DeepMind. (2 sources) _stub_
- [FIRST Robotics Competition](entities/first-robotics-competition.md) — world's leading high-school robotics competition; ~3,700 teams, 30+ countries. (4 sources)
- [AndyMark](entities/andymark.md) — major FRC vendor; AM14U6 chassis, field elements, FUEL scoring elements. (2 sources)
- [Team 254: The Cheesy Poofs](entities/team-254.md) — elite FRC team (2022 World Champions); 2026 "AI in FRC" presentation; Claude Code + wpilib-agent-tools. (2 sources)
- [HHMI Janelia Research Campus](entities/hhmi-janelia.md) — HHMI's pure-research lab; Turaga lab leads flybody + flyvis; *Drosophila* neuroscience & connectomics anchor. (3 sources)
- [NeLy-EPFL (Neuroengineering Laboratory)](entities/nely-epfl.md) — EPFL lab; maintains [NeuroMechFly](entities/neuromechfly.md) + the `flygym` Python library; European counterweight to HHMI Janelia in fly-body simulation. (2 sources)

### Simulators / frameworks
- [NVIDIA Isaac Sim](entities/nvidia-isaac-sim.md) — Omniverse-based robotics simulator. (4 sources)
- [NVIDIA Isaac Lab](entities/nvidia-isaac-lab.md) — open-source learning framework on Isaac Sim. (5 sources)
- [Newton physics engine](entities/newton-physics-engine.md) — Linux-Foundation, GPU-accelerated. (4 sources)
- [MuJoCo](entities/mujoco.md) — DeepMind-maintained physics engine; substrate for Gymnasium-Robotics, MuJoCo Playground (via MJX), Adroit, Franka Kitchen, DM Control, flybody, NeuroMechFly v2. (11 sources)
- [MuJoCo Playground](entities/mujoco-playground.md) — DeepMind's MJX-based learning framework. (4 sources)
- [Genesis](entities/genesis.md) — generative + ultra-fast physics engine. (2 sources)
- [AGIBOT Genie Sim 3.0](entities/agibot-genie-sim.md) — open embodied-AI sim on Isaac Sim. (2 sources)
- [RoboCasa](entities/robocasa.md) — household manipulation benchmark (RoboCasa365 at ICLR 2026). (3 sources)
- [ManiSkill](entities/maniskill.md) — [SAPIEN](entities/sapien.md)-based GPU-parallel manipulation benchmark. (2 sources)
- [SAPIEN](entities/sapien.md) — UCSD robot simulation framework underlying ManiSkill. (1 source) _stub_
- [Gymnasium-Robotics](entities/gymnasium-robotics.md) — Farama's [MuJoCo](entities/mujoco.md)-backed robotics envs (Fetch / Hand / Maze / Adroit / Franka Kitchen / MaMuJoCo). (2 sources)
- [Arcade Learning Environment](entities/ale.md) — Farama's Atari 2600 RL benchmark; 100+ single-agent + 23 multi-agent envs; Gymnasium API. (1 source)
- [Metaworld](entities/metaworld.md) — Stanford/Berkeley meta-RL benchmark; 50 manipulation tasks on simulated Sawyer; staple across V-JEPA-line work. (1 source)
- [PushT](entities/pusht.md) — 2D T-block pushing benchmark; default lightweight bench across LeWM / DINO-WM / JEPA-WMs. (3 sources)
- [PointMaze](entities/pointmaze.md) — 2D point-mass maze navigation; default lightweight nav bench across LeWM / DINO-WM / JEPA-WMs. (0 sources)
- [DM Control Suite](entities/dm-control.md) — DeepMind continuous-control RL benchmark on top of MuJoCo; pre-Gymnasium-Robotics legacy substrate. (2 sources)
- [LIBERO](entities/libero.md) — lifelong-learning manipulation benchmark; de-facto VLA-eval bench (Spatial / Object / Goal / 100 task families). (0 sources)
- [SimplerEnv](entities/simplerenv.md) — Sapien-adjacent mid-weight sim positioned as real-world-correlation harness; used by VLA-JEPA. (0 sources)
- [Habitat](entities/habitat.md) — Meta FAIR embodied-AI sim (navigation + manipulation in photorealistic 3D scenes); legacy substrate. (0 sources)
- [flybody](entities/flybody.md) — HHMI Janelia + Google DeepMind anatomically detailed *Drosophila* body in MuJoCo (102 DoFs, walking + flight); Apache-2.0. (3 sources)
- [NeuroMechFly](entities/neuromechfly.md) — NeLy/EPFL *Drosophila* body sim with vision + olfaction + brain–VNC hierarchy; v2 (Wang-Chen 2024); flygym v2.x.x package actively maintained 2026 with Warp/MJWarp GPU acceleration. Apache-2.0. (3 sources)

### RL API standards
- [Gymnasium](entities/gymnasium.md) — single-agent RL env API; OpenAI gym successor under Farama. (2 sources)
- [PettingZoo](entities/pettingzoo.md) — multi-agent RL env API. (2 sources)

### Robot platforms
- [Franka Panda](entities/franka-panda.md) — 7-DOF research-grade arm; default tabletop manipulator across DROID, V-JEPA 2, JEPA-WMs, RUM. (5 sources)
- [xArm 7](entities/xarm-7.md) — UFactory commercial 7-DOF arm; secondary tabletop manipulator; RUM cross-embodiment transfer target (~10pt drop vs Stretch). (1 source) _stub_
- [TurtleBot](entities/turtlebot.md) — canonical educational ROS mobile robot (4 generations); TurtleBot 4: Clearpath + iRobot Create 3 + Raspberry Pi 4B + ROS 2. (1 source)
- [iRobot Create 3](entities/irobot-create-3.md) — Roomba-i3-derived ROS 2 mobile-robot base; chassis under [TurtleBot 4](entities/turtlebot.md). (0 sources) _stub_

### Humanoids
- [Atlas](entities/atlas.md) — Boston Dynamics flagship; closed development; capability-bar humanoid. (0 sources) _stub_
- [Tesla Optimus](entities/tesla-optimus.md) — Tesla's vertically-integrated humanoid; closed development. (0 sources) _stub_
- [Figure](entities/figure.md) — Figure AI's humanoid line (01/02/03) + Helix VLA; BMW pilots. (0 sources) _stub_
- [1X NEO](entities/1x-neo.md) — household humanoid; 22 hand DOF/side; Redwood AI VLM; 22 dB; $200 deposit. (1 source)
- [Apptronik Apollo](entities/apptronik-apollo.md) — UT Austin spinout; NVIDIA-aligned ([GR00T](entities/nvidia-groot.md) target); Mercedes-Benz pilots. (0 sources) _stub_
- [Digit](entities/digit.md) — Agility Robotics; **first commercially-deployed humanoid** (GXO, Amazon). (0 sources) _stub_
- [Unitree H1](entities/unitree-h1.md) — Chinese affordable research humanoid (~$90k); rapid 2024–2026 academic adoption. (0 sources) _stub_
- [Unitree G1](entities/unitree-g1.md) — smaller, cheaper Unitree (~$16k); cheapest serious humanoid platform. (0 sources) _stub_
- [NAO](entities/nao.md) — SoftBank/Aldebaran 58-cm educational humanoid; canonical since 2008. (0 sources) _stub_
- [TonyPi](entities/tonypi.md) — Hiwonder hobby-tier biped kit ($300–700); educational-tier sibling of [ROSOrin Pro](entities/rosorin-pro.md). (0 sources) _stub_
- [Stretch](entities/stretch.md) — Hello Robot's mobile manipulator (Stretch 3). De-facto research platform. (7 sources)
- [Reachy 2](entities/reachy.md) — Pollen Robotics' open-source bimanual mobile manipulator for embodied AI; ROS 2; 7 DOF/arm. (1 source)
- [myAGV](entities/myagv.md) — Elephant Robotics autonomous mobile base; ROS; Raspberry Pi 4B; pairs with arms. (1 source)
- [myBuddy 280](entities/mybuddy-280.md) — Elephant Robotics 13 DOF dual-arm desktop robot; $1,619; ROS1. (1 source)
- [ROSOrin](entities/rosorin.md) — Hiwonder's Jetson Orin Nano educational mobile robot kit. (2 sources)
- [ROSOrin Pro](entities/rosorin-pro.md) — Hiwonder's 6-DOF arm + base variant of ROSOrin. (2 sources)
- [ROSOrin Pro 6-DOF arm](entities/rosorin-pro-arm.md) — HX-12H-servo manipulator on the ROSOrin Pro kit. (2 sources)
- [FRC KitBot](entities/frc-kitbot.md) — beginner-friendly FRC robot on AndyMark AM14U6 chassis; included in Kickoff Kit. (2 sources)

### Software stacks
- [stretch_ai](entities/stretch-ai.md) — Hello Robot's open-source Python stack with an LLM agent. (5 sources)
- [OpenClaw](entities/openclaw.md) — Hiwonder's manipulation-aware LLM-agent framework for ROSOrin Pro. (1 source)

### Controllers
- [roboRIO](entities/roborio.md) — NI's mandatory FRC robot controller (ARM Cortex-A9 + FPGA); WPILib ecosystem. (2 sources)
- [stable-worldmodel](entities/stable-worldmodel.md) — Python infrastructure under LeWorldModel (env zoo + planning API + dataset format). DM Control + Gymnasium-Robotics Fetch + classic + OGBench + more. (0 sources)

### Formats / standards
- [OpenUSD](entities/openusd.md) — open scene-description + robotics physics-schema layer (UsdPhysics, MjcPhysics, NewtonSceneAPI). (5 sources)

### Datasets
- [DROID](entities/droid.md) — Distributed Robot Interaction Dataset; 350 hr / 76k traj / 564 scenes of Franka Panda teleop; the dominant real-robot dataset in JEPA-for-robotics work. (2 sources)

### Model organisms / connectomes
- [Drosophila melanogaster](entities/drosophila.md) — fruit fly; canonical "whole-organism AI" target; substrate for both [FlyWire](entities/flywire.md) and [flybody](entities/flybody.md). (6 sources)
- [FlyWire](entities/flywire.md) — international consortium + dataset for the complete adult *Drosophila* brain connectome (139,255 neurons, ~50M synapses; *Nature* 2024). (3 sources)
- [Drosophila brain model](entities/drosophila-brain-model.md) — Phil Shiu's MIT-licensed Brian 2 LIF model on the FlyWire connectome (paper code). (1 source)
- [flyvis](entities/flyvis.md) — TuragaLab's MIT-licensed PyTorch connectome-constrained DMN of the fly visual system; v1.1.3 March 2026. (1 source)

### Vision foundation models
- [DINOv2](entities/dinov2.md) — Meta FAIR self-supervised ViT (142M images, ViT-S/B/L/g); substrate for DINO-WM, DINO-world, JEPA-WMs. Apache 2.0. (3 sources)

### World models
- [NVIDIA Cosmos](entities/nvidia-cosmos.md) — world foundation model + simulation engine (generative video). (5 sources)
- [Genie Envisioner](entities/genie-envisioner.md) — AGIBOT's world simulator GE-Sim2 (generative video). (4 sources)
- [V-JEPA 2](entities/v-jepa-2.md) — Meta FAIR's JEPA world model (latent prediction); zero-shot Franka. (5 sources)
- [LeWorldModel](entities/leworldmodel.md) — first stable end-to-end JEPA from raw pixels. (5 sources)
- [JEPA-WMs](entities/jepa-wms.md) — FAIR (Terver et al.); first JEPA-for-robotics paper using RoboCasa. (1 source)
- [DINO-WM](entities/dino-wm.md) — NYU + FAIR; frozen DINOv2 features + learned predictor; zero-shot planning. (5 sources)
- [DINO-world](entities/dino-world.md) — FAIR DINOv2 video world model ("Back to the Features"). (1 source)
- [VLA-JEPA](entities/vla-jepa.md) — JEPA-as-auxiliary inside a VLA policy. (1 source)

### VLA models / generalist policies
- [NVIDIA GR00T](entities/nvidia-groot.md) — open VLA bundled with Isaac Lab. (3 sources)
- [OK-Robot](entities/ok-robot.md) — NYU zero-shot pick-and-drop framework; 58.5% in 10 homes; 1.8× over OVMM. (1 source)
- [Robot Utility Models](entities/robot-utility-models.md) — NYU/Meta zero-shot mobile-manipulation BC. (3 sources)
- [Dobb·E](entities/dobb-e.md) — NYU predecessor to RUM; HPR encoder + Stick-v1 + Homes of New York dataset. (1 source) _stub_

### Behavior-cloning methods
- [VQ-BeT](entities/vq-bet.md) — Vector-Quantized Behavior Transformer (Lee et al. 2024); top performer in RUM ablation. (1 source) _stub_
- [Diffusion Policy](entities/diffusion-policy.md) — Chi et al. 2023, Columbia/TRI/MIT; introduced/popularized PushT + UMI gripper. (1 source) _stub_

### LLMs
- [Qwen](entities/qwen.md) — Alibaba's open-weights LLM family. Default local LLM in both stretch_ai (3B) and ROSOrin (1.7B). (2 sources)

### Tools
- [Ollama](entities/ollama.md) — local LLM runtime (used by ROSOrin offline curriculum). (1 source) _stub_
- [MimicGen](entities/mimicgen.md) — synthetic-demo expansion tool used by RoboCasa365. (1 source) _stub_

### People
- [Yann LeCun](entities/yann-lecun.md) — NYU; Turing Award 2018; architect of the JEPA program; reported founder of AMI Labs (Apr 2026, provisional). (7 sources)
- [Navid Azizan](entities/navid-azizan.md) — MIT ME / IDSS / LIDS; learning-based control; SD-LQR (ICML 2023) + drone adaptive control (2025). (2 sources)
- [Adrien Bardes](entities/adrien-bardes.md) — FAIR researcher; co-senior on V-JEPA 2, V-JEPA 2.1, JEPA-WMs. The FAIR-side champion of the V-JEPA program. (3 sources)
- [Basile Terver](entities/basile-terver.md) — researcher (FAIR-affiliated, inferred); bread-crumb across DINO-world → JEPA-WMs lineage. (2 sources)
- [Sergey Levine](entities/sergey-levine.md) — UC Berkeley EECS; senior on DROID + Metaworld. (0 source pages yet — referenced via entity pages)
- [Chelsea Finn](entities/chelsea-finn.md) — Stanford CS; senior on DROID + Metaworld. (0 source pages yet — referenced via entity pages)
- [Lerrel Pinto](entities/lerrel-pinto.md) — NYU CS; co-senior on DINO-WM, RUM, and OK-Robot. (2 sources)
- [Yuke Zhu](entities/yuke-zhu.md) — UT Austin / NVIDIA Research; senior on RoboCasa365. (0 sources)
- [Karl Pertsch](entities/karl-pertsch.md) — DROID co-lead with Khazatsky; Berkeley/Stanford. (0 source pages yet — referenced via entity pages)
- [Mahi Shafiullah](entities/mahi-shafiullah.md) — NYU + Hello Robot; lead/co-author on Dobb·E, RUM, and OK-Robot. (2 sources)
- [Phil Shiu](entities/phil-shiu.md) — UC Berkeley → Eon Systems; lead author + maintainer of the FlyWire-based LIF brain simulation. (2 sources)

## Concepts
- [World model](concepts/world-model.md) — umbrella concept: learned predictive model of environment dynamics (generative-video / JEPA / frozen-feature / model-based-RL). (8 sources)
- [VLA models](concepts/vla-models.md) — vision-language-action robot foundation models. (8 sources)
- [Sim-to-real transfer](concepts/sim-to-real-transfer.md) — bridging simulator-trained policies to real robots. (8 sources)
- [World-model simulators](concepts/world-model-simulators.md) — narrower companion to [World model](concepts/world-model.md): world-models-used-as-simulators (generative-video and JEPA paradigms). (9 sources)
- [Joint-Embedding Predictive Architecture](concepts/jepa.md) — predict next-state representations, not pixels. (7 sources)
- [Imitation learning](concepts/imitation-learning.md) — supervised learning from demonstrations. (7 sources)
- [AI safety and alignment](concepts/ai-safety-alignment.md) — corrigibility, broadly safe behaviors, hard constraints, catastrophic risk framing; connects to agentic robot deployments. (2 sources)
- [Corrigibility](concepts/corrigibility.md) — the corrigibility dial (fully corrigible ↔ fully autonomous); asymmetric cost argument; galaxy-brained reasoning risk; agentic deployment implications. (1 source)
- [LLM-agent architecture](concepts/llm-agent-architecture.md) — LLM-emits-tool-calls control pattern; MCP and A2A as inter-agent/tool-access protocols. (5 sources)
- [AprilTags](concepts/apriltags.md) — visual fiducial markers for 6-DOF pose estimation; standard in FRC and research robotics. (2 sources)
- [Learned latent space](concepts/latent-space.md) — vector space where a trained encoder represents inputs; substrate for JEPA prediction, DINOv2 features, VQ-BeT codebook. (7 sources)
- [Agentic UAVs](concepts/agentic-uavs.md) — autonomous aerial systems with goal-driven behavior; 4-layer architecture; 8 domains; adaptive control. (2 sources)
- [Assistive robotics](concepts/assistive-robotics.md) — robots helping disabled/elderly users regain autonomy; Stretch, RELab tenoexo, social robots. (4 sources)
- [Biomechanical simulation](concepts/biomechanical-simulation.md) — physics-based simulation of an animal body; lineage *C. elegans* → Hydra → virtual rodent → NeuroMechFly v1/v2 → flybody. (5 sources)
- [Connectome](concepts/connectome.md) — complete wiring diagram of a nervous system; *C. elegans* → fly hemibrain → FlyWire → mouse → human. (3 sources)

## Syntheses
- [Simulators for agentic robotics — 2026 landscape](syntheses/simulators-for-agentic-robotics-2026.md) — full landscape survey, 6 categories. (updated 2026-05-07)
- [LLM-agent architecture across stacks](syntheses/llm-agent-architecture-across-stacks.md) — three-way comparison of stretch_ai, ROSOrin, OpenClaw. (2026-05-07)
- [Generative-video vs JEPA world models](syntheses/generative-video-vs-jepa-world-models.md) — what each predicts, costs, and demonstrates. (2026-05-07)
- [Newton + OpenUSD — the substrate convergence](syntheses/newton-openusd-substrate-convergence.md) — vendor-neutral physics + scene format across Isaac Lab and MuJoCo Playground. (2026-05-07)
- [Sim-heavy vs real-data paths to generalist policies](syntheses/sim-heavy-vs-real-data-paths.md) — three-path comparison: synthetic teleop, real demos, observation pretraining. (2026-05-07)
- [LeWorldModel — train and run howto](syntheses/leworldmodel-howto.md) — install, train, and evaluate LeWM on a single GPU. (2026-05-07)
- [OpenUSD support across simulators](syntheses/openusd-support-across-simulators.md) — catalog of which simulators consume USD, how, and which are exceptions. (2026-05-07)
- [Why JEPA research skips the simulator stack](syntheses/why-jepa-research-skips-the-simulator-stack.md) — JEPA literature fragments across sim weight classes (none / light / mid / heavy). Major revision after 5 new ingests. (updated 2026-05-07)
- [JEPA task capabilities](syntheses/jepa-task-capabilities.md) — reference index of seven task categories JEPA models demonstrate, mapped per-paper. (2026-05-08)
- [LeWM on ROSOrin Pro — feasibility analysis](syntheses/lewm-on-rosorin-pro-feasibility.md) — what's missing to deploy LeWM on Hiwonder ROSOrin Pro; realistic path; risks. (2026-05-08)
- [LeWM on Stretch — feasibility analysis](syntheses/lewm-on-stretch-feasibility.md) — companion: Stretch resolves the teleop-data blocker via RUM's open dataset; concrete LeWM-vs-RUM-BC experiment design. (2026-05-08)
- [Robot platforms — comparison](syntheses/robot-platforms-comparison.md) — at-a-glance table of every robot entity in the wiki by tier / type / use; flags missing humanoids + cross-tier transfer gap. (2026-05-08)
- [Humanoid platforms survey](syntheses/humanoid-platforms-survey.md) — companion to robot-platforms-comparison focused on humanoids; 10 entities listed by tier; AI-strategy archetypes + price stratification. (2026-05-08)
- [Household robot decision — Stretch vs Unitree G1](syntheses/household-robot-decision-stretch-vs-g1.md) — buying-decision comparison for navigate + floor pickup + dishes + cans use case. Recommends Stretch. (2026-05-08)
- [JEPA project ladder for ROSOrin Pro](syntheses/jepa-project-ladder-rosorin-pro.md) — six-rung educational/research project ladder for learning JEPA on ROSOrin Pro hardware. (2026-05-08)
- [LeWM hello world — Project 1 detailed scope](syntheses/lewm-hello-world-project-scope.md) — phase-by-phase plan for reproducing LeWM PushT, training from scratch, one-knob ablation. (2026-05-08)
- [FRC simulation & AI landscape](syntheses/frc-simulation-and-ai-landscape.md) — what simulation programs FRC teams use for autonomous dev and AI training; three-tier analysis (trajectory planners / physics sims / ML frontier); Team 254 presentation deep-dive. (updated 2026-05-08)
- [Whole-organism agentic AI](syntheses/whole-organism-agentic-ai.md) — brain (FlyWire connectome + LIF dynamics) + body (flybody MuJoCo) for *Drosophila*; first plausible end-to-end animal-scale agent; contrasts with robotics-flavoured agentic AI. (2026-05-08)
- [Assistive robotics — R&D landscape and JEPA applicability](syntheses/assistive-robotics-research-landscape.md) — seven blocking problems, timeline table, active researchers (wiki + beyond), four independent-researcher actions, JEPA applicability analysis. (2026-05-09)

### JEPA-related concepts/entities/sources to potentially expand
- Metaworld — referenced by [JEPA-WMs](sources/jepa-wms-paper.md) (42 tasks); deserves an entity page.
- LIBERO / LIBERO-Plus — referenced by [VLA-JEPA](sources/vla-jepa-paper.md); benchmark concept/source pages.
- SimplerEnv — referenced by [VLA-JEPA](sources/vla-jepa-paper.md); mid-weight Sapien-adjacent simulator.
- `stable-worldmodel` package — env zoo broader than [LeWM howto](syntheses/leworldmodel-howto.md) exposed; verify and update.
- PLDM — comparison baseline for LeWM; needs primary-source ingest.
- DreamerV3, TD-MPC — also referenced as JEPA baselines.

## Known gaps / TBD
- ABB / FANUC / KUKA / Yaskawa industrial-OEM Isaac-Sim adoption (referenced from a GTC 2026 search snippet; needs a primary-source ingest to file properly)
- URDF, MJCF, SDFormat — entity / concept pages; currently referenced as bare text from the OpenUSD discussion
- MjcPhysics USD plugin — could become its own entity if it accumulates more references
- newton-usd-schemas repo — could become its own entity if it accumulates more references
- Engineering.com CAD-to-USD article — 403'd on fetch; revisit with a different access path
- Drake (TRI/MIT) entity page
- Gazebo (the simulator itself) — referenced by both Hello Robot and Hiwonder docs; deserves its own entity page distinct from MuJoCo Playground
- Webots, CoppeliaSim, PyBullet entity pages (low priority — not agentic-robotics center of gravity)
- Skild AI entity + approach
- RoboMimic benchmark concept/source pages ([LIBERO](entities/libero.md) now filed)
- TRI LBM (Toyota Research Institute Large Behavior Model) — referenced in RoboCasa365 paper as baseline
- Octo — referenced in RoboCasa365 paper as baseline
- Stretch Mujoco — Hello Robot's MuJoCo wrapper; thin or substantive?
- Dreamer/DreamerV3, TD-MPC, PLDM — world-model baselines referenced in LeWorldModel paper ([DINO-WM](entities/dino-wm.md) now filed)
- DROID paper itself (arxiv 2403.12945), Metaworld paper (arxiv 1910.10897), DINOv2 paper (arxiv 2304.07193), Dobb·E paper (arxiv 2306.16650), VQ-BeT paper (Lee et al. 2024), Diffusion Policy paper (arxiv 2303.04137), IBC paper (Florence et al. 2021, PushT origin) — entity pages exist but the papers themselves are not yet source pages; would let us cite design rationale directly
- StepFun — Chinese multimodal AI provider used by ROSOrin's Chinese-language fallback
- sherpa-onnx — offline ASR + TTS toolkit used by ROSOrin
- WonderEcho Pro — Hiwonder voice module accessory
- Hiwonder vision/CV chapter (YOLOv11 + TensorRT) — could warrant its own concept/source page on a deeper ingest
- HX-12H bus servo, COIN-D6 LiDAR, Deptrum Aurora930 depth camera, MPU6050 IMU — hardware-component pages on demand
- People pages (low priority remaining): Aaron Edsinger, Mahmoud Assran, Alexander Khazatsky, Pulkit Agrawal, Pieter Abbeel, Cheng Chi, Seungjae Lee — surfacing from DROID + RUM + V-JEPA + RUM-paper ingest. ([Yann LeCun](entities/yann-lecun.md), [Adrien Bardes](entities/adrien-bardes.md), [Basile Terver](entities/basile-terver.md), [Sergey Levine](entities/sergey-levine.md), [Chelsea Finn](entities/chelsea-finn.md), [Lerrel Pinto](entities/lerrel-pinto.md), [Yuke Zhu](entities/yuke-zhu.md), [Karl Pertsch](entities/karl-pertsch.md), [Mahi Shafiullah](entities/mahi-shafiullah.md) now filed.)
- Farama projects not ingested as standalone pages: Minari (offline RL dataset standard), Shimmy (DM Control / OpenSpiel bridge), MO-Gymnasium, MOMAland, MAgent2, MPE2, Minigrid, MiniWoB++, ViZDoom, HighwayEnv, Procgen2, Stable-Retro, Jumpy — listed in [Farama Foundation Projects Page](sources/farama-projects-page.md); promote to entity pages if they show up in a robotics paper. ([Metaworld](entities/metaworld.md) and [ALE](entities/ale.md) now filed.)
- Gymnasium-Robotics env families not ingested as standalone pages: Fetch, Shadow Hand, Maze (Ant/Point), Adroit (Door/Hammer/Pen/Relocate — staple in D4RL offline RL eval), Franka Kitchen (multi-task kitchen), MaMuJoCo (multi-agent locomotion). Promote when referenced.
- Humanoids not yet filed: AGIBOT humanoid hardware (A2/X1/X2 — [company](entities/agibot.md) is filed), Fourier GR-1/GR-2, LimX CL-2/CL-3, Booster T1, EngineAI PM01 (Chinese affordable). PAL TIAGo/TALOS, Pepper, Robotis OP3/DARwIn-MINI, Sanctuary Phoenix, Kawasaki Kaleido, AIST HRP-5P, Toyota T-HR3 (research / educational). See [humanoid-platforms-survey](syntheses/humanoid-platforms-survey.md) for landscape context.

---

[Log](log.md) — chronological record of ingests, queries, and lint passes.
- Boston Dynamics Spot — quadruped reference platform; no entity page ([Atlas](entities/atlas.md) is filed).
- Maple-Sim — Shenzhen Robotics Alliance's dyn4j-based FRC physics simulator; most active FRC sim project. Entity page on demand.
- xRC Simulator — standalone Unity-based FRC driving/strategy simulator. Entity page on demand.
- WPILib — open-source FRC software framework. Core to the entire FRC software ecosystem. Deserves entity page.
- PhotonVision / Limelight — FRC vision processing solutions for AprilTag detection. Entity pages on demand.
- Chief Delphi — FRC community forum; primary knowledge-sharing platform. Entity page on demand.
- ~~Team 254~~ — now filed as [Team 254: The Cheesy Poofs](entities/team-254.md).
- MathWorks / MATLAB — FRC sponsor; provides MATLAB + Simulink for autonomous algorithm design. Entity page on demand.
- Mi et al. 2022 (ICLR) connectome-constrained latent-variable model — still referenced via [Connectome](concepts/connectome.md) and [flybody Paper](sources/flybody-paper.md) only; not yet a primary-source page. ([Shiu et al. 2024](sources/shiu-fly-brain-paper.md) and [Lappalainen et al. 2024](sources/lappalainen-flyvis-paper.md) now filed.)
- Brian 2 spiking-NN simulator — substrate under [Shiu et al. 2024](sources/shiu-fly-brain-paper.md); entity page on demand. ([flyvis](entities/flyvis.md) and [Drosophila brain model](entities/drosophila-brain-model.md) now filed.)
- Yuval Tassa, Srinivas Turaga (now senior on two ingested sources), Josh Merel, Janne Lappalainen, Kristin Scott, Jakob Macke — entity pages on demand. ([Phil Shiu](entities/phil-shiu.md) now filed.)
- Virtual rodent (Merel et al. 2020, ICLR) — direct DeepMind ancestor of [flybody](entities/flybody.md); entity page on demand.
- *C. elegans* / Hydra body sims (Boyle 2012, Wang 2023) — earlier whole-organism biomechanics; one-line references in flybody-paper.
