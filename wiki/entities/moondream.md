---
title: Moondream
type: entity
subtype: model
created: 2026-08-13
updated: 2026-08-13
sources: 2
tags: [moondream, vlm, small-vlm, pointing, object-detection, segmentation, edge-inference, jetson, photon, open-weights, apache-2-0, m87-labs]
---

**Moondream** — *"a tiny vision language model that kicks ass and runs anywhere"* — an **Apache-2.0 open-weights** VLM family from **M87 Labs**, wrapped in a commercial stack: **Photon** (inference engine), **Lens** (fine-tuning), **Moondream Cloud** (hosted API). [m87-labs/moondream](https://github.com/m87-labs/moondream) — **9,963★**, **5M+ monthly downloads**. Primary source: [moondream.ai](../sources/moondream-ai.md).

| Model | Size | Note |
|---|---|---|
| **Moondream 3.1** | **9 B sparse MoE, 2 B active** | current flagship; `moondream3.1-9B-A2B` on HF |
| **Moondream 2** | 2 B dense | **what the ecosystem actually runs** — 2.39 M HF downloads vs 3.1's ~12.6 K |
| Moondream 2 0.5B | 0.5 B dense | fine-tuning base for constrained hardware |

Five operations on every tier: **Query · Caption · Detect · Point · Segment**.

## Why it matters in this wiki

- **[DimOS](dimos.md)** ships it as a local VLM backend (local + hosted) alongside [Florence-2](florence-2.md), Qwen, and OpenAI — the perception service an LLM agent calls.
- It is the **only small VLM here with a published edge-latency ladder**, which is the measurement the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) and [deployability landscape](../syntheses/platforms/vla-deployability-landscape.md) keep finding absent.
- **Photon 2.0 is marketed as an "inference engine for Physical AI"** — a small-VLM vendor aiming explicitly at robotics.

## Measured latency (vendor-published)

Moondream 3.1 + Photon, ChartQA, batch 1, P50 of 200 runs:

| Hardware | P50 | Throughput |
|---|---:|---:|
| B200 / **H100** | 49 / **59 ms** | 77.7 / 58.0 req/s |
| RTX PRO 6000 | 68 ms | 38.8 req/s |
| A100 80 GB | 136 ms | 16.7 req/s |
| **[Jetson AGX Thor](jetson-thor.md)** | **246 ms** | 12.6 req/s |
| **Jetson AGX Orin** (Moondream **2**) | **514 ms** | 4.6 req/s |

> [!note] It lands in the planner tier, which is the right place for it
> **246 ms on Thor ≈ 4 Hz; 514 ms on Orin ≈ 2 Hz.** On the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) that is the **perception/planner band** — above frontier LLMs (0.2–0.4 Hz), near [SmolVLA](smolvla.md) (1.4 Hz on an Orin Nano), far below the [ACT](act.md) control tier (27.8 Hz). A VLM answering *"where is the misoriented box"* does not belong in a servo loop; it needs to be fast enough that the agent above it feels responsive, and at 4 Hz on a Thor it is.

> [!warning] Read the vendor's comparison table with one row discarded
> The headline is Moondream+Photon **59 ms vs GPT-5.4 Mini 2.78 s (47×) and Gemini 2.5 Flash 3.79 s (64×)** — but those are **network APIs**, so the gap is dominated by round-trip and queueing. That compares local inference to a hosted service, not model to model. **The honest row is Qwen 3.5 4B + vLLM at 73 ms** — same hardware, same batch, both local — a **21% edge, not 47×**.
>
> Everything here is **vendor-benchmarked with no independent replication**, and the Jetson AGX Orin row runs **Moondream 2, not 3.1**, so the bottom of the ladder is not apples-to-apples.

## Pointing

**Point** and **Detect** put Moondream in the small club of VLMs that emit *spatial* output rather than text about space — the same signature capability the wiki tracks in **[Molmo](molmo.md)**, where pointing underpins [MolmoAct](molmoact.md)'s action traces. **Two independent small-VLM lines converged on pointing as the primitive that makes a VLM useful to a robot**, and neither is a VLA.

That is the practical reason a robot stack reaches for Moondream over a general chat VLM: `detect("misoriented box") → bbox` is directly consumable by a grasp planner; a caption is not.

> [!warning] Open weights ≠ open stack
> The weights are genuinely Apache-2.0 and **3.1 is published** — this is not a case of the open line quietly stopping. But the **GitHub repo was last pushed 2026-04-20**, ~4 months before ingest, while the product shipped 3.1 and Photon 2.0. The value moved into **Photon and Lens**, both commercial, and **the latency ladder above is a Photon result** — reproducing it on open weights alone is untested. Same shape as [Vulcan Robotics](vulcan-robotics.md)'s rented inference and [Dimensional](dimensional-inc.md)'s hosted broker: give away the model, sell what makes it fast.

## Related

- [DimOS](dimos.md) — ships it as a local VLM option · [Florence-2](florence-2.md) — the other small VLM in that zoo
- [Molmo](molmo.md) / [MolmoAct](molmoact.md) — the other pointing-capable line
- [Jetson Thor](jetson-thor.md) · [Jetson Orin Nano](jetson-orin-nano.md) · [control-rate ladder](../syntheses/platforms/control-rate-ladder.md)
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — the slot it occupies, below the agent and above the robot

## Open questions

- **No independent benchmark.** The Qwen-vs-Moondream row is the one worth reproducing.
- **What does the ladder look like without Photon** (vLLM, llama.cpp) on the same hardware? The missing control.
- **No accuracy numbers** — ChartQA is used as a *latency* workload; grounding/pointing accuracy vs Molmo or Qwen is unestablished here.
- **Nothing below AGX Orin is published**, and this wiki's low-cost platforms run **Orin NX 16 GB / Orin Nano 8 GB** — below every row on the ladder.

## Mentioned in

- [moondream.ai](../sources/moondream-ai.md)
- [DimOS GitHub repository](../sources/dimos-github.md)
