# Log

Append-only chronological record of wiki events. Each entry begins with `## [YYYY-MM-DD] <action> | <subject>` for grep-ability.

## [2026-05-14] ingest | Onchain AI Garage — LeWM reproduction video (2026-04-24, 27 min)
- Created [Onchain AI Garage — "I Reproduced LeCun's JEPA World Model That Doesn't Predict Tokens" (2026-04-24)](sources/onchain-ai-garage-lewm-reproduction.md) — first independent LeWM reproduction on record in the wiki. Trains LeWM on Two Room on an RTX 3060 (12 GB VRAM) in WSL2 using Claude Code as implementation assistant; 4 epochs / ~8 hours / **92% success rate vs paper's 97%**. First half doubles as a JEPA popular-explainer. Full transcript ingested (~26K chars, 1634 s).
- Updated [Curriculum Module 12 — LeWorldModel deep-dive](syntheses/curriculum-12-lewm-deep-dive.md) — added a "Prior-art reproduction video" callout right after the Anchor exercise Part A (the reproduce-LeWM-PushT step).
- Updated [LeWorldModel — train and run howto](syntheses/leworldmodel-howto.md) — added an "Independent reproduction available" callout at the top; flagged that all four of the howto's documented gotchas (Python version, batch-128 OOM, WSL2 CUDA errors, throughput) were corroborated by the video.
- Updated [LeWM hello-world project scope](syntheses/lewm-hello-world-project-scope.md) — added a "Prior-art reproduction" note: the Two Room reproduction is on the *weakest* of LeWM's environments, so a PushT consumer-GPU reproduction is still wiki-novel.
- Updated [index.md](index.md) — added the video under Sources (chronological), right after the Welch Labs explainer (now two video sources in the LeWM cluster).
- Cross-cutting frame: this video is the **first concrete empirical data point in the wiki that LeWM trains and produces paper-ballpark numbers on consumer hardware**. Everything before this was paper-derived. The pattern (plan in main session → handoff markdown → execute in WSL via Claude Code) is also a wiki-relevant generalizable template for any reproduction work.
- Open follow-up: the host's prediction-loss starting value (0.08) is much lower than the paper's (0.25) — could be Two Room being simpler, different normalization, or different default hyperparameters in `stable-worldmodel`. Worth pinning down if the wiki's own PushT reproduction is attempted.

## [2026-05-14] ingest | Two foundational arch papers — Transformer (Vaswani 2017) + Siamese (Bromley/LeCun 1993)
- Created [Attention Is All You Need (Vaswani et al., NeurIPS 2017)](sources/attention-is-all-you-need.md) — the Transformer paper. Architecture (encoder–decoder, `N=6`, `d_model=512`, `h=8`), scaled dot-product attention math, multi-head attention, sinusoidal positional encoding, complexity table (self-attention `O(1)` max path length vs RNN `O(n)`), training setup (Adam + warmup + inverse-sqrt LR), WMT 2014 results (28.4 BLEU EN-DE big, 41.8 BLEU EN-FR), Section 6.3 constituency parsing as the first transformer task-generalization signal. Positioned as the foundation under LLMs, ViTs, VLA action heads, JEPA predictors, BeT / VQ-BeT, Diffusion Policy backbones — i.e., everything past curriculum Module 3.
- Created [Bromley, Guyon, LeCun, Säckinger, Shah 1993 — Signature Verification using a "Siamese" TDNN](sources/bromley1993-siamese-signature-verification.md) — the original Siamese network paper, AT&T Bell Labs / NIPS 1993. Two weight-tied TDNN sub-networks + cosine head + `±1` targets for genuine:genuine vs genuine:forgery pairs; 80-byte credit-card-stripe template constraint. Architecturally continuous with the modern joint-embedding SSL family (Barlow Twins, VICReg, DINOv2/v3) and with JEPA (J/A = Siamese, P = predictor on top). LeCun is a co-author — the 1990s seed of his 2020s JEPA program.
- Created [Siamese network](concepts/siamese-network.md) concept page — defining property (weight-tied branches), variants (asymmetric / triplet / N-way), the rep-collapse failure mode that emerged when later SSL work tried to train Siamese networks *without* labels, current state (DINOv3 / V-JEPA / LeWM are all Siamese descendants). 5 sources at creation.
- Updated [Joint-Embedding Predictive Architecture](concepts/jepa.md) — added "the J/A in JEPA descend from the [Siamese network](concepts/siamese-network.md) family; JEPA's contribution is the P" framing at the top of "What 'Joint' means"; added Bromley 1993 to Mentioned in; sources 14→15.
- Updated [Yann LeCun](entities/yann-lecun.md) — added "Earlier work (AT&T Bell Labs era)" section featuring the 1993 Siamese paper; bumped sources 16→17.
- Updated [glossary.md](glossary.md) — new "Siamese network" entry between SGD and SIGReg; linked the existing Transformer entry to the new Vaswani 2017 source page.
- Updated [index.md](index.md) — added both papers under "Sources (foundational, out of chronological order)" (alongside Barlow 1961 / Barlow Twins / VICReg / LeCun 2022 / DINOv3); added Siamese network under Concepts; bumped LeCun source count.
- Cross-cutting frame: this ingest closes two of the wiki's largest "foundational reference" gaps. **Transformer** was the single most-referenced architecture in the curriculum (Module 3 + Modules 5–14) with no primary-source page. **Siamese network** was the architectural ancestor cited across the SSL / JEPA lineage with no primary source. Both are now anchored to their original papers.
- Notable historical observation: the same Yann LeCun who is the senior author on every modern JEPA paper this wiki tracks co-authored the original Siamese network paper as a young researcher at AT&T Bell Labs **33 years earlier**. The architecture is continuous (two weight-tied encoders + a head); only the loss has changed (cos = ±1 → contrastive → anti-collapse regularizer → predictor-in-latent-space). The Welch Labs explainer's "JEPA is LeCun continuing his 1990s Siamese-network research" framing is literally correct.

## [2026-05-10] ingest | LeRobot Worldwide Hackathon 2025 — All Winners HF Space
- Created [LeRobot Worldwide Hackathon 2025 — All Winners](sources/lerobot-worldwide-hackathon-2025-winners.md) — June 14–15, 2025; 916 team members; ~400 submissions; 30 ranked winners pulled from the `maringetxway/all-winners` HF dataset (filenames carry rank + team).
- Created [LeRobot Worldwide Hackathon 2025](entities/lerobot-worldwide-hackathon-2025.md) (event entity), [Hope Jr Arm](entities/hope-jr-arm.md) (stub — premium-tier prize hardware), [Remi Cadene](entities/remi-cadene.md) (LeRobot lead at HF).
- Updated [LeRobot](entities/lerobot.md) 3→4 sources; added ecosystem-scale snapshot (916 / 400 / 30 / 189 datasets / 12 models) and linked Cadene as the project lead.
- Updated [Hugging Face](entities/hugging-face.md) 3→4 sources; added robotics-adjacent people (Cadene, Wolf, Caous).
- Updated [LeKiwi](entities/lekiwi.md) 2→3, [SO-ARM101](entities/so-arm101.md) 3→4, [Seeed Studio](entities/seeed-studio.md) 1→2 — flagged hackathon usage. Key market signal: LeKiwi was prize hardware in 22 of 30 ranked positions (top-3 + 6th–24th).
- Added new index subsection "Events" with the hackathon entity. Added the source under chronological sources.
- Headline: this is the ecosystem-scale evidence for the LeRobot stack ingested in the prior commit — ~400 community-team submissions on a single weekend means the buy → assemble → teleop → train → deploy loop is being closed in practice, not just in research papers.

## [2026-05-10] ingest | LeRobot ecosystem — XLeRobot, LeKiwi (SIGRobotics-UIUC), Seeed tutorial
- Created [XLeRobot Documentation](sources/xlerobot-docs.md) — Vector Wang's $660 dual-arm household manipulator; 2× SO-ARM101 on LeKiwi-class base; built on LeRobot; v0.3.0 released 2025-08-30.
- Created [Seeed Studio LeRobot LeKiwi Wiki](sources/seeed-lekiwi-wiki.md) — end-to-end build/teleop/train tutorial; STS3215 motor / Raspberry Pi 5 / ACT-policy spec; Seeed distributes LeKiwi hardware.
- Created [LeKiwi GitHub (SIGRobotics-UIUC/LeKiwi)](sources/lekiwi-github.md) — 1,300+ stars; 3-wheel Kiwi-drive holonomic base; Apache 2.0; Dynamixel/Koch v1.1 alternative arm variant.
- Created entities: [LeRobot](entities/lerobot.md), [LeKiwi](entities/lekiwi.md), [XLeRobot](entities/xlerobot.md), [SO-ARM101](entities/so-arm101.md) (SO-ARM100 lineage), [Vector Wang](entities/vector-wang.md), [SIGRobotics-UIUC](entities/sigrobotics-uiuc.md), [Seeed Studio](entities/seeed-studio.md), [The Robot Studio](entities/the-robot-studio.md), [Hugging Face](entities/hugging-face.md).
- Updated [Imitation learning](concepts/imitation-learning.md) 17→20 sources; added "Frameworks and stacks" section comparing LeRobot vs. Stretch AI vs. research-code tiers.
- Updated [index.md](index.md) — new sources under "Sources (chronological)"; new entities in Robot platforms, Software stacks, Companies, People; ACT/LeRobot tier flagged as the dominant sub-$1k IL stack.
- Cross-cutting frame: the LeRobot stack is the **gluing-existing-pieces-together** answer to affordable mobile manipulation — SO-ARM101 (The Robot Studio) + LeKiwi (SIGRobotics-UIUC) + LeRobot (Hugging Face) composes into XLeRobot's $660 dual-arm rig. Distinct from the integrated-vendor approach of Hello Robot (Stretch) or Pollen Robotics (Reachy 2).
- Noted UIUC footprint: [SIGRobotics-UIUC](entities/sigrobotics-uiuc.md) (low-cost mobile manipulation, LeKiwi) and the [Driggs-Campbell lab](entities/katherine-driggs-campbell.md) (assistive navigation, DRAGON) are independent UIUC groups both relevant to accessible robotics.

## [2026-05-10] ingest | Four new PDFs (DRAGON, Huh accessibility, Schneiders domestic, PAR review published version)
- Created [DRAGON — Dialogue-Based Robot for Assistive Navigation (Liu et al. 2024)](sources/dragon-assistive-nav-2024.md) — IEEE RA-L 2024; UIUC/Driggs-Campbell; TurtleBot 2i + CLIP landmark grounding + dialogue + VQA for PwVI; N=5 user study.
- Created [Designing Accessible Robot Communication for Blind People (Huh et al. 2026)](sources/huh2026-accessible-robot-comm.md) — CHI 2026 InterAI Workshop; cross-institutional (UC Berkeley × UT Austin × UW); observational (10 blind) + controlled (20 blind + 20 sighted) study; 6 design guidelines; mixed-initiative narration preferred by blind users; Cakmak among co-authors.
- Created [Domestic Robots and the Dream of Automation (Schneiders et al. 2021)](sources/schneiders2021-domestic-robots-automation.md) — CHI 2021; Aalborg University; 24 Danish households; task fragmentation finding; under-trust → co-located monitoring pattern; strict task division contradicts Forlizzi 2007 (flagged with warning callout).
- Updated [Physically Assistive Robots — Systematic Review (Nanavati et al. 2024)](sources/nanavati2024-physically-assistive-robots-review.md) — `raw/annurev-control-062823-024352.pdf` is the published Annual Review version of `raw/nanavati2024physically.pdf` (already ingested). Source page now references both files and incorporates §6 detail on interaction interfaces, levels of autonomy, and adaptation (resolves previously open question).
- Created entities: [Katherine Driggs-Campbell](entities/katherine-driggs-campbell.md), [Shuijing Liu](entities/shuijing-liu.md), [Mina Huh](entities/mina-huh.md), [Amy Pavel](entities/amy-pavel.md), [Roberto Martin-Martin](entities/roberto-martin-martin.md), [Huihan Liu](entities/huihan-liu.md), [Eike Schneiders](entities/eike-schneiders.md), [Tiago](entities/tiago.md).
- Updated entities: [Maya Cakmak](entities/maya-cakmak.md) 8→9 sources; [Yuke Zhu](entities/yuke-zhu.md) 1→2; [Amal Nanavati](entities/amal-nanavati.md) (added Huh 2026 cross-reference for §6.1.3 follow-up); [Franka Panda](entities/franka-panda.md) 9→10; [TurtleBot](entities/turtlebot.md) 1→2; [HCR Lab](entities/hcrlab.md) 8→9.
- Created new concept page [Accessible robot communication](concepts/accessible-robot-communication.md) — the output-interface side of HRI for non-visual users; 6 DGs from Huh et al. 2026; ties together DRAGON / Huh / Nanavati-review / Schneiders.
- Updated concept page [Assistive robotics](concepts/assistive-robotics.md) 13→16 sources; added "Communication and the output-interface gap" + "Domestic-robot precursors" sections.
- Updated [index.md](index.md) — added new sources/entities/concept; bumped source counts; added new highlights under "Assistive Robotics" block.
- Notable cross-citations: Huh et al. 2026 is positioned as direct response to Nanavati et al. 2024 §6.1.3 (output-interface gap); DRAGON 2024 documented as counter-example to "TurtleBot no longer in research" hypothesis on the TurtleBot page; Schneiders 2021 under-trust + co-location pattern flagged as conceptual precursor to the blind-user monitoring problem.

