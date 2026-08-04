---
title: "allenai/vla-evaluation-harness — GitHub repository"
type: source
url: https://github.com/allenai/vla-evaluation-harness
author: Ai2 (Allen Institute for AI)
affiliation: Ai2
published: 2026-07
ingested: 2026-08-03
venue: GitHub
format: code repository / README
license: open source (Ai2)
tags: [vla-evaluation-harness, evaluation, benchmark, libero, libero-pro, lerobot, ai2, infrastructure, reproducibility, primary-source]
---

## Summary

**The infrastructure that makes the wiki's most consequential open question answerable.** Ai2's unified framework to "evaluate any VLA model on any robot simulation benchmark" — models decoupled from benchmarks via Docker containers and standalone model servers, with **47× throughput** via episode sharding and batched GPU inference: **2,000 LIBERO episodes in ~18 minutes on one H100**.

The wiki's evaluation thread has carried "**run a 2026-class model through LIBERO-PRO**" as its most consequential open item since 2026-07-27 — every LIBERO number is provisional until someone does. This harness supports **[LIBERO-Pro](libero-pro-paper.md)** *and* **[MolmoAct2](../entities/molmoact2.md), GR00T N1.7, and [π0.5](../entities/pi-zero-5.md)** (via [LeRobot](../entities/lerobot.md)) in one system. The question is no longer blocked on tooling — only on someone running and publishing it.

## Key claims

- **Models:** official servers for OpenVLA, π0, π0-FAST, GR00T N1.6, OFT, X-VLA, CogACT, RTC, VLANeXt, MolmoBot; **via LeRobot**: π0.5, GR00T N1.7, MolmoAct2, [VLA-JEPA](../entities/vla-jepa.md), SmolVLA, and others; partner ecosystems (dexbotic, starVLA).
- **Benchmarks: 18** — LIBERO, **LIBERO-Pro**, LIBERO-Plus, LIBERO-Mem, SimplerEnv, CALVIN, ManiSkill2, [RoboCasa](../entities/robocasa.md)/365, VLABench, RoboTwin, RLBench, [BEHAVIOR-1K](../entities/behavior-benchmark.md), and more.
- **Leaderboard** aggregating "2,456 models × 18 benchmarks" from 2,087 papers.
- **Reproduction reports:** four LeRobot checkpoints verified at π0.5 **100%**, GR00T N1.7 **99%**, MolmoAct2 **97%**, VLA-JEPA **96%** of their published LIBERO scores — the wiki's first ingested *independent reproduction* of headline VLA numbers, and all four within a few points of the papers.
- Maintained by Ai2; v0.4.0, July 2026.

## Why it matters in this wiki
- **Reproducibility infrastructure had no page here** — the audit's "record N at ingest" discipline had no corresponding *run-it-yourself* tool. Now it does.
- The **reproduction-report numbers quietly validate the LIBERO table** the [audit](../syntheses/platforms/vla-success-rate-audit.md) audited: the published 94–98 scores replicate. (The [LIBERO-PRO](libero-pro-paper.md) critique — that they measure memorization — is untouched by replication.)
- **MolmoAct2 arrives via LeRobot** here too, consistent with the [MolmoAct2 repo ingest](molmoact2-github-repo.md): Ai2's whole stack is LeRobot-native.

## Open questions
- **The README reports no perturbation-specific results** — the harness *supports* LIBERO-Pro but the reproduction reports cover standard LIBERO only. The consequential run remains unpublished, though a June 2026 paper (arXiv 2606.27663, "Direct Action-Head Injection…") appears to report expanded LIBERO-PRO numbers incl. GR00T-N1.6 — **a lead, not yet ingested**.
- Leaderboard scale (2,456 models) implies heavy automation; curation/verification standards not captured at this depth.

## Related sources
- [LIBERO-PRO paper](libero-pro-paper.md) — the benchmark whose adoption this enables.
- [MolmoAct2 GitHub repo](molmoact2-github-repo.md) — the sibling Ai2 release.
- [Success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) · [RoboArena](roboarena-paper.md) — the methodology thread this joins.
