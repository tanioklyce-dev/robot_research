---
title: "airockchip/rknn-llm — README, benchmark table, changelog, license (RKLLM v1.3.0)"
type: source
url: https://github.com/airockchip/rknn-llm
local_path: raw/2026-09-13-rknn-llm-readme-benchmark-changelog-license.md
sha256: e9c795fab8320b90f9afb48d9dd9465cc76c23d32f974236eb231ab4a7562bb1
author: Rockchip Electronics Co., Ltd.
published: 2024-03-14
ingested: 2026-09-13
venue: "GitHub; Rockchip's LLM / VLM runtime for its NPUs"
format: repository README + benchmark.md + CHANGELOG + LICENSE, plus API metadata
github_stats: "1,674 stars, 219 forks, 280 open issues, created 2024-03-14, pushed 2026-06-17, latest release v1.3.0 (2026-06-17) (captured 2026-09-13)"
tags: [rkllm, rknn-llm, rockchip, npu, llm, vlm, rk3588, rk3576, edge-ai, on-device-llm, benchmark, gemma4, smolvlm, qwen, toolchain, github]
---

# airockchip/rknn-llm (RKLLM)

## Summary

The other half of Rockchip's NPU software, and the half that is alive: **RKLLM** converts a Hugging Face-format language or vision-language model on a PC into `.rkllm` and runs it on the **RK3588, RK3576, RK3562 or RV1126B** NPU through a C API — the SDK [rknn-toolkit2](rknn-toolkit2-github.md) sends you to for anything LLM-shaped. Where the vision SDK has been quiet since mid-2025, this repo shipped **v1.3.0 on 2026-06-17** with Gemma 4, Qwen3.5 and SmolLM3 support. Its `benchmark.md` is the reason to ingest it: **the wiki's first NPU-measured LLM and VLM throughput for a Rockchip board**, with model, quantisation, sequence length and memory stated. Three numbers reorganise the wiki's edge tier. **Gemma 4 E2B decodes at 11.1 tok/s on the RK3588 NPU (w8a8)** — between the Pi 5 CPU's 7.6 and the Orin Nano GPU's 24.2 for the same model in Google's table. **A 6B model on the NPU decodes at 4.98 tok/s**, essentially the 5.46 tok/s the [Turing Pi article](turingpi-rk3588-architecture-deep-dive.md) measured for a 7B on the *CPU* — the NPU does not escape the shared LPDDR path, it only spends it more efficiently. And **image encoding is the slow step for any VLM here**: 0.7–3.3 s per image on RK3588 (SmolVLM-256M 0.84 s, Qwen2.5-VL-3B 2.9 s), which puts VLM-in-the-loop perception on this class at roughly **1 Hz at best**. Also on file: an **OpenAI-compatible server demo**, function calling, LoRA joint inference, prompt caching, 16K context, and a BSD-style license text that — unlike toolkit2's — is permissive, though the runtime ships as binaries.

## Key claims

### Stack and scope (README)
- **RKLLM-Toolkit** (PC: conversion + quantisation, Python 3.9–3.12) → `.rkllm` → **RKLLM Runtime** (`librkllmrt.so`, C/C++, Linux and Android) → open-source RKNPU kernel driver. Vision encoders for multimodal models run through **RKNN** (toolkit2) in FP16; the language model through RKLLM.
- **Platforms: RK3588, RK3576, RK3562, RV1126B.** Not the RK3566 under [Microduck](../entities/microduck.md), not the [RK1828](../entities/rockchip-rk1828.md).
- **Supported model families** (v1.3.0): Llama / TinyLlama, **Qwen2 / 2.5 / 3 / 3.5**, Phi-2/3, ChatGLM3-6B, **Gemma 2 / 3 / 3n / 4**, InternLM2, MiniCPM 3/4, TeleChat2, **Qwen2-VL / Qwen3-VL**, MiniCPM-V-2.6, DeepSeek-R1-Distill, Janus-Pro-1B, InternVL2/3-1B, **SmolVLM / SmolLM3**, RWKV7, DeepSeek-OCR.
- Quickstart is a multimodal demo pushed over `adb`: `demo image encoder.rknn llm.rkllm max_new_tokens max_context rknn_core_num platform` — e.g. Qwen2.5-VL-3B w8a8 on three NPU cores, 4,096 context.
- Performance method: max CPU/NPU frequencies via `scripts/fix_freq_<platform>.sh`, `RKLLM_LOG_LEVEL=1` for per-inference timing and memory, CPU/NPU utilisation watch scripts. Models converted with `optimization_level 0`.
- Distribution: SDK and pre-converted `rkllm_model_zoo` via Chinese file-shares with fetch codes.

