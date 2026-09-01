---
title: Microsoft
type: entity
created: 2026-08-31
updated: 2026-08-31
sources: 7
tags: [microsoft, company, research-lab, lora, florence-2, coco, msr]
---

**Microsoft** — US software company whose research arm (Microsoft Research, MSR) is the origin of several methods and datasets this wiki depends on, even though Microsoft has no robotics program covered here. It appears in this wiki almost entirely as a **producer of substrate**: the adaptation method, the VLM backbone, and the detection benchmark that other people's robots are built on.

## What this wiki actually uses from Microsoft

- **[LoRA](../concepts/learning/low-rank-adaptation.md)** — Hu, Shen, Wallis, Allen-Zhu, Li, Wang, Wang & Chen, 2021 ([paper](../sources/lora-paper.md), ICLR 2022). Low-rank adaptation of frozen weights. **Every VLA fine-tune in this wiki is a LoRA fine-tune.** Reference implementation released as `microsoft/LoRA`.
- **[Florence-2](florence-2.md)** — unified prompt-conditioned vision-language model (Xiao et al., 2024), trained on FLD-5B. The vision-language encoder inside **[X-VLA](x-vla.md)**, the 0.9 B model that took SOTA on five of six benchmarks ([X-VLA paper](../sources/xvla-paper.md)).
- **MS COCO** — the detection/segmentation benchmark and its evaluation protocol ([COCO detection eval](../sources/coco-detection-eval.md)); the mAP@0.5:0.95 convention that edge-perception results in this wiki are quoted in.
- **DeBERTa / GPT-2-era baselines** — the models LoRA validated against; DeBERTa-XXL is Microsoft's.

## Peripheral appearances

- **[DIAMOND](../sources/diamond-paper.md)** — two of the authors (Tim Pearce, François Fleuret) are MSR; the diffusion world model that runs as a playable Atari/CS:GO engine.
- **Orca** — GPT-4 reasoning-trace SFT dataset, surveyed in [Wolfe's SFT overview](../sources/wolfe-sft-blog.md).
- **Presidio** — PII detection, listed among [NeMo Guardrails](nemo-guardrails.md)' integrations.
- **Customer of [Goodfire](goodfire.md)** — named in the Series B announcement ([source](../sources/goodfire-series-b.md)).

> [!warning] Microsoft telemetry as a measurement instrument
> The [AI Index 2026](../sources/stanford-hai-ai-index-2026.md)'s country-level AI-adoption figure (§4.3, Fig. 4.3.10) is **Microsoft product telemetry**, not a population survey — a provenance the report's April edition described differently and corrected in the June re-export. Telemetry counts accounts touching Microsoft AI surfaces, so it measures Microsoft's distribution as much as a country's adoption. Treat any "national AI adoption" number sourced this way as a market-share proxy.

## Mentioned in

- [LoRA paper](../sources/lora-paper.md) — all eight authors.
- [X-VLA paper](../sources/xvla-paper.md) — via Florence-2.
- [COCO detection eval](../sources/coco-detection-eval.md)
- [DIAMOND paper](../sources/diamond-paper.md)
- [Stanford HAI AI Index 2026](../sources/stanford-hai-ai-index-2026.md)
- [Wolfe — SFT blog](../sources/wolfe-sft-blog.md)
- [Goodfire Series B](../sources/goodfire-series-b.md)
- [NeMo Guardrails library overview](../sources/nemo-guardrails-library-overview.md)
