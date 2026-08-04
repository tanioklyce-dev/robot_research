---
title: "allenai/MolmoAct2-SO100_101 — Hugging Face model card"
type: source
url: https://huggingface.co/allenai/MolmoAct2-SO100_101
author: Ai2 (Allen Institute for AI)
affiliation: Ai2
published: 2026-05
ingested: 2026-08-03
venue: Hugging Face model hub
format: model card
license: Apache 2.0 (per the repo; subject to Ai2 Responsible Use Guidelines)
tags: [molmoact2, vla, so-arm101, so-100, checkpoint, deployment, flow-matching, lerobot, ai2, edge-inference, primary-source]
---

## Summary

The **SO-100/SO-101 fine-tuned checkpoint** of [MolmoAct2](../entities/molmoact2.md) — the only released MolmoAct2 variant targeting the low-cost arm class this wiki's own projects are built on ([SO-ARM101](../entities/so-arm101.md), [XLeRobot](../entities/xlerobot.md), [LeKiwi](../entities/lekiwi.md)). Its value to the wiki is not new capability claims (the card reports none) but **concrete deployment numbers** the [paper](molmoact2-paper.md) never gave: parameter count, memory footprint, and precision options.

> [!note] The card is thin by design
> No success rates, no benchmark table, no training-set size. It points at [Fang et al. 2026](molmoact2-paper.md) for all evaluation. What it adds is the **engineering envelope** — which is exactly what the wiki was missing.

## Key claims

### Identity and architecture
- **5B parameters**, Safetensors format.
- Built on **[Molmo2-ER](../entities/molmo2-er.md)**, "attaches a flow-matching continuous action expert that conditions on the VLM key-value cache through a per-layer connection" — an independent restatement of the [per-layer KV conditioning](../concepts/learning/per-layer-kv-conditioning.md) mechanism the wiki had only from the paper.
- Fine-tuned on **"the SO-100/101 mixture with absolute joint-pose control and annotated language instructions."**

> [!note] Absolute joint-pose control is a notable choice
> Not delta/relative end-effector actions — **absolute joint poses**. That matters for anyone porting: the action space is joint-space and absolute, so calibration and joint-limit agreement between the training rig and yours are load-bearing in a way relative-EE control would soften.

### Memory footprint — the numbers the wiki wanted

| Precision | VRAM |
|---|---|
| float32, with CUDA graph | **~26 GB** |
| float32, without CUDA graph | ~24 GB |
| **bfloat16** | **~16 GB** |

Dependencies: `torch`, `transformers`, `pillow`, `numpy`, `huggingface_hub`. Loaded through standard `transformers`:

```python
from transformers import AutoModelForImageTextToText
model = AutoModelForImageTextToText.from_pretrained(
    "allenai/MolmoAct2-SO100_101",
    trust_remote_code=True, device_map="auto")
```

### Intended use
"Use this checkpoint for SO-100/101 inference or for further fine-tuning." **Continuous action prediction is the primary mode**; discrete action prediction is retained "for compatibility" — consistent with the paper's finding that the continuous flow path is 3.94× faster than the discrete autoregressive one.

### Stated limitations
"Users should carefully validate model outputs before deployment… actions should be monitored through interpretable intermediate outputs… before execution on hardware." The interpretable-intermediates framing is the deployment-time expression of MolmoAct2's action-reasoning design.

## Entities mentioned
- [MolmoAct2](../entities/molmoact2.md) · [Molmo2-ER](../entities/molmo2-er.md) · [Ai2](../entities/ai2.md)
- [SO-ARM101](../entities/so-arm101.md) — the target hardware · [LeRobot](../entities/lerobot.md) — the data/training substrate (see the [repo](molmoact2-github-repo.md))

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) · [Flow matching](../concepts/learning/flow-matching.md) · [Per-layer KV conditioning](../concepts/learning/per-layer-kv-conditioning.md)

## Open questions

> [!warning] ~16 GB bf16 does not mean it fits a 16 GB Orin NX
> Jetson modules use **unified memory** shared between CPU and GPU, so a 16 GB Orin NX has meaningfully less than 16 GB available after the OS, camera pipeline, and ROS stack. A model whose *weights alone* want ~16 GB in bf16 is therefore **not a realistic Orin NX 16 GB target**, and the [XLeRobot compute page](../syntheses/platforms/jetson-onboard-compute-xlerobot.md)'s "3B-class VLAs become workable, if tight" verdict does not extend to this 5B checkpoint. AGX Orin 64 GB or [Thor](../entities/jetson-thor.md) 128 GB are the plausible edge targets. **This is inference from the stated footprint, not a measurement** — nobody has published MolmoAct2 on Jetson.
- **Still no throughput number outside a datacenter GPU.** The card gives memory, not Hz. The paper's 55.79 Hz is H100. See [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) — the gap narrows but does not close.
- **The SO-100/101 mixture is unquantified** — no hours, episodes, or task count for the fine-tuning data.
- **The paper's SO-100 number (56.7% zero-shot, +11.4 over in-house π0-SO100/101) has no stated N**, and this card does not supply one.
- Is the checkpoint SO-100-trained and SO-101-transferred, or trained on both? The single `SO100_101` name and "mixture" wording suggest both, but the split is unstated.

## Related sources
- [MolmoAct2 paper](molmoact2-paper.md) — all evaluation numbers; the card defers to it entirely.
- [MolmoAct2 GitHub repo](molmoact2-github-repo.md) — training, deployment, and the rest of the checkpoint family.
