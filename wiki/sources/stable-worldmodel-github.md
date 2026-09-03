---
title: "galilai-group/stable-worldmodel — the repository, four months after the paper"
type: source
url: https://github.com/galilai-group/stable-worldmodel
author: "Lucas Maes, Quentin Le Lidec et al. (GalilAI group; Mila, NYU, Brown, LanceDB, Oxford)"
published: 2026-09-03
ingested: 2026-09-02
venue: GitHub repository (PyPI `stable-worldmodel`; docs at galilai-group.github.io/stable-worldmodel)
format: code + documentation
tags: [stable-worldmodel, swm, world-model, benchmark, planning, solvers, lance, lerobot, factors-of-variation, mpc, balestriero, infrastructure]
---

# stable-worldmodel — repository state, 2026-09

## Summary

The wiki already carries the [stable-worldmodel paper](stable-worldmodel-paper.md) (arXiv 2605.21800, 2026-05-20) and an [entity page](../entities/stable-worldmodel.md) last updated in July. This ingests **the repository as it stands now** — last commit `6f1e499`, *"Freeze TD-MPC2 running scale during validation (#322)"*, **2026-09-03** — because four months of development have added things that change what the platform is *for*, and because the entity page carries a fact that is now wrong.

The current self-description: *"a single, unified interface for the three stages of world model research — **collecting data**, **training**, and **evaluating with model-predictive control** — across a large suite of standardized environments."*

> [!warning] Correction: `rbalestr-lab` → `galilai-group` is a move, not a mirror
> The [entity page](../entities/stable-worldmodel.md) says the package is *"maintained at `rbalestr-lab/stable-worldmodel`... also mirrored at `galilai-group/stable-worldmodel`."* As of 2026-09-02 the old URL **301-redirects** to the new one, and every canonical link — docs site, Colab notebook, HuggingFace datasets (`galilai-group/lewm-pusht`), CI badges — is under `galilai-group`. The mirror is the original. Same for [`lejepa`](lejepa-github.md).

## What the repository has that the paper does not

### A planning-solver library, not one planner

Seven solvers, which makes the platform a place to study *the planner* rather than only the world model — the wiki's [gradient-based planning](../concepts/world-models/gradient-based-planning.md) page compares two of these and now has a harness for the rest:

| Sampling | Gradient | Constrained |
|---|---|---|
| CEM, iCEM, MPPI, Predictive Sampling | SGD/Adam, PGD | Augmented Lagrangian |

And **six reference baselines** spanning three method families: **DINO-WM, PLDM, LeWM** (JEPA), **GCBC** (behavior cloning), **GCIVL, GCIQL** (offline goal-conditioned RL). That last pair matters — it means a JEPA world model and an offline-RL policy can be scored on identical environments and identical data, which is exactly the comparison the wiki's [online MBRL vs imitation](../syntheses/rl/online-mbrl-vs-imitation-robot-learning.md) synthesis has to make from separate papers.

### Factors of variation, counted per environment

**29 registered environment IDs** plus 100+ ALE Atari games, and — the part worth having — most ship **independently controllable visual and physical parameters** (lighting, texture, dynamics, morphology) with the count published per environment: `swm/TwoRoom-v1` **17**, `swm/PushT-v1` **16**, `swm/OGBScene-v0` 12, `swm/OGBCube-v0` and the Fetch push/slide/pick-and-place tasks 11 each, down to `swm/MountainCarContinuousControl-v0` 4.

This is the machinery behind the wiki's most-cited counter-result — [LeWM dropping from 50.8% to 6–26%](stable-worldmodel-paper.md) under targeted perturbation — exposed as a first-class, enumerable API rather than an experiment someone ran. Sources: DM Control Suite, Gymnasium classic control, OGBench, Craftax, ALE, plus Two-Room and Push-T.

### A dataset-format registry, including a LeRobot adapter

Five backends behind one interface (`lance` default, `hdf5`, `folder`, `video`, `lerobot`), with `swm.data.convert()` for one-shot migration and an `append`/`overwrite`/`error` mode on every writer.

The **`lerobot://<repo_id>` read-only adapter** is the one that matters for this wiki: it lets a world model train and evaluate directly on [LeRobot](../entities/lerobot.md) Hub datasets without conversion. That connects the JEPA world-model line to the wiki's actual hardware stack for the first time. (Python 3.12+, separate extra.)

