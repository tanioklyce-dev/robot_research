---
title: "RK1828 vs Jetson Orin NX vs Hailo-8: Which Edge AI Accelerator Should You Choose? (Geniatech)"
type: source
url: https://www.geniatech.com/rk1828-vs-jetson-orin-nx-vs-hailo-8/
fetch_url: https://www.geniatech.com/rk1828-vs-jetson-orin-nx-vs-hailo-8/
author: Geniatech (byline "emily")
published: 2026-05-29
ingested: 2026-09-13
local_path: raw/2026-05-29-geniatech-rk1828-vs-orin-nx-vs-hailo-8.html
sha256: 24700d8bfea8203e6f0956b50613410b85d638f766af9e6a5f89924ea8a65a09
tags: [rk1828, rk1820, rockchip, geniatech, jetson-orin-nx, hailo-8, npu, edge-ai, llm, memory-bandwidth, m2-accelerator, vendor-comparison, secondary-source]
format: ODM vendor blog post (~1,500 words, four comparison tables); page modified in place 2026-09-04
---

# RK1828 vs Jetson Orin NX vs Hailo-8 (Geniatech)

## Summary

A marketing comparison from [Geniatech](../entities/geniatech.md), a Shenzhen ARM-embedded ODM that sells M.2 cards built on the chip it is promoting, positioning [Rockchip](../entities/rockchip.md)'s **[RK1828](../entities/rockchip-rk1828.md)** LLM coprocessor against the [Jetson Orin NX](../entities/jetson-orin-nx.md) and the [Hailo](../entities/hailo.md)-8. Its one real idea is correct and already the wiki's position: for on-device LLM inference **memory bandwidth, not TOPS, is the bottleneck**, and the RK1828 attacks it by putting **5 GB of 3D-stacked DRAM in the package at a claimed 1,024 GB/s** rather than borrowing the host's LPDDR. Everything else is a vendor table. The RK1828 figures (20 TOPS INT8, ~5 W passive, 7B at 56 tok/s, PCIe 2.0 ×1 / USB 3.0, M.2 2280, "RKNN3" toolkit) are stated without model, quantisation or method, and the two competitor columns contain **two errors the wiki can catch from its own primaries**: the Orin NX is given 68 GB/s of bandwidth (NVIDIA's datasheet says 102.4), and the Hailo-8 is credited with running 3B LLMs at ~30 tok/s (the Hailo-8 is a vision-CNN part; generative AI arrived with the Hailo-10H). Ingested as the wiki's first sighting of an **M.2 LLM coprocessor with on-package memory** — a fourth architectural bet next to CUDA, on-die NPU and HAT NPU — and as a specimen of what a secondary comparison table looks like when its author sells one column.

> [!warning] Secondary source with a commercial interest, and no Rockchip primary behind it yet
> No Rockchip datasheet, product page or RKNN3 documentation for the RK1828 is ingested. Every RK1828 number on this page is Geniatech's. Do not carry any of them into a buying decision without the primary (see the [backlog](../backlog.md)).

## Key claims (as stated)

### RK1828 specification table
| Feature | Geniatech's figure |
|---|---|
| Process | 20 nm |
| AI performance | 20 TOPS (INT8) |
| Precision | INT4 / FP8 / FP16 / BF16 |
| Memory | **5 GB 3D-stacked DRAM, on-package** |
| Memory bandwidth | **1,024 GB/s** |
| CPU | triple-core RISC-V 64GCB |
| Host interface | **PCIe 2.0 ×1 / USB 3.0** |
| Typical power | ~5 W, passive cooling |
| Form factor | M.2 2280 / SO-DIMM-compatible |
| Target models | up to 7B LLMs |

### Comparison tables
| Chip | INT8 TOPS | Memory | Bandwidth | "7B inference" | Power |
|---|---|---|---|---|---|
| RK1828 | 20 | 5 GB on-package | 1,024 GB/s | **56 tok/s** | ~5 W, passive |
| Jetson Orin NX | 100 | 8 GB LPDDR5 | **68 GB/s** (sic) | 14.5 tok/s | 10–20 W, active |
| Hailo-8 | 26 | host-dependent | "lower / host dependent" | "~30 tok/s" at ~3B (sic) | ~2.5 W, passive |
| RK1820 | 20 | 2.5 GB | — | 87.7 tok/s at **3B** | — |

- No model name, quantisation, context length, batch, or measurement method is given for any tokens/s figure.
- Software: RK1828 uses an **"RKNN3 toolkit"** with PyTorch / TensorFlow / Caffe import and "API-compatible inference interfaces" for cloud-native stacks; Orin NX has CUDA / TensorRT but "tightly coupled to NVIDIA's proprietary stack"; Hailo-8 is "optimized primarily for vision inference pipelines."
- Suggested topology: **[RK3588](../entities/rockchip-rk3588.md) as host + RK1828 as LLM coprocessor.**
- Positioned for fanless industrial boxes, "private AI agents," "industrial copilots," multi-channel 4K analytics.

