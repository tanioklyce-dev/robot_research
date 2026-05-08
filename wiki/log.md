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

## [2026-05-07] synthesis | Generative-video vs JEPA world models
- Filed [[generative-video-vs-jepa-world-models|Generative-video vs JEPA world models]].
- Deep comparison of paradigms A and B from [[world-model-simulators|World-model simulators]]. Five-table treatment: what each predicts, cost/speed, data scale, demonstrated real-robot results, failure modes — plus when-to-use guidance and a cross-paradigm interaction note (GR00T using Cosmos backbone; V-JEPA 2 encoder feeding multimodal LLMs).
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
- Filed [[newton-openusd-substrate-convergence|Newton + OpenUSD — the substrate convergence]].
- Argues the structural unusual-ness of a physics engine designed as a backend pluggable into both NVIDIA Isaac Lab and DeepMind's MuJoCo Playground, with OpenUSD as the shared scene format and Linux Foundation as the vendor-neutral governance layer. Implication: physics layer commoditizes, ML differentiation moves up the stack to environment APIs / learning frameworks / VLAs.
- Disney Research's role flagged as the puzzle piece — entertainment-grade physics keeping Newton's contact / soft-body models honest beyond industrial robotics.
- Open questions filed: real cross-stack adoption demo not yet ingested; throughput-parity comparisons absent; whether MuJoCo Playground defaults to Newton or keeps MJX as primary; Disney's specific contributions still opaque.

## [2026-05-07] synthesis | Sim-heavy vs real-data paths to generalist policies
- Filed [[sim-heavy-vs-real-data-paths|Sim-heavy vs real-data paths to generalist policies]].
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
- **Sources ingested** (4): [[openusd-rigid-body-physics-proposal|OpenUSD Rigid Body Physics Proposal]] (openusd.org, 2020 v1.0), [[nvidia-openusd-for-robotic-simulation|Using OpenUSD for Modular and Scalable Robotic Simulation]] (NVIDIA blog 2025-03-18 by Aaron Luk, Pomi Lee, Renato Gasoto), [[source-robotics-urdf-mjcf-usd-comparison|URDF vs MJCF vs USD comparison]] (Source Robotics blog 2026-03-13), [[nvidia-cad-to-usd-jt-workflows|Building CAD-to-USD Workflows with NVIDIA Omniverse]] (NVIDIA blog 2025-07-29 by Justine Lin).
- **New entity page** (1): [[openusd|OpenUSD]] — covers the format, the UsdPhysics schema, MjcPhysics + newton-usd-schemas extensions, and CAD ingestion paths.
- **Updated existing**: [[google-deepmind|Google DeepMind]] (sources 2→3; documented authorship of the `MjcPhysics` USD plugin and `mujoco-usd-converter`); [[newton-physics-engine|Newton physics engine]] (sources 3→4; added the `newton-usd-schemas` repo and the schema-promotion-into-UsdPhysics design); [[newton-openusd-substrate-convergence|Newton + OpenUSD substrate convergence synthesis]] (substantial enrichment — added the "OpenUSD as physics schema" section, the "DeepMind authors USD plugins" section, the "CAD ingestion — the upstream half" section, and updated the convergence table to include physics-schema and CAD-ingestion rows).
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
- **Source-count drift fixed** on six entity pages whose frontmatter under-counted inbound source-page references after the ingest: [[nvidia|NVIDIA]] 5→8, [[nvidia-isaac-sim|NVIDIA Isaac Sim]] 2→4, [[newton-physics-engine|Newton physics engine]] 3→4 (already in ingest commit), [[nvidia-cosmos|NVIDIA Cosmos]] 4→5, [[google-deepmind|Google DeepMind]] 2→3 (already in ingest commit), [[disney-research|Disney Research]] 1→2. Mirrored counts in `index.md`.
- **Removed a stray `Mentioned in` entry**: I had added `openusd-rigid-body-physics-proposal` under [[newton-physics-engine|Newton]]'s "Mentioned in" but that source page does not list Newton in its "Entities mentioned" — only OpenUSD and NVIDIA. Removed.
- **Added missing `Mentioned in` entries**: appended the four new sources to the relevant entity pages (NVIDIA, Isaac Sim, Cosmos, Disney Research, Newton, DeepMind) per the convention.
- DeepMind's `_stub_` marker dropped from index since the entity page now has 3 sources and substantive content (MjcPhysics + Newton + MuJoCo).

