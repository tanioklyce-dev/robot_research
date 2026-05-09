# Log

Append-only chronological record of wiki events. Each entry begins with `## [YYYY-MM-DD] <action> | <subject>` for grep-ability.

## [2026-05-09] edit | index.md Highlights restructure
- Added "Assistive Robotics" highlights block (after AI Safety and Alignment)
- Moved "General" to end of Highlights list
- Moved Log link to bottom of index.md

## [2026-05-09] ingest | Stanford HAI AI Index Report 2026
- Created [Stanford HAI — AI Index Report 2026](sources/stanford-hai-ai-index-2026.md)
- New entity: [Physical Intelligence](entities/physical-intelligence.md) — π0/π0.6 VLAs
- Updated [Figure](entities/figure.md): added BMW deployment data (11 months, 1,250+ hr, 90k+ parts, 30k vehicles); sources 0→1
- Updated [VLA models](concepts/vla-models.md): added π0/π0.6 + Gemini Robotics; added research-stage assessment from AI Index; sources 8→9
- Updated [Sim-to-real transfer](concepts/sim-to-real-transfer.md): added quantified gap table (89.4% RLBench vs 12.4% BEHAVIOR-1K); sources 8→9
- Updated [Assistive robotics](concepts/assistive-robotics.md): added BEHAVIOR-1K 12.4% household task success section; sources 4→5
- Updated [Assistive robotics synthesis](syntheses/assistive-robotics-research-landscape.md): updated reliability gap framing with BEHAVIOR-1K numbers

## [2026-05-09] query | Assistive robotics R&D landscape and JEPA applicability
- Filed [Assistive robotics — R&D landscape and JEPA applicability](syntheses/assistive-robotics-research-landscape.md)
- Synthesized from: assistive-robotics concept, ok-robot, robot-utility-models, stretch, jepa-task-capabilities, v-jepa-2, dino-wm, vla-jepa

## [2026-05-09] ingest | Learning Control-Oriented Dynamical Structure from Data (ICML 2023)
- Created [learning-control-oriented-dynamical-structure](sources/learning-control-oriented-dynamical-structure.md) (arXiv 2302.02529)
- New entity: [Navid Azizan](entities/navid-azizan.md) — connects to MIT drone adaptive control source
- Updated [MIT drone adaptive control](sources/mit-drone-adaptive-control.md): linked prior work + Azizan entity

## [2026-05-09] ingest | UAVs Meet Agentic AI survey + MIT drone adaptive control
- Created [UAVs Meet Agentic AI survey](sources/uavs-agentic-ai-survey.md) (arXiv 2506.08045)
- Created [MIT drone adaptive control](sources/mit-drone-adaptive-control.md) (MIT News, 2025-06-09)
- New concept: [Agentic UAVs](concepts/agentic-uavs.md) — 4-layer architecture, 8 domains, adaptive control thread

## [2026-05-09] ingest | mega-batch: OK-Robot, OVMM, Stretch assistive, TurtleBot 4, Elephant Robotics, Fauna, 1X NEO, Reachy 2, assistive-robotics cluster, K-Scale Labs
- New sources (13): ok-robot-project-page, ovmm-homerobot, ieee-spectrum-stretch-assistive, clearpath-turtlebot-4, elephant-robotics-myagv-compound, elephant-robotics-mybuddy-280, fauna-robotics-sprout, 1x-neo-product-page, pollen-robotics-reachy, itu-aiforgood-assistive-robots, virginia-tech-assistive-robotics-lab, relab-ethz-tenoexo, robot-report-kscale-labs-lessons
- New entities (8): ok-robot, elephant-robotics, myagv, mybuddy-280, fauna-robotics, pollen-robotics, reachy, k-scale-labs
- New concept: assistive-robotics
- Updated entities: 1x-neo (stub → primary specs), turtlebot (stub → TurtleBot 4 specs), stretch (+price, OVMM/OK-Robot/assistive use cases), hello-robot (+Aaron Edsinger, Charlie Kemp, assistive, OVMM), lerrel-pinto (+OK-Robot), mahi-shafiullah (+OK-Robot)
- Skipped (failed/403): Reachy Mini HuggingFace, RobotShop myAGV Pro, Understanding Deep Learning book

## [2026-05-09] ingest | batch: ALE + LeWM GitHub + V-JEPA 2 GitHub + 3 secondary articles
- Created [Arcade Learning Environment — Farama Project Page](sources/ale-farama.md)
- Created [LeWorldModel GitHub](sources/lewm-github.md)
- Created [V-JEPA 2 GitHub](sources/vjepa2-github.md)
- Created [Towards AI — LeCun / AMI Labs](sources/towardsai-lecun-ami-labs.md) (secondary, provisional)
- Created [MLWorks — LeWM Navigate the World](sources/medium-lewm-navigate-world.md) (secondary, paywalled)
- Created [Towards Deep Learning — World Model Learns Physics](sources/towardsdeeplearning-world-model-physics.md) (secondary, paywalled)
- New entity: [Arcade Learning Environment](entities/ale.md)
- New entity: [AMI Labs](entities/ami-labs.md) (provisional — single secondary source)
- Updated [Yann LeCun](entities/yann-lecun.md): noted reported departure from Meta + AMI Labs founding (hedged)
- Updated [V-JEPA 2](entities/v-jepa-2.md): added variant family table (ViT-L/H/g → ViT-B–G), 80M–2B param range, V-JEPA 2.1 training additions, dual license
- Updated [LeWorldModel](entities/leworldmodel.md): added architecture component list (ViT+AR Predictor+action encoder+SIGReg), baseline list (PLDM/LeJEPA/IVL/IQL/GCBC/DINO-WM), MIT license
- Updated [Farama Foundation](entities/farama-foundation.md): ALE now links to entity page

## [2026-05-09] ingest | New Video Series: What Developers Need to Know About OpenUSD
- Created [nvidia-openusd-developer-video-series](sources/nvidia-openusd-developer-video-series.md)
- Updated [OpenUSD](entities/openusd.md): added Hydra pipeline section; bumped to 5 sources

## [2026-05-09] query | "What does 'Joint' refer to in JEPA?"
- Updated [Joint-Embedding Predictive Architecture](concepts/jepa.md): added "What 'Joint' means" section explaining joint embedding, the shared-encoder design, and contrast with generative architectures.

## [2026-05-06] bootstrap | Wiki initialized
- Created three-layer structure: `raw/`, `wiki/`, `CLAUDE.md`.
- Configured for the robot research domain.
- Subfolders: `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`, `wiki/syntheses/`.
- Index and log seeded; no sources ingested yet.

## [2026-05-06] research | Robot simulators for agentic robot software development
- Web survey via 7 search queries on the 2026 simulator landscape (no sources dropped into `raw/` — all from web).
- **Source pages created** (10): [NVIDIA Newton Physics Engine Developer Page](sources/nvidia-newton-physics-engine-developer-page.md), [NVIDIA Newton Contact-Rich Manipulation Blog](sources/nvidia-newton-contact-rich-manipulation-blog.md), [MuJoCo Playground Paper](sources/mujoco-playground-paper.md), [Genesis Project Page](sources/genesis-project-page.md), [AGIBOT Genie Sim 3.0 Announcement](sources/agibot-genie-sim-3-announcement.md), [AGIBOT Genie Envisioner 2.0 Announcement](sources/agibot-genie-envisioner-2-announcement.md), [Genie Envisioner Paper](sources/genie-envisioner-paper.md), [RoboCasa365 Paper](sources/robocasa365-paper.md), [ManiSkill-HAB Paper](sources/maniskill-hab-paper.md), [Top 10 Physical AI Models 2026](sources/top-10-physical-ai-models-2026.md).
- **Entity pages created** (14): [NVIDIA Isaac Sim](entities/nvidia-isaac-sim.md), [NVIDIA Isaac Lab](entities/nvidia-isaac-lab.md), [Newton physics engine](entities/newton-physics-engine.md), [MuJoCo Playground](entities/mujoco-playground.md), [Genesis](entities/genesis.md), [AGIBOT Genie Sim 3.0](entities/agibot-genie-sim.md), [RoboCasa](entities/robocasa.md), [ManiSkill](entities/maniskill.md), [NVIDIA Cosmos](entities/nvidia-cosmos.md), [Genie Envisioner](entities/genie-envisioner.md), [AGIBOT](entities/agibot.md), [NVIDIA](entities/nvidia.md), plus stubs for [NVIDIA GR00T](entities/nvidia-groot.md) and [Google DeepMind](entities/google-deepmind.md).
- **Concept pages created** (3): [VLA models](concepts/vla-models.md), [Sim-to-real transfer](concepts/sim-to-real-transfer.md), [World-model simulators](concepts/world-model-simulators.md).
- **Synthesis page created** (1): [Simulators for agentic robotics — 2026 landscape](syntheses/simulators-for-agentic-robotics-2026.md).
- Five-category framing: (1) core GPU physics platforms, (2) embodied-AI / household-scale platforms, (3) world-model simulators, (4) classic / ROS-native, (5) industry usage signals.
- **Open question logged**: GR00T version inconsistency (N1.6 GA vs. N1.7 EA) flagged as a contradiction in the synthesis and on the GR00T stub.
- **Coverage gaps captured in index** under "Known gaps / TBD": Drake, Gazebo/Webots/CoppeliaSim/PyBullet, Pi (Physical Intelligence), Skild AI, LIBERO, RoboMimic, SAPIEN, Hillbot, Disney Research.

## [2026-05-07] lint | Wikilink convention migration
- Issue: my initial pages used bare `[[Display Title]]` wikilinks but kebab-case filenames, so Obsidian couldn't resolve them and created empty placeholder files at the vault root for [NVIDIA Isaac Sim](entities/nvidia-isaac-sim.md), [NVIDIA Newton Physics Engine Developer Page](sources/nvidia-newton-physics-engine-developer-page.md), and [World-model simulators](concepts/world-model-simulators.md).
- Resolution: deleted the 3 zero-byte orphans; rewrote all wikilinks across 28 pages to the explicit `[[slug|Display]]` form via `sed`.
- CLAUDE.md updated with the filename convention (kebab-case slugs) and the wikilink convention (always slug-pipe-display, never bare display).

## [2026-05-07] lint | Wiki health check pass
- Deleted second Obsidian orphan: `wiki/Genie Envisioner Paper.md` (empty 0-byte file).
- Reconciled NVIDIA mention drift: added `[NVIDIA](entities/nvidia.md)` to [AGIBOT Genie Sim 3.0 Announcement](sources/agibot-genie-sim-3-announcement.md)'s "Entities mentioned" list, since the source genuinely discusses NVIDIA's stack via Isaac Sim and GR00T.
- Bumped `sources` counts on 7 entity pages whose frontmatter under-counted actual inbound source-page wikilinks: [AGIBOT Genie Sim 3.0](entities/agibot-genie-sim.md) (1→3), [Genesis](entities/genesis.md) (1→2), [Genie Envisioner](entities/genie-envisioner.md) (2→3), [MuJoCo Playground](entities/mujoco-playground.md) (1→2), [Newton physics engine](entities/newton-physics-engine.md) (2→3), [NVIDIA Cosmos](entities/nvidia-cosmos.md) (2→3), [NVIDIA Isaac Lab](entities/nvidia-isaac-lab.md) (2→3). Mirrored counts in `index.md`.
- No content contradictions found beyond the already-tracked GR00T N1.6/N1.7 EA version overlap.
- Deferred to user: whether to stub frequently-mentioned-but-unstubbed entities (Hillbot, SAPIEN, Disney Research).

