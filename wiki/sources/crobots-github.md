---
title: "CRobots (troglobit/crobots) — GitHub"
type: source
url: https://github.com/troglobit/crobots
author: Tom Poindexter (original, 1985); Joachim Wiberg / "troglobit" (current maintainer)
published: 1985
ingested: 2026-05-31
format: github
license: GPL-2.0
tags: [programming-game, autonomous-agents, virtual-machine, c, core-war-lineage, retro, agent-based, code]
---

## Summary

**CROBOTS** ("see-robots") is a classic **programming game**: you write a **C-language program** that controls an autonomous battle robot, compile it, and then **up to four robots run unattended** in a virtual arena, scanning for and firing on each other — *all strategy is coded beforehand, with no real-time human input*. Created by **Tom Poindexter in 1985** (DOS shareware), it was relicensed **GPL-2.0** in 2013 and is maintained today by **Joachim Wiberg ("troglobit")** as a cross-platform continuation. It belongs to the **"program-an-autonomous-agent" game** genre (cousin to [Core War](../entities/core-war.md)), which is why it sits adjacent to — but is distinct from — the wiki's artificial-life and autonomous-agent threads.

## Key claims / facts

- **Gameplay.** Players write robot control programs in a **limited subset of C**; the program uses **hardware functions** to scan for opponents, drive, and fire cannons/missiles. Compiled robots run independently in a virtual computer; a text battlefield display (mono or color) shows movement, missile trajectories, and results.
- **Constraints.** Faithful to the original's design, including a **MAX 1000 CPU-instructions-per-cycle limit** — the resource budget that shapes viable strategies (an explicit nod to preserving Poindexter's original balance).
- **Architecture.** Ships a **C compiler + a virtual machine (virtual computer) + battlefield renderer** — i.e. it's also a small compiler/VM artifact, not just a game.
- **History & licensing.** Original 1985 DOS shareware (Tom Poindexter) → first Linux port by Pablo Algar (2018) → **GPL-2.0 since 2013-10-23**; the troglobit repo is "the logical continuation of Tom's project." Runs on Linux, FreeBSD, DragonflyBSD, macOS, OmniOS.
- **Audience.** Programmers, C learners, and people interested in compiler/VM design.

## Why this is in the wiki (and what it is *not*)
- **Programming-game / autonomous-agent lineage.** CRobots is a canonical example of **"write code, then watch it act autonomously"** — the deterministic, pre-programmed ancestor of today's agent arenas and multi-agent battle environments. It connects culturally to the wiki's [artificial-life branch](../concepts/alife/artificial-life-and-self-replication.md) via the [Core War](../entities/core-war.md) programming-game family (Core War's Redcode warriors are the self-replication-relevant sibling; CRobots itself does **not** self-replicate).
- **Not a learning system.** CRobots robots are **hand-coded and static** — no learning, no evolution, no self-modification. It is therefore a contrast/baseline to the wiki's [RL](../syntheses/curriculum/curriculum-08-rl-vocabulary.md), [evolutionary computation](../concepts/alife/evolutionary-computation.md), and self-modifying-soup ([cubff](cubff-github.md)) approaches, not an instance of them.

## Concepts touched
- [Artificial life and the emergence of self-replication](../concepts/alife/artificial-life-and-self-replication.md) — programming-game cultural lineage (Core War family); see the "Programming games" note there.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — historical contrast: hand-coded autonomous agents vs. LLM-driven ones.

## Open questions
- The user grouped CRobots with the Xenobots self-replication links — the likely throughline is **"autonomous agents / self-acting programs,"** but CRobots has **no replication or emergence** of its own. The *self-replicating* programming-game cousin, [Core War](../entities/core-war.md), has since been ingested ([Dewdney 1984](dewdney-1984-core-war-scientific-american.md)).
