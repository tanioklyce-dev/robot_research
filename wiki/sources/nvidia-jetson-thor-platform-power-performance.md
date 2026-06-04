---
title: Jetson Linux Developer Guide — Platform Power and Performance (Jetson Thor)
type: source
url: https://docs.nvidia.com/jetson/archives/r38.4/DeveloperGuide/SD/PlatformPowerAndPerformance/JetsonThor.html
author: NVIDIA Corporation
published: undated (R38.4 Developer Guide chapter)
ingested: 2026-06-03
tags: [jetson, jetson-thor, t5000, t4000, nvpmodel, maxn, power-modes, power-efficiency, performance, edge-ai]
---

## Summary
The authoritative chapter on **Jetson Thor power modes** — defines **MAXN** as the unconstrained mode (max cores/clocks, but hardware-throttles when module power exceeds the **TDP** budget) and tabulates the `nvpmodel` prequalified power-budget modes per module (**T5000**, **T4000**). The decisive fact for a battery-powered robot: **Thor's power draw is software-selectable**. On the **T5000** you can pin **70 W / 90 W / 120 W** budgets (or run uncapped MAXN up to the **130 W TDP**), trading GPU/CPU throughput for a lower, predictable power envelope. Mode switching is `sudo nvpmodel -m <id>`, persistent across reboots and SC7. The dev kit additionally enforces a **168 W total-system cap** (to protect the 140 W adapter) — separate from the module-level nvpmodel budget.

> [!note]
> Tables below extracted via WebFetch summarization of the R38.4 chapter. Specific frequencies, core counts, and the exact default mode should be verified against the live document before being relied on for hardware planning. (The fetch was ambiguous on whether the out-of-box default is MAXN or the 120 W budget — treat "default = 120 W budget (Mode 1)" as provisional.)

## Key claims

### MAXN vs fixed power-budget modes
- **MAXN (Mode 0)** — "an unconstrained power mode that allows a maximum number of cores and clock frequency," but it "does not guarantee the best performance for all use cases because hardware throttling is engaged when the total module power exceeds the TDP budget." Framed as experimental; **not** recommended for sustained heavy workloads.
- **Fixed power-budget modes** (120 W / 90 W / 70 W) are **"prequalified levels"** that balance performance against thermal/power constraints — the modes to use for sustained / production workloads.
- **Module TDP**: **130 W (T5000)**, **90 W (T4000)**.

### T5000 nvpmodel modes
| Mode ID | Name / budget | CPU cores online | CPU max | GPU (TPC / FBP) | GPU max | Mem max |
|---|---|---|---|---|---|---|
| 0 | **MAXN** (unconstrained, throttles at 130 W TDP) | 14 | 2601 MHz | 10 / 4 | 1386 MHz | 4266 MHz |
| 1 | **120 W** (default) | 14 | 2601 MHz | 10 / 4 | 1386 MHz | 4266 MHz |
| 2 | **90 W** | 14 | 2601 MHz | **6 / 3** | 1530 MHz | 4266 MHz |
| 3 | **70 W** | **12** | **1998 MHz** | **6 / 3** | 1530 MHz | 4266 MHz |

**The key trade-off:** dropping below the 120 W budget **cuts the GPU from 10 → 6 TPC (~−40%)** at Mode 2/3 (the GPU clock rises slightly, 1386 → 1530 MHz, but nowhere near compensating for losing 4 of 10 TPCs). Mode 2 (90 W) keeps the full 14-core CPU; Mode 3 (70 W) further trims CPU to 12 cores @ 1998 MHz. So for **GPU-bound VLA inference**, any sub-120 W mode is roughly a 40 %-GPU-throughput cut; for **CPU / control-loop / perception** work, 90 W is nearly free and 70 W is a modest CPU clock reduction.

### T4000 nvpmodel modes
| Mode ID | Name / budget | CPU cores | CPU max | GPU (TPC / FBP) | GPU max | Mem max |
|---|---|---|---|---|---|---|
| 0 | **MAXN** (unconstrained) | 12 | 2601 MHz | 6 / 3 | 1530 MHz | 4266 MHz |
| 1 | **70 W** (default) | 12 | 1998 MHz | 6 / 3 | 1530 MHz | 4266 MHz |

### Switching modes
```bash
sudo /usr/sbin/nvpmodel -m <x>   # set mode (0–3 on T5000; 0–1 on T4000)
sudo /usr/sbin/nvpmodel -q       # query current mode
```
- **Persistence**: the mode persists across power cycles and SC7 suspend.
- **Reboot edge case**: `gpu_pg_mask` can only be set once before GPU initialization; if a mode transition requires a different mask, **a reboot is required**.

### Module power vs total-system power
- nvpmodel budgets are **module** power (the SoC + memory).
- The dev kit's carrier monitors **total system power** via an **INA238** and enforces a **168 W cap** to keep total draw under the **140 W** adapter's capability. This cap is **independent** of the nvpmodel module budget — pinning a low nvpmodel mode reduces module draw but the 168 W system ceiling still applies to the whole board.

## Entities mentioned
- [Jetson Thor](../entities/jetson-thor.md) (T5000 / T4000)
- [Jetson Linux](../entities/jetson-linux.md)
- [NVIDIA](../entities/nvidia.md)

## Concepts touched
- None as a dedicated page yet. The Orin + Thor power-mode pages together could seed a future `concepts/robotics/edge-ai-power-budgets.md` if power-vs-throughput tuning becomes a recurring theme.

## Open questions
- **Exact default mode** (MAXN vs 120 W budget) — the fetch was ambiguous; verify on the live doc.
- **TOPS per mode** — the chapter quotes frequencies/core counts, not TOPS. Effective AI throughput per budget must be inferred from GPU TPC count × clock (≈ Mode 1/MAXN throughput × 0.6 for the 6-TPC modes, before clock adjustment).
- **Measured wall-power at each mode** under a real VLA load (GR00T / π0) — not in the doc; would convert these budget caps into actual battery-runtime numbers.
- **T4000 TDP (90 W) vs its 70 W MAXN mode** — the module TDP exceeds its top nvpmodel budget; unclear whether a higher T4000 budget exists on non-dev-kit carriers.
