# Index

> **New here?** Read the [wiki overview](overview.md) — what this is, what's in it, and where to start.

## Highlights

Curated entry points across the wiki.

**Curriculum / learning path**
- [Robot-learning curriculum — from neurons to LeWorldModel](syntheses/curriculum/robot-learning-curriculum.md) — 14-module bottom-up syllabus, **all modules drafted**; PushT as the connecting thread; ends with a Stretch-platform capstone.
- [Curriculum Module 1 — Neural networks and training](syntheses/curriculum/curriculum-01-neural-networks.md) — Tier 1. Neurons, MLP, forward pass + backprop, MSE/CE, SGD/Adam, regularization, BN/LN, residuals, depth. Brisk-but-rigorous refresher.
- [Curriculum Module 2 — CNNs and visual representation learning](syntheses/curriculum/curriculum-02-cnns.md) — Tier 1. Convolution, pooling, receptive field, ResNet skip connections, ImageNet pretraining + fine-tuning, "visual encoder" abstraction. ResNet-18 as the BC-line default.
- [Curriculum Module 3 — Sequence models, attention, and transformers](syntheses/curriculum/curriculum-03-attention-and-transformers.md) — Tier 1. Attention, self-attention, multi-head, transformer blocks, positional encoding, causal masking, ViT (patches + [CLS]). Encoder-only / decoder-only / encoder-decoder.
- [Curriculum Module 4 — Self-supervised learning and embeddings](syntheses/curriculum/curriculum-04-self-supervised-learning.md) — Tier 1. SSL taxonomy (contrastive vs predictive); representation collapse as first-order failure mode; five anti-collapse families (EMA + stop-grad, VICReg, frozen encoder, multi-fix soup, SIGReg). Sets up Module 11.
- [Curriculum Module 5 — Generative modeling fundamentals (DDPM, full math)](syntheses/curriculum/curriculum-05-generative-models.md) — Tier 2. Full ELBO → `L_simple` derivation; KL bounds; ε-parameterization; noise schedules; DDIM sampling; classifier-free guidance derivation; bridges to Diffusion Policy, π0 flow matching, and generative-video WMs.
- [Curriculum Module 6 — Imitation learning and behavior cloning](syntheses/curriculum/curriculum-06-imitation-learning.md) — IL/BC frame, multi-modality + distribution-shift failure modes, PushT setup; anchor exercise = train vanilla MSE-MLP BC and watch it fail.
- [Curriculum Module 7 — BC lineage on PushT (IBC → BeT → DP)](syntheses/curriculum/curriculum-07-bc-lineage-pusht.md) — direct successor to Module 6; the policy-learning side of the LeWM ablation table.
- [Curriculum Module 8 — Reinforcement learning vocabulary](syntheses/curriculum/curriculum-08-rl-vocabulary.md) — light, vocabulary-only RL coverage (MDP, return, value, policy, REINFORCE → PPO, DQN, MFRL vs MBRL, Dreamer-class latent imagination). Just enough to read the LeWM baseline columns.
- [Curriculum Module 9 — Vision-Language-Action models](syntheses/curriculum/curriculum-09-vla.md) — VLA = VLM + action head; major instances (GR00T, π0, Helix, Gemini Robotics, OpenVLA); action-head design (AR tokens / flow matching / DDPM); System 1 / System 2 pattern; VLA-JEPA cross-over.
- [Curriculum Module 10 — World models, broad](syntheses/curriculum/curriculum-10-world-models.md) — four-family WM taxonomy (generative-video / JEPA / frozen-feature / MBRL); MPC + CEM + gradient-based planning; horizon vs compounding error; bridge to LeWM.
- [Curriculum Module 11 — JEPA in depth](syntheses/curriculum/curriculum-11-jepa-deep.md) — joint-embedding architectural commitment; V-JEPA 1→2→2-AC→2.1 progression; the six-family collapse-prevention zoo (EMA/stop-grad, VICReg, frozen encoder, multi-fix soup, SIGReg); DINO-WM vs end-to-end JEPA; JEPA-WMs real-Franka.
- [Curriculum Module 12 — LeWorldModel deep-dive (with full SIGReg math)](syntheses/curriculum/curriculum-12-lewm-deep-dive.md) — **the curriculum's destination**. LeWM section by section; full SIGReg derivation (Cramér–Wold + Epps–Pulley + backprop through the test statistic); two-loss architecture; CEM-MPC planning; four-environment results; latent probing + violation-of-expectation; the BN-after-CLS engineering trick.
- [Curriculum Module 13 — Home robotics deployment reality](syntheses/curriculum/curriculum-13-home-robotics-deployment.md) — the deployment-reality module. 89.4% / 12.4% RLBench-vs-BEHAVIOR-1K gap; Stretch as de-facto platform; RUM + OK-Robot as the strongest current home-robotics results; PAR + EUP + autonomy-preference framing; underserved domains; where LeWM-class fits and doesn't.
- [Curriculum Module 14 — Capstone (paper-first, hardware-second)](syntheses/curriculum/curriculum-14-capstone.md) — the capstone. Phase A (paper/sim, required): reproduce LeWM PushT + 5–10 page experiment-design memo. Phase B (Stretch hardware, gated): execute the memo with a Diffusion Policy baseline.
- [Glossary](glossary.md) — flat acronym + term reference (BC, VLM, CNN, SSL, MPC, MSE, LSTM, SIGReg, …); cross-linked from every curriculum module.