### Benchmark table — RK3588, w8a8, 128-token prompt, 64 new tokens
| Model | Params | TTFT (ms) | Decode (tok/s) | Memory (MB) |
|---|---|---|---|---|
| Qwen2 | 0.5B | 146 | **41.6** | 670 |
| Qwen3 | 0.6B | 199 | 32.9 | 791 |
| Qwen3.5 | 0.8B | 588 | 27.1 | 1,040 |
| Qwen2.5 | 1.5B | 378 | 16.7 | 1,689 |
| Qwen3-VL (text) | 2B | 384 | 15.0 | 1,869 |
| Gemma 2 | 2B | 598 | 10.4 | 2,779 |
| **Gemma 4** | **E2B** | **599** | **11.1** | **2,499** |
| Qwen3.5 | 4B | 2,069 | 6.2 | 4,576 |
| Phi-3 | 3.8B | 1,017 | 7.5 | 3,758 |
| ChatGLM3 | **6B** | 1,353 | **4.98** | **5,986** |
| DeepSeek-OCR | 3B (A570M MoE) | 701 | 31.6 | 3,067 |

### Other platforms (same conditions)
- **RK3576** supports **w4a16** (and grouped `w4a16_g128`), which the RK3588 table never uses: ChatGLM3-6B w4a16 **4.63 tok/s in 3,023 MB** (half the RK3588's memory, similar speed); Gemma 4 E2B w4a16 9.2 tok/s; Qwen2 0.5B 32.6. On nearly every model the **RK3588 at 8-bit still out-decodes the RK3576 at 4-bit**.
- **RK3562**: Qwen2 0.5B 13.6 tok/s. **RV1126B**: Qwen2 0.5B w4a16 20.9 tok/s in 411 MB.

### Multimodal (vision encoder on RKNN FP16, all NPU cores)
| Model | Stage | RK3588 (w8a8) | RK3576 (w4a16) |
|---|---|---|---|
| **SmolVLM-256M** | image encoder 512² / prefill 128 / decode | **842 ms** / 77 ms / **78 tok/s** | 768 ms / 180 ms / 57.7 |
| Qwen3.5-0.8B | encoder 448² / prefill 216 / decode | 690 ms / 1.56 s / 27 | 815 ms / 3.4 s / 15.4 |
| Qwen3-VL-2B | encoder 448² / prefill 196 / decode | 2.08 s / 649 ms / 14.9 | 1.61 s / 1.59 s / 10.4 |
| Qwen2.5-VL-3B | encoder 392² / prefill 196 / decode | **2.93 s** / 1.12 s / 8.7 | 2.87 s / 2.13 s / 7.9 |
| MiniCPM-V-2.6 | encoder 448² / prefill 64 / decode | 3.27 s / 826 ms / 4.2 | 2.4 s / 1.23 s / 3.9 |

### Changelog — the capability timeline
| Version | Date | Notable |
|---|---|---|
| v1.0.0 | 2024 | RK3588 / RK3576; Llama, Qwen, Phi-2; w8a8 + w4a16 |
| v1.1.0 | 2024 | grouped quantisation; **LoRA joint inference**; prompt-cache save/preload; **GGUF import (q4_0, fp16)**; PC simulation; four input types incl. embedding + multimodal |
| v1.2.0 | 2025-04 | custom model conversion; chat templates; multi-turn; **16K context**; embedding flash storage; GRQ int4; GPTQ-int8 import; RK3562; InternVL2 / Janus / Qwen2.5-VL; Gemma 3 |
| v1.2.1 | 2025-06 | RWKV7, Qwen3, MiniCPM4; RV1126B; **function calling**; cross-attention; multi-batch; thinking-mode templates; **OpenAI-compatible server**; mrope |
| v1.2.2 | 2025-09 | Gemma 3n, InternVL3; multi-instance; LongRoPE |
| v1.2.3 | 2025-11 | InternVL3.5, DeepSeek-OCR, Qwen3-VL; automatic cache reuse for embedding input |
| **v1.3.0** | **2026-06-17** | **Qwen3.5, Gemma 4, SmolLM3**; multimodal cache reuse; tokenizer/embedding callbacks; RK3576 long-context decode; RK3588 overflow fixes |

### License
- Repo `LICENSE` is a **BSD-3-Clause-style** Rockchip copyright notice (redistribution with attribution, no endorsement) — permissive, in contrast to toolkit2's Rockchip-products-only SDK agreement. The runtime library and toolkit wheels are distributed as binaries; whether the notice is meant to cover them is not stated. GitHub shows "Other".

## What this settles for the wiki

- **The RK3588 gets a same-model rung on the Gemma 4 E2B ladder**: Pi 5 CPU 7.6 → **RK3588 NPU 11.1** → Orin Nano CPU 12.2 → Orin Nano GPU 24.2 → Dragonwing NPU 31.7 tok/s ([Gemma 4 E2B card](gemma-4-e2b-model-card.md)). Decode is comparable across the two tables; **TTFT is not** (Google measured a 1,024-token prefill, Rockchip 128), and the quantisations differ (QAT 2/4/8-bit vs w8a8).
- **NPU ≈ CPU at the top of the memory budget.** 4.98 tok/s for a 6B at 8-bit weights on the NPU against 5.46 tok/s for a 7B at 4-bit on four A76 cores ([Turing Pi](turingpi-rk3588-architecture-deep-dive.md)): the NPU moves roughly twice the bytes per token at the same rate, so it is about twice as bandwidth-efficient — and still bounded by the same ~21.5 GB/s. This is the cross-source confirmation the [edge-SoC page](../concepts/robotics/heterogeneous-edge-soc.md)'s first fact was missing.
- **VLM perception on this class is ~1 Hz.** The image encoder alone is 0.7–3.3 s; the smallest usable VLM (SmolVLM-256M) needs ~0.9 s before its first token. That puts a Rockchip-hosted "System 2" VLM at the bottom of the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md), below the ~10 Hz design target and near the frontier-LLM tier.
- **SmolVLM runs; SmolVLA does not.** SmolVLM-256M — the backbone FEARL's [SmolVLA](../entities/smolvla.md) variant uses — decodes at 78 tok/s here, but that is the VLM half only; the flow-matching action expert would have to go through toolkit2 as a separate `.rknn`, with the two runtimes sharing features. Nobody has tried it.
- **Memory sets the ceiling, so the SKU matters**: a 6B at w8a8 wants ~6 GB, so an RK3588 board with 8 GB is the floor and 16 GB the comfortable choice; on the RK3576, w4a16 halves that.
- **It plugs into the wiki's agent stack as-is**: an OpenAI-compatible endpoint on the robot is what [NeMo Guardrails](nemo-guardrails-library-overview.md) and the [on-device agent](../syntheses/agents/on-device-and-on-robot-agents.md) pattern assume.

