---
title: "MuZero — Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model"
type: source
url: https://arxiv.org/abs/1911.08265
author: Julian Schrittwieser*, Ioannis Antonoglou*, Thomas Hubert*, ..., Demis Hassabis, Thore Graepel, Timothy Lillicrap, David Silver* (DeepMind/UCL)
published: 2019-11 (arXiv); Nature 588, 2020
ingested: 2026-07-09
venue: Nature (2020)
local_path: raw/1911.08265v2.pdf
sha256: 25588ee1d48690b33359a08a42fadfe86335aefefeee241d465b8bbd5eaa445c
format: paper PDF (21 pp)
tags: [muzero, mbrl, mcts, planning, alphazero, atari, go, value-equivalence, deepmind]
---

# MuZero — Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model

## Summary

DeepMind's completion of the AlphaGo→AlphaZero arc: **tree search with a *learned* model, no game rules**. MuZero's model is trained to predict only the **quantities relevant to planning** — reward, policy, and value — *not* to reconstruct observations or environment states ("value-equivalent" modeling). With MCTS over this abstract model it **matched AlphaZero's superhuman Go/chess/shogi play without being given the rules**, and set a then-new **state of the art on all 57 Atari games** — the canonical domain where model-based planning had historically failed. The wiki's anchor for the **decision-time-planning pole** of MBRL, opposite [Dreamer](../entities/dreamer.md)'s train-in-imagination pole.

## Key claims

- Model = representation + dynamics + prediction networks trained end-to-end on (reward, policy, value) targets only — no pixel reconstruction, no explicit state semantics. The philosophical opposite of generative world models: model *for* planning, not *of* the world.
- MCTS at decision time (contrast: PlaNet's CEM, Dreamer's amortized actor-critic, [TD-MPC2](../entities/td-mpc.md)'s local MPC — the wiki's four planning-recipe exemplars are now all sourced).
- Superhuman Go/chess/shogi at AlphaZero level, rules withheld; SOTA Atari-57.
- Descendants: [EfficientZero](efficientzero-paper.md) (sample-efficient variant), Sampled/Stochastic MuZero (not ingested).

## Entities mentioned

- DeepMind ([Google DeepMind](../entities/google-deepmind.md)); David Silver et al. — no person pages.
- [Dreamer](../entities/dreamer.md) / [TD-MPC](../entities/td-mpc.md) — the contrasting MBRL poles.

## Concepts touched

- [World model](../concepts/world-models/world-model.md) — the value-equivalent (non-generative, non-JEPA) corner of the design space; already name-dropped there, now sourced.

## Open questions

- Whether a MuZero entity page is warranted if the line grows (EfficientZero ingested; Stochastic MuZero / AlphaDev candidates).
