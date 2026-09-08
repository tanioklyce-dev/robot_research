---
title: LeHome Challenge 2026 (ICRA)
type: entity
subtype: event
created: 2026-09-07
updated: 2026-09-07
sources: 1
tags: [event, competition, icra-2026, garment-folding, deformable, bimanual, so-arm101, lerobot, isaac-lab, benchmark]
---

**LeHome Challenge 2026** — *"1st Simulation-Driven Competition on Deformable Object Manipulation"*, an ICRA 2026 (Vienna, 1–5 June) competition on **bimanual garment folding with the LeRobot [SO-ARM101](so-arm101.md)**, in two phases: an online **simulation round** (Feb 1 – Apr 30, 2026; 62 teams) and an on-site **real-world final** for the top eight. Simulator: **[Isaac Lab](nvidia-isaac-lab.md)** 2.3.1 on Isaac Sim 5.1, with [LeRobot](lerobot.md) 0.4.2; assets and organiser demonstrations on the Hugging Face Hub. Sponsor: Lightwheel.

## The task

Four garment types — long-sleeve tops, short-sleeve tops, long pants, shorts — each with a prescribed folding strategy. **Only full success counts**, scored automatically from **garment keypoint distances**: some pairs must fall under a threshold (sleeves meet, halves meet), others must stay apart (the garment is spread, not balled). Garment category is **not** given to the policy at evaluation; competitors must infer it. Hardware, placement, and gripper are fixed by the organisers; the final ran on the organisers' robot, which competitors had never touched ([Larchenko](../sources/larchenko-lehome-part1-rl-for-vlas.md) [08:16–09:18]).

## Results in this wiki

| Place | Team | Simulation round | Real final |
|---|---|---|---|
| 1st sim / 2nd real | [Ilia Larchenko](ilia-larchenko.md) | **79.63 %** full-fold (74.5 / 70.0 / 80.5 / 93.5 by garment), +6.1 pts over 2nd | **865 / 1080** |
| 1st real | *(not identified in ingested sources)* | — | 895 / 1080 |

Numbers from the winner's blog post; the official leaderboard is dynamic and not captured.

## Why it matters in this wiki

- **A public, reproducible benchmark on the wiki's own hardware class.** The SO-ARM101 is the arm behind [XLeRobot](xlerobot.md), [LeKiwi](lekiwi.md), and the wiki's home-robot projects; this is the first competition-grade, keypoint-scored task on it, with a released simulator and demonstrations.
- **Deformables.** Folding is contact-rich and the object has no rigid state — the class of task every [BEHAVIOR-1K](behavior-benchmark.md)-style household survey ranks near the top of what people want done.
- **A sim-first, real-final structure** that forces a sim-to-real story from every entrant.

## Related

- [SO-ARM101](so-arm101.md), [LeRobot](lerobot.md), [NVIDIA Isaac Lab](nvidia-isaac-lab.md).
- [BEHAVIOR-1K](behavior-benchmark.md) — the other household-manipulation challenge; same winner.
- [LeRobot Worldwide Hackathon 2025](lerobot-worldwide-hackathon-2025.md) — the community event on the same hardware.

## Mentioned in

- [Larchenko — LeHome deep dive, Part 1](../sources/larchenko-lehome-part1-rl-for-vlas.md)
