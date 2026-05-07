# Log

Append-only chronological record of wiki events. Each entry begins with `## [YYYY-MM-DD] <action> | <subject>` for grep-ability.

## [2026-05-06] bootstrap | Wiki initialized
- Created three-layer structure: `raw/`, `wiki/`, `CLAUDE.md`.
- Configured for the robot research domain.
- Subfolders: `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`, `wiki/syntheses/`.
- Index and log seeded; no sources ingested yet.

## [2026-05-06] research | Robot simulators for agentic robot software development
- Web survey via 7 search queries on the 2026 simulator landscape (no sources dropped into `raw/` — all from web).
- **Source pages created** (10): [[nvidia-newton-physics-engine-developer-page|NVIDIA Newton Physics Engine Developer Page]], [[nvidia-newton-contact-rich-manipulation-blog|NVIDIA Newton Contact-Rich Manipulation Blog]], [[mujoco-playground-paper|MuJoCo Playground Paper]], [[genesis-project-page|Genesis Project Page]], [[agibot-genie-sim-3-announcement|AGIBOT Genie Sim 3.0 Announcement]], [[agibot-genie-envisioner-2-announcement|AGIBOT Genie Envisioner 2.0 Announcement]], [[genie-envisioner-paper|Genie Envisioner Paper]], [[robocasa365-paper|RoboCasa365 Paper]], [[maniskill-hab-paper|ManiSkill-HAB Paper]], [[top-10-physical-ai-models-2026|Top 10 Physical AI Models 2026]].
- **Entity pages created** (14): [[nvidia-isaac-sim|NVIDIA Isaac Sim]], [[nvidia-isaac-lab|NVIDIA Isaac Lab]], [[newton-physics-engine|Newton physics engine]], [[mujoco-playground|MuJoCo Playground]], [[genesis|Genesis]], [[agibot-genie-sim|AGIBOT Genie Sim 3.0]], [[robocasa|RoboCasa]], [[maniskill|ManiSkill]], [[nvidia-cosmos|NVIDIA Cosmos]], [[genie-envisioner|Genie Envisioner]], [[agibot|AGIBOT]], [[nvidia|NVIDIA]], plus stubs for [[nvidia-groot|NVIDIA GR00T]] and [[google-deepmind|Google DeepMind]].
- **Concept pages created** (3): [[vla-models|VLA models]], [[sim-to-real-transfer|Sim-to-real transfer]], [[world-model-simulators|World-model simulators]].
- **Synthesis page created** (1): [[simulators-for-agentic-robotics-2026|Simulators for agentic robotics — 2026 landscape]].
- Five-category framing: (1) core GPU physics platforms, (2) embodied-AI / household-scale platforms, (3) world-model simulators, (4) classic / ROS-native, (5) industry usage signals.
- **Open question logged**: GR00T version inconsistency (N1.6 GA vs. N1.7 EA) flagged as a contradiction in the synthesis and on the GR00T stub.
- **Coverage gaps captured in index** under "Known gaps / TBD": Drake, Gazebo/Webots/CoppeliaSim/PyBullet, Pi (Physical Intelligence), Skild AI, LIBERO, RoboMimic, SAPIEN, Hillbot, Disney Research.

## [2026-05-07] lint | Wikilink convention migration
- Issue: my initial pages used bare `[[Display Title]]` wikilinks but kebab-case filenames, so Obsidian couldn't resolve them and created empty placeholder files at the vault root for [[nvidia-isaac-sim|NVIDIA Isaac Sim]], [[nvidia-newton-physics-engine-developer-page|NVIDIA Newton Physics Engine Developer Page]], and [[world-model-simulators|World-model simulators]].
- Resolution: deleted the 3 zero-byte orphans; rewrote all wikilinks across 28 pages to the explicit `[[slug|Display]]` form via `sed`.
- CLAUDE.md updated with the filename convention (kebab-case slugs) and the wikilink convention (always slug-pipe-display, never bare display).

