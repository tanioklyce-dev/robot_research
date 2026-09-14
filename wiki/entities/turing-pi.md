---
title: Turing Pi
type: entity
subtype: company
created: 2026-09-13
updated: 2026-09-13
sources: 1
tags: [turing-pi, rk3588, cluster-board, compute-module, single-board-computer, homelab, edge-compute]
---

# Turing Pi

Maker of the **Turing Pi 2 / 2.5** cluster baseboards (four compute-module slots on one board, aimed at homelab Kubernetes and edge clusters) and the **Turing RK1**, a [Rockchip RK3588](rockchip-rk3588.md) compute module sold in **8 / 16 / 32 GB** LPDDR variants with a matching heatsink and 5 V PWM fan ([architecture deep dive](../sources/turingpi-rk3588-architecture-deep-dive.md)).

In this wiki Turing Pi appears as an **author**, not a robot vendor: its RK3588 architecture article is the most carefully measured public explanation of how a heterogeneous ARM SoC's engines share one memory path, and the reference numbers on the [RK3588](rockchip-rk3588.md) page were taken on a 32 GB RK1 in a Turing Pi 2.5 under Ubuntu Server 24.04. The article cross-references three earlier Turing Pi pieces — an RK1 benchmark (STREAM / mbw / memcpy / kernel-build), an RK3588 GGUF LLM benchmark, and a Jellyfin hardware-transcoding guide — none of which is ingested.

> [!note] Vendor context
> Turing Pi sells the RK1 it benchmarks. The article's method is stated in enough detail to reproduce (kernel, governor, pinning, median of three, variance, temperatures) and it consistently narrows Rockchip's marketing claims, but no wattage is ever reported. See the [source page](../sources/turingpi-rk3588-architecture-deep-dive.md). **One transcription error found (2026-09-13)**: the three model-zoo fps figures it attributes to the RK3588 are the [zoo](../sources/rknn-model-zoo-github.md)'s RK3576 column.

## Related
- [Rockchip RK3588](rockchip-rk3588.md) · [Rockchip](rockchip.md)
- [Raspberry Pi 5](raspberry-pi-5.md) — the board the RK1 class is positioned against.

## Mentioned in
- [RK3588 Architecture Deep Dive (Turing Pi)](../sources/turingpi-rk3588-architecture-deep-dive.md)
