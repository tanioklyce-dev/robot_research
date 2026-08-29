---
title: "PlaNet — Learning Latent Dynamics for Planning from Pixels"
type: source
url: https://arxiv.org/abs/1811.04551
author: Danijar Hafner, Timothy Lillicrap, Ian Fischer, Ruben Villegas, David Ha, Honglak Lee, James Davidson
published: 2018-11 (arXiv); ICML 2019
ingested: 2026-07-09
venue: ICML 2019
local_path: raw/1811.04551v5.pdf
sha256: abac727526e6a45669d3ab9957126587e22aacf4dc9bcd60ffe5c853108e5bcc
format: paper PDF (20 pp)
tags: [planet, rssm, mbrl, latent-dynamics, planning, cem, dmc, hafner]
---

# PlaNet — Learning Latent Dynamics for Planning from Pixels

## Summary

The origin of the **RSSM (recurrent state-space model)** — the latent-dynamics backbone that carried the entire [Dreamer](../entities/dreamer.md) line until [S5WM](s5wm-paper.md)-style SSM replacements. PlaNet ([Hafner](../entities/danijar-hafner.md) et al., ICML 2019) is a **purely model-based** agent: it learns latent dynamics from pixels and picks actions by **online planning in latent space (CEM)** — no policy network, no actor-critic (that arrives with Dreamer). Solves DMC continuous-control tasks with contact dynamics, partial observability, and sparse rewards, outperforming model-free A3C (and sometimes D4PG) with **~200× less environment interaction**.

## Key claims

- **RSSM**: latent dynamics with both **deterministic and stochastic** transition paths — the design argument (deterministic for memory, stochastic for multimodality) that every RSSM descendant inherits.
- **Latent overshooting**: multi-step variational objective training the model to predict multiple steps ahead in latent space.
- Planning: cross-entropy method over latent rollouts, replanning each step — the *decision-time-planning* recipe later abandoned by Dreamer (amortized actor-critic) but kept by the [TD-MPC](../entities/td-mpc.md) line.
- ~200× sample-efficiency gain over A3C at similar compute; pixels-only.

## Entities mentioned

- [Danijar Hafner](../entities/danijar-hafner.md) — first author; RSSM as his through-line. [Dreamer](../entities/dreamer.md) — successor. David Ha — [World Models](world-models-paper.md) link in the author list.

## Concepts touched

- [World model](../concepts/world-models/world-model.md) — RSSM origin; the planning-vs-imagination fork point.
- [Latent space](../concepts/world-models/latent-space.md) — planning happens there.

## Open questions

- None — lineage anchor. Closes the "PlaNet as separate source page" TBD on the [Dreamer entity](../entities/dreamer.md).
