---
title: "Seeed Studio Jetson Product-Line Selection Guide"
type: source
url: https://www.seeedstudio.com/blog/2026/05/13/seeed-jetson-product-line-selection-guide-choose-the-right-edge-ai-computer-for-your-project/
author: Seeed Studio
published: 2026-05-13
ingested: 2026-06-04
venue: Seeed Studio blog
tags: [jetson, jetson-orin-nano, orin-nx, agx-orin, jetson-thor, seeed, recomputer, edge-ai, comparison, robotics, hardware, buying-decision]
---

# Seeed Studio Jetson Product-Line Selection Guide

> [!note] Provenance
> The Seeed blog bot-blocks automated fetches (403). The user supplied the **full article text + the selection-guide infographic** directly; both are transcribed here. The only thing absent is **pricing** (the article carries none). Module-spec figures cross-checked against NVIDIA-official (the [Forecr comparison](https://www.forecr.io/blogs/embedded-systems/nvidia-jetson-comparison) mis-assigns AGX-Orin GPU core counts to Orin NX — official is 1024-core/32-TC for both Orin NX variants).

## Summary

A buyer's guide to Seeed's NVIDIA Jetson portfolio — **edge-AI carriers spanning industrial automation, autonomous vehicles, robotics, and large-model inference.** It organizes products into *series* that wrap Jetson modules (Xavier NX, Orin Nano/NX, AGX Orin, AGX Thor) into application-ready boxes, and gives a **by-scenario decision tree**. The wiki value is two-fold: the **series → module → use-case mapping** (the bridge from a bare SoM to a buyable carrier), and the confirmation that Seeed sells a **purpose-built battery-powered robot line (Robotics J30/40)** — the concrete onboard-compute carrier for a robot like the [XLeRobot](../entities/xlerobot.md).

## Product series (guide §1)

| Series | Positioning | Modules | Max compute | Key feature | Typical scenarios |
|---|---|---|---|---|---|
| **reComputer Industrial** | Industrial-grade edge AI | Xavier NX / Orin Nano/NX | 100 TOPS | Fanless, wide-temp, PoE, full industrial IO | Industrial automation, smart agriculture, security |
| **reComputer Rugged** | Vehicle-grade rugged (⟨coming soon⟩) | Orin Nano 8 GB / Orin NX 16 GB Super | 157 TOPS | IP66 waterproof, wide-voltage, shock, isolated CAN-FD | Autonomous vehicles, mining trucks, port AGVs, outdoor robots |
| **reServer Industrial** | AI NAS / inference server | Orin Nano / Orin NX | 100 TOPS | 5× GbE (4× PoE) + SSD, multi-channel video | Warehouse, security, local RAG knowledge base |
| **reComputer Classic** | Compact entry-level dev | Orin Nano / Orin NX | 100 TOPS | Rich IO, pre-installed JetPack, mass-producible | Smart retail, in-vehicle compute |
| **reComputer Classic J401 Board** | Carrier board for Classic | Orin Nano / Orin NX | 100 TOPS | Flexible expansion, rapid dev | System-integrator custom enclosures |
| **reComputer Jetson Super** | Desktop AI workstation | Orin Nano / Orin NX | **157 TOPS** | JetPack 6.2 MAXN; runs LLM/ViT/DeepSeek | Complex video analysis, AI assistants, large-model inference |
| **reComputer Robotics J30/40** | **Robot-dedicated (battery-powered)** | Orin Nano (J30) / Orin NX (J40) | **157 TOPS** | **19–54 V wide-voltage input, CAN/GMSL** | Mobile robots, strategy training, on-site deployment |
| **reServer Industrial J501 Board** | AGX Orin high-perf carrier | AGX Orin 32/64 GB | 275 TOPS | 16× MIPI CSI / 8× GMSL + 10 GbE | Humanoid "brain", multi-sensor fusion |
| **reComputer Mini J501 Board** | Small-robot reasoning unit | AGX Orin 32/64 GB | 275 TOPS | 110×110 mm, wide-temp, 8× GMSL | Humanoid / AMR, 60 °C environments |
| **reComputer Robotics J50** | "Autonomous-driving brain" | AGX Orin 32/64 GB | 275 TOPS | 4× CAN-FD + 10 GbE + multi-comms | Humanoid, complex autonomous decision-making |
| **reComputer J601 Board** | Humanoid "brain + cerebellum" (⟨soon⟩) | **AGX Thor T5000** | **2070 TFLOPS** | **EtherCAT + 4× CAN + 8× GMSL + dual 10 GbE** | Embodied intelligence, humanoid rapid deployment |

## AI-performance / use-case bands (infographic)

The infographic plots AI performance against three tiers: **Vision AI** (Orin Nano 8 GB → Orin NX 16 GB, 40→157 TOPS) → **Generative AI / Robotics** (Orin NX Super → AGX Orin, 157→275 TOPS) → **Multimodal Perception / Humanoids** (AGX Thor, 2070 TFLOPS).

## By-scenario decision tree (guide §3)

| Your scenario | Recommended |
|---|---|
| Industrial-line AI recognition (defect detection) | reComputer **Industrial** |
| Vehicle / outdoor / mining truck | **Rugged** |
| Multi-channel network camera / storage | **reServer Industrial** |
| Prototype dev / mass production | **Classic** or **J401** carrier |
| Running large models (LLM / DeepSeek) | **Super** |
| **Mobile robots** | **Robotics J30/40** |
| AGX-Orin-level AMR / autonomous driving | **Mini J501** / **Robotics J50** |
| Thor-level humanoid robots | **J601** |

Per-scenario highlights from §2: **Rugged** = IP66, 19–48 V, −20→60 °C, 2× isolated CAN, 5× GbE (4× waterproof PoE), 5G/GPS (not yet launched). **Super** = JetPack 6.2 MAXN unlocks **157 TOPS (1.7× the prior 100 TOPS)**, 4× CSI. **Robotics J30/40** = 157 TOPS at **60 °C ambient / 40 W**, 6× USB, **2× CAN, 4× GMSL expandable, 2× I2C for IMU**, 19–54 V battery, JetPack 6.2. **Mini J501** = "perfect replacement for the official AGX Orin dev kit," 8× GMSL, 19–48 V, 60 °C. **J601** = AGX Thor, EtherCAT + 4× CAN + 8× GMSL + 4× 10 GbE + M.2 NVMe + 5G.

## The Jetson module ladder (verified specs)

| Module | AI perf | GPU (NVIDIA-official) | Memory | Bandwidth | Power |
|---|---|---|---|---|---|
| **Orin Nano 4 GB** | **34 TOPS** | 512-core Ampere / 16 TC | 4 GB 64-bit LPDDR5 | 51 GB/s | 7 / 10 / 25 W |
| **Orin Nano 8 GB** | **67 TOPS** | 1024-core / 32 TC | 8 GB 128-bit LPDDR5 | 102 GB/s | 7 / 15 / 25 W |
| **Orin NX 8 GB** | **117 TOPS** | 1024-core / 32 TC | 8 GB 128-bit LPDDR5 | 102.4 GB/s | 10–25 W (40 W Super) |
| **Orin NX 16 GB** | **157 TOPS** | 1024-core / 32 TC | 16 GB 128-bit LPDDR5 | 102.4 GB/s | 10–40 W |
| **AGX Orin 32 GB** | **200 TOPS** | 1792-core / 56 TC | 32 GB 256-bit LPDDR5 | 204.8 GB/s | 15–60 W |
| **AGX Orin 64 GB** | **275 TOPS** | 2048-core / 64 TC | 64 GB 256-bit LPDDR5 | 204.8 GB/s | 15–60 W (≤75 W MAXN per some listings) |
| **AGX Thor T5000** | **2070 TFLOPS** (FP4 sparse) | 2560-core Blackwell / 5th-gen TC | 128 GB 256-bit LPDDR5X | 273 GB/s | 40–130 W |
| **AGX Thor T4000** | **1200 TFLOPS** (FP4 sparse) | 1536-core Blackwell | 64 GB 256-bit LPDDR5X | 273 GB/s | 40–70 W |

Cross-precision caveat: the Orin ladder is INT8 TOPS; Thor's headline is FP4/FP8 — see [Jetson onboard compute for XLeRobot](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) for the "≈7.5× AGX Orin" relative anchor.

## Specific-product matrix (infographic — interfaces, power, size)

| Product | Module | Heat | Wireless | Power input | Size (mm) | Interface highlights |
|---|---|---|---|---|---|---|
| **reComputer Mini J3011** | [Orin Nano](../entities/jetson-orin-nano.md) 8 GB | Fan | Wi-Fi/BT | XT30 12–54 V DC | 63×95×42/66.7 | 2×USB 3.2, 4×USB 3.0, 2×USB 2.0, 2×CAN, 1×Eth |
| **reComputer J4012B** | Orin NX 16 GB | Fan | Wi-Fi/BT/4G/5G | DC 9–19 V (barrel 5525) | 130×120×58.5 | 1×mini-PCIe, 2×USB 3.2, 1×USB 2.0 |
| **reServer Industrial J4012** | Orin NX 16 GB | **Fanless** | Wi-Fi/BT/4G/5G | DC 12–36 V (terminal) | 194×187×95.5 | 4×USB 3.1, 2×USB 2.0, DB9 RS-232/422/485, **5×Eth** |
| **reComputer Super J4012** | Orin NX 16 GB Super | Fan | Wi-Fi/BT/4G/5G | DC 12–19 V (barrel 5525) | 194×187×95.5 | **4×MIPI CSI**, 4×USB 3.2, 1×USB 2.0, 2×Eth |
| **reComputer Robotics J4012** | Orin NX 16 GB Super | Fan | Wi-Fi/BT/4G/5G | **XT30 (2+2) 19–54 V DC** | 130×121×66 | 1×USB 3.0(DP), 6×USB 3.2, **(4-in-1) GMSL2**, 2×Eth |
| **reComputer Mini J501 Board** ⟨new⟩ | AGX Orin 32/64 GB | Fan (add'l) | Wi-Fi/BT | XT30 19–48 V DC | 110×110×38 | 2×USB 3.2, **2×CAN-FD (isolated)**, 2×(4-in-1) GMSL2, 2×Eth (1×10 GbE), RS-485 |
| **reComputer Robotics J50 Series** ⟨new⟩ | AGX Orin 32/64 GB | Fan | Wi-Fi/BT/5G/GPS | DC 19–48 V (2-pin) | 210×180×87 | 3×USB 3.0, **4×CAN-FD (isolated)**, 2×DB9 RS-232/422/485, 2×(4-in-1) GMSL2, 5×Eth (1×10 GbE) |
| **reComputer Thor J601 Board** ⟨new⟩ | **AGX Thor 128 GB** | Fan (add'l) | Wi-Fi/BT/5G | XT30 19–48 V DC | 169×155×40 | 4×USB 3.2, **4×CAN-FD**, 2×(4-in-1) GMSL2, **4×10 GbE**, **EtherCAT**, DB9 RS-232/422/485, RS-485 (JST), Audio+Mic |

## Builder notes (XLeRobot relevance)

- **Robotics J30/40 is the purpose-built battery-powered robot carrier** — 19–54 V input, CAN + GMSL, 157 TOPS at 60 °C / 40 W, JetPack 6.2. The **Robotics J4012** (Orin NX 16 GB Super variant) is concretely the carrier behind the [onboard-compute comparison](../syntheses/platforms/jetson-onboard-compute-xlerobot.md)'s "Orin NX 16 GB" XLeRobot upgrade pick — and its **19–54 V XT30 input** matters for the [power budget](../syntheses/projects/xlerobot-thor-power-budget.md) (a robotics carrier wants a higher-voltage rail than the 12 V STS3215 motor bus; a C300 DC USB-C PD or its 12 V car outlet → buck would feed it).
- **J601 (Thor)** is explicitly the **humanoid / embodied-intelligence tier** ("brain + cerebellum," EtherCAT for real-time actuation buses) — consistent with the wiki's verdict that Thor is over-budget for a small mobile manipulator and aimed at heavier robots.

## Entities mentioned
- [Jetson Orin NX](../entities/jetson-orin-nx.md) — the module behind the J4012 / Super J4012 / Robotics J40 carriers.
- [Seeed Studio](../entities/seeed-studio.md) — author/distributor.
- [Jetson Orin Nano](../entities/jetson-orin-nano.md), [Jetson Orin NX](../entities/jetson-orin-nx.md), [Jetson Thor](../entities/jetson-thor.md) — module entities. **AGX Orin still has no entity page.**

## Concepts touched
- [Jetson onboard compute for XLeRobot](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) — corroborates the four-tier ladder; supplies the buyable-carrier mapping + the battery-powered Robotics line.
- [How to Choose the Right Jetson Carrier Board (Seeed)](seeed-jetson-carrier-board-selection.md) — companion: this guide picks the *product/module tier*; that one picks the *carrier board* by system design (J401 carrier ↔ J40xx product).

## Open questions / notes
- **Prices not in the article** — series positioning + the decision tree are captured, but reComputer pricing is not.
- **Rugged J4012** is "coming soon" (not launched); IP66 vehicle-grade Orin NX carrier.
- ~~**AGX Orin / Orin NX entity gap**~~ — **Orin NX filed 2026-08-28** ([entity](../entities/jetson-orin-nx.md)). **AGX Orin still has none**; full specs are here and in the [comparison](../syntheses/platforms/jetson-onboard-compute-xlerobot.md).
