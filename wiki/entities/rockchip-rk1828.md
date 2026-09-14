---
title: Rockchip RK1828 (and RK1820)
type: entity
subtype: product
created: 2026-09-13
updated: 2026-09-13
sources: 2
tags: [rk1828, rk1820, rockchip, npu, llm-coprocessor, m2-accelerator, on-package-memory, edge-ai, secondary-only]
---

# Rockchip RK1828 (and RK1820)

[Rockchip](rockchip.md)'s edge **LLM coprocessor**: a standalone accelerator chip (not an application SoC) with **on-package 3D-stacked DRAM**, sold on M.2 2280 cards by ODMs such as [Geniatech](geniatech.md), meant to sit beside a host like the [RK3588](rockchip-rk3588.md) or a [Raspberry Pi 5](raspberry-pi-5.md) and run a quantised 7B-class model entirely from its own memory.

> [!warning] Everything below is from one ODM's marketing page
> The only ingested source is [Geniatech's comparison](../sources/geniatech-rk1828-vs-orin-nx-vs-hailo-8.md), whose competitor columns contain two errors the wiki caught against NVIDIA and Hailo primaries. No Rockchip datasheet is ingested. Treat every figure as unverified vendor claim.

## Claimed specification (Geniatech)

| | RK1828 | RK1820 |
|---|---|---|
| AI performance | 20 TOPS INT8 | 20 TOPS |
| Precision | INT4 / FP8 / FP16 / BF16 | — |
| Memory | **5 GB on-package 3D-stacked DRAM** | 2.5 GB |
| Memory bandwidth | **1,024 GB/s** (claimed) | — |
| Host CPU on chip | 3× RISC-V 64GCB | — |
| Host link | **PCIe 2.0 ×1 / USB 3.0** | — |
| Power | ~5 W, passive | — |
| Form factor | M.2 2280 / SO-DIMM-compatible | M.2 |
| Target | "up to 7B LLMs", 56 tok/s claimed (model and quant unstated) | 3B, 87.7 tok/s claimed |
| Toolchain | "RKNN3" | — |

## Why the design is interesting, and what bounds it

The wiki's [edge-SoC page](../concepts/robotics/heterogeneous-edge-soc.md) argues that every onboard board is bounded by one shared LPDDR path (21–273 GB/s). The RK1828 is the first part here that answers that by **moving the memory into the accelerator's package**. But the host link is a single PCIe 2.0 lane (~500 MB/s), so the 1,024 GB/s is usable only for weights and KV cache that are already resident: **model size is capped by the 5 GB on the card**, which is roughly a 7B model at 4-bit with thin KV headroom — the reason the 2.5 GB RK1820 is a 3B part. It is an LLM appliance on a stick, not a general accelerator: nothing about it helps a vision pipeline that has to stream frames across that lane.

Two cross-source facts. The RK1828 is **not in [rknn-toolkit2](../sources/rknn-toolkit2-github.md)'s supported-platform list**, and Geniatech names a different toolchain ("RKNN3"), so its software story is unknown here. And on an M.2 2280 with PCIe ×1, it occupies the same slot and lane a [Hailo](hailo.md) HAT would on a Pi 5 — an LLM-shaped rather than vision-shaped use of the one lane.

## Related
- [Rockchip](rockchip.md) · [Rockchip RK3588](rockchip-rk3588.md) — the proposed host.
- [Hailo](hailo.md) — the HAT-NPU alternative for the same slot (vision on 8/8L, generative on 10H with 8 GB of its own DRAM — the closest architectural analogue).
- [Jetson Orin NX](jetson-orin-nx.md) — the CUDA column of the comparison, misquoted at 68 GB/s.
- [Heterogeneous edge SoCs and the shared-memory budget](../concepts/robotics/heterogeneous-edge-soc.md)

## Mentioned in
- [RK1828 vs Jetson Orin NX vs Hailo-8 (Geniatech)](../sources/geniatech-rk1828-vs-orin-nx-vs-hailo-8.md)
- [airockchip/rknn-toolkit2](../sources/rknn-toolkit2-github.md) — by its absence from the platform list
