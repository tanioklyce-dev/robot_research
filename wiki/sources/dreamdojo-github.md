---
title: "NVIDIA/DreamDojo — DreamDojo training, distillation and evaluation code (GitHub README)"
type: source
url: https://github.com/NVIDIA/DreamDojo
fetch_url: https://raw.githubusercontent.com/NVIDIA/DreamDojo/main/README.md
local_path: raw/2026-11-13-dreamdojo-github-readme.md
sha256: 282a66f968095ca8482176cfd027d7602379ff646885dd9a42ac8e485d375015
local_path_docs: raw/2026-11-13-dreamdojo-github-docs.md
author: NVIDIA GEAR (DreamDojo authors)
published: 2026-02-09 (repo created; last commit 02f119b, 2026-03-21)
venue: GitHub repository (Apache-2.0 code)
format: README (3.2 KB) plus seven docs pages (SETUP, LAM, PRETRAIN, POSTTRAIN, DISTILL, EVAL, ISSUES), saved together as a second raw file
license: Apache-2.0 (code); weights on Hugging Face under the NVIDIA Open Model License
tags: [dreamdojo, nvidia-gear, world-model, cosmos, open-weights, apache-2, h100, distillation, self-forcing, latent-action, gr1, unitree-g1, agibot, yam, repo-health]
ingested: 2026-11-13
---

## Summary

**The repo releases all of [DreamDojo](../entities/dreamdojo.md)'s training code, but not the fast model the paper is known for.** It holds code for latent-action-model training, pretraining, post-training, distillation and evaluation, built on a Cosmos-Predict2.5 codebase. It is tested only on the NVIDIA H100 80 GB. The README's release log lists pretraining and post-training code, all 2B and 14B checkpoints, and the GR-1 post-training data, all on 2026-02-18. The distillation pipeline arrived later, in the last commit (2026-03-21), and **no distilled checkpoint has been published**. The 10 FPS real-time model therefore has to be distilled by the user. Open issues report that distilled output is garbled, and that the distillation code needs a library version the pinned install can't provide. **No maintainer has replied to any of the open issues checked, and there have been no commits since March.**

## Key claims

