---
title: "NVIDIA Jetson AGX Thor Developer Kit — Hardware Layout (User Guide)"
type: source
url: https://docs.nvidia.com/jetson/agx-thor-devkit/user-guide/latest/hardware_layout.html
local_path: null
author: NVIDIA (official documentation)
affiliations: NVIDIA
published: 2026
ingested: 2026-05-31
format: web-docs
tags: [jetson-thor, agx-thor, devkit, hardware, primary-source, micro-fit, usb-c-pd, qsfp28, m2-nvme, power]
---

## Summary

Official NVIDIA documentation page giving the **physical connector/port layout of the Jetson AGX Thor Developer Kit** carrier board — the primary source for what the dev kit actually exposes. Directly corroborates and tightens the power facts the wiki had previously assembled from forum threads (the [Thor power budget synthesis](../syntheses/projects/xlerobot-thor-power-budget.md) and [Jetson Thor entity](../entities/jetson-thor.md)): **Micro-Fit 9–28 V DC / up to 8 A** input, and — newly confirmed from a primary source — **USB-C is PD Sink 140 W**. Also documents a notably high-speed networking story for an edge module (**QSFP28 4×25 Gbps + 5 GbE**).

## Key claims (verbatim labels where given)

**IO side**
- **USB**: 2× **USB Type-A "USB 3.2 Gen 2 (10 Gbps)"**; 2× **USB-C** (port 5a + 5b) — both UFP and DFP "USB 3.2 Gen 1 – 5 Gbps" with **"PD Sink (140 W)"**; **port 5a** additionally does **Force-Recovery Mode**. A separate **debug USB-C** sits behind the lid cover.
- **Networking**: **RJ45 Ethernet "5 Gbps"** + a **"QSFP28 cage" supporting "4× 25 Gbps"** (i.e. 100 Gb-class networking on the dev kit).
- **Display**: **DisplayPort** out + **HDMI** out.
- **Power**: **"Micro-fit power input"** rated **"9–28 V DC input (Up to 8 A)."**

**Button side**
- **Power button (11)**, **Force Recovery button (12)**, **Reset button (13)**, **White LED (14)**.
- Force-Recovery procedure: hold **12**, briefly press **13** while holding **12**, then release **12**.

**Carrier board**
- **J103 — "M.2 Key M Connectivity Slot"** with a **1 TB NVMe SSD pre-populated**.
- Page defers deeper detail to the official **Carrier Board Specification** document.

> [!note] Not on this page
> No 40-pin GPIO header, CSI camera connectors, M.2 Key E (Wi-Fi), fan header, microSD, CAN, or T5000 module memory specs are described here — this is the high-level IO/layout page; those live in the Carrier Board Specification (not yet ingested).

## Entities mentioned
- [Jetson Thor](../entities/jetson-thor.md) — the dev kit documented here.

## Concepts touched
- (Hardware reference; no concept pages.)

## Why this matters for the wiki
- **Primary-source upgrade for the power story.** The earlier [power-budget synthesis](../syntheses/projects/xlerobot-thor-power-budget.md) leaned on NVIDIA *forum* posts for the 9–28 V / 8 A Micro-Fit input and the "USB-C may not reach the 168 W ceiling" caveat. This page confirms both from official docs and pins the **USB-C input at PD Sink 140 W** — so USB-C alone is hard-capped 28 W below the dev kit's 168 W power ceiling, reinforcing the "power Thor via the 28 V brick / Micro-Fit, not USB-C, for full load" recommendation.
- **New datapoint: QSFP28 4×25 Gbps + 5 GbE.** Surprisingly high-bandwidth networking for an on-robot module — relevant to multi-sensor / CSI-over-Ethernet (Holoscan Sensor Bridge) and distributed-compute setups, and a differentiator vs the Orin generation.

## Open questions
- The **Carrier Board Specification** (referenced but not linked here) holds the 40-pin header, CSI, M.2 Key E, fan, and CAN details — the natural next ingest if those matter for a build.
- USB-C is **PD Sink** only (no listed source/DFP power-out wattage beyond data) — worth confirming whether either USB-C can *source* power to peripherals.