## Entities mentioned
- [RKLLM](../entities/rknn-llm.md) (new) · [RKNN-Toolkit2](../entities/rknn-toolkit2.md) · [Rockchip](../entities/rockchip.md) · [Rockchip RK3588](../entities/rockchip-rk3588.md)
- [Gemma 4](../entities/gemma4.md) · [Qwen](../entities/qwen.md) · [SmolVLA](../entities/smolvla.md) (via SmolVLM)
- [Microduck](../entities/microduck.md) — excluded by the platform list (RK3566).
- [Jetson Orin Nano](../entities/jetson-orin-nano.md), [Raspberry Pi 5](../entities/raspberry-pi-5.md) — the neighbouring rungs.

## Concepts touched
- [Heterogeneous edge SoCs and the shared-memory budget](../concepts/robotics/heterogeneous-edge-soc.md)
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) · [VLA models](../concepts/learning/vla-models.md) · [Embodied reasoning VLMs](../concepts/learning/embodied-reasoning-vlms.md)

## Open questions
- Power draw during decode and during the image-encoder burst — absent, as on every Rockchip page.
- Decode at realistic context (the table is 128 + 64 tokens; a robot agent's prompt is thousands) — the 16K-context claim has no throughput attached.
- Whether a SmolVLA can be split across RKLLM (VLM) and RKNN (action expert) with acceptable feature hand-off; whether the `embedding` input type is the hook.
- What the RK1828's "RKNN3" is relative to this SDK.
- Accuracy after w8a8 / w4a16 — no eval scores anywhere in the repo.