**AI Safety and Alignment**
- [Claude's Constitution](sources/claudes-constitution.md) — Anthropic's primary specification for Claude's values, corrigibility model, principal hierarchy, and hard constraints.
- [AI safety and alignment](concepts/safety/ai-safety-alignment.md) — concept overview; connects to agentic robot deployments.
- [Corrigibility](concepts/safety/corrigibility.md) — the corrigibility dial, asymmetric cost argument, galaxy-brained reasoning risk.
- [Apollo Research](entities/apollo-research.md) — independent safety evaluation institute; red-teamed Claude Opus 4.

**Assistive Robotics**
- [Assistive robotics](concepts/robotics/assistive-robotics.md) — concept overview; sim-to-real gap quantified (89.4% RLBench vs 12.4% BEHAVIOR-1K household tasks).
- [Accessible robot communication](concepts/robotics/accessible-robot-communication.md) — output-interface side of HRI for non-visual users; mixed-initiative narration preferred by blind users.
- [Assistive robotics — R&D landscape](syntheses/assistive/assistive-robotics-research-landscape.md) — seven blocking problems, timeline, active researchers, independent-researcher paths, JEPA fit.
- [Levels of autonomy in assistive robotics](syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md) — three orthogonal autonomy axes; EUP preserves agency; variable-LoC design pattern.
- [Long-term in-home robot deployments](syntheses/assistive/long-term-in-home-robot-deployments.md) — what the longitudinal record actually shows (Henry Evans summers + Nanavati 2025 + RUM/OK-Robot breadth).
- [Stretch as the de-facto assistive-robotics platform](syntheses/assistive/stretch-as-assistive-platform.md) — why every wiki-relevant in-home deployment converged on Stretch.
- [Underserved PAR domains — dressing, bathing, medication](syntheses/assistive/underserved-par-domains.md) — what blocks each, realistic researcher targets.
- [OK-Robot](entities/ok-robot.md) — zero-shot pick-and-drop in 10 homes; 58.5% success; state-of-the-art household manipulation.
- [Robot Utility Models](entities/robot-utility-models.md) — NYU/Meta zero-shot BC; data diversity > data quantity insight.
- [Stanford HAI — AI Index Report 2026](sources/stanford-hai-ai-index-2026.md) — 89.4% vs 12.4% gap; humanoid landscape; Physical AI assessment.
- [DRAGON (Liu et al. 2024)](sources/dragon-assistive-nav-2024.md) — TurtleBot guide robot for visually impaired users; CLIP-grounded landmark recognition + dialogue.
- [Designing Accessible Robot Communication for Blind People (Huh et al. 2026)](sources/huh2026-accessible-robot-comm.md) — 6 DGs; mixed-initiative narration; observational + controlled study (10+20+20).

**FRC (FIRST Robotics Competition)**
- [FRC 2026 Game Manual — REBUILT](sources/frc-2026-game-manual.md) — deep ingest of the 166-page 2026 REBUILT game manual.
- [FIRST Robotics Competition](entities/first-robotics-competition.md) — competition overview, robot constraints, technical infrastructure.
- [FRC KitBot](entities/frc-kitbot.md) — the beginner-friendly KitBot platform.
- [FRC simulation & AI landscape](syntheses/simulators/frc-simulation-and-ai-landscape.md) — what simulation & AI tools FRC teams use (trajectory planners, physics sims, ML frontier).

**JEPA / LeWorldModel**
- [Joint-Embedding Predictive Architecture](concepts/world-models/jepa.md) — JEPA concept page.
- [Learned latent space](concepts/world-models/latent-space.md) — the substrate JEPAs predict in.
- [LeWorldModel Paper](sources/leworldmodel-paper.md) — LeWM paper ingest.
- [LeWorldModel — train and run howto](syntheses/world-models/leworldmodel-howto.md) — how to install, train, and evaluate LeWM on a single GPU.
- [LeWM hello world — Project 1 detailed scope](syntheses/projects/lewm-hello-world-project-scope.md) — reproduce LeWM PushT from scratch.
- [JEPA task capabilities](syntheses/world-models/jepa-task-capabilities.md) — what JEPA models can do, mapped per-paper.

**ROSOrin Pro JEPA project ladder**
- [JEPA project ladder for ROSOrin Pro](syntheses/projects/jepa-project-ladder-rosorin-pro.md) — six-rung educational/research project ladder for learning JEPA on ROSOrin Pro hardware.
- [LeWM on ROSOrin Pro — feasibility analysis](syntheses/projects/lewm-on-rosorin-pro-feasibility.md) — feasibility analysis for deploying LeWM on ROSOrin Pro.

**Whole-organism agentic AI (fruit fly)**
- [Whole-organism agentic AI](syntheses/agents/whole-organism-agentic-ai.md) — brain ([FlyWire](entities/flywire.md)) + body ([flybody](entities/flybody.md) / [NeuroMechFly v2](entities/neuromechfly.md)) for *Drosophila*: the first plausible end-to-end animal-scale agent loop.
- [flybody](entities/flybody.md) — HHMI Janelia + DeepMind whole-body fly physics in MuJoCo (walking + flight).
- [NeuroMechFly](entities/neuromechfly.md) — NeLy/EPFL parallel platform (walking + vision + olfaction + brain–VNC); active flygym v2.x.x with GPU acceleration.
- [FlyWire](entities/flywire.md) — complete adult *Drosophila* connectome.
- [Drosophila brain model](entities/drosophila-brain-model.md) and [flyvis](entities/flyvis.md) — open-source brain-side controllers (LIF + connectome-constrained DMN).
- [Biomechanical simulation](concepts/bio/biomechanical-simulation.md) and [Connectome](concepts/bio/connectome.md) — concept pages.

**General**
- [Simulators for agentic robotics — 2026 landscape](syntheses/simulators/simulators-for-agentic-robotics-2026.md) — landscape survey across six categories.

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
- [JEPA-WMs Paper](sources/jepa-wms-paper.md) — Terver, Yang, Ponce, Bardes, LeCun (FAIR + Inria + ENS/PSL + NYU; TMLR 05/2026). First systematic ablation of JEPA-WM design choices (encoder / predictor arch / multi-step rollout / context / proprioception / planner / scaling). Recommended recipe — **DINOv3-L + AdaLN+RoPE predictor + 6-step rollout + CEM-L₂** on real manipulation; **DINOv2-S + 2-step rollout** in sim. **Beats DINO-WM and V-JEPA-2-AC on every evaluated env** (Wall 78.8 vs 64.1; MW-R 58.2 vs 44.8; DROID 48.2 vs 39.4/42.9). First JEPA paper to use RoboCasa + Metaworld + DROID + real Franka. (TMLR 05/2026; arxiv preprint 2025-12)
- [JEPA-WMs GitHub (facebookresearch/jepa-wms)](sources/jepa-wms-github.md) — official PyTorch implementation + 12 pretrained checkpoints (5 JEPA-WMs paper recipe + 5 DINO-WM baselines + 2 V-JEPA-2-AC variants, including the **"fixed" rollout-loss-bug-corrected** version used in the paper Table 2) + 4 VM2M decoder heads. Conda + uv install; env vars `JEPAWM_DSET / JEPAWM_LOGS / JEPAWM_HOME`. Datasets on HF (`facebook/jepa-wms`); DROID requires separate `gsutil` download (5.6–8.7 TB). **License: CC-BY-NC 4.0** — non-commercial only. (2025-12-30)
- [Mobile ALOHA Paper (Fu, Zhao, Finn — Stanford)](sources/mobile-aloha-paper.md) — **$32k bimanual mobile manipulator** with whole-body teleoperation (operator tethered to AgileX Tracer base, backdrives wheels by walking while both hands run [ALOHA](entities/aloha.md) leader arms). Closes long-standing wiki gap (ALOHA / ACT were repeatedly flagged as missing). Key result: **co-training 825 static-bimanual demos + 20–50 in-domain mobile-bimanual demos boosts success by up to +90% absolute** (avg +34% across 7 tasks: Wipe Wine, Cook Shrimp, Rinse Pan, Use Cabinet, Call Elevator, Push Chairs, High Five). Method-agnostic — works with [ACT](entities/act.md), [Diffusion Policy](entities/diffusion-policy.md), and (weakly) VINN. Robust to 30/50/70% co-train mixture; beats pre-train→fine-tune. Hardware: 4× [Trossen ViperX 300](entities/viperx-300.md) + RTX 3070 Ti laptop + 1.26 kWh battery; 12 hr runtime. Fully open-source (hardware + software + tutorials). (2024-01)
- [Mobile ALOHA project page (mobile-aloha.github.io)](sources/mobile-aloha-project-page.md) — companion to the paper; surfaces the tutorial Google Doc, dataset Google Drive, author homepages, and the **[ACT++](entities/act-plus-plus.md)** codebase (`MarkFzp/act-plus-plus`) as the mobile-extended ML successor to original [ACT](entities/act.md). (2024-01)
- [Robot Learning: A Tutorial (LeRobot, Capuano et al.)](sources/lerobot-robot-learning-tutorial.md) — **official LeRobot team-authored tutorial** (arXiv 2510.12403 + HF Space at huggingface.co/spaces/lerobot/robot-learning-tutorial; 410 likes). Chapter arc: Classical Robotics → RL → IL → Generalist (VLA) Policies, with runnable `lerobot` code examples for [ACT](entities/act.md), [Diffusion Policy](entities/diffusion-policy.md), async inference, π₀, and SmolVLA. First HF-Space ingest in the wiki; the parallel official version of the [robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md) (theirs is mid-stack-first, the wiki's is bottom-up). (2025-10-14)
- [Grievous (alexkoven/Grievous)](sources/grievous-github.md) — Alex Koven's early-stage cheap-bimanual-mobile testbed; design "based on [Mobile ALOHA](entities/aloha.md) + [XLeRobot](entities/xlerobot.md)"; software built on [LeRobot](entities/lerobot.md); RPi5-host + remote-PC architecture. **First wiki-tracked downstream-of-Mobile-ALOHA project** and first concrete attempt to cost-reduce Mobile ALOHA from $32k toward the XLeRobot ($660) tier. Repo is WIP — README + install + run only; no BOM, paper, or specs yet. (2026)
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
- [π0 Paper](sources/pi-zero-paper.md) — Black et al. ([Physical Intelligence](entities/physical-intelligence.md), Oct 2024). **Full HTML ingested 2026-05-25** (supersedes prior abstract-only ingest). 3.3 B-param VLA = PaliGemma 3 B VLM + flow-matching action expert with full bidirectional self-attention. Trained on **~10,000 hours of in-house dexterous teleop** across 7 robot configurations + 68 tasks + OXE + DROID + Bridge. Tasks: laundry folding, table bussing, microwave dish loading, egg-carton stacking, box assembly, grocery bagging. Beats OpenVLA + Octo baselines. Now has dedicated [π0 entity](entities/pi-zero.md). (2024-10; full HTML re-ingest 2026-05-25)
- [SmolVLA Paper](sources/smolvla-paper.md) — Shukor, Aubakirova, Capuano, …, Wolf, [Cadene](entities/remi-cadene.md) ([Hugging Face](entities/hugging-face.md) LeRobot team + Sorbonne + valeo.ai + ENS Paris-Saclay; June 2025). **450 M-param affordable-VLA reference**; SmolVLM-2 backbone + flow-matching action expert with **interleaved cross-attention + causal self-attention**; pretrained on **22.9 K episodes from 481 community HF datasets** (≈10× less data than π0). **Beats [π0](entities/pi-zero.md) 3.5 B by +16.6 pts on real-world SO-100 multi-task** (78.3 vs 61.7 avg) despite ~7× fewer params. Ties or beats [OpenVLA 7 B](concepts/learning/vla-models.md) + Octo + [Diffusion Policy](entities/diffusion-policy.md) on LIBERO and Meta-World simulation. Introduces **async-inference RobotClient/PolicyServer stack** with threshold-`g` queue management + observation similarity filter — the practical-deployment piece most VLA papers skip. Available as [`lerobot/smolvla_base`](https://huggingface.co/lerobot/smolvla_base). (2025-06-02)
- [π0.7 Paper](sources/pi07-paper.md) — [Physical Intelligence](entities/physical-intelligence.md) (86 authors incl. Black, Driess, Finn, Hausman, Levine, Pertsch; 2025). **5 B-param successor to [π0](entities/pi-zero.md)** = Gemma3 4B VLM + 860 M flow-matching action expert + MEM video-history encoder. Headline contribution: **diversified prompt** (subtask instructions + subgoal images from a BAGEL 14B world model + episode metadata + control mode), each component dropped randomly during training. **First credible "emergent capabilities" in a VLA** — out-of-the-box espresso machine, laundry folding, vegetable peeling; zero-shot cross-embodiment; compositional generalization (e.g., loading a sweet potato into an air fryer when neither appeared in training). Uses **Knowledge Insulation (KI) training**: VLM supervised via FAST tokens; flow-matching action expert with stop-gradient. (2025)
- [π*0.6 Paper](sources/pistar06-paper.md) — [Physical Intelligence](entities/physical-intelligence.md) (53 authors; 2025). RL-adapted variant of π0.6 + **RECAP** ("RL with Experience and Corrections via Advantage-conditioned Policies"). Pre-trains VLA via offline RL, then iterates with deployment data + human interventions (human-gated DAgger) + sparse outcome rewards. Trains a **multi-task distributional value function** (201 bins, MC return target) and extracts an **advantage-conditioned** policy via CFGRL-style classifier-free guidance — sidesteps the policy-gradient problem on flow-matching VLAs. **2× throughput, ½ failure rate** on hardest tasks; **13-hr continuous espresso operation**; 2+ hr novel-laundry folding in a new home. The wiki's first VLA-scale RL-from-deployment recipe. (2025)
- [The Elements of Differentiable Programming (Blondel & Roulet, Google DeepMind)](sources/blondel-roulet-differentiable-programming.md) — **485-page reference textbook**, draft v3 (June 24, 2025); free on arXiv. By [Mathieu Blondel](entities/mathieu-blondel.md) + Vincent Roulet. Five parts × 18 chapters covering the entire mathematical substrate of modern ML: univariate/multivariate differentiation + linear maps + JVPs/VJPs (ch. 2); MLPs + activations + normalizations + RNNs + **transformers** (ch. 4); differentiable control flow + data structures + "attention as differentiable dict lookup" (chs. 5–6); **forward + reverse mode autodiff** + Baur-Strassen theorem + checkpointing (ch. 8); second-order autodiff + Hessian + Gauss-Newton + Fisher information (ch. 9); **inference as differentiation** in graphical models (ch. 10); **implicit function theorem + adjoint state method + differentiable optimization** (ch. 11); **REINFORCE + reparametrization trick + Gumbel tricks + continuous adjoint for ODEs** (ch. 12); **Legendre-Fenchel transforms + softmax + sparsemax + Fenchel-Young losses** (chs. 13 + 18); SGD + Adam + L-BFGS + natural gradient (chs. 15–17). The wiki's most comprehensive single mathematical-foundation reference; pairs with the [robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md) as the rigorous lookup-reference. (2025-06-24 v3)
- [Helix (Figure AI blog)](sources/helix-blog.md) — Figure AI; hierarchical S1/S2 VLA on Figure 02 humanoid (7B VLM @ 7–9 Hz + 80M transformer @ 200 Hz, end-to-end); ~500h teleop; onboard inference. Vendor blog only. (2025-02)
- [PLDM Paper](sources/pldm-paper.md) — Sobal, Zhang, Cho, Balestriero, Rudner, LeCun (NYU + FAIR; WRL @ ICLR 2025); end-to-end JEPA WM trained with VICReg + inverse-dynamics + similarity loss (~6 anti-collapse hyperparameters); the canonical "end-to-end JEPA before LeWM" baseline. Stress-tested on 23 datasets / 6 generalization properties; only method that doesn't completely fail in any setting. (2025-02-28)
- [Sobal et al. 2022 — JEPA slow features](sources/sobal2022-jepa-slow-features-paper.md) — Sobal, Jyothir S V, Jalagam, Carion, Cho, LeCun (NYU + FAIR; NeurIPS 2022 SSL workshop, arxiv 2211.10831); the PLDM precursor. Establishes that JEPA representations preferentially encode slowly-varying features (like the position of a moving dot); fixed-distractor noise breaks this bias. (2022-11-20)
- [LeJEPA Paper](sources/lejepa-paper.md) — Balestriero & LeCun (Brown + NYU/FAIR, arxiv 2511.08544); the foundational SIGReg paper. Proves isotropic Gaussian is optimal for JEPA embeddings; proposes Sketched Isotropic Gaussian Regularization (SIGReg). Single hyperparameter, no stop-gradient, no teacher-student. ImageNet-1k linear-eval 79% on ViT-H/14; 10+ datasets / 60+ architectures. The methodological precursor to LeWM. (2025-11-11)
- [Welch Labs — Yann LeCun's $1B Bet Against LLMs (video)](sources/welchlabs-lecun-1b-bet-against-llms.md) — 37-min popular-explainer with LeCun interview clips; arc from blurry generative video → Siamese → Barlow Twins → DINO → JEPA / world models; recommended curriculum-orientation video. (2026-05-01)
- [Kona: Energy-Based Models (EBMs) for AI Reasoning — Logical Intelligence page](sources/2026-05-14-logical-intelligence-kona-ebms-page.md) — primary-source [Kona](entities/kona.md) product page; first vendor-authored EBM-for-reasoning positioning in the wiki. Subtitle "Certainty, Not Probability." Verbatim: "It does not predict likely outcomes. It enforces constraints." / "Replaces trust with proof." Links to a live [Sudoku demo](https://sudoku.logicalintelligence.com) with code-execution disabled on both sides. Marketing-light on architecture; no benchmarks. (2026-05-14)
- [Aleph and Energy-Based Models: The AI That Refuses to Bullshit (video)](sources/2026-05-aleph-ebm-refuses-bullshit-video.md) — editorial commentary on [Logical Intelligence](entities/logical-intelligence.md)'s Jan 2026 launch + May 2026 [Aleph](entities/aleph.md) PutnamBench result. Thesis: real reasoning isn't next-token prediction. Aleph + GPT-5.2 hits **99.4% / 668-of-672 on PutnamBench in Lean**, beating ByteDance + Apple. [Kona](entities/kona.md) = non-autoregressive EBM reasoning model under the orchestration. [Yann LeCun](entities/yann-lecun.md) as Founding Chair of Tech Research Board (separate from [AMI Labs](entities/ami-labs.md)); Fields Medalist [Michael Freedman](entities/michael-freedman.md) as Chief of Math. (~2026-05-15)
- [Onchain AI Garage — I Reproduced LeCun's JEPA World Model (video)](sources/onchain-ai-garage-lewm-reproduction.md) — 27-min walk-through reproducing LeWM on Two Room. RTX 3060 / 12 GB VRAM in WSL2, Claude Code as implementation assistant; **92% success vs paper's 97%** after 4 epochs / ~8 hours. First independent LeWM reproduction in the wiki; corroborates the four [LeWM howto](syntheses/world-models/leworldmodel-howto.md) gotchas. Linked from [Curriculum Module 12](syntheses/curriculum/curriculum-12-lewm-deep-dive.md). (2026-04-24)
- [karpathy/autoresearch (GitHub repo)](sources/karpathy-autoresearch.md) — Karpathy's agent-driven LLM training research repo. Single GPU + simplified nanochat + 5-min experiment budget + an AI coding agent that edits `train.py`, runs the experiment, compares val_bpb, and keeps or reverts. Produced two nanochat speedrun-leaderboard improvements (2.02 → 1.65 hours wall-clock). First public evidence that an agent loop can produce measurable gains on a frontier ML training pipeline. Linked from the [LLM-agent architecture](concepts/agents/llm-agent-architecture.md) concept as the non-robotics example of the LLM-emits-tool-calls pattern. (2026-03-06)
- [karpathy/nanochat (GitHub repo)](sources/karpathy-nanochat.md) — Karpathy's full end-to-end ChatGPT pipeline (tokenizer + pretrain + SFT + RL + chat UI) for ~$48 on an 8XH100 node. Single `--depth` complexity dial; "Time-to-GPT-2" speedrun leaderboard. Modern successor to [nanoGPT](sources/karpathy-nanogpt.md); the substrate [autoresearch](sources/karpathy-autoresearch.md) iterates on. Linked from [Curriculum Module 3](syntheses/curriculum/curriculum-03-attention-and-transformers.md). (2025-10-13)
- [karpathy/nanoGPT (GitHub repo)](sources/karpathy-nanogpt.md) — Karpathy's minimal GPT training repo. Two ~300-line files: `model.py` (cleanest decoder-only-transformer reference implementation) + `train.py`. **Deprecated November 2025** in favor of [nanochat](sources/karpathy-nanochat.md), but `model.py` is still the wiki's recommended *architecture-reading* exit-ramp at the bottom of [Curriculum Module 3](syntheses/curriculum/curriculum-03-attention-and-transformers.md). (2022-12-28)
- [karpathy/micrograd (GitHub repo)](sources/karpathy-micrograd.md) — Karpathy's tiny scalar-valued autograd engine (~100 lines) plus a ~50-line PyTorch-style NN library on top. The cleanest "I understand backprop" milestone. Linked from [Curriculum Module 1](syntheses/curriculum/curriculum-01-neural-networks.md). (2020-04-13)
- [NVIDIA Brev Docs](sources/nvidia-brev-docs.md) — NVIDIA's cross-cloud GPU-instance broker (`brev` CLI + Launchables; B200 → P4 catalog). Lifecycle is `Running ⇄ Stopped → Deleted` with hourly billing while running, no compute fees while stopped (capacity-loss risk on restart), and **no native auto-stop / TTL / spend-cap** — `brev stop --all` is the only real cost lever. (2025–2026)
- [Isaac Launchable (isaac-sim/isaac-launchable)](sources/isaac-launchable-repo.md) — NVIDIA's official "try [Isaac Sim](entities/nvidia-isaac-sim.md) + [Isaac Lab](entities/nvidia-isaac-lab.md) in a browser" [Brev](entities/nvidia-brev.md) Launchable (`env-35JP2ywERLgqtD0b0MIeK1HnF46`). VS Code + Isaac Sim 5.1 + Isaac Lab 2.3 + Kit App Streaming. RT-core GPU required (no T4-tier escape); AWS-default; v1.2.1 (Jan 2026); 150★. (ongoing)
- [NVIDIA GEAR Lab — Publications](sources/nvidia-gear-publications.md) — 32 publications (Nov 2022 → Aug 2026) from NVIDIA's Generalist Embodied Agent Research lab ([Jim Fan](entities/jim-fan.md) + [Yuke Zhu](entities/yuke-zhu.md), founded Feb 2024). Five pillars: GR00T humanoid stack, Dream*-world-model line (DreamGen → DreamZero → DreamDojo), Eureka LLM-reward-design, MineDojo/Voyager/NitroGen open-ended agents, and Isaac Lab / RoboCasa / MimicGen / EgoScale data infrastructure. (extracted 2026-05-15)
- [EgoScale Paper](sources/egoscale-paper.md) — NVIDIA GEAR (Zheng, Niu, Xie, ..., Yuke Zhu, Danfei Xu, Jim Fan, Feb 2026). First published VLA pretraining scaling law: `L = 0.024 − 0.003·ln(D)` (R² = 0.9983) on 20,854 hr of egocentric human video — the same corpus underlying GR00T N1.7. Two-stage transfer recipe (large-scale human pretrain + small aligned mid-training) yields +54% over no-pretrain and 88% one-shot shirt folding. (2026-02-18)
- [DreamDojo Paper](sources/dreamdojo-paper.md) — NVIDIA GEAR + Berkeley + HKUST + 6 unis (Gao, Liang, ..., Yuke Zhu, Joel Jang, Jim Fan; Pieter Abbeel + Jitendra Malik on author list; ICML 2026 Spotlight). Foundation generative-video world model pretrained on **44,711 hr** of egocentric human video — the largest WM-pretraining corpus to date. **Continuous latent actions** as unified self-supervised proxy; built on Cosmos-Predict2.5 (2B + 14B variants); **Self-Forcing distillation** to 10.81 FPS real-time. Destination paper of the Dream* triplet (DreamGen → DreamZero → DreamDojo). (2026-02-06)
- [NVIDIA Jetson Orin Nano Dev Kit software setup](sources/nvidia-jetson-orin-nano-devkit-software-setup.md) — official user-guide chapter; SDK Manager flow, FC REC + GND recovery jumper, Ubuntu 20.04 host requirement. (undated)
- [JetPack 6.2.2 release](sources/nvidia-jetpack-6-2-2-release.md) — latest production JetPack 6; bundles Jetson Linux 36.5 + CUDA 12.6.10 + TensorRT 10.3 + DeepStream 7.1 + VPI 3.2; ships first-party AprilTag detector in VPI. (2025)
- [JetPack docs index](sources/nvidia-jetpack-docs-index.md) — canonical JetPack documentation entry-point; lists 6.2.1, lags the developer-site release page. (last updated 2025-06-26)
- [Jetson Linux R36.5 release](sources/nvidia-jetson-linux-r36-5-release.md) — L4T BSP release landing page; Ubuntu 22.04 + kernel 5.15 + UEFI + OP-TEE; covers all production Orin modules and Dev Kits. (2024)
- [Jetson Linux R36.5 update mechanism](sources/nvidia-jetson-linux-r36-5-update-mechanism.md) — apt-based update procedures; point vs minor releases; 35.x→36.x reflash requirement; QSPI bootloader via `nvidia-l4t-bootloader`. (2024)
- [Jetson Linux R36.5 release notes (PDF)](sources/nvidia-jetson-linux-r36-5-release-notes.md) — 17-page official release notes; security-fix-focused minor pairing with JetPack 6.2.2; flash-config table with module part numbers; Super Mode (25W Orin Nano / 40W Orin NX / MAXN); known + fixed issues including the initrd-flash and UEFI-assertion fixes and the CUDA-memory regression. (2026-02 document revision)
- [Platform Power and Performance — Orin series](sources/nvidia-jetson-platform-power-performance-orin.md) — Jetson Linux Developer Guide chapter; defines Super Mode = MAXN_SUPER; per-module nvpmodel tables (Orin Nano 4GB/8GB, Orin NX 8GB/16GB, AGX Orin 32GB/64GB); flash-config lock-in; nvpmodel runtime switching; OC3 87.5% throttle. (undated)
- [NVIDIA Jetson Thor product page](sources/nvidia-jetson-thor-product-page.md) — official Thor specs: T5000 (2560-core Blackwell / 14-core Neoverse-V3AE / 128 GB LPDDR5X / 2070 FP4-sparse TFLOPS / 40–130W) and T4000 (1536-core / 12-core / 64 GB / 1200 FP4-sparse TFLOPS / 40–70W); 7.5× / 3.5× vs Orin. (2025)
- [NVIDIA Blackwell-Powered Jetson Thor Now Available — Newsroom](sources/nvidia-jetson-thor-launch-newsroom.md) — Aug 25 2025 launch; $3,499 dev kit; named adopters: Agility, Amazon Robotics, Boston Dynamics, Caterpillar, Figure, Hexagon, Medtronic, Meta, 1X, John Deere, OpenAI, Physical Intelligence; Jensen "ultimate supercomputer" quote. (2025-08-25)
- [JetPack 7.0 for Jetson Thor software-stack reference](sources/nvidia-jetpack-7-thor-whitepaper.md) — stand-in for the never-published "JetPack 7 whitepaper"; combines NVIDIA's 2025-08-25 forum announcement (Jetson Linux 38.2 / kernel 6.8 / Ubuntu 24.04 / CUDA 13 / TensorRT 10.13 / MIG / real-time kernel / SBSA) with the Oct 2025 7×-generative-AI-throughput blog (NVFP4 + EAGLE-3 specdec; Llama 3.3 70B 41.5→88.62 tok/s). Corrects the wiki's prior R37.x → R38.2 mis-pairing. (2025-08-25 / 2025-10-15)
- [Stretch 4 launch — Hello Robot purchase + product + forum announcement](sources/hello-robot-stretch-4-launch.md) — Hello Robot's [Stretch 4](entities/stretch.md) launch (2026-05-12, $29,950 base). New omnidirectional holonomic base; ~2× faster arm/lift/base; +10% reach; 8 redundant DOF + gripper; dual hemispherical 3D LiDAR (>2M depth readings/sec) + fisheye RGB + 12 MP central + Luxonis OAK-SR wrist; Intel Ultra 5 NUC + optional $2,495 Jetson Orin NX; ROS 2 Jazzy + MuJoCo self-collision avoidance. Generational jump (differential→holonomic base; 7→8 DOF); Stretch-3-trained policies likely need retraining to transfer. (2026-05-12)
- [Stretch 4 Datasheet (Rev 5, As Launched)](sources/hello-robot-stretch-4-datasheet.md) — official Hello Robot spec sheet PDF, two pages. Adds exact sensor SKUs (Hesai J128 LiDAR; Luxonis OAK-FFC AR0234 / IMX378 / OAK-D SR), specific compute (Intel NUC 15 Core Ultra 5 225H + Jetson Orin NX 16 GB / 128 GB), active-safety architecture (motor-current force limiting + 100 Hz watchdog + 6× Pixart cliff curtains + head Runstop), 24 V Feetech RS485 tool bus, environmental ratings (10–30 °C / IP20 / 10–90 % RH), 12-month warranty, and the **"not yet FCC Class A certified"** caveat. Datasheet count: **9 DOF** (including omni base + optional tool) — see [warning callout on Stretch entity](entities/stretch.md) reconciling against the launch page's "8 + gripper" framing. (2026-05-12)
- [PX4 Autopilot Documentation (docs.px4.io/main)](sources/px4-docs-main.md) — top-of-tree summary of the canonical PX4 docs site. BSD-licensed open-source autopilot for drones / autonomous vehicles (Dronecode Foundation / Linux Foundation). v1.16 stable / v1.17 alpha; six vehicle classes; [Pixhawk](entities/pixhawk.md) FMUv3–v6X-RT hardware family; NuttX RTOS + uORB pub-sub + [MAVLink](entities/mavlink.md) + ROS 2 / uXRCE-DDS bridge. Notable for the wiki: **dedicated Neural Networks subsystem** (TensorFlow Lite Micro, RAPTOR Adaptive RL NN Module, MC NN Control), Jetson companion-computer carriers, and direct overlap with the wiki's [agentic UAVs concept](concepts/robotics/agentic-uavs.md) + [MIT drone adaptive control](sources/mit-drone-adaptive-control.md). (continuously updated)
- [NVIDIA DGX Spark Hardware Overview](sources/nvidia-dgx-spark-hardware-overview.md) — official GB10 Grace Blackwell spec: 20-core ARM (10× X925 + 10× A725), 6144-CUDA-core Blackwell with **4th-gen RT Cores**, 128 GB LPDDR5X **unified** at 273 GB/s, ConnectX-7, up to 1 PFLOP FP4 sparse, up to 200B-param inference (405B paired). (2025)
- [Isaac Sim and Isaac Lab on NVIDIA Jetson AGX Thor — RS DesignSpark](sources/rs-designspark-isaac-sim-on-thor.md) — the authoritative explainer on Thor's no-RT-cores constraint; Isaac Sim/Lab cannot run on Thor even headless; NVIDIA's prescribed train-on-Spark / deploy-on-Thor workflow. (2025)
- [DROID Paper](sources/droid-paper.md) — Khazatsky, Pertsch, Finn, Levine, +97 (2024-04). 76k trajectories / 350 hr / 564 scenes / 84 tasks; standardized Franka platform; scene-diversity-over-embodiment-diversity design. CC BY 4.0. (2024-04)
- [Metaworld Paper](sources/metaworld-paper.md) — Yu, Quillen, ..., Hausman, Finn, Levine (CoRL 2019). 50-task manipulation benchmark for meta-RL / multi-task RL; ML10/ML45/MT10/MT50 splits; the surprising result: even 10 tasks defeats SOTA multi-task RL. (2019-10)
- [DINOv2 Paper](sources/dinov2-paper.md) — Oquab, Darcet, ..., Bojanowski (Meta FAIR, 2023). LVD-142M curated SSL dataset; ViT-1B teacher distilled to ViT-S/B/L/g; surpasses OpenCLIP at image + pixel levels; substrate for the DINO-line robotics literature. (2023-04)
- [Dobb·E Paper](sources/dobb-e-paper.md) — Shafiullah, Rai, Etukuru, ..., Chintala, Pinto (NYU, 2023-11). The Stick + Homes-of-New-York + HPR encoder; 81% success on 109 tasks across 10 homes with 5 min demo + 15 min adaptation. CC-BY-4.0. Direct precursor to RUM. (2023-11)
- [VQ-BeT Paper](sources/vq-bet-paper.md) — Lee, Wang, Etukuru, Kim, Shafiullah, Pinto (ICML 2024). Hierarchical VQ codebook replaces BET's k-means action clustering; ~5× faster inference than Diffusion Policy across 7 environments. (2024-03)
- [LeRobot ICLR 2026 paper](sources/lerobot-iclr-2026-paper.md) — [Cadene](entities/remi-cadene.md), Aliberts, Capuano, …, Wolf (17 [Hugging Face](entities/hugging-face.md) authors; arxiv 2602.22818; ICLR 2026). **The canonical academic reference for the [LeRobot](entities/lerobot.md) framework.** Vertically-integrated stack: unified middleware across 8 platforms ([SO-100/101](entities/so-arm101.md), Koch-v1.1, [ALOHA-2](entities/aloha.md), [HopeJR-Arm](entities/hope-jr-arm.md), [LeKiwi](entities/lekiwi.md), [Stretch-3](entities/stretch.md), [Reachy-2](entities/reachy.md)); `LeRobotDataset` format (**16K+ datasets from 2.2K+ contributors as of Sep 2025**); async producer-consumer inference stack with physical + logical decoupling; PyTorch implementations of [ACT](entities/act.md), [Diffusion Policy](entities/diffusion-policy.md), [VQ-BET](entities/vq-bet.md), HIL-SERL, [TD-MPC](entities/td-mpc.md), [π0](entities/pi-zero.md), [SmolVLA](entities/smolvla.md); native [LIBERO](entities/libero.md) + [Metaworld](entities/metaworld.md) eval integration. Compute-footprint tables: ACT 52M (5 ms RTX 4090) → π0 3.5B (13.32 GB A100; CPU-incompatible). Async SmolVLA on SO-100 doubles throughput vs sync (1.8 → 3.8 cubes/60s) with similar success. (2026-02-26)
- [Rosetta GitHub (iblnkn/rosetta)](sources/rosetta-github.md) — solo-author Apache-2.0 framework "LeRobot for ROS2 Robots" (76 stars / 14 forks / last push 2026-05-24; created Sep 2025). YAML-contract approach maps ROS 2 topics to LeRobot features declaratively — no Python driver class required. 5-step pipeline (Define → Record → Convert → Train → Deploy); 5 packages (`rosetta`, `rosetta_interfaces`, `lerobot_robot_rosetta`, `lerobot_teleoperator_rosetta`, `rosetta_rl` coming soon); MCAP rosbag2 storage; gRPC async policy server. Reference contracts ship for [SO-101](entities/so-arm101.md) (multi-cam manipulator), SO-101+HIL (intervention buttons + reward), and [TurtleBot3](entities/turtlebot.md) Waffle (wheeled mobile base, 20-dim state from JointState + IMU + Odometry). Supports a superset of upstream LeRobot's policy menu: ACT, [SmolVLA](entities/smolvla.md), [π0](entities/pi-zero.md), π0.5, [GR00T](entities/nvidia-groot.md), Wall-X, X-VLA. **Directly resolves the LeRobot↔ROS 2 gap** identified in the [LeRobot-on-ROSOrin-Pro synthesis](syntheses/projects/lerobot-on-rosorin-pro.md). (2025-09-14 created; 2026-05-24 last push)
- [lerobot-ros GitHub (ycheng517/lerobot-ros)](sources/lerobot-ros-github.md) — generic Python-class-based LeRobot↔[ROS 2](entities/ros2.md) wrapper (**194 stars / 28 forks**, the most-popular of the 3 bridges; no license listed). ROS 2 **Jazzy only**; minimal 2-package architecture; 3 control modes (joint position / joint trajectory / EE velocity via MoveIt Servo); gamepad + keyboard teleop. Add a new robot in ~30 lines (sub-class `ROS2Robot` + `ROS2Config`). Quickstart uses simulated [SO-101](entities/so-arm101.md) in Gazebo. Last push Nov 2025 — momentum slowing relative to [Rosetta](entities/rosetta.md). (2025-07-27 created)
- [so101_ros2 readthedocs (nimiCurtis/so101_ros2)](sources/so101-ros2-readthedocs.md) — MIT-licensed SO-101-specific ROS 2 workspace + LeRobot bridge (50 stars / 8 forks). ROS 2 **Humble** only; Python 3.10+; **8-package full workspace** (URDF/USD, hardware interface, controllers, bringup, teleop, bridge); **Isaac Sim 5.0+ integration** (unique among the 3 bridges); tested deployment of SmolVLA + π0.5. Dedicated readthedocs documentation site. Operational cost: 2 conda envs + dependency on the author's [`nimiCurtis/lerobot`](https://github.com/nimiCurtis/lerobot) fork rather than upstream LeRobot. (2025-06-12 created; v0.1.1 released 2025-12-13)
- [ROS 2 Humble docs](sources/ros2-humble-docs.md) — official documentation for the LTS distribution most commonly used as an integration target in robotics 2024–2026. Released 2022-05-23, EOL May 2027; 5-year LTS cadence; new ROS 2 distribution every May 23rd (World Turtle Day). Current distros: Lyrical Luth (May 2026), Kilted Kaiju (non-LTS), Jazzy Jalisco (LTS, May 2024 / EOL May 2029), Humble Hawksbill (LTS). Cross-distro communication not guaranteed. **Operationally load-bearing for LeRobot↔ROS 2 bridge selection** ([Rosetta](entities/rosetta.md) distro-agnostic; [lerobot-ros](entities/lerobot-ros.md) Jazzy-only; [so101-ros2](entities/so101-ros2.md) Humble-only).

## Sources (pedagogical / curriculum companions, undated)
- [Welch Labs Illustrated Guide to AI, Vol I (book)](sources/welchlabs-illustrated-guide-to-ai.md) — Stephen Welch's 376-page illustrated textbook (Feb 2026, Revision V15). 9 chapters: perceptron → gradient descent → backprop → deep learning → AlexNet → **neural scaling laws** → **mechanistic interpretability** → **attention (DeepSeek MLA)** → diffusion. Pairs chapter-by-chapter with Welch Labs YouTube videos; code at github.com/stephencwelch/ai_book. **The wiki's first ingested primary source on LLM-side scaling laws, mech-interp, and DeepSeek MLA.** (2026-02)
- [Welch Labs — The Perceptron (YouTube, Feb 2025)](sources/welchlabs-perceptron.md) — "ChatGPT is made from 100 million of these." Stephen Welch's pedagogical prequel to the [LeCun $1B Bet video](sources/welchlabs-lecun-1b-bet-against-llms.md); also the video companion to **Ch 1** of [the Illustrated Guide](sources/welchlabs-illustrated-guide-to-ai.md). Rosenblatt 1957 → Mark I (1958) → XOR roadblock (Minsky & Papert 1969) → backprop (Rumelhart/Hinton/Williams 1986) → MLP-at-scale (GPT-3). Recommended-viewing for [Curriculum Module 1](syntheses/curriculum/curriculum-01-neural-networks.md). (2025-02)
- [3Blue1Brown — How might LLMs store facts | Deep Learning Chapter 7](sources/3blue1brown-mlp-in-llms.md) — Grant Sanderson; the MLP / FFN block inside a transformer LLM as a key–value fact-lookup mechanism. Covers up/down projection, ReLU, superposition (Johnson–Lindenstrauss), and the "~2/3 of GPT-3's parameters live in MLPs" arithmetic. Foundation for the interpretability / SAE-feature-decomposition program. Recommended-viewing for [Curriculum Module 3](syntheses/curriculum/curriculum-03-attention-and-transformers.md). (2024-08-31)
- [fast.ai — Practical Deep Learning for Coders 2022](sources/fastai-practical-deep-learning.md) — Jeremy Howard; 9-lesson, library-first PyTorch + fastai + Hugging Face Transformers + Gradio onboarding. Strongest "first-touch" pedagogical companion *before* [Curriculum Module 1](syntheses/curriculum/curriculum-01-neural-networks.md) for readers without a year of DL programming. (2022)
- [Cameron R. Wolfe — Understanding and Using SFT for Language Models](sources/wolfe-sft-blog.md) — *Deep (Learning) Focus* Substack, Sep 2023. Three-stage alignment (Pretrain → SFT → RLHF); LIMA's "1,000 examples sufficient" finding; survey of LLaMA-2 / Falcon / MPT / Alpaca / Vicuna / Orca / WizardLM. The theory-side companion to [HF TRL SFT Trainer docs](sources/huggingface-trl-sft-trainer.md). (2023-09-11)
- [Hugging Face TRL — SFT Trainer documentation](sources/huggingface-trl-sft-trainer.md) — the de-facto SFT trainer for LLMs and VLMs in 2026. One-line API; dataset-format dispatch; chat-template auto-application; PEFT/LoRA, Liger Kernel, Unsloth, RapidFire AI integrations; VLM support (Qwen2.5-VL, LLaVA-Instruct-Mix); tool-calling SFT. The implementation companion every wiki-tracked VLA fine-tuning recipe builds on top of. (continuously updated)
- [DS4DS 7.01 — Optimal Control, Introduction (Peitz & Wallscheid)](sources/ds4ds-7-01-optimal-control-intro.md) — Data Science for Dynamical Systems open course (CC BY-SA 4.0; Julia / Jupyter), YouTube Jan 2024. Opening lecture of the 7-lesson module 7 (intro → discrete-time → LQR → LMPC → data-driven MPC via DMD → differential predictive control). The modern-pedagogy companion to [Sussmann & Willems 1997](sources/sussmann-willems-1997-300-years-optimal-control.md) — together they form a complete optimal-control orientation. (2024-01-21)

## Sources (foundational, out of chronological order)
- [Sussmann & Willems 1997 — 300 Years of Optimal Control: From the Brachystochrone to the Maximum Principle](sources/sussmann-willems-1997-300-years-optimal-control.md) — Rutgers / Groningen; IEEE Control Systems Magazine "Historical Perspectives," June 1997. Tercentenary essay arguing optimal control was born in 1697 with Bernoulli's brachystochrone solution — not in 1956 with Pontryagin. Distinguishes OC ⊋ CoV: dynamical constraints `q̇ = f(q, u, t)` + control-set constraints `u ∈ U` are the structural additions. Walks the canonical chain Bernoulli → Euler–Lagrange → Hamilton → Jacobi → Weierstrass → Pontryagin's Maximum Principle. The wiki's primary-source anchor for the optimal-control machinery underneath MPC / CEM / TD-MPC / learned-world-model planning. (1997-06)
- [Barlow 1961 — Possible Principles Underlying the Transformations of Sensory Messages](sources/barlow1961-sensory-messages.md) — Horace Barlow's foundational neuroscience paper introducing the redundancy-reduction principle (recode redundant sensory input into a factorial code with statistically independent components). Eponymous source for Barlow Twins (2021). The lineage root for VICReg → SIGReg → DINOv3 Gram anchoring. (1961)
- [Bromley, Guyon, LeCun, Säckinger, Shah 1993 — Signature Verification using a "Siamese" Time Delay Neural Network](sources/bromley1993-siamese-signature-verification.md) — original Siamese network paper, AT&T Bell Labs / NIPS 1993. Two weight-tied TDNN sub-networks + cosine + `±1` targets for genuine vs forgery pairs. The architectural ancestor of every joint-embedding SSL system: Barlow Twins, VICReg, DINOv2/v3, and the J/A in [JEPA](concepts/world-models/jepa.md). LeCun's 1990s precursor to his 2020s JEPA program — same author, same architectural family, different loss. (1993)
- [Vaswani et al. 2017 — Attention Is All You Need](sources/attention-is-all-you-need.md) — the Transformer paper. NeurIPS 2017; Google Brain / Google Research. Sequence transduction built entirely on attention, no recurrence, no convolution. Encoder–decoder, multi-head scaled dot-product attention, sinusoidal positional encoding, `h=8`, `d_model=512`, `N=6`. 28.4 BLEU EN-DE / 41.8 BLEU EN-FR. The foundation of every modern architecture downstream: LLMs, ViTs, VLA action heads, JEPA predictors, BeT / VQ-BeT policies, Diffusion Policy transformer backbones. (2017-06-12)
- [Dosovitskiy et al. 2020 — An Image Is Worth 16x16 Words (ViT)](sources/vit-paper.md) — the Vision Transformer paper. ICLR 2021; Google Research, Brain Team. Patch tokenization + learned positional embedding + `[CLS]` token + standard transformer encoder = first pure-attention vision model. Pre-trained on JFT-300M, ViT-H/14 hits 88.55% ImageNet top-1 at 2–4× less compute than BiT-L / Noisy Student. Central claim: **at scale, data trumps inductive bias.** The backbone underneath every ViT-encoder in this wiki — DINOv2, DINOv3, V-JEPA 2, LeWM, DINO-WM, DINO-world, JEPA-WMs, LeJEPA, PLDM. (2020-10-22)
- [Sutton & Barto — Reinforcement Learning: An Introduction (2nd ed., MIT Press 2018 / 2020 reprint)](sources/sutton-barto-rl-textbook.md) — UMass / UAlberta / DeepMind; A Bradford / MIT Press; ISBN 9780262039246; CC BY-NC-ND 2.0 electronic. The canonical RL textbook (548 pp). Defines the field's four-subelement decomposition (policy / reward / value function / model) and the unifying narrative MC ↔ TD ↔ DP via Bellman bootstrapping. **Ch 13 (Policy Gradient Methods)** is the lineage of REINFORCE → Actor-Critic → PPO / SAC / GRPO. **Ch 16 (Applications)** covers DQN/Atari (Mnih 2015) + AlphaGo/AlphaGo Zero (Silver 2016/2017). **Ch 11 (Deadly Triad)** is the cleanest theoretical diagnosis of why deep-RL training is fragile. The primary-source anchor for [Module 8 — RL vocabulary](syntheses/curriculum/curriculum-08-rl-vocabulary.md), every MBRL paper ([DreamerV3](sources/dreamer-v3-paper.md), [TD-MPC2](sources/td-mpc2-paper.md)), every learned-WM thread, and the RLHF/DPO/GRPO line underneath every VLA. The "RL = approximate optimal control under uncertainty" bridge to [Sussmann & Willems 1997](sources/sussmann-willems-1997-300-years-optimal-control.md). Sutton + Barto won the 2024 Turing Award for the work consolidated in this book. (2018 final 2nd ed.; 2014–2015 in-progress draft also on file for historical reference)
- [Barlow Twins Paper](sources/barlow-twins-paper.md) — Zbontar, Jing, Misra, LeCun, Deny (FAIR + NYU; ICML 2021, arxiv 2103.03230). First non-asymmetric anti-collapse SSL method: cross-correlation between two augmented views' embeddings → identity. No predictor, no momentum encoder, no stop-gradient. ImageNet linear top-1 73.2%. Names itself after Horace Barlow's redundancy-reduction principle. (2021-03-04)
- [VICReg Paper](sources/vicreg-paper.md) — Bardes, Ponce, LeCun (FAIR + Inria + NYU; ICLR 2022, arxiv 2105.04906). Three-term anti-collapse loss: variance hinge + covariance decorrelation + invariance MSE. Branches need not share weights or architecture — natural multi-modal SSL. The regularizer LeCun's AMI paper cites by name as the JEPA anti-collapse method; methodological precursor to SIGReg / LeJEPA. (2021-05-11)
- [LeCun 2022 — A Path Towards Autonomous Machine Intelligence](sources/lecun2022-path-towards-ami.md) — LeCun's position paper. Defines the JEPA / H-JEPA architecture, the configurable world model + configurator framing, intrinsic-cost + critic, and the EBM training story behind all subsequent JEPA papers. The vision document AMI Labs was founded to execute. (2022-06-27)
- [DINOv3 Paper](sources/dinov3-paper.md) — Siméoni et al., Meta AI Research (arxiv 2508.10104). 7B-parameter ViT SSL foundation model; introduces Gram anchoring (regularize patch-similarity structure toward an earlier "Gram teacher") to fix the long-training dense-feature degradation observed in DINOv2 at scale. Frozen-backbone COCO mAP 66.1; ADE20k mIoU 63.0. New SSL state-of-the-art and natural drop-in upgrade for the DINO-WM / DINO-world / JEPA-WMs lineage. (2025-08-13)

## Entities

### Companies
- [NVIDIA](entities/nvidia.md) — owns most of the agentic-robotics simulation substrate; also owns [Brev](entities/nvidia-brev.md) GPU-cloud broker and the in-house [GEAR](entities/nvidia-gear.md) research lab. (19 sources)
- [NVIDIA GEAR](entities/nvidia-gear.md) — Generalist Embodied Agent Research; co-led by [Jim Fan](entities/jim-fan.md) + [Yuke Zhu](entities/yuke-zhu.md); founded Feb 2024; source of GR00T, the Dream*-WM line, Eureka, and much of the Isaac Lab / RoboCasa / MimicGen substrate. (3 sources)
- [Hiwonder](entities/hiwonder.md) — Chinese educational-robotics vendor; ROSOrin / ROSOrin Pro kits + OpenClaw. (3 sources)
- [Hugging Face](entities/hugging-face.md) — open-source AI company; maintainer of [LeRobot](entities/lerobot.md); HF Hub hosts model checkpoints across the wiki's JEPA / VLA / IL coverage. (5 sources)
- [SIGRobotics-UIUC](entities/sigrobotics-uiuc.md) — student-led robotics org at UIUC; designs and maintains [LeKiwi](entities/lekiwi.md); won U.S. site of the Oct 2025 Embodied AI Hackathon with a GR00T-driven matcha-making XLeRobot; sponsored by FrodoBots / Hugging Face / K-Scale Labs / Neuralink / ROBOTIS / others. (4 sources)
- [Seeed Studio](entities/seeed-studio.md) — Shenzhen open-hardware distributor; sells LeKiwi and hosts the canonical end-user tutorial; co-organizer of LeRobot 2025 + Embodied AI 2025 hackathons. (3 sources)
- [The Robot Studio](entities/the-robot-studio.md) — open-hardware design group behind **both** the SO-ARM100/101 lineage **and** the HopeJR humanoid arm (confirmed via [LeRobot ICLR 2026 paper](sources/lerobot-iclr-2026-paper.md) Appendix A). (4 sources)
- [AGIBOT](entities/agibot.md) — Shanghai embodied-AI / humanoid company. Open-source-heavy. (3 sources)
- [Hello Robot](entities/hello-robot.md) — Stretch mobile manipulator + stretch_ai stack. (7 sources)
- [HCR Lab](entities/hcrlab.md) — Human-Centered Robotics Lab, UW (Maya Cakmak); assistive robots + EUP; Stretch platform; long-term in-home deployments. (9 sources)
- [Elephant Robotics](entities/elephant-robotics.md) — Chinese edu-robotics vendor; myAGV + myBuddy 280 + arm ecosystem. (2 sources)
- [Pollen Robotics](entities/pollen-robotics.md) — French open-source humanoid maker; Reachy 2. (1 source)
- [Fauna Robotics](entities/fauna-robotics.md) — NYC; Sprout Creator Edition; 107cm, 29 DOF, Jetson AGX Orin. (1 source)
- [K-Scale Labs](entities/k-scale-labs.md) — YC humanoid startup; shut down late 2025; notable post-mortem; was Embodied AI Hackathon mentor + SIGRobotics-UIUC "Mini Humanoid" project sponsor. (3 sources)
- [Welch Labs](entities/welch-labs.md) — independent AI-pedagogy operation (Stephen Welch). YouTube channel + the Feb 2026 *Illustrated Guide to AI* book + GitHub code. One of the wiki's three canonical pedagogy publishers alongside Sutton & Barto and 3Blue1Brown. (3 sources)
- [Meta FAIR](entities/meta-fair.md) — Yann LeCun's lab; JEPA research line. (11 sources)
- [Google DeepMind](entities/google-deepmind.md) — MuJoCo, Newton co-development, MjcPhysics USD plugin, Gemini Robotics. (7 sources)
- [Boston Dynamics](entities/boston-dynamics.md) — robotics company (Hyundai-owned); Spot + Atlas + Stretch + Orbit + AIVI-Learning. (1 source)
- [Mila](entities/mila.md) — Quebec AI Institute; frequent JEPA collaborator. (4 sources) _stub_
- [Farama Foundation](entities/farama-foundation.md) — non-profit; took over OpenAI gym → Gymnasium; 19 RL projects. (3 sources)
- [Dronecode Foundation](entities/dronecode-foundation.md) — non-profit (Linux Foundation Collaborative Project); steward of PX4, MAVLink, Pixhawk, QGroundControl, MAVSDK. (1 source)
- [AMI Labs](entities/ami-labs.md) — Yann LeCun's reported post-Meta AI lab; $1.03B seed round (single secondary source, provisional). (1 source)
- [Logical Intelligence](entities/logical-intelligence.md) — commercializes [energy-based reasoning models](concepts/learning/energy-based-models.md) for critical systems; Eve Bodnia CEO, [Yann LeCun](entities/yann-lecun.md) Founding Chair of Tech Research Board, [Michael Freedman](entities/michael-freedman.md) Chief of Math. Products: [Aleph](entities/aleph.md) (formal-verification agent) + [Kona](entities/kona.md) (EBM reasoning model). Distinct from AMI Labs. (1 source)
- [Anthropic](entities/anthropic.md) — developer of Claude; AI safety mission; author of Claude's Constitution; MCP protocol. (2 sources)
- [Apollo Research](entities/apollo-research.md) — independent AI safety evaluation institute; red-teamed Claude Opus 4 (2025). (2 sources)
- [Physical Intelligence](entities/physical-intelligence.md) — San Francisco; π-series (π0 / π0.5 / π0.6 / π0.6-MEM / π0.7 / π*0.6) cross-platform generalist VLAs. (5 sources)
- [Hillbot](entities/hillbot.md) — UCSD spinoff that maintains ManiSkill. (1 source) _stub_
- [Disney Research](entities/disney-research.md) — Newton co-developer with NVIDIA + DeepMind. (2 sources) _stub_
- [FIRST Robotics Competition](entities/first-robotics-competition.md) — world's leading high-school robotics competition; ~3,700 teams, 30+ countries. (4 sources)
- [AndyMark](entities/andymark.md) — major FRC vendor; AM14U6 chassis, field elements, FUEL scoring elements. (2 sources)
- [Team 254: The Cheesy Poofs](entities/team-254.md) — elite FRC team (2022 World Champions); 2026 "AI in FRC" presentation; Claude Code + wpilib-agent-tools. (2 sources)
- [HHMI Janelia Research Campus](entities/hhmi-janelia.md) — HHMI's pure-research lab; Turaga lab leads flybody + flyvis; *Drosophila* neuroscience & connectomics anchor. (3 sources)
- [NeLy-EPFL (Neuroengineering Laboratory)](entities/nely-epfl.md) — EPFL lab; maintains [NeuroMechFly](entities/neuromechfly.md) + the `flygym` Python library; European counterweight to HHMI Janelia in fly-body simulation. (3 sources)
- [Toyota Research Institute (TRI)](entities/tri.md) — Toyota's R&D arm; Los Altos + Cambridge; co-affiliation across [Diffusion Policy](entities/diffusion-policy.md) + [UMI](entities/umi.md); home of TRI LBM. (2 sources)

### Simulators / frameworks
- [NVIDIA Isaac Sim](entities/nvidia-isaac-sim.md) — Omniverse-based robotics simulator. (6 sources)
- [NVIDIA Isaac Lab](entities/nvidia-isaac-lab.md) — open-source learning framework on Isaac Sim; primary reference paper is [GEAR](entities/nvidia-gear.md)-authored (arXiv 2511.04831). (7 sources)
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
- [Metaworld](entities/metaworld.md) — Stanford/Berkeley meta-RL benchmark; 50 manipulation tasks on simulated Sawyer; staple across V-JEPA-line work; natively integrated in LeRobot. (4 sources)
- [PushT](entities/pusht.md) — 2D T-block pushing benchmark; introduced by IBC, popularized by Diffusion Policy; default lightweight bench across LeWM / DINO-WM / JEPA-WMs. (5 sources)
- [PointMaze](entities/pointmaze.md) — 2D point-mass maze navigation; default lightweight nav bench across LeWM / DINO-WM / JEPA-WMs. (3 sources)
- [DM Control Suite](entities/dm-control.md) — DeepMind continuous-control RL benchmark on top of MuJoCo; pre-Gymnasium-Robotics legacy substrate. (4 sources)
- [LIBERO](entities/libero.md) — lifelong-learning manipulation benchmark (Liu et al. NeurIPS 2023); de-facto VLA-eval bench (SPATIAL / OBJECT / GOAL / 90 / LONG task families); natively integrated in LeRobot. (2 sources)
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
- [Sharpa Wave hand](entities/sharpa-wave.md) — 22-DoF anthropomorphic dexterous hand; primary post-training target on Galaxea R1Pro in [EgoScale](sources/egoscale-paper.md). Joint-space control. (1 source) _stub_
- [TurtleBot](entities/turtlebot.md) — canonical educational ROS mobile robot (4 generations); TurtleBot 4 in education, TurtleBot 2i used in DRAGON 2024 assistive navigation; Rosetta ships `turtlebot3.yaml` as the reference mobile-base contract. (3 sources)
- [iRobot Create 3](entities/irobot-create-3.md) — Roomba-i3-derived ROS 2 mobile-robot base; chassis under [TurtleBot 4](entities/turtlebot.md). (1 source) _stub_
- [Tiago](entities/tiago.md) — PAL Robotics dual-arm mobile manipulator; ROS-native; used in Huh et al. 2026 accessibility study. (1 source)

### Humanoids
- [Atlas](entities/atlas.md) — Boston Dynamics flagship; closed development; capability-bar humanoid. (1 source) _stub_
- [Fourier GR-1](entities/fourier-gr-1.md) — Fourier Intelligence humanoid; primary OOD eval target across all four [DreamDojo](sources/dreamdojo-paper.md) benchmarks; one of four robot embodiments in DreamDojo's latent-action training. (1 source) _stub_
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
- [Stretch](entities/stretch.md) — Hello Robot's mobile manipulator (Stretch 3 / Stretch 4). De-facto research platform; natively supported in LeRobot. (16 sources)
- [Mobile ALOHA](entities/aloha.md) — Stanford bimanual mobile manipulator with whole-body teleop; 4× [ViperX 300](entities/viperx-300.md) + AgileX Tracer base; $32k incl. onboard compute + power; the [ACT](entities/act.md) + co-training-with-static-data reference; ALOHA-2 is in LeRobot's 8 supported platforms (~€21k). (3 sources)
- [Trossen ViperX 300](entities/viperx-300.md) — 6-DOF benchtop arm; the bimanual-teleop SKU underneath [ALOHA / Mobile ALOHA](entities/aloha.md). (1 source)
- [Grievous](entities/grievous.md) — Alex Koven's WIP cheap-bimanual-mobile testbed; design based on [Mobile ALOHA](entities/aloha.md) + [XLeRobot](entities/xlerobot.md); software on [LeRobot](entities/lerobot.md); RPi5-host + remote-PC. First downstream-of-Mobile-ALOHA project ingested here. (1 source) _stub_
- [Reachy 2](entities/reachy.md) — Pollen Robotics' open-source bimanual mobile manipulator for embodied AI; ROS 2; 7 DOF/arm; natively supported in LeRobot. (2 sources)
- [myAGV](entities/myagv.md) — Elephant Robotics autonomous mobile base; ROS; Raspberry Pi 4B; pairs with arms. (1 source)
- [LeKiwi](entities/lekiwi.md) — SIGRobotics-UIUC 3-wheel Kiwi-drive holonomic mobile manipulator; Raspberry Pi 5 + STS3215; sub-$1k; LeRobot ecosystem; 1,300+ stars; ICLR 2026 paper lists at ~€230. (7 sources)
- [XLeRobot](entities/xlerobot.md) — Vector Wang's $660 dual-arm household manipulator (2× SO-ARM101 + LeKiwi base + LeRobot); 90% 3D-printed; v0.3.0 (Aug 2025); 2 winning teams at Oct 2025 Embodied AI Hackathon (incl. matcha-bot champion). (2 sources)
- [SO-ARM101](entities/so-arm101.md) — open-source low-cost arm (The Robot Studio); SO-ARM100 successor; default LeRobot manipulator; SO-10X drives 50%+ of community-contributed LeRobotDatasets as of Sep 2025; **most-tooled platform in the LeRobot↔ROS 2 ecosystem** — reference robot for all 3 bridges (Rosetta `so_101.yaml`, lerobot-ros quickstart, dedicated so101_ros2 workspace). (9 sources)
- [HopeJR-Arm](entities/hope-jr-arm.md) — humanoid arm + hand from [The Robot Studio](entities/the-robot-studio.md); ~€500; one of 8 LeRobot-supported platforms; BOM in TheRobotStudio/HOPEJr repo. (2 sources)
- [myBuddy 280](entities/mybuddy-280.md) — Elephant Robotics 13 DOF dual-arm desktop robot; $1,619; ROS1. (1 source)
- [ROSOrin](entities/rosorin.md) — Hiwonder's Jetson Orin Nano educational mobile robot kit. (2 sources)
- [ROSOrin Pro](entities/rosorin-pro.md) — Hiwonder's 6-DOF arm + base variant of ROSOrin. (2 sources)
- [ROSOrin Pro 6-DOF arm](entities/rosorin-pro-arm.md) — HX-12H-servo manipulator on the ROSOrin Pro kit. (2 sources)
- [FRC KitBot](entities/frc-kitbot.md) — beginner-friendly FRC robot on AndyMark AM14U6 chassis; included in Kickoff Kit. (2 sources)

### Software stacks
- [stretch_ai](entities/stretch-ai.md) — Hello Robot's open-source Python stack with an LLM agent. (5 sources)
- [OpenClaw](entities/openclaw.md) — Hiwonder's manipulation-aware LLM-agent framework for ROSOrin Pro. (1 source)
- [LeRobot](entities/lerobot.md) — Hugging Face's open-source **end-to-end robot learning library** ([ICLR 2026](sources/lerobot-iclr-2026-paper.md)); 8 platforms; 16K+ datasets / 2.2K+ contributors (Sep 2025); async producer-consumer inference; reference RL + BC + VLA implementations; 916-team Worldwide Hackathon in June 2025; **three independent community ROS 2 bridges** (Rosetta / lerobot-ros / so101-ros2). (12 sources)
- [Rosetta](entities/rosetta.md) — solo-author Apache-2.0 bridge from [LeRobot](entities/lerobot.md) to [ROS 2](entities/ros2.md) (76 stars, Sep 2025); YAML-contract-driven topic-to-LeRobot-feature mapping; ships SO-101 + TurtleBot3 reference contracts + experimental HIL support; extends supported policies with π0.5, GR00T, Wall-X, X-VLA. Distro-agnostic; best fit for non-arm or non-Jazzy ROS 2 robots. (1 source)
- [lerobot-ros](entities/lerobot-ros.md) — generic Python-class-based LeRobot↔ROS 2 wrapper by ycheng517 (**194 stars**, the most popular of 3 bridges; Jul 2025); Jazzy only; ros2_control + MoveIt Servo; minimal 2-package architecture; no license listed; arm-focused. (1 source)
- [so101-ros2](entities/so101-ros2.md) — SO-101-specific MIT-licensed ROS 2 workspace + LeRobot bridge by nimiCurtis (50 stars, Jun 2025); Humble only; 8 packages incl. URDF/USD + Isaac Sim 5.0+ integration; tested SmolVLA + π0.5 deployment; needs author's LeRobot fork. (1 source)
- [ROS 2](entities/ros2.md) — Open Robotics' middleware framework; LTS distros Humble (2022, EOL May 2027) + Jazzy (2024, EOL May 2029); operationally load-bearing for LeRobot↔ROS 2 bridge selection. (1 source)
- [PX4 Autopilot](entities/px4-autopilot.md) — Dronecode Foundation's BSD-licensed open-source autopilot for UAVs / drones (multirotor / fixed-wing / VTOL / heli / rover / experimental); NuttX RTOS + uORB + MAVLink + ROS 2 bridge; v1.16 stable, v1.17 alpha; first-class Neural Networks subsystem (TFLM + RAPTOR Adaptive RL + MC NN Control). (1 source)
- [JetPack SDK](entities/jetpack.md) — NVIDIA's bundled software stack for Jetson products; Jetson Linux + CUDA + cuDNN + TensorRT + DeepStream + VPI + DLA. Current production 6.2.2. (4 sources)
- [Jetson Linux (L4T)](entities/jetson-linux.md) — the L4T BSP underneath JetPack; R36.5 current for Orin (Ubuntu 22.04 + kernel 5.15 + UEFI + OP-TEE). (3 sources)

### Controllers / edge AI compute
- [roboRIO](entities/roborio.md) — NI's mandatory FRC robot controller (ARM Cortex-A9 + FPGA); WPILib ecosystem. (2 sources)
- [Jetson Orin Nano](entities/jetson-orin-nano.md) — NVIDIA's entry-tier Ampere-GPU edge-AI module + Developer Kit; substrate for ROSOrin / ROSOrin Pro / many wiki-tracked educational robots. (6 sources)
- [Jetson Thor](entities/jetson-thor.md) — NVIDIA's Blackwell-generation flagship on-robot compute (T5000 + T4000 + AGX Thor Dev Kit); 7.5× / 3.5× vs Orin; **no RT cores → can't host Isaac Sim**. (4 sources)
- [NVIDIA DGX Spark](entities/dgx-spark.md) — GB10 Grace Blackwell desktop AI supercomputer; 128 GB unified memory, 4th-gen RT cores, ConnectX-7; train-on-Spark / deploy-on-Thor split. (1 source)
- [stable-worldmodel](entities/stable-worldmodel.md) — Python infrastructure under LeWorldModel (env zoo + planning API + dataset format). DM Control + Gymnasium-Robotics Fetch + classic + OGBench + more. (0 sources)
- [Pixhawk](entities/pixhawk.md) — open-hardware flight-controller standard (Dronecode); FMUv3–v6X-RT family; 30+ manufacturer-supported boards (Holybro, CUAV, CubePilot, ARK, ModalAI); the dominant hardware target for PX4. (1 source)

### Formats / standards
- [OpenUSD](entities/openusd.md) — open scene-description + robotics physics-schema layer (UsdPhysics, MjcPhysics, NewtonSceneAPI). (5 sources)
- [MAVLink](entities/mavlink.md) — lightweight binary telemetry / command protocol for drones (Dronecode); spoken by PX4 + ArduPilot + QGroundControl + MAVSDK + MAVROS. (1 source)

### Datasets
- [DROID](entities/droid.md) — Distributed Robot Interaction Dataset; 350 hr / 76k traj / 564 scenes of Franka Panda teleop; the dominant real-robot dataset in JEPA-for-robotics work. (4 sources)
- [Open X-Embodiment (OXE)](entities/open-x-embodiment.md) — 22-embodiment + ~500-skill umbrella corpus (O'Neill et al. 2024); the standard cross-embodiment pretraining corpus for [π0](entities/pi-zero.md), [Octo](entities/octo.md), [OpenVLA](entities/openvla.md). [DROID](entities/droid.md) is the Franka-Panda subset. (0 sources) _stub_
- [EgoDex](entities/egodex.md) — 829 hr Apple Vision Pro–captured egocentric dataset; 194 tabletop manipulation tasks; clean wrist + hand keypoints. The high-precision complement to in-the-wild egocentric data in [EgoScale](sources/egoscale-paper.md) pretraining. (1 source)

### Model organisms / connectomes
- [Drosophila melanogaster](entities/drosophila.md) — fruit fly; canonical "whole-organism AI" target; substrate for both [FlyWire](entities/flywire.md) and [flybody](entities/flybody.md). (6 sources)
- [FlyWire](entities/flywire.md) — international consortium + dataset for the complete adult *Drosophila* brain connectome (139,255 neurons, ~50M synapses; *Nature* 2024). (4 sources)
- [Drosophila brain model](entities/drosophila-brain-model.md) — Phil Shiu's MIT-licensed Brian 2 LIF model on the FlyWire connectome (paper code). (3 sources)
- [flyvis](entities/flyvis.md) — TuragaLab's MIT-licensed PyTorch connectome-constrained DMN of the fly visual system; v1.1.3 March 2026. (1 source)

### Vision foundation models
- [DINOv2](entities/dinov2.md) — Meta FAIR self-supervised ViT (142M images, ViT-S/B/L/g); substrate for DINO-WM, DINO-world, JEPA-WMs. Apache 2.0. (4 sources)
- [DINOv3](entities/dinov3.md) — Meta AI Research 7B-parameter ViT SSL foundation model (Aug 2025); Gram anchoring fixes dense-feature degradation; new SSL state-of-the-art on dense tasks (COCO mAP 66.1 frozen, ADE20k mIoU 63.0). (1 source)

### VLM backbones (for VLAs)
- [PaliGemma](entities/paligemma.md) — Google's 3 B VLM (SigLIP + Gemma 2B; Beyer et al. 2024); backbone of [π0](entities/pi-zero.md). (0 sources) _stub_
- [Gemma3](entities/gemma3.md) — Google's 2025 VLM family (1B/4B/12B/27B; built-in 400M vision encoder); backbone of [π0.7](entities/pi07.md). (0 sources) _stub_
- [SmolVLM-2](entities/smolvlm.md) — Hugging Face's compact ~0.4 B VLM (SigLIP + SmolLM2; Marafioti et al. 2025); backbone of [SmolVLA](entities/smolvla.md). (0 sources) _stub_

### Generative models for image / world
- [BAGEL](entities/bagel.md) — 14B mixture-of-transformers image-gen + editing model (2025); used as the subgoal-image world model substrate in [π0.7](entities/pi07.md). (0 sources) _stub_

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
- [TD-MPC / TD-MPC2](entities/td-mpc.md) — Hansen-line decoder-free MBRL with MPC + TD-bootstrapped value; LeWM baseline; closest MBRL relative to JEPA; **the only model-based method natively in LeRobot**. (3 sources)
- [PLDM (Planning with Latent Dynamics Models)](entities/pldm.md) — Sobal-line end-to-end JEPA WM (NYU + FAIR); VICReg + inverse-dynamics + similarity multi-term loss; the canonical "end-to-end JEPA before LeWM" baseline. (2 sources — 2022 precursor + 2025 paper)

### VLA models / generalist policies
- [NVIDIA GR00T](entities/nvidia-groot.md) — open VLA bundled with Isaac Lab; N1.5 won both sites of the Oct 2025 Embodied AI Hackathon; N1.7 EA pretraining sourced via [EgoScale](sources/egoscale-paper.md); GR00T N1.5 used as the post-trained policy in [DreamDojo](sources/dreamdojo-paper.md)'s policy-eval demo. (13 sources)
- [π0](entities/pi-zero.md) — [Physical Intelligence](entities/physical-intelligence.md)'s 3.3 B VLA (Oct 2024); PaliGemma 3 B VLM + flow-matching action expert; cross-embodiment teleop on 7 robots / 68 tasks / 10k hours. The canonical flow-matching VLA; LeRobot-supported (lerobot/pi0). (6 sources)
- [π0.7](entities/pi07.md) — [Physical Intelligence](entities/physical-intelligence.md)'s 5 B VLA (2025); Gemma3 4B + MEM video encoder + 860 M flow-matching action expert; diversified prompt with subgoal images + episode metadata; first VLA with emergent compositional generalization (espresso machine, sweet-potato-into-air-fryer out-of-the-box). (1 source)
- [π*0.6](entities/pistar06.md) — [Physical Intelligence](entities/physical-intelligence.md)'s RL-adapted π0.6 (2025); RECAP recipe = offline-RL pretraining + iterative deployment with advantage-conditioned policy extraction; 2× throughput, ½ failure rate; 13-hr continuous espresso operation. (1 source)
- [π0.6 (and π0.5, π0.6-MEM intermediates)](entities/pi-zero-6.md) — anchor for the intermediate π-series generations between [π0](entities/pi-zero.md) and [π0.7](entities/pi07.md) / [π*0.6](entities/pistar06.md). No primary source ingested. (0 sources) _stub_
- [SmolVLA](entities/smolvla.md) — [Hugging Face](entities/hugging-face.md) LeRobot team's 450 M VLA (June 2025); SmolVLM-2 + flow-matching with interleaved CA + causal SA; 22.9 K community-dataset episodes; **beats π0-3.5 B by +16.6 pts on real-world SO-100 multi-task**; async-inference RobotClient/PolicyServer stack; runs on CPU (only frontier VLA that does). (5 sources)
- [OpenVLA](entities/openvla.md) — Kim et al. 2024; 7B open-weights baseline (Llama-2 backbone + autoregressive action tokens); the reference comparison VLA across nearly every 2024–2025 VLA paper. (0 sources) _stub_
- [Octo](entities/octo.md) — Octo Model Team 2024; transformer-from-scratch generalist policy trained on [OXE](entities/open-x-embodiment.md); pre-flow-matching-era baseline. (0 sources) _stub_
- [Gemini Robotics](entities/gemini-robotics.md) — Google DeepMind robot foundation models; full VLA + Gemini Robotics-**ER** embodied-reasoning VLM (tool-call planner). (1 source)
- [OK-Robot](entities/ok-robot.md) — NYU zero-shot pick-and-drop framework; 58.5% in 10 homes; 1.8× over OVMM. (1 source)
- [Robot Utility Models](entities/robot-utility-models.md) — NYU/Meta zero-shot mobile-manipulation BC. (5 sources)
- [Dobb·E](entities/dobb-e.md) — NYU predecessor to RUM; HPR encoder + Stick-v1 + Homes of New York dataset. (2 sources) _stub_

### Behavior-cloning methods
- [IBC](entities/ibc.md) — Implicit Behavioral Cloning (Florence et al., CoRL 2021); energy-based-model BC; introduced PushT; direct ancestor of Diffusion Policy. (1 source)
- [BET](entities/bet.md) — Behavior Transformer (Shafiullah et al., NeurIPS 2022); transformer + k-means action discretization; ancestor of VQ-BeT. (1 source)
- [VQ-BeT](entities/vq-bet.md) — Vector-Quantized Behavior Transformer (Lee et al. 2024); top performer in RUM ablation; LeRobot-supported. (7 sources)
- [Diffusion Policy](entities/diffusion-policy.md) — Chi et al. 2023, Columbia/TRI/MIT; conditional DDPM over actions; popularized PushT + UMI gripper + action-chunking convention; LeRobot-supported (263 M params; CPU-incompatible without acceleration). (11 sources)
- [ACT (Action Chunking Transformer)](entities/act.md) — Zhao et al. 2023, Stanford; default IL policy for [ALOHA / Mobile ALOHA](entities/aloha.md); operationalized **action chunking** as a first-class IL primitive (now near-default across 2024–2026 BC + VLA); LeRobot's most-used policy (52 M params, ~100–200 Hz on RTX 4090). (4 sources)
- [ACT++](entities/act-plus-plus.md) — the mobile-extended ML codebase shipped with [Mobile ALOHA](entities/aloha.md) (`MarkFzp/act-plus-plus`); adds the 16-dim base+arm action vector + co-training + action-chunk delay-shift. (2 sources)
- [UMI](entities/umi.md) — Universal Manipulation Interface (Chi et al., RSS 2024); hand-held gripper data-collection system; same lead author as Diffusion Policy. (1 source)

### LLMs
- [Qwen](entities/qwen.md) — Alibaba's open-weights LLM family. Default local LLM in both stretch_ai (3B) and ROSOrin (1.7B). (2 sources)

### Tools
- [Ollama](entities/ollama.md) — local LLM runtime (used by ROSOrin offline curriculum). (1 source) _stub_
- [MimicGen](entities/mimicgen.md) — synthetic-demo expansion tool used by RoboCasa365. (1 source) _stub_
- [NVIDIA Brev](entities/nvidia-brev.md) — NVIDIA's cross-cloud GPU-instance broker (`brev` CLI + Launchables); no native auto-stop, so cost discipline is on the user. (2 sources)

### Reasoning / formal-verification models
- [Aleph](entities/aleph.md) — [Logical Intelligence](entities/logical-intelligence.md)'s agentic orchestration product; pairs frontier LLM (GPT-5.2) + [Kona](entities/kona.md) + [Lean](concepts/learning/lean-theorem-prover.md); **99.4% / 668-of-672 on [PutnamBench](concepts/learning/putnambench.md)** (May 2026). (1 source)
- [Kona](entities/kona.md) — non-autoregressive [energy-based reasoning model](concepts/learning/energy-based-models.md) from [Logical Intelligence](entities/logical-intelligence.md); 16M–200M params; pilots in energy / advanced manufacturing / semiconductor (Q1 2026). (1 source)

### Events
- [LeRobot Worldwide Hackathon 2025](entities/lerobot-worldwide-hackathon-2025.md) — Hugging Face hybrid hackathon, June 14–15, 2025; 916 team members, ~400 submissions, 30 ranked winners; prizes: Hope Jr Arm / LeKiwi / SO-101. (1 source)

### People
- [Yann LeCun](entities/yann-lecun.md) — NYU; Turing Award 2018; architect of the JEPA program; reported founder of AMI Labs (Apr 2026, provisional). Co-authored the original 1993 Siamese network paper at AT&T Bell Labs. (17 sources)
- [Andrej Karpathy](entities/andrej-karpathy.md) — independent AI researcher/educator; formerly Tesla AI director + OpenAI founding member; author of micrograd / nanoGPT / nanochat / autoresearch — the wiki's recommended pedagogical reference implementations for backprop, transformers, end-to-end LLM training, and agent-driven ML research. (4 sources)
- [Navid Azizan](entities/navid-azizan.md) — MIT ME / IDSS / LIDS; learning-based control; SD-LQR (ICML 2023) + drone adaptive control (2025). (2 sources)
- [Adrien Bardes](entities/adrien-bardes.md) — FAIR researcher; lead author on VICReg (ICLR 2022); co-senior on V-JEPA 2, V-JEPA 2.1, JEPA-WMs. The FAIR-side champion of the V-JEPA program. (4 sources)
- [Basile Terver](entities/basile-terver.md) — researcher (FAIR-affiliated, inferred); bread-crumb across DINO-world → JEPA-WMs lineage. (2 sources)
- [Sergey Levine](entities/sergey-levine.md) — UC Berkeley EECS; senior on DROID + Metaworld. (0 source pages yet — referenced via entity pages)
- [Chelsea Finn](entities/chelsea-finn.md) — Stanford CS; senior on DROID + Metaworld + Mobile ALOHA. (1 source page: Mobile ALOHA)
- [Tony Z. Zhao](entities/tony-zhao.md) — Stanford CS; first author on original ALOHA + [ACT](entities/act.md); co-lead on [Mobile ALOHA](entities/aloha.md). (1 source)
- [Zipeng Fu](entities/zipeng-fu.md) — Stanford CS PhD; co-lead on [Mobile ALOHA](entities/aloha.md). (1 source)
- [Lerrel Pinto](entities/lerrel-pinto.md) — NYU CS; co-senior on DINO-WM, RUM, and OK-Robot. (5 sources)
- [Jim Fan (Linxi Fan)](entities/jim-fan.md) — NVIDIA Director of Robotics, Distinguished Scientist; co-founder + co-lead of [NVIDIA GEAR](entities/nvidia-gear.md) (Feb 2024); co-leads [GR00T](entities/nvidia-groot.md); project lead on [EgoScale](sources/egoscale-paper.md) + [DreamDojo](sources/dreamdojo-paper.md); pre-GEAR author on MineDojo / VIMA / Voyager / Eureka. (3 sources)
- [Yuke Zhu](entities/yuke-zhu.md) — UT Austin Associate Prof / NVIDIA Director; co-leads [GEAR](entities/nvidia-gear.md); senior on RoboCasa365 + the original RoboCasa + MimicGen line; project lead on [EgoScale](sources/egoscale-paper.md) + [DreamDojo](sources/dreamdojo-paper.md); co-author on Huh et al. 2026. (5 sources)
- [Joel Jang](entities/joel-jang.md) — research scientist at [NVIDIA GEAR](entities/nvidia-gear.md); third project lead on [DreamDojo](sources/dreamdojo-paper.md) alongside Yuke Zhu + Jim Fan. (1 source) _stub_
- [Stephen Welch](entities/stephen-welch.md) — founder of [Welch Labs](entities/welch-labs.md); independent AI educator; author of the [Illustrated Guide to AI Vol I](sources/welchlabs-illustrated-guide-to-ai.md). Based in Winston-Salem, NC. (3 sources)
- [Mathieu Blondel](entities/mathieu-blondel.md) — Google DeepMind; co-author of [The Elements of Differentiable Programming](sources/blondel-roulet-differentiable-programming.md) (Blondel & Roulet, 485 pp, draft v3 June 2025); long-running research line on Fenchel-Young losses + sparsemax + structured prediction + JAX ecosystem (JAXopt, optax). (1 source)
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
- [Remi Cadene](entities/remi-cadene.md) — robotics lead at [Hugging Face](entities/hugging-face.md); responsible for [LeRobot](entities/lerobot.md); **lead author on ICLR 2026 LeRobot paper**; SmolVLA co-author; co-organizer of the [Worldwide Hackathon 2025](entities/lerobot-worldwide-hackathon-2025.md). (3 sources)
- [Eve Bodnia](entities/eve-bodnia.md) — Founder + CEO of [Logical Intelligence](entities/logical-intelligence.md); EBM-for-reasoning agenda. (1 source)
- [Michael Freedman](entities/michael-freedman.md) — Fields Medal 1986; Chief of Mathematics at [Logical Intelligence](entities/logical-intelligence.md). (1 source)
- [Vlad Isenbaev](entities/vlad-isenbaev.md) — Chief of AI at [Logical Intelligence](entities/logical-intelligence.md); ICPC World Champion; ex-Facebook/Cruise/Nuro. (1 source) _stub_
- [Patrick Hillmann](entities/patrick-hillmann.md) — Chief Strategy Officer at [Logical Intelligence](entities/logical-intelligence.md); ex-Binance CSO. (1 source) _stub_

## Concepts

### Learning
- [VLA models](concepts/learning/vla-models.md) — vision-language-action robot foundation models. (20 sources)
- [Imitation learning](concepts/learning/imitation-learning.md) — supervised learning from demonstrations. (17 sources)
- [Flow matching](concepts/learning/flow-matching.md) — learn a vector field that transports noise to actions; the dominant continuous-action-head technique in 2025+ VLAs ([π0](entities/pi-zero.md), [π0.7](entities/pi07.md), [π*0.6](entities/pistar06.md), [SmolVLA](entities/smolvla.md), [EgoScale](sources/egoscale-paper.md)). Sibling-not-subclass of [DDPM](entities/ddpm.md). (7 sources)
- [Sim-to-real transfer](concepts/learning/sim-to-real-transfer.md) — bridging simulator-trained policies to real robots. (9 sources)
- [Scaling laws — VLAs and human data](concepts/learning/scaling-laws-vla.md) — the empirical data-vs-performance relationship for VLA pretraining; seeded from [EgoScale](sources/egoscale-paper.md)'s log-linear loss law (R² = 0.9983) on 20,854 hr of egocentric human video; LLM-side companion via Welch Labs Ch 6 (Kaplan 2020). (2 sources)
- [Chain of thought](concepts/learning/chain-of-thought.md) — intermediate-reasoning-token technique; origin (Wei 2022); zero-shot/self-consistency/ToT; modern reasoning models; embodied CoT in VLAs and S1/S2 splits. (0 sources — hub page)
- [Energy-based models (EBMs)](concepts/learning/energy-based-models.md) — `E_θ(x, y)` low when compatible; inference is `argmin_y E`. Connects [IBC](entities/ibc.md), [JEPA](concepts/world-models/jepa.md) training, and [Kona](entities/kona.md) — three different applications of the same LeCun-line commitment to non-autoregressive learning. (4 sources)
- [Formal verification](concepts/learning/formal-verification.md) — machine-checkable proofs; "translate, propose, verify" pipeline; deterministic kernel as the hallucination cure. Used by [Aleph](entities/aleph.md). (1 source)
- [Lean theorem prover](concepts/learning/lean-theorem-prover.md) — the verification substrate underneath [Aleph](entities/aleph.md); Mathlib; tactic + term mode; PutnamBench-native. (1 source)
- [PutnamBench](concepts/learning/putnambench.md) — 672 Putnam Exam problems formalized in [Lean](concepts/learning/lean-theorem-prover.md); machine-checkable formal-reasoning benchmark; [Aleph](entities/aleph.md) at 99.4% (May 2026). (1 source)

### World models
- [World model](concepts/world-models/world-model.md) — umbrella concept: learned predictive model of environment dynamics (generative-video / JEPA / frozen-feature / model-based-RL). (14 sources)
- [Joint-Embedding Predictive Architecture](concepts/world-models/jepa.md) — predict next-state representations, not pixels. (15 sources)
- [World-model simulators](concepts/world-models/world-model-simulators.md) — narrower companion to [World model](concepts/world-models/world-model.md): world-models-used-as-simulators (generative-video and JEPA paradigms). (14 sources)
- [Learned latent space](concepts/world-models/latent-space.md) — vector space where a trained encoder represents inputs; substrate for JEPA prediction, DINOv2 features, VQ-BeT codebook. (10 sources)
- [Siamese network](concepts/world-models/siamese-network.md) — two weight-tied encoders + similarity/distance/predictor head; ancestor of every joint-embedding SSL system since 1993. (5 sources)

### Agents
- [LLM-agent architecture](concepts/agents/llm-agent-architecture.md) — LLM-emits-tool-calls control pattern; MCP and A2A as inter-agent/tool-access protocols. (8 sources)

### Safety
- [AI safety and alignment](concepts/safety/ai-safety-alignment.md) — corrigibility, broadly safe behaviors, hard constraints, catastrophic risk framing; connects to agentic robot deployments. (3 sources)
- [Corrigibility](concepts/safety/corrigibility.md) — the corrigibility dial (fully corrigible ↔ fully autonomous); asymmetric cost argument; galaxy-brained reasoning risk; agentic deployment implications. (1 source)
- [Mechanistic interpretability](concepts/safety/mechanistic-interpretability.md) — reading and steering features inside trained neural nets; sparse autoencoders (Anthropic / Templeton et al. 2024); Chris Olah's "dark matter of interpretability" (~1% of concepts extracted). Seeded by [Welch Labs Illustrated Guide Ch 7](sources/welchlabs-illustrated-guide-to-ai.md). (1 source)

### Robotics
- [Assistive robotics](concepts/robotics/assistive-robotics.md) — robots helping disabled/elderly users regain autonomy; systematic review; three research themes; autonomy finding. (16 sources)
- [End-user robot programming](concepts/robotics/end-user-robot-programming.md) — enabling non-experts to customize robot behavior; EUP approaches; sense of agency evidence; Stretch SE2 transfer. (7 sources)
- [Accessible robot communication](concepts/robotics/accessible-robot-communication.md) — robot output-interface design for non-visual users; mixed-initiative narration findings; 6 design guidelines (Huh et al. 2026). (4 sources)
- [Optimal control](concepts/robotics/optimal-control.md) — minimize a cost over trajectory-control pairs subject to dynamics. Brachystochrone (1697) → Euler–Lagrange → Hamilton–Jacobi → Pontryagin's Maximum Principle (1956) → Bellman DP → modern LQR / MPC / iLQR / CEM / learned-WM-OC. The "RL = approximate OC under uncertainty" bridge. (6 sources)
- [AprilTags](concepts/robotics/apriltags.md) — visual fiducial markers for 6-DOF pose estimation; standard in FRC and research robotics. (2 sources)
- [Agentic UAVs](concepts/robotics/agentic-uavs.md) — autonomous aerial systems with goal-driven behavior; 4-layer architecture; 8 domains; adaptive control. (2 sources)

### Bio
- [Biomechanical simulation](concepts/bio/biomechanical-simulation.md) — physics-based simulation of an animal body; lineage *C. elegans* → Hydra → virtual rodent → NeuroMechFly v1/v2 → flybody. (5 sources)
- [Connectome](concepts/bio/connectome.md) — complete wiring diagram of a nervous system; *C. elegans* → fly hemibrain → FlyWire → mouse → human. (3 sources)

## Syntheses

### Curriculum
- [Robot-learning curriculum — from neurons to LeWorldModel](syntheses/curriculum/robot-learning-curriculum.md) — 14-module curriculum hub; **all 14 modules drafted**. (2026-05-10)
- [Curriculum Module 1 — Neural networks and training](syntheses/curriculum/curriculum-01-neural-networks.md) — Tier 1; neuron, MLP, backprop, BN/LN, residuals, Adam. Anchor: tiny MLP digit classifier. (2026-05-10)
- [Curriculum Module 2 — CNNs and visual representation learning](syntheses/curriculum/curriculum-02-cnns.md) — Tier 1; convolution, pooling, ResNet, ImageNet pretrain + fine-tune, visual encoders. Anchor: ResNet-18 features on PushT. (2026-05-10)
- [Curriculum Module 3 — Sequence models, attention, and transformers](syntheses/curriculum/curriculum-03-attention-and-transformers.md) — Tier 1; attention, MHA, transformer blocks, ViT, positional encoding, causal masking. Anchor: tiny transformer on PushT patches. (2026-05-10)
- [Curriculum Module 4 — Self-supervised learning and embeddings](syntheses/curriculum/curriculum-04-self-supervised-learning.md) — Tier 1; SSL taxonomy, representation collapse, anti-collapse families (EMA, VICReg, frozen, multi-fix, SIGReg). Anchor: VICReg on CIFAR with/without regularizer. (2026-05-10)
- [Curriculum Module 5 — Generative modeling fundamentals (DDPM, full math)](syntheses/curriculum/curriculum-05-generative-models.md) — Tier 2. Full ELBO → `L_simple` derivation; KL bounds; ε-parameterization; noise schedules; DDIM sampling; classifier-free guidance derivation. Anchor: train tiny DDPM on MNIST + paper-derive `L_simple` from ELBO. (2026-05-10)
- [Curriculum Module 6 — Imitation learning and behavior cloning](syntheses/curriculum/curriculum-06-imitation-learning.md) — IL/BC frame, multi-modal failure mode, distribution shift / DAgger, action chunking + receding-horizon control, PushT setup. (2026-05-10)
- [Curriculum Module 7 — BC lineage on PushT (IBC → BeT → DP)](syntheses/curriculum/curriculum-07-bc-lineage-pusht.md) — multi-modal-action problem + IBC/BeT/Diffusion Policy + bridge to world models; anchor exercise on PushT. (2026-05-10)
- [Curriculum Module 8 — Reinforcement learning vocabulary](syntheses/curriculum/curriculum-08-rl-vocabulary.md) — light/vocabulary-only RL coverage (MDP, return, value, policy, REINFORCE → PPO, DQN, MFRL vs MBRL, Dreamer-class latent imagination); supporting module for the LeWM Dreamer / TD-MPC baselines. (2026-05-10)
- [Curriculum Module 9 — Vision-Language-Action models](syntheses/curriculum/curriculum-09-vla.md) — closes the policy-side reading chain (6 → 7 → 9). VLA structural definition; VLAs are not world models; action-head taxonomy; major 2026 VLAs; S1/S2 hierarchical pattern; VLA-JEPA as Module-11 cross-over. (2026-05-10)
- [Curriculum Module 10 — World models, broad](syntheses/curriculum/curriculum-10-world-models.md) — functional definition; four families (generative-video / JEPA / frozen-feature / MBRL); MPC + CEM + gradient-based planning; horizon vs compounding error; LeWM positioned in the taxonomy. (2026-05-10)
- [Curriculum Module 11 — JEPA in depth](syntheses/curriculum/curriculum-11-jepa-deep.md) — joint-embedding architecture; collapse-prevention zoo (EMA, VICReg, frozen encoder, multi-fix, SIGReg); V-JEPA progression; DINO-WM frozen-feature variants; JEPA-WMs first-real-Franka; LeWM-vs-V-JEPA-2 axis-by-axis. (2026-05-10)
- [Curriculum Module 12 — LeWorldModel deep-dive (with full SIGReg math)](syntheses/curriculum/curriculum-12-lewm-deep-dive.md) — the destination module. LeWM section by section; full SIGReg derivation (random projections + Epps–Pulley + Cramér–Wold + backprop); architecture (incl. the BN-after-CLS trick); CEM-MPC; four-env results; latent probing + VoE; what it means for the JEPA program. (2026-05-10)
- [Curriculum Module 13 — Home robotics deployment reality](syntheses/curriculum/curriculum-13-home-robotics-deployment.md) — the 89.4 / 12.4 gap; Stretch convergence; RUM + OK-Robot as strongest current results; PAR / EUP / autonomy-preference framing; where LeWM-class techniques plausibly fit (and don't). Anchor: pick LeWM-on-Stretch vs DINO-WM-on-Stretch. (2026-05-10)
- [Curriculum Module 14 — Capstone (paper-first, hardware-second)](syntheses/curriculum/curriculum-14-capstone.md) — the capstone. Phase A: reproduce LeWM PushT + 5–10 page experiment-design memo for a Stretch experiment. Phase B (gated): execute on real Stretch, compare to a Diffusion Policy baseline. The curriculum is completable on phase A alone. (2026-05-10)

### Platforms
- [Robot platforms — comparison](syntheses/platforms/robot-platforms-comparison.md) — at-a-glance table of every robot entity in the wiki by tier / type / use; flags missing humanoids + cross-tier transfer gap. (2026-05-08)
- [Humanoid platforms survey](syntheses/platforms/humanoid-platforms-survey.md) — companion to robot-platforms-comparison focused on humanoids; 10 entities listed by tier; AI-strategy archetypes + price stratification. (2026-05-08)
- [Household robot decision — Stretch vs Unitree G1](syntheses/platforms/household-robot-decision-stretch-vs-g1.md) — buying-decision comparison for navigate + floor pickup + dishes + cans use case. Recommends Stretch. (2026-05-08)
- [Jetson Thor vs DGX Spark](syntheses/platforms/jetson-thor-vs-dgx-spark.md) — train-on-Spark / deploy-on-Thor split; RT-cores as the gating capability for Isaac Sim/Lab; decision tree for which-NVIDIA-box-for-what. (2026-05-16)
- [Open-source robot AI research projects — landscape](syntheses/platforms/open-source-robot-ai-projects.md) — grouped catalog of every open-source project tracked in this wiki: LeRobot ecosystem, JEPA / world-model code, open VLAs, BC baselines, Karpathy's repos, whole-organism fly, open simulators, Farama RL stack, open robot platforms, the orgs behind them. (2026-05-17)
- [NVIDIA GPU rental landscape](syntheses/platforms/nvidia-gpu-rental-landscape.md) — providers, pricing, and how to choose: NVIDIA-native (Brev, DGX Cloud, Launchables), AI-focused clouds (RunPod, Lambda Labs, CoreWeave, Vast.ai, Modal), hyperscalers, DGX Spark-specific (Enverge $0.48/hr, Server Room, Primcast), peer-to-peer. H100 spans $1.25–$6.98/hr across 15+ providers in mid-2026. (2026-05-17)

### Projects
- [LeWM on ROSOrin Pro — feasibility analysis](syntheses/projects/lewm-on-rosorin-pro-feasibility.md) — what's missing to deploy LeWM on Hiwonder ROSOrin Pro; realistic path; risks. (2026-05-08)
- [LeWM on Stretch — feasibility analysis](syntheses/projects/lewm-on-stretch-feasibility.md) — companion: Stretch resolves the teleop-data blocker via RUM's open dataset; concrete LeWM-vs-RUM-BC experiment design. (2026-05-08)
- [JEPA project ladder for ROSOrin Pro](syntheses/projects/jepa-project-ladder-rosorin-pro.md) — six-rung educational/research project ladder for learning JEPA on ROSOrin Pro hardware. (2026-05-08)
- [ROSOrin Pro — Lego pick-and-place project plan](syntheses/projects/rosorin-pro-lego-pick-place.md) — the BC-path sibling to the JEPA ladder; three tiers (OpenClaw color-threshold → LeRobot ACT/DP behavior cloning → GR00T fine-tune); recommends Tier 2 for "robust enough to use." (2026-05-15)
- [LeWM hello world — Project 1 detailed scope](syntheses/projects/lewm-hello-world-project-scope.md) — phase-by-phase plan for reproducing LeWM PushT, training from scratch, one-knob ablation. (2026-05-08)
- [DINO-WM on Stretch — concrete experiment plan](syntheses/projects/dino-wm-on-stretch-experiment.md) — sibling to LeWM-on-Stretch; lower-risk frozen-encoder variant; train predictor only on RUM dataset. (2026-05-09)
- [Jetson Orin Nano — flash Jetson OS to NVMe SSD howto](syntheses/projects/jetson-orin-nano-flash-howto.md) — operational guide: SDK Manager or CLI `l4t_initrd_flash.sh`; QSPI bootloader caveat for pre-mid-2023 dev kits. (2026-05-16)
- [Wiki-query agent on DGX Spark — deployment plan](syntheses/projects/wiki-query-agent-on-dgx-spark.md) — scoping plan for serving this wiki as a queryable agent from a local DGX Spark running Qwen 2.5 72B Q8 via vLLM. Compares Anthropic-API / RAG-site / MCP / local-LLM paths; explains why Spark over Thor (RT cores for the dev-box use case); includes rent-before-buy section (Spark cloud rentals from Enverge at $0.48/hr). (2026-05-17)
- [LeRobot on ROSOrin Pro — adaptation plan for in-home floor-pickup-and-tidy](syntheses/projects/lerobot-on-rosorin-pro.md) — concrete porting plan (wrap `~/arm_group_control` ROS service vs direct STM32 serial; HX-12H ≠ FeeTech/Dynamixel SDK gap; Aurora930 12 fps vs LeRobot 30 Hz default) + 4-step ladder toward "navigate the house, pick objects off the floor, tidy them." Recommendation: keep OpenClaw as orchestrator, swap deterministic `/start_pick` for a LeRobot-trained ACT/SmolVLA policy fed by Dobb·E-style stick demos. (2026-05-28)

### World models
- [Generative-video vs JEPA world models](syntheses/world-models/generative-video-vs-jepa-world-models.md) — what each predicts, costs, and demonstrates. (2026-05-07)
- [LeWorldModel — train and run howto](syntheses/world-models/leworldmodel-howto.md) — install, train, and evaluate LeWM on a single GPU. (2026-05-07)
- [Why JEPA research skips the simulator stack](syntheses/world-models/why-jepa-research-skips-the-simulator-stack.md) — JEPA literature fragments across sim weight classes (none / light / mid / heavy). Major revision after 5 new ingests. (updated 2026-05-07)
- [JEPA task capabilities](syntheses/world-models/jepa-task-capabilities.md) — reference index of seven task categories JEPA models demonstrate, mapped per-paper. (2026-05-08)

### Simulators
- [Simulators for agentic robotics — 2026 landscape](syntheses/simulators/simulators-for-agentic-robotics-2026.md) — full landscape survey, 6 categories. (updated 2026-05-07)
- [Newton + OpenUSD — the substrate convergence](syntheses/simulators/newton-openusd-substrate-convergence.md) — vendor-neutral physics + scene format across Isaac Lab and MuJoCo Playground. (2026-05-07)
- [Sim-heavy vs real-data paths to generalist policies](syntheses/simulators/sim-heavy-vs-real-data-paths.md) — three-path comparison: synthetic teleop, real demos, observation pretraining. (2026-05-07)
- [OpenUSD support across simulators](syntheses/simulators/openusd-support-across-simulators.md) — catalog of which simulators consume USD, how, and which are exceptions. (2026-05-07)
- [FRC simulation & AI landscape](syntheses/simulators/frc-simulation-and-ai-landscape.md) — what simulation programs FRC teams use for autonomous dev and AI training; three-tier analysis (trajectory planners / physics sims / ML frontier); Team 254 presentation deep-dive. (updated 2026-05-08)

### Assistive
- [Assistive robotics — R&D landscape and JEPA applicability](syntheses/assistive/assistive-robotics-research-landscape.md) — seven blocking problems, timeline table, active researchers (wiki + beyond), four independent-researcher actions, JEPA applicability analysis. (2026-05-09)
- [Levels of autonomy in assistive robotics](syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md) — three orthogonal autonomy axes (execution / programming / intent inference); five empirical findings; user-EUP-over-RUM stack as unbuilt natural integration. (2026-05-09)
- [Long-term in-home robot deployments](syntheses/assistive/long-term-in-home-robot-deployments.md) — depth-sorted table of every in-home deployment in the wiki; reliability gradient; what's missing from the longitudinal record. (2026-05-09)
- [Stretch as the de-facto assistive-robotics platform](syntheses/assistive/stretch-as-assistive-platform.md) — why every wiki-relevant in-home deployment uses Stretch; eight features that compound; what Stretch doesn't solve. (2026-05-09)
- [Underserved PAR domains — dressing, bathing, medication](syntheses/assistive/underserved-par-domains.md) — sub-capability decomposition for each; ranked researcher targets (medication-fetcher most tractable). (2026-05-09)

### Agents
- [LLM-agent architecture across stacks](syntheses/agents/llm-agent-architecture-across-stacks.md) — three-way comparison of stretch_ai, ROSOrin, OpenClaw. (2026-05-07)
- [Whole-organism agentic AI](syntheses/agents/whole-organism-agentic-ai.md) — brain (FlyWire connectome + LIF dynamics) + body (flybody MuJoCo) for *Drosophila*; first plausible end-to-end animal-scale agent; contrasts with robotics-flavoured agentic AI. (2026-05-08)

### RL
- [Atari RL lineage — from ALE to Agent57 and MuZero](syntheses/rl/atari-rl-lineage.md) — hub for the Atari/DQN material; DQN → Rainbow → A3C/PPO → Go-Explore/Agent57 → MuZero/Dreamer; why robotics moved on but kept the toolbox. (2026-05-15)

### JEPA-related concepts/entities/sources to potentially expand
- Metaworld — referenced by [JEPA-WMs](sources/jepa-wms-paper.md) (42 tasks); deserves an entity page.
- LIBERO / LIBERO-Plus — referenced by [VLA-JEPA](sources/vla-jepa-paper.md); benchmark concept/source pages.
- SimplerEnv — referenced by [VLA-JEPA](sources/vla-jepa-paper.md); mid-weight Sapien-adjacent simulator.
- `stable-worldmodel` package — env zoo broader than [LeWM howto](syntheses/world-models/leworldmodel-howto.md) exposed; verify and update.
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
- ~~DROID paper, Metaworld paper, DINOv2 paper, Dobb·E paper, VQ-BeT paper~~ — all filed 2026-05-16: [DROID](sources/droid-paper.md), [Metaworld](sources/metaworld-paper.md), [DINOv2](sources/dinov2-paper.md), [Dobb·E](sources/dobb-e-paper.md) (arxiv ID corrected to 2311.16098), [VQ-BeT](sources/vq-bet-paper.md) (arxiv 2403.03181). ([Diffusion Policy Paper](sources/diffusion-policy-paper.md), [IBC Paper](sources/ibc-paper.md), [BET Paper](sources/bet-paper.md), [DDPM Paper](sources/ddpm-paper.md), [UMI Project Page](sources/umi-paper.md) already filed earlier.)
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
- Humanoids not yet filed: AGIBOT humanoid hardware (A2/X1/X2 — [company](entities/agibot.md) is filed), Fourier GR-1/GR-2, LimX CL-2/CL-3, Booster T1, EngineAI PM01 (Chinese affordable). PAL TIAGo/TALOS, Pepper, Robotis OP3/DARwIn-MINI, Sanctuary Phoenix, Kawasaki Kaleido, AIST HRP-5P, Toyota T-HR3 (research / educational). See [humanoid-platforms-survey](syntheses/platforms/humanoid-platforms-survey.md) for landscape context.

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
- Mi et al. 2022 (ICLR) connectome-constrained latent-variable model — still referenced via [Connectome](concepts/bio/connectome.md) and [flybody Paper](sources/flybody-paper.md) only; not yet a primary-source page. ([Shiu et al. 2024](sources/shiu-fly-brain-paper.md) and [Lappalainen et al. 2024](sources/lappalainen-flyvis-paper.md) now filed.)
- Brian 2 spiking-NN simulator — substrate under [Shiu et al. 2024](sources/shiu-fly-brain-paper.md); entity page on demand. ([flyvis](entities/flyvis.md) and [Drosophila brain model](entities/drosophila-brain-model.md) now filed.)
- Yuval Tassa, Srinivas Turaga (now senior on two ingested sources), Josh Merel, Janne Lappalainen, Kristin Scott, Jakob Macke — entity pages on demand. ([Phil Shiu](entities/phil-shiu.md) now filed.)
- Virtual rodent (Merel et al. 2020, ICLR) — direct DeepMind ancestor of [flybody](entities/flybody.md); entity page on demand.
- *C. elegans* / Hydra body sims (Boyle 2012, Wang 2023) — earlier whole-organism biomechanics; one-line references in flybody-paper.
