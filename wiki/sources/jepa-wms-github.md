---
title: "JEPA-WMs GitHub (facebookresearch/jepa-wms)"
type: source
url: https://github.com/facebookresearch/jepa-wms
hf_models: https://huggingface.co/facebook/jepa-wms
hf_dataset: https://huggingface.co/datasets/facebook/jepa-wms
license: CC-BY-NC 4.0
author: Meta FAIR (Basile Terver, Tsung-Yen Yang, Jean Ponce, Adrien Bardes, Yann LeCun)
published: 2025-12-30
ingested: 2026-05-25
created: 2026-05-25
updated: 2026-05-25
tags: [jepa-wms, jepa, world-model, fair, meta-fair, github, reproducibility, dinov2, dinov3, vjepa-2-ac, droid, robocasa, metaworld, cc-by-nc, primary-source]
---

## Summary

Official PyTorch implementation, datasets, and pretrained checkpoints for **[JEPA-WMs (Terver et al., TMLR 05/2026)](jepa-wms-paper.md)**. Distinct from the paper ingest: this source page captures the **reproducibility recipe** — which checkpoints exist, how to load them, the environment setup, dataset sources, and config-file → paper-figure mapping. The most operationally useful fact for the wiki is that the repo ships a **"fixed" V-JEPA-2-AC baseline** alongside the JEPA-WM checkpoints — i.e. the rollout-loss-bug-fix retraining the paper §C describes, now downloadable rather than requiring user retraining.

**License: CC-BY-NC 4.0** — non-commercial. Important practical constraint for the wiki's [project-ladder syntheses](../syntheses/projects/jepa-project-ladder-rosorin-pro.md) and any downstream Stretch/ROSOrin Pro work.

## Key claims

### Pretrained models — JEPA-WM (paper's "Ours")

| Environment | Resolution | Encoder | Pred. depth | HF | Direct |
|---|---|---|---|---|---|
| DROID & RoboCasa | 256×256 | **DINOv3 ViT-L/16** | **12** | `jepa_wm_droid.pth.tar` | `droid_jepa-wm_noprop.pth.tar` |
| Metaworld | 224×224 | DINOv2 ViT-S/14 | 6 | `jepa_wm_metaworld.pth.tar` | `mw_jepa-wm.pth.tar` |
| Push-T | 224×224 | DINOv2 ViT-S/14 | 6 | `jepa_wm_pusht.pth.tar` | `pt_jepa-wm.pth.tar` |
| PointMaze | 224×224 | DINOv2 ViT-S/14 | 6 | `jepa_wm_pointmaze.pth.tar` | `mz_jepa-wm.pth.tar` |
| Wall | 224×224 | DINOv2 ViT-S/14 | 6 | `jepa_wm_wall.pth.tar` | `wall_jepa-wm.pth.tar` |

Matches the [paper's recommended recipe](jepa-wms-paper.md): DINOv2-S + depth-6 in sim, DINOv3-L + depth-12 for real manipulation. **The DROID checkpoint is single-checkpoint, no proprioception** (`noprop` in the filename) because DROID and Robocasa proprio spaces don't align for zero-shot transfer.

### Pretrained models — DINO-WM baseline (reproduced)

| Environment | Resolution | Encoder | Depth |
|---|---|---|---|
| DROID & RoboCasa | 224×224 | DINOv2 ViT-S/14 | 6 |
| Metaworld | 224×224 | DINOv2 ViT-S/14 | 6 |
| Push-T | 224×224 | DINOv2 ViT-S/14 | 6 |
| PointMaze | 224×224 | DINOv2 ViT-S/14 | 6 |
| Wall | 224×224 | DINOv2 ViT-S/14 | 6 |

### Pretrained models — V-JEPA-2-AC "fixed" baseline

| Environment | Resolution | Encoder | Depth |
|---|---|---|---|
| DROID & RoboCasa | 256×256 | **V-JEPA-2 ViT-G/16** | **24** |

> [!note] The "fixed" V-JEPA-2-AC is what the paper used
> The paper's Table 2 comparison ([source](jepa-wms-paper.md)) used a V-JEPA-2-AC **retrained with a rollout-loss bug fix** (§C of the paper), not the public V-JEPA-2-AC checkpoint. This repo ships **both**: `vjepa2_ac_droid` (the fixed version that produced the paper's numbers) and `vjepa2_ac_oss` (the original [V-JEPA 2 GitHub](vjepa2-github.md) checkpoint). When the [V-JEPA 2 entity](../entities/v-jepa-2.md) says "JEPA-WMs beats V-JEPA-2-AC on Rc-R + DROID," the apples-to-apples comparison is against this fixed variant.

