---
title: Lightwheel
type: entity
subtype: company
created: 2026-09-14
updated: 2026-09-14
sources: 5
tags: [lightwheel, company, simulation, physical-ai, isaac-lab-arena, robocasa, libero, lehome, benchmark]
---

# Lightwheel

**Lightwheel** (Lightwheel AI) — a *"physical AI infrastructure company"* (NVIDIA's phrase) that co-developed **[Isaac Lab-Arena](isaac-lab-arena.md)** with NVIDIA — the README credits it with *"the evaluation and task layers"* — and publishes the largest task suites on it. It had been a name-only "parked" entity in this wiki since the Seeed hackathon recap (October 2025); the Arena ingest is the first source that says what it does.

## What it has shipped (as stated by NVIDIA / the Arena README)
- **Lightwheel RoboCasa Tasks** — *"138+ open-source tasks, 50 datasets per task, 7+ robots"* in the `LW-BenchHub` repo; **Lightwheel LIBERO Tasks** — adapted [LIBERO](libero.md); together *"250+ tasks"* in the January 2026 announcement ([Arena GitHub](../sources/isaaclab-arena-github.md)). The Lightwheel RoboCasa kitchens (U-shaped farmhouse, G-shaped Scandinavian, L-shaped…) are the backgrounds of Arena's 31-task Kitchen Benchmark, loaded through a `lightwheel-sdk` dependency.
- **RoboFinals** — *"high-fidelity industrial benchmarks"* on Arena, described in the announcement as *"representative of complex real-world environments."*
- The **40× parallel-vs-sequential** figure (0.76 h vs 34.9 h for 10 RoboCasa tasks × 4,096 variations with GR00T N1.5 on 8 GPUs) is Lightwheel's measurement, added to the NVIDIA blog on 2026-02-03.
- Four Lightwheel engineers are named in Arena's `CONTRIBUTORS.md`.

## Elsewhere in the wiki
- Sponsor of the **[LeHome Challenge 2026](lehome-challenge-2026.md)** and co-author institution of the [LeHome simulator paper](../sources/lehome-benchmark-paper.md) (PKU / CASIA / Lightwheel / HKU) — the deformable-object benchmark the wiki's own SO-101 line competed in.
- Partner at the [Seeed × NVIDIA × HF Embodied AI Hackathon 2025](../sources/seeed-embodied-ai-hackathon-2025-recap.md).

> [!note] Thin page
> Everything here is from NVIDIA-authored or NVIDIA-adjacent sources. No Lightwheel primary (site, paper, funding disclosure) has been ingested; headcount, funding, and whether the task suites are sim-to-real validated are unknown.

## Related
- [Isaac Lab-Arena](isaac-lab-arena.md) · [RoboCasa](robocasa.md) · [LIBERO](libero.md) · [NVIDIA Isaac Lab](nvidia-isaac-lab.md)

## Mentioned in
- [Isaac Lab-Arena GitHub](../sources/isaaclab-arena-github.md) — co-developer credit, task suites, RoboFinals, 40× figure.
- [LeHome simulator paper](../sources/lehome-benchmark-paper.md) — co-author institution.
- [Larchenko — LeHome deep dive, Part 1](../sources/larchenko-lehome-part1-rl-for-vlas.md) — challenge sponsor.
- [Seeed Embodied AI Hackathon 2025 recap](../sources/seeed-embodied-ai-hackathon-2025-recap.md) — partner.
