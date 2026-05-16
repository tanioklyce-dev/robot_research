---
title: stable-worldmodel
type: entity
subtype: software
created: 2026-05-08
updated: 2026-05-10
sources: 1
tags: [stable-worldmodel, lewm, world-model, infrastructure, env-zoo, mila, balestriero]
---

**stable-worldmodel** (`swm`) — Python package for **training and evaluating world models** end-to-end on a small-to-medium scale. The infrastructure layer underneath [LeWorldModel](leworldmodel.md): provides the env zoo, the planning / cost-model API, the dataset format, and the evaluation harness. Maintained at `rbalestr-lab/stable-worldmodel` on GitHub (Randall Balestriero's lab; also mirrored at `galilai-group/stable-worldmodel`).

## Components
- **Env zoo** — much broader than the four benches the LeWM howto initially exposed. Per the canonical README:
  - **DM Control Suite** (12 envs)
  - **Gymnasium classic control**
  - **Atari** (ALE 100+)
  - **[Push-T](pusht.md)**, **Two-Room**, **OGBench cube + scene**, **Craftax** (pixels + symbolic)
  - **Gymnasium-Robotics Fetch** (`swm/FetchReach-v3`, etc. — reach / push / slide / pick-and-place)
- **Cost-model API** — `swm.policy.AutoCostModel('<task>/<model>')` is the entry point for loading a trained world model and evaluating it as a planning cost.
- **Dataset format** — HDF5 archives shipped on HuggingFace, default storage `~/.stable-wm/` (overridable with `STABLEWM_HOME`).
- **Companion package**: `stable-pretraining` provides the training loop.

## What it is *not*
- **Not yet integrated with heavy sim.** No Isaac Lab, MuJoCo Playground, ManiSkill, RoboCasa, or Habitat integration in the canonical repo. The env zoo is "lightweight + Fetch-class."
- **Not the model itself.** `stable-worldmodel` is the harness; [LeWorldModel](leworldmodel.md) is the model that lives on top.

## Why it matters
- **Underrepresented in the wiki.** The [LeWM howto](../syntheses/world-models/leworldmodel-howto.md) originally described only PushT / cube / two-rooms / reacher — a small slice of what `swm` ships. Lint pass surfaced this as a 7-reference gap.
- **Implicitly load-bearing for the JEPA-skips-sim synthesis.** When discussions describe LeWM as "lightweight benches only," the truth is "a broad zoo of lightweight benches *plus* Fetch-class manipulation envs that bridges toward heavier sim." The synthesis ([revised version](../syntheses/world-models/why-jepa-research-skips-the-simulator-stack.md)) now reflects this nuance.

## Related
- [LeWorldModel](leworldmodel.md) — the model `stable-worldmodel` was built around.
- [LeWorldModel — train and run howto](../syntheses/world-models/leworldmodel-howto.md) — practical commands targeting `stable-worldmodel`.
- [Mila](mila.md) — Balestriero's lab affiliation.
- [Gymnasium-Robotics](gymnasium-robotics.md) — Fetch envs `swm` exposes via `swm/FetchReach-v3` etc.
- [MuJoCo](mujoco.md) / DM Control — env-zoo dependencies.

## Mentioned in
- [LeWorldModel Paper](../sources/leworldmodel-paper.md)
- [LeWorldModel — train and run howto](../syntheses/world-models/leworldmodel-howto.md)

## Open questions / TBD
- Roadmap for heavier-sim integration (Isaac Lab / MuJoCo Playground / RoboCasa) — not stated in the README.
- License terms — not surfaced.
- Boundary between `stable-worldmodel` and `stable-pretraining` — useful to document if the wiki adds a second LeWM-line ingest.
