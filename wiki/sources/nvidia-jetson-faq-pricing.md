---
title: NVIDIA Jetson FAQ — price list, and the 2026 price increases
type: source
url: https://developer.nvidia.com/embedded/faq
author: NVIDIA
published: 2026-07-21
ingested: 2026-09-28
format: web (FAQ section "What is the price of Jetson products?"), live capture + four Wayback Machine captures
local_path: raw/2026-09-28-nvidia-jetson-faq-pricing.md
sha256: b7db3eef2d1c55a678615a34d8555110ddcec9da08b921c543c066b687a4c673
tags: [nvidia, jetson, pricing, price-increase, jetson-thor, agx-orin, orin-nx, orin-nano, t5000, t4000, buying-decision, memory-costs]
---

## Summary

NVIDIA's Jetson FAQ carries the company's own price list: **MSRP for developer kits** and **"volume suggested pricing at 1KU+"** for production modules. Between **2026-07-06 and 2026-07-29**, NVIDIA raised the price of **every current-generation Jetson (Orin and Thor) by 20–75%**, with no announcement, no changelog, and no date on the page. The news coverage dates it to **2026-07-21**, when the change appeared on the US Marketplace and the FAQ. A separate, earlier step (between **2026-06-22 and 2026-07-06**) had already raised the legacy parts (Xavier, TX2, Nano) by 17–54%. This page records the FAQ table before and after, reconstructed from Wayback Machine captures so that it rests on NVIDIA's own figures rather than on the press.