### What is released (README, docs)
- **Code**, Apache-2.0, in seven stages: setup (`install.sh`, uv), latent-action model, pretraining, post-training, distillation, evaluation, troubleshooting.
- **Checkpoints** on [Hugging Face](https://huggingface.co/nvidia/DreamDojo): `2B_pretrain` and `14B_pretrain` (both at step 140,000), post-trained versions for GR-1, G1, AgiBot and YAM at each size, and `LAM_400k.ckpt`. These are the full diffusion "teacher" models. The model card's licence is the NVIDIA Open Model License.
- **Data**: only the GR-1 post-training set, plus three evaluation sets, In-lab, EgoDex and DreamDojo-HV ([HF](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-GR00T-Teleop-GR1), CC BY-NC 4.0). The LAM config ships with the GR-1 data only. Users add their own video folders.

### Hardware and setup (SETUP, PRETRAIN, ISSUES)
- **"Tested with NVIDIA H100 80GB."** No other GPU is mentioned.
- The pretraining and LAM scripts assume one node with 8 GPUs. A multi-node LAM launcher is included.
- ISSUES lists six environment variables to set, mostly NCCL timeouts and EFA/RDMA settings, warning that leaving them out "may cause unstable training performance." This points to AWS-style multi-node clusters.

### Action space (POSTTRAIN)
- **One 384-dimensional action input is shared by all embodiments.** Each robot gets a fixed slice: GR-1 [0, 29), Manus-glove-retargeted GR-1 [29, 58), Unitree G1 [58, 101), **bimanual YAM [101, 147)**, i.e. 46 dimensions, AgiBot [147, 169), reserved [169, 220), MANO hand actions [220, 352), latent actions [352, 384).
- Adding a new robot therefore means fitting it into the reserved 51 dimensions or retraining the first projection layer. The docs say this layer can be shrunk after post-training.
- Post-training configs exist for GR-1, G1, AgiBot and YAM at 480×640.

### Distillation (DISTILL)
- **Three stages:** teacher generation (precomputed denoising targets), warmup (the causal student matches the teacher), then Self-Forcing with DMD (Distribution Matching Distillation), where the student trains on its own rollouts.
- **Two inference modes:** offline generation from recorded action sequences, and real-time teleoperation from a starting frame and live or file actions at a 10 FPS target (`launch_student_inference_teleop.sh`).

### Evaluation (EVAL)
- **Evaluation compares generated video with recorded video** for post-trained checkpoints: 49-frame clips, 100 samples, the three held-out sets above. It can follow a run live and score new checkpoints as they appear.
- The README and docs give no command for **policy evaluation or model-based planning**, the paper's two headline uses. The tree contains GR00T-specific inference code (`inference_gr00t.py`, `exp_2B_action_conditioned_rectify_flow_gr00t.py`) but no documentation for it. The multi-view DreamDojo variant that [GR00T 2](gr00t-2-whitepaper.md) used for RL isn't in this repo.

### Repo health (GitHub API, 2026-11-13)
- 1,133 stars, 82 forks, 19 open issues. The last commit is 02f119b, "Add distillation", 2026-03-21.

| Issue | Opened | Problem | Maintainer reply |
|---|---|---|---|
| [#11](https://github.com/NVIDIA/DreamDojo/issues/11) | 2026-04-02 | Distilled student checkpoint not on HF; the inference scripts expect one | None |
| [#16](https://github.com/NVIDIA/DreamDojo/issues/16) | 2026-06-04 | The causal student requires `natten>=0.21.5`, but the install pins torch 2.7 + natten 0.21.0 | None |
| [#22](https://github.com/NVIDIA/DreamDojo/issues/22) | 2026-08-16 | Garbled video after following DISTILL.md | None |
| [#23](https://github.com/NVIDIA/DreamDojo/issues/23) | 2026-08-27 | Possible reshape bug mixing latent actions across samples during pretraining | None |
| [#4](https://github.com/NVIDIA/DreamDojo/issues/4) | 2026-03-09 | `eval.sh` still downloads Cosmos-Predict2.5 weights; the pinned HF revision ID doesn't exist | Users posted a workaround |

> [!warning] Unconfirmed reports
> These are user reports with no maintainer reply. The wiki hasn't reproduced any of them. #23 matters most if confirmed: it would affect how the latent-action conditioning was trained in the released pretrained checkpoints. Its claim that latent actions match ground-truth actions rests on the paper's Table 2, which used NVIDIA's own runs.

## Entities mentioned
- [DreamDojo](../entities/dreamdojo.md), [NVIDIA GEAR](../entities/nvidia-gear.md), [NVIDIA Cosmos](../entities/nvidia-cosmos.md)
- [Fourier GR-1](../entities/fourier-gr-1.md), [Unitree G1](../entities/unitree-g1.md), [AGIBOT](../entities/agibot.md), [YAM](../entities/yam.md), [EgoDex](../entities/egodex.md)

## Concepts touched
- [World-model simulators](../concepts/world-models/world-model-simulators.md): what can actually be run, not what the paper shows.
- [Cross-embodiment transfer](../concepts/learning/cross-embodiment.md): one shared action vector with fixed per-robot slices, a simple alternative to per-embodiment heads.

## Open questions
- **Will a distilled checkpoint ship?** Without one, the paper's real-time claim is reproducible only by running the three-stage distillation, and the one public attempt (#22) failed.
- **Is #23 a real bug?** If so, do the released checkpoints carry it?
- **Hardware below the H100 80 GB.** Can the 2B teacher run inference on an RTX 4090 or 5090, or on a Jetson? Nothing in the repo says.
- **Where is the policy-evaluation and planning code?** It seems to be internal, as is GR00T 2's multi-view adaptation.