## [2026-05-09] ingest | Boston Dynamics blog: Tools for Your To Do List with Spot and Gemini Robotics
- Created [Tools for Your To Do List with Spot and Gemini Robotics](sources/bostondynamics-spot-gemini-robotics.md) — Boston Dynamics Spot-team engineers wired Gemini Robotics-ER 1.5 into Spot via a tool-call layer over the Spot SDK; 2025 hackathon demo (living-room cleanup); productized as AIVI-Learning with ER 1.6.
- Created [Boston Dynamics](entities/boston-dynamics.md) entity (parent company, Hyundai-owned) — first BD entity page; ties to Atlas/Spot/Stretch/Orbit/AIVI-Learning.
- Created [Spot](entities/spot.md) entity — commercial quadruped; Spot SDK as the integration surface; documented Gemini Robotics-ER and Meta object-retrieval integrations.
- Created [Gemini Robotics](entities/gemini-robotics.md) entity — Google DeepMind robot foundation models; full VLA + Gemini Robotics-ER (embodied-reasoning VLM that emits tool calls).
- Updated [Google DeepMind](entities/google-deepmind.md) — added Gemini Robotics section, Boston Dynamics partnership, source count 5→6.
- Updated [Meta FAIR](entities/meta-fair.md) — added cross-vendor Spot-for-object-retrieval reference, source count 6→7.
- Updated [Atlas](entities/atlas.md) — linked to new Boston Dynamics + Spot entity pages.
- Updated [LLM-agent architecture](concepts/llm-agent-architecture.md) — added Spot + Gemini Robotics-ER as a third concrete example; added note on "embodied reasoning" as vendor branding for the same architecture; source count 5→6.
- Updated [VLA models](concepts/vla-models.md) — clarified Gemini Robotics two-variant structure (full VLA vs -ER VLM).
- Updated [index.md](index.md) — added new source/entities; removed Spot from "needs-page" backlog.

## [2026-05-09] synthesis | Five new assistive-robotics syntheses
- Filed [Levels of autonomy in assistive robotics](syntheses/levels-of-autonomy-in-assistive-robotics.md) — three orthogonal autonomy axes; HCR Lab finding cluster (HRI 2020 → Walker 2024 → Yang 2025 → Nanavati 2025); EUP-over-RUM stack as unbuilt integration target.
- Filed [Long-term in-home robot deployments](syntheses/long-term-in-home-robot-deployments.md) — depth-sorted table; reliability gradient (RLBench 89.4% → BEHAVIOR-1K 12.4%); only one home has ≥1 month deployment data.
- Filed [Stretch as the de-facto assistive-robotics platform](syntheses/stretch-as-assistive-platform.md) — six of seven in-home deployments use Stretch; eight features that compound; decision matrix for platform choice.
- Filed [DINO-WM on Stretch — concrete experiment plan](syntheses/dino-wm-on-stretch-experiment.md) — sibling to LeWM-on-Stretch; lower-risk frozen-encoder variant; predictor-only training on RUM dataset; phase-by-phase plan.
- Filed [Underserved PAR domains — dressing, bathing, medication](syntheses/underserved-par-domains.md) — sub-capability decomposition; medication-fetcher ranked most tractable for independent researcher.
- Updated index.md Highlights and Syntheses sections.

## [2026-05-09] lint | Audit of recent Sonnet ingestion + counts/cascade fixes
- Audited HCR Lab ingest (6 papers, 2 entities, 2 concepts, 1 synthesis): coverage solid, citations rigorous, no contradictions found.
- Fixed: synthesis heading "Six blocking problems" → "Seven blocking problems" (had 7 problem sections).
- Synced index source counts: HCR Lab 2→8, Maya Cakmak 7→8, Anthropic 1→2, DINO-WM 5→6, V-JEPA 2 5→6.
- Cascaded `Mentioned in` updates: DINO-WM (added LeWM, LeWM-GitHub, JEPA-WMs, DINO-world, VLA-JEPA), V-JEPA 2 (added JEPA-WMs, VLA-JEPA, towardsai-lecun).
- Anthropic frontmatter sources 1→2.
- No broken markdown links across 196 wiki pages. No orphan pages.
- Remaining drift between frontmatter `sources:` and `Mentioned in` lists for ~40 pages — bookkeeping-only, not load-bearing for retrieval.

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

## [2026-05-09] ingest | HCR Lab Publications + Maya Cakmak Research Overview
- Fetched [HCR Lab Publications](sources/hcrlab-publications.md) from hcrlab.cs.washington.edu/publications/ — full publication record 2016–2025; key claims: HRI 2020 autonomy preference finding, Henry Evans Stretch deployments (summers 2021–2023), EUP transferred to Stretch SE2, feeding + handover award papers.
- Fetched [Maya Cakmak — Research Overview](sources/maya-cakmak-research.md) from mayacakmak.io/research — narrative research overview; stated goal; WHO statistic (190M PwD); HRI 2020 key finding; Henry Evans summer deployment details (2021/2022/2023); EUP rationale; FLEX-SDK; 45-paper EUP survey.
- Created [Maya Cakmak](entities/maya-cakmak.md) — UW professor, HCR Lab PI; two research tracks; Henry Evans deployments; autonomy preference + sense of agency findings; FLEX-SDK; systematic review; awards.
- Created [HCR Lab](entities/hcrlab.md) — Human-Centered Robotics Lab, UW; primary platform Stretch; two tracks (assistive robots + EUP); notable awards; collaborators (Srinivasa, Fox, Mutlu, Björling).
- Created [End-user robot programming](concepts/end-user-robot-programming.md) — EUP definition, rationale, key approaches (visual programming, PbD, multimodal, sketch+holes, tangible), FLEX-SDK, connection to assistive robotics.
- Updated [Stretch](entities/stretch.md) — added HCR Lab long-term deployment bullets (summers 2021–2023, Henry Evans; EUP tool built for Henry in summer 2022); EUP transfer to Stretch SE2; sources 7→9.
- Updated [Assistive robotics](concepts/assistive-robotics.md) — added "Autonomy and agency" section (HRI 2020 finding; assistive autonomy model; EUP as scalable response; sense of agency 2025 paper); added EUP cross-link to Related concepts; added HCR Lab sources to Mentioned in; sources 5→7.
- Updated [Assistive robotics — R&D landscape](syntheses/assistive-robotics-research-landscape.md) — moved Cakmak from "Beyond the wiki" to "Strong in the wiki" with full specifics: HRI 2020 finding, summer deployments, EUP, sense of agency paper, HCR Lab sources.
- Updated [index.md](index.md) — added 2 source entries, HCR Lab entity, Maya Cakmak entity, end-user-robot-programming concept; bumped Stretch sources 7→9; bumped assistive-robotics sources 4→7.

## [2026-05-09] ingest | 6 HCR Lab papers (murray2024, nanavati×3, walker2024, yang2025)
- Created [Physically Assistive Robots — Systematic Review](sources/nanavati2024-physically-assistive-robots-review.md) — PRISMA review (*Annual Review*, 2024); 1,981 screened, 87 included; three themes (interaction interfaces, levels of autonomy, adaptation); dressing/bathing/medication underserved; ~half of PAR papers involve no PwD. (raw/nanavati2024physically.pdf)
- Created [Sense of Agency — Yang et al. 2025](sources/yang2025-sense-of-agency.md) — RO-MAN 2025; four autonomy levels; EUP robots preserve sense of agency even when autonomous; high-risk tasks drive control preference; uses Stretch 3. (raw/yang2025senseofagency.pdf)
- Created [Feeding System Out-of-lab — Nanavati et al. 2025](sources/nanavati2025-feeding-out-of-lab.md) — HRI 2025 Best Systems Paper Finalist; open-source Kinova JACO system; CBPR co-design with two SCI quadriplegic CRs; 3 key lessons: customizability, variable autonomy, context-dependence. (raw/nanavati2025lessons.pdf)
- Created [Multiple Ways of Working with Users — Nanavati et al. 2024](sources/nanavati2024-multiple-ways-par.md) — A3DE @ HRI 2024 workshop; 3 PAR projects; participatory + empowerment design methodology. (raw/nanavati2024multiple.pdf)
- Created [Explicit-Input Teleoperation — Walker et al. 2024](sources/walker2024-explicit-input-teleoperation.md) — IROS 2024; pointing-based explicit assistance vs. implicit inference; N=20 user study; Franka + Isaac Sim; NVIDIA collaboration. (raw/walker2024explicit.pdf)
- Created [Grasping in Clutter IVFP — Murray et al. 2024](sources/murray2024-grasping-clutter-ivfp.md) — IVFP on Stretch RE1; interactive probing before extraction; autonomous reward assignment; Amazon Science Fellowship. (raw/murray2024learning.pdf)
- Created [Amal Nanavati](entities/amal-nanavati.md) — UW HCR Lab; lead author on feeding system, systematic review, multiple ways; CBPR methodology.
- Updated [Maya Cakmak](entities/maya-cakmak.md) — added specific paper citations for all 6 new papers; updated Mentioned in; sources 2→7.
- Updated [HCR Lab](entities/hcrlab.md) — added all 6 papers to Mentioned in; sources 2→8.
- Updated [Stretch](entities/stretch.md) — added sense of agency paper (Stretch 3 used) and IVFP paper (Stretch RE1); sources 9→11.
- Updated [Assistive robotics](concepts/assistive-robotics.md) — added "Literature landscape" section (systematic review stats: 1.3B PwD, 87 papers, three themes, underserved domains); sources 7→13; added all 6 papers to Mentioned in.
- Updated [End-user robot programming](concepts/end-user-robot-programming.md) — added sense of agency finding (EUP preserves agency) and feeding paper lessons; sources 2→4; updated Mentioned in.
- Updated [index.md](index.md) — 6 new source entries; Amal Nanavati entity; updated source counts (Stretch 9→11, assistive-robotics 7→13, EUP 2→4, Maya Cakmak 2→7).

## [2026-05-09] ingest | Diffusion Policy paper (Chi et al., RSS 2023)
- Created [Diffusion Policy Paper](sources/diffusion-policy-paper.md) — Chi, Feng, Du, Xu, Cousineau, Burchfiel, Song; Columbia / TRI / MIT; arxiv 2303.04137; conditional DDPM over actions with closed-loop receding-horizon action chunking, visual conditioning, time-series diffusion transformer. 12-task simulation sweep (RoboMimic + Push-T + BlockPush + Franka Kitchen) at 46.9% avg improvement; real-world UR5 Push-T (95%) + Franka mug-flip (90%) + sauce pouring (79%) + sauce spreading (100%); DDIM(10) inference at 0.1s on 3080. (raw/diffusion_policy_2023.pdf)
- Updated [Diffusion Policy](entities/diffusion-policy.md) — promoted from stub; added approach mechanics (DDPM formulation, CNN+FiLM and Transformer backbones, ResNet-18 + spatial softmax + GroupNorm, DDIM acceleration); empirical headline (46.9% / four real-world tasks); position-vs-velocity-control finding; latency robustness; downstream conventions (action-chunking, UMI). sources 1→2.
- Updated [PushT](entities/pusht.md) — added Diffusion Policy paper to Mentioned in (canonical PushT variant); resolved IBC/Diffusion-Policy TBD partially. sources 3→4.
- Updated [Franka Panda](entities/franka-panda.md) — added Diffusion Policy real-world bullet (3 of 4 tasks: mug flipping 90%, pouring 79%, spreading 100%). sources 5→6.
- Updated [Imitation learning](concepts/imitation-learning.md) — added action-chunking convention attribution + 46.9%/12-task headline; added paper to Mentioned in. sources 7→8.
- Updated [index.md](index.md) — added paper entry; bumped Diffusion Policy 1→2 (de-stubbed); PushT 3→4; Franka Panda 5→6; Imitation learning 7→8.