## [2026-05-07] synthesis | LeWorldModel — train and run howto
- Filed [[leworldmodel-howto|LeWorldModel — train and run howto]] from `lucas-maes/le-wm` README + project page.
- Updated [[leworldmodel-paper|LeWorldModel Paper]]: added `code` and `project_page` frontmatter; resolved the "code/website URLs missing" open question; added a Code & artifacts section.
- Updated [[leworldmodel|LeWorldModel]]: added Code section + howto link; bumped sources 1 → 2.
- Updated [[index|index.md]]: filed howto under Syntheses.

## [2026-05-07] update | LeWorldModel howto: install gotchas added
- Installed and verified `quentinll/lewm-pusht` end-to-end on RTX 5070 / WSL2 / Python 3.10.
- Updated [[leworldmodel-howto|LeWorldModel — train and run howto]] with a Gotchas section covering four real snags: gym 0.21.0 PEP 440 metadata, box2d-py SWIG dep, datasets resolved to 1.1.1, and the README conversion script's missing `_target_` filter.
- Expanded the "use pretrained" section with the actual HF→`_object.ckpt` conversion script + the `strip_target` fix.

## [2026-05-07] ingest | Farama Foundation Projects Page
- Source: [[farama-projects-page|Farama Foundation Projects Page]] (https://farama.org/projects).
- New entities (focused scope): [[farama-foundation|Farama Foundation]], [[gymnasium|Gymnasium]], [[pettingzoo|PettingZoo]], [[gymnasium-robotics|Gymnasium-Robotics]].
- Cross-referenced gym/gymnasium gotchas in [[leworldmodel-howto|LeWM howto]] to the new Gymnasium entity.
- Deferred: Minari, Metaworld, Shimmy, MO-Gymnasium, MOMAland, MAgent2, MPE2, Minigrid, MiniWoB++, ViZDoom, ALE, HighwayEnv, Procgen2, Stable-Retro, Jumpy — listed in index "Known gaps" with the source page as the canonical reference.

## [2026-05-07] ingest | Gymnasium-Robotics Documentation
- Source: [[gymnasium-robotics-docs|Gymnasium-Robotics Documentation]] (https://robotics.farama.org/).
- Expanded [[gymnasium-robotics|Gymnasium-Robotics]] from stub to real entity: confirmed MuJoCo backend (new bindings, not legacy mujoco-py), enumerated all six env families (Fetch, Shadow Hand, Maze, Adroit, Franka Kitchen, MaMuJoCo), added install snippet.
- Bumped source counts: gymnasium-robotics 1→2, gymnasium 1→2, farama-foundation 1→2.
- Added six env families to "Known gaps" for on-demand promotion (Adroit + Franka Kitchen most likely to surface, given D4RL / RoboCasa365 evaluation traditions).

## [2026-05-07] lint | Source-count drift fixes + MuJoCo entity
- Fixed source counts: [[leworldmodel|LeWorldModel]] 2→1 (synthesis pages don't count per schema); [[pettingzoo|PettingZoo]] 1→2; [[mujoco-playground|MuJoCo Playground]] 3→5; [[nvidia-isaac-lab|NVIDIA Isaac Lab]] 3→4. Index updated to match.
- New entity: [[mujoco|MuJoCo]] — the physics engine itself (was a 110-mention gap). 7 source pages reference it; entity covers `mujoco` vs `mujoco-py` vs MJX vs MJCF, history (Roboti → DeepMind 2021), and ecosystem role.
- Qualified the speculative "single-process CPU MuJoCo" claim on [[gymnasium-robotics|Gymnasium-Robotics]] with a `> [!note]` callout — the docs root didn't actually state CPU-only.
- No broken wikilinks, no orphans, no contradictions surfaced.

## [2026-05-07] synthesis | OpenUSD support across simulators
- Filed [[openusd-support-across-simulators|OpenUSD support across simulators]] — reference catalog of which simulators consume USD natively (Isaac Sim/Lab, Genie Sim 3.0), via plugin (MuJoCo via MjcPhysics + mujoco-usd-converter), as substrate (Newton via newton-usd-schemas), or not at all (Genesis, ManiSkill/SAPIEN, Gymnasium-Robotics).
- Companion to [[newton-openusd-substrate-convergence|Newton + OpenUSD — the substrate convergence]] (structural argument) and [[openusd|OpenUSD entity]] (format reference). Compiles the per-simulator answer into a single grep-able page.
- Updated [[index|index.md]]: filed under Syntheses.

## [2026-05-07] synthesis | Why JEPA research skips the simulator stack
- Filed [[why-jepa-research-skips-the-simulator-stack|Why JEPA research skips the simulator stack]] — synthesis observing that V-JEPA 2 and LeWorldModel both avoid heavy agentic-robotics simulators (Isaac Lab, MuJoCo Playground, ManiSkill, RoboCasa, Genesis).
- V-JEPA 2: internet video pretrain → real Droid teleop post-train → real Franka zero-shot eval (no sim anywhere). LeWM: trains/evals on PushT/cube/two-rooms/reacher (lightweight 2D/3D control benches, not real-robot sim).
- Four plausible reasons: (1) JEPA's data thesis is observation-scale, internet video beats sim; (2) latent-space prediction sidesteps pixel-level sim-to-real gap; (3) Droid removes sim's data-multiplier role; (4) test-of-truth is real-robot zero-shot.
- Caveats explicit: sample size of two; `stable-worldmodel` env zoo may extend further than ingested; future JEPA work may converge back into sim once it scales up.
- Updated [[index|index.md]]: filed under Syntheses.

## [2026-05-07] ingest | Five JEPA / JEPA-adjacent papers (probe of original synthesis)
- Triggered by: user query "find more information about JEPA and LeWorldModel and probe whether these methods use simulations." Research agent surfaced one paper that contradicts the original [[why-jepa-research-skips-the-simulator-stack|"JEPA skips sim" synthesis]] and four more that broaden the picture.
- New sources:
  - [[jepa-wms-paper|JEPA-WMs Paper]] (Terver, Yang, Ponce, Bardes, LeCun — FAIR, Dec 2025) — **first JEPA-for-robotics paper this wiki has ingested using heavy sim**: RoboCasa kitchen manipulation + 42 Metaworld tasks + Push-T + PointMaze + DROID + real Franka.
  - [[v-jepa-2-1-paper|V-JEPA 2.1 Paper]] (Mur-Labadia et al. — FAIR + Mila, Mar 2026) — "dense features"; +20pt real-Franka grasping per secondary research; sustains the no-sim line.
  - [[dino-wm-paper|DINO-WM Paper]] (Zhou, Pan, LeCun, Pinto — NYU + FAIR, Nov 2024) — DINOv2 patch features + zero-shot planning on PushT/Wall/PointMaze/Rope/Granular/Reacher.
  - [[vla-jepa-paper|VLA-JEPA Paper]] (Sun et al., Feb 2026) — JEPA-as-auxiliary inside VLA on LIBERO + SimplerEnv + real.
  - [[dino-world-paper|DINO-world Paper]] ("Back to the Features", Baldassarre et al. — FAIR, Jul 2025) — DINOv2 video world model; Basile Terver bridge author to JEPA-WMs.
- New entities: [[jepa-wms|JEPA-WMs]], [[dino-wm|DINO-WM]], [[vla-jepa|VLA-JEPA]], [[dino-world|DINO-world]].
- Updated entities: [[meta-fair|Meta FAIR]] sources 1→5, expanded JEPA-program description to include both encoder-co-trained (V-JEPA family) and frozen-DINOv2 (DINO-WM/DINO-world/JEPA-WMs) lines; [[v-jepa-2|V-JEPA 2]] sources 1→2 + V-JEPA 2.1 successor note; [[robocasa|RoboCasa]] sources 1→2 with JEPA-WMs cross-reference; [[mujoco|MuJoCo]] sources 6→7 (DINO-WM uses it).
- Updated concept: [[jepa|JEPA]] sources 2→7; added all 5 new instances; added "Simulator stance — fragmenting, not avoiding" section; cross-referenced revised synthesis.
- Index updated: 5 new sources under chronological list, 4 new world-model entities, JEPA concept source-count bump, JEPA-related expansion gaps section added.

## [2026-05-07] synthesis | Major revision — Why JEPA research skips the simulator stack
- Rewrote [[why-jepa-research-skips-the-simulator-stack|the synthesis]] in response to JEPA-WMs ingest (which directly contradicts the original claim).
- New framing: JEPA literature **fragments across four sim weight classes** (none / lightweight / mid-weight / heavy), not "skips sim wholesale." Original V-JEPA 2 + LeWM observation is correct for those papers but does not generalize.
- Each sim weight class explained by paper-specific question (representation learning vs. training-method vs. VLA-eval vs. physical-planning benchmark).
- The four "why" hypotheses from the original draft re-labeled: only (a) "internet-scale video > sim" has direct primary-source backing; (b)/(c)/(d) are wiki-author inference, not paper rationale.
- Two corrections folded in: `stable-worldmodel` env zoo includes DM Control + Gymnasium-Robotics Fetch (broader than the LeWM howto exposed); DINO-world → JEPA-WMs share research lineage via Basile Terver bread-crumb.
- New "watch item": first JEPA paper to explicitly train inside Isaac Lab or MuJoCo Playground (RoboCasa happened in Dec 2025; those two haven't yet).

## [2026-05-07] entity | DROID dataset
- Created [[droid|DROID]] entity page — Distributed Robot Interaction Dataset, 350 hr / 76k traj / 564 scenes / 86 tasks of Franka Panda teleop across 13 institutions; lead authors Khazatsky + Pertsch, senior Finn + Levine. Source: project page at https://droid-dataset.github.io/.
- Captured the OXE comparison (DROID +22% in-dist / +17% OOD vs Open-X Embodiment policies) and the BridgeV2/RH20T/RT-1 "order of magnitude more scenes" claim.
- Wikilinked DROID across [[v-jepa-2-paper|V-JEPA 2]] and [[jepa-wms-paper|JEPA-WMs]] sources so Mentioned-in flows correctly.
- Index updated: added Datasets subsection under Entities; removed DROID from Known gaps. Added Franka Panda + DROID-paper-itself to Known gaps as follow-ups.
- Open: DROID **paper itself** (arxiv 2403.12945) not yet a source page; license terms not surfaced; Dec 2024 / Apr 2025 update deltas not documented.

## [2026-05-07] entities | Batch 1 — Franka Panda + Metaworld + DINOv2 + PushT + 3 people + world-model concept
- Filed 8 pages in one batch in response to "recommend entities, then file batch 1":
  - [[franka-panda|Franka Panda]] — 7-DOF research arm; default tabletop manipulator across DROID, V-JEPA 2, V-JEPA 2.1, JEPA-WMs, RUM. (4 sources)
  - [[metaworld|Metaworld]] — Yu/Quillen/Levine/Finn 2019 meta-RL benchmark; 50 manipulation tasks on simulated Sawyer; staple in JEPA-WMs (42 tasks) + MuJoCo Playground. (3 sources)
  - [[dinov2|DINOv2]] — Meta FAIR self-supervised ViT (Oquab et al. 2023); 142M images, ViT-S/B/L/g; substrate for DINO-WM, DINO-world, JEPA-WMs. Apache 2.0. (3 sources)
  - [[pusht|PushT]] — 2D T-block pushing benchmark; introduced by IBC (Florence et al. 2021), popularized by Diffusion Policy (Chi et al. 2023). Default lightweight bench across LeWM / DINO-WM / JEPA-WMs. (3 sources)
  - [[yann-lecun|Yann LeCun]] — Meta VP, NYU, Turing Award 2018; senior on V-JEPA 2 / V-JEPA 2.1 / LeWM / DINO-WM / DINO-world / JEPA-WMs. (6 sources)
  - [[adrien-bardes|Adrien Bardes]] — FAIR; co-senior on V-JEPA 2 / V-JEPA 2.1 / JEPA-WMs; the FAIR-side champion of the V-JEPA program. (3 sources)
  - [[basile-terver|Basile Terver]] — bread-crumb author across DINO-world (Jul 2025) → JEPA-WMs (Dec 2025), the lineage signal called out in the JEPA-skips-sim synthesis. (2 sources)
  - [[world-model|World model]] — broad concept page, distinct from the narrower [[world-model-simulators|World-model simulators]] companion. Covers generative-video / JEPA / frozen-feature / model-based-RL design points. (11 sources)
- Sources for these pages were drawn from the existing wiki + a small primary-source pass on Metaworld (project page), DINOv2 (GitHub README), PushT (Diffusion Policy project page).
- Primary sources note: people pages (LeCun, Bardes, Terver) are written from the wiki's own author-overlap context plus widely-known facts; primary-source bio fetches deferred.
- Index updated: new Vision foundation models subsection (DINOv2); new People subsection (LeCun, Bardes, Terver); Franka Panda added under Robot platforms; Metaworld + PushT added under Simulators / frameworks; World-model concept added at top of Concepts.
- Known gaps cleaned: Franka Panda removed; Metaworld removed from Farama gap list; LeCun removed from People-low-priority list. Added new gaps surfaced by ingest: Sergey Levine, Chelsea Finn, Karl Pertsch, Alexander Khazatsky, Lerrel Pinto, Pulkit Agrawal as future people pages.
- Open: bidirectional source-to-entity cross-links (e.g. adding [[yann-lecun|Yann LeCun]] under "Entities mentioned" in V-JEPA 2 + LeWM + DINO-WM + DINO-world + JEPA-WMs source pages) **not done in this pass** — would tighten the graph but isn't load-bearing for retrieval. Worth a future lint pass.

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
Sims/benchmarks: [[libero|LIBERO]], [[simplerenv|SimplerEnv]], [[dm-control|DM Control Suite]], [[pointmaze|PointMaze]], [[habitat|Habitat]].
Software: [[stable-worldmodel|stable-worldmodel]] — Python infrastructure under LeWorldModel; clarifies the LeWM-vs-stable-worldmodel boundary; documents the broader env zoo (DM Control + Gymnasium-Robotics Fetch + …) understated in the LeWM howto.
People: [[lerrel-pinto|Lerrel Pinto]], [[sergey-levine|Sergey Levine]], [[chelsea-finn|Chelsea Finn]], [[yuke-zhu|Yuke Zhu]], [[karl-pertsch|Karl Pertsch]] — top cross-paper authors surfaced by lint.
Updated meta-fair entity to wikilink the new Habitat page.

### Deferred from this pass
PLDM, TD-MPC, Dreamer/DreamerV3 baseline stubs — kept in known-gaps; primary-source confirmation needed before filing.
DROID/Metaworld/DINOv2 papers as standalone source pages — entities are filed; primary-source ingest deferred to next pass.

### What lint still flags
- Source-count drift detector noise: my actual-count algorithm includes synthesis pages and entity pages in the Mentioned-in count, while the schema's `sources:` field counts source pages only. The 10 fixes above all addressed real missing entries; future drift checks should filter to source-page targets only.

## [2026-05-08] synthesis | JEPA task capabilities
- Filed [[jepa-task-capabilities|JEPA task capabilities]] in response to user query "what tasks can a JEPA model perform?"
- Reference index, not analytical synthesis: maps 7 JEPA / JEPA-adjacent papers (V-JEPA 2, V-JEPA 2.1, LeWM, DINO-WM, DINO-world, VLA-JEPA, JEPA-WMs) to 7 task categories: real-robot manipulation, navigation, planning-as-cost-function, video understanding, dense vision, video prediction, probing/interpretability.
- Includes a per-task per-model matrix, structural notes (cost-function-not-policy framing, no pixel generation, sim weight class independence), and a "what JEPA doesn't yet do" gap list.
- Updated [[index|index.md]]: filed under Syntheses.

## [2026-05-08] synthesis | LeWM on ROSOrin Pro — feasibility analysis
- Filed [[lewm-on-rosorin-pro-feasibility|LeWM on ROSOrin Pro — feasibility analysis]] in response to user query "can LeWM be adapted to ROSOrin Pro?"
- Combines [[leworldmodel|LeWM]] entity + [[leworldmodel-howto|howto]] + [[stable-worldmodel|stable-worldmodel]] with [[rosorin-pro|ROSOrin Pro]] hardware + [[openclaw|OpenClaw]] orchestration into a deployment-feasibility analysis.
- Verdict: feasible but research-grade. Five blockers documented (action-space mismatch, no teleop pipeline, LeWM not yet validated on real robots, no Gazebo wrapper for stable-worldmodel, partial sensor integration). Five enabling factors documented (compute footprint, planner latency, no reward shaping, OpenClaw-as-orchestrator architectural fit, cheap-training iteration).
- Recommended path: tabletop pushing in Gazebo first, retrain LeWM with 8-D action space, deploy with image-goal MPC.
- Architectural precedent: [[robot-utility-models|RUM]]-on-[[stretch|Stretch]] is the closest "low-cost robot + learned-from-data policy" blueprint, even though it's BC not JEPA.
- Updated [[index|index.md]]: filed under Syntheses.

## [2026-05-08] ingest | Robot Utility Models full paper (arxiv 2409.05865)
- Source: [[robot-utility-models-paper|Robot Utility Models Paper]] — full paper companion to the existing project-page source. PDF at `raw/robot_utility_models_2409.05865v1.pdf`.
- Extracted via pypdf (per memory note on broken pdftotext).
- New paper-body content vs project page:
  - **Architecture**: VQ-BeT + Diffusion Policy as top performers; ACT + MLP-BC as baselines. ResNet34 vision encoder initialized from Dobb·E HPR; transformer policy trunk; 500 epochs on 2× A100.
  - **Stick-v2 details**: iPhone Pro + $25 BOM, 60 Hz RGB+depth, 100 Hz 6D pose via ARKit, no SLAM, no calibration. Trained gripper-aperture predictor from RGB.
  - **2,950 robot rollouts** across NYC / Jersey City / Pittsburgh.
  - **Performance breakdown**: 74.4% from raw VQ-BeT policy + 15.6% from gpt-4o-2024-05-13 retry → 90% headline.
  - **Cross-embodiment**: Stretch → xArm 7 with ~10pt drop (tissue 80%→70%, bag 84%→76%).
  - **Three data-recipe lessons**: data > algorithm; diversity > quantity (25 demos × many envs > 200 × few); expert > non-expert (co-training can hurt).
- Updated entities: [[robot-utility-models|Robot Utility Models]] (1→2 sources, expanded with new architecture + ablation detail), [[lerrel-pinto|Lerrel Pinto]] (2→3), [[franka-panda|Franka Panda]] (4→5), [[stretch|Stretch]] (3→4), [[hello-robot|Hello Robot]] (3→4).
- Updated concept: [[imitation-learning|Imitation learning]] (2→3).
- Index: filed under Sources chronological; all source-count bumps reflected.
- The paper provides the empirical backing for the [[lewm-on-rosorin-pro-feasibility|LeWM-on-ROSOrin-Pro feasibility]] synthesis's "RUM-on-Stretch is the closest deployment-shape precedent" claim.

## [2026-05-08] entities | 5 follow-up pages from RUM-paper ingest
- Created entity pages for the gaps surfaced at the end of the RUM-paper ingest:
  - [[xarm-7|xArm 7]] — UFactory 7-DOF arm; RUM cross-embodiment transfer target.
  - [[dobb-e|Dobb·E]] — NYU predecessor to RUM (Shafiullah et al. 2023, arxiv 2306.16650). HPR encoder + Stick-v1 + Homes of New York dataset.
  - [[vq-bet|VQ-BeT]] — Vector-Quantized Behavior Transformer (Lee et al. 2024); top performer in RUM ablation.
  - [[diffusion-policy|Diffusion Policy]] — Chi et al. 2023 (arxiv 2303.04137); introduced/popularized PushT + UMI gripper.
  - [[mahi-shafiullah|Mahi Shafiullah]] — NYU + Hello Robot; lead author on Dobb·E and RUM.
- All 5 marked as `_stub_` in the index — primary sources not yet ingested for any of them; they're anchored in existing wiki context (mostly RUM-paper references).
- Updated [[robot-utility-models-paper|RUM paper source]] to wikilink the 5 new entities under "Entities mentioned." Updated [[pusht|PushT]] to wikilink Diffusion Policy. Updated [[lerrel-pinto|Lerrel Pinto]] to add Dobb·E + Shafiullah-as-advisee.
- Index: new "Behavior-cloning methods" subsection added under Entities. xArm 7 added under Robot platforms. Dobb·E added under VLA models / generalist policies (alongside RUM). Shafiullah added under People.
- Known gaps cleaned: xArm 7 removed; Mahi Shafiullah removed from People-low-priority list. New gaps surfaced: Cheng Chi, Seungjae Lee, plus standalone source pages for Dobb·E / VQ-BeT / Diffusion Policy / IBC.

## [2026-05-08] entity + synthesis | TurtleBot + robot-platforms comparison
- Created [[turtlebot|TurtleBot]] entity (stub). Four generations (2010 Willow Garage, 2012 Yujin, 2017 Robotis, 2022 Clearpath/iRobot). The educational-tier reference point that [[rosorin|ROSOrin]] / [[rosorin-pro|ROSOrin Pro]] succeed in modern form.
- Created [[robot-platforms-comparison|Robot platforms — comparison]] synthesis. At-a-glance table for the 6 robot entities currently filed (Franka Panda, xArm 7, Stretch, ROSOrin Pro, ROSOrin, TurtleBot) sorted by tier (research / educational) and type (tabletop / mobile-manipulator / mobile-no-arm). Cross-tier observations on data availability, software-stack maturity, and the educational-tier convergence on "Jetson + LLM agent + ROS 2."
- Flagged missing platforms in the wiki: humanoids (Atlas, Optimus, Unitree, AGIBOT humanoid line), iRobot Create 3, ALOHA/ViperX bimanual, UR5/UR10, xArm 6.
- Index updated: TurtleBot added under Robot platforms; robot-platforms-comparison filed under Syntheses; TurtleBot removed from Known gaps.

## [2026-05-08] entities + synthesis | Humanoid robots batch + iRobot Create 3
- Created 10 humanoid entity stubs covering closed-development tier ([[atlas|Atlas]], [[tesla-optimus|Tesla Optimus]], [[figure|Figure]], [[1x-neo|1X NEO]]), industrial-deployed ([[apptronik-apollo|Apptronik Apollo]], [[digit|Digit]]), affordable research ([[unitree-h1|Unitree H1]], [[unitree-g1|Unitree G1]]), and educational ([[nao|NAO]], [[tonypi|TonyPi]]).
- Created [[irobot-create-3|iRobot Create 3]] entity — Roomba-i3-derived ROS 2 mobile-robot base; chassis under [[turtlebot|TurtleBot 4]]. Cross-linked from TurtleBot entity.
- Filed [[humanoid-platforms-survey|Humanoid platforms survey]] synthesis — companion to [[robot-platforms-comparison|Robot platforms — comparison]] focused on humanoids. 10 entities tabulated by tier (closed-development, industrial-deployed, affordable research, educational); strategic patterns (3 AI-strategy archetypes, geographic clustering, price stratification with no $25–50k tier).
- All 11 entity stubs marked _stub_ — none has a primary source ingested. Anchored in general knowledge with explicit "no primary source" callouts.
- Updated [[robot-platforms-comparison|robot-platforms-comparison]] synthesis: removed humanoids gap entry (now redirects to humanoid-platforms-survey).
- Index: new "Humanoids" subsection under Robot platforms; iRobot Create 3 added under Robot platforms; humanoid-platforms-survey filed under Syntheses; Known gaps cleaned of filed entities; new gaps added (AGIBOT humanoid hardware, Fourier GR-1/2, LimX CL-2/3, Booster T1, EngineAI PM01, PAL TIAGo/TALOS, Pepper, Robotis OP3, Sanctuary Phoenix, Kawasaki Kaleido, HRP-5P, Toyota T-HR3).

## [2026-05-08] synthesis | Household robot decision — Stretch vs Unitree G1
- Filed [[household-robot-decision-stretch-vs-g1|Household robot decision — Stretch vs Unitree G1]] in response to user buying-decision query: research-grade robot for home navigation + floor pickup + dishes + cans.
- Verdict: Stretch wins decisively. Three reasons: (1) exact use case is published academic research ([[robot-utility-models|RUM]] hit 90% on 3 of the 4 task categories across 2,950 real-home rollouts); (2) bundled software stack ([[stretch-ai|stretch_ai]] LLM agent, mapping, manipulation, navigation); (3) safety/reliability — wheeled bases don't fall.
- Honest about ceiling: tasks 1–2 mostly solved out-of-the-box; task 3 (dishes) is partially feasible with DIY data; task 4 (can opening) is beyond both 2026 platforms regardless of choice.
- G1 framed as wrong tool *for this use case* — right tool for bipedal-humanoid research, not household chores.
- Cost: ~$25k Stretch 3 vs ~$30–45k for fully-equipped G1; the headline ~$16k G1 number is misleading once you spec up to match manipulation capability.
- Updated [[index|index.md]]: filed under Syntheses.

## [2026-05-08] synthesis | LeWM on Stretch — feasibility analysis
- Filed [[lewm-on-stretch-feasibility|LeWM on Stretch — feasibility analysis]] as companion to [[lewm-on-rosorin-pro-feasibility|LeWM on ROSOrin Pro]].
- Stretch resolves blocker #2 (no teleop pipeline) via RUM's open 5,500-trajectory dataset — the single biggest practical advantage.
- Concrete experiment proposed: train LeWM on RUM's open dataset, plan with image goals, compare directly to RUM's 90% BC baseline. Both projects open-source; data formats compatible (one-time HDF5 reformatting); same hardware. **Not possible on ROSOrin Pro at all.**
- Other blockers (action-space retraining, LeWM unvalidated on real robots, no Stretch swm wrapper, single-arm payload limits) carry over.
- Realistic expectation framed: LeWM-vs-BC parity, not "JEPA wins" — VQ-BeT won RUM's policy shootout fairly. Interesting LeWM-on-Stretch results would be *efficiency win* / *interpretable latent structure* / *48× planning speedup* extensions.
- Updated [[index|index.md]]: filed under Syntheses.

## [2026-05-08] synthesis | JEPA project ladder for ROSOrin Pro
- User query: categorize what JEPA/LeWM is good at and recommend educational/amateur research projects for ROSOrin Pro.
- Filed [[jepa-project-ladder-rosorin-pro|JEPA project ladder for ROSOrin Pro]] — companion to [[lewm-on-rosorin-pro-feasibility|feasibility analysis]] and [[jepa-task-capabilities|JEPA task capabilities]].
- Five-tier ladder (A–E), six concrete projects ordered by ascending difficulty: (1) LeWM hello world, (2) latent probing study, (3) surprise detector on ROSOrin camera, (4) ROSOrin-Pro PushT in Gazebo, (5) plan-and-execute on real arm, (6a/b/c) OpenClaw integration / multi-task / real teleop dataset.
- Each project tagged with outcome, effort estimate, risk level. Rolls up the feasibility doc's "research-grade not plug-and-play" framing into concrete next steps.
- "How to pick" decision matrix at the end: learn-deeply path (1→2→3), real-research path (4→5), reliable-automation path (don't start with JEPA — do BC first).
- Updated [[index|index.md]]: filed under Syntheses.

## [2026-05-08] synthesis | LeWM hello world — Project 1 scope
- User picked Project 1 from the [[jepa-project-ladder-rosorin-pro|project ladder]] for detailed scoping.
- Filed [[lewm-hello-world-project-scope|LeWM hello world — Project 1 detailed scope]] with four phases: (1) reproduce pretrained PushT eval, (2) train from scratch + compare, (3) one-knob ablation (recommended: planning horizon), (4) writeup.
- Confirmed install state on disk: repo at `~/projects_tanio/lewm/le-wm/`, HF checkpoint at `~/.stable-wm/hf_pusht/`, converted ckpt at `~/.stable-wm/pusht/lewm_object.ckpt` — Project 1's plumbing is done; remaining work is running and analysis.
- Four success-criteria questions framed: paper success-rate match, from-scratch reproduction, two-loss behavior (MSE + SIGReg, anti-collapse canary), one-knob sensitivity.
- Total ~2.5 days estimated. Connects forward to Project 2 (probes the from-scratch checkpoint) and Project 4 (reuses training pipeline with new dataset + action space).
- Updated [[index|index.md]]: filed under Syntheses.

## [2026-05-08] expand | PushT entity — concrete mechanics
- Added "Concrete mechanics" section to [[pusht|PushT entity]]: visual scene (gray T, green target, blue end-effector circle), observation variants (image vs state), 2D continuous action space, episode structure (IoU > 0.95 success), why-it's-hard (rotational asymmetry + no regrasping + position precision), dataset shape.
- Linked from [[lewm-hello-world-project-scope|LeWM hello world project scope]] as prerequisite reading before Phase 1.
- Bumped `updated` date on the entity. No change to source count (no new sources ingested).

## [2026-05-08] expand | PushT entity — video link
- Added a "See it in action" callout to [[pusht|PushT entity]] linking the [LeWM project page](https://le-wm.github.io/) GIFs (success rollouts, failure case, latent-space viz). LeWM-on-PushT specifically — closest reference to what Project 1 reproduces.
- Verified via WebFetch: page hosts `pusht_1_half.gif`, `pusht_2_half.gif`, `pusht_3_fail_half.gif`, `pusht_viz_lewm.gif`. Diffusion Policy project page checked too but didn't surface direct video URLs at the standard paths.