Published throughput and storage benchmarks, reproducible from `scripts/benchmark/compare_h5_lance.py` on the LeWM Push-T dataset:

| Format | Source | samples/s | ms/step |
|---|---|---|---|
| LanceDB | local | **4814.8** | 13.3 |
| HDF5 | local | 1416.1 | 45.2 |
| Video | local | 1330.6 | 48.1 |
| LanceDB | S3 | **3183.7** | 20.1 |
| HDF5 | S3 (no cache) | **9.1** | **7032.5** |

Storage for the same data: HDF5 **43.12 GB**, LanceDB **13.31 GB**, Video **496.29 MB**.

> [!note] Two numbers with consequences beyond this repo
> **HDF5 over S3 without caching collapses to 9.1 samples/s — a 350× penalty** against the same data in LanceDB. Any "stream your dataset from object storage" plan built on HDF5 is not slow, it is unusable, and the wiki's [cloud GPU rental](../syntheses/platforms/nvidia-gpu-rental-landscape.md) page should assume the dataset format decides whether remote training is viable at all.
>
> And **video storage is 87× smaller than HDF5** (496 MB vs 43 GB) at ~94% of HDF5's local throughput. For anyone training a world model on a workstation with a consumer SSD, that is the difference between fitting the dataset and not.

### Packaging shaped around robot deployment

The install extras are split with an explicit rationale, and it is a robotics rationale:

> *"`[data]` pulls in the Lance stack... It is a separate extra so that consumers who only need the solvers and world model — e.g. **embedding `stable_worldmodel.planning` in a robotics image** — are not forced to install ~410 MB of native wheels they never import."*

So `pip install stable-worldmodel` gives planning and models with no dataset I/O. That is the maintainers anticipating exactly the [on-robot deployment](../syntheses/agents/on-device-and-on-robot-agents.md) case this wiki keeps hitting, where image size on a [Jetson](../entities/jetson-orin-nx.md) is a real constraint.

### Miscellany

- A `swm` **CLI** — `swm datasets / inspect / envs / fovs / checkpoints / convert` — for inspecting datasets, environments, factors of variation and checkpoints without writing code.
- Reference training scripts: `scripts/train/lewm.py` implements LeWM, `scripts/train/prejepa.py` reproduces DINO-WM.
- A Colab notebook training **directly from HuggingFace object storage with no local download**.
- Full docs site with API reference and tutorials; on PyPI; pre-commit, Ruff, CI.
- Downstream users named: **C-JEPA** and **LeWM**.

## Caveats

> [!warning] Explicitly unstable
> *"The library is in active development. APIs may change between minor versions."* Anything the wiki records from this page is a snapshot of 2026-09-02, and the commit that day (#322) was a correctness fix to TD-MPC2 validation — this is a moving target, not a released artifact.

- Benchmarks are self-reported by the maintainers using their own script on their own dataset. Reproducible in principle; not independently reproduced here.
- The environment suite is entirely **simulated**; the LeRobot adapter reads real robot data but nothing here evaluates on hardware.

## Entities mentioned
- [stable-worldmodel](../entities/stable-worldmodel.md), [LeWorldModel](../entities/leworldmodel.md), [DINO-WM](../entities/dino-wm.md), [PLDM](../entities/pldm.md), [Push-T](../entities/pusht.md), [LeRobot](../entities/lerobot.md), [Randall Balestriero](../entities/randall-balestriero.md), [Lucas Maes](../entities/lucas-maes.md).

## Concepts touched
- [Gradient-based planning](../concepts/world-models/gradient-based-planning.md) — seven solvers under one API.
- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) · [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — factors of variation as an enumerable API.
- [World model](../concepts/world-models/world-model.md) · [SIGReg](../concepts/world-models/sigreg.md).

## Open questions
- **Has anyone run the JEPA baselines against GCIVL/GCIQL on the same environments?** The platform makes it a config change, and it is the comparison the wiki most wants.
- **Does the LeRobot adapter work on a real dataset end to end?** If so, the shortest path from this wiki's [SO-101](../entities/so-arm101.md)/[LeKiwi](../entities/lekiwi.md) hardware to a trained JEPA world model is much shorter than the [project pages](../syntheses/projects/lewm-on-stretch-feasibility.md) assume.
- **The paper's headline OOD collapse — has it moved?** Four months and 300+ merged PRs later, nothing in the README says whether the 50.8% → 6–26% Push-T result still holds under the current code.
