---
title: LeWorldModel — train and run howto
type: synthesis
created: 2026-05-07
updated: 2026-05-07
tags: [leworldmodel, lewm, jepa, world-model, howto]
---

Practical recipe for training and running [[leworldmodel|LeWorldModel]] (LeWM) — the bits the [[leworldmodel-paper|LeWorldModel Paper]] doesn't spell out. Commands sourced from the official `lucas-maes/le-wm` repo README; the gotchas section below comes from a real install on Ubuntu/WSL2 + Python 3.10 + uv 0.11 in May 2026.

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

The naive command above hits four real problems on a current toolchain — see [Gotchas](#gotchas) below before running it.

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

The HF artifact is `weights.pt` (state dict) + `config.json` (Hydra-style spec). The `swm.policy.AutoCostModel` loader expects a full pickled stable-pretraining module saved as `*_object.ckpt` — a different format. **You must convert once before loading.**

```bash
hf download quentinll/lewm-pusht --local-dir "$STABLEWM_HOME/hf_pusht"
cd le-wm   # imports below need this on PYTHONPATH
python - <<'PY'
import json, torch, stable_pretraining as spt
from pathlib import Path
from jepa import JEPA
from module import ARPredictor, Embedder, MLP
import stable_worldmodel as swm

def strip_target(d):  # drop Hydra _target_/_partial_ keys + nested dicts
    return {k: v for k, v in d.items() if not k.startswith("_") and not isinstance(v, dict)}

src = Path(swm.data.utils.get_cache_dir(), "hf_pusht")
out = Path(swm.data.utils.get_cache_dir(), "pusht", "lewm_object.ckpt")
cfg = json.loads((src / "config.json").read_text())

encoder = spt.backbone.utils.vit_hf(
    cfg["encoder"]["size"], patch_size=cfg["encoder"]["patch_size"],
    image_size=cfg["encoder"]["image_size"], pretrained=False, use_mask_token=False,
)
mlp = lambda k: MLP(input_dim=cfg[k]["input_dim"], output_dim=cfg[k]["output_dim"],
                    hidden_dim=cfg[k]["hidden_dim"], norm_fn=torch.nn.BatchNorm1d)
model = JEPA(
    encoder=encoder,
    predictor=ARPredictor(**strip_target(cfg["predictor"])),
    action_encoder=Embedder(**strip_target(cfg["action_encoder"])),
    projector=mlp("projector"), pred_proj=mlp("pred_proj"),
)
model.load_state_dict(torch.load(src / "weights.pt", map_location="cpu", weights_only=False))
out.parent.mkdir(parents=True, exist_ok=True)
torch.save(model, out)
PY
```

Then load:

```python
import stable_worldmodel as swm
from jepa import JEPA              # noqa — needed so torch.load can unpickle
from module import ARPredictor, Embedder, MLP, SIGReg  # noqa

cost = swm.policy.AutoCostModel('pusht/lewm').to('cuda').eval()
cost.requires_grad_(False)
cost.interpolate_pos_encoding = True
```

The pusht model is **18M params** (paper headline of 15M is the encoder + predictor; full module incl. projectors is larger). Loads with 0 missing / 0 unexpected state-dict keys.

> [!note] The README's conversion script as published has a bug
> Without the `strip_target` helper the call fails with `TypeError: ARPredictor.__init__() got an unexpected keyword argument '_target_'`. The HF `config.json` includes Hydra `_target_` / `_partial_` keys that have to be filtered before being passed as kwargs.

## Gotchas

Real install snags as of May 2026 on Python 3.10 + uv 0.11 + Ubuntu/WSL2. None of these are documented in the upstream README; all four hit any fresh install.

### 1. `gym==0.21.0` has malformed PEP 440 metadata

`stable-worldmodel[env]` transitively pins `gym==0.21.0`, whose `setup.py` declares `opencv-python>=3.` (trailing dot — invalid PEP 440). uv refuses to parse it:

```
× Metadata for `gym` (v0.21.0) could not be parsed:
  after parsing `3`, found `.`, which is not part of a valid version
```

**Fix** — patch the sdist locally:

```bash
curl -sLO https://files.pythonhosted.org/packages/source/g/gym/gym-0.21.0.tar.gz
tar xzf gym-0.21.0.tar.gz
sed -i 's|opencv-python>=3\.|opencv-python>=3.0|' gym-0.21.0/setup.py
uv pip install "setuptools<66" "wheel<0.40"   # gym 0.21 also needs legacy setuptools
uv pip install --no-build-isolation ./gym-0.21.0
```

### 2. `gymnasium[all]` → `box2d-py 2.3.5` needs system `swig`

`stable-worldmodel[env]` pulls [[gymnasium|gymnasium]]`[all]`, which pulls `box2d-py==2.3.5`, which has no manylinux wheel for Python 3.10 and builds C extensions via SWIG. Without it:

```
error: command 'swig' failed: No such file or directory
```

**Fix** — install the system package (one-time):

```bash
sudo apt install -y swig
```

### 3. uv resolves `datasets` to 1.1.1 (2020-era) by default

`stable-pretraining` declares `datasets` with no version pin. uv's resolver picks the oldest compatible version — HuggingFace `datasets==1.1.1` from 2020 — which lacks `datasets.config` and breaks `stable_pretraining` import:

```
ImportError: cannot import name 'config' from 'datasets'
```

**Fix** — force a modern version after the main install:

```bash
uv pip install -U "datasets>=3.0"
```

### 4. The README conversion script for HF checkpoints has a bug

See the call-out under [Skip training — use pretrained](#skip-training--use-pretrained): you need `strip_target()` to filter Hydra `_target_` / `_partial_` keys from `config.json` before passing as kwargs.

## Caveats before committing time
- Benchmarks are 2D/3D control benches (PushT, cube, two-rooms, reacher), not real robots. The "scales to real deployment" question is open ([[leworldmodel-paper|LeWorldModel Paper]] open questions).
- Single-GPU, hours-scale training is for these tasks at their native resolution. No reported numbers for high-res or video-scale inputs.
- Reconstruction-free, reward-free, task-agnostic — but **task-conditioned via the planner cost**, not via an end-to-end policy. If you want a behavior-cloning-style "policy.act(obs)" interface, this isn't it.
- Different design point from [[v-jepa-2|V-JEPA 2]]: V-JEPA 2 = massive video pretraining + frozen encoder + post-training; LeWM = small, end-to-end pixel-trained, single-GPU.

## Sources
- `lucas-maes/le-wm` README — install/train/eval commands; HF→ckpt conversion script.
- `le-wm.github.io` — project page; HF dataset + checkpoint pointers.
- [[leworldmodel-paper|LeWorldModel Paper]] — model design, claims, benchmarks.
- Live install on 2026-05-07 (Python 3.10, uv 0.11, RTX 5070 WSL2): produced the four gotchas above and verified `AutoCostModel('pusht/lewm')` loads `quentinll/lewm-pusht` with 0 missing / 0 unexpected keys after conversion.
