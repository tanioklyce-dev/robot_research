---
title: "Jalapeño's first results show industry-leading speed and efficiency in AI inference (OpenAI, Aug 2026)"
type: source
url: https://openai.com/index/jalapeno-first-results/
local_path: raw/2026-08-25-openai-jalapeno-first-results.md
sha256: 792bc2a35207f0cdb16000ab8df3760a2d923b1da55219542c5d5303ca3e46c0
author: "OpenAI (no individual authors)"
affiliation: OpenAI
published: 2026-08-25
venue: "OpenAI blog — Engineering / Company post; charts and an appendix of InferenceX results"
format: web (vendor blog; captured via Wayback snapshot 2026-09-11 — openai.com 403s non-browser fetches; charts lost, labels kept)
tags: [openai, jalapeno, inference-chip, custom-silicon, inference, latency, throughput-per-watt, InferenceX, GB200, GB300, nvidia, agents, codex, gpt-astra, ai-designed-hardware, vendor-source]
ingested: 2026-09-13
---

# Jalapeño's first results show industry-leading speed and efficiency in AI inference

## Summary

**OpenAI's first custom inference chip, benchmarked by OpenAI against NVIDIA's GB200 and GB300, on a public benchmark, with the numbers normalised by each package's rated power.** On SemiAnalysis's **InferenceX** (8k-in / 1k-out, three open-weight models: GPT-OSS 120B, DeepSeek R1 670B, Kimi K2.5 1T), Jalapeño is reported at **1.5–1.9× more throughput per kilowatt at peak** and **1.7–3.6× lower end-to-end latency** than the comparison system, with **2.1–4.1× higher performance for "highly interactive" workloads**. The chip is rated at **700 W** (measured ≤550 W on these runs) against 1,200 W for GB200 and 1,400 W for GB300, and the post argues that **performance per watt, not per chip, is the right standard**. Design-to-tapeout took **nine months**, with AI in the loop; Codex with GPT-Astra brought three models not in the original plan to high performance in two months and wrote attention and MoE kernels **1.5–1.8× faster than the human-expert versions** for selected blocks. Deployment inside OpenAI's fleet is planned *"by the end of the year"*; Gen 2 is *"deep in development."*

> [!warning] Vendor benchmark of the vendor's own chip
> Every number is OpenAI's, on a benchmark OpenAI chose, against a *"comparison system"* the body never names beyond package TDP (the appendix labels say GB200 for GPT-OSS and GB300 for the two larger models). The normalisation is by **rated** TDP — conservative for Jalapeño (rated 700 W, measured ≤550 W) but also applied to NVIDIA's rating, so the actual power draw of either side on these runs is not published. The largest headline multiples (**53.7×, 104.3×, 56.1×** "more throughput at previous TBT") are read at the comparison system's own minimum time-between-tokens, i.e. at an operating point the other system barely reaches; the per-watt peak (1.5–1.9×) and end-to-end latency (1.7–3.6×) figures are the ones comparable to ordinary practice. Nothing is reproducible from outside OpenAI, and Broadcom — named as the fabrication partner in every secondary — is not mentioned in the post.

## Key claims

### Appendix results (InferenceX, nominal 8k/1k, STP)

| Model | Comparison (TDP) | Peak mixed tok/s per kW | End-to-end latency | Min TBT (tok/s/user) | Throughput at the comparison's previous-best TBT |
|---|---|---|---|---|---|
| GPT-OSS 120B | GB200 (1,200 W) | **85,448 vs 44,960 (≈1.9×)** | **1.03 s vs 1.80 s (≈1.7×)** | 0.69 vs 1.87 ms (1,459 vs 535 tok/s/user, ≈2.7×) | 22,935 vs 427 per kW (≈53.7×) at 535 tok/s/user |
| DeepSeek R1 670B, MXFP4 | GB300 (1,400 W) | 19,641 vs 11,781 (≈1.7×) | **1.65 s vs 5.99 s (≈3.6×)** | 1.43 vs 5.90 ms (700 vs 169, ≈4.1×) | 12,258 vs 118 (≈104.3×) at 169 tok/s/user |
| Kimi K2.5 1T, MXFP4 | GB300 (1,400 W) | 18,195 vs 11,862 (≈1.5×) | 1.56 s vs 5.31 s (≈3.4×) | 1.44 vs 5.48 ms (694 vs 182, ≈3.8×) | 6,744 vs 120 (≈56.1×) at 182 tok/s/user |

