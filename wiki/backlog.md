---
title: Wiki Backlog — deferred lint items & knowledge gaps
type: meta
created: 2026-07-04
updated: 2026-07-18
tags: [backlog, lint, todo, knowledge-gaps]
---

# Wiki Backlog

Deferred maintenance items and knowledge gaps surfaced during lint passes but not yet actioned. Pick these up in a future session. Newest section first. When an item is done, strike it and note the commit/date, or delete it.

## [2026-07-27] Five-source batch — follow-ups
- [x] ~~**Re-audit the wiki's real-robot success-rate claims against the ~1,030-rollout bar.**~~ — **done 2026-07-27**: [Success-rate audit](syntheses/platforms/vla-success-rate-audit.md). Top of the LIBERO table is one statistical tie (needs >1.8 pp to separate at ~97%; cluster spans 1.6 pp); every structural conclusion survives; MolmoAct2-Think's +0.9 shown unestablished. **Residual work:** (a) **record N at ingest going forward** — the audit was expensive because trial counts were missing from the pages quoting the rates; (b) **two unknown-N comparisons still need their rollout counts** — SmolVLA 78.3 vs π0 61.7, and Cosmos3-Nano vs π0.5 on RoboLab-120; (c) the audit assumes LIBERO = 500 trials/suite — **confirm the actual protocol** from the LIBERO paper (still un-ingested), which would firm up every verdict in section A.
- [ ] **rliable / robomimic / RoboArena still unfiled** — [robot policy evaluation](concepts/robotics/robot-policy-evaluation.md) now exists but rests on one source and covers only the *simulation* half. RoboArena (real-world leaderboard, already referenced from the Cosmos entity) is the obvious next ingest.
- [ ] **Cosmos3-Edge-Policy-DROID has no published benchmark score.** The wiki has the 16B Nano at 39.7% vs π0.5's 28.1% on RoboLab-120; the 4B Edge policy's number is unpublished, so the 16B→4B quality drop is unpriced. Watch for it — it decides whether the 15 Hz edge rate is worth having.
- [ ] **Is Cosmos 3 Edge's 15 Hz end-to-end?** Camera→action (like the [Cutting the Cord](sources/cutting-the-cord-untethered-xlerobot.md) numbers it sits beside on the [control-rate ladder](syntheses/platforms/control-rate-ladder.md)) or model-forward only? Also unstated: power draw at that rate, T2000/T3000 numbers, and the **Edge license** (Nano/Super are OpenMDW-1.1).
- [ ] **microGPT line count** — 243 per Karpathy's announcement, ~200 per one reading of his blog post. Resolvable in one minute by reading the [gist](https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95) directly; not done during ingest.
- [ ] **Who is Mitchell A. Carroll / what is arcnem.ai?** No affiliation on the [deck](sources/arcnem-strange-loops-ai-agents.md), no other source from either in the wiki. If the strange-loop thread continues, verify before leaning on it.
- [ ] **Hofstadter primaries un-ingested** — *GEB* and *I Am a Strange Loop*. Both wiki sources invoking him are secondary. Also unsourced here: **Hofstadter's own skepticism about LLMs**, which is directly relevant to sources borrowing his metaphor to argue LLMs are strange loops.
- [ ] **Model collapse / synthetic-data recursion has no page** — the [strange-loops concept](concepts/agents/strange-loops-and-self-reference.md) names the robotics instance (DreamGen/DreamDojo neural trajectories, MimicGen, 827 h in GR00T N1's data pyramid) and asks whether it is a productive or compounding-error loop. The wiki has no source that answers it.
- [ ] **GNW / IIT / predictive processing** are named once each (via Masood) and nowhere else. Only worth pages if consciousness/cog-sci sources keep arriving.
- [ ] **NPE (Neural Posterior Estimation) is a one-mention technique** — first simulation-based-inference sighting in the wiki. If it recurs in evaluation work, it deserves a concept page.

## [2026-07-27] Anthropic Frontier Red Team robotics arc — follow-ups
*(Three sources ingested this day: [Project Fetch](sources/anthropic-project-fetch-robot-dog.md), [Phase Two](sources/anthropic-project-fetch-phase-two.md), [How Claude Performs on Robotics Tasks](sources/anthropic-how-claude-performs-on-robotics-tasks.md).)*

- [x] ~~**Ingest *How Claude Performs on Robotics Tasks***~~ — **done 2026-07-27**, and it turned up a third page ([Phase Two](sources/anthropic-project-fetch-phase-two.md)) that was also ingested. The arc is complete.
- [x] ~~**Confirm the Project Fetch robot**~~ — **resolved 2026-07-27**: the eval names it, *"a real Unitree Go2 (the quadruped robot of Project Fetch)"*. Caveat retired on [Unitree Go2](entities/unitree-go2.md).
- [x] ~~**Uplift measurement is a one-source concept**~~ — partially: [AI uplift studies](concepts/safety/ai-uplift.md) now has 3 sources including the autonomy re-run. **Still open:** no *non-Anthropic* uplift study. The biological-risk originals are referenced but un-ingested; METR-style developer-productivity RCTs would be the obvious outside anchor and would test whether the control-arm-habituation problem generalizes.
- [ ] **Frontier Red Team people pages** — five bylined authors across the arc, none filed: **Michael Ilie** and **C. Daniel Freeman** (both on two of three papers — the connective authors), **Kevin K. Troy**, **Shmuel Berman**, **Jia Deng**. If Deng is the Princeton/ImageNet Jia Deng that's worth confirming and noting, but the sources don't say.
- [ ] **Is `github.com/safety-research/embody` actually released?** The eval gives the URL as "once released." An ingest of the harness would ground the four-level taxonomy in runnable code and is the single highest-value follow-up here — it would make [control abstraction levels](concepts/robotics/control-abstraction-levels.md) reproducible rather than descriptive.
- [x] ~~**Put the 83 Hz figure on one axis with the wiki's edge-latency numbers.**~~ — **done 2026-07-27**: [The control-rate ladder](syntheses/platforms/control-rate-ladder.md). ~30 rows, four bands, REQ/MEAS/CAP tagging. Main result: the 83 Hz figure names a band *nothing in the wiki deploys into*, so the tracking comparison is LLM (0.2–0.4 Hz) vs the **VLA planner tier** (1.4–27.8 Hz). **Residual gaps recorded on the page** — (a) no 2026-class VLA has an on-Jetson number ([MolmoAct2](entities/molmoact2.md) is H100-only; **the highest-value missing measurement in this area**), (b) no published chunk-adjusted *effective control rates*, so inference-Hz vs control-Hz stays qualitative, (c) **no ingested source measures a small local LLM in a control loop** — the 1 Hz agent figures are status heartbeats, (d) power is an unmodelled third axis.
- [ ] **Why does VLA supervision hurt in-distribution?** The eval establishes that every tested model scores below [MolmoAct](entities/molmoact.md)-alone on tasks it already handles, and that better models hurt less — but not what the overrides get *wrong*. This is the crux for the whole [LLM-agent robot](concepts/agents/llm-agent-architecture.md) thread. Watch for a follow-up that decomposes it.
- [ ] **Unitree Robotics company entity** — the wiki has [G1](entities/unitree-g1.md), [H1](entities/unitree-h1.md), and [Go2](entities/unitree-go2.md) but **no parent-company page**, and all three link to bare-text "Unitree Robotics". Not filed because no ingested source carries citable company facts (founding, Wang Xingxing, Hangzhou, funding, IPO).
- [ ] **Claude 4 System Card p. 114** — the prior "Claude trains a quadruped locomotion policy in sim, not yet autonomously capable" evaluation is cited by Project Fetch but un-ingested. Would be the wiki's first system-card ingest and the actual baseline the whole arc is measured against.
- [ ] **Quadruped tier is still the thinnest-sourced platform group.** [Go2](entities/unitree-go2.md) is now well-instrumented *as an evaluation target* but has **no primary technical source** (no datasheet, no SDK docs), same for [Spot](entities/spot.md), and **no ingested research paper uses a quadruped** — while quadruped locomotion RL is a major subfield. Flagged on the [robot platforms comparison](syntheses/platforms/robot-platforms-comparison.md).
- [ ] **No wiki page for any model named in the eval** — Claude Opus 4.5/4.6/4.7, Claude Mythos Preview, GPT-5.1/5.4, Gemini 3.1 Pro Preview, Kimi K2.6, Qwen 3.6+. Recorded as the source states them. Probably fine (the wiki isn't an LLM tracker), but the *Mythos Preview* profile is genuinely anomalous — only model where reasoning budget mattered, best novel-task supervisor, worst in-distribution supervisor — and would be worth a page if it recurs.

## [2026-07-18] VLA-cluster session — wrap-up notes (where things stand)
Session arc: ingested 3 raw drops (VLA-0, YOLOv11n child-detection, USC table-tennis MARL) → filed the VLA-baseline cluster VLA-0 pointed at (OpenVLA-OFT, FAST/π0-FAST, MolmoAct, Molmo + concepts: Knowledge Insulation, multi-agent-rl, SAHI) → then paid down the "primary un-ingested" debt by ingesting **4 VLA primaries**: VLA-0 (2510.13054), Knowledge Insulation (2505.23705), OpenVLA-OFT (2502.19645), FAST (2501.09747). The VLA action-representation design space is now anchored on those four ingested primaries.
- [ ] **Remaining un-ingested VLA primaries (secondary-grounded satellites):** **MolmoAct** (2508.07917) + **Molmo** (2409.17146, Ai2) — the Allen-Institute lineage, distinct from the Physical-Intelligence one. Plus **OLMo / OLMoE** (Molmo's LLM backbones) have no entity. Lower priority than the PI cluster; ingest if that lineage recurs.
- [ ] **Author page — Moo Jin Kim** (OpenVLA + OpenVLA-OFT first author); flagged on [openvla.md](entities/openvla.md). Karl Pertsch / Levine / Finn already filed.

## [2026-07-17] VLA-0 ingest — lint follow-ups
- [x] ~~**OpenVLA-OFT entity**~~ — filed 2026-07-17; **primary ingested 2026-07-18** ([openvla-oft-paper](sources/openvla-oft-paper.md), arXiv 2502.19645): parallel decoding + action chunking + continuous L1 head; 76.5→97.1 LIBERO at 26× throughput. Entity now primary-grounded + de-stubbed.
- [x] ~~**π0-FAST / π0.5-KI entities**~~ — filed 2026-07-17; **both primaries ingested**: [FAST paper](sources/fast-paper.md) (2501.09747, 2026-07-18; acronym corrected to *Frequency-space Action Sequence Tokenization*) + [Knowledge Insulation paper](sources/knowledge-insulation-paper.md) (2505.23705, 2026-07-17). Both concept/entity pages now primary-grounded.
- [x] ~~**MolmoAct entity**~~ — **filed 2026-07-17**: [MolmoAct entity](entities/molmoact.md) (grounded in VLA-0's LIBERO row; **primary 2508.07917 still un-ingested** → see wrap-up above).
- [x] ~~**Molmo entity**~~ — **filed 2026-07-17**: [Molmo entity](entities/molmo.md) (Ai2 fully-open VLM; pointing capability; [MolmoAct](entities/molmoact.md) backbone). **Primary arXiv 2409.17146 + OLMo/OLMoE LLMs still un-ingested** → see wrap-up above.
- [ ] **`## Mentioned in` section missing** on 6 stub entities: [octo](entities/octo.md), [paligemma](entities/paligemma.md), [smolvlm](entities/smolvlm.md), [gemma3](entities/gemma3.md), [bagel](entities/bagel.md), [open-x-embodiment](entities/open-x-embodiment.md). (openvla fixed 2026-07-18 during FAST ingest.) Cosmetic; normalize on a stub-cleanup pass.
- [ ] **13 pre-existing index/frontmatter source-count mismatches** (2026-07-17 lint): mostly off-by-one — `lerobot` 19/20, `nvidia-cosmos` 15/16, `google-deepmind` 8/9, `jetson-orin-nano` 11/12, `nvidia-halos` 3/4, `nvidia-brev` 2/3, `ros2` 4/5, `robot-safety-standards` 2/3, `ai-red-teaming` 4/5, `large-behavior-models` 4/5, `world-model` 29/30; plus two larger needing ground-truth recount before syncing: **`latent-space` 18/22**, **`whole-body-control` 3/5**. (The 4 self-introduced this session were fixed in-commit.)

## [2026-07-16] NVIDIA batch (Jetson skills / DeepStream / RoboLab / Halos blog) — follow-ups
- [ ] **TensorRT entity** — referenced as bare text from [DeepStream](entities/nvidia-deepstream.md), JetPack, and several Jetson pages; no entity page. File if it keeps recurring.
- [ ] **NVIDIA SRL (Seattle Robotics Lab) entity** — [RoboLab](entities/nvidia-robolab.md) is filed but its parent lab (Dieter Fox / Birchfield / Ramos / Tremblay group) isn't; would anchor DROID + a lot of NVIDIA robot-eval work. The `/labs/srl/` attribution is inferred from the URL path — confirm the lab's official name before filing.
- [ ] **RoboArena** — the *real-world* leaderboard cited alongside RoboLab in the [Cosmos entity](entities/nvidia-cosmos.md); no page. Pairs with the evaluation-methodology gap (rliable / robomimic).
- [ ] **DeepStream vs Isaac ROS** perception-boundary synthesis — if both keep recurring (video-analytics/IVA vs robot-perception/VSLAM).
- [ ] **Halos deploy-skill name reconciliation** — `hoisa-deploy-profile` (Trust Center) vs `warehouse-deploy` / `halos-deploy` (blog); confirm on next Halos update.

## [2026-07-16] Agile / Techman / EngineAI ingest — follow-ups
- [ ] **NavBot store** — deliberately not filed as a source (user call, thin page). If it recurs, a source page could anchor the **[NavBot-D1 quadruped ($4,999)](https://navbot.com/collections/complete-robots)**, EN01 wheel-legged kit, OpenDuck Mini RL kit — open-source-robotics-store tier alongside Elephant/Hiwonder. Reviewed 2026-07-16.
- [ ] **Universal Robots entity** — referenced from the new [cobots concept](concepts/robotics/collaborative-robots.md) as the market leader (~50% share) but has no entity page. File if cobots recur.
- [ ] **EngineAI SA01 / SE01 / PM01** — company + [T800](entities/engineai-t800.md) filed; the cheaper/earlier models (incl. the world-first-front-flip **PM01**, <$15k) are only mentioned in prose. Break out if referenced.
- [ ] **Agile Robots "Thor Series"** — Agile Robots markets a product line called "Thor" (its own naming). Confirm it's unrelated to [NVIDIA Jetson Thor](entities/jetson-thor.md) (assumed collision).
- [ ] **Autonomy of URKL combat robots** — unresolved whether T800 fighters run learned policies, scripted move-sets, or teleop. Watch for a technical source that settles it (decides whether combat leagues are a real autonomy benchmark).

## [2026-07-04] Fleet-framework build pieces (from the fleet synthesis)
Surfaced by [Fleet agentic control framework](syntheses/projects/fleet-agentic-framework.md) — genuine wiki gaps that are also the project's DIY work:
- [x] ~~**ROS 2 ↔ MCP server**~~ — **built + published + ingested 2026-07-04**: [design doc](syntheses/projects/ros2-mcp-server-design.md), the [`ros2-mcp-server`](https://github.com/tanioklyce-dev/ros2-mcp-server) repo (MIT), and the round-trip [source page](sources/ros2-mcp-server-github.md) + [entity](entities/ros2-mcp-server.md). Remaining (in the *repo*, not the wiki): wire the `ros_bridge` ROS 2 calls + SSE transport; re-ingest to deepen the source page as the repo matures.
- [ ] **A2A for multi-robot robotics** — the wiki names the [A2A protocol](concepts/agents/llm-agent-architecture.md) but has **no robotics instance**; watch for the first real one.
- [ ] **HIL-SERL** has no dedicated concept/source page (only referenced via LeRobot); would anchor the "minimal-human continual-improvement" flywheel.
- [~] ~~**Cross-embodiment policy transfer at hobby scale** — SO-ARM101 ↔ HX-12H~~ — **being designed out** (2026-07-04): the fleet owner is swapping the ROSOrin Pro's HX-12H for an [SO-ARM101](entities/so-arm101.md), homogenizing all three robots to one arm → one shared policy, no transfer problem. See the [fleet framework arm-swap decision](syntheses/projects/fleet-agentic-framework.md). (The measurement question only matters if someone keeps a mixed-arm fleet.)

## [2026-07-04] New gaps from the SONIC / Gemini-1.5 / YAM batch
- [ ] **Vision-language navigation (VLN)** — flagged by the [Awesome-Embodied-Robotics list](sources/awesome-embodied-robotics-agent.md) as a genuine wiki gap (ALFRED / R2R / VLN-CE); no concept or source yet.
- [ ] **Household simulators** beyond the [Habitat](entities/habitat.md) stub — AI2-THOR, iGibson (same list).
- [x] ~~**BEHAVIOR / BEHAVIOR-1K + OmniGibson**~~ — **fully ingested 2026-07-04**: [BEHAVIOR-1K paper](sources/behavior-1k-paper.md) + [BEHAVIOR entity](entities/behavior-benchmark.md) + [OmniGibson entity](entities/omnigibson.md) + dedicated [OmniGibson codebase ingest](sources/omnigibson-github.md) (Isaac Sim 4.1.0, 14-robot roster, install). Residual: **iGibson** predecessor lineage + **AI2-THOR / Habitat** peer sims still un-ingested; exact OmniGibson VRAM/disk minimums (inherited from Isaac Sim 4.1.0) unconfirmed.
- [ ] **Nemotron entity** (carried) — now also referenced from the SONIC-adjacent NVIDIA stack.

## [2026-07-04] Agents / edge-inference ingest — follow-ups
- [x] ~~**Duplicate raw PDF decision**~~ — resolved 2026-07-04: the re-dropped `xlerobot_cutting_the_cord_2603.09051v1.pdf` was byte-identical to the tracked `raw/2603.09051v1.pdf`; deleted the duplicate (paper already fully ingested as [Cutting the Cord](sources/cutting-the-cord-untethered-xlerobot.md)). If the descriptive filename is preferred, `git mv` the tracked file + update its `local_path` — not done (cosmetic).
- [ ] **Gemma 4 primary source** — [entity](entities/gemma4.md) built from the NVIDIA edge blog only; Google's Gemma 4 model card/report not ingested (variant params confirmed via the blog). Deepen when filed.
- [ ] **Nemotron entity** — `nvidia/nemotron-3-super-120b-a12b` (120B-MoE / 12B-active) is now referenced by [NemoClaw](entities/nemoclaw.md) + [Hermes quickstart](sources/nvidia-nemoclaw-hermes-quickstart.md) but has no entity page; file if it recurs.

## [2026-07-04] Concept-subdir count audit (NEW — found during DreamGen/FLARE/Eagle ingest)
- [ ] **Re-lint concept catalog counts for pages in subdirectories.** The [2026-07-04] lint's mismatch checker used regex `(?:entities|concepts)/([a-z0-9-]+\.md)` which does **not** match `concepts/<subdir>/<page>.md` (world-models/, learning/, robotics/, …), so all subdirectory concept counts went unverified. Use a corrected regex like `(?:entities|concepts)(?:/[a-z0-9-]+)+\.md`. **10 known stale index counts** (index vs frontmatter, found 2026-07-04; verify ground truth before syncing — frontmatter itself may be over/undercounted, per the entity lesson last session): `scaling-laws-vla` 2/4, `energy-based-models` 4/5, `latent-space` 10/14, `siamese-network` 5/8, `llm-agent-architecture` 8/18, `ai-safety-alignment` 3/6, `assistive-robotics` 16/22, `agentic-uavs` 4/5, `biomechanical-simulation` 5/7, `connectome` 3/4. (jepa/world-model/world-model-simulators already fixed; nvidia-gear + joel-jang were this-session-introduced and fixed immediately.)

## [2026-07-04] Lint pass (post GR00T-version-line ingest)

Clean at time of writing: 0 broken links (7,175 checked), 0 orphan pages, all `sources/` pages linked from index, all catalog counts synced to frontmatter (6 mismatches fixed this session — apptronik-apollo, tonypi, dobb-e, grievous, ollama, pi-zero-6).

### Knowledge gaps — NVIDIA GR00T line (highest value first)
- [x] ~~**DreamGen entity**~~ — filed 2026-07-04: [DreamGen entity](entities/dreamgen.md) + [DreamGen paper](sources/dreamgen-paper.md).
- [x] ~~**FLARE concept note**~~ — filed 2026-07-04: [FLARE concept](concepts/world-models/flare.md) + [FLARE paper](sources/flare-paper.md).
- [x] ~~**Eagle VLM entity**~~ — filed 2026-07-04: [Eagle entity](entities/eagle-vlm.md) + [Eagle-1](sources/eagle-paper.md) + [Eagle 2.5](sources/eagle-2-5-paper.md) papers.
- [ ] **Eagle 2** — the exact GR00T N1 production backbone has no standalone paper on file (only Eagle-1 research study + Eagle 2.5). Low priority.
- [ ] **DreamZero** — the middle Dream\* entry (DreamGen → **DreamZero** → DreamDojo) still has no source page.
- [x] ~~**YAM arms**, **Galaxea R1 Pro**, **GEAR-SONIC controller**~~ — all filed 2026-07-04: [YAM](entities/yam.md), [Galaxea R1](entities/galaxea-r1.md), [GEAR-SONIC](entities/gear-sonic.md) ([SONIC paper](sources/sonic-paper.md)).

### Deferred stub-marker cleanups (cosmetic, not counted as lint failures)
- [ ] [Dobb·E](entities/dobb-e.md) is still marked `_stub_` in [index.md](index.md) despite having a full entity page + an ingested paper ([dobb-e-paper](sources/dobb-e-paper.md)) + 4 citing sources. The `_stub_` marker is stale — drop it on next pass.
- [ ] Re-audit `_stub_` markers globally against actual page depth — several may be stale now that counts are synced (candidates: [pi-zero-6](entities/pi-zero-6.md), [ollama](entities/ollama.md)). Not urgent.

### Pre-existing gaps carried forward (not from this session)
- [ ] **`concepts/reinforcement-learning.md` hub page** — the most-overdue concept page; natural RL-side companion to [optimal-control](concepts/robotics/optimal-control.md). Both primary anchors ([Sutton & Barto](sources/sutton-barto-rl-textbook.md), [Kober 2013](sources/kober-rl-robotics-survey-2013.md)) are now filed.
- [ ] **`syntheses/rl/robot-rl-lineage.md`** — Kober 2013 → deep-RL locomotion → RECAP-class VLA fine-tuning; the robotics companion to the existing [atari-rl-lineage](syntheses/rl/atari-rl-lineage.md).
- [ ] **Nicklas Hansen entity** — would anchor the TD-MPC1 → TD-MPC2 lineage ([TD-MPC](sources/td-mpc-paper.md) now filed).
- [ ] **VQ-BeT parameter count** — unpublished in the paper; only layer dims are citable.