### VM2M decoder heads (optional)

For visualization / rollout decoding only. **Not required** for world-model training or planning evals.

| Decoder | Encoder | Resolution |
|---|---|---|
| `dinov2_vits_224` (05norm) | DINOv2 ViT-S/14 | 224×224 |
| `dinov2_vits_224_INet` | DINOv2 ViT-S/14 | 224×224 |
| `dinov3_vitl_256_INet` | DINOv3 ViT-L/16 | 256×256 |
| `vjepa2_vitg_256_INet` | V-JEPA-2 ViT-G/16 | 256×256 |

Assignment rule: DINO-WM → `dinov2_vits_224` (05norm); JEPA-WM → INet variants (`dinov2_vits_224_INet` sim, `dinov3_vitl_256_INet` real); V-JEPA-2-AC → `vjepa2_vitg_256_INet`.

### Loading checkpoints

Two paths. Both go through `torch.hub.load('facebookresearch/jepa-wms', '<name>')`:

```python
import torch

# JEPA-WMs (paper's "Ours")
model, preprocessor = torch.hub.load('facebookresearch/jepa-wms', 'jepa_wm_droid')
model, preprocessor = torch.hub.load('facebookresearch/jepa-wms', 'jepa_wm_metaworld')
# (+ jepa_wm_pusht, jepa_wm_pointmaze, jepa_wm_wall)

# Baselines
model, preprocessor = torch.hub.load('facebookresearch/jepa-wms', 'dino_wm_droid')
model, preprocessor = torch.hub.load('facebookresearch/jepa-wms', 'vjepa2_ac_droid')    # fixed
model, preprocessor = torch.hub.load('facebookresearch/jepa-wms', 'vjepa2_ac_oss')      # original
```

HF Hub equivalent via `huggingface_hub.hf_hub_download(repo_id="facebook/jepa-wms", filename="...")`.

### Environment setup (operational)

```bash
# Conda for system deps (ffmpeg), uv for Python pkgs
conda create -n jepa-wms python=3.10 ffmpeg=7 -c conda-forge -y
conda activate jepa-wms
curl -LsSf https://astral.sh/uv/install.sh | sh
git clone git@github.com:facebookresearch/jepa-wms.git && cd jepa-wms
uv pip install -e .
```

Required env vars (set in `~/.bashrc`):

| Var | Purpose |
|---|---|
| `JEPAWM_DSET` | datasets root |
| `JEPAWM_LOGS` | train + planning eval logs |
| `JEPAWM_HOME` | workspace (parent of cloned repo) |
| `JEPAWM_CKPT` | saved checkpoints (optional, defaults to logs) |
| `JEPAWM_OSSCKPT` | pretrained encoder weights (optional) |

Then `cd $JEPAWM_HOME/jepa-wms && python setup_macros.py`.

### External dependencies

