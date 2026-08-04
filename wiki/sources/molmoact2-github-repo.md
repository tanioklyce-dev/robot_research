---
title: "allenai/molmoact2 — GitHub repository"
type: source
url: https://github.com/allenai/molmoact2
author: Ai2 (Allen Institute for AI)
affiliation: Ai2
published: 2026-05
ingested: 2026-08-03
venue: GitHub
format: code repository / README
license: Apache 2.0 (research and educational use per Ai2 Responsible Use Guidelines)
tags: [molmoact2, vla, codebase, lerobot, maniskill, deployment, fastapi, so-arm101, yam, droid, ai2, edge-inference, primary-source]
---

## Summary

The **MolmoAct2 codebase** — checkpoints, datasets, training workflows, simulation evaluation, and deployment servers. Ingesting it closes a [backlog item](../backlog.md) open since 2026-07-28 ("repo IDs are now recorded but no codebase ingest exists").

The headline finding for this wiki is architectural rather than scientific: **MolmoAct2 ships as a [LeRobot](../entities/lerobot.md) application.** Datasets are in **LeRobot v3.0 format**, LeRobot is vendored as a **git submodule**, and training runs through **LeRobot workflows**. Ai2's fully-open VLA is not a parallel stack to the one this wiki's projects already use — it *is* that stack, which materially lowers the cost of trying it on an [SO-ARM101](../entities/so-arm101.md)-class arm.

## Key claims

### The full checkpoint family

| Kind | Checkpoints |
|---|---|
| **Base** | MolmoAct2, MolmoAct2-Think, MolmoAct2-Pretrain, [Molmo2-ER](../entities/molmo2-er.md) |
| **Fine-tuned** | MolmoAct2-DROID ([Franka](../entities/franka-panda.md)), MolmoAct2-BimanualYAM ([YAM](../entities/yam.md)), **[MolmoAct2-SO100_101](molmoact2-so100-101-model-card.md)**, MolmoAct2-LIBERO, MolmoAct2-Think-LIBERO |

**Stated porting guidance:** start "from fine-tuned checkpoints if your embodiment is similar to Bimanual YAM, DROID Franka, or SO-100/SO-101," otherwise from the base checkpoint. This is the clearest statement in the wiki of how Ai2 expects cross-embodiment transfer to actually be done — *pick the nearest embodiment's checkpoint*, not the generalist one.

### Memory requirements — and a large per-embodiment spread

| Deployment | float32 | bfloat16 |
|---|---|---|
| **DROID** (Franka) | **~88 GB** | ~16 GB |
| **YAM** (bimanual) | ~26 GB | **under 16 GB** |

- Tested on an **NVIDIA RTX A6000**; **Intel XPU support** available.
- The DROID float32 figure (~88 GB) is **3.4× the YAM figure** for the same base model — presumably camera count and context length. Worth noting that "MolmoAct2 needs X GB" is not a single number; it depends on the embodiment config.

> [!note] No Jetson anywhere in the repo
> Supported/tested hardware is RTX A6000 and Intel XPU. There is **no Jetson build, benchmark, or mention** — so the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md)'s "single most valuable missing measurement" (a 2026-class VLA on Thor) remains missing, and MolmoAct2 does not ship anything that would make it easy.

### Deployment architecture
- **Two FastAPI inference servers** — DROID on port 8000, YAM on port 8202. A client/server split, i.e. the model is expected to run off-robot with the robot as a client. That is the same architecture as the wiki's own [fleet framework](../syntheses/projects/fleet-agentic-framework.md) and [ROS2-MCP](../entities/ros2-mcp-server.md) work.
- **Out-of-the-box deployment** claimed for **SO-100, Bimanual YAM, and Franka DROID**.
- Sim evaluation for DROID and Bimanual YAM on **[ManiSkill](../entities/maniskill.md)** — notable because the paper's headline sim benchmark is [LIBERO](../entities/libero.md); ManiSkill is the repo-level eval harness.

### Toolchain
`uv` package manager with pinned dependencies, **PyTorch CUDA-12.1**, transformers, FastAPI. The CUDA-12.1 pin is worth flagging for Jetson users — JetPack ships its own CUDA, and a pinned desktop CUDA wheel set is a common porting friction point.

### On the mechanisms the wiki wanted grounded
The README mentions **"depth-token reasoning"** for MolmoAct2-Think but **does not detail per-layer KV conditioning or the FAST/OpenFAST tokenizer**. So the backlog item's stated goal — "ground the [per-layer KV conditioning](../concepts/learning/per-layer-kv-conditioning.md) and [adaptive-depth](../concepts/learning/adaptive-depth-reasoning.md) mechanisms in runnable code" — is **only partially met by the README**; it would need reading the source, not the docs.

## Entities mentioned
- [MolmoAct2](../entities/molmoact2.md) · [Molmo2-ER](../entities/molmo2-er.md) · [Ai2](../entities/ai2.md)
- [LeRobot](../entities/lerobot.md) — submodule, data format, and training workflow · [ManiSkill](../entities/maniskill.md) — sim eval
- [SO-ARM101](../entities/so-arm101.md) · [YAM](../entities/yam.md) · [Franka Panda](../entities/franka-panda.md) · [DROID](../entities/droid.md) · [LIBERO](../entities/libero.md)

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) · [Per-layer KV conditioning](../concepts/learning/per-layer-kv-conditioning.md) · [Adaptive-depth reasoning](../concepts/learning/adaptive-depth-reasoning.md) · [Flow matching](../concepts/learning/flow-matching.md)

## Open questions
- **No Jetson support or benchmark** — the highest-value missing measurement in the wiki's edge thread stays missing.
- **Per-layer KV conditioning and OpenFAST are undocumented in the README** — grounding them needs a source-level read, which this ingest did not do.
- **No throughput figures in the repo** at all; memory only. The 55.79 Hz H100 number remains paper-only.
- **What does "out-of-the-box deployment for SO-100" mean operationally** — which cameras, what calibration, what control rate? The repo asserts support; the card gives no rate.
- The **DROID ~88 GB float32** figure is unexplained and worth confirming before anyone budgets hardware from it.

## Related sources
- [MolmoAct2 paper](molmoact2-paper.md) — the science; this repo is its artifact.
- [MolmoAct2-SO100_101 model card](molmoact2-so100-101-model-card.md) — the checkpoint most relevant to this wiki's hardware.
