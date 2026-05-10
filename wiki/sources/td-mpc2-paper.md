---
title: TD-MPC2 Paper — Scalable, Robust World Models for Continuous Control (Hansen et al., ICLR 2024)
type: source
url: https://arxiv.org/abs/2310.16828
author: Nicklas Hansen, Hao Su, Xiaolong Wang
affiliation: Not stated on the arxiv abstract page (UC San Diego, Hansen / Su / Wang labs based on prior work)
published: 2023-10-25 (arxiv v1); 2024-03-21 (v2); ICLR 2024
ingested: 2026-05-10
created: 2026-05-10
updated: 2026-05-10
tags: [td-mpc, td-mpc2, world-model, model-based-rl, mpc, latent-space, hansen, mbrl, decoder-free]
---

> [!note] Ingest depth
> This source page is **based on the arxiv abstract page only** (paper PDF not in `raw/`). Filed as part of the curriculum-driven backfill of LeWM baselines. To deepen, drop the PDF in `raw/` and re-ingest; [tdmpc2.com](https://tdmpc2.com) hosts the official code, models, and videos.

## Summary

**TD-MPC2** — Hansen, Su, Wang (ICLR 2024). Successor to **TD-MPC** (Hansen et al. 2022). Trains a **decoder-free implicit world model** in latent space and plans against it with **local trajectory optimization (MPC)**, bootstrapped by a **TD-trained value function** to extend the effective planning horizon beyond the MPC window. Headline contribution: **single set of hyperparameters** consistently strong across **104 online-RL tasks in 4 domains**; demonstration that a single 317M-parameter agent can operate across multiple task domains, embodiments, and action spaces, with performance scaling in model and data. Architecturally the closest MBRL relative to JEPA in this wiki — both elide pixel reconstruction.

## Abstract (verbatim opener)

> "TD-MPC2 improves significantly over baselines across 104 online RL tasks spanning 4 diverse task domains, achieving consistently strong results with a single set of hyperparameters."
>
> "We further show that agent capabilities increase with model and data size, and successfully apply TD-MPC2 to train a single 317M parameter agent to perform 80 tasks across multiple task domains, embodiments, and action spaces."

## Key claims

- **Decoder-free latent world model.** The world model predicts in latent space without a pixel decoder; this avoids the cost of generating pixels and the representation pressure of reconstruction.
- **MPC + TD value bootstrap.** Local trajectory optimization (MPC against the learned latent dynamics) is supplemented by a TD-trained value function that bootstraps beyond the MPC horizon — the "TD-MPC" structural commitment.
- **Single hyperparameter set across 104 tasks / 4 domains.** Matches DreamerV3's generality claim from the opposite ([decoder-free](#)) end of the design axis.
- **Scaling.** Performance improves with model and data size; a 317M-param agent does 80 tasks across embodiments and action spaces.

## Why it matters in this wiki

- **The TD-MPC baseline column.** TD-MPC (and by extension TD-MPC2) is one of the four world-model baselines in [LeWM](../entities/leworldmodel.md). With this source page filed, curriculum [Module 10](../syntheses/robot-learning-curriculum.md) can place it on the four-family taxonomy.
- **Closest MBRL relative to JEPA in this wiki.** Decoder-free latent dynamics + planning is structurally analogous to LeWM's setup — the differences (TD-bootstrapped value vs MPC-only; single-task RL fine-tune vs generalist offline-trained predictor; collapse-prevention strategy) are the interesting axes for [Module 11](../syntheses/robot-learning-curriculum.md) (JEPA depth) and [Module 12](../syntheses/robot-learning-curriculum.md) (LeWM deep-dive).
- **Continuous-control RL canon.** Sits alongside [PPO](#), [SAC](#), and Dreamer as a default RL baseline whose vocabulary is needed to read modern RL/robotics papers (curriculum Module 8).

## Entities mentioned

- [TD-MPC](../entities/td-mpc.md) — the algorithm/family entity.
- [LeWorldModel](../entities/leworldmodel.md) — uses TD-MPC as a baseline column.
- [Dreamer](../entities/dreamer.md) — sibling MBRL family.

## Concepts touched

- [World model](../concepts/world-model.md) — TD-MPC2 is a decoder-free MBRL exemplar.

## Open questions / TBD

- **Full paper not yet ingested** — abstract-level only. The exact MPC sampling scheme (CEM? MPPI?), value-bootstrap details, and 4-domain task breakdown are unquoted here.
- **TD-MPC1 as a separate source.** The 2022 paper (Hansen, Wang, Su) introduces the architecture; useful to file as a separate page if the family lineage gets curriculum weight.
- **Author entity page for Nicklas Hansen** — would anchor TD-MPC1 → TD-MPC2 lineage.
