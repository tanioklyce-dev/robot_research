---
title: "NVIDIA Jetson Thor Module Carrier Board — Product Specification (SP-12533-001 v1.2)"
type: source
url: https://developer.nvidia.com/embedded/downloads
local_path: raw/Jetson_Thor_Module_Carrier_Board_Spec_SP-12533-001_v1.2.pdf
author: NVIDIA (official product specification)
affiliations: NVIDIA
published: 2025-11-26
ingested: 2026-05-31
doc_id: SP-12533-001_v1.2
format: pdf
tags: [jetson-thor, agx-thor, carrier-board, hardware, primary-source, micro-fit, usb-c-pd, power, m2, can, automation-header, no-csi, no-40-pin]
---

## Summary

The **official NVIDIA carrier-board product specification** for the Jetson Thor Module Carrier Board (the AGX Thor Dev Kit board), SP-12533-001 **v1.2, Nov 26 2025**. This is the authoritative source for connector inventory, power delivery, and expansion — and it **fills the gaps** the [hardware-layout user-guide page](nvidia-jetson-agx-thor-devkit-hardware-layout.md) deferred, while **refining the power story** the wiki had assembled. The headline takeaways: a precise per-input current split (**USB-C 5 A vs Micro-Fit 15 A**), confirmation the **bundled adapter is USB-C** (Micro-Fit is the alternative), and the notable **absence of any 40-pin GPIO header or MIPI-CSI camera connector** — the Thor dev kit replaces them with CAN, an Automation Header, and high-speed Ethernet/QSFP28.

## Key claims

### Power (Chapter 6 + §3.4)
- **Main input `VCC_SRC`: 9–28 V**, with **max current 5 A over USB-C, 15 A over Micro-Fit 3.0** (Table 6-2). So Micro-Fit has ~3× the current headroom of USB-C.
- **Two USB-C ports either accept power input — and the included power adapter is USB-C** ("2× USB-C (either for power input – Power Adapter included)"). The **Micro-Fit 3.0 (J83)** is explicitly "an alternative to using the included USB Type-C power supply," 9–28 V, **3.0 mm pitch 2×2 header** (part # in the separate Supported Component List DA-12429-001).
- **First-come-first-serve power arbitration:** if both Micro-Fit and USB-C are connected, the **CYPD8225 USB-PD controller lets the first supply through** — the two inputs **cannot be summed**.
- On-board rails: Main 5 V (TPS53015), 3.3 V (TPS53015), 1.8 V buck (MP2384), **12 V buck-boost (MP28167GQ)**, a dedicated **12 V fan rail (1.5 A)**, USB-A VBUS load switches (AP22811).
- **Caution (verbatim):** "ALWAYS CONNECT THE JETSON THOR SERIES MODULE AND ALL EXTERNAL PERIPHERAL DEVICES BEFORE CONNECTING THE POWER SUPPLY TO THE DEV KIT." Board is ESD-sensitive.

> [!warning] Corrects the wiki's earlier "28 V brick via Micro-Fit" framing
> The wiki previously implied the bundled adapter feeds the Micro-Fit. Per this spec, **the included adapter is a USB-C PD supply** (28 V / 5 A = 140 W), and **Micro-Fit is the alternative DC input** — its value is **higher current (up to 15 A) and a latching connector**, letting you deliver the full board budget where USB-C's 5 A (≈140 W @ 28 V) falls ~28 W short of the 168 W ceiling. (Minor inter-doc inconsistency: the [hardware-layout page](nvidia-jetson-agx-thor-devkit-hardware-layout.md) lists Micro-Fit "up to 8 A"; this carrier spec's Table 6-2 says 15 A — trust the spec for the interface capability.)

### Module + board-to-board (§1.1–1.2)
- Module: **NVIDIA Thor**, **LPDDR5X** DRAM, DVFS, multiple power/clock domains, **Thermal Transfer Plate (TTP) + optional fan/heatsink**.
- **699-pin (11 × 65) board-to-board module connector.**
- Operating temperature: **0 °C to 35 °C**.