## Where the wiki's primaries disagree

> [!warning] Contradiction — Orin NX memory bandwidth
> Geniatech: **68 GB/s**. NVIDIA datasheet DS-10712, as recorded on the [Jetson Orin NX](../entities/jetson-orin-nx.md) page: **102.4 GB/s** (128-bit LPDDR5) for both the 8 GB and 16 GB modules. 68 GB/s is the *pre-Super* Orin **Nano** 8 GB figure. The comparison understates the NVIDIA column by a third on exactly the axis the article says matters most.

> [!warning] Contradiction — Hailo-8 and LLMs
> Geniatech credits the **Hailo-8** with ~3B LLM inference at ~30 tok/s. Per Raspberry Pi's and Hailo's own materials on the [Hailo](../entities/hailo.md) page, the Hailo-8 / 8L are **vision-CNN accelerators**; generative-AI support is the **Hailo-10H** (AI HAT+ 2, with 8 GB of its own DRAM). Either the row conflates the two parts or it reports something not in Hailo's public positioning; the wiki holds no tokens/s for any Hailo part.

Smaller notes: the Orin NX "100 TOPS" is the standard-flash 16 GB figure (157 Super) with the [DLA caveat](../entities/jetson-orin-nx.md) unmentioned; "10–20 W" omits the 40 W Super envelope; the RK1828's "20 nm" is unusual for a 2026 part and unverified.

## What is genuinely new here

- **On-package memory as the design axis.** Every board on the [heterogeneous edge SoC](../concepts/robotics/heterogeneous-edge-soc.md) page shares one LPDDR pool at 21–273 GB/s. A 1,024 GB/s figure, if it holds, is a different class — but it lives *inside the package*. The host link is **PCIe 2.0 ×1 (~500 MB/s)**, so nothing streams from host memory at speed: the entire model must be resident in the card's 5 GB, which caps it at roughly a 7B model at 4-bit with little room for KV cache. That is why the "up to 7B" ceiling is a memory-capacity statement, not a compute one — and why the [RK1820](../entities/rockchip-rk1828.md) with 2.5 GB is a 3B part.
- **A cross-source fact**: the RK1828 is **absent from the platform list of [rknn-toolkit2](rknn-toolkit2-github.md)** (RK3588 / 3576 / 3566 / 3568 / 3562 / RV11xx / RK2118), and Geniatech names a different toolchain, "RKNN3." Whatever RK1828 runs, it is not the RKNN2 stack the wiki has documented, and rknn-toolkit2's last push was July 2025.
- **A Pi 5 / RK3588 coprocessor option.** On an M.2 2280 with a PCIe ×1 link, the RK1828 is the same slot the [Hailo](../entities/hailo.md) HATs use on a [Raspberry Pi 5](../entities/raspberry-pi-5.md) — an LLM-shaped rather than vision-shaped occupant for the single lane, at a similar ~5 W. Untested anywhere in the wiki.

## Entities mentioned
- [Rockchip RK1828](../entities/rockchip-rk1828.md) (new) · [Rockchip](../entities/rockchip.md) · [Rockchip RK3588](../entities/rockchip-rk3588.md) — proposed host.
- [Geniatech](../entities/geniatech.md) (new) — author and ODM.
- [Jetson Orin NX](../entities/jetson-orin-nx.md) · [Hailo](../entities/hailo.md) — the two competitor columns.

## Concepts touched
- [Heterogeneous edge SoCs and the shared-memory budget](../concepts/robotics/heterogeneous-edge-soc.md) — this is the counter-design: move the memory into the accelerator's package.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — the "private AI agent" use case, with decode rate as the number.

## Open questions
- **Rockchip's own RK1828 / RK1820 documentation** — datasheet, RKNN3 toolkit repo, supported model list, measured tokens/s with model and quant named. Until ingested, the 56 tok/s figure is one vendor's marketing number quoted by another vendor.
- Does "RKNN3" share anything with rknn-toolkit2 / rknn-llm, or is it a new SDK for the RISC-V-hosted parts?
- Real KV-cache headroom at 7B / 4-bit in 5 GB; usable context length.
- Whether the card works in a Pi 5's M.2 HAT+ slot (PCIe Gen 2/3 ×1) and what the Linux driver story is on a non-Rockchip host.
- Geniatech's companion pieces — an M.2 accelerator comparison chart (DeepX, MemryX, NXP Ara-240), the RK1828/RK1820 card launch (2026-09-08), "RK1828 vs RK1820" (2026-09-07), and "RKNN Toolkit vs HailoRT vs ONNX Runtime" (2026-09-11) — are not ingested.
