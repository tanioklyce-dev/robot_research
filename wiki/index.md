# Index

## Highlights

Curated entry points across the wiki.

**Curriculum / learning path**
- [Robot-learning curriculum — from neurons to LeWorldModel](syntheses/robot-learning-curriculum.md) — 14-module bottom-up syllabus, **all modules drafted**; PushT as the connecting thread; ends with a Stretch-platform capstone.
- [Curriculum Module 1 — Neural networks and training](syntheses/curriculum-01-neural-networks.md) — Tier 1. Neurons, MLP, forward pass + backprop, MSE/CE, SGD/Adam, regularization, BN/LN, residuals, depth. Brisk-but-rigorous refresher.
- [Curriculum Module 2 — CNNs and visual representation learning](syntheses/curriculum-02-cnns.md) — Tier 1. Convolution, pooling, receptive field, ResNet skip connections, ImageNet pretraining + fine-tuning, "visual encoder" abstraction. ResNet-18 as the BC-line default.
- [Curriculum Module 3 — Sequence models, attention, and transformers](syntheses/curriculum-03-attention-and-transformers.md) — Tier 1. Attention, self-attention, multi-head, transformer blocks, positional encoding, causal masking, ViT (patches + [CLS]). Encoder-only / decoder-only / encoder-decoder.
- [Curriculum Module 4 — Self-supervised learning and embeddings](syntheses/curriculum-04-self-supervised-learning.md) — Tier 1. SSL taxonomy (contrastive vs predictive); representation collapse as first-order failure mode; five anti-collapse families (EMA + stop-grad, VICReg, frozen encoder, multi-fix soup, SIGReg). Sets up Module 11.
- [Curriculum Module 5 — Generative modeling fundamentals (DDPM, full math)](syntheses/curriculum-05-generative-models.md) — Tier 2. Full ELBO → `L_simple` derivation; KL bounds; ε-parameterization; noise schedules; DDIM sampling; classifier-free guidance derivation; bridges to Diffusion Policy, π0 flow matching, and generative-video WMs.
- [Curriculum Module 6 — Imitation learning and behavior cloning](syntheses/curriculum-06-imitation-learning.md) — IL/BC frame, multi-modality + distribution-shift failure modes, PushT setup; anchor exercise = train vanilla MSE-MLP BC and watch it fail.
- [Curriculum Module 7 — BC lineage on PushT (IBC → BeT → DP)](syntheses/curriculum-07-bc-lineage-pusht.md) — direct successor to Module 6; the policy-learning side of the LeWM ablation table.
- [Curriculum Module 8 — Reinforcement learning vocabulary](syntheses/curriculum-08-rl-vocabulary.md) — light, vocabulary-only RL coverage (MDP, return, value, policy, REINFORCE → PPO, DQN, MFRL vs MBRL, Dreamer-class latent imagination). Just enough to read the LeWM baseline columns.
- [Curriculum Module 9 — Vision-Language-Action models](syntheses/curriculum-09-vla.md) — VLA = VLM + action head; major instances (GR00T, π0, Helix, Gemini Robotics, OpenVLA); action-head design (AR tokens / flow matching / DDPM); System 1 / System 2 pattern; VLA-JEPA cross-over.
- [Curriculum Module 10 — World models, broad](syntheses/curriculum-10-world-models.md) — four-family WM taxonomy (generative-video / JEPA / frozen-feature / MBRL); MPC + CEM + gradient-based planning; horizon vs compounding error; bridge to LeWM.
- [Curriculum Module 11 — JEPA in depth](syntheses/curriculum-11-jepa-deep.md) — joint-embedding architectural commitment; V-JEPA 1→2→2-AC→2.1 progression; the six-family collapse-prevention zoo (EMA/stop-grad, VICReg, frozen encoder, multi-fix soup, SIGReg); DINO-WM vs end-to-end JEPA; JEPA-WMs real-Franka.
- [Curriculum Module 12 — LeWorldModel deep-dive (with full SIGReg math)](syntheses/curriculum-12-lewm-deep-dive.md) — **the curriculum's destination**. LeWM section by section; full SIGReg derivation (Cramér–Wold + Epps–Pulley + backprop through the test statistic); two-loss architecture; CEM-MPC planning; four-environment results; latent probing + violation-of-expectation; the BN-after-CLS engineering trick.
- [Curriculum Module 13 — Home robotics deployment reality](syntheses/curriculum-13-home-robotics-deployment.md) — the deployment-reality module. 89.4% / 12.4% RLBench-vs-BEHAVIOR-1K gap; Stretch as de-facto platform; RUM + OK-Robot as the strongest current home-robotics results; PAR + EUP + autonomy-preference framing; underserved domains; where LeWM-class fits and doesn't.
- [Curriculum Module 14 — Capstone (paper-first, hardware-second)](syntheses/curriculum-14-capstone.md) — the capstone. Phase A (paper/sim, required): reproduce LeWM PushT + 5–10 page experiment-design memo. Phase B (Stretch hardware, gated): execute the memo with a Diffusion Policy baseline.
- [Glossary](glossary.md) — flat acronym + term reference (BC, VLM, CNN, SSL, MPC, MSE, LSTM, SIGReg, …); cross-linked from every curriculum module.

