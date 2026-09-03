---
title: stable-worldmodel
type: entity
subtype: software
created: 2026-05-08
updated: 2026-09-02
sources: 6
tags: [stable-worldmodel, swm, lewm, world-model, infrastructure, env-zoo, benchmark, generalization, lance, mila, balestriero]
---

**stable-worldmodel** (`swm`) — Python package for **training and evaluating world models** end-to-end on a small-to-medium scale. The infrastructure layer underneath [LeWorldModel](leworldmodel.md): provides the env zoo, the planning / cost-model API, the dataset format, and the evaluation harness. Maintained at **`galilai-group/stable-worldmodel`** on GitHub — the **GalilAI group**, Randall Balestriero's lab org (*"Foundation Models, Theory, World Models, Everything AI"*). **Corrected 2026-09-02**: an earlier version of this page called galilai-group a mirror of `rbalestr-lab`. It is the other way round — the `rbalestr-lab` URL now **301-redirects** here, and every canonical link (docs site, PyPI, Colab, HuggingFace datasets) is under `galilai-group`. See [the repository source page](../sources/stable-worldmodel-github.md).

> [!note] The repository has outgrown the paper — see [the 2026-09 repo snapshot](../sources/stable-worldmodel-github.md)
> Added since the May paper: **seven planning solvers** (CEM, iCEM, MPPI, Predictive Sampling, SGD/Adam, PGD, Augmented Lagrangian), **six baselines across three method families** (DINO-WM / PLDM / LeWM, GCBC, GCIVL / GCIQL), a **five-backend dataset-format registry** including a read-only **`lerobot://` adapter**, per-environment **factor-of-variation counts** as a first-class API, a `swm` CLI, and an extras split that keeps `stable_worldmodel.planning` installable into a robotics image without ~410 MB of Lance wheels.

## Components
- **Env zoo** — much broader than the four benches the LeWM howto initially exposed. Per the canonical README:
  - **DM Control Suite** (12 envs)
  - **Gymnasium classic control**
  - **Atari** (ALE 100+)
  - **[Push-T](pusht.md)**, **Two-Room**, **OGBench cube + scene**, **Craftax** (pixels + symbolic)
  - **Gymnasium-Robotics Fetch** (`swm/FetchReach-v3`, etc. — reach / push / slide / pick-and-place)