## [2026-05-07] lint | Wiki health check pass
- Deleted second Obsidian orphan: `wiki/Genie Envisioner Paper.md` (empty 0-byte file).
- Reconciled NVIDIA mention drift: added `[[nvidia|NVIDIA]]` to [[agibot-genie-sim-3-announcement|AGIBOT Genie Sim 3.0 Announcement]]'s "Entities mentioned" list, since the source genuinely discusses NVIDIA's stack via Isaac Sim and GR00T.
- Bumped `sources` counts on 7 entity pages whose frontmatter under-counted actual inbound source-page wikilinks: [[agibot-genie-sim|AGIBOT Genie Sim 3.0]] (1→3), [[genesis|Genesis]] (1→2), [[genie-envisioner|Genie Envisioner]] (2→3), [[mujoco-playground|MuJoCo Playground]] (1→2), [[newton-physics-engine|Newton physics engine]] (2→3), [[nvidia-cosmos|NVIDIA Cosmos]] (2→3), [[nvidia-isaac-lab|NVIDIA Isaac Lab]] (2→3). Mirrored counts in `index.md`.
- No content contradictions found beyond the already-tracked GR00T N1.6/N1.7 EA version overlap.
- Deferred to user: whether to stub frequently-mentioned-but-unstubbed entities (Hillbot, SAPIEN, Disney Research).

## [2026-05-07] stubs | Filled three lint-flagged entity gaps
- Created stub pages for [[hillbot|Hillbot]] (UCSD spinoff, ManiSkill maintainer), [[sapien|SAPIEN]] (simulation framework underlying ManiSkill), and [[disney-research|Disney Research]] (Newton co-developer).
- Converted bare text mentions to wikilinks across `entities/maniskill.md` (Hillbot + SAPIEN ×3), `entities/newton-physics-engine.md`, `entities/google-deepmind.md`, `entities/nvidia.md`, `syntheses/simulators-for-agentic-robotics-2026.md` (Hillbot + SAPIEN + Disney in the Newton table cell), and added entries to `Entities mentioned` sections in `sources/maniskill-hab-paper.md` (Hillbot, SAPIEN) and `sources/nvidia-newton-physics-engine-developer-page.md` (Disney Research).
- Removed the three corresponding rows from `index.md` "Known gaps / TBD"; added the new stubs to Companies / Simulators sections.
- Updated synthesis "Coverage gaps" to drop SAPIEN (now stubbed); Drake remains.