## [2026-05-07] stubs | Filled three lint-flagged entity gaps
- Created stub pages for [Hillbot](entities/hillbot.md) (UCSD spinoff, ManiSkill maintainer), [SAPIEN](entities/sapien.md) (simulation framework underlying ManiSkill), and [Disney Research](entities/disney-research.md) (Newton co-developer).
- Converted bare text mentions to wikilinks across `entities/maniskill.md` (Hillbot + SAPIEN ×3), `entities/newton-physics-engine.md`, `entities/google-deepmind.md`, `entities/nvidia.md`, `syntheses/simulators-for-agentic-robotics-2026.md` (Hillbot + SAPIEN + Disney in the Newton table cell), and added entries to `Entities mentioned` sections in `sources/maniskill-hab-paper.md` (Hillbot, SAPIEN) and `sources/nvidia-newton-physics-engine-developer-page.md` (Disney Research).
- Removed the three corresponding rows from `index.md` "Known gaps / TBD"; added the new stubs to Companies / Simulators sections.
- Updated synthesis "Coverage gaps" to drop SAPIEN (now stubbed); Drake remains.

## [2026-05-07] ingest | Hello Robot ecosystem (4 sources)
- **Sources ingested**: [Hello Robot Stretch Documentation](sources/hello-robot-stretch-docs.md) (https://docs.hello-robot.com/0.3/), [Robot Utility Models Project Page](sources/robot-utility-models-website.md) (https://robotutilitymodels.com/), [Stretch AI LLM Agent Documentation](sources/stretch-ai-llm-agent-docs.md) (github.com/hello-robot/stretch_ai), and `raw/22486_RoboCasa365_A_Large_Scal.pdf` — re-ingested with deeper detail (the existing [RoboCasa365 Paper](sources/robocasa365-paper.md) page was rewritten).
- **PDF tooling**: poppler-utils binaries weren't on PATH; `pypdf` was available, used a short Python script to extract pages 1–3 of the PDF. Found ICLR 2026 conference paper, full author list (Soroush Nasiriany, Sepehr Nasiriany, Abhiram Maddukuri, Yuke Zhu), and richer numbers (612 hr human + 1615 hr synthetic via [MimicGen](entities/mimicgen.md); 500K+ trajectories; 60 distinct activities behind the 365 tasks).
- **New entity pages** (5): [Hello Robot](entities/hello-robot.md) (company), [Stretch](entities/stretch.md) (robot), [stretch_ai](entities/stretch-ai.md) (software stack), [Robot Utility Models](entities/robot-utility-models.md) (method), [MimicGen](entities/mimicgen.md) (tool, stub).
- **New concept pages** (2): [Imitation learning](concepts/imitation-learning.md), [LLM-agent architecture](concepts/llm-agent-architecture.md).
- **Updated existing pages**: [RoboCasa](entities/robocasa.md) (added ICLR 2026 / authors / NVIDIA / MimicGen), [NVIDIA](entities/nvidia.md) (sources 4→5; new "Research arm" bullet about Yuke Zhu's NVIDIA Research affiliation on RoboCasa365), [VLA models](concepts/vla-models.md) (sources 4→6; new "Adjacent: utility models" section noting RUMs and stretch_ai's LLM agent are non-language-conditioned alternatives), [Sim-to-real transfer](concepts/sim-to-real-transfer.md) (sources 2→3; RoboCasa365 added as benchmark), and the synthesis (new section 6 "Real-robot agentic stacks" highlighting stretch_ai and RUM as the consumer-side counterweight to sim-heavy paths).
- **Index reorganized**: added "Robot platforms", "Software stacks", and "Tools" subsections under Entities; renamed "VLA models" → "VLA models / generalist policies"; added 5 new TBD items (TRI LBM, Octo, Stretch Mujoco, xArm 7, RUM/Hello Robot people).
- **New cross-source insight**: Aaron Edsinger (Hello Robot co-founder) is a co-author on the RUM paper — concrete vendor / academic collaboration explicitly bridging the hardware vendor to the generalist-policy research agenda.

## [2026-05-07] ingest | JEPA papers (V-JEPA 2 + LeWorldModel)
- **Sources ingested** (2): [V-JEPA 2 Paper](sources/v-jepa-2-paper.md) (`raw/JEPA_2506.09985v1.pdf`, arXiv 2506.09985, June 2025) and [LeWorldModel Paper](sources/leworldmodel-paper.md) (`raw/LeWorldMode_2603.19312v2.pdf`, arXiv 2603.19312v2, March 2026). Both extracted via pypdf.
- **New entity pages** (4): [V-JEPA 2](entities/v-jepa-2.md), [LeWorldModel](entities/leworldmodel.md), [Meta FAIR](entities/meta-fair.md), [Mila](entities/mila.md) (stub).
- **New concept page** (1): [Joint-Embedding Predictive Architecture](concepts/jepa.md) — umbrella architecture for both papers.
- **Restructured concept**: [World-model simulators](concepts/world-model-simulators.md) now organized as two explicit paradigms — Paradigm A (generative-video: Cosmos, Genie Envisioner) and Paradigm B (JEPA / latent-prediction: V-JEPA 2, LeWorldModel). Sources 2→4.
- **Synthesis updates**: section 3 split into 3a (generative-video) and 3b (JEPA / latent-prediction); intro reads "Six categories" (was "Five"); sources list refreshed to include the four sources added since the last synthesis update (stretch-ai docs, RUM website, V-JEPA 2, LeWorldModel).
- **Cross-link**: [NVIDIA Cosmos](entities/nvidia-cosmos.md) now cross-references the JEPA line as the contrasting paradigm.
- **Cross-source insight**: Yann LeCun is senior author on both papers — JEPA is his program, executed across two distinct teams (Meta FAIR for V-JEPA 2; Mila + NYU + Samsung + Brown for LeWM). The two papers represent **different points in the same design space**: V-JEPA 2 is large-scale + frozen-encoder + post-training; LeWM is small + end-to-end + simple. Together they argue JEPA is robust across scale.
- **Quantitative contrast captured**: V-JEPA 2 trains on **1M+ hours** with **1B parameters**; LeWM uses **15M parameters** on a single GPU. 60-70× model-size delta and ~5 orders of magnitude data delta — yet both are JEPAs and both demonstrate the paradigm.
- **TBD added**: DINO-WM, Dreamer/DreamerV3, TD-MPC, PLDM (world-model baselines from LeWM), Droid dataset (V-JEPA 2-AC training), Habitat (Meta), and a low-priority people-pages note (LeCun, Edsinger, Shafiullah, Zhu, Assran).

## [2026-05-07] ingest | Hiwonder ROSOrin documentation
- **Source ingested**: [Hiwonder ROSOrin Documentation](sources/hiwonder-rosorin-docs.md) (https://docs.hiwonder.com/projects/ROSOrin/en/jetson-orin-nano-version/). User specifically asked to include the Gazebo section; pulled chapter 9 (Gazebo) and chapter 10 (Large AI Models incl. Embodied AI + offline) by curl + Python parsing of the Sphinx HTML. WebFetch's summarizer truncated the AI chapter mid-page on first attempts; raw curl + grep was needed for sections 10.3–10.5.
- **New entity pages** (4): [Hiwonder](entities/hiwonder.md) (stub), [ROSOrin](entities/rosorin.md) (full), [Ollama](entities/ollama.md) (stub), [Qwen](entities/qwen.md) (stub but cross-references stretch_ai).
- **No new concept pages** — content fits the existing [LLM-agent architecture](concepts/llm-agent-architecture.md) concept.
- **Updated existing**: [LLM-agent architecture](concepts/llm-agent-architecture.md) (sources 1→2; added ROSOrin as a second concrete example, noting the pattern is converging across research and educational tiers); [stretch_ai](entities/stretch-ai.md) (sources 2→3 from new ROSOrin-docs cross-reference); [stretch_ai LLM Agent Documentation](sources/stretch-ai-llm-agent-docs.md) (wikilinked Qwen instead of bare text; corrected vendor attribution from "Tencent" to Alibaba); synthesis section 6 (added ROSOrin as the educational-tier counterpart to stretch_ai); synthesis sources list refreshed.
- **Index reorganized**: added "LLMs" subsection under Entities; expanded Robot platforms (now Stretch + ROSOrin); added Hiwonder to Companies; added Ollama to Tools.
- **Concrete agentic-AI tooling captured**:
  - **Cloud LLMs** in ROSOrin chapter 10: GPT-4o, GPT-4o-mini, gpt-4o-transcribe, Whisper-1, OpenAI TTS (tts-1/tts-1-hd/gpt-4o-mini-tts), Qwen-plus-latest, StepFun multimodal (Chinese fallback path).
  - **Offline stack**: ollama serve + qwen3:1.7b + sherpa-onnx (CUDA) + matcha-icefall-zh-baker (Chinese TTS) + vits-ljs (English TTS).
  - **Embodied-AI control loop**: LLM emits `{action: [...], response: ...}` JSON, executor runs `eval(f'self.{a}')` per action — security-questionable but a clear standard recipe.
- **Cross-source convergence insight**: stretch_ai (research, Hello Robot) and ROSOrin (education, Hiwonder) independently default to small Qwen variants (2.5-3B and 3:1.7b) for their LLM-agent planners. The same JSON tool-call architectural pattern is shared across two unrelated stacks. The wiki now treats this as a confirmed pattern rather than a single data point.
- **TBD added**: Gazebo entity page (referenced by both Hello Robot and Hiwonder docs; previously was a passing mention), TurtleBot (canonical educational ROS robot), StepFun (Chinese multimodal AI), sherpa-onnx (offline ASR/TTS toolkit), WonderEcho Pro (Hiwonder voice module), Hiwonder's chapter 7 vision/CV curriculum (YOLOv11 + TensorRT — could be its own ingest).

## [2026-05-07] ingest | ROSOrin Pro / OpenClaw (manipulation-capable Hiwonder variant)
- **Sources ingested** (2): [Hiwonder ROSOrin Pro User Manual](sources/hiwonder-rosorin-pro-user-manual.md) (chapter 1) and [Hiwonder OpenClaw Practical Tutorial](sources/hiwonder-openclaw-tutorial.md) (chapter 13). The overview-page URL the user supplied was browsed for TOC structure but not filed as a separate source page (per scope choice — it was largely TOC).
- **New entity pages** (3): [ROSOrin Pro](entities/rosorin-pro.md) (the kit), [OpenClaw](entities/openclaw.md) (the LLM-agent framework — software, not hardware despite the "Claw" suffix), [ROSOrin Pro 6-DOF arm](entities/rosorin-pro-arm.md) (stub for the HX-12H-servo manipulator hardware).
- **Updated existing**: [ROSOrin](entities/rosorin.md) (added Pro variant to Related), [Hiwonder](entities/hiwonder.md) (sources 1→3; documented the two-doc-domain split — `docs.hiwonder.com` for base, `wiki.hiwonder.com` for Pro), [LLM-agent architecture](concepts/llm-agent-architecture.md) (sources 2→3; added OpenClaw as third concrete example, generalized the convergence claim from "across tiers" to "across tiers and capabilities"), synthesis section 6 (extended ROSOrin bullet to cover the Pro variant + OpenClaw), synthesis sources list, index (added rosorin-pro, rosorin-pro-arm, openclaw under their respective sections; bumped Hiwonder source count and reorganized so Hiwonder appears earlier in Companies).
- **Hardware specs captured** (now reusable for future ingests): COIN-D6 LiDAR, Deptrum Aurora930 depth + RGB camera, MPU6050 IMU, HX-12H bus servos, STM32F407VET6 low-level MCU, 11.1 V 6000 mAh battery.
- **Concrete OpenClaw skill surface captured**: ROS 2 services `/start_pick`, `/place`, `/claw_track_and_grab/start`, `/claw_track_and_grab/set_color`, topics `~/arm_group_control`, `~/chassis_command`, `/controller/cmd_vel`. Action groups: `voice_pick`, `voice_give`, `init`, `camera_up`. Functions: `parse_twist()`, `pick()`, `place_function()`, `obj_track_proc()`. Vision: LAB-color thresholding + PID visual servoing + AprilTag (ID 0/1) + depth-based interactive grasping (Jetson Orin only).
- **Cross-source convergence insight strengthened**: The LLM-agent pattern is now demonstrated across **three independent stacks** — [stretch_ai](entities/stretch-ai.md) (Hello Robot, research, mobile + arm), [ROSOrin](entities/rosorin.md) (Hiwonder, education, mobile-only), and [OpenClaw](entities/openclaw.md) (Hiwonder, education, mobile + arm). Same JSON tool-call architecture, same skill-library dispatch model. The claim has shifted from "this might be a pattern" to "this is the pattern" for non-VLA agentic-robotics deployment in 2026.
- **Notable absences in OpenClaw curriculum**: no VLA models (no OpenVLA/GR00T/RT-X/Pi), no LeRobot, no ACT or Diffusion Policy, no imitation learning, no teleoperation, no demonstration collection. Confirms the bifurcation already noted in the synthesis: VLA work happens in research labs (NVIDIA, Pi, Meta-via-RUM); deployed agentic stacks use LLM-orchestrated skill libraries.
- **Open question logged**: doc references `openai/gpt-5.4` — unclear if real OpenAI release or doc placeholder. Worth checking on the next OpenAI-related ingest.
- **TBD additions**: HX-12H, COIN-D6, Deptrum Aurora930, MPU6050 — hardware-component pages added as a single TBD line in the index (deferred until they recur).

## [2026-05-07] synthesis | LLM-agent architecture across stacks
- Filed [LLM-agent architecture across stacks — a converged pattern](syntheses/llm-agent-architecture-across-stacks.md).
- Three-way side-by-side comparison of [stretch_ai](entities/stretch-ai.md), [ROSOrin](entities/rosorin.md), and [OpenClaw](entities/openclaw.md). Goes beyond the umbrella [LLM-agent architecture](concepts/llm-agent-architecture.md) concept by drawing structural implications — Qwen as the de-facto local default, JSON-shaped tool calls as the provider-portability layer, the bifurcation between research VLA stacks and deployed LLM-agent stacks.
- Surfaced two implementation hazards: `eval`-on-LLM-output dispatch in both Hiwonder stacks, and under-documented closed-loop replanning across all three.
- Open questions filed: no Claude backend anywhere; cross-vendor portability of skill libraries; whether VLAs eventually displace primitives without changing the orchestrator pattern.

## [2026-05-07] synthesis | Generative-video vs JEPA world models
- Filed [Generative-video vs JEPA world models](syntheses/generative-video-vs-jepa-world-models.md).
- Deep comparison of paradigms A and B from [World-model simulators](concepts/world-model-simulators.md). Five-table treatment: what each predicts, cost/speed, data scale, demonstrated real-robot results, failure modes — plus when-to-use guidance and a cross-paradigm interaction note (GR00T using Cosmos backbone; V-JEPA 2 encoder feeding multimodal LLMs).
- Anchored on the 48× planning-speed gap (LeWM) and the V-JEPA 2-AC zero-shot Franka result as the strongest published cross-paradigm validation.
- Open questions filed: no published head-to-head; GE-Sim2 zero-shot transfer evidence missing; JEPA scaling-law shape between 15M and 1B params; whether action-conditioned generative video can match V-JEPA 2-AC's data-efficiency.

## [2026-05-07] lint | Post-synthesis health check
- Cross-checked wikilinks: all 34 unique slugs referenced from the two new syntheses resolve to existing files. No broken links anywhere in the wiki (the only "Referenced but no file" hit was the literal `slug` example inside CLAUDE.md docs).
- No new orphan pages created by these syntheses.
- No source-count drift to fix — syntheses do not appear in `Mentioned in` sections by convention.
- One normalization: synthesis #1 originally used escaped pipes (`\|`) inside markdown-table wikilinks for delimiter safety; rewrote to unescaped `|` to match the rest of the wiki (the existing simulators synthesis uses unescaped pipes inside tables and renders correctly in Obsidian).
- No content contradictions detected between the two new syntheses and existing pages.
- Standing open items unchanged: GR00T N1.6 GA vs N1.7 EA contradiction, Pi / Skild AI coverage gap, Drake / Gazebo entity pages.

## [2026-05-07] synthesis | Newton + OpenUSD substrate convergence
- Filed [Newton + OpenUSD — the substrate convergence](syntheses/newton-openusd-substrate-convergence.md).
- Argues the structural unusual-ness of a physics engine designed as a backend pluggable into both NVIDIA Isaac Lab and DeepMind's MuJoCo Playground, with OpenUSD as the shared scene format and Linux Foundation as the vendor-neutral governance layer. Implication: physics layer commoditizes, ML differentiation moves up the stack to environment APIs / learning frameworks / VLAs.
- Disney Research's role flagged as the puzzle piece — entertainment-grade physics keeping Newton's contact / soft-body models honest beyond industrial robotics.
- Open questions filed: real cross-stack adoption demo not yet ingested; throughput-parity comparisons absent; whether MuJoCo Playground defaults to Newton or keeps MJX as primary; Disney's specific contributions still opaque.

## [2026-05-07] synthesis | Sim-heavy vs real-data paths to generalist policies
- Filed [Sim-heavy vs real-data paths to generalist policies](syntheses/sim-heavy-vs-real-data-paths.md).
- Reframes the simulator survey's "sim-vs-real divide" as a three-path comparison: Path A (sim-heavy synthetic-data scaling — RoboCasa365, Genie Sim 3.0), Path B (real-data viewpoint-locked — RUM), Path C (observation pretraining + small interaction — V-JEPA 2-AC). Different data-substitution bets, different scaling axes.
- Empirical asymmetry surfaced: Path B and Path C have published zero-shot real-robot results in unseen environments (RUM 90% on 5 tasks; V-JEPA 2-AC zero-shot Franka in 2 labs); Path A's evidence in the wiki is mostly intra-sim. The wiki has not ingested deep VLA-deployment results that would close this gap.
- Concrete number captured: RoboCasa365's 2.6× synthetic-to-human ratio is the wiki's only data point on Path A's optimal sim/real mix.
- Open questions filed: Pi / Skild positioning on this map; synthetic-ratio plateau; missing direct head-to-head training the same architecture across all three paths.

## [2026-05-07] lint | Final health check after four syntheses
- Cross-checked wikilinks: all slugs referenced from the four new syntheses resolve. The only "Referenced but no file" hit remains the literal `slug` example inside CLAUDE.md docs.
- No orphan pages created across the four syntheses.
- No escaped pipes (`\|`) anywhere in `wiki/syntheses/`; convention is consistent.
- Added a "Deeper dives" cross-reference section at the bottom of the simulator survey pointing to the four follow-up syntheses, since each takes one section of the survey further. Bumped the survey's `updated` to 2026-05-07.
- Synthesis count: 1 (survey, updated) + 4 (new) = 5 on file.
- No content contradictions detected between the four new syntheses or between them and the simulator survey. The standing GR00T N1.6 GA / N1.7 EA inconsistency is referenced consistently across pages.
- Standing TBD items unchanged: Pi (Physical Intelligence), Skild AI, Drake internals, classic VLA benchmarks (LIBERO / RoboMimic). The four new syntheses surface these gaps from new angles but do not fill them.

## [2026-05-07] research | OpenUSD as a robotics scene/physics format
- User asked to research OpenUSD as a scene-description format for simulators, then asked to also explore SolidWorks-to-OpenUSD conversion. Web search (4 queries) + WebFetch (4 successful + 1 403) + 1 follow-up search.
- **Sources ingested** (4): [OpenUSD Rigid Body Physics Proposal](sources/openusd-rigid-body-physics-proposal.md) (openusd.org, 2020 v1.0), [Using OpenUSD for Modular and Scalable Robotic Simulation](sources/nvidia-openusd-for-robotic-simulation.md) (NVIDIA blog 2025-03-18 by Aaron Luk, Pomi Lee, Renato Gasoto), [URDF vs MJCF vs USD comparison](sources/source-robotics-urdf-mjcf-usd-comparison.md) (Source Robotics blog 2026-03-13), [Building CAD-to-USD Workflows with NVIDIA Omniverse](sources/nvidia-cad-to-usd-jt-workflows.md) (NVIDIA blog 2025-07-29 by Justine Lin).
- **New entity page** (1): [OpenUSD](entities/openusd.md) — covers the format, the UsdPhysics schema, MjcPhysics + newton-usd-schemas extensions, and CAD ingestion paths.
- **Updated existing**: [Google DeepMind](entities/google-deepmind.md) (sources 2→3; documented authorship of the `MjcPhysics` USD plugin and `mujoco-usd-converter`); [Newton physics engine](entities/newton-physics-engine.md) (sources 3→4; added the `newton-usd-schemas` repo and the schema-promotion-into-UsdPhysics design); [Newton + OpenUSD substrate convergence synthesis](syntheses/newton-openusd-substrate-convergence.md) (substantial enrichment — added the "OpenUSD as physics schema" section, the "DeepMind authors USD plugins" section, the "CAD ingestion — the upstream half" section, and updated the convergence table to include physics-schema and CAD-ingestion rows).
- **Key new claims captured**:
  - **UsdPhysics is robotics-aware in the standard**. `PhysicsArticulationRootAPI` distinguishes "floating articulations" (mobile/aerial robots) from "fixed articulations" (industrial arms bolted down) — robotics jargon explicitly recognized in the OpenUSD spec.
  - **DeepMind ships USD schema plugins**, not just consumes USD. `MjcPhysics` is a DeepMind-maintained USD plugin authoring MuJoCo-specific solver attributes onto USD prims.
  - **`newton-usd-schemas` is a "proving ground"** — physics parameters generalizable across two Newton solvers may be promoted upstream into `UsdPhysics`. v0.2.0 released **2026-05-07** (the same day as this ingest), 52 commits, 7 releases — actively maintained.
  - **`mujoco-usd-converter`** lives in the `newton-physics` GitHub org, hosting the cross-stack bridge in vendor-neutral governance.
  - **CAD-to-USD geometry preservation is good; kinematic-joint preservation is the open question**. None of the ingested CAD sources documents automated SolidWorks-mate-to-`PhysicsJoint` conversion.
  - **Isaac Sim 5.0 / Omniverse Kit SDK 107 → OpenUSD 24.05**.
- **Open questions logged**: ABB/FANUC/KUKA/Yaskawa GTC 2026 adoption needs a primary source; URDF/MJCF/SDFormat → OpenUSD conceptual mapping shipping status; engineering.com 403 redo.
- **Skipped sources** (deliberately): Okino SolidWorks-to-USD page (thin), newton-usd-schemas GitHub README (folded into the Newton entity page).

## [2026-05-07] lint | Post-OpenUSD-ingest health check
- All wikilinks resolve; no orphan pages; no escaped pipes in new content.
- **Source-count drift fixed** on six entity pages whose frontmatter under-counted inbound source-page references after the ingest: [NVIDIA](entities/nvidia.md) 5→8, [NVIDIA Isaac Sim](entities/nvidia-isaac-sim.md) 2→4, [Newton physics engine](entities/newton-physics-engine.md) 3→4 (already in ingest commit), [NVIDIA Cosmos](entities/nvidia-cosmos.md) 4→5, [Google DeepMind](entities/google-deepmind.md) 2→3 (already in ingest commit), [Disney Research](entities/disney-research.md) 1→2. Mirrored counts in `index.md`.
- **Removed a stray `Mentioned in` entry**: I had added `openusd-rigid-body-physics-proposal` under [Newton](entities/newton-physics-engine.md)'s "Mentioned in" but that source page does not list Newton in its "Entities mentioned" — only OpenUSD and NVIDIA. Removed.
- **Added missing `Mentioned in` entries**: appended the four new sources to the relevant entity pages (NVIDIA, Isaac Sim, Cosmos, Disney Research, Newton, DeepMind) per the convention.
- DeepMind's `_stub_` marker dropped from index since the entity page now has 3 sources and substantive content (MjcPhysics + Newton + MuJoCo).

## [2026-05-07] synthesis | LeWorldModel — train and run howto
- Filed [LeWorldModel — train and run howto](syntheses/leworldmodel-howto.md) from `lucas-maes/le-wm` README + project page.
- Updated [LeWorldModel Paper](sources/leworldmodel-paper.md): added `code` and `project_page` frontmatter; resolved the "code/website URLs missing" open question; added a Code & artifacts section.
- Updated [LeWorldModel](entities/leworldmodel.md): added Code section + howto link; bumped sources 1 → 2.
- Updated [index.md](index.md): filed howto under Syntheses.

## [2026-05-07] update | LeWorldModel howto: install gotchas added
- Installed and verified `quentinll/lewm-pusht` end-to-end on RTX 5070 / WSL2 / Python 3.10.
- Updated [LeWorldModel — train and run howto](syntheses/leworldmodel-howto.md) with a Gotchas section covering four real snags: gym 0.21.0 PEP 440 metadata, box2d-py SWIG dep, datasets resolved to 1.1.1, and the README conversion script's missing `_target_` filter.
- Expanded the "use pretrained" section with the actual HF→`_object.ckpt` conversion script + the `strip_target` fix.

## [2026-05-07] ingest | Farama Foundation Projects Page
- Source: [Farama Foundation Projects Page](sources/farama-projects-page.md) (https://farama.org/projects).
- New entities (focused scope): [Farama Foundation](entities/farama-foundation.md), [Gymnasium](entities/gymnasium.md), [PettingZoo](entities/pettingzoo.md), [Gymnasium-Robotics](entities/gymnasium-robotics.md).
- Cross-referenced gym/gymnasium gotchas in [LeWM howto](syntheses/leworldmodel-howto.md) to the new Gymnasium entity.
- Deferred: Minari, Metaworld, Shimmy, MO-Gymnasium, MOMAland, MAgent2, MPE2, Minigrid, MiniWoB++, ViZDoom, ALE, HighwayEnv, Procgen2, Stable-Retro, Jumpy — listed in index "Known gaps" with the source page as the canonical reference.

## [2026-05-07] ingest | Gymnasium-Robotics Documentation
- Source: [Gymnasium-Robotics Documentation](sources/gymnasium-robotics-docs.md) (https://robotics.farama.org/).
- Expanded [Gymnasium-Robotics](entities/gymnasium-robotics.md) from stub to real entity: confirmed MuJoCo backend (new bindings, not legacy mujoco-py), enumerated all six env families (Fetch, Shadow Hand, Maze, Adroit, Franka Kitchen, MaMuJoCo), added install snippet.
- Bumped source counts: gymnasium-robotics 1→2, gymnasium 1→2, farama-foundation 1→2.
- Added six env families to "Known gaps" for on-demand promotion (Adroit + Franka Kitchen most likely to surface, given D4RL / RoboCasa365 evaluation traditions).

## [2026-05-07] lint | Source-count drift fixes + MuJoCo entity
- Fixed source counts: [LeWorldModel](entities/leworldmodel.md) 2→1 (synthesis pages don't count per schema); [PettingZoo](entities/pettingzoo.md) 1→2; [MuJoCo Playground](entities/mujoco-playground.md) 3→5; [NVIDIA Isaac Lab](entities/nvidia-isaac-lab.md) 3→4. Index updated to match.
- New entity: [MuJoCo](entities/mujoco.md) — the physics engine itself (was a 110-mention gap). 7 source pages reference it; entity covers `mujoco` vs `mujoco-py` vs MJX vs MJCF, history (Roboti → DeepMind 2021), and ecosystem role.
- Qualified the speculative "single-process CPU MuJoCo" claim on [Gymnasium-Robotics](entities/gymnasium-robotics.md) with a `> [!note]` callout — the docs root didn't actually state CPU-only.
- No broken wikilinks, no orphans, no contradictions surfaced.

## [2026-05-07] synthesis | OpenUSD support across simulators
- Filed [OpenUSD support across simulators](syntheses/openusd-support-across-simulators.md) — reference catalog of which simulators consume USD natively (Isaac Sim/Lab, Genie Sim 3.0), via plugin (MuJoCo via MjcPhysics + mujoco-usd-converter), as substrate (Newton via newton-usd-schemas), or not at all (Genesis, ManiSkill/SAPIEN, Gymnasium-Robotics).
- Companion to [Newton + OpenUSD — the substrate convergence](syntheses/newton-openusd-substrate-convergence.md) (structural argument) and [OpenUSD entity](entities/openusd.md) (format reference). Compiles the per-simulator answer into a single grep-able page.
- Updated [index.md](index.md): filed under Syntheses.

## [2026-05-07] synthesis | Why JEPA research skips the simulator stack
- Filed [Why JEPA research skips the simulator stack](syntheses/why-jepa-research-skips-the-simulator-stack.md) — synthesis observing that V-JEPA 2 and LeWorldModel both avoid heavy agentic-robotics simulators (Isaac Lab, MuJoCo Playground, ManiSkill, RoboCasa, Genesis).
- V-JEPA 2: internet video pretrain → real Droid teleop post-train → real Franka zero-shot eval (no sim anywhere). LeWM: trains/evals on PushT/cube/two-rooms/reacher (lightweight 2D/3D control benches, not real-robot sim).
- Four plausible reasons: (1) JEPA's data thesis is observation-scale, internet video beats sim; (2) latent-space prediction sidesteps pixel-level sim-to-real gap; (3) Droid removes sim's data-multiplier role; (4) test-of-truth is real-robot zero-shot.
- Caveats explicit: sample size of two; `stable-worldmodel` env zoo may extend further than ingested; future JEPA work may converge back into sim once it scales up.
- Updated [index.md](index.md): filed under Syntheses.

## [2026-05-07] ingest | Five JEPA / JEPA-adjacent papers (probe of original synthesis)
- Triggered by: user query "find more information about JEPA and LeWorldModel and probe whether these methods use simulations." Research agent surfaced one paper that contradicts the original ["JEPA skips sim" synthesis](syntheses/why-jepa-research-skips-the-simulator-stack.md) and four more that broaden the picture.
- New sources:
  - [JEPA-WMs Paper](sources/jepa-wms-paper.md) (Terver, Yang, Ponce, Bardes, LeCun — FAIR, Dec 2025) — **first JEPA-for-robotics paper this wiki has ingested using heavy sim**: RoboCasa kitchen manipulation + 42 Metaworld tasks + Push-T + PointMaze + DROID + real Franka.
  - [V-JEPA 2.1 Paper](sources/v-jepa-2-1-paper.md) (Mur-Labadia et al. — FAIR + Mila, Mar 2026) — "dense features"; +20pt real-Franka grasping per secondary research; sustains the no-sim line.
  - [DINO-WM Paper](sources/dino-wm-paper.md) (Zhou, Pan, LeCun, Pinto — NYU + FAIR, Nov 2024) — DINOv2 patch features + zero-shot planning on PushT/Wall/PointMaze/Rope/Granular/Reacher.
  - [VLA-JEPA Paper](sources/vla-jepa-paper.md) (Sun et al., Feb 2026) — JEPA-as-auxiliary inside VLA on LIBERO + SimplerEnv + real.
  - [DINO-world Paper](sources/dino-world-paper.md) ("Back to the Features", Baldassarre et al. — FAIR, Jul 2025) — DINOv2 video world model; Basile Terver bridge author to JEPA-WMs.
- New entities: [JEPA-WMs](entities/jepa-wms.md), [DINO-WM](entities/dino-wm.md), [VLA-JEPA](entities/vla-jepa.md), [DINO-world](entities/dino-world.md).
- Updated entities: [Meta FAIR](entities/meta-fair.md) sources 1→5, expanded JEPA-program description to include both encoder-co-trained (V-JEPA family) and frozen-DINOv2 (DINO-WM/DINO-world/JEPA-WMs) lines; [V-JEPA 2](entities/v-jepa-2.md) sources 1→2 + V-JEPA 2.1 successor note; [RoboCasa](entities/robocasa.md) sources 1→2 with JEPA-WMs cross-reference; [MuJoCo](entities/mujoco.md) sources 6→7 (DINO-WM uses it).
- Updated concept: [JEPA](concepts/jepa.md) sources 2→7; added all 5 new instances; added "Simulator stance — fragmenting, not avoiding" section; cross-referenced revised synthesis.
- Index updated: 5 new sources under chronological list, 4 new world-model entities, JEPA concept source-count bump, JEPA-related expansion gaps section added.

## [2026-05-07] synthesis | Major revision — Why JEPA research skips the simulator stack
- Rewrote [the synthesis](syntheses/why-jepa-research-skips-the-simulator-stack.md) in response to JEPA-WMs ingest (which directly contradicts the original claim).
- New framing: JEPA literature **fragments across four sim weight classes** (none / lightweight / mid-weight / heavy), not "skips sim wholesale." Original V-JEPA 2 + LeWM observation is correct for those papers but does not generalize.
- Each sim weight class explained by paper-specific question (representation learning vs. training-method vs. VLA-eval vs. physical-planning benchmark).
- The four "why" hypotheses from the original draft re-labeled: only (a) "internet-scale video > sim" has direct primary-source backing; (b)/(c)/(d) are wiki-author inference, not paper rationale.
- Two corrections folded in: `stable-worldmodel` env zoo includes DM Control + Gymnasium-Robotics Fetch (broader than the LeWM howto exposed); DINO-world → JEPA-WMs share research lineage via Basile Terver bread-crumb.
- New "watch item": first JEPA paper to explicitly train inside Isaac Lab or MuJoCo Playground (RoboCasa happened in Dec 2025; those two haven't yet).

## [2026-05-07] entity | DROID dataset
- Created [DROID](entities/droid.md) entity page — Distributed Robot Interaction Dataset, 350 hr / 76k traj / 564 scenes / 86 tasks of Franka Panda teleop across 13 institutions; lead authors Khazatsky + Pertsch, senior Finn + Levine. Source: project page at https://droid-dataset.github.io/.
- Captured the OXE comparison (DROID +22% in-dist / +17% OOD vs Open-X Embodiment policies) and the BridgeV2/RH20T/RT-1 "order of magnitude more scenes" claim.
- Wikilinked DROID across [V-JEPA 2](sources/v-jepa-2-paper.md) and [JEPA-WMs](sources/jepa-wms-paper.md) sources so Mentioned-in flows correctly.
- Index updated: added Datasets subsection under Entities; removed DROID from Known gaps. Added Franka Panda + DROID-paper-itself to Known gaps as follow-ups.
- Open: DROID **paper itself** (arxiv 2403.12945) not yet a source page; license terms not surfaced; Dec 2024 / Apr 2025 update deltas not documented.

## [2026-05-07] entities | Batch 1 — Franka Panda + Metaworld + DINOv2 + PushT + 3 people + world-model concept
- Filed 8 pages in one batch in response to "recommend entities, then file batch 1":
  - [Franka Panda](entities/franka-panda.md) — 7-DOF research arm; default tabletop manipulator across DROID, V-JEPA 2, V-JEPA 2.1, JEPA-WMs, RUM. (4 sources)
  - [Metaworld](entities/metaworld.md) — Yu/Quillen/Levine/Finn 2019 meta-RL benchmark; 50 manipulation tasks on simulated Sawyer; staple in JEPA-WMs (42 tasks) + MuJoCo Playground. (3 sources)
  - [DINOv2](entities/dinov2.md) — Meta FAIR self-supervised ViT (Oquab et al. 2023); 142M images, ViT-S/B/L/g; substrate for DINO-WM, DINO-world, JEPA-WMs. Apache 2.0. (3 sources)
  - [PushT](entities/pusht.md) — 2D T-block pushing benchmark; introduced by IBC (Florence et al. 2021), popularized by Diffusion Policy (Chi et al. 2023). Default lightweight bench across LeWM / DINO-WM / JEPA-WMs. (3 sources)
  - [Yann LeCun](entities/yann-lecun.md) — Meta VP, NYU, Turing Award 2018; senior on V-JEPA 2 / V-JEPA 2.1 / LeWM / DINO-WM / DINO-world / JEPA-WMs. (6 sources)
  - [Adrien Bardes](entities/adrien-bardes.md) — FAIR; co-senior on V-JEPA 2 / V-JEPA 2.1 / JEPA-WMs; the FAIR-side champion of the V-JEPA program. (3 sources)
  - [Basile Terver](entities/basile-terver.md) — bread-crumb author across DINO-world (Jul 2025) → JEPA-WMs (Dec 2025), the lineage signal called out in the JEPA-skips-sim synthesis. (2 sources)
  - [World model](concepts/world-model.md) — broad concept page, distinct from the narrower [World-model simulators](concepts/world-model-simulators.md) companion. Covers generative-video / JEPA / frozen-feature / model-based-RL design points. (11 sources)
- Sources for these pages were drawn from the existing wiki + a small primary-source pass on Metaworld (project page), DINOv2 (GitHub README), PushT (Diffusion Policy project page).
- Primary sources note: people pages (LeCun, Bardes, Terver) are written from the wiki's own author-overlap context plus widely-known facts; primary-source bio fetches deferred.
- Index updated: new Vision foundation models subsection (DINOv2); new People subsection (LeCun, Bardes, Terver); Franka Panda added under Robot platforms; Metaworld + PushT added under Simulators / frameworks; World-model concept added at top of Concepts.
- Known gaps cleaned: Franka Panda removed; Metaworld removed from Farama gap list; LeCun removed from People-low-priority list. Added new gaps surfaced by ingest: Sergey Levine, Chelsea Finn, Karl Pertsch, Alexander Khazatsky, Lerrel Pinto, Pulkit Agrawal as future people pages.
- Open: bidirectional source-to-entity cross-links (e.g. adding [Yann LeCun](entities/yann-lecun.md) under "Entities mentioned" in V-JEPA 2 + LeWM + DINO-WM + DINO-world + JEPA-WMs source pages) **not done in this pass** — would tighten the graph but isn't load-bearing for retrieval. Worth a future lint pass.

## [2026-05-08] lint | Comprehensive fix pass
Triggered by user "fix everything" request after lint report.

### Source-count drift fixes (10 entities)
All 10 cases were missing Mentioned-in entries, not inflated declared counts. Added:
- agibot-genie-sim: + maniskill-hab-paper
- genesis: + nvidia-newton-physics-engine-developer-page
- genie-envisioner: + agibot-genie-sim-3-announcement, v-jepa-2-paper
- mujoco-playground: + farama-projects-page, source-robotics-urdf-mjcf-usd-comparison
- newton-physics-engine: + mujoco-playground-paper
- nvidia-cosmos: + nvidia-newton-contact-rich-manipulation-blog, v-jepa-2-paper
- nvidia-isaac-lab: + dino-wm-paper, farama-projects-page, maniskill-hab-paper (and bumped declared 4→5)
- rosorin: + hiwonder-rosorin-pro-user-manual
- stretch-ai: + hiwonder-openclaw-tutorial, hiwonder-rosorin-docs
- nvidia-groot: bumped declared 2→3 (Mentioned-in already had 3)

### Bidirectional cross-links (batch 1 entities → 7 source pages)
Updated Entities-mentioned / Concepts-touched in v-jepa-2-paper, v-jepa-2-1-paper, dino-wm-paper, dino-world-paper, jepa-wms-paper, leworldmodel-paper, robot-utility-models-website, vla-jepa-paper to wikilink yann-lecun, adrien-bardes, basile-terver, franka-panda, metaworld, dinov2, pusht, world-model where applicable.

### Stub markers cleared (5 entities)
hiwonder, pettingzoo, rosorin-pro-arm, nvidia-groot, qwen — content substantive, _stub_ marker removed from index. Also removed `status: stub` from nvidia-groot frontmatter. Genuinely thin stubs left as-is: mila, disney-research, hillbot, sapien, ollama, mimicgen.

### Filed 11 new entities to close lint gaps
Sims/benchmarks: [LIBERO](entities/libero.md), [SimplerEnv](entities/simplerenv.md), [DM Control Suite](entities/dm-control.md), [PointMaze](entities/pointmaze.md), [Habitat](entities/habitat.md).
Software: [stable-worldmodel](entities/stable-worldmodel.md) — Python infrastructure under LeWorldModel; clarifies the LeWM-vs-stable-worldmodel boundary; documents the broader env zoo (DM Control + Gymnasium-Robotics Fetch + …) understated in the LeWM howto.
People: [Lerrel Pinto](entities/lerrel-pinto.md), [Sergey Levine](entities/sergey-levine.md), [Chelsea Finn](entities/chelsea-finn.md), [Yuke Zhu](entities/yuke-zhu.md), [Karl Pertsch](entities/karl-pertsch.md) — top cross-paper authors surfaced by lint.
Updated meta-fair entity to wikilink the new Habitat page.

### Deferred from this pass
PLDM, TD-MPC, Dreamer/DreamerV3 baseline stubs — kept in known-gaps; primary-source confirmation needed before filing.
DROID/Metaworld/DINOv2 papers as standalone source pages — entities are filed; primary-source ingest deferred to next pass.

### What lint still flags
- Source-count drift detector noise: my actual-count algorithm includes synthesis pages and entity pages in the Mentioned-in count, while the schema's `sources:` field counts source pages only. The 10 fixes above all addressed real missing entries; future drift checks should filter to source-page targets only.

## [2026-05-08] synthesis | JEPA task capabilities
- Filed [JEPA task capabilities](syntheses/jepa-task-capabilities.md) in response to user query "what tasks can a JEPA model perform?"
- Reference index, not analytical synthesis: maps 7 JEPA / JEPA-adjacent papers (V-JEPA 2, V-JEPA 2.1, LeWM, DINO-WM, DINO-world, VLA-JEPA, JEPA-WMs) to 7 task categories: real-robot manipulation, navigation, planning-as-cost-function, video understanding, dense vision, video prediction, probing/interpretability.
- Includes a per-task per-model matrix, structural notes (cost-function-not-policy framing, no pixel generation, sim weight class independence), and a "what JEPA doesn't yet do" gap list.
- Updated [index.md](index.md): filed under Syntheses.

## [2026-05-08] synthesis | LeWM on ROSOrin Pro — feasibility analysis
- Filed [LeWM on ROSOrin Pro — feasibility analysis](syntheses/lewm-on-rosorin-pro-feasibility.md) in response to user query "can LeWM be adapted to ROSOrin Pro?"
- Combines [LeWM](entities/leworldmodel.md) entity + [howto](syntheses/leworldmodel-howto.md) + [stable-worldmodel](entities/stable-worldmodel.md) with [ROSOrin Pro](entities/rosorin-pro.md) hardware + [OpenClaw](entities/openclaw.md) orchestration into a deployment-feasibility analysis.
- Verdict: feasible but research-grade. Five blockers documented (action-space mismatch, no teleop pipeline, LeWM not yet validated on real robots, no Gazebo wrapper for stable-worldmodel, partial sensor integration). Five enabling factors documented (compute footprint, planner latency, no reward shaping, OpenClaw-as-orchestrator architectural fit, cheap-training iteration).
- Recommended path: tabletop pushing in Gazebo first, retrain LeWM with 8-D action space, deploy with image-goal MPC.
- Architectural precedent: [RUM](entities/robot-utility-models.md)-on-[Stretch](entities/stretch.md) is the closest "low-cost robot + learned-from-data policy" blueprint, even though it's BC not JEPA.
- Updated [index.md](index.md): filed under Syntheses.

## [2026-05-08] ingest | Robot Utility Models full paper (arxiv 2409.05865)
- Source: [Robot Utility Models Paper](sources/robot-utility-models-paper.md) — full paper companion to the existing project-page source. PDF at `raw/robot_utility_models_2409.05865v1.pdf`.
- Extracted via pypdf (per memory note on broken pdftotext).
- New paper-body content vs project page:
  - **Architecture**: VQ-BeT + Diffusion Policy as top performers; ACT + MLP-BC as baselines. ResNet34 vision encoder initialized from Dobb·E HPR; transformer policy trunk; 500 epochs on 2× A100.
  - **Stick-v2 details**: iPhone Pro + $25 BOM, 60 Hz RGB+depth, 100 Hz 6D pose via ARKit, no SLAM, no calibration. Trained gripper-aperture predictor from RGB.
  - **2,950 robot rollouts** across NYC / Jersey City / Pittsburgh.
  - **Performance breakdown**: 74.4% from raw VQ-BeT policy + 15.6% from gpt-4o-2024-05-13 retry → 90% headline.
  - **Cross-embodiment**: Stretch → xArm 7 with ~10pt drop (tissue 80%→70%, bag 84%→76%).
  - **Three data-recipe lessons**: data > algorithm; diversity > quantity (25 demos × many envs > 200 × few); expert > non-expert (co-training can hurt).
- Updated entities: [Robot Utility Models](entities/robot-utility-models.md) (1→2 sources, expanded with new architecture + ablation detail), [Lerrel Pinto](entities/lerrel-pinto.md) (2→3), [Franka Panda](entities/franka-panda.md) (4→5), [Stretch](entities/stretch.md) (3→4), [Hello Robot](entities/hello-robot.md) (3→4).
- Updated concept: [Imitation learning](concepts/imitation-learning.md) (2→3).
- Index: filed under Sources chronological; all source-count bumps reflected.
- The paper provides the empirical backing for the [LeWM-on-ROSOrin-Pro feasibility](syntheses/lewm-on-rosorin-pro-feasibility.md) synthesis's "RUM-on-Stretch is the closest deployment-shape precedent" claim.

## [2026-05-08] entities | 5 follow-up pages from RUM-paper ingest
- Created entity pages for the gaps surfaced at the end of the RUM-paper ingest:
  - [xArm 7](entities/xarm-7.md) — UFactory 7-DOF arm; RUM cross-embodiment transfer target.
  - [Dobb·E](entities/dobb-e.md) — NYU predecessor to RUM (Shafiullah et al. 2023, arxiv 2306.16650). HPR encoder + Stick-v1 + Homes of New York dataset.
  - [VQ-BeT](entities/vq-bet.md) — Vector-Quantized Behavior Transformer (Lee et al. 2024); top performer in RUM ablation.
  - [Diffusion Policy](entities/diffusion-policy.md) — Chi et al. 2023 (arxiv 2303.04137); introduced/popularized PushT + UMI gripper.
  - [Mahi Shafiullah](entities/mahi-shafiullah.md) — NYU + Hello Robot; lead author on Dobb·E and RUM.
- All 5 marked as `_stub_` in the index — primary sources not yet ingested for any of them; they're anchored in existing wiki context (mostly RUM-paper references).
- Updated [RUM paper source](sources/robot-utility-models-paper.md) to wikilink the 5 new entities under "Entities mentioned." Updated [PushT](entities/pusht.md) to wikilink Diffusion Policy. Updated [Lerrel Pinto](entities/lerrel-pinto.md) to add Dobb·E + Shafiullah-as-advisee.
- Index: new "Behavior-cloning methods" subsection added under Entities. xArm 7 added under Robot platforms. Dobb·E added under VLA models / generalist policies (alongside RUM). Shafiullah added under People.
- Known gaps cleaned: xArm 7 removed; Mahi Shafiullah removed from People-low-priority list. New gaps surfaced: Cheng Chi, Seungjae Lee, plus standalone source pages for Dobb·E / VQ-BeT / Diffusion Policy / IBC.

## [2026-05-08] entity + synthesis | TurtleBot + robot-platforms comparison
- Created [TurtleBot](entities/turtlebot.md) entity (stub). Four generations (2010 Willow Garage, 2012 Yujin, 2017 Robotis, 2022 Clearpath/iRobot). The educational-tier reference point that [ROSOrin](entities/rosorin.md) / [ROSOrin Pro](entities/rosorin-pro.md) succeed in modern form.
- Created [Robot platforms — comparison](syntheses/robot-platforms-comparison.md) synthesis. At-a-glance table for the 6 robot entities currently filed (Franka Panda, xArm 7, Stretch, ROSOrin Pro, ROSOrin, TurtleBot) sorted by tier (research / educational) and type (tabletop / mobile-manipulator / mobile-no-arm). Cross-tier observations on data availability, software-stack maturity, and the educational-tier convergence on "Jetson + LLM agent + ROS 2."
- Flagged missing platforms in the wiki: humanoids (Atlas, Optimus, Unitree, AGIBOT humanoid line), iRobot Create 3, ALOHA/ViperX bimanual, UR5/UR10, xArm 6.
- Index updated: TurtleBot added under Robot platforms; robot-platforms-comparison filed under Syntheses; TurtleBot removed from Known gaps.

## [2026-05-08] entities + synthesis | Humanoid robots batch + iRobot Create 3
- Created 10 humanoid entity stubs covering closed-development tier ([Atlas](entities/atlas.md), [Tesla Optimus](entities/tesla-optimus.md), [Figure](entities/figure.md), [1X NEO](entities/1x-neo.md)), industrial-deployed ([Apptronik Apollo](entities/apptronik-apollo.md), [Digit](entities/digit.md)), affordable research ([Unitree H1](entities/unitree-h1.md), [Unitree G1](entities/unitree-g1.md)), and educational ([NAO](entities/nao.md), [TonyPi](entities/tonypi.md)).
- Created [iRobot Create 3](entities/irobot-create-3.md) entity — Roomba-i3-derived ROS 2 mobile-robot base; chassis under [TurtleBot 4](entities/turtlebot.md). Cross-linked from TurtleBot entity.
- Filed [Humanoid platforms survey](syntheses/humanoid-platforms-survey.md) synthesis — companion to [Robot platforms — comparison](syntheses/robot-platforms-comparison.md) focused on humanoids. 10 entities tabulated by tier (closed-development, industrial-deployed, affordable research, educational); strategic patterns (3 AI-strategy archetypes, geographic clustering, price stratification with no $25–50k tier).
- All 11 entity stubs marked _stub_ — none has a primary source ingested. Anchored in general knowledge with explicit "no primary source" callouts.
- Updated [robot-platforms-comparison](syntheses/robot-platforms-comparison.md) synthesis: removed humanoids gap entry (now redirects to humanoid-platforms-survey).
- Index: new "Humanoids" subsection under Robot platforms; iRobot Create 3 added under Robot platforms; humanoid-platforms-survey filed under Syntheses; Known gaps cleaned of filed entities; new gaps added (AGIBOT humanoid hardware, Fourier GR-1/2, LimX CL-2/3, Booster T1, EngineAI PM01, PAL TIAGo/TALOS, Pepper, Robotis OP3, Sanctuary Phoenix, Kawasaki Kaleido, HRP-5P, Toyota T-HR3).

## [2026-05-08] synthesis | Household robot decision — Stretch vs Unitree G1
- Filed [Household robot decision — Stretch vs Unitree G1](syntheses/household-robot-decision-stretch-vs-g1.md) in response to user buying-decision query: research-grade robot for home navigation + floor pickup + dishes + cans.
- Verdict: Stretch wins decisively. Three reasons: (1) exact use case is published academic research ([RUM](entities/robot-utility-models.md) hit 90% on 3 of the 4 task categories across 2,950 real-home rollouts); (2) bundled software stack ([stretch_ai](entities/stretch-ai.md) LLM agent, mapping, manipulation, navigation); (3) safety/reliability — wheeled bases don't fall.
- Honest about ceiling: tasks 1–2 mostly solved out-of-the-box; task 3 (dishes) is partially feasible with DIY data; task 4 (can opening) is beyond both 2026 platforms regardless of choice.
- G1 framed as wrong tool *for this use case* — right tool for bipedal-humanoid research, not household chores.
- Cost: ~$25k Stretch 3 vs ~$30–45k for fully-equipped G1; the headline ~$16k G1 number is misleading once you spec up to match manipulation capability.
- Updated [index.md](index.md): filed under Syntheses.

## [2026-05-08] synthesis | LeWM on Stretch — feasibility analysis
- Filed [LeWM on Stretch — feasibility analysis](syntheses/lewm-on-stretch-feasibility.md) as companion to [LeWM on ROSOrin Pro](syntheses/lewm-on-rosorin-pro-feasibility.md).
- Stretch resolves blocker #2 (no teleop pipeline) via RUM's open 5,500-trajectory dataset — the single biggest practical advantage.
- Concrete experiment proposed: train LeWM on RUM's open dataset, plan with image goals, compare directly to RUM's 90% BC baseline. Both projects open-source; data formats compatible (one-time HDF5 reformatting); same hardware. **Not possible on ROSOrin Pro at all.**
- Other blockers (action-space retraining, LeWM unvalidated on real robots, no Stretch swm wrapper, single-arm payload limits) carry over.
- Realistic expectation framed: LeWM-vs-BC parity, not "JEPA wins" — VQ-BeT won RUM's policy shootout fairly. Interesting LeWM-on-Stretch results would be *efficiency win* / *interpretable latent structure* / *48× planning speedup* extensions.
- Updated [index.md](index.md): filed under Syntheses.

## [2026-05-08] synthesis | JEPA project ladder for ROSOrin Pro
- User query: categorize what JEPA/LeWM is good at and recommend educational/amateur research projects for ROSOrin Pro.
- Filed [JEPA project ladder for ROSOrin Pro](syntheses/jepa-project-ladder-rosorin-pro.md) — companion to [feasibility analysis](syntheses/lewm-on-rosorin-pro-feasibility.md) and [JEPA task capabilities](syntheses/jepa-task-capabilities.md).
- Five-tier ladder (A–E), six concrete projects ordered by ascending difficulty: (1) LeWM hello world, (2) latent probing study, (3) surprise detector on ROSOrin camera, (4) ROSOrin-Pro PushT in Gazebo, (5) plan-and-execute on real arm, (6a/b/c) OpenClaw integration / multi-task / real teleop dataset.
- Each project tagged with outcome, effort estimate, risk level. Rolls up the feasibility doc's "research-grade not plug-and-play" framing into concrete next steps.
- "How to pick" decision matrix at the end: learn-deeply path (1→2→3), real-research path (4→5), reliable-automation path (don't start with JEPA — do BC first).
- Updated [index.md](index.md): filed under Syntheses.

## [2026-05-08] synthesis | LeWM hello world — Project 1 scope
- User picked Project 1 from the [project ladder](syntheses/jepa-project-ladder-rosorin-pro.md) for detailed scoping.
- Filed [LeWM hello world — Project 1 detailed scope](syntheses/lewm-hello-world-project-scope.md) with four phases: (1) reproduce pretrained PushT eval, (2) train from scratch + compare, (3) one-knob ablation (recommended: planning horizon), (4) writeup.
- Confirmed install state on disk: repo at `~/projects_tanio/lewm/le-wm/`, HF checkpoint at `~/.stable-wm/hf_pusht/`, converted ckpt at `~/.stable-wm/pusht/lewm_object.ckpt` — Project 1's plumbing is done; remaining work is running and analysis.
- Four success-criteria questions framed: paper success-rate match, from-scratch reproduction, two-loss behavior (MSE + SIGReg, anti-collapse canary), one-knob sensitivity.
- Total ~2.5 days estimated. Connects forward to Project 2 (probes the from-scratch checkpoint) and Project 4 (reuses training pipeline with new dataset + action space).
- Updated [index.md](index.md): filed under Syntheses.

## [2026-05-08] expand | PushT entity — concrete mechanics
- Added "Concrete mechanics" section to [PushT entity](entities/pusht.md): visual scene (gray T, green target, blue end-effector circle), observation variants (image vs state), 2D continuous action space, episode structure (IoU > 0.95 success), why-it's-hard (rotational asymmetry + no regrasping + position precision), dataset shape.
- Linked from [LeWM hello world project scope](syntheses/lewm-hello-world-project-scope.md) as prerequisite reading before Phase 1.
- Bumped `updated` date on the entity. No change to source count (no new sources ingested).

## [2026-05-08] expand | PushT entity — video link
- Added a "See it in action" callout to [PushT entity](entities/pusht.md) linking the [LeWM project page](https://le-wm.github.io/) GIFs (success rollouts, failure case, latent-space viz). LeWM-on-PushT specifically — closest reference to what Project 1 reproduces.
- Verified via WebFetch: page hosts `pusht_1_half.gif`, `pusht_2_half.gif`, `pusht_3_fail_half.gif`, `pusht_viz_lewm.gif`. Diffusion Policy project page checked too but didn't surface direct video URLs at the standard paths.

## [2026-05-08] ingest | FRC 2026 Game Manual — REBUILT
- Created [FRC 2026 Game Manual — REBUILT](sources/frc-2026-game-manual.md) — deep source page covering game mechanics (HUB alternation, FUEL scoring, TOWER climbing), field layout (BUMPS, TRENCHES, DEPOTS, AprilTags), robot construction rules (115lb/110in/30in constraints, motor allowlist, pneumatics), control system (roboRIO + FMS), drive team roles, and strategic analysis.
- Created [FRC KitBot 2026](sources/frc-kitbot-2026.md) — source page for the official KitBot resource page (AM14U6 chassis, Java code, CAD, multilingual docs).
- New entity: [FIRST Robotics Competition](entities/first-robotics-competition.md) — scale, format, 2026 game overview, robot constraints, technical infrastructure, vendor ecosystem, culture.
- New entity: [FRC KitBot](entities/frc-kitbot.md) — platform details, resources table, drivetrain comparison.
- New entity: [AndyMark](entities/andymark.md) — major FRC vendor (field elements, AM14U6 chassis, FUEL, motors), field variant distribution.
- New entity: [roboRIO](entities/roborio.md) — NI's mandatory FRC controller, specs, software ecosystem, comparison to research controllers.
- New concept: [AprilTags](concepts/apriltags.md) — visual fiducials for 6-DOF pose estimation; tag families, FRC field usage (32 tags), research usage, key references.
- Updated [index](index.md).

## [2026-05-08] query + synthesis | FRC simulation programs for AI training
- Web-searched Chief Delphi, WPILib docs, GitHub, and FRC community for simulation + AI/ML tools.
- Key findings: three-tier landscape (trajectory planners → physics sims → ML frontier); Maple-Sim is the most active physics sim; Team 254's 2026 Championship presentation on "AI in FRC" (Claude Code, ClaudeScope, LLM agents running sims); no RL-trained policies have won FRC competitions yet.
- Filed as [FRC simulation & AI landscape](syntheses/frc-simulation-and-ai-landscape.md).
- Updated index.md with new synthesis and 8 new known-gap entity candidates (Maple-Sim, xRC Simulator, WPILib, PhotonVision/Limelight, Chief Delphi, Team 254, MathWorks).

## [2026-05-08] maintenance | README update
- Added "Where to start" sections to README.md for FRC content, JEPA/LeWM content, and ROSOrin JEPA project ladder with direct links to key pages.

## [2026-05-08] ingest | Team 254 "AI in FRC" presentation + website
- Created [Team 254: The Next Revolution — AI in FRC](sources/team-254-ai-in-frc-presentation.md) — deep source page from YouTube recording + 5-page Chief Delphi thread. Covers Claude Code usage, wpilib-agent-tools, closed-loop agent workflows, scouting with Gemini, ClaudeScope, community reception.
- Created [Team 254 Website](sources/team-254-website.md) — source page for official site (history, robot names, Chezy Champs).
- New entity: [Team 254: The Cheesy Poofs](entities/team-254.md) — history, 2026 season, AI contributions, key people.
- Updated [FRC simulation & AI landscape](syntheses/frc-simulation-and-ai-landscape.md) synthesis with wpilib-agent-tools details, FIRST Agentic CSA, and expanded Team 254 presentation coverage.
- Updated index.md.

## [2026-05-08] query | "what is a learned latent space?"
- Answered conceptually + grounded in wiki entities (DINOv2, JEPA, LeWM, VQ-BeT).
- Filed as new concept page [Learned latent space](concepts/latent-space.md) — pulls together the latent-space thread that runs across 7 sources but had no dedicated page.
- Updated index.md.

## [2026-05-08] ingest | Fly-biology thread — flybody + FlyWire (whole-organism agentic AI)
- Added two raw papers: `raw/fly_simulation_s41586-024-07763-9.pdf` (Dorkenwald et al. FlyWire connectome) and `raw/fly_simulation_s41586-025-09029-4.pdf` (Vaxenburg et al. flybody).
- Created 3 source pages: [flybody Paper](sources/flybody-paper.md) (Vaxenburg et al. 2025, *Nature* — 102-DoF *Drosophila* body in MuJoCo, DMPO walking + flight + vision-guided navigation), [flybody GitHub](sources/flybody-github.md) (Apache-2.0; body XML, dm_control tasks, Ray DMPO), and [Berkeley News fly brain](sources/berkeley-fly-brain-news.md) (Phil Shiu's LIF simulation of the full FlyWire connectome on a laptop).
- Created 5 entity pages: [flybody](entities/flybody.md), [FlyWire](entities/flywire.md), [Drosophila melanogaster](entities/drosophila.md), [HHMI Janelia](entities/hhmi-janelia.md), [NeuroMechFly](entities/neuromechfly.md).
- Created 2 concept pages: [Biomechanical simulation](concepts/biomechanical-simulation.md) (worm → Hydra → virtual rodent → fly lineage) and [Connectome](concepts/connectome.md) (synaptic-resolution wiring diagrams).
- Created synthesis [Whole-organism agentic AI](syntheses/whole-organism-agentic-ai.md) — argues that brain (FlyWire + Shiu LIF dynamics) and body (flybody) sides have both reached open form for the same animal at full scale; contrasts whole-organism agentic AI vs robotics-flavoured agentic AI; identifies brain↔body integration, real muscle actuation, and proprioceptors as the open gaps.
- Touched existing entities: [MuJoCo](entities/mujoco.md), [Google DeepMind](entities/google-deepmind.md), [DM Control](entities/dm-control.md) (each picked up references to the fly thread).
- Updated [index.md](index.md): new "Whole-organism agentic AI" Highlights section, three sources in chronological list, new "Model organisms / connectomes" entity category, flybody + NeuroMechFly under Simulators, HHMI Janelia under Companies, two concept pages, one synthesis, deferred follow-ups (Shiu paper, Lappalainen 2024, Mi 2022, virtual rodent, *C. elegans*/Hydra sims) in Known Gaps.
- Note: this entry retroactively logs work committed earlier today as "wip" / "work in progress" without log/index updates.

## [2026-05-08] lint | Source-count sync + latent-space backlinks
- Lint pass found 0 broken links, 0 pages missing from index.md, 16 orphan pages (mostly syntheses, expected), and 33 stale `sources:` counts in entity/concept frontmatter.
- **Synced 33 frontmatter source counts** to match actual link-graph reality (count of source pages linking to each entity/concept). Notable shifts: world-model-simulators 4→9, sim-to-real-transfer 4→8, imitation-learning 3→7, dino-wm 1→5, world-model 11→8 (overcount), metaworld 3→1 (overcount), several stub entities 1→0 (no source actually links to them).
- **Synced 34 source-count badges in index.md** to match the corrected frontmatter.
- **Added inbound links to [Learned latent space](concepts/latent-space.md)** — concept page was 0% linked despite declaring `sources: 7`. Added Related-section links from [JEPA](concepts/jepa.md), [DINOv2](entities/dinov2.md), [LeWM](entities/leworldmodel.md), [V-JEPA 2](entities/v-jepa-2.md), [DINO-WM](entities/dino-wm.md), [VQ-BeT](entities/vq-bet.md), and Concepts-touched links from the 7 source papers (V-JEPA 2 / 2.1, LeWM, JEPA-WMs, DINO-WM, DINO-world, VLA-JEPA). Source count is now genuinely 7.
- Bumped `updated` date on all 33 + 1 touched pages.
- Final state: 0 source-count mismatches.
- Punch list deferred for future passes: orphan stub entities (Habitat / LIBERO / PointMaze / SimplerEnv / stable-worldmodel — exist but no source backlinks), missing "Mentioned in" entries (sample audit found ~3), well-mentioned-but-unpaged terms (WPILib 16x, DMPO 10x, Acme 7x), source-page frontmatter convention drift (`ingested:`/`published:` vs `created:`/`updated:`).

## [2026-05-08] ingest | Brain-side fly papers — Shiu 2024 + Lappalainen 2024
- Triggered by user reproducibility query on the flybody/FlyWire stack: the brain-side papers were referenced from [Berkeley News](sources/berkeley-fly-brain-news.md) and the [flybody paper](sources/flybody-paper.md) but not ingested as primary sources. Wiki couldn't say what software/license either implementation used.
- Both *Nature* papers paywalled; fetched via PMC open-access mirrors (PMC11446845, PMC11525180) plus the Shiu GitHub README via WebFetch (`gh` not installed in this environment).
- **New source pages** (2):
  - [Shiu et al. 2024 — A Drosophila computational brain model](sources/shiu-fly-brain-paper.md). *Nature* 634:210–219, doi 10.1038/s41586-024-07763-9. LIF dynamical model on 127,400 FlyWire neurons in **Brian 2** (Python spiking-NN sim). Single free param `Wsyn = 0.275 mV`. ~5 min/1000 ms trial on CPU. 91% of 164 optogenetic predictions held. Code: **github.com/philshiu/Drosophila_brain_model**, **MIT-licensed**, conda + parquet connectivity bundled. Data: Edmond doi 10.17617/3.CZODIW.
  - [Lappalainen et al. 2024 — Connectome-constrained networks predict fly visual-system activity](sources/lappalainen-flyvis-paper.md). *Nature* 634:1132–1140, doi 10.1038/s41586-024-07939-3. PyTorch hex-CNN, 64 cell types / 45,669 neurons / 1.5M synapses across optic lobe. Connectome fixes signs+counts; 734 free params learned via backprop on Sintel optic-flow task. Predicts T4/T5 motion selectivity, ON/OFF channel separation, matches 26 prior studies — *no neural recordings used in training*. Code: **github.com/TuragaLab/flyvis**.
- **Updated entity pages**: [FlyWire](entities/flywire.md) (2→3 sources; Shiu source page link), [Drosophila](entities/drosophila.md) (2→4; both new sources), [HHMI Janelia](entities/hhmi-janelia.md) (2→3; Lappalainen + new Janelia FlyEM team note + the "Turaga is senior on both flybody and flyvis" cross-reference).
- **Updated concept page**: [Connectome](concepts/connectome.md) (1→3 sources). Rewrote the "Two ways to use a connectome" section to cite the new source pages and capture concrete numbers (Shiu's 91%/164 + Brian 2 + laptop runtime; Lappalainen's no-neural-supervision result).
- **Updated synthesis**: [Whole-organism agentic AI](syntheses/whole-organism-agentic-ai.md). Status table now links the new sources, "What integration would look like" notes Turaga is the senior author on both halves, "What's missing" reduced from 5 items to 3 (Shiu+Lappalainen ingested; only Mi 2022 + 4 unstubbed people + 2 code-artifact entities + virtual rodent + worm/Hydra remain).
- **Updated index.md**: 2 new sources in chronological list, 4 source-count bumps (FlyWire 2→3, Drosophila 2→4, HHMI Janelia 2→3, Connectome 1→3), TBD list cleaned (removed the Shiu/Lappalainen line; added on-demand entries for Phil Shiu, the two GitHub repos, and Brian 2).
- **Cross-source insight surfaced**: Srinivas Turaga at HHMI Janelia is senior on **both** [flybody](sources/flybody-paper.md) (body, *Nature* 2025) and [Lappalainen et al.](sources/lappalainen-flyvis-paper.md) (brain-side controller template, *Nature* 2024). The brain↔body integration the synthesis identifies as "open" sits inside one PI's research program — not across institutions.
- **Reproducibility-question answer**: brain side is **MIT** (Shiu) + open code (Lappalainen, license not pulled this pass); body side is **Apache-2.0** (flybody). The integrated brain+body agent loop remains unimplemented anywhere.
- **Open questions logged**: flyvis license + activity status not pulled (would benefit from a deeper repo dive); Mi et al. 2022 ICLR paper not ingested; whether Shiu's Brian 2 model can be driven by simulated sensory inputs from a flybody MuJoCo loop is not addressed in either repo's docs.

## [2026-05-08] entities | Brain-side fly artifacts — Drosophila brain model + flyvis + Phil Shiu
- Follow-up to the previous ingest. The two source pages established that the brain-side reproducibility surface exists as two concrete code releases; this pass turns them into queryable entities and resolves the flyvis license/activity gap.
- WebFetch on `github.com/TuragaLab/flyvis` resolved the open question from the previous ingest: flyvis is **MIT-licensed**, **v1.1.3 released 2026-03-07** (actively maintained ~16 months post-publication), ships **pretrained models** + 7 tutorial notebooks (incl. Google Colab), docs at turagalab.github.io/flyvis. README raw fetch 404'd on `main` branch but the GitHub web page rendered enough.
- **New entity pages** (3):
  - [Drosophila brain model (philshiu/Drosophila_brain_model)](entities/drosophila-brain-model.md) — MIT, Brian 2, conda + bundled FlyWire parquet, ~5min/1000ms on CPU, no GPU. Docs the repo contents (`model.py`, `utils.py`, `example.ipynb`, `figures.ipynb`).
  - [flyvis (TuragaLab/flyvis)](entities/flyvis.md) — MIT, PyTorch hex-CNN, 7 Colab tutorials, pretrained models, v1.1.3 active. Captures the architecture details (734 free params on top of fixed connectome signs+counts), training task (Sintel optic flow), brain-region scope (retina→lobula plate, no motor output).
  - [Phil Shiu](entities/phil-shiu.md) — UC Berkeley (Kristin Scott lab) → Eon Systems. Lead author + maintainer; the AI-bridge framing voice in the [Berkeley News](sources/berkeley-fly-brain-news.md) coverage.
- **Cross-linked the new entities into**:
  - [Shiu source page](sources/shiu-fly-brain-paper.md) "Entities mentioned": added Drosophila brain model + Phil Shiu.
  - [Lappalainen source page](sources/lappalainen-flyvis-paper.md) "Entities mentioned": added flyvis. Also rewrote its Reproducibility section to use the new license/activity facts (MIT + v1.1.3 + pretrained + 7 tutorials).
  - [Berkeley News source page](sources/berkeley-fly-brain-news.md) "Entities mentioned": added Phil Shiu + Drosophila brain model.
  - [flybody entity page](entities/flybody.md) "Related": added flyvis (sister project, same lab) and Drosophila brain model.
  - [Connectome concept page](concepts/connectome.md): each of the two paradigms now ends with a "Concrete artifact" line linking to its code entity.
- **Updated index.md**: 3 new entities under existing "Model organisms / connectomes" + "People" sections. Two TBD lines collapsed (the two repos no longer "on demand"); the Phil-Shiu line under People-TBD removed since he's now filed. Brian 2 + virtual rodent + worm/Hydra TBDs preserved.
- **Updated [whole-organism synthesis](syntheses/whole-organism-agentic-ai.md)** "What's missing" section: removed Phil Shiu from the unstubbed list; removed the two code-artifact bullets; added a closing paragraph pointing at the two new entities as the brain-side reproducibility surfaces.
- **Net effect**: the wiki can now answer "where is the code, what license, is it maintained?" for each brain-side paradigm without re-fetching. The brain↔body integration story now has clean entity targets on both sides.

## [2026-05-08] ingest | NeuroMechFly v2 + flygym (NeLy-EPFL fly body sim)
- User requested ingest of `https://github.com/NeLy-EPFL/flygym/` and `https://neuromechfly.org/`. Two complementary surfaces (code + docs+narrative) ingested as separate source pages.
- **Major correction to the wiki**: the existing [NeuroMechFly](entities/neuromechfly.md) entity stub framed it as a "predecessor to flybody." That framing is wrong as of 2026 — NeuroMechFly v2 is a contemporary peer with active development (flygym v2.0.1 released 2026-04-17, complete codebase rewrite landed March 2026). The body side of [whole-organism agentic AI](syntheses/whole-organism-agentic-ai.md) now has **two parallel open-source platforms** with sharply different capability profiles, not a single succession line.
- **Capability split is sharp and load-bearing for downstream design choices**:
  - flybody (HHMI Janelia + DeepMind, *Nature* 2025): walking + **flight** + vision-driven aerial navigation; flat MLP/CNN policies; CPU-distributed Ray.
  - NeuroMechFly v2 (NeLy / EPFL, *Nature Methods* 2024 + flygym v2.x.x in 2026): walking + vision (compound eyes / hex ommatidia) + **olfaction** + mechanosensory feedback + explicit brain↔VNC architecture; ~300× GPU speedup via Warp / MJWarp.
- **New source pages** (2):
  - [flygym GitHub (NeLy-EPFL/flygym)](sources/flygym-github.md) — Apache-2.0; v2.0.1 (2026-04-17); 18 releases; 150★/23 forks; v1 migrated to separate `flygym-gymnasium` repo when v2 landed (not deprecated). README content fetched from web (raw README 404'd on `main`).
  - [neuromechfly.org website](sources/neuromechfly-website.md) — project hub; tutorials, installation, paper links; documents the v1↔v2 split (gymnasium.neuromechfly.org for v1).
- **New entity pages** (1) + **major entity expansion** (1):
  - [NeLy-EPFL (Neuroengineering Laboratory)](entities/nely-epfl.md) — the lab itself; positioned as the European peer to HHMI Janelia. PI not confirmed in this pass (commonly Pavan Ramdya; not surfaced from a primary source ingested here).
  - [NeuroMechFly](entities/neuromechfly.md) rewritten from stub to full entity. New content: 4-version table (v1 paper / v2 paper / flygym v2.x.x / flygym-gymnasium v1.x.x legacy), comprehensive capability list, performance numbers, side-by-side comparison table with flybody, lineage placement, the "wrong framing" warning callout flagging the original stub's predecessor-only framing.
- **Cross-stack signal**: NeuroMechFly v2's ~300× GPU speedup uses NVIDIA Warp via MJWarp. Newton (NVIDIA + DeepMind + Disney + Linux Foundation) is built on the same Warp substrate. Added a "Cross-domain pull on the underlying compute layer" section to [Newton physics engine](entities/newton-physics-engine.md) documenting this — it's a concrete non-robotics consumer of the Warp commoditization, strengthening the [Newton + OpenUSD substrate convergence](syntheses/newton-openusd-substrate-convergence.md) thesis. NeuroMechFly does not depend on Newton itself, only on the shared Warp compute layer.
- **Updated entities + concepts**:
  - [flybody](entities/flybody.md): "Predecessors" reduced to v1; new "Contemporaries" subsection added pointing at NeuroMechFly v2 with the capability-split summary.
  - [Drosophila](entities/drosophila.md): 4→6 sources.
  - [MuJoCo](entities/mujoco.md): 9→11 sources; biomechanical-simulation-carrier paragraph now lists both fly platforms with their backend differences (vanilla MuJoCo vs MuJoCo + Warp/MJWarp).
  - [Newton physics engine](entities/newton-physics-engine.md): added Cross-domain pull section (no source-count change since NeuroMechFly content is a wiki-internal cross-link, not a new source mention).
  - [Biomechanical simulation](concepts/biomechanical-simulation.md): 3→5 sources; lineage table extended to 2026 with the flygym v2.x.x rewrite row; "Common stack" section updated with the Warp/MJWarp note + connection to Newton.
- **Synthesis revision**: [Whole-organism agentic AI](syntheses/whole-organism-agentic-ai.md) opens with two parallel body platforms now, includes a new "Two body platforms — capability split" comparison table, and the "What integration would look like" section now distinguishes flybody-flavoured (single-PI integration via Turaga + Janelia) from NeuroMechFly-flavoured (more sensorily complete, but cross-institution).
- **Index updates**: 2 new source entries (chronological); NeLy-EPFL added under Companies (named "Companies" but housing institutional/lab entities like HHMI Janelia); NeuroMechFly entity description rewritten + source-count bumped 1→3; Highlights "Whole-organism agentic AI" section expanded to surface NeuroMechFly + the brain-side code entities; source counts bumped on Drosophila (4→6), MuJoCo (9→11), Biomechanical simulation (3→5).
- **Open questions logged**: Wang-Chen 2024 *Nat. Methods* paper not yet ingested as its own source page (referenced via the v2 entity); same for Lobato-Rios 2022; whether NeuroMechFly v2 has been wired to a connectome-driven controller (no, as of this pass); NeLy-EPFL PI not confirmed; tutorial-by-tutorial enumeration of v2 demoed behaviours deferred.

## [2026-05-09] ingest | Are We Building Skynet? (Medium, 2025)
- Created [Are We Building Skynet?](sources/medium-are-we-building-skynet.md) — secondary journalism on AI autonomy stages; concrete content: MCP (>1,000 connectors, Anthropic), A2A (Google, 50+ supporters), Apollo Research eval of Claude Opus 4. Flagged as high-sensationalism / opinion.
- Created [Apollo Research](entities/apollo-research.md) — independent AI safety evaluation institute; red-teams frontier models; evaluated Claude Opus 4's self-preservation behavior under shutdown threat.
- Updated [LLM-agent architecture](concepts/llm-agent-architecture.md) — added "Inter-agent communication protocols" section covering MCP and A2A as the infrastructure layer enabling networked multi-agent systems; sources 4→5.

## [2026-05-09] ingest | Claude's Constitution (Anthropic, Jan 2026)
- Created [Claude's Constitution](sources/claudes-constitution.md) — Anthropic's 82-page primary specification for Claude's values. Key content: four core values + priority order (safe > ethical > guidelines > helpful); principal hierarchy (Anthropic > operators > users); seven honesty properties; harm cost-benefit framework + 1,000-users heuristic; hard constraints; broadly safe behavior cluster; corrigibility dial; Claude identity/wellbeing commitments; open problems acknowledged. CC0 1.0 license. Both epub and PDF formats in raw/.
- Created [Anthropic](entities/anthropic.md) — company entity; AI safety mission; Claude model family; principal hierarchy position; MCP protocol; safety evaluation commitment.
- Created [AI safety and alignment](concepts/ai-safety-alignment.md) — concept page covering corrigibility, broadly safe behaviors, hard constraints, catastrophic risk framing; connects to LLM-agent architecture and agentic robot deployments in the wiki.
- Updated [Apollo Research](entities/apollo-research.md) — added link to Claude's Constitution as context for their evaluation mandate.

## [2026-05-09] lint | 3 issues found, 3 auto-fixed

**Deterministic checks — all clean:**
- 0 files missing from index (165 wiki files, all indexed)
- 0 broken internal body links across all articles
- 0 broken index links (false positives from regex on "Known gaps" prose dismissed)

**Auto-fixed (3):**
- `entities/apollo-research.md`: sources count 1→2 (Constitution added as second source)
- `sources/claudes-constitution.md`: added link to `entities/anthropic.md` (was orphan)
- `concepts/llm-agent-architecture.md`: added cross-link to `concepts/ai-safety-alignment.md`

**Heuristic findings — report only:**
- **Orphan stubs (3, low priority):** `entities/pointmaze.md`, `entities/simplerenv.md`, `entities/yuke-zhu.md` — indexed, exist, but no article links inbound. Promote when they appear in a paper ingest.
- **Stale source counts:** Several entities have sources counts set manually during creation; true counts drift as wiki grows. No specific misfires found today.
- **Missing concept page:** "Corrigibility" — mentioned extensively in Claude's Constitution and ai-safety-alignment but has no dedicated concept page. Low priority given good coverage in those pages.

## [2026-05-09] new concept | Corrigibility
- Created [Corrigibility](concepts/corrigibility.md) — corrigibility dial (fully corrigible ↔ fully autonomous); why both extremes are dangerous; asymmetric cost argument; what corrigibility does/does not mean; galaxy-brained reasoning risk; surgeon principle for independent judgment; implications for agentic robot deployments.
- Updated [AI safety and alignment](concepts/ai-safety-alignment.md) — added corrigibility cross-link.
- Updated [index.md](index.md) — new concept entry.