## [2026-05-10] ingest | IBC + BET + DDPM + UMI + TRI (BC-lineage and Diffusion Policy adjacencies)
- Created [IBC Paper](sources/ibc-paper.md) — Florence, Lynch, Zeng et al., Google Research, CoRL 2021 (arxiv 2109.00137); implicit-BC via energy-based models; PushT origin. Abstract-level ingest (PDF not in raw/).
- Created [IBC](entities/ibc.md) entity — energy-based-model BC method; direct ancestor of Diffusion Policy; weak on harder RoboMimic per Diffusion Policy ablation; training instability via InfoNCE noted.
- Created [BET Paper](sources/bet-paper.md) — Shafiullah, Cui, Altanzaya, Pinto, NYU, NeurIPS 2022 (arxiv 2206.11251); transformer + k-means action discretization; multi-modal-BC problem statement. Abstract-level ingest.
- Created [BET](entities/bet.md) entity — direct ancestor of [VQ-BeT](entities/vq-bet.md); strong on BlockPush (`p1=0.96`), weak on Franka Kitchen multi-stage.
- Created [DDPM Paper](sources/ddpm-paper.md) — Ho, Jain, Abbeel, UC Berkeley, NeurIPS 2020 (arxiv 2006.11239); foundational diffusion-model paper; CIFAR-10 FID 3.17. Abstract-level ingest.
- Created [DDPM](entities/ddpm.md) entity — substrate of [Diffusion Policy](entities/diffusion-policy.md); also implicit foil for the JEPA-vs-pixel-prediction argument; iDDPM/DDIM lineage noted.
- Created [UMI Project Page](sources/umi-paper.md) — Chi, Xu, Pan, Cousineau, Burchfiel, Feng, Tedrake, Song; Stanford / Columbia / TRI; RSS 2024 Best Systems Finalist (arxiv 2402.10329); hand-held gripper with wrist GoPro; 30s/demo, 111 demos/hour, zero-shot UR5e + Franka transfer. Project-page ingest.
- Created [UMI](entities/umi.md) entity — same-lead-author follow-on to Diffusion Policy; data-collection-side companion; cited as Stick-v2 design inspiration in [Robot Utility Models Paper](sources/robot-utility-models-paper.md) §2.1.
- Created [TRI Website](sources/tri-website.md) — Toyota Research Institute homepage; mission + 5 research areas (automated driving, energy/materials, human-centered AI, human interactive driving, robotics); Atlas-robot reference TBD.
- Created [TRI](entities/tri.md) entity — co-affiliation hub: Cousineau / Burchfiel / Feng on Diffusion Policy; same + Tedrake on UMI; TRI LBM referenced in RoboCasa365 paper as baseline. Drake on TBD list.
- Updated [Diffusion Policy](entities/diffusion-policy.md) — closed 4 of 5 TBDs (IBC, BET, DDPM, UMI, TRI now filed); added direct-successor lineage section; added Related links to all 5 new entities. sources 2→3 (added UMI Project Page).
- Updated [Diffusion Policy Paper](sources/diffusion-policy-paper.md) — closed same TBDs; updated Baselines references to point at new IBC/BET entity + source pages; TRI link redirected from placeholder to [TRI](entities/tri.md).
- Updated [VQ-BeT](entities/vq-bet.md) — added BET as direct ancestor (k-means → learned VQ codebook); added IBC as earlier multi-modal-BC ancestor; added Mahi Shafiullah cross-link.
- Updated [PushT](entities/pusht.md) — IBC paper now filed as origin; added to Mentioned in. sources 4→5.
- Updated [Franka Panda](entities/franka-panda.md) — UMI added as deployment platform (1 of 2 alongside UR5e). sources 6→7.
- Updated [Mahi Shafiullah](entities/mahi-shafiullah.md) — BET as first-author paper; sources 2→3.
- Updated [Lerrel Pinto](entities/lerrel-pinto.md) — BET as senior-author paper; earliest in his wiki trajectory; sources 2→3.
- Updated [index.md](index.md) — 5 new source entries; new [TRI](entities/tri.md) under Companies; new [IBC](entities/ibc.md), [BET](entities/bet.md), [UMI](entities/umi.md) under Behavior-cloning methods; new "### Generative models" subsection with [DDPM](entities/ddpm.md); bumped Diffusion Policy 2→3, Franka Panda 6→7, PushT 4→5; updated Known gaps TBD list to reflect 5 resolutions and 4 new follow-on TBDs (DDIM, iDDPM, R3M, author pages for Chi/Song/Du/Tedrake).

## [2026-05-10] curriculum-outline | Robot-learning curriculum from neurons to LeWorldModel
- Created [Robot-learning curriculum](syntheses/robot-learning-curriculum.md) — 14-module bottom-up syllabus (NN → CNN → attention → SSL → generative → BC lineage → RL vocab → VLA → world models → JEPA depth → LeWM deep-dive → home-robotics deployment → capstone).
- Audience: strong programmer with some ML / robotics exposure.
- Format: module-per-synthesis. Hub is the syllabus; each module body is a separate synthesis page filed on signal.
- PushT chosen as the connecting thread across tiers 2–4.
- Updated [index.md](index.md) — new "Curriculum / learning path" highlights entry; new bullet under Syntheses.
- Open scoping questions filed at the bottom of the curriculum page (Tier 1 brevity, math depth on SIGReg / DDPM, capstone hardware-or-paper, classical-robotics scope).

## [2026-05-10] resolve | Curriculum scoping decisions + glossary
- User answered the 5 open scoping questions on [Robot-learning curriculum](syntheses/robot-learning-curriculum.md):
  1. Tier 1 stays at 4 modules (NN / CNN / attention / SSL).
  2. SIGReg math: **go deep** (full random-projection + normality test + backprop derivation in Module 12).
  3. DDPM math: **go deep** (full forward/reverse + ELBO + KL + CFG derivation in Module 5).
  4. Capstone: paper first (phase A required), Stretch hardware second (phase B gated on hardware).
  5. Modules 13 + 14 both retained.
- Created [Glossary](glossary.md) — flat acronym reference covering ~80 terms across NN basics, CNNs, sequence models, SSL, generative models, BC/IL, RL, VLA, world models, robot platforms, and infra. Each entry tags the curriculum module that introduces it.
- Updated [Robot-learning curriculum](syntheses/robot-learning-curriculum.md):
  - New "Decisions (resolved 2026-05-10)" section near the top.
  - First-mention acronyms throughout all 14 modules now spell out and link to glossary anchors.
  - Modules 5 and 12 expanded to flag the full-math depth.
  - Module 14 split into phase A (paper / sim, required) + phase B (hardware, gated).
  - Effort estimate updated for "go deep" decisions: ~125–205 hr without hardware phase.
  - Removed "Open scoping questions" section (now resolved).
- Updated [index.md](index.md) — Curriculum highlights now lists [Glossary](glossary.md).

## [2026-05-10] sort | Glossary alphabetized
- User asked to sort [Glossary](glossary.md) alphabetically rather than by curriculum module.
- Flattened the per-module sections into a single A–Z list (case-insensitive, hyphens ignored). Per-entry "(Module N)" annotations preserved so the curriculum mapping stays intact.
- Added a fourth bullet under "How to use" noting the new sort order.

## [2026-05-10] ingest | DreamerV3 + TD-MPC2 + π0 + Helix (curriculum-driven backfill of LeWM baselines and VLA exemplars)
- All four ingests are abstract / blog-post depth (PDFs not in `raw/`). Filed to unblock curriculum modules 8–10 (RL + world models) and 9 (VLAs); flagged for re-ingest at higher fidelity if module bodies need it.
- Created [DreamerV3 Paper](sources/dreamer-v3-paper.md) — Hafner, Pasukonis, Ba, Lillicrap (arxiv 2301.04104, Jan 2023); single-config MBRL across 150+ tasks; first to mine Minecraft diamonds without human data/curricula. Generative-style WM (predicts state + reward) + actor-critic in imagination.
- Created [Dreamer / DreamerV3](entities/dreamer.md) entity — family lineage (PlaNet → V1 → V2 → V3); position table vs TD-MPC, LeWM, DINO-WM on the four design axes (latent dynamics, decoder?, planning method, value bootstrap?).
- Created [TD-MPC2 Paper](sources/td-mpc2-paper.md) — Hansen, Su, Wang (ICLR 2024, arxiv 2310.16828); decoder-free latent WM + local trajectory MPC + TD-bootstrapped value; 104 tasks / 4 domains / 317M-param multi-task agent. The closest MBRL relative to JEPA in this wiki.
- Created [TD-MPC / TD-MPC2](entities/td-mpc.md) entity — same 4-axis position table.
- Created [π0 Paper](sources/pi-zero-paper.md) — Black, Brown, Driess et al., Physical Intelligence (arxiv 2410.24164, Oct 2024); VLA with **flow-matching** action head on a pre-trained VLM; cross-platform (single-arm, dual-arm, mobile manipulator); laundry folding + table cleaning + box assembly. 24 authors including Levine, Finn, Hausman, Ichter, Pertsch.
- Created [Helix (Figure AI blog)](sources/helix-blog.md) — Figure AI (Feb 2025); hierarchical S1/S2 VLA (7B VLM @ 7–9 Hz + 80M transformer @ 200 Hz, end-to-end-trained); full humanoid upper-body continuous control; multi-robot collaboration; ~500h teleop ("<5%" of typical VLA datasets); onboard inference. Vendor blog only — flagged as marketing-grade until peer-reviewed.
- Updated [World model](concepts/world-model.md) — closed the "Reward-conditioned MBRL not yet ingested as standalone source pages" hedge; added Dreamer (generative-WM MBRL) + TD-MPC (decoder-free MBRL) bullets with source/entity links; added both source pages to Mentioned in; sources 8 → 10. Removed Dreamer/TD-MPC from Open questions (now filed).
- Updated [VLA models](concepts/vla-models.md) — π0 bullet now links the new source page and surfaces the flow-matching action-head choice; new Helix bullet (architecture + claims); added a hierarchical S1/S2 callout; added an "Action-head design across VLAs" comparison table contrasting OpenVLA (AR tokens), π0 (flow matching), Diffusion Policy (DDPM), Helix S1 (continuous regression at 200 Hz), GR00T. sources 9 → 11.
- Updated [Physical Intelligence](entities/physical-intelligence.md) — π0 capability bullet now cites the new paper and names the flow-matching action head + cross-platform training. sources 1 → 2.
- Updated [Figure](entities/figure.md) — full Helix subsection rewritten with S1/S2 specs, Figure-claimed firsts, training scale, marketing-only warning callout. sources 1 → 2 (corrected from 0 in index.md). Closed the "No primary source ingested" open question.
- Updated [Glossary](glossary.md) — added source/entity links to the Dreamer / DreamerV3, TD-MPC, π0, and Helix entries.
- Updated [index.md](index.md) — 4 new sources appended to chronological list; Dreamer + TD-MPC entities added under World models section; Physical Intelligence 1→2 sources, Figure 0→2 sources (`_stub_` removed); World-model concept 8→10, VLA-models concept 8→11; Known gaps lines for Dreamer/TD-MPC closed (PLDM still open).
- Cross-cutting note for the curriculum: the four ingests collectively unblock Modules 8 (RL vocab — Dreamer + TD-MPC as named baselines), 9 (VLA — π0 + Helix as concrete exemplars), and 10 (world models — full four-family taxonomy now backed by primary sources).

## [2026-05-10] curriculum-module | Module 7 drafted — BC lineage on PushT
- Created [Curriculum Module 7 — BC lineage on PushT](syntheses/curriculum-07-bc-lineage-pusht.md) — first drafted curriculum module body (out of 14). Chosen as the template-setter because all five prerequisite source ingests ([IBC](sources/ibc-paper.md), [BET](sources/bet-paper.md), [DDPM](sources/ddpm-paper.md), [Diffusion Policy](sources/diffusion-policy-paper.md), [UMI](sources/umi-paper.md)) were already filed.
- Structure:
  1. Curriculum-context callout + acronym pointer to glossary.
  2. "What this module is" + four learning objectives.
  3. Pedagogical hook on PushT (why the task; multi-modality engineered in by design).
  4. The failure mode of vanilla MSE-BC.
  5. IBC: EBM-as-policy + InfoNCE. Strengths, weaknesses, why it matters.
  6. BeT: k-means discretization + transformer + offset regression. Successor (VQ-BeT).
  7. Diffusion Policy: conditional DDPM over action chunks + receding horizon. The contemporary default. Quantitative results from the paper.
  8. Visual encoders side-note (ResNet-18 vs R3M vs DINOv2).
  9. UMI in one paragraph (data-collection context).
  10. **The bridge to Module 10** — BC lineage vs world-model lineage as two answers to the same PushT problem; comparison table.
  11. Anchor exercise — run pretrained Diffusion Policy on PushT; sample-and-plot multi-modal action chunks; compare against MSE-BC baseline.
  12. Recommended reading order.
  13. What you should now be able to do.
  14. Related curriculum modules + Mentioned in + Open questions.
- Updated [Robot-learning curriculum](syntheses/robot-learning-curriculum.md) — Module 7 entry now links the drafted page (replacing "Future home"); coverage table cell updated to "drafted"; status frontmatter notes Module 7 drafted.
- Updated [index.md](index.md) — new Highlights bullet under Curriculum (Module 7 link); new Syntheses bullet for the module page.
- Pattern set for future modules: a curriculum module body should orient → state objectives → tell a narrative → end with an anchor exercise + reading order + open questions. Module 7 is ~12kB; expect tier-1 modules (NN, CNN, attention, SSL) to be similar size; tier-2/3 modules (Module 5, Module 7, Module 10) somewhat longer; Module 12 (LeWM deep-dive with full SIGReg math) will be the longest.

## [2026-05-10] curriculum-module | Module 6 drafted — Imitation learning and behavior cloning
- Created [Curriculum Module 6 — Imitation learning and behavior cloning](syntheses/curriculum-06-imitation-learning.md) — second drafted module; the conceptual prerequisite Module 7 implicitly assumed. Written after Module 7 to close the reader-order gap (Module 7 references "the multi-modal-action failure mode" as if Module 6 were already in place).
- Structure (~12kB):
  1. Curriculum-context callout + acronym pointer to glossary; explicit "Module 7 is the direct successor" framing.
  2. Five learning objectives.
  3. IL vs RL vs world-model + planning comparison table; explicit "why IL dominates 2023–2026 robotics" paragraph.
  4. BC as the simplest possible IL — dataset, model, loss, training, inference, all spelled out.
  5. Where the demonstrations come from — teleop, scripted, human video, cross-platform; the data-diversity-over-quantity scaling pattern (RUM finding).
  6. **Failure mode 1: multi-modal action distributions** — precise statement, mode-averaging math (`E[a|s] = (a_1+a_2)/2` not in either mode), examples, hand-off to Module 7.
  7. **Failure mode 2: distribution shift** — covariate-shift framing, the O(T²) Ross-Bagnell bound, DAgger as the classical fix, why DAgger isn't run in modern practice (data-coverage substitute).
  8. Action chunking + receding-horizon control (orthogonal to action-head choice; Module 7 covers in detail).
  9. Canonical PushT setup (brief; pointer to the [PushT entity](entities/pusht.md) for full mechanics).
  10. **Anchor exercise** — train a vanilla MSE-MLP BC policy on state-variant PushT, roll out for 50 episodes, plot the policy alongside demo trajectories, observe mode-averaging at ambiguous states. Optional extension: mixture-of-Gaussians head (the LSTM-GMM Diffusion Policy ablation).
  11. Recommended reading (concept page → PushT entity → Pomerleau 1989 → DAgger paper → RUM paper); explicit "do not yet read IBC/BeT/DP — that's Module 7."
  12. Hand-off to Module 7 — names IBC, BeT, Diffusion Policy as the three answers to multi-modality.
  13. Related modules + Mentioned in + Open questions.
