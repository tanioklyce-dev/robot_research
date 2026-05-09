---
source_url: https://github.com/facebookresearch/vjepa2
collected: 2026-05-09
published: Unknown
author: Meta FAIR
affiliation: Meta FAIR
---

# vjepa2 GitHub README

V-JEPA 2 is Meta FAIR's self-supervised video learning framework using PyTorch. Enables video understanding, prediction, and planning through masked latent feature prediction trained on internet-scale video data.

## Model variants
- **V-JEPA 2**: ViT-L/H/g at 256–384px resolution
- **V-JEPA 2.1**: Improved recipe focusing on dense, temporally consistent features; ViT-B through ViT-G at 384px
- **V-JEPA 2-AC**: Action-conditioned variant for robot manipulation tasks

## Parameter range
80M to 2B parameters across variants.

## Key architecture
- Training via "masked latent feature prediction" — encoders and predictors learn from video through self-supervision
- V-JEPA 2.1 additions: dense predictive loss, deep self-supervision at multiple representation levels, multi-modal tokenizers

## Training details
- Pretraining: masked prediction objectives on video data + cooldown phase
- Action-conditioned post-training uses robot trajectory data (DROID: 62 hr Franka Panda)
- Supports local and distributed SLURM-based training

## Installation
```
conda create -n vjepa2-312 python=3.12
conda activate vjepa2-312
pip install .
```
Note: macOS users need alternative decord implementations due to platform incompatibility.

## Pretrained models
Available via PyTorch Hub and HuggingFace. Checkpoints range from 80M to 2B parameters.

## Benchmark results
- EK100: 39.7% (previous best: 27.6%)
- Something-Something v2: 77.3% (previous: 69.7%)
- Diving48: 90.2% (previous: 86.4%)
- Robot manipulation: 100% reach success; 60–80% grasp / pick-and-place success

## Evaluation
Probe-based: attentive classifiers on frozen features for video classification, action anticipation, video QA.

## License
Dual: MIT (majority) + Apache 2.0 (specific utility modules).