**AI Safety and Alignment**
- [Claude's Constitution](sources/claudes-constitution.md) — Anthropic's primary specification for Claude's values, corrigibility model, principal hierarchy, and hard constraints.
- [AI safety and alignment](concepts/ai-safety-alignment.md) — concept overview; connects to agentic robot deployments.
- [Corrigibility](concepts/corrigibility.md) — the corrigibility dial, asymmetric cost argument, galaxy-brained reasoning risk.
- [Apollo Research](entities/apollo-research.md) — independent safety evaluation institute; red-teamed Claude Opus 4.

**Assistive Robotics**
- [Assistive robotics](concepts/assistive-robotics.md) — concept overview; sim-to-real gap quantified (89.4% RLBench vs 12.4% BEHAVIOR-1K household tasks).
- [Accessible robot communication](concepts/accessible-robot-communication.md) — output-interface side of HRI for non-visual users; mixed-initiative narration preferred by blind users.
- [Assistive robotics — R&D landscape](syntheses/assistive-robotics-research-landscape.md) — seven blocking problems, timeline, active researchers, independent-researcher paths, JEPA fit.
- [Levels of autonomy in assistive robotics](syntheses/levels-of-autonomy-in-assistive-robotics.md) — three orthogonal autonomy axes; EUP preserves agency; variable-LoC design pattern.
- [Long-term in-home robot deployments](syntheses/long-term-in-home-robot-deployments.md) — what the longitudinal record actually shows (Henry Evans summers + Nanavati 2025 + RUM/OK-Robot breadth).
- [Stretch as the de-facto assistive-robotics platform](syntheses/stretch-as-assistive-platform.md) — why every wiki-relevant in-home deployment converged on Stretch.
- [Underserved PAR domains — dressing, bathing, medication](syntheses/underserved-par-domains.md) — what blocks each, realistic researcher targets.
- [OK-Robot](entities/ok-robot.md) — zero-shot pick-and-drop in 10 homes; 58.5% success; state-of-the-art household manipulation.
- [Robot Utility Models](entities/robot-utility-models.md) — NYU/Meta zero-shot BC; data diversity > data quantity insight.
- [Stanford HAI — AI Index Report 2026](sources/stanford-hai-ai-index-2026.md) — 89.4% vs 12.4% gap; humanoid landscape; Physical AI assessment.
- [DRAGON (Liu et al. 2024)](sources/dragon-assistive-nav-2024.md) — TurtleBot guide robot for visually impaired users; CLIP-grounded landmark recognition + dialogue.
- [Designing Accessible Robot Communication for Blind People (Huh et al. 2026)](sources/huh2026-accessible-robot-comm.md) — 6 DGs; mixed-initiative narration; observational + controlled study (10+20+20).

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
- [HCR Lab Publications](sources/hcrlab-publications.md) — Human-Centered Robotics Lab (UW) full publication record 2016–2025; autonomy preference finding; Henry Evans Stretch deployments; EUP transferred to Stretch SE2. (2025)
- [Maya Cakmak — Research Overview](sources/maya-cakmak-research.md) — personal research narrative; stated goal quote; WHO statistic; HRI 2020 finding; Henry Evans summer deployment details; EUP rationale. (Unknown, continuously updated)
- [Physically Assistive Robots — Systematic Review](sources/nanavati2024-physically-assistive-robots-review.md) — PRISMA review; 1,981 screened, 87 included; three themes; dressing/bathing/medication underserved; half of PAR papers involve no PwD. (*Annual Review*, 2024)
- [Sense of Agency — Yang et al. 2025](sources/yang2025-sense-of-agency.md) — EUP robots preserve sense of agency even when acting autonomously; high-risk tasks drive preference for control. (RO-MAN 2025)
- [Feeding System Out-of-lab — Nanavati et al. 2025](sources/nanavati2025-feeding-out-of-lab.md) — open-source Kinova JACO feeding system; CBPR co-design; 3 lessons from out-of-lab deployment; HRI 2025 Best Systems Paper Finalist. (2025)
- [Multiple Ways of Working with Users — Nanavati et al. 2024](sources/nanavati2024-multiple-ways-par.md) — methodology for PwD inclusion in PAR research; 3 projects; participatory + empowerment design. (A3DE @ HRI 2024)
- [DRAGON — Dialogue-Based Robot for Assistive Navigation (Liu et al. 2024)](sources/dragon-assistive-nav-2024.md) — UIUC/Driggs-Campbell; TurtleBot 2i + CLIP landmark grounding + dialogue + VQA for persons with visual impairments. (IEEE RA-L 2024)
- [Designing Accessible Robot Communication for Blind People (Huh et al. 2026)](sources/huh2026-accessible-robot-comm.md) — Berkeley × UT Austin × UW; Franka + Tiago observational study (10 blind) + Gemini-Live controlled study (20 blind + 20 sighted); 6 design guidelines; mixed-initiative narration is preferred by blind users. (CHI 2026 InterAI Workshop)
- [Domestic Robots and the Dream of Automation (Schneiders et al. 2021)](sources/schneiders2021-domestic-robots-automation.md) — Aalborg; 24 Danish households; task fragmentation finding; strict task division contradicts Forlizzi 2007. (CHI 2021)
- [XLeRobot Documentation](sources/xlerobot-docs.md) — $660 dual-arm mobile manipulator; 2× SO-ARM101 on LeKiwi-class base; 90% 3D-printed; built on LeRobot. (v0.3.0, 2025-08-30)
- [Seeed Studio LeRobot LeKiwi Wiki](sources/seeed-lekiwi-wiki.md) — end-to-end build/use tutorial; 11-step assembly; ACT-policy training pipeline; Seeed distributes the hardware. (2025-06)
- [LeKiwi GitHub (SIGRobotics-UIUC/LeKiwi)](sources/lekiwi-github.md) — 1,300+ stars; 3-wheel Kiwi-drive base; SO-ARM101 default arm; Dynamixel/Koch v1.1 alt; Apache 2.0. (2025)
- [LeRobot Worldwide Hackathon 2025 — All Winners](sources/lerobot-worldwide-hackathon-2025-winners.md) — HF Space with 30 ranked teams; June 14–15, 2025; 916 team members, ~400 submissions; LeKiwi/SO-101/Hope Jr Arm prizes. (2025-06)
- [Seeed × NVIDIA × HF Embodied AI Hackathon 2025 Recap](sources/seeed-embodied-ai-hackathon-2025-recap.md) — two-site (Shenzhen + Mountain View) October 2025 hackathon; 700+ devs, 30+ teams; both site champions ran GR00T N1.5 on XLeRobot / SO-ARM101; theme = home + cooking robots. (2025-11-06)
- [SIGRobotics (ACM @ UIUC) — Projects page](sources/sigrobotics-uiuc-projects-page.md) — institutional landing page; 4 flagship projects (LeKiwi, Koch arms, Mini Humanoid sponsored by K-Scale Labs, TB3 coffee bot); 7 sponsors; ~25 additional repos visible in GitHub org. (rolling)
- [Explicit-Input Teleoperation — Walker et al. 2024](sources/walker2024-explicit-input-teleoperation.md) — pointing-based explicit assistance vs. implicit inference; fewer failures, lower workload; NVIDIA collaboration. (IROS 2024)
- [Grasping in Clutter IVFP — Murray et al. 2024](sources/murray2024-grasping-clutter-ivfp.md) — IVFP on Stretch RE1 in warehouse; pre-emptive failure detection; autonomous reward assignment. (2024)
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
- [Tools for Your To Do List with Spot and Gemini Robotics (Boston Dynamics blog)](sources/bostondynamics-spot-gemini-robotics.md) — Spot + Gemini Robotics-ER 1.5 hackathon: tool-call layer over the Spot SDK; AIVI-Learning (ER 1.6) productization. (2025)
- [Diffusion Policy Paper](sources/diffusion-policy-paper.md) — Chi et al., Columbia / TRI / MIT (RSS 2023, arxiv 2303.04137); conditional DDPM over actions; 46.9% avg improvement across 12 tasks; UR5 + Franka real-world (Push-T 95%, mug flip 90%, sauce pouring 79%, sauce spreading 100%). (2023-03)
- [DDPM Paper](sources/ddpm-paper.md) — Ho, Jain, Abbeel; UC Berkeley (NeurIPS 2020, arxiv 2006.11239); foundational diffusion-model class; CIFAR-10 FID 3.17. (2020-06)
- [IBC Paper](sources/ibc-paper.md) — Florence et al., Google Research (CoRL 2021, arxiv 2109.00137); implicit-BC via energy-based models; introduced PushT benchmark; ancestor of Diffusion Policy. (2021-09)
- [BET Paper](sources/bet-paper.md) — Shafiullah, Cui, Altanzaya, Pinto; NYU (NeurIPS 2022, arxiv 2206.11251); transformer + k-means action discretization; ancestor of VQ-BeT. (2022-06)
- [UMI Project Page](sources/umi-paper.md) — Chi et al.; Stanford / Columbia / TRI (RSS 2024 Best Systems Finalist, arxiv 2402.10329); hand-held gripper data collection; 111 demos/hr; zero-shot UR5e + Franka transfer. (2024-02)
- [TRI Website](sources/tri-website.md) — Toyota Research Institute homepage; mission + 5 research areas; co-affiliation hub for Diffusion Policy + UMI; home of TRI LBM. (continuously updated)
- [DreamerV3 Paper](sources/dreamer-v3-paper.md) — Hafner, Pasukonis, Ba, Lillicrap (arxiv 2301.04104); single-config MBRL across 150+ tasks; first to mine Minecraft diamonds without human data/curricula. Abstract-level ingest. (2023-01)
- [TD-MPC2 Paper](sources/td-mpc2-paper.md) — Hansen, Su, Wang (ICLR 2024, arxiv 2310.16828); decoder-free latent WM + MPC + TD-bootstrapped value; 104 tasks / 4 domains / 317M-param multi-task agent. Abstract-level ingest. (2023-10)
- [π0 Paper](sources/pi-zero-paper.md) — Black, Brown, Driess et al., Physical Intelligence (arxiv 2410.24164); VLA flow-matching model on a pre-trained VLM backbone; cross-platform (single-arm, dual-arm, mobile manipulator); laundry folding + table cleaning + box assembly. Abstract-level ingest. (2024-10)
- [Helix (Figure AI blog)](sources/helix-blog.md) — Figure AI; hierarchical S1/S2 VLA on Figure 02 humanoid (7B VLM @ 7–9 Hz + 80M transformer @ 200 Hz, end-to-end); ~500h teleop; onboard inference. Vendor blog only. (2025-02)
- [PLDM Paper](sources/pldm-paper.md) — Sobal, Zhang, Cho, Balestriero, Rudner, LeCun (NYU + FAIR; WRL @ ICLR 2025); end-to-end JEPA WM trained with VICReg + inverse-dynamics + similarity loss (~6 anti-collapse hyperparameters); the canonical "end-to-end JEPA before LeWM" baseline. Stress-tested on 23 datasets / 6 generalization properties; only method that doesn't completely fail in any setting. (2025-02-28)
- [Sobal et al. 2022 — JEPA slow features](sources/sobal2022-jepa-slow-features-paper.md) — Sobal, Jyothir S V, Jalagam, Carion, Cho, LeCun (NYU + FAIR; NeurIPS 2022 SSL workshop, arxiv 2211.10831); the PLDM precursor. Establishes that JEPA representations preferentially encode slowly-varying features (like the position of a moving dot); fixed-distractor noise breaks this bias. (2022-11-20)
- [LeJEPA Paper](sources/lejepa-paper.md) — Balestriero & LeCun (Brown + NYU/FAIR, arxiv 2511.08544); the foundational SIGReg paper. Proves isotropic Gaussian is optimal for JEPA embeddings; proposes Sketched Isotropic Gaussian Regularization (SIGReg). Single hyperparameter, no stop-gradient, no teacher-student. ImageNet-1k linear-eval 79% on ViT-H/14; 10+ datasets / 60+ architectures. The methodological precursor to LeWM. (2025-11-11)
- [Welch Labs — Yann LeCun's $1B Bet Against LLMs (video)](sources/welchlabs-lecun-1b-bet-against-llms.md) — 37-min popular-explainer with LeCun interview clips; arc from blurry generative video → Siamese → Barlow Twins → DINO → JEPA / world models; recommended curriculum-orientation video. (2026-05-01)
- [Onchain AI Garage — I Reproduced LeCun's JEPA World Model (video)](sources/onchain-ai-garage-lewm-reproduction.md) — 27-min walk-through reproducing LeWM on Two Room. RTX 3060 / 12 GB VRAM in WSL2, Claude Code as implementation assistant; **92% success vs paper's 97%** after 4 epochs / ~8 hours. First independent LeWM reproduction in the wiki; corroborates the four [LeWM howto](syntheses/leworldmodel-howto.md) gotchas. Linked from [Curriculum Module 12](syntheses/curriculum-12-lewm-deep-dive.md). (2026-04-24)
- [karpathy/autoresearch (GitHub repo)](sources/karpathy-autoresearch.md) — Karpathy's agent-driven LLM training research repo. Single GPU + simplified nanochat + 5-min experiment budget + an AI coding agent that edits `train.py`, runs the experiment, compares val_bpb, and keeps or reverts. Produced two nanochat speedrun-leaderboard improvements (2.02 → 1.65 hours wall-clock). First public evidence that an agent loop can produce measurable gains on a frontier ML training pipeline. Linked from the [LLM-agent architecture](concepts/llm-agent-architecture.md) concept as the non-robotics example of the LLM-emits-tool-calls pattern. (2026-03-06)
- [karpathy/nanochat (GitHub repo)](sources/karpathy-nanochat.md) — Karpathy's full end-to-end ChatGPT pipeline (tokenizer + pretrain + SFT + RL + chat UI) for ~$48 on an 8XH100 node. Single `--depth` complexity dial; "Time-to-GPT-2" speedrun leaderboard. Modern successor to [nanoGPT](sources/karpathy-nanogpt.md); the substrate [autoresearch](sources/karpathy-autoresearch.md) iterates on. Linked from [Curriculum Module 3](syntheses/curriculum-03-attention-and-transformers.md). (2025-10-13)
- [karpathy/nanoGPT (GitHub repo)](sources/karpathy-nanogpt.md) — Karpathy's minimal GPT training repo. Two ~300-line files: `model.py` (cleanest decoder-only-transformer reference implementation) + `train.py`. **Deprecated November 2025** in favor of [nanochat](sources/karpathy-nanochat.md), but `model.py` is still the wiki's recommended *architecture-reading* exit-ramp at the bottom of [Curriculum Module 3](syntheses/curriculum-03-attention-and-transformers.md). (2022-12-28)
- [karpathy/micrograd (GitHub repo)](sources/karpathy-micrograd.md) — Karpathy's tiny scalar-valued autograd engine (~100 lines) plus a ~50-line PyTorch-style NN library on top. The cleanest "I understand backprop" milestone. Linked from [Curriculum Module 1](syntheses/curriculum-01-neural-networks.md). (2020-04-13)
- [NVIDIA Brev Docs](sources/nvidia-brev-docs.md) — NVIDIA's cross-cloud GPU-instance broker (`brev` CLI + Launchables; B200 → P4 catalog). Lifecycle is `Running ⇄ Stopped → Deleted` with hourly billing while running, no compute fees while stopped (capacity-loss risk on restart), and **no native auto-stop / TTL / spend-cap** — `brev stop --all` is the only real cost lever. (2025–2026)

## Sources (pedagogical / curriculum companions, undated)
- [Welch Labs — The Perceptron (YouTube, Feb 2025)](sources/welchlabs-perceptron.md) — "ChatGPT is made from 100 million of these." Stephen Welch's pedagogical prequel to the [LeCun $1B Bet video](sources/welchlabs-lecun-1b-bet-against-llms.md): Rosenblatt 1957 → Mark I (1958) → XOR roadblock (Minsky & Papert 1969) → backprop (Rumelhart/Hinton/Williams 1986) → MLP-at-scale (GPT-3). Recommended-viewing for [Curriculum Module 1](syntheses/curriculum-01-neural-networks.md). (2025-02)
- [3Blue1Brown — How might LLMs store facts | Deep Learning Chapter 7](sources/3blue1brown-mlp-in-llms.md) — Grant Sanderson; the MLP / FFN block inside a transformer LLM as a key–value fact-lookup mechanism. Covers up/down projection, ReLU, superposition (Johnson–Lindenstrauss), and the "~2/3 of GPT-3's parameters live in MLPs" arithmetic. Foundation for the interpretability / SAE-feature-decomposition program. Recommended-viewing for [Curriculum Module 3](syntheses/curriculum-03-attention-and-transformers.md). (2024-08-31)
- [fast.ai — Practical Deep Learning for Coders 2022](sources/fastai-practical-deep-learning.md) — Jeremy Howard; 9-lesson, library-first PyTorch + fastai + Hugging Face Transformers + Gradio onboarding. Strongest "first-touch" pedagogical companion *before* [Curriculum Module 1](syntheses/curriculum-01-neural-networks.md) for readers without a year of DL programming. (2022)
- [Cameron R. Wolfe — Understanding and Using SFT for Language Models](sources/wolfe-sft-blog.md) — *Deep (Learning) Focus* Substack, Sep 2023. Three-stage alignment (Pretrain → SFT → RLHF); LIMA's "1,000 examples sufficient" finding; survey of LLaMA-2 / Falcon / MPT / Alpaca / Vicuna / Orca / WizardLM. The theory-side companion to [HF TRL SFT Trainer docs](sources/huggingface-trl-sft-trainer.md). (2023-09-11)
- [Hugging Face TRL — SFT Trainer documentation](sources/huggingface-trl-sft-trainer.md) — the de-facto SFT trainer for LLMs and VLMs in 2026. One-line API; dataset-format dispatch; chat-template auto-application; PEFT/LoRA, Liger Kernel, Unsloth, RapidFire AI integrations; VLM support (Qwen2.5-VL, LLaVA-Instruct-Mix); tool-calling SFT. The implementation companion every wiki-tracked VLA fine-tuning recipe builds on top of. (continuously updated)
- [DS4DS 7.01 — Optimal Control, Introduction (Peitz & Wallscheid)](sources/ds4ds-7-01-optimal-control-intro.md) — Data Science for Dynamical Systems open course (CC BY-SA 4.0; Julia / Jupyter), YouTube Jan 2024. Opening lecture of the 7-lesson module 7 (intro → discrete-time → LQR → LMPC → data-driven MPC via DMD → differential predictive control). The modern-pedagogy companion to [Sussmann & Willems 1997](sources/sussmann-willems-1997-300-years-optimal-control.md) — together they form a complete optimal-control orientation. (2024-01-21)

## Sources (foundational, out of chronological order)
- [Sussmann & Willems 1997 — 300 Years of Optimal Control: From the Brachystochrone to the Maximum Principle](sources/sussmann-willems-1997-300-years-optimal-control.md) — Rutgers / Groningen; IEEE Control Systems Magazine "Historical Perspectives," June 1997. Tercentenary essay arguing optimal control was born in 1697 with Bernoulli's brachystochrone solution — not in 1956 with Pontryagin. Distinguishes OC ⊋ CoV: dynamical constraints `q̇ = f(q, u, t)` + control-set constraints `u ∈ U` are the structural additions. Walks the canonical chain Bernoulli → Euler–Lagrange → Hamilton → Jacobi → Weierstrass → Pontryagin's Maximum Principle. The wiki's primary-source anchor for the optimal-control machinery underneath MPC / CEM / TD-MPC / learned-world-model planning. (1997-06)
- [Barlow 1961 — Possible Principles Underlying the Transformations of Sensory Messages](sources/barlow1961-sensory-messages.md) — Horace Barlow's foundational neuroscience paper introducing the redundancy-reduction principle (recode redundant sensory input into a factorial code with statistically independent components). Eponymous source for Barlow Twins (2021). The lineage root for VICReg → SIGReg → DINOv3 Gram anchoring. (1961)
- [Bromley, Guyon, LeCun, Säckinger, Shah 1993 — Signature Verification using a "Siamese" Time Delay Neural Network](sources/bromley1993-siamese-signature-verification.md) — original Siamese network paper, AT&T Bell Labs / NIPS 1993. Two weight-tied TDNN sub-networks + cosine + `±1` targets for genuine vs forgery pairs. The architectural ancestor of every joint-embedding SSL system: Barlow Twins, VICReg, DINOv2/v3, and the J/A in [JEPA](concepts/jepa.md). LeCun's 1990s precursor to his 2020s JEPA program — same author, same architectural family, different loss. (1993)
- [Vaswani et al. 2017 — Attention Is All You Need](sources/attention-is-all-you-need.md) — the Transformer paper. NeurIPS 2017; Google Brain / Google Research. Sequence transduction built entirely on attention, no recurrence, no convolution. Encoder–decoder, multi-head scaled dot-product attention, sinusoidal positional encoding, `h=8`, `d_model=512`, `N=6`. 28.4 BLEU EN-DE / 41.8 BLEU EN-FR. The foundation of every modern architecture downstream: LLMs, ViTs, VLA action heads, JEPA predictors, BeT / VQ-BeT policies, Diffusion Policy transformer backbones. (2017-06-12)
- [Dosovitskiy et al. 2020 — An Image Is Worth 16x16 Words (ViT)](sources/vit-paper.md) — the Vision Transformer paper. ICLR 2021; Google Research, Brain Team. Patch tokenization + learned positional embedding + `[CLS]` token + standard transformer encoder = first pure-attention vision model. Pre-trained on JFT-300M, ViT-H/14 hits 88.55% ImageNet top-1 at 2–4× less compute than BiT-L / Noisy Student. Central claim: **at scale, data trumps inductive bias.** The backbone underneath every ViT-encoder in this wiki — DINOv2, DINOv3, V-JEPA 2, LeWM, DINO-WM, DINO-world, JEPA-WMs, LeJEPA, PLDM. (2020-10-22)
- [Sutton & Barto — Reinforcement Learning: An Introduction (2nd ed., MIT Press 2018 / 2020 reprint)](sources/sutton-barto-rl-textbook.md) — UMass / UAlberta / DeepMind; A Bradford / MIT Press; ISBN 9780262039246; CC BY-NC-ND 2.0 electronic. The canonical RL textbook (548 pp). Defines the field's four-subelement decomposition (policy / reward / value function / model) and the unifying narrative MC ↔ TD ↔ DP via Bellman bootstrapping. **Ch 13 (Policy Gradient Methods)** is the lineage of REINFORCE → Actor-Critic → PPO / SAC / GRPO. **Ch 16 (Applications)** covers DQN/Atari (Mnih 2015) + AlphaGo/AlphaGo Zero (Silver 2016/2017). **Ch 11 (Deadly Triad)** is the cleanest theoretical diagnosis of why deep-RL training is fragile. The primary-source anchor for [Module 8 — RL vocabulary](syntheses/curriculum-08-rl-vocabulary.md), every MBRL paper ([DreamerV3](sources/dreamer-v3-paper.md), [TD-MPC2](sources/td-mpc2-paper.md)), every learned-WM thread, and the RLHF/DPO/GRPO line underneath every VLA. The "RL = approximate optimal control under uncertainty" bridge to [Sussmann & Willems 1997](sources/sussmann-willems-1997-300-years-optimal-control.md). Sutton + Barto won the 2024 Turing Award for the work consolidated in this book. (2018 final 2nd ed.; 2014–2015 in-progress draft also on file for historical reference)
- [Barlow Twins Paper](sources/barlow-twins-paper.md) — Zbontar, Jing, Misra, LeCun, Deny (FAIR + NYU; ICML 2021, arxiv 2103.03230). First non-asymmetric anti-collapse SSL method: cross-correlation between two augmented views' embeddings → identity. No predictor, no momentum encoder, no stop-gradient. ImageNet linear top-1 73.2%. Names itself after Horace Barlow's redundancy-reduction principle. (2021-03-04)
- [VICReg Paper](sources/vicreg-paper.md) — Bardes, Ponce, LeCun (FAIR + Inria + NYU; ICLR 2022, arxiv 2105.04906). Three-term anti-collapse loss: variance hinge + covariance decorrelation + invariance MSE. Branches need not share weights or architecture — natural multi-modal SSL. The regularizer LeCun's AMI paper cites by name as the JEPA anti-collapse method; methodological precursor to SIGReg / LeJEPA. (2021-05-11)
- [LeCun 2022 — A Path Towards Autonomous Machine Intelligence](sources/lecun2022-path-towards-ami.md) — LeCun's position paper. Defines the JEPA / H-JEPA architecture, the configurable world model + configurator framing, intrinsic-cost + critic, and the EBM training story behind all subsequent JEPA papers. The vision document AMI Labs was founded to execute. (2022-06-27)
- [DINOv3 Paper](sources/dinov3-paper.md) — Siméoni et al., Meta AI Research (arxiv 2508.10104). 7B-parameter ViT SSL foundation model; introduces Gram anchoring (regularize patch-similarity structure toward an earlier "Gram teacher") to fix the long-training dense-feature degradation observed in DINOv2 at scale. Frozen-backbone COCO mAP 66.1; ADE20k mIoU 63.0. New SSL state-of-the-art and natural drop-in upgrade for the DINO-WM / DINO-world / JEPA-WMs lineage. (2025-08-13)

## Entities

### Companies
- [NVIDIA](entities/nvidia.md) — owns most of the agentic-robotics simulation substrate; also owns [Brev](entities/nvidia-brev.md) GPU-cloud broker. (14 sources)
- [Hiwonder](entities/hiwonder.md) — Chinese educational-robotics vendor; ROSOrin / ROSOrin Pro kits + OpenClaw. (3 sources)
- [Hugging Face](entities/hugging-face.md) — open-source AI company; maintainer of [LeRobot](entities/lerobot.md); HF Hub hosts model checkpoints across the wiki's JEPA / VLA / IL coverage. (4 sources)
- [SIGRobotics-UIUC](entities/sigrobotics-uiuc.md) — student-led robotics org at UIUC; designs and maintains [LeKiwi](entities/lekiwi.md); won U.S. site of the Oct 2025 Embodied AI Hackathon with a GR00T-driven matcha-making XLeRobot; sponsored by FrodoBots / Hugging Face / K-Scale Labs / Neuralink / ROBOTIS / others. (4 sources)
- [Seeed Studio](entities/seeed-studio.md) — Shenzhen open-hardware distributor; sells LeKiwi and hosts the canonical end-user tutorial; co-organizer of LeRobot 2025 + Embodied AI 2025 hackathons. (3 sources)
- [The Robot Studio](entities/the-robot-studio.md) — open-hardware design group behind the SO-ARM100/101 lineage. (3 sources) _stub_
- [AGIBOT](entities/agibot.md) — Shanghai embodied-AI / humanoid company. Open-source-heavy. (3 sources)
- [Hello Robot](entities/hello-robot.md) — Stretch mobile manipulator + stretch_ai stack. (7 sources)
- [HCR Lab](entities/hcrlab.md) — Human-Centered Robotics Lab, UW (Maya Cakmak); assistive robots + EUP; Stretch platform; long-term in-home deployments. (9 sources)
- [Elephant Robotics](entities/elephant-robotics.md) — Chinese edu-robotics vendor; myAGV + myBuddy 280 + arm ecosystem. (2 sources)
- [Pollen Robotics](entities/pollen-robotics.md) — French open-source humanoid maker; Reachy 2. (1 source)
- [Fauna Robotics](entities/fauna-robotics.md) — NYC; Sprout Creator Edition; 107cm, 29 DOF, Jetson AGX Orin. (1 source)
- [K-Scale Labs](entities/k-scale-labs.md) — YC humanoid startup; shut down late 2025; notable post-mortem; was Embodied AI Hackathon mentor + SIGRobotics-UIUC "Mini Humanoid" project sponsor. (3 sources)
- [Meta FAIR](entities/meta-fair.md) — Yann LeCun's lab; JEPA research line. (11 sources)
- [Google DeepMind](entities/google-deepmind.md) — MuJoCo, Newton co-development, MjcPhysics USD plugin, Gemini Robotics. (7 sources)
- [Boston Dynamics](entities/boston-dynamics.md) — robotics company (Hyundai-owned); Spot + Atlas + Stretch + Orbit + AIVI-Learning. (1 source)
- [Mila](entities/mila.md) — Quebec AI Institute; frequent JEPA collaborator. (4 sources) _stub_
- [Farama Foundation](entities/farama-foundation.md) — non-profit; took over OpenAI gym → Gymnasium; 19 RL projects. (3 sources)
- [AMI Labs](entities/ami-labs.md) — Yann LeCun's reported post-Meta AI lab; $1.03B seed round (single secondary source, provisional). (1 source)
- [Anthropic](entities/anthropic.md) — developer of Claude; AI safety mission; author of Claude's Constitution; MCP protocol. (2 sources)
- [Apollo Research](entities/apollo-research.md) — independent AI safety evaluation institute; red-teamed Claude Opus 4 (2025). (2 sources)
- [Physical Intelligence](entities/physical-intelligence.md) — San Francisco; π0/π0.6 cross-platform generalist VLAs. (2 sources)
- [Hillbot](entities/hillbot.md) — UCSD spinoff that maintains ManiSkill. (1 source) _stub_
- [Disney Research](entities/disney-research.md) — Newton co-developer with NVIDIA + DeepMind. (2 sources) _stub_
- [FIRST Robotics Competition](entities/first-robotics-competition.md) — world's leading high-school robotics competition; ~3,700 teams, 30+ countries. (4 sources)
- [AndyMark](entities/andymark.md) — major FRC vendor; AM14U6 chassis, field elements, FUEL scoring elements. (2 sources)
- [Team 254: The Cheesy Poofs](entities/team-254.md) — elite FRC team (2022 World Champions); 2026 "AI in FRC" presentation; Claude Code + wpilib-agent-tools. (2 sources)
- [HHMI Janelia Research Campus](entities/hhmi-janelia.md) — HHMI's pure-research lab; Turaga lab leads flybody + flyvis; *Drosophila* neuroscience & connectomics anchor. (3 sources)
- [NeLy-EPFL (Neuroengineering Laboratory)](entities/nely-epfl.md) — EPFL lab; maintains [NeuroMechFly](entities/neuromechfly.md) + the `flygym` Python library; European counterweight to HHMI Janelia in fly-body simulation. (3 sources)
- [Toyota Research Institute (TRI)](entities/tri.md) — Toyota's R&D arm; Los Altos + Cambridge; co-affiliation across [Diffusion Policy](entities/diffusion-policy.md) + [UMI](entities/umi.md); home of TRI LBM. (2 sources)

### Simulators / frameworks
- [NVIDIA Isaac Sim](entities/nvidia-isaac-sim.md) — Omniverse-based robotics simulator. (5 sources)
- [NVIDIA Isaac Lab](entities/nvidia-isaac-lab.md) — open-source learning framework on Isaac Sim. (5 sources)
- [Newton physics engine](entities/newton-physics-engine.md) — Linux-Foundation, GPU-accelerated. (5 sources)
- [MuJoCo](entities/mujoco.md) — DeepMind-maintained physics engine; substrate for Gymnasium-Robotics, MuJoCo Playground (via MJX), Adroit, Franka Kitchen, DM Control, flybody, NeuroMechFly v2. (11 sources)
- [MuJoCo Playground](entities/mujoco-playground.md) — DeepMind's MJX-based learning framework. (4 sources)
- [Genesis](entities/genesis.md) — generative + ultra-fast physics engine. (2 sources)
- [AGIBOT Genie Sim 3.0](entities/agibot-genie-sim.md) — open embodied-AI sim on Isaac Sim. (2 sources)
- [RoboCasa](entities/robocasa.md) — household manipulation benchmark (RoboCasa365 at ICLR 2026). (4 sources)
- [ManiSkill](entities/maniskill.md) — [SAPIEN](entities/sapien.md)-based GPU-parallel manipulation benchmark. (1 source)
- [SAPIEN](entities/sapien.md) — UCSD robot simulation framework underlying ManiSkill. (1 source) _stub_
- [Gymnasium-Robotics](entities/gymnasium-robotics.md) — Farama's [MuJoCo](entities/mujoco.md)-backed robotics envs (Fetch / Hand / Maze / Adroit / Franka Kitchen / MaMuJoCo). (11 sources)
- [Arcade Learning Environment](entities/ale.md) — Farama's Atari 2600 RL benchmark; 100+ single-agent + 23 multi-agent envs; Gymnasium API. (1 source)
- [Metaworld](entities/metaworld.md) — Stanford/Berkeley meta-RL benchmark; 50 manipulation tasks on simulated Sawyer; staple across V-JEPA-line work. (3 sources)
- [PushT](entities/pusht.md) — 2D T-block pushing benchmark; introduced by IBC, popularized by Diffusion Policy; default lightweight bench across LeWM / DINO-WM / JEPA-WMs. (5 sources)
- [PointMaze](entities/pointmaze.md) — 2D point-mass maze navigation; default lightweight nav bench across LeWM / DINO-WM / JEPA-WMs. (3 sources)
- [DM Control Suite](entities/dm-control.md) — DeepMind continuous-control RL benchmark on top of MuJoCo; pre-Gymnasium-Robotics legacy substrate. (4 sources)
- [LIBERO](entities/libero.md) — lifelong-learning manipulation benchmark; de-facto VLA-eval bench (Spatial / Object / Goal / 100 task families). (1 source)
- [SimplerEnv](entities/simplerenv.md) — Sapien-adjacent mid-weight sim positioned as real-world-correlation harness; used by VLA-JEPA. (1 source)
- [Habitat](entities/habitat.md) — Meta FAIR embodied-AI sim (navigation + manipulation in photorealistic 3D scenes); legacy substrate. (1 source)
- [flybody](entities/flybody.md) — HHMI Janelia + Google DeepMind anatomically detailed *Drosophila* body in MuJoCo (102 DoFs, walking + flight); Apache-2.0. (3 sources)
- [NeuroMechFly](entities/neuromechfly.md) — NeLy/EPFL *Drosophila* body sim with vision + olfaction + brain–VNC hierarchy; v2 (Wang-Chen 2024); flygym v2.x.x package actively maintained 2026 with Warp/MJWarp GPU acceleration. Apache-2.0. (3 sources)

### RL API standards
- [Gymnasium](entities/gymnasium.md) — single-agent RL env API; OpenAI gym successor under Farama. (3 sources)
- [PettingZoo](entities/pettingzoo.md) — multi-agent RL env API. (2 sources)

### Robot platforms
- [Franka Panda](entities/franka-panda.md) — 7-DOF research-grade arm; default tabletop manipulator across DROID, V-JEPA 2, JEPA-WMs, RUM, Diffusion Policy, UMI, Huh-et-al-accessibility. (10 sources)
- [xArm 7](entities/xarm-7.md) — UFactory commercial 7-DOF arm; secondary tabletop manipulator; RUM cross-embodiment transfer target (~10pt drop vs Stretch). (2 sources) _stub_
- [TurtleBot](entities/turtlebot.md) — canonical educational ROS mobile robot (4 generations); TurtleBot 4 in education, TurtleBot 2i used in DRAGON 2024 assistive navigation. (2 sources)
- [iRobot Create 3](entities/irobot-create-3.md) — Roomba-i3-derived ROS 2 mobile-robot base; chassis under [TurtleBot 4](entities/turtlebot.md). (1 source) _stub_
- [Tiago](entities/tiago.md) — PAL Robotics dual-arm mobile manipulator; ROS-native; used in Huh et al. 2026 accessibility study. (1 source)

### Humanoids
- [Atlas](entities/atlas.md) — Boston Dynamics flagship; closed development; capability-bar humanoid. (1 source) _stub_
- [Spot](entities/spot.md) — Boston Dynamics' commercial quadruped; the BD-platform-with-an-API; documented Gemini Robotics-ER 1.5 integration. (1 source)
- [Tesla Optimus](entities/tesla-optimus.md) — Tesla's vertically-integrated humanoid; closed development. (0 sources) _stub_
- [Figure](entities/figure.md) — Figure AI's humanoid line (01/02/03) + Helix VLA; BMW pilots. (2 sources)
- [1X NEO](entities/1x-neo.md) — household humanoid; 22 hand DOF/side; Redwood AI VLM; 22 dB; $200 deposit. (2 sources)
- [Apptronik Apollo](entities/apptronik-apollo.md) — UT Austin spinout; NVIDIA-aligned ([GR00T](entities/nvidia-groot.md) target); Mercedes-Benz pilots. (5 sources) _stub_
- [Digit](entities/digit.md) — Agility Robotics; **first commercially-deployed humanoid** (GXO, Amazon). (0 sources) _stub_
- [Unitree H1](entities/unitree-h1.md) — Chinese affordable research humanoid (~$90k); rapid 2024–2026 academic adoption. (0 sources) _stub_
- [Unitree G1](entities/unitree-g1.md) — smaller, cheaper Unitree (~$16k); cheapest serious humanoid platform. (0 sources) _stub_
- [NAO](entities/nao.md) — SoftBank/Aldebaran 58-cm educational humanoid; canonical since 2008. (0 sources) _stub_
- [TonyPi](entities/tonypi.md) — Hiwonder hobby-tier biped kit ($300–700); educational-tier sibling of [ROSOrin Pro](entities/rosorin-pro.md). (2 sources) _stub_
- [Stretch](entities/stretch.md) — Hello Robot's mobile manipulator (Stretch 3). De-facto research platform. (11 sources)
- [Reachy 2](entities/reachy.md) — Pollen Robotics' open-source bimanual mobile manipulator for embodied AI; ROS 2; 7 DOF/arm. (1 source)
- [myAGV](entities/myagv.md) — Elephant Robotics autonomous mobile base; ROS; Raspberry Pi 4B; pairs with arms. (1 source)
- [LeKiwi](entities/lekiwi.md) — SIGRobotics-UIUC 3-wheel Kiwi-drive holonomic mobile manipulator; Raspberry Pi 5 + STS3215; sub-$1k; LeRobot ecosystem; 1,300+ stars. (3 sources)
- [XLeRobot](entities/xlerobot.md) — Vector Wang's $660 dual-arm household manipulator (2× SO-ARM101 + LeKiwi base + LeRobot); 90% 3D-printed; v0.3.0 (Aug 2025); 2 winning teams at Oct 2025 Embodied AI Hackathon (incl. matcha-bot champion). (2 sources)
- [SO-ARM101](entities/so-arm101.md) — open-source low-cost arm (The Robot Studio); SO-ARM100 successor; default LeRobot manipulator; leader-follower teleoperation convention. (4 sources)
- [Hope Jr Arm](entities/hope-jr-arm.md) — premium-tier prize arm at the LeRobot Worldwide Hackathon 2025; specs not yet ingested. (1 source) _stub_
- [myBuddy 280](entities/mybuddy-280.md) — Elephant Robotics 13 DOF dual-arm desktop robot; $1,619; ROS1. (1 source)
- [ROSOrin](entities/rosorin.md) — Hiwonder's Jetson Orin Nano educational mobile robot kit. (2 sources)
- [ROSOrin Pro](entities/rosorin-pro.md) — Hiwonder's 6-DOF arm + base variant of ROSOrin. (2 sources)
- [ROSOrin Pro 6-DOF arm](entities/rosorin-pro-arm.md) — HX-12H-servo manipulator on the ROSOrin Pro kit. (2 sources)
- [FRC KitBot](entities/frc-kitbot.md) — beginner-friendly FRC robot on AndyMark AM14U6 chassis; included in Kickoff Kit. (2 sources)

### Software stacks
- [stretch_ai](entities/stretch-ai.md) — Hello Robot's open-source Python stack with an LLM agent. (5 sources)
- [OpenClaw](entities/openclaw.md) — Hiwonder's manipulation-aware LLM-agent framework for ROSOrin Pro. (1 source)
- [LeRobot](entities/lerobot.md) — Hugging Face's open-source imitation-learning framework; de-facto stack for affordable mobile manipulators (SO-ARM, LeKiwi, XLeRobot, Bambot, Koch v1.1); ACT default policy; 916-team Worldwide Hackathon in June 2025. (4 sources)

### Controllers
- [roboRIO](entities/roborio.md) — NI's mandatory FRC robot controller (ARM Cortex-A9 + FPGA); WPILib ecosystem. (2 sources)
- [stable-worldmodel](entities/stable-worldmodel.md) — Python infrastructure under LeWorldModel (env zoo + planning API + dataset format). DM Control + Gymnasium-Robotics Fetch + classic + OGBench + more. (0 sources)

### Formats / standards
- [OpenUSD](entities/openusd.md) — open scene-description + robotics physics-schema layer (UsdPhysics, MjcPhysics, NewtonSceneAPI). (5 sources)

### Datasets
- [DROID](entities/droid.md) — Distributed Robot Interaction Dataset; 350 hr / 76k traj / 564 scenes of Franka Panda teleop; the dominant real-robot dataset in JEPA-for-robotics work. (4 sources)

### Model organisms / connectomes
- [Drosophila melanogaster](entities/drosophila.md) — fruit fly; canonical "whole-organism AI" target; substrate for both [FlyWire](entities/flywire.md) and [flybody](entities/flybody.md). (6 sources)
- [FlyWire](entities/flywire.md) — international consortium + dataset for the complete adult *Drosophila* brain connectome (139,255 neurons, ~50M synapses; *Nature* 2024). (4 sources)
- [Drosophila brain model](entities/drosophila-brain-model.md) — Phil Shiu's MIT-licensed Brian 2 LIF model on the FlyWire connectome (paper code). (3 sources)
- [flyvis](entities/flyvis.md) — TuragaLab's MIT-licensed PyTorch connectome-constrained DMN of the fly visual system; v1.1.3 March 2026. (1 source)

### Vision foundation models
- [DINOv2](entities/dinov2.md) — Meta FAIR self-supervised ViT (142M images, ViT-S/B/L/g); substrate for DINO-WM, DINO-world, JEPA-WMs. Apache 2.0. (4 sources)
- [DINOv3](entities/dinov3.md) — Meta AI Research 7B-parameter ViT SSL foundation model (Aug 2025); Gram anchoring fixes dense-feature degradation; new SSL state-of-the-art on dense tasks (COCO mAP 66.1 frozen, ADE20k mIoU 63.0). (1 source)

### Generative models
- [DDPM](entities/ddpm.md) — Denoising Diffusion Probabilistic Models (Ho, Jain, Abbeel; NeurIPS 2020); foundational diffusion-model class; substrate of [Diffusion Policy](entities/diffusion-policy.md), [NVIDIA Cosmos](entities/nvidia-cosmos.md), [Genie Envisioner](entities/genie-envisioner.md). (5 sources)

### World models
- [NVIDIA Cosmos](entities/nvidia-cosmos.md) — world foundation model + simulation engine (generative video). (7 sources)
- [Genie Envisioner](entities/genie-envisioner.md) — AGIBOT's world simulator GE-Sim2 (generative video). (5 sources)
- [V-JEPA 2](entities/v-jepa-2.md) — Meta FAIR's JEPA world model (latent prediction); zero-shot Franka. (7 sources)
- [LeWorldModel](entities/leworldmodel.md) — first stable end-to-end JEPA from raw pixels. (14 sources)
- [JEPA-WMs](entities/jepa-wms.md) — FAIR (Terver et al.); first JEPA-for-robotics paper using RoboCasa. (1 source)
- [DINO-WM](entities/dino-wm.md) — NYU + FAIR; frozen DINOv2 features + learned predictor; zero-shot planning. (10 sources)
- [DINO-world](entities/dino-world.md) — FAIR DINOv2 video world model ("Back to the Features"). (1 source)
- [VLA-JEPA](entities/vla-jepa.md) — JEPA-as-auxiliary inside a VLA policy. (1 source)
- [Dreamer / DreamerV3](entities/dreamer.md) — Hafner-line MBRL family with generative WM + actor-critic in imagination; LeWM baseline. (2 sources)
- [TD-MPC / TD-MPC2](entities/td-mpc.md) — Hansen-line decoder-free MBRL with MPC + TD-bootstrapped value; LeWM baseline; closest MBRL relative to JEPA. (2 sources)
- [PLDM (Planning with Latent Dynamics Models)](entities/pldm.md) — Sobal-line end-to-end JEPA WM (NYU + FAIR); VICReg + inverse-dynamics + similarity multi-term loss; the canonical "end-to-end JEPA before LeWM" baseline. (2 sources — 2022 precursor + 2025 paper)

### VLA models / generalist policies
- [NVIDIA GR00T](entities/nvidia-groot.md) — open VLA bundled with Isaac Lab; N1.5 won both sites of the Oct 2025 Embodied AI Hackathon. (6 sources)
- [Gemini Robotics](entities/gemini-robotics.md) — Google DeepMind robot foundation models; full VLA + Gemini Robotics-**ER** embodied-reasoning VLM (tool-call planner). (1 source)
- [OK-Robot](entities/ok-robot.md) — NYU zero-shot pick-and-drop framework; 58.5% in 10 homes; 1.8× over OVMM. (1 source)
- [Robot Utility Models](entities/robot-utility-models.md) — NYU/Meta zero-shot mobile-manipulation BC. (5 sources)
- [Dobb·E](entities/dobb-e.md) — NYU predecessor to RUM; HPR encoder + Stick-v1 + Homes of New York dataset. (2 sources) _stub_

### Behavior-cloning methods
- [IBC](entities/ibc.md) — Implicit Behavioral Cloning (Florence et al., CoRL 2021); energy-based-model BC; introduced PushT; direct ancestor of Diffusion Policy. (1 source)
- [BET](entities/bet.md) — Behavior Transformer (Shafiullah et al., NeurIPS 2022); transformer + k-means action discretization; ancestor of VQ-BeT. (1 source)
- [VQ-BeT](entities/vq-bet.md) — Vector-Quantized Behavior Transformer (Lee et al. 2024); top performer in RUM ablation. (1 source) _stub_
- [Diffusion Policy](entities/diffusion-policy.md) — Chi et al. 2023, Columbia/TRI/MIT; conditional DDPM over actions; popularized PushT + UMI gripper + action-chunking convention. (3 sources)
- [UMI](entities/umi.md) — Universal Manipulation Interface (Chi et al., RSS 2024); hand-held gripper data-collection system; same lead author as Diffusion Policy. (1 source)

### LLMs
- [Qwen](entities/qwen.md) — Alibaba's open-weights LLM family. Default local LLM in both stretch_ai (3B) and ROSOrin (1.7B). (2 sources)

### Tools
- [Ollama](entities/ollama.md) — local LLM runtime (used by ROSOrin offline curriculum). (1 source) _stub_
- [MimicGen](entities/mimicgen.md) — synthetic-demo expansion tool used by RoboCasa365. (1 source) _stub_
- [NVIDIA Brev](entities/nvidia-brev.md) — NVIDIA's cross-cloud GPU-instance broker (`brev` CLI + Launchables); no native auto-stop, so cost discipline is on the user. (1 source)

### Events
- [LeRobot Worldwide Hackathon 2025](entities/lerobot-worldwide-hackathon-2025.md) — Hugging Face hybrid hackathon, June 14–15, 2025; 916 team members, ~400 submissions, 30 ranked winners; prizes: Hope Jr Arm / LeKiwi / SO-101. (1 source)

### People
- [Yann LeCun](entities/yann-lecun.md) — NYU; Turing Award 2018; architect of the JEPA program; reported founder of AMI Labs (Apr 2026, provisional). Co-authored the original 1993 Siamese network paper at AT&T Bell Labs. (17 sources)
- [Andrej Karpathy](entities/andrej-karpathy.md) — independent AI researcher/educator; formerly Tesla AI director + OpenAI founding member; author of micrograd / nanoGPT / nanochat / autoresearch — the wiki's recommended pedagogical reference implementations for backprop, transformers, end-to-end LLM training, and agent-driven ML research. (4 sources)
- [Navid Azizan](entities/navid-azizan.md) — MIT ME / IDSS / LIDS; learning-based control; SD-LQR (ICML 2023) + drone adaptive control (2025). (2 sources)
- [Adrien Bardes](entities/adrien-bardes.md) — FAIR researcher; lead author on VICReg (ICLR 2022); co-senior on V-JEPA 2, V-JEPA 2.1, JEPA-WMs. The FAIR-side champion of the V-JEPA program. (4 sources)
- [Basile Terver](entities/basile-terver.md) — researcher (FAIR-affiliated, inferred); bread-crumb across DINO-world → JEPA-WMs lineage. (2 sources)
- [Sergey Levine](entities/sergey-levine.md) — UC Berkeley EECS; senior on DROID + Metaworld. (0 source pages yet — referenced via entity pages)
- [Chelsea Finn](entities/chelsea-finn.md) — Stanford CS; senior on DROID + Metaworld. (0 source pages yet — referenced via entity pages)
- [Lerrel Pinto](entities/lerrel-pinto.md) — NYU CS; co-senior on DINO-WM, RUM, and OK-Robot. (5 sources)
- [Yuke Zhu](entities/yuke-zhu.md) — UT Austin / NVIDIA Research; senior on RoboCasa365; co-author on Huh et al. 2026. (2 sources)
- [Karl Pertsch](entities/karl-pertsch.md) — DROID co-lead with Khazatsky; Berkeley/Stanford. (0 source pages yet — referenced via entity pages)
- [Mahi Shafiullah](entities/mahi-shafiullah.md) — NYU + Hello Robot; lead/co-author on Dobb·E, RUM, and OK-Robot. (5 sources)
- [Phil Shiu](entities/phil-shiu.md) — UC Berkeley → Eon Systems; lead author + maintainer of the FlyWire-based LIF brain simulation. (2 sources)
- [Maya Cakmak](entities/maya-cakmak.md) — UW; HCR Lab PI; physically assistive robots + EUP; Henry Evans long-term deployments; autonomy preference finding. (9 sources)
- [Amal Nanavati](entities/amal-nanavati.md) — UW HCR Lab; robot-assisted feeding; PAR systematic review; out-of-lab deployment methodology. (4 sources)
- [Katherine Driggs-Campbell](entities/katherine-driggs-campbell.md) — UIUC ECE; senior on DRAGON; HRI + safety-critical autonomy + assistive navigation. (1 source)
- [Shuijing Liu](entities/shuijing-liu.md) — UIUC ECE PhD (Driggs-Campbell); first author on DRAGON. (1 source)
- [Mina Huh](entities/mina-huh.md) — UC Berkeley; accessibility + HRI; first author on Huh et al. 2026. (1 source)
- [Amy Pavel](entities/amy-pavel.md) — UC Berkeley; accessibility + AI-mediated description; senior on Huh et al. 2026. (1 source)
- [Roberto Martin-Martin](entities/roberto-martin-martin.md) — UT Austin CS; embodied AI, manipulation, mobile manipulation; co-author on Huh et al. 2026. (1 source)
- [Huihan Liu](entities/huihan-liu.md) — UT Austin; robot learning; co-author on Huh et al. 2026 (distinct from Shuijing Liu). (1 source)
- [Eike Schneiders](entities/eike-schneiders.md) — Aalborg University; qualitative HRI/HCI of domestic robots and automation. (1 source)
- [Vector Wang (Gaotian Wang)](entities/vector-wang.md) — creator of [XLeRobot](entities/xlerobot.md); composition-style affordable-robotics builder. (1 source)
- [Remi Cadene](entities/remi-cadene.md) — robotics lead at [Hugging Face](entities/hugging-face.md); responsible for [LeRobot](entities/lerobot.md); co-organizer of the [Worldwide Hackathon 2025](entities/lerobot-worldwide-hackathon-2025.md). (1 source)

## Concepts
- [World model](concepts/world-model.md) — umbrella concept: learned predictive model of environment dynamics (generative-video / JEPA / frozen-feature / model-based-RL). (14 sources)
- [VLA models](concepts/vla-models.md) — vision-language-action robot foundation models. (13 sources)
- [Joint-Embedding Predictive Architecture](concepts/jepa.md) — predict next-state representations, not pixels. (15 sources)
- [Siamese network](concepts/siamese-network.md) — two weight-tied encoders + similarity/distance/predictor head; ancestor of every joint-embedding SSL system since 1993. (5 sources)
- [Sim-to-real transfer](concepts/sim-to-real-transfer.md) — bridging simulator-trained policies to real robots. (9 sources)
- [World-model simulators](concepts/world-model-simulators.md) — narrower companion to [World model](concepts/world-model.md): world-models-used-as-simulators (generative-video and JEPA paradigms). (14 sources)
- [Imitation learning](concepts/imitation-learning.md) — supervised learning from demonstrations. (17 sources)
- [AI safety and alignment](concepts/ai-safety-alignment.md) — corrigibility, broadly safe behaviors, hard constraints, catastrophic risk framing; connects to agentic robot deployments. (3 sources)
- [Corrigibility](concepts/corrigibility.md) — the corrigibility dial (fully corrigible ↔ fully autonomous); asymmetric cost argument; galaxy-brained reasoning risk; agentic deployment implications. (1 source)
- [LLM-agent architecture](concepts/llm-agent-architecture.md) — LLM-emits-tool-calls control pattern; MCP and A2A as inter-agent/tool-access protocols. (8 sources)
- [AprilTags](concepts/apriltags.md) — visual fiducial markers for 6-DOF pose estimation; standard in FRC and research robotics. (2 sources)
- [Learned latent space](concepts/latent-space.md) — vector space where a trained encoder represents inputs; substrate for JEPA prediction, DINOv2 features, VQ-BeT codebook. (10 sources)
- [Agentic UAVs](concepts/agentic-uavs.md) — autonomous aerial systems with goal-driven behavior; 4-layer architecture; 8 domains; adaptive control. (2 sources)
- [Assistive robotics](concepts/assistive-robotics.md) — robots helping disabled/elderly users regain autonomy; systematic review; three research themes; autonomy finding. (16 sources)
- [Accessible robot communication](concepts/accessible-robot-communication.md) — robot output-interface design for non-visual users; mixed-initiative narration findings; 6 design guidelines (Huh et al. 2026). (4 sources)
- [End-user robot programming](concepts/end-user-robot-programming.md) — enabling non-experts to customize robot behavior; EUP approaches; sense of agency evidence; Stretch SE2 transfer. (7 sources)
- [Biomechanical simulation](concepts/biomechanical-simulation.md) — physics-based simulation of an animal body; lineage *C. elegans* → Hydra → virtual rodent → NeuroMechFly v1/v2 → flybody. (5 sources)
- [Connectome](concepts/connectome.md) — complete wiring diagram of a nervous system; *C. elegans* → fly hemibrain → FlyWire → mouse → human. (3 sources)
- [Optimal control](concepts/optimal-control.md) — minimize a cost over trajectory-control pairs subject to dynamics. Brachystochrone (1697) → Euler–Lagrange → Hamilton–Jacobi → Pontryagin's Maximum Principle (1956) → Bellman DP → modern LQR / MPC / iLQR / CEM / learned-WM-OC. The "RL = approximate OC under uncertainty" bridge. (12 sources)

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
- [Levels of autonomy in assistive robotics](syntheses/levels-of-autonomy-in-assistive-robotics.md) — three orthogonal autonomy axes (execution / programming / intent inference); five empirical findings; user-EUP-over-RUM stack as unbuilt natural integration. (2026-05-09)
- [Long-term in-home robot deployments](syntheses/long-term-in-home-robot-deployments.md) — depth-sorted table of every in-home deployment in the wiki; reliability gradient; what's missing from the longitudinal record. (2026-05-09)
- [Stretch as the de-facto assistive-robotics platform](syntheses/stretch-as-assistive-platform.md) — why every wiki-relevant in-home deployment uses Stretch; eight features that compound; what Stretch doesn't solve. (2026-05-09)
- [DINO-WM on Stretch — concrete experiment plan](syntheses/dino-wm-on-stretch-experiment.md) — sibling to LeWM-on-Stretch; lower-risk frozen-encoder variant; train predictor only on RUM dataset. (2026-05-09)
- [Underserved PAR domains — dressing, bathing, medication](syntheses/underserved-par-domains.md) — sub-capability decomposition for each; ranked researcher targets (medication-fetcher most tractable). (2026-05-09)
- [Robot-learning curriculum — from neurons to LeWorldModel](syntheses/robot-learning-curriculum.md) — 14-module curriculum hub; **all 14 modules drafted**. (2026-05-10)
- [Curriculum Module 1 — Neural networks and training](syntheses/curriculum-01-neural-networks.md) — Tier 1; neuron, MLP, backprop, BN/LN, residuals, Adam. Anchor: tiny MLP digit classifier. (2026-05-10)
- [Curriculum Module 2 — CNNs and visual representation learning](syntheses/curriculum-02-cnns.md) — Tier 1; convolution, pooling, ResNet, ImageNet pretrain + fine-tune, visual encoders. Anchor: ResNet-18 features on PushT. (2026-05-10)
- [Curriculum Module 3 — Sequence models, attention, and transformers](syntheses/curriculum-03-attention-and-transformers.md) — Tier 1; attention, MHA, transformer blocks, ViT, positional encoding, causal masking. Anchor: tiny transformer on PushT patches. (2026-05-10)
- [Curriculum Module 4 — Self-supervised learning and embeddings](syntheses/curriculum-04-self-supervised-learning.md) — Tier 1; SSL taxonomy, representation collapse, anti-collapse families (EMA, VICReg, frozen, multi-fix, SIGReg). Anchor: VICReg on CIFAR with/without regularizer. (2026-05-10)
- [Curriculum Module 5 — Generative modeling fundamentals (DDPM, full math)](syntheses/curriculum-05-generative-models.md) — Tier 2. Full ELBO → `L_simple` derivation; KL bounds; ε-parameterization; noise schedules; DDIM sampling; classifier-free guidance derivation. Anchor: train tiny DDPM on MNIST + paper-derive `L_simple` from ELBO. (2026-05-10)
- [Curriculum Module 6 — Imitation learning and behavior cloning](syntheses/curriculum-06-imitation-learning.md) — IL/BC frame, multi-modal failure mode, distribution shift / DAgger, action chunking + receding-horizon control, PushT setup. (2026-05-10)
- [Curriculum Module 7 — BC lineage on PushT (IBC → BeT → DP)](syntheses/curriculum-07-bc-lineage-pusht.md) — multi-modal-action problem + IBC/BeT/Diffusion Policy + bridge to world models; anchor exercise on PushT. (2026-05-10)
- [Curriculum Module 8 — Reinforcement learning vocabulary](syntheses/curriculum-08-rl-vocabulary.md) — light/vocabulary-only RL coverage (MDP, return, value, policy, REINFORCE → PPO, DQN, MFRL vs MBRL, Dreamer-class latent imagination); supporting module for the LeWM Dreamer / TD-MPC baselines. (2026-05-10)
- [Curriculum Module 9 — Vision-Language-Action models](syntheses/curriculum-09-vla.md) — closes the policy-side reading chain (6 → 7 → 9). VLA structural definition; VLAs are not world models; action-head taxonomy; major 2026 VLAs; S1/S2 hierarchical pattern; VLA-JEPA as Module-11 cross-over. (2026-05-10)
- [Curriculum Module 10 — World models, broad](syntheses/curriculum-10-world-models.md) — functional definition; four families (generative-video / JEPA / frozen-feature / MBRL); MPC + CEM + gradient-based planning; horizon vs compounding error; LeWM positioned in the taxonomy. (2026-05-10)
- [Curriculum Module 11 — JEPA in depth](syntheses/curriculum-11-jepa-deep.md) — joint-embedding architecture; collapse-prevention zoo (EMA, VICReg, frozen encoder, multi-fix, SIGReg); V-JEPA progression; DINO-WM frozen-feature variants; JEPA-WMs first-real-Franka; LeWM-vs-V-JEPA-2 axis-by-axis. (2026-05-10)
- [Curriculum Module 12 — LeWorldModel deep-dive (with full SIGReg math)](syntheses/curriculum-12-lewm-deep-dive.md) — the destination module. LeWM section by section; full SIGReg derivation (random projections + Epps–Pulley + Cramér–Wold + backprop); architecture (incl. the BN-after-CLS trick); CEM-MPC; four-env results; latent probing + VoE; what it means for the JEPA program. (2026-05-10)
- [Curriculum Module 13 — Home robotics deployment reality](syntheses/curriculum-13-home-robotics-deployment.md) — the 89.4 / 12.4 gap; Stretch convergence; RUM + OK-Robot as strongest current results; PAR / EUP / autonomy-preference framing; where LeWM-class techniques plausibly fit (and don't). Anchor: pick LeWM-on-Stretch vs DINO-WM-on-Stretch. (2026-05-10)
- [Curriculum Module 14 — Capstone (paper-first, hardware-second)](syntheses/curriculum-14-capstone.md) — the capstone. Phase A: reproduce LeWM PushT + 5–10 page experiment-design memo for a Stretch experiment. Phase B (gated): execute on real Stretch, compare to a Diffusion Policy baseline. The curriculum is completable on phase A alone. (2026-05-10)

### JEPA-related concepts/entities/sources to potentially expand
- Metaworld — referenced by [JEPA-WMs](sources/jepa-wms-paper.md) (42 tasks); deserves an entity page.
- LIBERO / LIBERO-Plus — referenced by [VLA-JEPA](sources/vla-jepa-paper.md); benchmark concept/source pages.
- SimplerEnv — referenced by [VLA-JEPA](sources/vla-jepa-paper.md); mid-weight Sapien-adjacent simulator.
- `stable-worldmodel` package — env zoo broader than [LeWM howto](syntheses/leworldmodel-howto.md) exposed; verify and update.
- ~~PLDM~~ — now filed: [PLDM Paper](sources/pldm-paper.md) + [PLDM entity](entities/pldm.md) (2026-05-10).
- ~~DreamerV3, TD-MPC~~ — both now filed: [DreamerV3 Paper](sources/dreamer-v3-paper.md) + [Dreamer entity](entities/dreamer.md), [TD-MPC2 Paper](sources/td-mpc2-paper.md) + [TD-MPC entity](entities/td-mpc.md).

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
- TRI LBM (Toyota Research Institute Large Behavior Model) — referenced in RoboCasa365 paper as baseline. ([TRI](entities/tri.md) parent entity now filed.)
- Octo — referenced in RoboCasa365 paper as baseline
- Stretch Mujoco — Hello Robot's MuJoCo wrapper; thin or substantive?
- ~~PLDM~~ — now filed: [PLDM Paper](sources/pldm-paper.md) + [PLDM entity](entities/pldm.md) (2026-05-10). All four LeWM baselines ([DINO-WM](entities/dino-wm.md), [Dreamer](entities/dreamer.md), [TD-MPC](entities/td-mpc.md), [PLDM](entities/pldm.md)) now have primary-source pages.
- DROID paper itself (arxiv 2403.12945), Metaworld paper (arxiv 1910.10897), DINOv2 paper (arxiv 2304.07193), Dobb·E paper (arxiv 2306.16650), VQ-BeT paper (Lee et al. 2024) — entity pages exist but the papers themselves are not yet source pages; would let us cite design rationale directly. ([Diffusion Policy Paper](sources/diffusion-policy-paper.md), [IBC Paper](sources/ibc-paper.md), [BET Paper](sources/bet-paper.md), [DDPM Paper](sources/ddpm-paper.md), [UMI Project Page](sources/umi-paper.md) now filed.)
- DDIM (Song, Meng, Ermon, ICLR 2021, arxiv 2010.02502) and iDDPM (Nichol & Dhariwal, ICML 2021) — diffusion-model advances Diffusion Policy uses directly; primary sources not yet filed.
- R3M visual encoder (Nair et al. 2022) — appears in Diffusion Policy real-world Push-T ablation as alternative to end-to-end ResNet-18.
- Cheng Chi, Shuran Song, Yilun Du, Russ Tedrake — author entity pages for the Diffusion Policy / UMI line.
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
- ~~Boston Dynamics Spot~~ — now filed as [Spot](entities/spot.md); [Boston Dynamics](entities/boston-dynamics.md) parent entity also filed.
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