- Updated [Robot-learning curriculum](syntheses/robot-learning-curriculum.md) — Module 6 entry now links the drafted page; coverage table cell updated to "drafted"; status frontmatter notes Modules 6 + 7 drafted.
- Updated [index.md](index.md) — Highlights bullet for Module 6; Syntheses bullet for Module 6; reader-order is now Module 6 → Module 7.
- Notes for sequencing: Modules 6 + 7 are now reader-consumable in order. The next prereqs that block reader-order continuation are Module 5 (DDPM math, "go deep") for the Diffusion Policy section of Module 7, and Modules 1–4 (Tier 1 ML foundations) for everything. Module 10 (world models, broad) is reader-dependency-light because Modules 6 + 7 + Tier 1 are its main prereqs and Module 10 itself is mostly synthesis from existing wiki pages.

## [2026-05-10] curriculum-module | Module 10 drafted — World models, broad
- Created [Curriculum Module 10 — World models, broad](syntheses/curriculum-10-world-models.md) — third drafted module; the bridge into Tier 4 (JEPA depth + LeWM deep-dive). Chosen as the next module because it had the most existing wiki material to lean on ([world-model concept](concepts/world-model.md), [WM simulators concept](concepts/world-model-simulators.md), [generative-video vs JEPA synthesis](syntheses/generative-video-vs-jepa-world-models.md), 8 WM entity pages including the just-filed Dreamer + TD-MPC) and unlocks the Tier-4 destination of the curriculum.
- Structure (~14kB):
  1. Curriculum-context callout — Tier 4 bridge framing; explicit statement that "LeWM = JEPA, end-to-end-trained, with MPC planner" reads as word-soup without this module.
  2. Five learning objectives.
  3. Functional definition — refers out to [`concepts/world-model.md`](concepts/world-model.md) for the design-axis table; flags world-model ≠ world-simulator distinction.
  4. **The four families** with one example, one structural commitment, pros, cons each:
     - Generative-video (Cosmos, Genie Envisioner — DDPM substrate)
     - JEPA / latent-prediction (V-JEPA 2, LeWM, PLDM — LeCun's program)
     - Frozen-foundation-feature (DINO-WM, JEPA-WMs — DINOv2 base)
     - Reward-conditioned MBRL (Dreamer = generative; TD-MPC = decoder-free)
     Plus a four-row comparison table.
  5. **Planning vocabulary** — MPC loop pseudocode; CEM (full pseudo-code; named as the dominant sampler); MPPI as sibling; gradient-based MPC tradeoffs; "default to assuming MPC means CEM-MPC" rule of thumb.
  6. **Horizon and compounding error** — the O(H) → O(H²) intuition; per-task horizon ranges (5–20 for JEPA / frozen / MBRL); value-bootstrap as the trick that lets MBRL extend effective horizon.
  7. Generative-video vs JEPA tradeoff — points to the [existing synthesis](syntheses/generative-video-vs-jepa-world-models.md); surfaces three load-bearing facts (48× planning gap, action-free pretraining, complementary-not-competing paradigms).
  8. **Where LeWM lives** — explicit 8-axis table positioning LeWM's choices against alternatives (end-to-end encoder vs frozen; SIGReg vs PLDM/V-JEPA collapse zoo; no value function vs Dreamer/TD-MPC; no reward at training vs MBRL). Each axis flagged as "a contestable bet" the reader should be able to evaluate by Module 12.
  9. **Anchor exercise** — 3-line MPC pseudocode + three concrete extensions (CEM upgrade; toy-MLP-on-pendulum to *see* the optimal-horizon peak; gradient-based MPC comparison). Bridge to LeWM howto code.
  10. Recommended reading (concept pages → generative-video-vs-JEPA synthesis → V-JEPA 2 / DreamerV3 / TD-MPC2 abstracts → LeWM Fig 1 only).
  11. What you should now be able to do.
  12. Hand-off to Module 11 — names V-JEPA progression, collapse-prevention zoo, DINO-WM vs end-to-end, JEPA-WMs.
  13. Related modules + Mentioned in + Open questions (PLDM ingest still gap; Genie Envisioner deeper paper; CEM walkthrough; MPPI source).
- Updated [Robot-learning curriculum](syntheses/robot-learning-curriculum.md) — Module 10 entry now links the drafted page; coverage table cell updated to "drafted" with full pre-existing-coverage list (concept + simulators concept + GV-vs-JEPA synthesis + Dreamer + TD-MPC entities and sources); status frontmatter notes Modules 6 + 7 + 10 drafted.
- Updated [index.md](index.md) — Highlights bullet for Module 10; Syntheses bullet for Module 10; reader hint that Modules 6 → 7 and Module 10 are now consumable.
- Sequencing note: Modules 6 + 7 + 10 are the three most-loaded modules in the curriculum (most pre-existing wiki material), and they're now drafted. Remaining work splits into:
  - **Tier 1 greenfield** (Modules 1–4: NN, CNN, attention, SSL).
  - **Module 5** (DDPM math, "go deep" — heaviest single piece because of derivations).
  - **Module 8** (RL vocabulary — light; just enough to read MBRL papers).
  - **Module 9** (VLA — has π0 + Helix sources; mostly synthesis from existing concept page).
  - **Module 11** (JEPA depth — heavy synthesis; existing JEPA concept page + V-JEPA 2 / 2.1 / DINO-WM / JEPA-WMs / VLA-JEPA sources).
  - **Module 12** (LeWM deep-dive with full SIGReg math — the destination, longest module).
  - **Modules 13 + 14** (deployment + capstone — leans on already-rich syntheses).

## [2026-05-10] curriculum-module | Module 11 drafted — JEPA in depth
- Created [Curriculum Module 11 — JEPA in depth](syntheses/curriculum-11-jepa-deep.md) — fourth drafted module; the Tier-4 successor to Module 10. The single most material-rich module in the curriculum (existing concept page + 6 source pages + 8 entity pages + 3 syntheses).
- Structure (~17kB):
  1. Curriculum-context callout — Tier-4 chain (Module 10 → 11 → 12); explicit framing that SIGReg math is deferred to Module 12.
  2. Six learning objectives.
  3. **What "joint embedding" means** — the architectural commitment (same encoder both sides; loss in latent space); contrast with generative/AR; **why representation collapse is a first-order failure mode** (loss=0 at constant latent).
  4. **The collapse-prevention zoo** — six families with pseudocode where useful: EMA + stop-grad (BYOL/V-JEPA), variance-covariance (VICReg/Barlow Twins), frozen encoder (DINO-WM), asymmetric augmentation (SimCLR), multi-fix soup (PLDM, 4–6 hyperparameters), SIGReg (LeWM, 1 hyperparameter). Side-by-side comparison table.
  5. **V-JEPA progression** — V-JEPA 1 → V-JEPA 2 (1B params, 22M videos, 1M+ hrs) → V-JEPA 2-AC (300M predictor, 62hr DROID, zero-shot Franka in 2 new labs) → V-JEPA 2.1 (dense features, +20pt grasping). Variant scale table; the 16,000× pretraining-vs-post-training data ratio.
  6. **Frozen-feature variants** — DINO-WM (NYU+FAIR, lightweight benches), DINO-world (FAIR, video-scale), JEPA-WMs (FAIR Dec 2025, first JEPA-on-RoboCasa + real Franka).
  7. **Action conditioning** — action-free pretraining + action-conditioned post-training; predictor-level pseudocode; tie back to home-robotics teleop scarcity (Module 13).
  8. **VLA-JEPA** — JEPA-as-auxiliary in a VLA; the cross-over with Module 9.
  9. **LeWM-vs-V-JEPA-2 axis-by-axis** — 9-row comparison table sharper than Module 10's: encoder size (1B vs 15M), encoder training (EMA+stop-grad vs nothing), pretraining data (1M+hr vs none), action stage (post-train vs co-train), anti-collapse mechanism (EMA + L1 + ... vs single SIGReg), anti-collapse hyperparameters (~3 vs 1). The two are not competing for the same job — generalist vs single-task — and LeWM's contribution is methodological (one knob), not scaling.
  10. **Anchor exercise** — annotate LeWM Fig 1 against V-JEPA 2 and DINO-WM; deeper variant: implement a toy 2D JEPA and watch it collapse without anti-collapse mechanisms (then rescue it with each fix in turn).
  11. Recommended reading (concept page → V-JEPA 2 + GitHub + 2.1 → DINO-WM → JEPA-WMs → VLA-JEPA → LeWM architecture only — explicit "do NOT yet read SIGReg derivation").
  12. What you should now be able to do.
  13. Hand-off to Module 12 — names the SIGReg derivation pieces (random projections + empirical CDF + Anderson-Darling-style normality test + backprop through test statistic).
  14. Related modules + Mentioned in + Open questions (PLDM ingest still gap; toy-JEPA notebook; DINOv2 paper; LeCun 2022 position paper).
- Updated [Robot-learning curriculum](syntheses/robot-learning-curriculum.md) — Module 11 entry now links the drafted page; coverage table cell updated to "drafted"; status frontmatter notes Modules 6 + 7 + 10 + 11 drafted.
- Updated [index.md](index.md) — Highlights bullet for Module 11; Syntheses bullet for Module 11; reader-order is now Modules 6 → 7 and 10 → 11, all consumable.
- Tier 4 is now half-drafted (Modules 10 + 11). Module 12 (LeWM deep-dive with full SIGReg math) is the destination and the longest module by design.

## [2026-05-10] curriculum-module | Module 12 drafted — LeWorldModel deep-dive (with full SIGReg math)
- Created [Curriculum Module 12 — LeWorldModel deep-dive (with full SIGReg math)](syntheses/curriculum-12-lewm-deep-dive.md) — **the curriculum destination**. Fifth drafted module, completes Tier 4.
- Source: full PDF extraction of `raw/LeWorldMode_2603.19312v2.pdf` via pypdf (per [PDF extraction memory](file:///home/tklyce/.claude/projects/-home-tklyce-projects-tanio-robot-research/memory/pdf_extraction.md)). The paper's method, planning, and results sections were re-read from the PDF rather than from the paraphrased source page.
- **Two corrections found during the deep-dive:**
  - The curriculum hub previously described SIGReg's normality test as "Anderson-Darling-style." The paper actually uses **Epps–Pulley**. Curriculum hub fixed; module 12 flags the correction in a top-level callout.
  - The glossary's SIGReg expansion was "Sliced Integral Gaussian Regularization" (with a TBD flag). The paper's actual name is **Sketched Isotropic Gaussian Regularizer** (Balestriero 2025, ref [25] in the LeWM paper). Glossary entry rewritten with the correct name + the Epps-Pulley / Cramér–Wold pieces in place.
- Structure (~25kB; longest module by design):
  1. Curriculum-context callout (destination framing) + the Epps–Pulley vs Anderson-Darling correction.
  2. Six learning objectives.
  3. **§1 — The two-loss architecture** with full forward-pass diagram + 10-line PyTorch pseudocode of the training step.
  4. **§2 — SIGReg in detail (the mathematical centerpiece)**, eight subsections:
     - 2.1 The goal (match isotropic Gaussian; rules out collapse trivially).
     - 2.2 Why high-dim normality testing is hard (multivariate tests don't scale).
     - 2.3 Random-projection sketch — projections `h^(m) = Z u^(m)` with `u^(m) ∈ S^{d-1}`.
     - 2.4 **Cramér–Wold theorem** — formal justification (matching all 1D marginals = matching joint).
     - 2.5 **Epps–Pulley univariate normality test** — explicit integral form via empirical characteristic function vs `e^{-t²/2}`; smooth + differentiable + full-distribution-sensitive (vs Anderson-Darling / KS which are quantile-based and non-smooth).
     - 2.6 **Backprop through the test statistic** — the calculus chain `∂T/∂h_k → ∂T/∂Z`.
     - 2.7 Hyperparameter analysis: M and K empirically insensitive; only λ matters (default 0.1; bisection-tunable in O(log n) vs PLDM's O(n^6)).
     - 2.8 SIGReg in one sentence — every word maps to a design decision.
  5. **§3 — Architecture details** including the **BN-after-CLS-token trick** (load-bearing! ViT's terminal LayerNorm pre-normalizes away the batch distribution SIGReg operates on; swapping to BN in the projection MLP is what makes SIGReg optimizable). Predictor: AdaLN-zero-init for action conditioning, 6-layer transformer + dropout.
  6. **§4 — Latent planning (CEM-MPC)** — terminal goal-matching cost `C(ẑ_H) = ‖ẑ_H − z_g‖²`; CEM solver pseudocode; receding horizon; horizon vs compounding error tradeoff. The 48× speedup decomposed (~200× fewer tokens than DINO-WM).
  7. **§5 — Empirical results** with the headline four-environment table (PushT, Reacher, OGBench-Cube, Two-Room) including the **Two-Room failure case** as a real SIGReg limitation (Gaussian prior over-regularizes when intrinsic task complexity is too low). Ablations on M, K, embedding dim d, encoder architecture (ResNet-18 also works → architecture-agnostic).
  8. **§6 — Latent-space analysis**: physical-quantity probing (Table 1: LeWM beats PLDM, competitive with DINO-WM); latent decoder reconstruction (despite no reconstruction in training); t-SNE; **temporal latent path straightening as an emergent property** (LeWM beats PLDM on this without a smoothness term, despite PLDM having one).
  9. **§7 — Violation-of-expectation framework** — surprise = `‖ẑ_{t+1} − z_{t+1}‖`, used to flag physically implausible events.
  10. **§8 — What this all means** — LeWM as a *methodological* (not scaling) contribution; the bridge to home-robotics deployment via the 15M-param-trainable-on-a-single-GPU profile.
  11. **Anchor exercise** — Part A: reproduce LeWM PushT (per [howto](syntheses/leworldmodel-howto.md) + [hello-world scope](syntheses/lewm-hello-world-project-scope.md)). Part B: derive the SIGReg gradient on paper.
  12. Recommended reading (LeWM paper end-to-end, GitHub, V-JEPA 2 GitHub as counterpoint, Balestriero 2025 SIGReg paper, generative-video-vs-JEPA synthesis, hello-world scope).
  13. What you should now be able to do.
  14. Hand-off to Modules 13 + 14.
  15. Related modules + Mentioned in + Open questions (Balestriero 2025 source page; PLDM ingest; Two-Room threshold quantification; SIGReg-at-scale).
- Updated [Robot-learning curriculum](syntheses/robot-learning-curriculum.md) — Module 12 entry now links the drafted page; fixed the "Anderson-Darling-style" → "Epps–Pulley" / "Cramér–Wold" reference; coverage table cell updated to "drafted"; status frontmatter notes Modules 6 + 7 + 10 + 11 + 12 drafted (Tier 4 complete).
- Updated [Glossary](glossary.md) — SIGReg entry rewritten: correct expansion (Sketched Isotropic Gaussian Regularizer), Balestriero 2025 attribution, Epps–Pulley test, Cramér–Wold theorem, λ default 0.1.
- Updated [index.md](index.md) — Highlights bullet + Syntheses bullet for Module 12; reader can now traverse Modules 6 → 7 and 10 → 11 → 12.
- Tier 4 is now complete. The curriculum's destination (Module 12) is reachable from the wiki's filed material. Five of fourteen modules are drafted.

## [2026-05-10] curriculum-module | Module 9 drafted — Vision-Language-Action models
- Created [Curriculum Module 9 — Vision-Language-Action models](syntheses/curriculum-09-vla.md) — sixth drafted module; closes the policy-side reading chain (Modules 6 → 7 → 9). Sibling of the world-model chain (Modules 10 → 11 → 12).
- Structure (~13kB):
  1. Curriculum-context callout — bridges into both Modules 7 and 11.
  2. Five learning objectives.
  3. Structural definition of a VLA (vision encoder + language tokens + trunk + action head); VLA vs VLM contrast.
  4. **VLA vs BC** — comparison table; the "scaling up + language conditioning + VLM-pretraining" framing.
  5. **Why VLAs aren't world models** — different jobs (actions vs next-state predictions); architectural similarity ≠ identity.
  6. **Action-head design** — AR tokens (OpenVLA), flow matching (π0), DDPM (Diffusion Policy / hybrids); recap table from concepts/vla-models.md.
  7. Major 2026 VLAs in one paragraph each: GR00T, π0, Helix (with S1/S2 caveat), Gemini Robotics (incl. -ER tool-call variant distinction), OpenVLA, smaller VLAs.
  8. **Hierarchical S1/S2 pattern** — recurring across Helix, GR00T, Gemini Robotics-ER; rate-decoupling intuition (~10 Hz reasoning + ~200 Hz control).
  9. **VLA-JEPA cross-over** — explicit architecture diagram showing the JEPA auxiliary loss alongside imitation loss; the "JEPA as a component, not a competitor" framing; bridge to Module 11.
  10. **Anchor exercise** — sketch data flow for π0 / Diffusion Policy / LeWM-MPC on the same PushT episode (3-architecture ASCII diagram); compare per-tick latency budgets and predict 30 Hz feasibility on consumer hardware.
  11. Recommended reading; What you should now be able to do; Closing the policy-side reading chain (with explicit "Module 13 evaluates both chains against deployment reality").
  12. Related modules + Mentioned in + Open questions (OpenVLA + GR00T N1.x + π0.6 source pages still TBD; Helix peer-reviewed paper still doesn't exist; flow-matching concept page on demand).
- Updated [Robot-learning curriculum](syntheses/robot-learning-curriculum.md) — Module 9 entry now links the drafted page; coverage table cell updated to "drafted" with full pre-existing-coverage list (concept page + 4 entity pages + 3 source pages); status frontmatter notes both reading chains complete.
- Updated [index.md](index.md) — Highlights bullet for Module 9; Syntheses bullet for Module 9.
- **Reader status:** Modules 6 → 7 → 9 (policy chain) and 10 → 11 → 12 (world-model chain) are both complete. The two paradigms cross over at [VLA-JEPA](entities/vla-jepa.md), covered in detail in this module. Six of fourteen modules drafted.

## [2026-05-10] curriculum-module | Module 13 drafted — Home robotics deployment reality
- Created [Curriculum Module 13 — Home robotics deployment reality](syntheses/curriculum-13-home-robotics-deployment.md) — seventh drafted module. Deliberately leans on existing rich syntheses ([assistive-robotics-research-landscape.md](syntheses/assistive-robotics-research-landscape.md), [stretch-as-assistive-platform.md](syntheses/stretch-as-assistive-platform.md), [levels-of-autonomy-in-assistive-robotics.md](syntheses/levels-of-autonomy-in-assistive-robotics.md), [underserved-par-domains.md](syntheses/underserved-par-domains.md), [lewm-on-stretch-feasibility.md](syntheses/lewm-on-stretch-feasibility.md), [dino-wm-on-stretch-experiment.md](syntheses/dino-wm-on-stretch-experiment.md)) as a curriculum-shaped framing of work already done.
- Structure (~12kB):
  1. Curriculum-context callout — explicit "read these existing syntheses *with* this module" framing (not "read after").
  2. Six learning objectives.
  3. **The 89.4 / 12.4 gap** — RLBench vs BEHAVIOR-1K (per Stanford HAI AI Index 2026); what changes between them (clutter, horizons, robustness, diversity).
  4. **Stretch convergence** — eight features compounding (price, Python API, ~22 dB, MuJoCo/Gazebo support, stretch_ai stack, active research community, Henry Evans deployments). What Stretch *doesn't* solve (bimanual, dexterity, whole-body).
  5. **The "real-data" path** — RUM (NYU/Meta, ~90% on novel envs, data-diversity-over-quantity insight) + OK-Robot (10 NYC homes, 58.5%, VLM + classical pipeline). The honest-pull statement: **the strongest 2026 home-robotics result is BC, not WM** — the WM bet is not yet vindicated empirically.
  6. **PAR + autonomy-preference** — Nanavati 2024 review (1,981 screened, 87 included, half no-PwD); Yang et al. 2025 sense-of-agency finding; Henry Evans summer-deployment record; three-axis autonomy decomposition.
  7. **EUP** — what it is; why it's the natural home for data-efficient policy-learning techniques; HCR Lab as the dominant wiki-cited thread.
  8. **Underserved PAR domains** table (dressing / bathing / medication) with **medication-fetcher** named as the most-tractable researcher target.
  9. **Where LeWM-class techniques fit** — explicit "plausibly move" (data efficiency, planning speed, action-consequence safety/pre-emption) vs "plausibly does not move" (whole-body, long-horizon, robustness-from-pretraining) lists.
  10. **Anchor exercise** — read [LeWM-on-Stretch feasibility](syntheses/lewm-on-stretch-feasibility.md) + [DINO-WM-on-Stretch plan](syntheses/dino-wm-on-stretch-experiment.md), pick one, defend the choice. Explicit framing as "argument for LeWM" vs "argument for DINO-WM" with my-personal-lean (DINO-WM first, LeWM second). Module 14 phase A is "actually scope the experiment you defended here."
  11. Recommended reading + What you should now be able to do + Hand-off to Module 14 + Related modules + Mentioned in + Open questions (LeWM-on-Stretch result; BEHAVIOR-1K WM result; cross-paradigm head-to-head; long-horizon WM eval).
- Updated [Robot-learning curriculum](syntheses/robot-learning-curriculum.md) — Module 13 entry now links the drafted page; coverage table cell updated to "drafted"; status frontmatter notes Module 13 drafted.
- Updated [index.md](index.md) — Highlights bullet for Module 13; Syntheses bullet for Module 13.
- **Reader status:** Seven of fourteen modules drafted. The deployment-reality framing is in place, ready for Module 14 (capstone) to land on top of it.

## [2026-05-10] curriculum-module | Module 14 drafted — Capstone (paper-first, hardware-second)
- Created [Curriculum Module 14 — Capstone (paper-first, hardware-second)](syntheses/curriculum-14-capstone.md) — eighth drafted module; the curriculum's terminating exercise. Pointer page tying Modules 12 + 13 to existing wiki artifacts ([hello-world scope](syntheses/lewm-hello-world-project-scope.md), [LeWM howto](syntheses/leworldmodel-howto.md), [LeWM-on-Stretch feasibility](syntheses/lewm-on-stretch-feasibility.md), [DINO-WM-on-Stretch plan](syntheses/dino-wm-on-stretch-experiment.md)).
- Structure (~10kB):
  1. Curriculum-context callout — phase-A required, phase-B hardware-gated.
  2. What the capstone is — three concrete deliverables.
  3. **Phase A (paper / sim — required):**
     - A.1: reproduce LeWM PushT (one-knob ablation flipping `λ` to feel collapse vs prediction-loss-failure failure modes; the BN-after-CLS engineering footgun explicitly flagged).
     - A.2: SIGReg gradient derivation on paper.
     - A.3: 5–10 page experiment-design memo with eight required sections (task, architecture, data, baselines, metrics, risk register, what-you'd-learn, phase-B gating).
  4. **Phase B (real Stretch — gated):** hardware logistics ($25K Stretch RE3, 40–80+ hr execution); explicit "honest reporting" framing (report what you got, including failure-to-beat-baseline); follow-up memo / short paper as deliverable.
  5. Beyond the capstone — two follow-on research questions (does SIGReg scale to Stretch data; does WM + planning beat or lose to BC + scaled data).
  6. Recommended reading (re-read of all relevant prior artifacts).
  7. What you should now be able to do.
  8. Closing the curriculum — what understanding-becomes-capability looks like.
  9. Related modules + Mentioned in + Open questions (no published LeWM-on-Stretch / DINO-WM-on-Stretch result yet — the capstone is designed to *be* that result).
- Updated [Robot-learning curriculum](syntheses/robot-learning-curriculum.md) — Module 14 entry now links the drafted page; coverage table cell updated to "drafted"; status frontmatter notes Tiers 3–5 complete.
- Updated [index.md](index.md) — Highlights bullet for Module 14; Syntheses bullet for Module 14.
- **Reader status:** Eight of fourteen modules drafted. **Tiers 3–5 are complete.** Remaining: Tier 1 (Modules 1–4 ML foundations; greenfield), Module 5 (DDPM full math; heavy), Module 8 (RL vocabulary; light). A reader with ML basics already can traverse the entire curriculum end-to-end (Modules 6 → 7 → 9, 10 → 11 → 12, 13 → 14).

## [2026-05-10] curriculum-module | Module 8 drafted — RL vocabulary
- Created [Curriculum Module 8 — Reinforcement learning vocabulary](syntheses/curriculum-08-rl-vocabulary.md) — ninth drafted module. Deliberately **light** (~12kB) per the curriculum decision: "RL is not the focus; read for vocabulary, not implementation."
- Structure:
  1. Curriculum-context callout — explicit "skim in 10 min if you know RL; spend 1–2 hr if you don't."
  2. Four learning objectives (read DreamerV3 paragraphs without confusion; parse TD-MPC2 abstract; distinguish policy gradient from value bootstrap; identify on/off-policy).
  3. **MDP** — the (S, A, P, R, γ) tuple; Markov property as modeling assumption.
  4. **Return, value (V/Q), policy** — three core objects + the V↔Q relationship.
  5. **On/off-policy** distinction with concrete examples (PPO on-policy, DQN/SAC off-policy, BC off-policy-ish, modern robotics RL is mostly off-policy or fully offline).
  6. **Policy gradient** — REINFORCE math; A2C variance-reduction; PPO as the modern default (clipped, on-policy, actor-critic).
  7. **Q-learning** — Bellman recursion; DQN target-network trick; DDPG/TD3/SAC as continuous-action extensions.
  8. **MFRL vs MBRL** — the model-question axis that maps onto Module 10's WM taxonomy (MBRL Family 4).
  9. **Dreamer-class latent imagination** — the specific MBRL recipe (train WM from data; train actor-critic *in* the WM; use the actor on real data; loop). Wins (sample-efficient via free imagined rollouts; reward head extends effective horizon) vs losses (model fidelity; reward labels required at training).
  10. Explicit "what this module is *not* doing" — RL theory, modern MFRL deep-dive, offline RL paradigm, implementation details.
  11. **Anchor exercise** — "read a DreamerV3 figure caption out loud and have it parse"; explicit checklist of phrases (actor-critic, imagined rollouts, RSSM, two-hot reward, symlog, world model latent) and where each is defined in this module.
  12. Recommended reading (Wikipedia → OpenAI Spinning Up → DreamerV3 abstract + intro → TD-MPC2 abstract → Sutton & Barto for depth).
  13. What you should now be able to do; Hand-off (use as reference when reading Modules 10–12).
  14. Related modules + Mentioned in + Open questions (Sutton & Barto + Spinning Up reference pages on demand; PPO + Dreamer notebook).
- Updated [Robot-learning curriculum](syntheses/robot-learning-curriculum.md) — Module 8 entry now links the drafted page; coverage table cell updated to "drafted"; status frontmatter notes only Tier 1 + Module 5 remain.
- Updated [index.md](index.md) — Highlights bullet for Module 8; Syntheses bullet for Module 8 (placed between Module 7 and Module 9 in chronological order).
- **Reader status:** Nine of fourteen modules drafted. Remaining: Tier 1 (Modules 1–4) and Module 5 (DDPM math). All upper-tier modules (5–14) except Module 5 are now drafted.

## [2026-05-10] ingest | PLDM (Sobal et al., WRL @ ICLR 2025) — closes the most-flagged TBD across Modules 10–12
- User asked what PLDM was during the post-Module-8 review. The answer surfaced two corrections the curriculum had been carrying: (1) the glossary's PLDM expansion was "Planning with Latent-**space** Dynamics Models" (paper title is "Planning with Latent Dynamics Models" — no "-space"); (2) Module 12 + glossary referenced the SIGReg foundational paper as "Balestriero 2025" without naming it as **LeJEPA** (Balestriero & LeCun 2025, [arxiv 2511.08544](https://arxiv.org/abs/2511.08544)). Both corrected here.
- Created [PLDM Paper](sources/pldm-paper.md) — Sobal, Zhang, Cho, Balestriero, Rudner, LeCun (NYU + FAIR; WRL @ ICLR 2025 Workshop, Feb 28 2025; OpenReview ID jON7H6A9UU). PDF extracted via pypdf — 21 pages; ingest reads pages 1–5 (abstract + method) and the headline results tables. Architecture: encoder + predictor end-to-end, multi-term loss = similarity (next-embedding MSE) + VICReg-inspired anti-collapse + inverse-dynamics auxiliary. Planning: latent-space MPC with MPPI sampling. Headline result: **the only method out of 6 tested (HILP, HIQL, GCIQL, CRL, GCBC, PLDM) that doesn't completely fail in any of 6 generalization properties** across 23 carefully-controlled offline reward-free datasets.
- Created [PLDM (Planning with Latent Dynamics Models)](entities/pldm.md) entity — family lineage (2022 precursor "Joint embedding predictive architectures focus on slow features" arxiv 2211.10831 + 2025 stress-test paper); architecture summary; position-vs-adjacent-methods table contrasting PLDM (~6 hyperparameters), LeWM (1), DINO-WM (0, frozen), V-JEPA 2-AC (~3), Dreamer (different family — generative WM), TD-MPC (different family — RL bootstrap).
- Updated [Glossary](glossary.md) — PLDM entry: corrected expansion to "Planning with Latent Dynamics Models" + linked source/entity. SIGReg entry: named the foundational paper as **LeJEPA** (Balestriero & LeCun 2025, arxiv 2511.08544).
- Updated [Joint-Embedding Predictive Architecture](concepts/jepa.md) — "no entity pages yet" line replaced; Dreamer / TD-MPC / PLDM all now linked to entity + source pages. sources 7→8.
- Updated [World model](concepts/world-model.md) — JEPA-family bullet now lists end-to-end (V-JEPA 2, LeWM, PLDM) vs frozen-feature (DINO-WM, JEPA-WMs) sub-grouping. PLDM Paper added to Mentioned in. sources 10→11.
- Updated [Curriculum Module 10](syntheses/curriculum-10-world-models.md) — replaced bare "PLDM" with linked [PLDM entity](entities/pldm.md); closed the Open-questions PLDM TBD.
- Updated [Curriculum Module 11](syntheses/curriculum-11-jepa-deep.md) — collapse-prevention zoo §5 (multi-fix soup) now cites PLDM as the canonical reference with details on its specific loss decomposition (similarity + VICReg + inverse-dynamics); closed the Open-questions PLDM TBD; replaced 4 stray glossary-link references to PLDM with entity-link references.
- Updated [Curriculum Module 12](syntheses/curriculum-12-lewm-deep-dive.md) — SIGReg attribution now names LeJEPA as the foundational paper (arxiv 2511.08544); PLDM comparison line now links source + entity pages; closed the PLDM TBD; renamed the Balestriero-2025 TBD to a LeJEPA TBD (still open — the LeJEPA paper itself isn't ingested as a wiki source page).
- Updated [index.md](index.md) — added PLDM Paper to chronological sources list (2025-02); added PLDM entity under World models section (1 source); closed two "PLDM still needs primary-source ingest" lines in Known gaps; bumped concept counts (world-model 10→11, jepa 7→8); deduplicated a stale JEPA concept entry.
- **Result:** All four LeWM baselines ([DINO-WM](entities/dino-wm.md), [Dreamer](entities/dreamer.md), [TD-MPC](entities/td-mpc.md), [PLDM](entities/pldm.md)) now have primary-source pages. The most-flagged TBD across Modules 10–12 is closed.

## [2026-05-10] ingest | Sobal et al. 2022 (PLDM precursor) + LeJEPA (Balestriero & LeCun 2025; SIGReg foundational paper)
- User asked to file the two follow-on TBDs from the PLDM ingest (the 2022 precursor and the LeJEPA paper). Both filed at abstract-level depth.
- Created [Sobal et al. 2022 — JEPA slow features](sources/sobal2022-jepa-slow-features-paper.md) — Sobal, Jyothir S V, Jalagam, Carion, Cho, LeCun (NYU + FAIR; arxiv 2211.10831; NeurIPS 2022 SSL Theory and Practice Workshop short paper). The first paper in the [PLDM](entities/pldm.md) lineage. Establishes the **slow-features framing**: JEPA representations preferentially encode slowly-varying features (e.g. the location of a moving dot in a pixel scene) when distractor noise varies across timesteps. Documents the **fixed-distractor failure mode**: JEPA fails when noise is fixed across timesteps — exposing that the slow-features bias depends on temporal variability.
- Created [LeJEPA Paper](sources/lejepa-paper.md) — Balestriero & LeCun (Brown + NYU/FAIR; arxiv 2511.08544; Nov 2025). The **foundational SIGReg paper**. Headline contributions: (1) prove isotropic Gaussian is the optimal distribution for JEPA embeddings (minimizes downstream prediction risk); (2) propose **SIGReg** (Sketched Isotropic Gaussian Regularizer) — random-projection + univariate normality test + average — as the regularizer that enforces this distributional shape; (3) demonstrate "single hyperparameter, no stop-gradient, no teacher-student, linear time/memory" SSL training that hits **79% ImageNet-1k linear-eval on ViT-H/14** with validation across 10+ datasets / 60+ architectures. **LeJEPA is the methodological precursor to [LeWM](entities/leworldmodel.md)**: same SIGReg, same single-knob recipe, but LeWM applies it to action-conditioned WM with CEM-MPC for offline RL.
- Updated [Glossary](glossary.md) — SIGReg entry now links the LeJEPA source page directly.
- Updated [Curriculum Module 12](syntheses/curriculum-12-lewm-deep-dive.md) — SIGReg attribution links the LeJEPA source page; closed the LeJEPA TBD in Open questions.
- Updated [Curriculum Module 11](syntheses/curriculum-11-jepa-deep.md) — SIGReg row in collapse-prevention zoo table now lists *both* LeJEPA (SSL setting) and LeWM (WM setting); evidence column upgraded from "one paper" to "two papers" reflecting the LeJEPA-LeWM pair. Bullet text under SIGReg subsection now explicitly attributes the optimality claim to LeJEPA.
- Updated [PLDM Paper](sources/pldm-paper.md) source page — predecessor section now links the 2022 source page; closed the 2022 TBD in Open questions.
- Updated [PLDM entity](entities/pldm.md) — family lineage section now links both source pages; sources count 1→2; closed the 2022 TBD in Open questions.
- Updated [JEPA concept page](concepts/jepa.md) — Mentioned in section now lists the new sources; sources count 8→10.
- Updated [index.md](index.md) — both new sources added to chronological list; PLDM entity bumped 1→2 sources; JEPA concept entry bumped 8→10 sources.
- **Result:** the SIGReg-LeWM-PLDM lineage is fully filed. The 2026 LeWM paper now has every cited dependency (LeJEPA for SIGReg theory; PLDM 2022 + 2025 for the end-to-end JEPA baseline) backed by primary-source pages in the wiki.

## [2026-05-10] ingest-deepen | Sobal 2022 + LeJEPA — full PDF ingest of both
- User dropped both PDFs into `raw/` (`2211.10831v1.pdf` for Sobal 2022; `2511.08544v3.pdf` for LeJEPA), explicitly enabling the deeper ingest both source pages had hooks for. Extracted via pypdf per the [PDF extraction memory](file:///home/tklyce/.claude/projects/-home-tklyce-projects-tanio-robot-research/memory/pdf_extraction.md).
- **Sobal 2022 deepened:** rewritten with full architecture details (encoder + predictor + auto-regressive rollout; probing protocol with frozen weights), full method comparison (VICReg-JEPA, SimCLR-JEPA, reconstruction, IDM, supervised, random), the **fixed-distractor failure proof** verbatim (eq. 1–4 in the paper: VICReg's three loss terms all reach 0 at the trivial solution where the encoder ignores foreground and the forward model is identity; SimCLR has the same failure via Wang & Isola's theorem 1), specific dataset details (1M pretraining sequences / 17 frames / two noise types × two temporal regimes), and the empirical-results table (JEPA fails on fixed noise of any kind; reconstruction works for α≤1.5; IDM works in single-dot but fails in 3-dot variant). Added counterintuitive framing: **"JEPA focuses on slow features" is not an unalloyed positive — fixed background = the slowest feature, and JEPA latches on to it instead of the moving dot**, the failure mode that motivates everything else in the JEPA program.
- **LeJEPA deepened:** rewritten with the formal theory chain.
  - **Theorem 1 (isotropic Gaussian optimality):** k-NN regression and kernel regression both have isotropic Gaussian as the *unique* minimizer of integrated square bias under a scalar-covariance constraint.
  - **Lemma 3 (hyperspherical Cramér-Wold):** matching all 1D marginals along directions on `S^{d-1}` is equivalent to matching the joint distribution.
  - **Theorem 2 (sufficiency of directional tests):** the max over `M` directional Epps-Pulley statistics is a level-α + power-1 test, asymptotically.
  - **Definition 2 (practical SIGReg):** **average** over directions, not max — the paper's explicit practical departure from Theorem 2's formal max, made for gradient flow ("avoid sparse gradient over the directions").
  - **Theorem 3 (insufficiency of K moments):** finite-K moment matching is non-identifying; going to large K causes gradient instability.
  - **Why Epps-Pulley** rigorously: ECF is differentiable + parallelizable via `all_reduce` + has bounded loss/gradient/**curvature**. CDF-based (Cramér-von Mises, Anderson-Darling, Watson) require sorting → break SGD parallelism + non-differentiable. KS uses `ℓ_∞` → sparse gradients. Shapiro-Wilk found unstable.
  - Empirical breadth: 10+ datasets, 60+ architectures, up to **1.8B-parameter ViT-g** trained without stop-gradient with stable loss curves. Loss-vs-linear-probe Spearman correlation 94.52% (training loss is a usable model-selection signal without a labeled probe).
- **Module 12 cascaded:**
  - Added a callout in §2.3 explicitly flagging the **average-vs-max** distinction (LeJEPA Theorem 2 = max, formally consistent; Definition 2 = average, practical for gradient flow). Module 12's earlier text was correct but didn't surface this departure.
  - Tightened §2.5 (Why Epps-Pulley) with the LeJEPA §4.2 walkthrough: added bounded *curvature* to the bounded loss/gradient claims; added `all_reduce` distributability; added the explicit ruling-out of moment-based / CDF-based / KS / Shapiro-Wilk alternatives.
- **Module 11 cascaded:** SIGReg row in the collapse-prevention zoo table now mentions the LeJEPA scale evidence (1.8B ViT-g, 10+ datasets / 60+ architectures) and names the formal proof tools (hyperspherical Cramér-Wold + Epps-Pulley) explicitly.
- **Result:** Modules 11 + 12 now have primary-source-grade backing for the SIGReg derivation. The "average vs max" distinction in particular is one the curriculum was carrying without flagging; it's now explicit. The two source pages are the curriculum's deepest (along with the LeWM paper itself) for the SIGReg argument.

## [2026-05-10] curriculum-module | Module 5 drafted — Generative modeling fundamentals (DDPM, full math)
- Created [Curriculum Module 5 — Generative modeling fundamentals (DDPM, full math)](syntheses/curriculum-05-generative-models.md) — the curriculum's tenth drafted module, closing Tier 2 and the heaviest single piece by design (the "go deep" decision from 2026-05-10 required full ELBO derivation + KL bounds + classifier-free guidance derivation, written rigorously).
- Structure (~31kB; among the longest curriculum modules alongside Module 12):
  1. Curriculum-context callout with explicit "2–4 evenings" effort estimate.
  2. Six learning objectives (write forward/reverse from memory; derive `L_simple` from ELBO; explain why dropping `λ_t` improves samples; derive CFG from Bayes' on score; place DDPM in the generative-models design space; explain why DDPM matters for Modules 7, 9, 10).
  3. **§1 — Generative modeling primer** (AE, VAE, EBM, score matching) — brief but explicit family map; explicit positioning: DDPM is the dominant 2024–2026 paradigm.
  4. **§2 — DDPM forward process** — single-step + chain + the closed-form marginal `q(x_t | x_0) = 𝒩(√ᾱ_t x_0, (1-ᾱ_t)I)` (Eq. 2.1) and the reparameterization `x_t = √ᾱ_t x_0 + √(1-ᾱ_t) ε` (Eq. 2.2).
  5. **§3 — DDPM reverse process** — parameterized denoising; the prior matches the forward chain's limit.
  6. **§4 — Full ELBO derivation** — bound via Jensen (4.1); per-step decomposition via Bayes/telescoping into L_T + L_{t-1} + L_0 (4.3); the forward posterior `q(x_{t-1} | x_t, x_0)` is Gaussian with explicit `μ̃_t` and `β̃_t` (4.4); KL between two Gaussians (closed form); reduction to a Gaussian-regression problem (4.5).
  7. **§5 — From ELBO to `L_simple`** — the ε-reparameterization (5.1, 5.2); substitution that cancels `x_t` terms; the `λ_t`-weighted MSE form (5.3); the simplified loss (5.4); why dropping `λ_t` improves samples despite making the bound loose. Explicit callout: **this is Module 12's anchor exercise Part B**.
  8. **§6 — Noise schedule** — linear (Ho et al.) vs cosine (iDDPM); the cosine schedule formula (6.1) and motivation.
  9. **§7 — Sampling** — ancestral (DDPM) + DDIM (deterministic non-Markovian, decouples training-step count from inference-step count).
  10. **§8 — Classifier-free guidance, full derivation** — Bayes' rule on score (8.2); the implicit-classifier identity (8.3); the guided distribution (8.4); the score-space combination (8.5); translation back to ε-parameterization (8.6); the "drop conditioning with `p_uncond ≈ 0.1` at training" trick.
  11. **§9 — Conditional diffusion in general** — concatenation, cross-attention, AdaLN, time-step + condition embedding addition.
  12. **§10 — Bridges** — to Module 6/7 (Diffusion Policy = conditional DDPM over action chunks, with a mapping table), Module 9 (π0's flow matching as a sibling), Module 10 (generative-video WMs as DDPM at scale), and EBM/IBC (sibling families that finesse explicit-density issues differently).
  13. **Anchor exercise** — Part A: tiny DDPM on MNIST + DDIM sampling. Part B: derive `L_simple` from ELBO on paper, with five specific sub-tasks (Bayes/telescoping; complete-the-square for `q(x_{t-1} | x_t, x_0)`; ε-reparam; KL-of-Gaussians substitution; identify what's dropped going to `L_simple`).
  14. Recommended reading (DDPM → Diffusion Policy §II → iDDPM → DDIM → CFG → Lilian Weng blog as backup).
  15. What you should now be able to do.
  16. Hand-off to Module 7 / 9 / 10 / 12 — names exact downstream consumers of this module's math.
  17. Related modules + Mentioned in + Open questions (iDDPM / DDIM / CFG / score-matching primary-source pages still TBD; flow-matching concept page; DDPM-on-MNIST notebook artifact).
- Updated [Robot-learning curriculum](syntheses/robot-learning-curriculum.md) — Module 5 entry now links the drafted page; module-list heading wraps "Module 5" in a markdown link; coverage table cell updated to "drafted"; status frontmatter notes **Tiers 2–5 complete**, only Tier 1 (Modules 1–4 ML foundations) remains.
- Updated [index.md](index.md) — Highlights bullet for Module 5; Syntheses bullet for Module 5.
- **Reader status:** Ten of fourteen modules drafted. **Tiers 2–5 are complete.** The curriculum is now reader-traversable from Module 5 through the destination (Module 12) and the deployment / capstone modules (13–14), in any order consistent with the module dependency graph. Remaining: Tier 1 (Modules 1–4 ML foundations, greenfield) only.

## [2026-05-10] curriculum-modules | Tier 1 drafted — Modules 1, 2, 3, 4
- Created **[Curriculum Module 1 — Neural networks and training](syntheses/curriculum-01-neural-networks.md)** — brisk-but-rigorous NN refresher: neuron, MLP, forward pass, MSE/CE loss, SGD/AdamW, backprop via chain rule, overfitting + regularization remedies, BN vs LN (with the SIGReg-interaction warning), residual connections + why-depth-helps, practical training recipe. Prereq diagnostic at top so readers can skim if comfortable. Anchor exercise: train an MLP digit classifier on MNIST; probe the second-to-last layer with t-SNE; observe the *embedding* emerging as a side effect of training the classifier (groundwork for Modules 4 + 11 framing of "the embedding is the object").
- Created **[Curriculum Module 2 — CNNs and visual representation learning](syntheses/curriculum-02-cnns.md)** — convolution operation (locality + weight sharing + translation equivariance), stride / padding, pooling (max / avg / GAP / strided-conv), feature maps + receptive fields (incl. the 3×3 stack trick), ResNet + bottleneck blocks, ResNet variants table with ImageNet top-1, ImageNet pretrain → fine-tune workflow, the "visual encoder" abstraction across BC-line / JEPA-line / VLA, when CNN vs ViT, mentions of U-Net (DDPM substrate), ConvNeXt, etc. Anchor: ResNet-18 features on PushT frames; t-SNE visualization.
- Created **[Curriculum Module 3 — Sequence models, attention, and transformers](syntheses/curriculum-03-attention-and-transformers.md)** — RNN/LSTM briefly (for context), scaled dot-product attention (with explicit formula + √d_k justification), self-attention, multi-head attention, transformer block (pre-norm vs post-norm), positional encoding (sinusoidal / learned / RoPE), causal masking (LeWM predictor + GPT + BeT), ViT recipe (patch tokenization, [CLS] token, why-more-data-needed), encoder-only / decoder-only / encoder-decoder taxonomy. Anchor: tiny transformer on PushT 8×8 patches with attention-map visualization.
- Created **[Curriculum Module 4 — Self-supervised learning and embeddings](syntheses/curriculum-04-self-supervised-learning.md)** — the prerequisite for the JEPA chain. SSL precise definition + vs unsupervised + supervised; contrastive (SimCLR / MoCo) vs predictive (BYOL / DINO / MAE / JEPA) families; the latent space as the object; **representation collapse as a first-order failure mode** (with complete-vs-dimensional distinction); the **five anti-collapse families** — EMA + stop-grad (BYOL-line), variance + covariance (VICReg / Barlow Twins), frozen pretrained encoder (DINO-WM-line), multi-fix soup (PLDM-line), distribution-matching (SIGReg / LeJEPA-line) — with side-by-side comparison table. This is the module that makes Module 11's collapse-prevention zoo parseable. Anchor: VICReg on CIFAR-10 with all three terms vs invariance-only; observe collapse in the invariance-only case via per-dimension variance and linear-probe accuracy.
- Updated [Robot-learning curriculum](syntheses/robot-learning-curriculum.md) — Modules 1–4 entries now link the drafted pages; module-list H4 headings wrap "Module N" in markdown links for all four; coverage table cells updated to "drafted"; **frontmatter status changed from "outline" to "complete — all 14 modules drafted 2026-05-10. Reader-traversable bottom-up. Module bodies may be deepened or revised on signal."**
- Updated [index.md](index.md) — four new Highlights bullets + four new Syntheses-chronological bullets; the curriculum-hub Highlights bullet now flags "all 14 modules drafted."
- **Curriculum status: COMPLETE — 14 of 14 modules drafted.** The reader can traverse the entire curriculum bottom-up from absolute beginning (Module 1 NN basics, no prerequisites beyond linear algebra + chain rule) through the destination (Module 12 LeWM deep-dive with full SIGReg math) and the deployment + capstone modules (13, 14). The dependency graph (encoded in the hub) gives readers permission to skip Tier 1 modules they're already comfortable with — each Tier 1 module has a prereq diagnostic at the top for self-assessment.

## [2026-05-11] ingest | Welch Labs — "Yann LeCun's $1B Bet Against LLMs" (YouTube, 2026-05-01)
- Created [Welch Labs — Yann LeCun's $1B Bet Against LLMs (video)](sources/welchlabs-lecun-1b-bet-against-llms.md) — 37-min Welch Labs explainer (Stephen Welch et al.) with LeCun interview clips; arc: deep-learning limits → cake-of-intelligence → generative AI → blurry pixels → why-so-blurry → "do we need to be generative?" → Siamese networks → representation collapse → Barlow Twins → DINO → JEPA & world models → "is JEPA good?". Special thanks credits Yann LeCun, Stephane Deny, David Fan, Nicolas Ballas. Embeds the V-JEPA 2 robot-arm demos. Indirectly corroborates the [Towards AI / AMI Labs reporting](sources/towardsai-lecun-ami-labs.md) — the "$1B bet" framing.
- Updated [Yann LeCun](entities/yann-lecun.md) — added in-text link from the "Latent-prediction over generative-video" and "Self-supervised learning at internet-scale" stances to the video as the on-camera articulation of these positions; added Mentioned-in entry; source count 12 → 13; updated 2026-05-11.
- Updated [Joint-Embedding Predictive Architecture](concepts/jepa.md) — added a `> [!note] Video overview` callout near the top recommending the Welch Labs video as a popular-explainer; added Mentioned-in entry; source count 10 → 11; updated 2026-05-11.
- Updated [Robot-learning curriculum](syntheses/robot-learning-curriculum.md) — added a `> [!note] Video overview — recommended before starting` callout near the beginning (right after the Acronyms note) pointing readers at the video as a non-technical orientation to *why* the curriculum points at JEPA / LeWM at all. Updated 2026-05-11.
- Updated [index.md](index.md) — added Sources-chronological bullet for the new video source; bumped [Yann LeCun](entities/yann-lecun.md) and [JEPA concept](concepts/jepa.md) source counts.

## [2026-05-11] deep-crawl | XLeRobot Documentation — subpage walk (Hardware / Sim / Software / Demos / Related Works)
- Deepened existing [XLeRobot Documentation](sources/xlerobot-docs.md) ingest (originally 2026-05-10). Added a "Deeper crawl — 2026-05-11" section covering: `hardware/hardware_intro`, `hardware/getting_started/{material,3d,assemble}`, `simulation/getting_started/{index,simdemos,vr_sim}`, `software/getting_started/{install,SO101,XLeRobot_teleop,RL,LLM_agent,VLA_ACT,VLA_pi05,VLA_smol,raspberry_pi_setup}`, `demos/`, `relatedworks/`.
- Surfaced new technical detail: PC-does-inference / Pi-relays-WiFi design intent; 12 kg mass; 0.5–1.25 m vertical workspace; 17× STS3215 12 V servos; Anker SOLIX C300 (288 Wh, 10+ hr runtime); BambuLab A1 / PLA print recipe; 8-step assembly with 9-motor expectation; ManiSkill 3.0 scene catalog (ReplicaCAD / AI2-THOR / RoboCasa / OpenCabinetDrawer); custom VRMonitor service over WebSocket-HTTPS for Quest 3; LangChain-style LLM agent on Gemini 3 Flash with RoboCrew tool library and "hey robot" wakeword; three VLA paths (ACT 50-ep, π0.5 via OpenPI fork + `bimanual-toy-box-cleanup` HF dataset, SmolVLA 12-D-padded-to-32-D, 80k steps ≈ 1 h 45 min on A100); RL stack still a placeholder pointing to `lerobot-sim2real` (Stone Tao) + HF HIL-SERL tutorial.
- **Wiki cross-link of note**: XLeRobot's Related Works page explicitly cites **[V-JEPA 2](entities/v-jepa-2.md)** under "Task Planning" — first independent low-cost-robotics platform documented in the wiki to name V-JEPA as a target policy/world-model framework. Added a reciprocal link from [XLeRobot entity](entities/xlerobot.md) → V-JEPA 2.
- Updated [XLeRobot entity](entities/xlerobot.md) — expanded Specs (mass, workspace, power, actuators); rewrote Software section to enumerate the five workflow paths; added V-JEPA 2 to Related; updated 2026-05-11.
- New entities surfaced but **not yet broken out** as their own pages (judgment: parked until a second source surfaces): **HIL-SERL**, **RoboCrew**, **OpenPI**, **STS3215 servo**, **BACH Hand**, **3D-ViTac**, **eFlesh**, **DRAWER**, **CoTracker3**, **RoboTwin 2.0**, **Hunyuan3D-2**, **Bambot**. Listed at the end of the source page so the next ingest can pick them up easily.
- No new source page created (same URL); no index.md bullet change beyond the existing xlerobot-docs entry — same source, more depth.

## [2026-05-11] ingest | Seeed × NVIDIA × Hugging Face Embodied AI Hackathon 2025 Recap
- Created [Seeed × NVIDIA × HF Embodied AI Hackathon 2025 Recap](sources/seeed-embodied-ai-hackathon-2025-recap.md) — November 2025 recap blog (Cloudflare-protected; content extracted via Seeed mirror at `seeed.cc/post/2025-embodied-ai-hackathon-recap` and triangulated against the Hackster.io contest page + winners post). Two-site (Shenzhen + Mountain View) Oct 2025 hackathon; 700+ devs registered; ~30 teams (~15 per site); theme = home + cooking robots. Co-organized by [Seeed Studio](entities/seeed-studio.md) + [NVIDIA](entities/nvidia.md) + [Hugging Face](entities/hugging-face.md). Partners: [K-Scale Labs](entities/k-scale-labs.md), [XLeRobot](entities/xlerobot.md), Lightwheel, Solo Tech, FashionStar, Circuit Launch (venue).
- **Winning projects**: U.S. champion = [SIGRobotics-UIUC](entities/sigrobotics-uiuc.md) matcha-bot ([XLeRobot](entities/xlerobot.md) + [GR00T N1.5](entities/nvidia-groot.md) via NVIDIA Brev on Jetson Thor); U.S. runners-up = Sprinkle Robot (SmolVLA, 170-ep) + Cloth Folding Robot (ACT + learned reward). China champion = Pick&Place w/ High Generalization ([GR00T N1.5](entities/nvidia-groot.md) on 300-episode 90/10 real/sim dataset); China runners-up = Soft Textiles Folding + **Mate XLeRobot** (hardware-modded XLeRobot with vertical lift-rail — first wiki-documented end-user mod of XLeRobot, addresses the fixed-height workspace limitation).
- **Technical signal**: GR00T N1.5 took both site championships on **non-humanoid dual-arm platforms** (XLeRobot, SO-ARM101). First strong external signal that GR00T fine-tunes work at weekend-hackathon data scales (150–300 episodes) outside the humanoid form factor it was designed for.
- Updated entities: [SIGRobotics-UIUC](entities/sigrobotics-uiuc.md) (added matcha-bot championship; 2→3 sources); [XLeRobot](entities/xlerobot.md) (added "In the wild — hackathon traction" section; 1→2 sources); [Seeed Studio](entities/seeed-studio.md) (positioned as co-organizer, not just sponsor; 2→3 sources); [NVIDIA GR00T](entities/nvidia-groot.md) (added N1.5 + Brev + Jetson Thor context; 5→6 sources); [K-Scale Labs](entities/k-scale-labs.md) (mentor role at hackathon — still active weeks before late-2025 shutdown).
- Updated [index.md](index.md) — added Sources-chronological bullet for the new source; bumped source counts and one-line summaries for the four entities above.
- **New entities surfaced but parked**: NVIDIA Jetson Thor + JetPack 7 SDK, NVIDIA Brev, Lightwheel, Solo Tech, FashionStar / StarAI, Circuit Launch, Mate XLeRobot. Listed at the bottom of the source page so a future ingest can pick them up.
- **Open questions logged**: exact October 2025 dates, cash prize amounts (if any), public availability of winning team repos/datasets, and the structural-ecosystem question of why HF + Seeed ran two parallel hackathon brands in 2025 (LeRobot Worldwide June, Embodied AI October).

## [2026-05-11] ingest | SIGRobotics (ACM @ UIUC) — Projects page
- Created [SIGRobotics (ACM @ UIUC) — Projects page](sources/sigrobotics-uiuc-projects-page.md). The site is a React SPA on GitHub Pages — `/projects` returns 404 from the static host but project + sponsor data is hard-coded in the JS bundle (`/static/js/main.e69055b8.js`), which is how the content was extracted. Bundle hash will change on rebuild; documented in the source page's frontmatter.
- **Four flagship projects surfaced**: [LeKiwi](entities/lekiwi.md), 3D-printed Koch arms (no public repo), **Mini Humanoid sponsored by [K-Scale Labs](entities/k-scale-labs.md)** ([micro-sim](https://github.com/SIGRobotics-UIUC/micro-sim)), and a "Turtlebot3 fetches coffee" project sponsored by UIUC CDS.
- **Seven sponsors** named: FrodoBots (big), BitRobot Foundation (big), Saronic (big), Hugging Face LeRobot (normal), Neuralink (normal), ROBOTIS (normal), UIUC CS (normal).
- **Gap-between-website-and-GitHub flagged**: the projects page shows 4 flagships but the GitHub org has ~25 public repos. Surfaced — but not yet broken out to their own pages — the **matcha-bot frontend (`seeed-hack-interface`)** and **`Isaac-GR00T-UIUC`** repos that constitute the Oct 2025 hackathon-win codebase; **F1Tenth autonomous racing**; a **Climbing Robot** project; the **`silent_speech`** EMG/HCI repo (probable Neuralink-sponsorship bridge); the bimanual SO-101 leader/follower repos; and the **FrodoBots Earth Rover Mini SDK** cluster (now explained: FrodoBots is a top-tier sponsor).
- **K-Scale Labs sponsorship of SIGRobotics Mini Humanoid** is the most material new fact — it shows K-Scale was funding *university humanoid-policy work* on top of its hackathon mentorship, all the way into late 2025 before the Series-A failed. The SIGRobotics projects page still lists the sponsorship 5+ months after K-Scale's shutdown (either UIUC hasn't updated or the project continues on prior seed funding — flagged as an open question).
- Updated entities: [SIGRobotics-UIUC](entities/sigrobotics-uiuc.md) (rewrote Projects section to enumerate flagships + GitHub-only projects; new Sponsors section; 3→4 sources); [K-Scale Labs](entities/k-scale-labs.md) (added Mini Humanoid sponsorship; 1→3 sources).
- Updated [index.md](index.md) — added Sources-chronological bullet; refreshed SIGRobotics-UIUC and K-Scale Labs entries with new context + source counts.
- **New entities surfaced but parked**: **FrodoBots / Earth Rover Mini**, **BitRobot Foundation**, **Saronic**, **ROBOTIS / Dynamixel**, **Koch arms (open-hardware lineage)**, **UIUC CDS**. Stub-worthy only if these come up in a second ingest.





## [2026-05-11] ingest | A Path Towards Autonomous Machine Intelligence (LeCun, 2022)
- Created [LeCun 2022 — A Path Towards Autonomous Machine Intelligence](sources/lecun2022-path-towards-ami.md) — long-form deep ingest of LeCun's 62-page position paper. Closes a long-standing wiki gap flagged in three places ([yann-lecun.md](entities/yann-lecun.md) Open questions, [world-model.md](concepts/world-model.md) Open questions, [curriculum-11-jepa-deep.md](syntheses/curriculum-11-jepa-deep.md) references).
- **Why this was a gap, not just a missing reference:** every JEPA / world-model paper in this wiki (V-JEPA 2/2.1, LeWM, DINO-WM, DINO-world, JEPA-WMs, PLDM, LeJEPA, VLA-JEPA) instantiates a piece of *this* document's blueprint. Without the paper, the wiki had implementations without their architectural rationale. The new source page lays out: six-module differentiable agent (perception / world model / actor / cost / short-term memory / configurator); Mode-1 reactive vs Mode-2 deliberative; energy-based-model framing of SSL; the collapse pathology + contrastive-vs-regularized fix taxonomy; JEPA / H-JEPA; intrinsic-cost + learned-critic instead of external reward.
- **AMI Labs gets its missing founding-document link.** Updated [ami-labs.md](entities/ami-labs.md) — the lab's name + mission map directly onto the title + content of the 2022 paper.
- Updated entities: [yann-lecun.md](entities/yann-lecun.md) (13→14 sources; rewrote Public-stance section to add the position paper as canonical reference; removed the "open question" marker; added two new open questions about H-JEPA implementation status and the configurator). Updated concept pages: [jepa.md](concepts/jepa.md) (11→12 sources; canonical-reference link at top + bottom), [world-model.md](concepts/world-model.md) (14→15 sources; cleared open-question entry).
- **Concepts surfaced but not yet filed as their own pages** (worth following up): Energy-based models (EBMs), Hierarchical JEPA (H-JEPA), Configurator, Intrinsic motivation, Mode-1 vs Mode-2. The LeCun source page covers them in-depth; pulling them out to their own concept pages would help cross-link future ingests.
- Updated [index.md](index.md) — added a "Sources (foundational, out of chronological order)" subsection holding both this paper and the DINOv3 paper from the same ingest pass; updated the Yann LeCun People entry from 13→14 sources.

## [2026-05-11] ingest | DINOv3 (Siméoni et al., Meta AI Research, August 2025)
- Created [DINOv3 Paper](sources/dinov3-paper.md) — deep ingest of the 67-page technical report. Covers: data scaling via automatic curation (Vo et al. lineage); 7B-ViT architecture w/ axial RoPE + RoPE-box jittering; constant-schedule 1M-iteration training; **Gram anchoring** (the central methodological contribution); single-teacher multi-student distillation family; high-resolution post-training; text alignment; satellite-imagery cross-domain transfer.
- **Gram anchoring is the headline.** The first clean fix for the long-training dense-feature degradation that has plagued SSL ViTs > 300M params since DINOv2. Regularize the *Gram matrix* (patch-pairwise similarity structure) toward an early-iteration "Gram teacher" — local features are free to drift, only the similarity structure is anchored. Decouples dense-feature consistency from global-feature improvement.
- Created [DINOv3](entities/dinov3.md) — new entity page; positioned as DINOv2's architectural and training-recipe successor; flagged Federico Baldassarre as the bridge author (co-corresponding on DINOv3 + senior author on DINO-world); cross-linked the methodological cousin relationship with LeJEPA / SIGReg (both target SSL stability at scale, different stances).
- Updated [dinov2.md](entities/dinov2.md) — added "Successor: DINOv3" section; 3→4 sources; removed the "DINOv3 if released" open-question marker.
- **Headline numbers (frozen 7B backbone, no fine-tuning):** COCO mAP 66.1 / ADE20k mIoU 63.0 (full) or 55.9 (linear) / Cityscapes mIoU 81.1 / NYUv2 depth RMSE 0.309. Beats DINOv2 by 6+ mIoU on ADE20k linear and weakly-supervised baselines by 13+ mIoU.
- **Robotics implication flagged:** every DINOv2-based world model in this wiki ([DINO-WM](entities/dino-wm.md), [DINO-world](entities/dino-world.md), [JEPA-WMs](entities/jepa-wms.md)) is a candidate for DINOv3-upgrade. No paper in this wiki has yet done this — DINOv3 (Aug 2025) post-dates DINO-WM (Nov 2024) but pre-dates JEPA-WMs (Dec 2025), so JEPA-WMs presumably did not have access to it at submission time. Open question logged.
- Updated [index.md](index.md) — added DINOv3 to the "Sources (foundational, out of chronological order)" subsection and to the Vision-foundation-models entity subsection.

## [2026-05-12] ingest | Three foundational SSL papers (Barlow Twins / VICReg / Barlow 1961)
- Created [Barlow Twins Paper](sources/barlow-twins-paper.md) — Zbontar, Jing, Misra, LeCun, Deny (FAIR + NYU; ICML 2021; arxiv 2103.03230). 13-page deep ingest covering the cross-correlation-identity loss, the Information-Bottleneck derivation, comparison with InfoNCE/BYOL/SimSiam/W-MSE, and the key empirical findings (works with batch 256; benefits from high-D embeddings — the opposite of contrastive). Names itself after Horace Barlow's redundancy-reduction principle.
- Created [VICReg Paper](sources/vicreg-paper.md) — Bardes, Ponce, LeCun (FAIR + Inria + NYU; ICLR 2022; arxiv 2105.04906). 23-page deep ingest covering the three-term loss (variance hinge + covariance decorrelation + invariance MSE), the explicit collapse-mode decomposition (norm vs informational collapse), and the structural property that makes VICReg's two branches **independent** (enabling multi-modal SSL, the property LeCun's AMI paper cites as load-bearing). Connects forward to PLDM, LeJEPA, LeWM as the methodological lineage that goes from VICReg's "5–6 hyperparameters" to SIGReg's "1 hyperparameter."
- Created [Barlow 1961](sources/barlow1961-sensory-messages.md) — Horace Barlow's foundational neuroscience chapter (book *Sensory Communication*, MIT Press, 1961). 18-page ingest of the three hypotheses (password / filter / redundancy-reduction) with full focus on redundancy reduction since that's the only one with continuing influence. **This is the eponymous reference for Barlow Twins** — the wiki had implicit "Barlow's redundancy-reduction principle" mentions in several places with no resolving citation. Now it does.
- **Why these three together.** They establish the **complete historical lineage** for the anti-collapse machinery the wiki has been building up: Barlow 1961 (factorial code) → Barlow Twins 2021 (cross-correlation → I) → VICReg 2022 (variance + covariance + invariance) → [LeCun 2022 AMI](sources/lecun2022-path-towards-ami.md) (endorses VICReg-class regularizers for JEPA) → [PLDM 2025](sources/pldm-paper.md) / [LeJEPA 2025](sources/lejepa-paper.md) / [LeWM 2026](sources/leworldmodel-paper.md). Previously the wiki had only the later links of this chain; now the methodological root is anchored in primary sources.
- Updated entities: [yann-lecun.md](entities/yann-lecun.md) (14→16 sources; added Barlow Twins + VICReg to Mentioned-in); [adrien-bardes.md](entities/adrien-bardes.md) (3→4 sources; rewrote Research-thread section — VICReg is now linked to the primary source instead of described in prose; added VICReg as Mentioned-in).
- Updated concepts: [jepa.md](concepts/jepa.md) (12→14 sources; added Barlow Twins / VICReg / Barlow 1961 to Mentioned-in section).
- Updated existing sources: [lecun2022-path-towards-ami.md](sources/lecun2022-path-towards-ami.md) (VICReg citation now links to source page); [welchlabs-lecun-1b-bet-against-llms.md](sources/welchlabs-lecun-1b-bet-against-llms.md) (Barlow Twins reference now links to primary-source ingest with Barlow 1961 as historical-root link).
- **Concepts surfaced but not yet filed as their own pages** (worth following up): Redundancy reduction / factorial code (the through-line concept that would unify Barlow 1961 → Barlow Twins → VICReg → SIGReg → DINOv3 Gram anchoring); Information Bottleneck (Tishby's framework, the IT-language descendant of Barlow's principle, used in Barlow Twins' theoretical derivation).
- Updated [index.md](index.md) — added all three to the "Sources (foundational, out of chronological order)" subsection; bumped Yann LeCun (14→16) and Adrien Bardes (3→4) source counts on the People entries.
