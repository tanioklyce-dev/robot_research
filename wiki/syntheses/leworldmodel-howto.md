---
title: LeWorldModel — train and run howto
type: synthesis
created: 2026-05-07
updated: 2026-05-07
tags: [leworldmodel, lewm, jepa, world-model, howto]
---

Practical recipe for training and running [[leworldmodel|LeWorldModel]] (LeWM) — the bits the [[leworldmodel-paper|LeWorldModel Paper]] doesn't spell out. All commands sourced from the official `lucas-maes/le-wm` repo README and project page.

## Repo layout
- Official code: https://github.com/lucas-maes/le-wm
- Project page: https://le-wm.github.io/
- The LeWM repo is intentionally small. Heavy lifting is done by two upstream packages:
  - **`stable-worldmodel`** — environments, planning, evaluation harness.
  - **`stable-pretraining`** — training loop.
- LeWM itself contributes the model + the two-loss objective (next-embedding MSE + SIGReg).

## Install

```bash
uv venv --python=3.10
source .venv/bin/activate
uv pip install stable-worldmodel[train,env]
git clone https://github.com/lucas-maes/le-wm && cd le-wm
```

## Datasets
Datasets ship as HDF5 archives on HuggingFace. Default storage is `~/.stable-wm/`; override with `STABLEWM_HOME`.

```bash
export STABLEWM_HOME=/path/to/storage   # optional
# download archive.tar.zst from HF, then:
tar --zstd -xvf archive.tar.zst -C "$STABLEWM_HOME"
```

Available task datasets: `pusht`, `cube`, `tworooms`, `reacher`. These match the paper's evaluation suite — 2D + 3D control benches, **not real-robot data**.

## Train

Edit `config/train/lewm.yaml` with your WandB credentials:

```yaml
wandb:
  config:
    entity: your_entity
    project: your_project
```

Then:

```bash
python train.py data=pusht
```

- ~15M parameters, single GPU, "hours" of wall-time per the paper ([[leworldmodel-paper|LeWorldModel Paper]]).
- Checkpoints land under `$STABLEWM_HOME`.
- Swap `data=pusht` for any of the four task datasets.

## Evaluate (planning)

```bash
python eval.py --config-name=pusht.yaml policy=pusht/lewm
```

`policy` is the checkpoint path under `$STABLEWM_HOME` minus the `_object.ckpt` suffix. Eval invokes the planner against the learned latent dynamics — there's no separately trained policy head, which is the whole point of the JEPA-as-cost-model formulation.

## Skip training — use pretrained

HuggingFace checkpoints from one of the authors (Quentin Le Lidec):

- `quentinll/lewm-pusht`
- `quentinll/lewm-cube`
- `quentinll/lewm-tworooms`
- `quentinll/lewm-reacher`

Load as a planning cost model from Python:

```python
import stable_worldmodel as swm
cost = swm.policy.AutoCostModel('pusht/lewm')
```

## Caveats before committing time
- Benchmarks are 2D/3D control benches (PushT, cube, two-rooms, reacher), not real robots. The "scales to real deployment" question is open ([[leworldmodel-paper|LeWorldModel Paper]] open questions).
- Single-GPU, hours-scale training is for these tasks at their native resolution. No reported numbers for high-res or video-scale inputs.
- Reconstruction-free, reward-free, task-agnostic — but **task-conditioned via the planner cost**, not via an end-to-end policy. If you want a behavior-cloning-style "policy.act(obs)" interface, this isn't it.
- Different design point from [[v-jepa-2|V-JEPA 2]]: V-JEPA 2 = massive video pretraining + frozen encoder + post-training; LeWM = small, end-to-end pixel-trained, single-GPU.

## Sources
- `lucas-maes/le-wm` README — install/train/eval commands.
- `le-wm.github.io` — project page; HF dataset + checkpoint pointers.
- [[leworldmodel-paper|LeWorldModel Paper]] — model design, claims, benchmarks.
