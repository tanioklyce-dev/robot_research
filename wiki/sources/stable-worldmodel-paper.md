---
title: "stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation (Maes et al., 2026)"
type: source
url: https://arxiv.org/abs/2605.21800
local_path: null
author: "Lucas Maes, Quentin Le Lidec, Luiz Facury, Nassim Massaudi, Ayush Chaurasia, Francesco Capuano, Richard Gao, Taj Gillin, Dan Haramati, Damien Scieur, Yann LeCun, Randall Balestriero"
affiliations: Mila & Université de Montréal; New York University; Universidade Federal de Minas Gerais; Independent; LanceDB; University of Oxford; Brown University
published: 2026-05-20
ingested: 2026-07-26
venue: arXiv preprint (cs.LG)
license: CC BY 4.0
tags: [stable-worldmodel, swm, world-model, benchmark, reproducibility, generalization, planning, lance, lerobot, dino-wm, leworldmodel, pldm, td-mpc2, maes, balestriero, lecun]
---

# stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation

## Summary

An open-source platform (**`swm`**) that standardizes world-model research — unified baselines, a fast columnar data layer, and a benchmark suite with **controllable factors of variation** for zero-shot generalization. Its headline empirical result is the one that matters for the wiki's JEPA thread: **current world models generalize poorly.** LeWorldModel scores ~50.8 % on the base Push-T task and drops to **6–26 % under targeted color / size / shape changes**; distractor objects produce a **quadratic collapse** across all baselines. The infrastructure is the contribution; the brittleness finding is the news.

> [!note] Same group, opposite direction from the theory paper
> Posted **five days before** [When Does LeJEPA Learn a World Model?](when-does-lejepa-learn-a-world-model-paper.md), sharing LeCun and Balestriero as co-authors, and led by the [LeWorldModel](../entities/leworldmodel.md) lead author. One paper proves what a faithful JEPA world model requires; this one measures how far current implementations are from it. Neither paper cites the other's result as a reconciliation.

## Key claims

### The three bottlenecks

| Bottleneck | Evidence given | `swm`'s answer |
|---|---|---|
| **Reproducibility fragmentation** | The **Cross-Entropy Method reimplemented separately across five papers** | Unified, battle-tested implementations; all solvers validated to reproduce their original papers' planning success rates |
| **Data I/O** | Individual frames = fast random access but prohibitive overhead; compressed video = small but poor random access | **Lance** columnar format (below) |
| **Robust-evaluation gap** | Standard benchmarks only evaluate near the training distribution | Systematic controllable visual / geometric / physical variations |

### Data layer — throughput (Push-T)

| Format | Samples/sec |
|---|---|
| **Lance (local)** | **4,815** |
| Lance (S3) | 3,184 |
| HDF5 (local) | 1,416 |
| Video (local) | 1,331 |

Native **MP4, HDF5, and [LeRobot](../entities/lerobot.md)** support with one-click conversion — real-robot LeRobot datasets convert automatically for the ~3.4× throughput gain over HDF5.

### What's implemented

- **World models:** [DINO-WM](../entities/dino-wm.md) (frozen [DINOv2](../entities/dinov2.md) + ViT predictor), [LeWorldModel](../entities/leworldmodel.md), [PLDM](../entities/pldm.md), [TD-MPC2](../entities/td-mpc.md), and goal-conditioned baselines (GCBC, GCIVL, GCIQL).
- **Planning solvers** — sampling-based: Predictive Sampling, **CEM**, iCEM, MPPI, Categorical CEM; gradient-based: Gradient Descent, Projected GD, Lagrangian, GRASP.
- **Environments:** Classic Control (CartPole), MuJoCo, Atari, Robotics (**Push-T**, OGBench), and partial observability (Craftax).
- **Factors of variation** — *visual*: agent color/size/shape, object properties, canvas background, lighting, textures, occlusions; *physical*: mass, density, gravity, friction. For closed-source environments (Atari), perturbations are applied at the **observation level** via boundary wrappers.

### The brittleness results

- **Visual perturbations:** color variations cause sharp success-rate drops **even under mild perturbation**. Distractor squares produce a **quadratic decay** — models tolerate a few, then degrade rapidly.
- **LeWorldModel:** **50.8 %** base-task success → **6–26 %** under targeted color/size/shape changes. Reported in-distribution Push-T is higher still (LeWM **94 %**, DINO-WM **92 %**), which is precisely the point: **in-distribution scores hide the fragility.**

> [!warning] Two different "baseline" numbers — reconcile before citing
> This ingest surfaced **both 50.8 % and 94 %** as LeWM's unperturbed score, presumably a base-task-aggregate vs a specific in-distribution Push-T configuration. **The wiki has not verified which is which.** The direction and magnitude of the collapse (down to 6–26 %) is consistent across both framings and is what the derived pages rely on; the exact unperturbed baseline should be checked against the paper's tables before being quoted as a headline number.
- **The counterintuitive finding:** prediction MSE rises monotonically across training → validation → random trajectories → random + all variations, but **prediction error correlates poorly with planning success**. It is *being out of distribution*, not the magnitude of prediction error, that drives planning failure. This breaks the intuitive habit of using rollout MSE as a proxy for planning competence.
- Overall: current world models show "limited zero-shot generalization: even modest shifts outside the training distribution lead to substantial degradation in planning performance."

## Entities mentioned
- [stable-worldmodel](../entities/stable-worldmodel.md) — the platform itself
- [Lucas Maes](../entities/lucas-maes.md) — lead author; also LeWorldModel lead
- [Yann LeCun](../entities/yann-lecun.md) / [Randall Balestriero](../entities/randall-balestriero.md) — co-authors
- [LeWorldModel](../entities/leworldmodel.md), [DINO-WM](../entities/dino-wm.md), [PLDM](../entities/pldm.md), [TD-MPC2](../entities/td-mpc.md) — implemented baselines
- [Mila](../entities/mila.md) — lead affiliation
- [LeRobot](../entities/lerobot.md) — supported dataset format
- [DINOv2](../entities/dinov2.md) — DINO-WM's frozen encoder

## Concepts touched
- [World model](../concepts/world-models/world-model.md)
- [JEPA](../concepts/world-models/jepa.md) — the family under test
- [Identifiability](../concepts/world-models/identifiability.md) — the property the companion theory paper proves, and which these results suggest is not being achieved in practice
- [World-model simulators](../concepts/world-models/world-model-simulators.md)

## Open questions

- **Does brittleness contradict the identifiability theorem, or sit outside its assumptions?** The theory assumes stationary additive-noise transitions and `m = n`; a color-shifted Push-T arguably violates the generative model entirely. The two papers do not address each other.
- **Would a model trained *with* the factors of variation hold up**, or is this a limit of the objective rather than of the training distribution? The paper measures zero-shot generalization only.
- **No JEPA-vs-generative-video comparison** — every baseline here is latent-prediction or goal-conditioned. [Cosmos](../entities/nvidia-cosmos.md)-class generative video models are absent, so this says nothing about which family is more robust.
- **Real-robot evaluation is absent** despite the LeRobot data path; all reported results are simulated.

## Code
- Repo: https://github.com/galilai-group/stable-worldmodel — CC BY 4.0
- Docs: https://galilai-group.github.io/stable-worldmodel/
- Predecessor: [stable-worldmodel-v1](https://arxiv.org/abs/2602.08968) (arXiv 2602.08968, Feb 2026)
- `swm` is the substrate [LeWorldModel's own repo](lewm-github.md) is built on.