- Jalapeño package TDP 700 W; *"measured sustained power remained at or below 550 watts on the workloads tested."*
- *"In our internal testing, Jalapeño's advantage widened further on frontier OpenAI models"* — no numbers.
- Method: *"a matched user experience, measuring how much useful AI work each system can complete per unit of power while meeting the latency customers and interactive agents require."* Agents are the stated reason latency matters: *"delays can compound across an entire task."*

### Architecture claims

- Designed for the two inference phases with different bottlenecks — prefill (compute-bound) and decode (memory-bandwidth-bound) — plus communication; the aim is *"to minimize data movement and communication delays,"* keeping model state including the **KV cache explicitly placed and local** and letting *"the entire workload remain within one connected system"* through a large network domain.
- *"A balanced and fungible accelerator that can support changing model architectures, excel at both prefill and decode, and adapt as the balance between them changes."*
- The three tiers it claims to move: ultra-fast-mode inference at fast-mode efficiency, fast at batched efficiency, and higher batched efficiency.

### AI in the loop

- *"Initial design to tapeout in nine months"*, with AI *"exploring implementations, shortening design, measurement, and verification loops"* and optimising arithmetic circuits.
- The chip was designed *"as a clear, predictable programming target for both humans and AI"* — local tensors, explicit communication, predictable synchronisation — so AI can do the mapping, placement and scheduling.
- **Codex + GPT-Astra**: three open-weight models outside the production plan brought to high performance in two months; **selected GPT-OSS attention and MoE blocks 1.5–1.8× faster than human-expert implementations** — *"those figures apply to the selected blocks, not the full model."*

### Roadmap and posture

- Deploy in OpenAI's own infrastructure by end of 2026; *"the first generation of a multigenerational roadmap"*, Gen 2 and Gen 3 in progress.
- *"We will continue to widely deploy accelerators from NVIDIA and other partners for both training and inference workloads."*
- Framed as *"a broader full-stack advantage"*: models, products, serving software, chips, memory, networking and systems designed together; and as **operating leverage** — revenue growing faster than cost to serve.

## Why a robotics wiki holds this

- **The LLM-in-the-loop latency assumption is moving.** The [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) puts frontier-LLM planning at 0.2–0.4 Hz from measured 2–8 s text responses. Jalapeño's reported **1,459 tokens per second per user** on a 120B model and 1.03 s end-to-end for an 8k/1k request are cloud figures, not edge ones, but they are the kind of number that changes whether a language planner can sit inside a control loop rather than above it. They are also vendor-reported and unverified.
- **Who owns inference silicon** is an industry-map fact: the wiki's compute pages are NVIDIA-centric ([Thor](../entities/jetson-thor.md), [DGX Spark](../entities/dgx-spark.md), the [GPU rental landscape](../syntheses/platforms/nvidia-gpu-rental-landscape.md)). A frontier lab benchmarking its own chip against GB200/GB300 in public, on a third-party benchmark, is a data point the [industry map](../syntheses/society/robot-ai-industry-map.md) did not have.
- **AI-designed, AI-programmed hardware** with a stated speedup over expert kernels is the same claim shape as the wiki's [Codex](../entities/openai.md)-as-harness thread, now applied to silicon.

## Entities mentioned

- [OpenAI](../entities/openai.md) — the vendor; GPT-OSS, GPT-Astra, Codex named. [Jalapeño](../entities/openai-jalapeno.md) — the chip.
- [NVIDIA](../entities/nvidia.md) — GB200 and GB300 as the comparison systems (appendix labels); NVIDIA accelerators to remain deployed.
- SemiAnalysis (InferenceX benchmark), DeepSeek, Moonshot (Kimi) — no pages. Broadcom — not in the post.

## Concepts touched

- [Control-rate ladder](../syntheses/platforms/control-rate-ladder.md) — per-user token rate as a planner-latency input.
- [LLM-agent architecture](../syntheses/agents/llm-agent-architecture-across-stacks.md) — the "delays compound across steps" argument for agent latency.

## Open questions

- **What is the comparison system, exactly** — node configuration, software stack, precision, batch — and who ran the InferenceX numbers for the NVIDIA side?
- **Measured power** on both sides, rather than rated TDP.
- **Frontier-model results** — claimed to widen the gap, not shown.
- **Availability**: internal deployment only; nothing about external sale or API-level latency changes.
- **Broadcom's role** and the process node — secondaries say Broadcom; the post says nothing.
