---
title: "EfficientZero — Mastering Atari Games with Limited Data"
type: source
url: https://arxiv.org/abs/2111.00210
author: Weirui Ye*, Shaohuai Liu*, Thanard Kurutach, Pieter Abbeel, Yang Gao (Tsinghua / UC Berkeley / Shanghai Qi Zhi)
published: 2021-11 (arXiv); NeurIPS 2021
ingested: 2026-07-09
venue: NeurIPS 2021
local_path: raw/2111.00210v2.pdf
sha256: 057c3466e3aabec6d9a7dc6ac597b43caf546d73ea50241263f7113fdc416a69
format: paper PDF (22 pp)
tags: [efficientzero, muzero, mbrl, sample-efficiency, atari-100k, self-supervised, tsinghua, berkeley]
---

# EfficientZero — Mastering Atari Games with Limited Data

## Summary

The **Atari-100K sample-efficiency milestone**: a [MuZero](muzero-paper.md) variant achieving **194.3% mean / 109.0% median human-normalized performance with only 2 hours of real-time gameplay** (100K steps) — the **first super-human Atari result at that budget**, ~500× less data than DQN needed for similar performance. Context for every 100K-benchmark number the wiki tracks (e.g. [EAWM](eawm-paper.md)'s Atari-100K SOTA claims and [DIAMOND](diamond-paper.md)'s 1.46 sit on the benchmark this paper made competitive).

## Key claims

- Three fixes to MuZero in the low-data regime: **self-supervised consistency loss** on the learned dynamics (SimSiam-style temporal consistency), **end-to-end value-prefix prediction** (off-by-a-few reward timing), and **model-based off-policy value correction**.
- 194.3%/109.0% mean/median human-normalized at 100K interactions; ≈DQN@200M frames with 500× less data.
- Explicit framing: low sample complexity as the path to **real-world RL applicability** — the same motivation the robot-side MBRL ingests ([S5WM](s5wm-paper.md), [DayDreamer](daydreamer-paper.md)) pursue with different bottlenecks (wall-clock, hardware).

## Entities mentioned

- [MuZero](muzero-paper.md) lineage (DeepMind); Pieter Abbeel (recurring senior figure, no person page); Tsinghua (also behind [EAWM](eawm-paper.md)).

## Concepts touched

- [World model](../concepts/world-models/world-model.md) — value-equivalent branch, sample-efficiency frontier.

## Open questions

- EfficientZero-v2 (2024, multi-domain) not ingested — the natural refresh if this line gets weight.
