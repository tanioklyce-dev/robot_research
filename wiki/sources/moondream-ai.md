---
title: Moondream — project site, open models, and the Photon hardware ladder (moondream.ai)
type: source
url: https://moondream.ai/
author: M87 Labs (project started by Vikhyat Korrapati)
published: 2023-12-29 (repo created; site current as of ingest; repo last pushed 2026-04-20)
ingested: 2026-08-13
license: Apache-2.0 (open weights); Photon and Lens are commercial products
tags: [moondream, vlm, small-vlm, pointing, object-detection, segmentation, edge-inference, jetson, photon, latency-benchmark, open-weights, vendor-benchmark, primary-source]
---

## Summary

**Moondream** — *"a tiny vision language model that kicks ass and runs anywhere"* — is an Apache-2.0 open-weights VLM family from M87 Labs, wrapped in a commercial stack: **Photon** (inference engine), **Lens** (fine-tuning), and **Moondream Cloud** (hosted API). **9,963★**, **5M+ monthly downloads**. Its five operations — **Query, Caption, Detect, Point, Segment** — include the two that matter most for robotics grounding, and Photon 2.0 is now explicitly marketed as an *"inference engine for Physical AI."*

Ingested to close the last of the [lint punch list](../backlog.md)'s §6 knowledge gaps. Moondream appears in the wiki as [DimOS](../entities/dimos.md)'s local VLM option, alongside [Florence-2](../entities/florence-2.md), Qwen, and OpenAI.

The reason it earns a full source page rather than a stub: **it publishes a nine-tier hardware latency ladder that runs down to Jetson**, which is exactly the measurement the wiki's [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) and [deployability landscape](../syntheses/platforms/vla-deployability-landscape.md) keep finding absent.

## The models

| Model | Size | Positioning |
|---|---|---|
| **Moondream 3.1** | **9 B sparse MoE, 2 B active** | Recommended. *"Frontier-level visual reasoning, segmentation, and long-context queries."* |
| **Moondream 2** | 2 B dense | *"The production workhorse"* — GPUs, CPUs, edge devices |
| **Moondream 2 0.5B** | 0.5 B dense | *"A small fine-tuning base for constrained hardware where every megabyte matters"* |

All five capabilities (Query / Caption / Detect / Point / Segment) on every tier. Checkpoints on Hugging Face, **Apache-2.0, free for commercial use**.

## Key claims — the hardware ladder

Moondream 3.1 on Photon, ChartQA test split, batch 1, prefix caching on, P50 of 200 runs:

| Hardware | Tier | P50 latency | Peak throughput |
|---|---|---:|---:|
| NVIDIA B200 | Datacenter | 49 ms | 77.7 req/s |
| **NVIDIA H100** | Datacenter | **59 ms** | 58.0 req/s |
| RTX PRO 6000 | Workstation | 68 ms | 38.8 req/s |
| NVIDIA L40S | Server | 99 ms | 24.7 req/s |
| NVIDIA A100 80GB | Cloud | 136 ms | 16.7 req/s |
| **[Jetson AGX Thor](../entities/jetson-thor.md)** | **Edge** | **246 ms** | 12.6 req/s |
| NVIDIA A10 | Cloud | 280 ms | 7.2 req/s |
| NVIDIA L4 | Cloud | 317 ms | 6.9 req/s |
| **Jetson AGX Orin** | Edge | **514 ms** | 4.6 req/s |

**The Orin row runs Moondream 2, not 3.1** — footnoted by the vendor, and it means the bottom of the ladder is not apples-to-apples.

### The head-to-head table

| Setup | Latency | vs Moondream |
|---|---:|---|
| Moondream 3.1 + Photon (H100, batch 1) | **59 ms** | baseline |
| Qwen 3.5 4B + vLLM (H100, batch 1) | 73 ms | 1.2× slower |
| GPT-5.4 Mini (OpenAI API) | 2.78 s | 47× slower |
| Gemini 2.5 Flash (Google API) | 3.79 s | 64× slower |

Cost claim: **$0.06 per 1,000 images** on Moondream Cloud, *"the lowest-cost VLM we have measured across the inference providers we tested."*

## Key claims — the commercial stack

- **Photon** — hand-tuned-kernel inference engine, *"Mac, Windows, CUDA — Jetson to B200."* Same API across tiers.
- **Lens** — fine-tuning by API, **SFT and RL**, claimed to *"dramatically improve accuracy with as few as 20 labeled images."* Self-serve or white-glove; *"you keep the weights, the training code, and the data."*
- **Moondream Cloud** — OpenAI-compatible hosted API, pay per image.
- A worked example on the site: `model.detect(image, "Misoriented box")` returning a normalized bounding box in **33 ms on a Linux RTX 6000**, from a Lens-fine-tuned 3.1 on Photon.

## Analysis