- **DINOv2** — auto-downloaded via TorchHub.
- **DINOv3** — manual install: clone [facebookresearch/dinov3](https://github.com/facebookresearch/dinov3) to `$JEPAWM_HOME/dinov3/`; download pretrained weights to `$JEPAWM_OSSCKPT/dinov3/`.
- **V-JEPA v1 / v2** — manual download recommended (TorchHub causes import conflicts). V-JEPA v1 from `facebookresearch/jepa`, V-JEPA v2 from `facebookresearch/vjepa2`.
- **MuJoCo 2.1** — required only for PointMaze (uses `d4rl` → `mujoco-py`). Other envs use the modern `mujoco` package.
- **RoboCasa + RoboSuite** — optional; uses **Basile-Terver/robosuite** and **Basile-Terver/robocasa** forks (not the upstream repos). Kitchen assets are ~20 GB.

### Datasets shipped via HF (`facebook/jepa-wms`)

| Dataset | Description |
|---|---|
| `pusht` | Push-T trajectories (re-host from `apple/ml-dino-wm`, unchanged) |
| `pointmaze` | PointMaze navigation (same provenance) |
| `wall` | Wall trajectories (same provenance) |
| `metaworld` | 42 Metaworld tasks × 100 episodes |
| `robocasa` | Kitchen manipulation |
| `franka` | Franka robot trajectories |

Download via `python src/scripts/download_data.py [--dataset ...]`.

### DROID dataset (optional, separate)

Not on HF — requires `gsutil` from Google Research's bucket:

- **Stereo HD MP4** (full raw): 8.7 TB
- **Non-stereo HD only** (skip SVO + stereo files): 5.6 TB

After download, run `src/scripts/generate_droid_paths.py` to produce `droid_paths.csv` that the dataloader reads.

### Optional pretraining datasets (decoder heads only)

Kinetics-400, Kinetics-710, Something-Something-v2, HowTo100M — referenced via CSV path files under `$JEPAWM_DSET/`.

### Config-file → paper-figure mapping

| Model | Environment | Config path (under `configs/vjepa_wm/`) |
|---|---|---|
| JEPA-WM | Metaworld | `mw_final_sweep/mw_4f_fsk5_ask1_r224_pred_AdaLN_ftprop_depth6_repro_2roll_save.yaml` |
| JEPA-WM | PointMaze | `mz_sweep/mz_4f_fsk5_ask1_r224_vjtranoaug_predAdaLN_ftprop_depth6_repro_2roll_save_2n.yaml` |
| JEPA-WM | Push-T | `pt_sweep/pt_4f_fsk5_ask1_r224_vjtranoaug_predAdaLN_ftprop_depth6_repro_2roll_save.yaml` |
| JEPA-WM | Wall | `wall_sweep/wall_4f_fsk5_ask1_r224_vjtranoaug_predAdaLN_ftprop_depth6_repro_2roll_save_2n.yaml` |
| JEPA-WM | RoboCasa & DROID | `droid_final_sweep/droid_4fpcs_fps4_r256_dv3vitl_asp1_pred_AdaLN_depth12_noprop_repro_2roll_4n.yaml` |
| DINO-WM | any env | `<env>_sweep/<env>_4f_fsk5_ask1_r224_pred_dino_wm_depth6_repro_1roll_save.yaml` |

Filename conventions encode the recipe inline: `4f` = 4-frame context; `fsk5` = frame-skip 5; `ask1` = action-skip 1; `r224`/`r256` = resolution; `AdaLN` = conditioning; `depth6`/`depth12` = predictor depth; `2roll`/`1roll` = rollout-loss steps; `ftprop` = with proprioception; `noprop` = without; `2n`/`4n` = number of compute nodes.

### Repro plot scripts

`app/plan_common/plot/logs_plan_joint_per_design_choice.py` reproduces every paper figure (encoder comparison, predictor architecture, rollout steps, final baseline). Driven by YAML design-choice files under `app/plan_common/plot/local/design_choice_yamls/`.

### Training entrypoints

- Local single-GPU: `python -m app.main --fname <config.yaml> --debug`
- Distributed SLURM (from login node): `python -m app.main_distributed --fname <config.yaml> --account ... --qos ... --time ...`
- Auto-launches planning evals every `meta.eval_freq` epochs (uses `evals.separate: true/false`)

### Evaluation entrypoints

- Single GPU: `python -m evals.main --fname <config.yaml> --debug`
- Distributed: `python -m evals.main_distributed ...`
- Grid sweep: `python -m evals.simu_env_planning.run_eval_grid --env <env> --config <config.yaml>`
- Visualization notebook: `app/plan_common/notebooks/logs_planning_joint.ipynb`

### License

**CC-BY-NC 4.0** — **non-commercial** only. This is the practical blocker for any downstream commercial deployment of this code or these checkpoints; restricts the [JEPA project ladder](../syntheses/projects/jepa-project-ladder-rosorin-pro.md) and the [LeWM-on-Stretch / LeWM-on-ROSOrin-Pro feasibility analyses](../syntheses/projects/lewm-on-stretch-feasibility.md) to research / personal use. Third-party licenses tracked in `THIRD-PARTY-LICENSES.md`.

## Entities mentioned

- [JEPA-WMs](../entities/jepa-wms.md) — the model family this repo implements.
- [V-JEPA 2](../entities/v-jepa-2.md) — baseline (both fixed + original variants downloadable here).
- [DINO-WM](../entities/dino-wm.md) — baseline (reproduced checkpoints).
- [DINOv2](../entities/dinov2.md), [DINOv3](../entities/dinov3.md) — encoder backbones.
- [DROID](../entities/droid.md) — primary real-robot dataset (separate download via gsutil).
- [RoboCasa](../entities/robocasa.md) — kitchen-manipulation eval env (uses Basile-Terver fork).
- [Metaworld](../entities/metaworld.md) — 42-task manipulation eval.
- [PushT](../entities/pusht.md), [PointMaze](../entities/pointmaze.md) — 2D / nav benches.
- [Franka Panda](../entities/franka-panda.md) — real-robot platform.
- [Meta FAIR](../entities/meta-fair.md) — lab.
- [Basile Terver](../entities/basile-terver.md), [Adrien Bardes](../entities/adrien-bardes.md), [Yann LeCun](../entities/yann-lecun.md), [Jean Ponce](../entities/jean-ponce.md) — authors.
- [Hugging Face](../entities/hugging-face.md) — model + dataset hosting.

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) — the architecture this repo implements; design-axis lessons live on the concept page.
- [Learned latent space](../concepts/world-models/latent-space.md) — frozen DINOv2/v3 features as the predicted substrate.

