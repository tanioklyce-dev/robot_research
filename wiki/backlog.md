---
title: Wiki Backlog — deferred lint items & knowledge gaps
type: meta
created: 2026-07-04
updated: 2026-07-04
tags: [backlog, lint, todo, knowledge-gaps]
---

# Wiki Backlog

Deferred maintenance items and knowledge gaps surfaced during lint passes but not yet actioned. Pick these up in a future session. Newest section first. When an item is done, strike it and note the commit/date, or delete it.

## [2026-07-04] Agents / edge-inference ingest — follow-ups
- [ ] **Duplicate raw PDF decision**: `raw/xlerobot_cutting_the_cord_2603.09051v1.pdf` is byte-identical to the tracked `raw/2603.09051v1.pdf` (already ingested as [Cutting the Cord](sources/cutting-the-cord-untethered-xlerobot.md)). Left un-added. Either delete the duplicate, or rename-to-replace the cryptic tracked name (then update that page's `local_path`). User call.
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
- [ ] **YAM arms**, **Galaxea R1 Pro**, **GEAR-SONIC controller** — new embodiments/controller from [GR00T N1.6](sources/groot-n1_6.md) / [N1.7](sources/isaac-gr00t-github.md). Low priority; file only if they recur in a future source.

### Deferred stub-marker cleanups (cosmetic, not counted as lint failures)
- [ ] [Dobb·E](entities/dobb-e.md) is still marked `_stub_` in [index.md](index.md) despite having a full entity page + an ingested paper ([dobb-e-paper](sources/dobb-e-paper.md)) + 4 citing sources. The `_stub_` marker is stale — drop it on next pass.
- [ ] Re-audit `_stub_` markers globally against actual page depth — several may be stale now that counts are synced (candidates: [pi-zero-6](entities/pi-zero-6.md), [ollama](entities/ollama.md)). Not urgent.

### Pre-existing gaps carried forward (not from this session)
- [ ] **`concepts/reinforcement-learning.md` hub page** — the most-overdue concept page; natural RL-side companion to [optimal-control](concepts/robotics/optimal-control.md). Both primary anchors ([Sutton & Barto](sources/sutton-barto-rl-textbook.md), [Kober 2013](sources/kober-rl-robotics-survey-2013.md)) are now filed.
- [ ] **`syntheses/rl/robot-rl-lineage.md`** — Kober 2013 → deep-RL locomotion → RECAP-class VLA fine-tuning; the robotics companion to the existing [atari-rl-lineage](syntheses/rl/atari-rl-lineage.md).
- [ ] **Nicklas Hansen entity** — would anchor the TD-MPC1 → TD-MPC2 lineage ([TD-MPC](sources/td-mpc-paper.md) now filed).
- [ ] **VQ-BeT parameter count** — unpublished in the paper; only layer dims are citable.
