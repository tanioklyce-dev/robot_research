---
title: Wiki Backlog — deferred lint items & knowledge gaps
type: meta
created: 2026-07-04
updated: 2026-07-17
tags: [backlog, lint, todo, knowledge-gaps]
---

# Wiki Backlog

Deferred maintenance items and knowledge gaps surfaced during lint passes but not yet actioned. Pick these up in a future session. Newest section first. When an item is done, strike it and note the commit/date, or delete it.

## [2026-07-17] VLA-0 ingest — lint follow-ups
- [x] ~~**OpenVLA-OFT entity**~~ — **filed 2026-07-17**: [OpenVLA-OFT entity](entities/openvla-oft.md) (grounded in the [VLA-0 paper](sources/vla-0-paper.md); primary arXiv 2502.19645 still un-ingested → noted as an open question on the page). Wired into openvla / vla-0 / libero / vla-models / curriculum-09 + index.
- [x] ~~**π0-FAST / π0.5-KI entities**~~ — **filed 2026-07-17**: [FAST / π0-FAST entity](entities/fast-action-tokenization.md) (DCT tokenization; also the KI token scheme) + [Knowledge Insulation concept](concepts/learning/knowledge-insulation.md) (the home for π0.5-KI; resolves the pi07-paper-flagged KI-page gap). Grounded in ingested pi07/pistar06/VLA-0; primaries 2501.09747 + 2505.23705 still un-ingested.
- [x] ~~**MolmoAct entity**~~ — **filed 2026-07-17**: [MolmoAct entity](entities/molmoact.md) (grounded in VLA-0's LIBERO row; primary 2508.07917 + Molmo backbone un-ingested → noted). **Molmo (Allen Institute open VLM)** still has no entity — new backlog candidate below.
- [x] ~~**Molmo entity**~~ — **filed 2026-07-17**: [Molmo entity](entities/molmo.md) (Ai2 fully-open VLM; pointing capability; [MolmoAct](entities/molmoact.md) backbone). Primary arXiv 2409.17146 + OLMo/OLMoE LLMs still un-ingested → noted on the page.
- [ ] **`## Mentioned in` section missing** on 7 stub entities: [openvla](entities/openvla.md), [octo](entities/octo.md), [paligemma](entities/paligemma.md), [smolvlm](entities/smolvlm.md), [gemma3](entities/gemma3.md), [bagel](entities/bagel.md), [open-x-embodiment](entities/open-x-embodiment.md). Cosmetic; normalize on a stub-cleanup pass.
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