### Connectors (standard, Chapter 2)
- **USB:** 2× USB-A **10 Gbps** (J69, from hub) · 2× USB-C **5 Gbps** (J81/J82) · USB-C **debug** (J90).
- **Ethernet:** MGBE up to **5 Gb/s** RJ45 (J85).
- **Display:** DisplayPort + **HDMI 2.1**, stacked (J104).
- **QSFP28 (J105): 4× MGBE (XFI)** = 4×25 Gbps.

### Connectors (custom, Chapter 3)
- **M.2 Key M (J103):** PCIe ×4 + I2C, NVMe — **SSD preinstalled**.
- **M.2 Key E (J505):** PCIe ×1 + USB 2.0 + I2S + UART — **Wi-Fi/BT module preinstalled**.
- **CAN Header (J47):** 26-pin (2×13, 1.27 mm pitch), **2× CAN** (routed through a transceiver).
- **Automation Header (J42):** 12-pin (2×6, 2.54 mm pitch) — exposes **Power, Reset, Force Recovery, Sleep, Overcurrent-Throttle-Enable, Auto-Power-ON Enable**, plus WOL and JTAG_TRST. *Auto-Power-On is enabled by tying pin 5 to pin 6* (useful for headless/robot boot-on-power).
- **Button & LED Header:** 2×3, 2 mm pitch. **Fan Header:** 4-pin, 2 mm pitch (backup). **Audio Panel Header (J511).**
- **RTC Backup Battery Connector (J13):** 2-pin, 1.25 mm pitch (`PMIC_BBATT`).
- **Not supported:** J87, J91, J502.

> [!note] No 40-pin GPIO header and no MIPI-CSI camera connectors
> Neither appears anywhere in this spec (0 hits for "40-pin", "CSI", "MIPI", "camera"). The AGX Thor Dev Kit **drops the classic Jetson 40-pin expansion header and the onboard CSI camera connectors** that the Orin generation had. In their place: a **CAN header**, an **Automation Header**, and the **QSFP28 (4×25 Gbps) + 5 GbE** networking — consistent with NVIDIA's **CSI-over-Ethernet (Holoscan Sensor Bridge)** sensor-ingest model in JetPack 7 (already noted on the [Jetson Thor entity](../entities/jetson-thor.md)). Cameras and low-speed GPIO peripherals are expected over Ethernet/USB/CAN, not ribbon cables and a pin header.

## Entities mentioned
- [Jetson Thor](../entities/jetson-thor.md) — the module + carrier board documented here.

## Why this matters for the wiki
- **Upgrades the power facts to a precise primary source** and **corrects** the bundled-adapter framing (USB-C, not Micro-Fit) plus the per-input current limits (USB-C 5 A / Micro-Fit 15 A) and the first-come-first-serve arbitration — all directly relevant to the [XLeRobot + Thor power budget](../syntheses/projects/xlerobot-thor-power-budget.md).
- **Resolves the carrier-layout open questions** (40-pin? CSI? Key E? fan? CAN? RTC?) the [hardware-layout source](nvidia-jetson-agx-thor-devkit-hardware-layout.md) had flagged.
- **The "no 40-pin / no CSI" finding is a real integration constraint** for anyone porting an Orin-era robot wiring harness to Thor — sensors must move to Ethernet/USB/CAN.

## Open questions
- Exact **Micro-Fit part number** is deferred to the **Supported Components List DA-12429-001** — a **download-gated PDF** on the [Jetson Download Center](https://developer.nvidia.com/embedded/downloads) (the dev-kit "Supported Hardware" web page is just a redirect to it; confirmed empty 2026-05-31). The wiki records the board-side part `2147561041` from a forum thread; reconcile against the SCL once the PDF is downloaded to `raw/` and ingested.
- The **8 A (layout page) vs 15 A (this spec, Micro-Fit)** input-current discrepancy — likely "rated dev-kit draw" vs "connector capability"; worth confirming.
- The **Jetson Thor Series Modules Design Guide** (referenced for routing) would be the next doc for anyone designing a custom carrier.
