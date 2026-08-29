---
title: "DIAMOND — Diffusion for World Modeling: Visual Details Matter in Atari"
type: source
url: https://arxiv.org/abs/2405.12399
author: Eloi Alonso*, Adam Jelley*, Vincent Micheli, Anssi Kanervisto, Amos Storkey, Tim Pearce, François Fleuret (Geneva / Edinburgh / Microsoft Research)
published: 2024-05 (arXiv); NeurIPS 2024 (spotlight)
ingested: 2026-07-09
venue: NeurIPS 2024
local_path: raw/2405.12399v2.pdf
sha256: 842ff972404c74ca4bac9d2f37a6d309506c19eb3f2efa3e0daf75d6abc19707
format: paper PDF (28 pp)
tags: [diamond, diffusion, world-model, mbrl, atari-100k, neural-game-engine, csgo, generative]
---

# DIAMOND — Diffusion for World Modeling: Visual Details Matter in Atari

## Summary

The bridge between the MBRL line and the wiki's video-diffusion coverage: **a diffusion model as the world model** for RL training. Argument: the discrete-latent compression used by transformer world models (IRIS, TWM, STORM) and DreamerV3 **discards visual details that matter for control**; a diffusion world model keeps them. RL agents trained **entirely inside** the diffusion world model reach **1.46 mean human-normalized on Atari 100K — best-in-class for within-world-model training** at the time (vs STORM, DreamerV3, IRIS, TWM, SimPLe). Second act: trained on **87 hours of static CS:GO gameplay**, DIAMOND's world model stands alone as an **interactive neural game engine** for Dust II — a direct ancestor of the playable-world-model wave (Genie-class, [Cosmos](../entities/nvidia-cosmos.md)).

## Key claims

- Diffusion (EDM-style, few denoising steps for real-time rollouts) replaces discrete-latent dynamics; visual fidelity → better policy learning where details are decision-relevant.
- **Atari 100K: 1.46 mean HNS**, new best for agents trained entirely in imagination (cf. [EfficientZero](efficientzero-paper.md)'s 1.94 via decision-time search — different regime).
- **CS:GO neural game engine**: playable Dust II from static gameplay data; code, agents, and playable models released.
- Together with [DFoT/History Guidance](history-guided-video-diffusion-paper.md) (controllable long rollouts) and [Cosmos 3](cosmos-3-technical-report.md) (world-action models), completes the wiki's arc: **video diffusion is simultaneously colonizing MBRL, simulation, and policy learning**.

## Entities mentioned

- Baselines: [Dreamer](../entities/dreamer.md)V3, IRIS, TWM, STORM (transformer-WM wave — no wiki pages), SimPLe.
- François Fleuret / Tim Pearce (Microsoft Research) — no person pages; [NVIDIA Cosmos](../entities/nvidia-cosmos.md) as the industrial-scale descendant of the neural-game-engine idea.

## Concepts touched

- [World model](../concepts/world-models/world-model.md) — the diffusion branch of MBRL.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — the CS:GO engine is an early playable instance.
- [Latent space](../concepts/world-models/latent-space.md) — the counter-argument: *don't* compress away pixels.

## Open questions

- Real-time budget: how few denoising steps before control quality degrades (the S5WM-style wall-clock question, diffusion edition).
- Line from DIAMOND → Genie 2 / GAIA-1 / UniSim (all still uningested — the remaining playable-WM gap).
