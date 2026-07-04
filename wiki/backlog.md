---
title: Wiki Backlog — deferred lint items & knowledge gaps
type: meta
created: 2026-07-04
updated: 2026-07-04
tags: [backlog, lint, todo, knowledge-gaps]
---

# Wiki Backlog

Deferred maintenance items and knowledge gaps surfaced during lint passes but not yet actioned. Pick these up in a future session. Newest section first. When an item is done, strike it and note the commit/date, or delete it.

## [2026-07-04] Lint pass (post GR00T-version-line ingest)

Clean at time of writing: 0 broken links (7,175 checked), 0 orphan pages, all `sources/` pages linked from index, all catalog counts synced to frontmatter (6 mismatches fixed this session — apptronik-apollo, tonypi, dobb-e, grievous, ollama, pi-zero-6).

### Knowledge gaps — NVIDIA GR00T line (highest value first)
- [ ] **DreamGen entity** (~9 mentions) — the first paper of NVIDIA GEAR's Dream* world-model triplet (**DreamGen → DreamZero → DreamDojo**). [DreamDojo](sources/dreamdojo-paper.md) has a source page; DreamGen is the missing root. Referenced by [GR00T N1.5](sources/groot-n1_5.md) (neural trajectories) and [nvidia-gear](entities/nvidia-gear.md). **Best single gap to fill.**
- [ ] **FLARE concept note** (~5 mentions) — Future LAtent Representation Alignment loss, the auxiliary objective introduced in [GR00T N1.5](sources/groot-n1_5.md) that lets action-less human video contribute to manipulation skill. Listed as "FLARE (implicit WM)" in [GEAR publications](sources/nvidia-gear-publications.md). A JEPA-adjacent auxiliary loss inside a VLA — worth a short concept page cross-linked to [world-model](concepts/world-models/world-model.md) + [VLA-JEPA](sources/vla-jepa-paper.md).
- [ ] **Eagle VLM entity** (~3 body mentions) — NVIDIA's in-house VLM family (Eagle-2 in [GR00T N1](sources/groot-n1-paper.md), Eagle 2.5 in [N1.5](sources/groot-n1_5.md)) before the Cosmos migration. Lower priority — superseded as the GR00T backbone by Cosmos-2B/Cosmos-Reason2-2B from N1.6 on.
- [ ] **YAM arms**, **Galaxea R1 Pro**, **GEAR-SONIC controller** — new embodiments/controller from [GR00T N1.6](sources/groot-n1_6.md) / [N1.7](sources/isaac-gr00t-github.md). Low priority; file only if they recur in a future source.

### Deferred stub-marker cleanups (cosmetic, not counted as lint failures)
- [ ] [Dobb·E](entities/dobb-e.md) is still marked `_stub_` in [index.md](index.md) despite having a full entity page + an ingested paper ([dobb-e-paper](sources/dobb-e-paper.md)) + 4 citing sources. The `_stub_` marker is stale — drop it on next pass.
- [ ] Re-audit `_stub_` markers globally against actual page depth — several may be stale now that counts are synced (candidates: [pi-zero-6](entities/pi-zero-6.md), [ollama](entities/ollama.md)). Not urgent.

### Pre-existing gaps carried forward (not from this session)
- [ ] **`concepts/reinforcement-learning.md` hub page** — the most-overdue concept page; natural RL-side companion to [optimal-control](concepts/robotics/optimal-control.md). Both primary anchors ([Sutton & Barto](sources/sutton-barto-rl-textbook.md), [Kober 2013](sources/kober-rl-robotics-survey-2013.md)) are now filed.
- [ ] **`syntheses/rl/robot-rl-lineage.md`** — Kober 2013 → deep-RL locomotion → RECAP-class VLA fine-tuning; the robotics companion to the existing [atari-rl-lineage](syntheses/rl/atari-rl-lineage.md).
- [ ] **Nicklas Hansen entity** — would anchor the TD-MPC1 → TD-MPC2 lineage ([TD-MPC](sources/td-mpc-paper.md) now filed).
- [ ] **VQ-BeT parameter count** — unpublished in the paper; only layer dims are citable.
