---
title: SmolVLA
type: entity
subtype: model
created: 2026-05-25
updated: 2026-07-17
sources: 12
tags: [smolvla, vla, vision-language-action, flow-matching, hugging-face, lerobot, smolvlm-2, async-inference, community-datasets, so-arm101, affordable-vla]
---

**SmolVLA** — compact, efficient, open-source VLA from the [Hugging Face](hugging-face.md) [LeRobot](lerobot.md) team (Shukor, Aubakirova, Capuano, …, Wolf, [Cadene](remi-cadene.md); [June 2025](../sources/smolvla-paper.md)). **450 M params (main model)**, trained on **22.9 K episodes from 481 community HF datasets** (an order of magnitude less data than prior VLAs), deployable on consumer GPUs or CPUs. **Beats [π0](pi-zero.md) 3.5 B by +16.6 pts on real-world SO-100 multi-task** (78.3% vs 61.7%). Available as a [LeRobot](lerobot.md) checkpoint at [`lerobot/smolvla_base`](https://huggingface.co/lerobot/smolvla_base).

## Three contributions ([paper](../sources/smolvla-paper.md))

1. **Lightweight architecture** — SmolVLM-2 backbone (SigLIP + SmolLM2) + flow-matching action expert with **interleaved cross-attention + causal self-attention**. Uses VLM features from layer N = L/2 (halves compute). 64 visual tokens/frame, no tiling. Hidden size 0.75× VLM.
2. **Community-driven pretraining** — 481 HF community datasets, filtered + standardized (VLM-cleaned task annotations via `Qwen2.5-VL-3B-Instruct`; manual camera-view normalization to OBS_IMAGE_1/2/3 = top/wrist/side).
3. **Asynchronous inference stack** — decouples action execution from chunk prediction via a RobotClient (consumes queue) + PolicyServer (predicts next chunk, possibly remote). Threshold `g ∈ [0, 1]` controls when to trigger inference; observation-similarity filter avoids redundant inferences. **The practical-deployment piece most VLA papers skip.**

## Architectural contrast with π0

| | π0 | SmolVLA |
|---|---|---|
| Total params | 3.3 B | **0.24 / 0.45 / 2.25 B** |
| Base VLM | PaliGemma 3 B | SmolVLM-2 (~0.4 B) |
| Action expert attention | Full bidirectional SA | **Interleaved CA + causal SA** |
| Action expert hidden size | matches VLM | **0.75× VLM** |
| VLM features read at | last layer | **layer N = L/2** |
| Visual tokens/frame | (paper-dependent) | **64 (pixel-shuffle, no tiling)** |
| Training data | 10,000 hr in-house teleop + OXE/DROID/Bridge | **22.9 K episodes from 481 HF community datasets** |
| Inference stack | sync (chunk-then-execute) | **async server/client + similarity filter** |

## Headline results ([paper](../sources/smolvla-paper.md))

### Simulation
- **LIBERO** (avg): SmolVLA-0.45 B = **87.3** vs π0-3.3 B = 86.0 vs OpenVLA-7 B = 76.5 vs Diffusion Policy = 72.4.
- **Meta-World** (avg): SmolVLA-0.45 B = **57.3** vs π0-3.5 B = 50.5 vs TinyVLA = 31.6.
- SmolVLA-2.25 B further pushes LIBERO to 88.75 and Meta-World to 68.24.

### Real-world SO-100 multi-task
- ACT (single-task) = 48.3 / π0-3.5 B (multi-task) = 61.7 / **SmolVLA-0.45 B (multi-task) = 78.3**.
- SmolVLA wins by **+16.6 pts** despite ~7× fewer params.

### Real-world SO-101 single-task pick-place-lego (OOD — not in pretrain)
- ACT = 70 in-distribution / 40 OOD.
- **SmolVLA-0.45 B = 90 in-distribution / 50 OOD**.

### Effect of pretraining
- No pretrain → 51.7 real-world avg; with community-data pretrain → 78.3 (**+26.6 pts**).

## Why it matters in this wiki

1. **The affordable-VLA reference.** SmolVLA + [LeRobot](lerobot.md) + [SO-100/101](so-arm101.md) is now the canonical sub-$1k VLA stack. Runs on [XLeRobot](xlerobot.md), [LeKiwi](lekiwi.md), [Grievous](grievous.md), and the SO-ARM101 hobbyist tier.
2. **"Smaller + community-data + clever attention > bigger + corporate-data"** is the wiki's first clean evidence of this pattern at the VLA scale. Same direction as the [Mobile ALOHA co-training pattern](../sources/mobile-aloha-paper.md), [RUM data-diversity finding](robot-utility-models.md), and [EgoScale's human-video pretraining](../sources/egoscale-paper.md) — all of which favor data composition over raw scale.
3. **Async inference is now a first-class VLA design topic.** SmolVLA establishes the server/client + threshold-`g` + similarity-filter pattern as a reusable primitive. The [LeRobot tutorial](../sources/lerobot-robot-learning-tutorial.md) elevates async inference to its own section.
4. **LeRobot ecosystem flagship.** Together with [`lerobot/pi0_base`](pi-zero.md), `lerobot/smolvla_base` is one of the two named VLA exemplars in the official [LeRobot tutorial](../sources/lerobot-robot-learning-tutorial.md).

## Code

- Checkpoint: [`lerobot/smolvla_base`](https://huggingface.co/lerobot/smolvla_base) on Hugging Face.
- Async variant: [`fracapuano/smolvla_async`](https://huggingface.co/fracapuano/smolvla_async).
- Datasets: 481 HF community datasets (full list in paper Appendix A.1).
- Real-world eval datasets: `lerobot/svla_so100_pickplace`, `lerobot/svla_so100_stacking`, `lerobot/svla_so100_sorting`, `lerobot/svla_so101_pickplace`.

## Related

- [π0](pi-zero.md) — primary VLA baseline; beaten on real-world SO-100 multi-task.
- [ACT](act.md) — secondary baseline.
- [LeRobot](lerobot.md) — framework.
- [SO-ARM101](so-arm101.md) — primary hardware.
- [Hugging Face](hugging-face.md) — primary lab.
- [Remi Cadene](remi-cadene.md) — LeRobot lead; SmolVLA co-author.
- [VLA models](../concepts/learning/vla-models.md) — broader concept.
- [Diffusion Policy](diffusion-policy.md) — uses DDPM; SmolVLA uses flow matching as the alternative.

## Mentioned in

- [SmolVLA Paper](../sources/smolvla-paper.md) — primary source.
- [Robot Learning: A Tutorial (LeRobot)](../sources/lerobot-robot-learning-tutorial.md) — canonical VLA code example.
- [π0 Paper](../sources/pi-zero-paper.md) — referenced via SmolVLA-as-contrasting-design ingestion.
- [π0 entity](pi-zero.md) — direct comparison.
- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — 450 M params, 1.75 GB peak mem A100, **99.2 ms** RTX 4090 latency; **only frontier VLA that runs on CPU** (2028 ms ± 303, 2% timeout). Async vs sync benchmark (Appendix E Table 5) reproduces SmolVLA's own async-inference results on SO-100 (1.8 → 3.8 cubes in 60s with async).
- [VLA-0 paper](../sources/vla-0-paper.md) — used as the real-world SO-100 baseline; **[VLA-0](vla-0.md) beats SmolVLA by 12.5 pts** on 4 real tasks despite SmolVLA's large-scale SO-100 pretraining (VLA-0 trained from scratch). On LIBERO, VLA-0's 94.7 avg > SmolVLA-2.25B's 88.8.