> [!warning] The "up to 101%" headline is not in NVIDIA's list
> Every news article carries "up to 101%", which comes from the **Jetson Nano module going $99 → $199** (and "AGX Orin 32 GB $899 → $1,799, +100%") ([CNX Software](https://www.cnx-software.com/2026/07/22/nvidia-increases-the-price-of-jetson-modules-and-devkits-by-up-to-101/), repeated by VideoCardz, Notebookcheck, Hackster and Hardware Busters). **Neither baseline appears in the FAQ in 2026.** The captures show the **Jetson Nano module at $129 (May and June) → $199 (July 6)**, which is +54% and happened *before* the July 21 change, and the **AGX Orin 32 GB module at $1,099 → $1,799 (+64%)**. The $99 and $899 figures were likely read from an older price list or a different page. The five outlets are **one origin**, per the wiki's [primary-source rule](../../CLAUDE.md). By NVIDIA's own table, **the largest single increase is the AGX Orin Developer Kit, $1,999 → $3,499 (+75%)**.

## Key claims

### The current-generation increase (between 2026-07-06 and 2026-07-29)

| Product | Before (2026-07-06) | **After (2026-07-29, still current 2026-09-28)** | Change | Basis |
|---|---|---|---|---|
| **Jetson AGX Thor Developer Kit** | $3,499 | **$5,499** | **+57%** | MSRP |
| Jetson T5000 module | $3,499 | **$4,999** | +43% | 1KU+ |
| Jetson T4000 module | $2,499 | **$2,999** | +20% | 1KU+ |
| **Jetson AGX Orin Developer Kit** (64 GB) | $1,999 | **$3,499** | **+75%** | MSRP |
| Jetson AGX Orin 64 GB module | $1,999 | **$2,999** | +50% | 1KU+ |
| Jetson AGX Orin Industrial | $2,899 | **$3,199** | +10% | 1KU+ |
| Jetson AGX Orin 32 GB module | $1,099 | **$1,799** | +64% | 1KU+ |
| **Jetson Orin NX 16 GB module** | $699 | **$999** | **+43%** | 1KU+ |
| Jetson Orin NX 8 GB module | $449 | **$649** | +45% | 1KU+ |
| **Jetson Orin Nano Super Developer Kit** | $249 | **$399** | **+60%** | MSRP |
| Jetson Orin Nano 8 GB module | $249 | **$399** | +60% | 1KU+ |
| Jetson Orin Nano 4 GB module | $229 | **$349** | +52% | 1KU+ |

The FAQ prose changed in step: *"The price of the Jetson AGX Orin developer kit with 64GB of memory is **$1999**"* (07-06) → *"**$3499**"* (07-29).

### The earlier legacy increase (between 2026-06-22 and 2026-07-06)

| Product | 2026-05-13 and 2026-06-22 | 2026-07-06 onward | Change |
|---|---|---|---|
| Jetson AGX Xavier module | $1,099 | $1,599 | +45% |
| Jetson AGX Xavier Industrial | $1,549 | $2,299 | +48% |
| Jetson Xavier NX 16 GB module | $649 | $899 | +39% |
| Jetson Xavier NX module | $479 | $599 | +25% |
| Jetson TX2 NX module | $179 | $249 | +39% |
| Jetson TX2i module | $849 | $999 | +18% |
| Jetson Nano module | $129 | $199 | +54% |

Orin and Thor prices were **unchanged** across the 05-13, 06-22 and 07-06 captures.

### What the list does not tell you

- **"1KU+" is volume pricing.** Single-unit module prices from distributors can differ, usually upward. The wiki's older **"~$600" Orin NX 16 GB** figure was already below the FAQ's pre-increase $699 1KU price, so it was probably a distributor or street price. **There is no current single-unit module price from NVIDIA.**
- **The Thor T3000 and T2000** ([announced 2026-07](nvidia-jetson-thor-t3000-t2000-blog.md)) are **not in the FAQ table**. No price is recorded.
- **Carrier-board vendors.** Coverage says Seeed and others passed the increase through, but no vendor price list is ingested. The wiki's recommended Orin NX box (Seeed reComputer J4012) has **no recorded price**.
- **Why.** NVIDIA gave no reason. Coverage attributes it to **LPDDR memory costs** and supply constraints. That is plausible but unconfirmed, and the percentages don't simply follow memory size: the 32 GB AGX Orin module rose more (+64%) than the 64 GB one (+50%).

## Entities mentioned

- [NVIDIA](../entities/nvidia.md); [Jetson Thor](../entities/jetson-thor.md), [Jetson AGX Orin](../entities/jetson-agx-orin.md), [Jetson Orin NX](../entities/jetson-orin-nx.md), [Jetson Orin Nano](../entities/jetson-orin-nano.md), [DGX Spark](../entities/dgx-spark.md) (for comparison only; not in the FAQ).

## Concepts touched

- [Jetson module ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md) and [onboard compute for XLeRobot](../syntheses/platforms/jetson-onboard-compute-xlerobot.md): every price column in the wiki's buying analyses.
- [VLA deployability landscape](../syntheses/platforms/vla-deployability-landscape.md): the "compute often costs more than the robot" tension widens.

## Edition history

- **Captures used:** Wayback 2026-05-13 12:46:20 and 2026-06-22 12:43:47 (identical price tables); 2026-07-06 16:06:07 (legacy step applied, Orin/Thor unchanged); 2026-07-29 11:33:09 (Orin/Thor step applied); live 2026-09-28 (same as 07-29). The 06-22, 07-06 and 07-29 tables and the full live text are in `raw/2026-09-28-nvidia-jetson-faq-pricing.md`.
- **Re-checking:** the FAQ is HTML with no version marker, so it has no `fetch_url` here. The drift script would hash-mismatch on every fetch. To re-check, fetch the FAQ and compare the price section against §1 of the raw capture, or list new Wayback captures with `web.archive.org/cdx/search/cdx?url=developer.nvidia.com/embedded/faq`.

## Open questions

- **Is the increase temporary?** Nothing on the page says so. Re-check the FAQ periodically, especially if LPDDR prices ease.
- **What do the T3000 / T2000 cost?**
- **Single-unit prices** for the Orin NX 16 GB module and the reComputer J4012 as of now.
- **Did the DGX Spark's price move too?** It uses the same LPDDR5X class, but it is not a Jetson and not in this table.
