---
title: XPolicyLab
type: entity
subtype: software
created: 2026-11-07
updated: 2026-11-07
sources: 3
tags: [xpolicylab, policy-serving, evaluation-infrastructure, robodojo, robotwin, rmbench, leaderboard, vla, world-action-model, lerobot, coding-agents, apache-2]
---

# XPolicyLab

**XPolicyLab** is an Apache-2.0 repository of robot-policy **adapters** and a websocket **policy server**, led by Tianxing Chen (MMLab@HKU and THU). It is the shared layer behind the [RoboDojo](robodojo.md) and [RoboTwin](robotwin.md) leaderboards: one adapter per policy, one client per environment ([XPolicyLab GitHub](../sources/xpolicylab-github.md)). Paper: arXiv 2608.09892 (not ingested). It won Best Tool Paper at the IROS 2026 scalable-infrastructure workshop.

## What it is
- **Environment isolation.** Each model keeps its own conda or uv environment, dependencies and checkpoints under `policy/<POLICY>/`. The simulator or robot client runs separately and talks to it over websocket with msgpack, locally or across machines.
- **One contract.** `Model.update_obs` / `get_action` (action chunks), batched variants and `reset()`. Ten standard positional arguments flow through install, conversion, training and eval, and there is a `debug` mode that checks shapes and IO without a simulator.
- **Standard formats.** Nested observation and trajectory dicts, quaternion-first poses, and official LeRobot v2.1/v3.0 converters that zero-pad mixed embodiments into one dataset.
- **Scale.** **77 policies** as of November 2026, up from 30 in the RoboDojo paper (July) and "40+" in RoboDojo's branch README. At least ten are world-action models, and one is a frontier LLM (GPT-6 Astra) driving the arm through a single end-effector tool.
- **Gatekeeping.** A PR here, with a checkpoint download script, is required to enter either official leaderboard. That is how RoboDojo enforces its rule that the verified board must release checkpoints ([RoboDojo paper](../sources/robodojo-paper.md)).

## Engineering lessons it writes down
- **The codec is the boundary.** Legacy JPEGs written from RGB arrays are channel-reversed, and new ones carry an `XPL-RGB1` marker. Both coexist in the same runs, and only `decode_image_bit` can tell them apart, so any hand-written color swap is a bug. The rule landed in three commits from August to September 2026 and matches the joint RoboDojo/RoboTwin RGB fix ([branch READMEs](../sources/robodojo-isaaclabarena-branch.md)).
- **Idempotent retries.** Requests carry IDs, and duplicates are answered from a cache. Timeouts and server restarts are fatal for the trial rather than silently retried.
- **Two robot-info files** (runtime vs `train.sh`) must agree, or training and evaluation disagree about action dimensions.
- **No pickle on the wire.** Object-dtype arrays are refused. There is **no authentication or TLS** either, so a split-machine deployment that binds `0.0.0.0` is open to anyone on the network (my own read of the transport code).

## Coding agents as contributors
The repo ships two skills in `.agents/skills/`, symlinked for Claude Code, Codex and Cursor:
- `xpolicylab-model-integration` builds an adapter from a one-line prompt.
- `xpolicylab-adapter-check` runs a nine-point pre-PR audit.

`AGENTS.md` is the always-on rule set, and `CLAUDE.md` simply imports it. It is a concrete case of a benchmark's integration standard written primarily for agents to follow ([XPolicyLab GitHub](../sources/xpolicylab-github.md)).

## Why it matters for this wiki
- **It decides what RoboDojo's numbers mean.** The 8.8%-best RoboDojo result is measured through these adapters. Until per-adapter parity with each model's home benchmark is shown, a low score is partly a statement about the adapter.
- **It is the broadest single harness the wiki has seen,** with VLAs, WAMs, imitation baselines and an LLM-with-planner all behind one interface. That makes it the natural place to run cross-family comparisons such as WAMs against VLAs.
- **For a home lab:** it is a ready-made split-machine serving layer (GPU box for the policy, robot PC for the client) with Piper and Franka already registered. Add authentication before using it on anything but a private link.

## Related
- [RoboDojo](robodojo.md) · [RoboTwin](robotwin.md) · [LeRobot](lerobot.md)
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) · [World-action model](../concepts/world-models/world-action-model.md) · [Agent skills](../concepts/agents/agent-skills.md)

## Mentioned in
- [XPolicyLab GitHub](../sources/xpolicylab-github.md) — the primary: architecture, transport, data contracts, 77-policy list, contribution rules and agent skills.
- [RoboDojo paper](../sources/robodojo-paper.md) — 30 integrated policies as of 2026-07-03; checkpoint release through XPolicyLab.
- [RoboDojo — RoboDojo-IsaacLabArena branch](../sources/robodojo-isaaclabarena-branch.md) — *"40+ policies behind one interface."*