> [!warning] These are vendor benchmarks, and one row of the comparison table is not a fair fight
> The site labels it *"Internal benchmark."* No independent replication exists, and the wiki's [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) discipline applies to latency claims too.
>
> More specifically: **comparing local Moondream+Photon at 59 ms against GPT-5.4 Mini and Gemini 2.5 Flash over a network API at 2.78–3.79 s is comparing local inference to a hosted service**, not model to model. That gap is dominated by network round-trip and provider queueing. The **Qwen 3.5 4B + vLLM row (73 ms, 1.2× slower) is the honest comparison** — same hardware, same batch size, both local — and it shows a much more modest 21% edge. Quote the Qwen row; treat the 47×/64× figures as an argument for local inference generally, which is a real point but a different one.

> [!note] Where this lands on the wiki's control-rate ladder — the planner tier, not the control tier
> **246 ms on Thor ≈ 4 Hz; 514 ms on Orin ≈ 2 Hz.** Against the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md), that places Moondream firmly in the **perception/planner band** — well above frontier LLMs at 0.2–0.4 Hz, comparable to [SmolVLA](../entities/smolvla.md)'s 1.4 Hz on an Orin Nano, and far below the [ACT](../entities/act.md) 27.8 Hz control tier.
>
> That is the correct place for it. A VLM answering *"where is the misoriented box"* does not need to run at control rate — it needs to run **fast enough that the agent loop above it feels responsive**, which at 4 Hz on a Thor it does. It is the same architectural slot [DimOS](../entities/dimos.md) puts it in: a perception service an LLM agent calls, not something in the servo loop.

> [!note] Pointing is the capability worth noticing
> **Point** and **Detect** put Moondream in the small club of VLMs that emit *spatial* output rather than text about space — the same signature capability the wiki tracks in **[Molmo](../entities/molmo.md)** (Ai2), where pointing is the distinguishing feature and the basis of [MolmoAct](../entities/molmoact.md)'s action traces. Two independent small-VLM lines converged on pointing as the primitive that makes a VLM useful to a robot, and neither is a VLA.
>
> This is the practical reason a robot stack reaches for Moondream over a general chat VLM: `detect("misoriented box") → bbox` is directly consumable by a grasp planner, where a caption is not.

> [!warning] Open-core, and the open half is going stale
> Weights are **Apache-2.0** and genuinely free for commercial use — that part is real. But the **GitHub repo was last pushed 2026-04-20, roughly four months before ingest**, while the site advertises **Moondream 3.1** and **Photon 2.0** as current. The value has moved into **Photon (the inference engine) and Lens (fine-tuning)**, both commercial.
>
> That is a legitimate business model and it is the same shape as [Vulcan Robotics](../entities/vulcan-robotics.md)'s rented inference and [Dimensional](../entities/dimensional-inc.md)'s hosted teleop broker — **give away the model, sell the thing that makes it fast**. Worth stating plainly because "open weights" and "open stack" are not the same claim, and the hardware ladder above is a *Photon* result, not an open-weights result. Reproducing those numbers without Photon is untested.
>
> To be fair on the weights specifically: **3.1 is genuinely published** (`moondream3.1-9B-A2B` on Hugging Face), so this is not a case of the open line quietly stopping. The gap is the *engine*, not the model.

## Entities mentioned

- [Moondream](../entities/moondream.md) — the subject of this source
- [DimOS](../entities/dimos.md) — ships it as a local VLM backend
- [Florence-2](../entities/florence-2.md) — the other small VLM in DimOS's zoo
- [Molmo](../entities/molmo.md) / [MolmoAct](../entities/molmoact.md) — the other pointing-capable small-VLM line
- [Jetson Thor](../entities/jetson-thor.md), [Jetson Orin Nano](../entities/jetson-orin-nano.md) — the edge tiers benchmarked
- [SmolVLA](../entities/smolvla.md), [ACT](../entities/act.md) — the rate comparison points

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — Moondream is explicitly *not* one; it is the perception tier under an agent
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — the slot it occupies
- [Heatmap object localization](../concepts/robotics/heatmap-object-localization.md) · [Detection evaluation metrics](../concepts/robotics/detection-evaluation-metrics.md)

## Open questions

- **No independent benchmark exists.** Every number here is vendor-published. The Qwen-vs-Moondream row is the one worth someone reproducing.
- **What does the ladder look like without Photon?** The open weights are Apache-2.0; the engine that produces these latencies is not. Running Moondream 3.1 under vLLM or llama.cpp on the same hardware is the missing control.
- **No accuracy numbers on this page.** ChartQA is used as a *latency* workload; how Moondream 3.1 actually scores against Qwen 3.5 4B or Molmo on grounding/pointing benchmarks is unestablished here.
- **Orin Nano, not just AGX Orin?** The ladder's cheapest tier is an AGX Orin at 514 ms with Moondream 2. The wiki's low-cost platforms ([XLeRobot](../entities/xlerobot.md)) run **Orin NX 16 GB or Orin Nano 8 GB**, which are below every row published.
- ~~Are the 3.1 weights open at all?~~ — **checked at ingest: yes.** `moondream/moondream3.1-9B-A2B` is published on Hugging Face (plus `moondream3-preview`), even though the site's product blurb lists only "2B, 1B, and 0.5B checkpoints." **The staleness is in the GitHub repo, not the weights.** Download counts also locate the real workhorse: **`vikhyatk/moondream2` at 2.39 M** vs 3.1 at ~12.6 K — the 2 B dense model is what the ecosystem actually runs.
