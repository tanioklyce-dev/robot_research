---
title: LeHome Challenge 2026 (ICRA)
type: entity
subtype: event
created: 2026-09-07
updated: 2026-09-11
sources: 3
tags: [event, competition, icra-2026, garment-folding, deformable, bimanual, so-arm101, lerobot, isaac-lab, benchmark]
---

**LeHome Challenge 2026** — *"1st Simulation-Driven Competition on Deformable Object Manipulation"*, an ICRA 2026 (Vienna, 1–5 June) competition on **bimanual garment folding with the LeRobot [SO-ARM101](so-arm101.md)**, in two phases: an online **simulation round** (Feb 1 – Apr 30, 2026; 62 teams) and an on-site **real-world final** for the top eight. Simulator: **[Isaac Lab](nvidia-isaac-lab.md)** 2.3.1 on Isaac Sim 5.1, with [LeRobot](lerobot.md) 0.4.2; assets and organiser demonstrations on the Hugging Face Hub. Sponsor: Lightwheel.

## The task

Four garment types — long-sleeve tops, short-sleeve tops, long pants, shorts — each with a prescribed folding strategy. **Only full success counts**, scored automatically from **garment keypoint distances**: some pairs must fall under a threshold (sleeves meet, halves meet), others must stay apart (the garment is spread, not balled). Garment category is **not** given to the policy at evaluation; competitors must infer it. Hardware, placement, and gripper are fixed by the organisers; the final ran on the organisers' robot, which competitors had never touched ([Larchenko](../sources/larchenko-lehome-part1-rl-for-vlas.md) [08:16–09:18]).

## Protocol (from the [tech report](../sources/larchenko-learning-to-fold-tech-report.md))

- **Sim round**: 20 garments per type — 10 seen (organiser BC data released), 2 unseen-public, 8 unseen-private — each × 10 episodes; binary full-fold success; 30 Hz; three RGB cameras (overhead + two wrists; overhead depth available). 62 teams.
- **Real final**: top 8 sim teams; 5 garments per type (3 seen, 2 unseen); **partial credit** and per-step quality scored by an organisers' jury; **unseen garments carry a 50 % bonus**; maximum **1080**; 20 Hz. Competitors never touch the evaluation robot beforehand.
- Organisers' simulator paper: [LeHome (ICRA 2026)](../sources/lehome-benchmark-paper.md) — **it describes the simulator and a six-task benchmark, not the challenge protocol**; the keypoint checker, seen/unseen split and real-final scoring above remain sourced only through the tech report.

## Leaderboards

| Rank | Simulation round — overall (long top / short top / long pants / shorts) | Real final (of 1080) |
|---|---|---|
| 1 | **ilya ([Larchenko](ilia-larchenko.md)) 79.63 %** (74.5 / 70.0 / 80.5 / 93.5) | sZs **895** |
| 2 | Shubham @ Vorwerk 73.50 % | ilya **865** |
| 3 | Dum-E 73.38 % | Dum-E 762.5 |
| 4 | SCUT-Unlimited 73.13 % | SCUT-Unlimited 635 |
| 5 | GraspYesAI 70.63 % | sisigakgak 570 |
| 6 | sZs 69.63 % | Shubham @ Vorwerk 470 |

Short tops were the hardest type for nearly every team and shorts the easiest. The sim winner's unseen-garment scores were *"only slightly below"* seen ones. Note the reordering between rounds: sZs, 6th in sim, won the real final.

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
- [Learning to Fold — tech report](../sources/larchenko-learning-to-fold-tech-report.md) — protocol, both leaderboards, data scale.
- [LeHome benchmark paper](../sources/lehome-benchmark-paper.md) — the simulator (six deformable classes, Action Graph, LeRobot-family embodiments, sim+real co-training 15% → 50%).