- **Cost-model API** — `swm.policy.AutoCostModel('<task>/<model>')` is the entry point for loading a trained world model and evaluating it as a planning cost.
- **Dataset format** — HDF5 archives shipped on HuggingFace, default storage `~/.stable-wm/` (overridable with `STABLEWM_HOME`). **As of the May 2026 paper the primary format is [Lance](https://lancedb.github.io/lance/)** columnar storage, with one-click conversion from MP4 / HDF5 / **[LeRobot](lerobot.md)**: **4,815 samples/sec** (Lance local) vs **1,416** (HDF5) and **1,331** (video); 3,184 streaming from S3 ([paper](../sources/stable-worldmodel-paper.md)).
- **Companion package**: `stable-pretraining` provides the training loop.

## Baselines and solvers (per the paper)
- **World models** — [DINO-WM](dino-wm.md) (frozen [DINOv2](dinov2.md) + ViT predictor), [LeWorldModel](leworldmodel.md), [PLDM](pldm.md), [TD-MPC2](td-mpc.md), plus goal-conditioned GCBC / GCIVL / GCIQL.
- **Planning solvers** — sampling-based (Predictive Sampling, **CEM**, iCEM, MPPI, Categorical CEM) and gradient-based (Gradient Descent, Projected GD, Lagrangian, GRASP). All validated to reproduce their original papers' planning success rates.
- **Factors of variation** — the piece that makes it a *generalization* benchmark rather than an env zoo: visual (agent color/size/shape, object properties, background, lighting, textures, occlusions) and physical (mass, density, gravity, friction), applied at the observation level for closed-source envs like Atari.

The stated motivation is a reproducibility indictment: the **Cross-Entropy Method had been reimplemented separately across five papers**.

## What it is *not*
- **Not yet integrated with heavy sim.** No Isaac Lab, MuJoCo Playground, ManiSkill, RoboCasa, or Habitat integration in the canonical repo. The env zoo is "lightweight + Fetch-class."
- **Not the model itself.** `stable-worldmodel` is the harness; [LeWorldModel](leworldmodel.md) is the model that lives on top.

## Why it matters
- **Underrepresented in the wiki.** The [LeWM howto](../syntheses/world-models/leworldmodel-howto.md) originally described only PushT / cube / two-rooms / reacher — a small slice of what `swm` ships. Lint pass surfaced this as a 7-reference gap.
- **Implicitly load-bearing for the JEPA-skips-sim synthesis.** When discussions describe LeWM as "lightweight benches only," the truth is "a broad zoo of lightweight benches *plus* Fetch-class manipulation envs that bridges toward heavier sim." The synthesis ([revised version](../syntheses/world-models/why-jepa-research-skips-the-simulator-stack.md)) now reflects this nuance.

## The brittleness result (May 2026 paper)

`swm`'s first headline finding is the empirical counterweight to the JEPA program's theory: **current world models barely generalize.** [LeWorldModel](leworldmodel.md) scores **50.8 %** on base Push-T and **6–26 %** under targeted color / size / shape shifts; distractor objects cause a **quadratic decay** across all baselines. In-distribution the same models look strong (LeWM 94 %, DINO-WM 92 %), which is the point — **in-distribution scores hide the fragility.**

The subtler finding: **prediction MSE correlates poorly with planning success.** Being out-of-distribution, not the size of the prediction error, is what breaks planning — so rollout MSE is not a safe proxy for planning competence. Full numbers on the [source page](../sources/stable-worldmodel-paper.md).

## Related
- [LeWorldModel](leworldmodel.md) — the model `stable-worldmodel` was built around.
- [Lucas Maes](lucas-maes.md) — lead author of both `swm` and LeWM.
- [Randall Balestriero](randall-balestriero.md) — co-author; the lab the canonical repo sits in.
- [Identifiability](../concepts/world-models/identifiability.md) — the theoretical property the [companion paper](../sources/when-does-lejepa-learn-a-world-model-paper.md) proves, and which these results suggest is not being achieved in practice.
- [LeWorldModel — train and run howto](../syntheses/world-models/leworldmodel-howto.md) — practical commands targeting `stable-worldmodel`.
- [Mila](mila.md) — Balestriero's lab affiliation.
- [Gymnasium-Robotics](gymnasium-robotics.md) — Fetch envs `swm` exposes via `swm/FetchReach-v3` etc.
- [MuJoCo](mujoco.md) / DM Control — env-zoo dependencies.

## Mentioned in
- [stable-worldmodel paper (Maes et al., 2026)](../sources/stable-worldmodel-paper.md) — the platform's own paper; 12 authors incl. [LeCun](yann-lecun.md) + [Balestriero](randall-balestriero.md). Supersedes [stable-worldmodel-v1](https://arxiv.org/abs/2602.08968) (Feb 2026).
- [LeWorldModel GitHub README](../sources/lewm-github.md) — names the `stable-worldmodel` package as the env-zoo + training API.
- [onchain-ai-garage — LeWM reproduction log](../sources/onchain-ai-garage-lewm-reproduction.md) — the `stable-worldmodel` repo install as the field-reported friction point.
- [LeWorldModel — train and run howto](../syntheses/world-models/leworldmodel-howto.md)

## Open questions / TBD
- Roadmap for heavier-sim integration (Isaac Lab / MuJoCo Playground / RoboCasa) — not stated in the README.
- ~~License terms~~ — **resolved: CC BY 4.0** (May 2026 paper).
- Boundary between `stable-worldmodel` and `stable-pretraining` — useful to document if the wiki adds a second LeWM-line ingest.