## [2026-05-07] ingest | Hello Robot ecosystem (4 sources)
- **Sources ingested**: [[hello-robot-stretch-docs|Hello Robot Stretch Documentation]] (https://docs.hello-robot.com/0.3/), [[robot-utility-models-website|Robot Utility Models Project Page]] (https://robotutilitymodels.com/), [[stretch-ai-llm-agent-docs|Stretch AI LLM Agent Documentation]] (github.com/hello-robot/stretch_ai), and `raw/22486_RoboCasa365_A_Large_Scal.pdf` — re-ingested with deeper detail (the existing [[robocasa365-paper|RoboCasa365 Paper]] page was rewritten).
- **PDF tooling**: poppler-utils binaries weren't on PATH; `pypdf` was available, used a short Python script to extract pages 1–3 of the PDF. Found ICLR 2026 conference paper, full author list (Soroush Nasiriany, Sepehr Nasiriany, Abhiram Maddukuri, Yuke Zhu), and richer numbers (612 hr human + 1615 hr synthetic via [[mimicgen|MimicGen]]; 500K+ trajectories; 60 distinct activities behind the 365 tasks).
- **New entity pages** (5): [[hello-robot|Hello Robot]] (company), [[stretch|Stretch]] (robot), [[stretch-ai|stretch_ai]] (software stack), [[robot-utility-models|Robot Utility Models]] (method), [[mimicgen|MimicGen]] (tool, stub).
- **New concept pages** (2): [[imitation-learning|Imitation learning]], [[llm-agent-architecture|LLM-agent architecture]].
- **Updated existing pages**: [[robocasa|RoboCasa]] (added ICLR 2026 / authors / NVIDIA / MimicGen), [[nvidia|NVIDIA]] (sources 4→5; new "Research arm" bullet about Yuke Zhu's NVIDIA Research affiliation on RoboCasa365), [[vla-models|VLA models]] (sources 4→6; new "Adjacent: utility models" section noting RUMs and stretch_ai's LLM agent are non-language-conditioned alternatives), [[sim-to-real-transfer|Sim-to-real transfer]] (sources 2→3; RoboCasa365 added as benchmark), and the synthesis (new section 6 "Real-robot agentic stacks" highlighting stretch_ai and RUM as the consumer-side counterweight to sim-heavy paths).
- **Index reorganized**: added "Robot platforms", "Software stacks", and "Tools" subsections under Entities; renamed "VLA models" → "VLA models / generalist policies"; added 5 new TBD items (TRI LBM, Octo, Stretch Mujoco, xArm 7, RUM/Hello Robot people).
- **New cross-source insight**: Aaron Edsinger (Hello Robot co-founder) is a co-author on the RUM paper — concrete vendor / academic collaboration explicitly bridging the hardware vendor to the generalist-policy research agenda.

## [2026-05-07] ingest | JEPA papers (V-JEPA 2 + LeWorldModel)
- **Sources ingested** (2): [[v-jepa-2-paper|V-JEPA 2 Paper]] (`raw/JEPA_2506.09985v1.pdf`, arXiv 2506.09985, June 2025) and [[leworldmodel-paper|LeWorldModel Paper]] (`raw/LeWorldMode_2603.19312v2.pdf`, arXiv 2603.19312v2, March 2026). Both extracted via pypdf.
- **New entity pages** (4): [[v-jepa-2|V-JEPA 2]], [[leworldmodel|LeWorldModel]], [[meta-fair|Meta FAIR]], [[mila|Mila]] (stub).
- **New concept page** (1): [[jepa|Joint-Embedding Predictive Architecture]] — umbrella architecture for both papers.
- **Restructured concept**: [[world-model-simulators|World-model simulators]] now organized as two explicit paradigms — Paradigm A (generative-video: Cosmos, Genie Envisioner) and Paradigm B (JEPA / latent-prediction: V-JEPA 2, LeWorldModel). Sources 2→4.
- **Synthesis updates**: section 3 split into 3a (generative-video) and 3b (JEPA / latent-prediction); intro reads "Six categories" (was "Five"); sources list refreshed to include the four sources added since the last synthesis update (stretch-ai docs, RUM website, V-JEPA 2, LeWorldModel).
- **Cross-link**: [[nvidia-cosmos|NVIDIA Cosmos]] now cross-references the JEPA line as the contrasting paradigm.
- **Cross-source insight**: Yann LeCun is senior author on both papers — JEPA is his program, executed across two distinct teams (Meta FAIR for V-JEPA 2; Mila + NYU + Samsung + Brown for LeWM). The two papers represent **different points in the same design space**: V-JEPA 2 is large-scale + frozen-encoder + post-training; LeWM is small + end-to-end + simple. Together they argue JEPA is robust across scale.
- **Quantitative contrast captured**: V-JEPA 2 trains on **1M+ hours** with **1B parameters**; LeWM uses **15M parameters** on a single GPU. 60-70× model-size delta and ~5 orders of magnitude data delta — yet both are JEPAs and both demonstrate the paradigm.
- **TBD added**: DINO-WM, Dreamer/DreamerV3, TD-MPC, PLDM (world-model baselines from LeWM), Droid dataset (V-JEPA 2-AC training), Habitat (Meta), and a low-priority people-pages note (LeCun, Edsinger, Shafiullah, Zhu, Assran).

## [2026-05-07] ingest | Hiwonder ROSOrin documentation
- **Source ingested**: [[hiwonder-rosorin-docs|Hiwonder ROSOrin Documentation]] (https://docs.hiwonder.com/projects/ROSOrin/en/jetson-orin-nano-version/). User specifically asked to include the Gazebo section; pulled chapter 9 (Gazebo) and chapter 10 (Large AI Models incl. Embodied AI + offline) by curl + Python parsing of the Sphinx HTML. WebFetch's summarizer truncated the AI chapter mid-page on first attempts; raw curl + grep was needed for sections 10.3–10.5.
- **New entity pages** (4): [[hiwonder|Hiwonder]] (stub), [[rosorin|ROSOrin]] (full), [[ollama|Ollama]] (stub), [[qwen|Qwen]] (stub but cross-references stretch_ai).
- **No new concept pages** — content fits the existing [[llm-agent-architecture|LLM-agent architecture]] concept.
- **Updated existing**: [[concepts/llm-agent-architecture|LLM-agent architecture]] (sources 1→2; added ROSOrin as a second concrete example, noting the pattern is converging across research and educational tiers); [[stretch-ai|stretch_ai]] (sources 2→3 from new ROSOrin-docs cross-reference); [[stretch-ai-llm-agent-docs|stretch_ai LLM Agent Documentation]] (wikilinked Qwen instead of bare text; corrected vendor attribution from "Tencent" to Alibaba); synthesis section 6 (added ROSOrin as the educational-tier counterpart to stretch_ai); synthesis sources list refreshed.
- **Index reorganized**: added "LLMs" subsection under Entities; expanded Robot platforms (now Stretch + ROSOrin); added Hiwonder to Companies; added Ollama to Tools.
- **Concrete agentic-AI tooling captured**:
  - **Cloud LLMs** in ROSOrin chapter 10: GPT-4o, GPT-4o-mini, gpt-4o-transcribe, Whisper-1, OpenAI TTS (tts-1/tts-1-hd/gpt-4o-mini-tts), Qwen-plus-latest, StepFun multimodal (Chinese fallback path).
  - **Offline stack**: ollama serve + qwen3:1.7b + sherpa-onnx (CUDA) + matcha-icefall-zh-baker (Chinese TTS) + vits-ljs (English TTS).
  - **Embodied-AI control loop**: LLM emits `{action: [...], response: ...}` JSON, executor runs `eval(f'self.{a}')` per action — security-questionable but a clear standard recipe.
- **Cross-source convergence insight**: stretch_ai (research, Hello Robot) and ROSOrin (education, Hiwonder) independently default to small Qwen variants (2.5-3B and 3:1.7b) for their LLM-agent planners. The same JSON tool-call architectural pattern is shared across two unrelated stacks. The wiki now treats this as a confirmed pattern rather than a single data point.
- **TBD added**: Gazebo entity page (referenced by both Hello Robot and Hiwonder docs; previously was a passing mention), TurtleBot (canonical educational ROS robot), StepFun (Chinese multimodal AI), sherpa-onnx (offline ASR/TTS toolkit), WonderEcho Pro (Hiwonder voice module), Hiwonder's chapter 7 vision/CV curriculum (YOLOv11 + TensorRT — could be its own ingest).

## [2026-05-07] ingest | ROSOrin Pro / OpenClaw (manipulation-capable Hiwonder variant)
- **Sources ingested** (2): [[hiwonder-rosorin-pro-user-manual|Hiwonder ROSOrin Pro User Manual]] (chapter 1) and [[hiwonder-openclaw-tutorial|Hiwonder OpenClaw Practical Tutorial]] (chapter 13). The overview-page URL the user supplied was browsed for TOC structure but not filed as a separate source page (per scope choice — it was largely TOC).
- **New entity pages** (3): [[rosorin-pro|ROSOrin Pro]] (the kit), [[openclaw|OpenClaw]] (the LLM-agent framework — software, not hardware despite the "Claw" suffix), [[rosorin-pro-arm|ROSOrin Pro 6-DOF arm]] (stub for the HX-12H-servo manipulator hardware).
- **Updated existing**: [[rosorin|ROSOrin]] (added Pro variant to Related), [[hiwonder|Hiwonder]] (sources 1→3; documented the two-doc-domain split — `docs.hiwonder.com` for base, `wiki.hiwonder.com` for Pro), [[concepts/llm-agent-architecture|LLM-agent architecture]] (sources 2→3; added OpenClaw as third concrete example, generalized the convergence claim from "across tiers" to "across tiers and capabilities"), synthesis section 6 (extended ROSOrin bullet to cover the Pro variant + OpenClaw), synthesis sources list, index (added rosorin-pro, rosorin-pro-arm, openclaw under their respective sections; bumped Hiwonder source count and reorganized so Hiwonder appears earlier in Companies).
- **Hardware specs captured** (now reusable for future ingests): COIN-D6 LiDAR, Deptrum Aurora930 depth + RGB camera, MPU6050 IMU, HX-12H bus servos, STM32F407VET6 low-level MCU, 11.1 V 6000 mAh battery.
- **Concrete OpenClaw skill surface captured**: ROS 2 services `/start_pick`, `/place`, `/claw_track_and_grab/start`, `/claw_track_and_grab/set_color`, topics `~/arm_group_control`, `~/chassis_command`, `/controller/cmd_vel`. Action groups: `voice_pick`, `voice_give`, `init`, `camera_up`. Functions: `parse_twist()`, `pick()`, `place_function()`, `obj_track_proc()`. Vision: LAB-color thresholding + PID visual servoing + AprilTag (ID 0/1) + depth-based interactive grasping (Jetson Orin only).
- **Cross-source convergence insight strengthened**: The LLM-agent pattern is now demonstrated across **three independent stacks** — [[stretch-ai|stretch_ai]] (Hello Robot, research, mobile + arm), [[rosorin|ROSOrin]] (Hiwonder, education, mobile-only), and [[openclaw|OpenClaw]] (Hiwonder, education, mobile + arm). Same JSON tool-call architecture, same skill-library dispatch model. The claim has shifted from "this might be a pattern" to "this is the pattern" for non-VLA agentic-robotics deployment in 2026.
- **Notable absences in OpenClaw curriculum**: no VLA models (no OpenVLA/GR00T/RT-X/Pi), no LeRobot, no ACT or Diffusion Policy, no imitation learning, no teleoperation, no demonstration collection. Confirms the bifurcation already noted in the synthesis: VLA work happens in research labs (NVIDIA, Pi, Meta-via-RUM); deployed agentic stacks use LLM-orchestrated skill libraries.
- **Open question logged**: doc references `openai/gpt-5.4` — unclear if real OpenAI release or doc placeholder. Worth checking on the next OpenAI-related ingest.
- **TBD additions**: HX-12H, COIN-D6, Deptrum Aurora930, MPU6050 — hardware-component pages added as a single TBD line in the index (deferred until they recur).

## [2026-05-07] synthesis | LLM-agent architecture across stacks
- Filed [[llm-agent-architecture-across-stacks|LLM-agent architecture across stacks — a converged pattern]].
- Three-way side-by-side comparison of [[stretch-ai|stretch_ai]], [[rosorin|ROSOrin]], and [[openclaw|OpenClaw]]. Goes beyond the umbrella [[llm-agent-architecture|LLM-agent architecture]] concept by drawing structural implications — Qwen as the de-facto local default, JSON-shaped tool calls as the provider-portability layer, the bifurcation between research VLA stacks and deployed LLM-agent stacks.
- Surfaced two implementation hazards: `eval`-on-LLM-output dispatch in both Hiwonder stacks, and under-documented closed-loop replanning across all three.
- Open questions filed: no Claude backend anywhere; cross-vendor portability of skill libraries; whether VLAs eventually displace primitives without changing the orchestrator pattern.
