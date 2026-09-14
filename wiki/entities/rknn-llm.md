---
title: RKLLM (airockchip/rknn-llm)
type: entity
subtype: software
created: 2026-09-13
updated: 2026-09-13
sources: 3
tags: [rkllm, rknn-llm, rockchip, npu, llm, vlm, on-device-llm, rk3588, rk3576, toolchain, openai-compatible, edge-ai]
---

# RKLLM

[Rockchip](rockchip.md)'s LLM / VLM runtime for its NPUs: **RKLLM-Toolkit** converts a Hugging Face-format model on a PC into `.rkllm` (w8a8 everywhere; w4a16 on RK3576 / RV1126B), and **RKLLM Runtime** (`librkllmrt.so`, C API, Linux / Android) runs it on the **RK3588, RK3576, RK3562 or RV1126B**. Vision encoders for multimodal models are compiled separately through [RKNN-Toolkit2](rknn-toolkit2.md) and run in FP16 on the NPU ([repo](../sources/rknn-llm-github.md)). Actively maintained: v1.3.0 on 2026-06-17 added Gemma 4, Qwen3.5 and SmolLM3.

## Measured (Rockchip's `benchmark.md`, 128-token prompt, 64 new tokens, max clocks)

| | RK3588 NPU, w8a8 | RK3576 NPU, w4a16 |
|---|---|---|
| Qwen2 0.5B | 41.6 tok/s, 670 MB | 32.6 tok/s, 443 MB |
| **Gemma 4 E2B** | **11.1 tok/s**, TTFT 599 ms, 2.5 GB | 9.2 tok/s, 1.5 GB |
| Qwen3.5 4B | 6.2 tok/s, 4.6 GB | 5.0 tok/s, 2.4 GB |
| ChatGLM3 **6B** | **4.98 tok/s**, 6.0 GB | 4.63 tok/s, 3.0 GB |
| SmolVLM-256M (image 512² / decode) | **842 ms / 78 tok/s** | 768 ms / 57.7 |
| Qwen2.5-VL-3B (image 392² / decode) | **2.93 s / 8.7 tok/s** | 2.87 s / 7.9 |

Three readings. The Gemma 4 E2B row lands **between the Pi 5 CPU (7.6) and the Orin Nano GPU (24.2)** on the same model ([Gemma 4](gemma4.md)). The 6B row matches the **CPU** rate the [Turing Pi article](../sources/turingpi-rk3588-architecture-deep-dive.md) measured for a 7B at 4-bit (5.46 tok/s) — the NPU moves ~2× the bytes at the same speed, and both are bounded by the [RK3588](rockchip-rk3588.md)'s ~21.5 GB/s LPDDR. And **image encoding is 0.7–3.3 s per frame**, which makes any VLM-in-the-loop on this class a ~1 Hz proposition on the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md).

## Features that matter for a robot agent
- **OpenAI-compatible server demo** (`rkllm_server_demo`, v1.2.1+) — drops into the wiki's guardrail / agent stack unchanged.
- **Function calling**, thinking-mode chat templates, multi-turn, **16K context**, prompt-cache save/preload and automatic reuse, multi-instance and multi-batch, **LoRA joint inference**, GGUF import (q4_0 / fp16), four input types (prompt / token / embedding / multimodal).
- Supported families include Llama, Qwen 2–3.5 (+VL), Gemma 2–4, Phi, InternLM2/VL, MiniCPM, SmolVLM / SmolLM3, RWKV7, DeepSeek-R1-Distill and DeepSeek-OCR.
- **Not** the RK3566 ([Microduck](microduck.md) has no LLM path) and not the [RK1828](rockchip-rk1828.md).
- License text is BSD-3-style, unlike toolkit2's proprietary SDK agreement; runtime and toolkit ship as binaries.

## Related
- [RKNN-Toolkit2](rknn-toolkit2.md) — the vision / general SDK; the two share the kernel driver and a robot would need both (VLM here, action head there).
- [Rockchip RK3588](rockchip-rk3588.md) · [Rockchip](rockchip.md)
- [Gemma 4](gemma4.md) · [SmolVLA](smolvla.md) — whose VLM backbone this runs, without its action expert.
- [Heterogeneous edge SoCs and the shared-memory budget](../concepts/robotics/heterogeneous-edge-soc.md)

## Mentioned in
- [airockchip/rknn-llm](../sources/rknn-llm-github.md)
- [airockchip/rknn-toolkit2](../sources/rknn-toolkit2-github.md) — the README's redirect for LLMs
- [KickPi RK3566 Microduck case study](../sources/kickpi-rk3566-microduck-case-study.md) — by the RK3566's absence from the platform list
