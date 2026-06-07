---
title: Raspberry Pi 5
type: entity
subtype: product
created: 2026-06-07
updated: 2026-06-07
sources: 1
tags: [raspberry-pi, single-board-computer, host-compute, edge, xlerobot, lekiwi]
---

# Raspberry Pi 5

The 2023-generation Raspberry Pi single-board computer (Broadcom BCM2712 quad-core Cortex-A76, 4/8/16 GB LPDDR4X). In this wiki it appears as the **low-cost host/relay compute** in several affordable robot builds, and now as the host for an onboard AI accelerator.

## Role in wiki robot platforms

- **[XLeRobot](xlerobot.md)** — the optional Raspberry Pi 4/5 (+$79) is the **data relay** in the stock "PC-does-inference, Pi-relays-WiFi" model; heavy policy inference runs off-board ([XLeRobot](xlerobot.md)).
- **[LeKiwi](lekiwi.md)** / **[Grievous](grievous.md)** — Raspberry-Pi-hosted mobile bases in the LeRobot lineage.
- A single **PCIe Gen 2/3 ×1 lane** is exposed on the Pi 5, which the Hailo AI HATs and NVMe SSDs share — a real constraint when stacking accelerators + storage.

## AI acceleration

The Pi 5 is the host for Raspberry Pi's [Hailo](hailo.md)-based AI HATs:
- **AI HAT+** (Hailo-8L 13 TOPS / Hailo-8 26 TOPS) — vision-CNN accelerator.
- **[AI HAT+ 2](../sources/raspberry-pi-ai-hat-plus-2.md)** (Hailo-10H, 40 TOPS INT4, 8 GB) — generative-AI / LLM / VLM accelerator.

These make a Pi 5 a viable **onboard host + NPU** for a robot — distinct from the CUDA path of a [Jetson](jetson-orin-nano.md); see [Jetson onboard compute for XLeRobot](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) and [Hailo](hailo.md) for where each fits.

## Related
- [Hailo](hailo.md) — AI HAT accelerator silicon.
- [XLeRobot](xlerobot.md), [LeKiwi](lekiwi.md), [Grievous](grievous.md) — Pi-hosted robot builds.
- [Jetson Orin Nano](jetson-orin-nano.md) — the CUDA alternative to a Pi-5-as-brain.

## Mentioned in
- [Raspberry Pi AI HAT+ 2 (Hailo-10H)](../sources/raspberry-pi-ai-hat-plus-2.md)
