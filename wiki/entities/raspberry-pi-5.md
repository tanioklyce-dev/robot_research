---
title: Raspberry Pi 5
type: entity
subtype: product
created: 2026-06-07
updated: 2026-08-30
sources: 5
tags: [raspberry-pi, single-board-computer, host-compute, edge, xlerobot, lekiwi, sourccey, nori]
---

# Raspberry Pi 5

The 2023-generation Raspberry Pi single-board computer (Broadcom BCM2712 quad-core Cortex-A76, 4/8/16 GB LPDDR4X). In this wiki it appears as the **low-cost host/relay compute** in several affordable robot builds, and now as the host for an onboard AI accelerator.

## Role in wiki robot platforms

- **[XLeRobot](xlerobot.md)** — the optional Raspberry Pi 4/5 (+$79) is the **data relay** in the stock "PC-does-inference, Pi-relays-WiFi" model; heavy policy inference runs off-board ([XLeRobot](xlerobot.md)).
- **[LeKiwi](lekiwi.md)** / **[Grievous](grievous.md)** — Raspberry-Pi-hosted mobile bases in the LeRobot lineage.
- **[Sourccey](sourccey.md)** ([Vulcan Robotics](vulcan-robotics.md), 2026) — the Pi 5 is the *only* onboard computer, running at 5.1 V through a Pi 5 power HAT with a **PCIe-to-USB HAT** and a cooling fan. Its USB budget is unusually heavy for a Pi: **4 cameras + 1 speaker + 2 motor drivers + 1 LCD**, which is why the PCIe lane is spent on USB expansion rather than an NVMe drive or a [Hailo](hailo.md) HAT. GPIO carries wheel motors, actuator sensing, and battery detection. Sourccey is the clearest case in this wiki of the Pi 5 as a **full robot controller** rather than a relay — and also of its limits: the [X-VLA](x-vla.md)-0.9B policies Sourccey ships cannot run on it, so inference is off-board ([Vulcan specs](../sources/vulcan-robotics-sourccey-site.md)).
- **[NORI A3](nori-a3.md)** ([Nori Robotics](nori-robotics.md), 2026) — a **Pi 5 4 GB** is the entire onboard computer of a **$1,688 bimanual home robot** with two 7+1-DOF arms, a 55 kg lift column, 2D LiDAR and four cameras ([YC profile](../sources/nori-robotics-yc-profile.md)). The vendor never names the board; the company's YC page does. The 4 GB SKU also forecloses the 8 GB [Hailo](hailo.md) AI HAT+ 2, so there is no onboard route to VLM-class inference — the "Nori Lab" **laptop** app is where policy inference must live. The clearest case yet of the Pi 5 as a **thin client's** sensor hub sold as a robot brain.
- A single **PCIe Gen 2/3 ×1 lane** is exposed on the Pi 5, which the Hailo AI HATs and NVMe SSDs share — a real constraint when stacking accelerators + storage.

## AI acceleration

The Pi 5 is the host for Raspberry Pi's [Hailo](hailo.md)-based AI HATs:
- **AI HAT+** (Hailo-8L 13 TOPS / Hailo-8 26 TOPS) — vision-CNN accelerator.
- **[AI HAT+ 2](../sources/raspberry-pi-ai-hat-plus-2.md)** (Hailo-10H, 40 TOPS INT4, 8 GB) — generative-AI / LLM / VLM accelerator.

These make a Pi 5 a viable **onboard host + NPU** for a robot — distinct from the CUDA path of a [Jetson](jetson-orin-nano.md); see [Jetson onboard compute for XLeRobot](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) and [Hailo](hailo.md) for where each fits.

## Agent-facing device support

Raspberry Pi (the company) is named an early adopter of [MHS](model-hardware-standard.md), "enabling MHS integration across a number of their products following successful tests using their **Camera MHS Driver**" ([Anthropic MHS preview](../sources/anthropic-model-hardware-standard-preview.md)). Notable because it is the only *consumer/maker-tier* hardware vendor on the list, next to Tecan, QIAGEN and Universal Robots — so the cheapest camera in this wiki's robot builds may become directly discoverable by an agent. Nothing is published yet. See [agent–hardware abstraction](../concepts/agents/agent-hardware-abstraction.md).

## Related
- [Hailo](hailo.md) — AI HAT accelerator silicon.
- [XLeRobot](xlerobot.md), [LeKiwi](lekiwi.md), [Grievous](grievous.md) — Pi-hosted robot builds.
- [Jetson Orin Nano](jetson-orin-nano.md) — the CUDA alternative to a Pi-5-as-brain.

## Mentioned in
- [Raspberry Pi AI HAT+ 2 (Hailo-10H)](../sources/raspberry-pi-ai-hat-plus-2.md)
- [Nori Robotics — Y Combinator company profile (S26)](../sources/nori-robotics-yc-profile.md)
- [Previewing the Model Hardware Standard](../sources/anthropic-model-hardware-standard-preview.md) — Raspberry Pi's Camera MHS Driver
