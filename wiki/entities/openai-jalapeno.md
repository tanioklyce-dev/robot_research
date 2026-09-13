---
title: Jalapeño (OpenAI inference chip)
type: entity
subtype: hardware
created: 2026-09-13
updated: 2026-09-13
sources: 1
tags: [hardware, inference-chip, custom-silicon, openai, accelerator, datacenter]
---

**Jalapeño** — [OpenAI](openai.md)'s first custom inference accelerator, announced before August 2026 and benchmarked by OpenAI on 2026-08-25 ([first results](../sources/openai-jalapeno-first-results.md)). Package TDP **700 W** (≤550 W measured); on SemiAnalysis's InferenceX with GPT-OSS 120B, DeepSeek R1 670B and Kimi K2.5 1T it is reported at **1.5–1.9× throughput per kW** and **1.7–3.6× lower end-to-end latency** than [NVIDIA](nvidia.md) GB200 / GB300 at rated TDP, and up to **1,459 tokens/s per user** on the 120B model. Designed for prefill and decode in one architecture with locally placed KV cache and a large network domain; nine months from design to tapeout with AI assistance; kernels partly written by Codex with GPT-Astra. Internal deployment planned by end of 2026; Gen 2 and Gen 3 in progress. All figures vendor-reported.

## Related

- [OpenAI](openai.md) · [NVIDIA](nvidia.md) · [DGX Spark](dgx-spark.md), [Jetson Thor](jetson-thor.md) (the wiki's NVIDIA compute references)
- [Control-rate ladder](../syntheses/platforms/control-rate-ladder.md)

## Mentioned in

- [Jalapeño's first results (OpenAI, 2026-08-25)](../sources/openai-jalapeno-first-results.md)

## Open questions / TBD

- Fabrication partner and node (secondaries say Broadcom; not in the post); comparison-system configuration; measured rather than rated power; any external availability.