## Open questions

- **CC-BY-NC blocker** for commercial use is unambiguous, but the **dataset re-hosts** (Push-T / PointMaze / Wall from `apple/ml-dino-wm`) inherit their original licenses — repo doesn't restate. Verify those before any downstream use.
- The `Basile-Terver/robosuite` and `Basile-Terver/robocasa` forks aren't versioned vs upstream in the README — open question how far they've diverged and whether upstream would accept them back.
- Repro guarantee — the README ships paper-config filenames but doesn't claim bit-exact reproducibility of Table 2 numbers. The `--debug` single-GPU path is for development, not paper reproduction.
- **No SLURM-free distributed-training path** beyond `--debug`; HPC users with non-SLURM clusters need to wire up their own launcher via `src/utils/cluster.py`. Affects anyone hoping to reproduce DROID-scale training on a non-SLURM cluster (cloud GPU rental, single multi-GPU box).

## Why it matters for the wiki

1. **Reproducibility surface** — gives the [JEPA-WMs entity](../entities/jepa-wms.md) a concrete "you can actually clone this and load the paper's winning checkpoints in 4 lines of Python" hook. Before this ingest, the wiki had paper-level claims but no operational recipe.
2. **The fixed V-JEPA-2-AC checkpoint is downloadable** — closes the loop on the [V-JEPA 2 entity's callout](../entities/v-jepa-2.md#why-it-matters) about the bug-fix retraining.
3. **License-scope evidence** for the [project-ladder](../syntheses/projects/jepa-project-ladder-rosorin-pro.md) and the [feasibility analyses](../syntheses/projects/lewm-on-stretch-feasibility.md) — CC-BY-NC 4.0 keeps downstream Stretch / ROSOrin Pro projects firmly in the research-and-personal-use lane.
4. **Operational details for the dependency stack** — DINOv3 manual install, MuJoCo 2.1 quirk for PointMaze, RoboCasa via forks, DROID via `gsutil` from Google Research bucket. These are the gotchas anyone reproducing the paper will hit.
