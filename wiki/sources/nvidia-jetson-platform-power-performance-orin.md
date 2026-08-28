---
title: Jetson Linux Developer Guide — Platform Power and Performance (Orin series)
type: source
url: https://docs.nvidia.com/jetson/archives/r36.5/DeveloperGuide/SD/PlatformPowerAndPerformance/JetsonOrinNanoSeriesJetsonOrinNxSeriesAndJetsonAgxOrinSeries.html
author: NVIDIA Corporation
published: undated (R36.5 Developer Guide chapter)
ingested: 2026-05-16
tags: [jetson, jetson-orin-nano, jetson-orin-nx, jetson-agx-orin, nvpmodel, super-mode, power-modes, performance]
---

## Summary
The authoritative chapter on Jetson Orin power modes — defines **Super Mode** (formerly **MAXN_SUPER**) as an experimental, unconstrained mode unlocking higher CPU / GPU / DLA / memory clocks than the standard nvpmodel profiles, and tabulates every `nvpmodel` mode ID per module variant (Orin Nano 4GB / 8GB, Orin NX 8GB / 16GB, AGX Orin 32GB / 64GB). Super Mode access is **hardware-locked at flash time**: the `-super` (or `-super-maxn`) `.conf` variant must be used when flashing or the module physically cannot enter the higher power profiles. Mode switching at runtime is `sudo nvpmodel -m <id>` (persistent across reboots and SC7). The chapter also documents the OC3 87.5%-throttle behavior and recommends the `-maxn` flash variant — with more conservative thermal settings — for sustained heavy workloads.

> [!note]
> Tables below extracted via WebFetch summarization. Specific frequency values should be verified against the live document before being relied on for hardware planning.

## Key claims

### Super Mode = MAXN_SUPER

- "An experimental mode that allows a maximum number of cores and clock frequency for CPU, GPU, DLA, PVA, and SOC engines."
- "The difference between MAXN and MAXN_SUPER is the maximum frequency of CPU, GPU, DLA, and EMC."
- Access is **hardware-variant + flash-config dependent**: a module flashed with `jetson-orin-nano-devkit.conf` cannot enter MAXN_SUPER. Flashing with `jetson-orin-nano-devkit-super.conf` (or `…-super-maxn.conf`) unlocks the higher profiles.

### nvpmodel power-mode tables

Mode IDs are **not portable across modules** — ID 0 means different things on Orin Nano 4GB vs 8GB vs Orin NX. Always cross-reference per-module.

#### Jetson Orin Nano 4GB

| Flash variant | Name | Power | Mode ID | Cores | CPU max (MHz) | GPU max (MHz) | Mem max (MHz) |
|---|---|---|---|---|---|---|---|
| Standard | 10W (default) | 10W | 0 | 6 | 1510.4 | 624.75 | 2133 |
| Standard | 7W_AI | 7W | 1 | 4 | 806.4 | 408 | 2133 |
| Standard | 7W_CPU | 7W | 2 | 4 | 960 | 306 | 2133 |
| Super | 10W | 10W | 0 | 6 | 1497.6 | 612 | 2133 |
| Super | 25W | 25W | 1 | 6 | 1728 | 1020 | 3199 |
| Super | MAXN_SUPER | n/a | 2 | 6 | 1728 | 1020 | 3199 |

#### Jetson Orin Nano 8GB

| Flash variant | Name | Power | Mode ID | Cores | CPU max (MHz) | GPU max (MHz) | Mem max (MHz) |
|---|---|---|---|---|---|---|---|
| Standard | 15W (default) | 15W | 0 | 6 | 1510.4 | 624.75 | 2133 |
| Standard | 7W | 7W | 1 | 4 | 960 | 408 | 2133 |
| Super | 15W | 15W | 0 | 6 | 1497.6 | 612 | 2133 |
| Super | 25W | 25W | 1 | 6 | 1344 | 918 | 3199 |
| Super | MAXN_SUPER | n/a | 2 | 6 | 1728 | 1020 | 3199 |

Headline 8GB Super-vs-standard uplift (25W Super vs 15W standard):
- **GPU**: 624.75 → 918 MHz (**+47%**)
- **Memory**: 2133 → 3199 MHz (**+50%**)
- CPU clock actually drops a touch (1510.4 → 1344 MHz) at 25W; full peak CPU only at MAXN_SUPER.

#### Jetson Orin NX 8GB

| Flash variant | Name | Power | Mode ID | Cores | CPU max | GPU max | DLA max | Mem max |
|---|---|---|---|---|---|---|---|---|
| Standard | MAXN | n/a | 0 | 6 | 1984 | 765 | 614.4 | 3200 |
| Standard | 10W | 10W | 1 | 4 | 1190.4 | 612 | 153.6 | 2133 |
| Standard | 15W | 15W | 2 | 4 | 1420.8 | 612 | 614.4 | 3200 |
| Standard | 20W | 20W | 3 | 6 | 1497.6 | 408 | 614.4 | 3200 |
| Super | MAXN_SUPER | n/a | 0 | 6 | 1984 | 1173 | 1228.8 | 3200 |
| Super | 40W | 40W | 4 | 6 | 1984 | 1173 | 1203.2 | 3200 |

#### Jetson Orin NX 16GB

| Flash variant | Name | Power | Mode ID | Cores | CPU max | GPU max | DLA max | Mem max |
|---|---|---|---|---|---|---|---|---|
| Standard | MAXN | n/a | 0 | 8 | 1984 | 918 | 614.4 | 3200 |
| Standard | 10W | 10W | 1 | 4 | 1190.4 | 612 | 153.6 | 2133 |
| Standard | 15W | 15W | 2 | 4 | 1420.8 | 612 | 614.4 | 3200 |
| Standard | 25W | 25W | 3 | 8 | 1497.6 | 408 | 614.4 | 3200 |
| Super | MAXN_SUPER | n/a | 0 | 8 | 1984 | 1173 | 1228.8 | 3200 |
| Super | 40W | 40W | 4 | 8 | 1497.6 | 1173 | 908.8 | 3200 |

#### Jetson AGX Orin 32GB

| Name | Power | Mode ID | Cores | CPU max | GPU max | DLA max | Mem max |
|---|---|---|---|---|---|---|---|
| MAXN (default) | n/a | 0 | 8 | 2188.8 | 930.75 | 1408 | 3200 |
| 15W | 15W | 1 | 4 | 1113.6 | 408 | 614.4 | 2133 |
| 30W | 30W | 2 | 8 | 1728 | 612 | 1369.6 | 3200 |
| 40W | 40W | 3 | 8 | 1497.6 | 816 | 1228.8 | 3200 |

#### Jetson AGX Orin 64GB

| Name | Power | Mode ID | Cores | CPU max | GPU max | DLA max | Mem max |
|---|---|---|---|---|---|---|---|
| MAXN (default) | n/a | 0 | 12 | 2201.6 | 1301 | 1600 | 3200 |
| 15W | 15W | 1 | 4 | 1113.6 | 408 | 614.4 | 2133 |
| 30W | 30W | 2 | 8 | 1728 | 612 | 1369.6 | 3200 |
| 50W | 50W | 3 | 12 | 1497.6 | 816 | 1369.6 | 3200 |

### Mode switching at runtime

```bash
sudo /usr/sbin/nvpmodel -m <mode-id>   # set
sudo /usr/sbin/nvpmodel -q             # query current
```

- **Persistence**: "After you set a power mode, the module stays in that mode until you change it. The mode persists across power cycles and SC7."
- **Reboot edge case**: changing GPU `tpc_pg_mask` requires reboot because the GPU "golden context" is created once.
- **Custom modes**: edit `/etc/nvpmodel.conf`. **Unit quirk**: CPU frequency in **kHz**, GPU and EMMC in **Hz**.

### Thermal / throttling caveats

- "We don't recommend running heavy workloads for prolonged periods in [MAXN] mode."
- For sustained heavy use, flash with the **`-maxn`** suffix variant which applies "more conservative thermal settings."
- Hardware OC3 throttle: CPU and GPU both throttle to **87.5%** when instantaneous power thresholds are exceeded.
- EMC / SCF / hub clocks differ slightly between standard and MAXN-optimized flash configs (standard EMC 3199 MHz, MAXN-optimized 3200 MHz; SCF 933 vs 1067 MHz).

### Flash-config variants (Orin Nano example)

- `jetson-orin-nano-devkit.conf` — standard envelopes; cannot reach 25W or MAXN_SUPER.
- `jetson-orin-nano-devkit-super.conf` — unlocks Super profiles.
- `jetson-orin-nano-devkit-super-maxn.conf` — Super profiles + conservative thermal config for sustained MAXN_SUPER workloads.

## Entities mentioned
- [Jetson Orin NX](../entities/jetson-orin-nx.md) — the module whose Super-Mode and nvpmodel tables this chapter defines.
- [Jetson Orin Nano](../entities/jetson-orin-nano.md)
- [Jetson Linux](../entities/jetson-linux.md)
- [NVIDIA](../entities/nvidia.md)
- **AGX Orin** — referenced but not yet an entity page. (Orin NX filed 2026-08-28, linked above.)

## Concepts touched
- None directly. Could seed a future `concepts/robotics/edge-ai-power-budgets.md` if power-mode trade-offs become a recurring theme.

## Open questions
- The chapter does **not** quote TOPS figures per mode — only frequencies. To get TOPS per mode you'd compute from the GPU clock × per-cycle ops, or pull from a separate marketing-grade datasheet ingest.
- `tpc_pg_mask` reboot requirement: which specific mode transitions trigger it? The text implies "when the new mode has a different mask," but the per-mode masks aren't tabulated.
- DLA and PVA clocks aren't tabulated for Orin Nano (4GB / 8GB) variants — only CPU/GPU/memory. Either Orin Nano modules don't expose DLA/PVA tuning or the chapter omitted them.
- The page implies a `jetson-orin-nx-devkit-super` config exists; this isn't called out in the [R36.5 release notes table](nvidia-jetson-linux-r36-5-release-notes.md), which lists Orin NX modules only under the Orin Nano carrier configs. Worth confirming whether Orin NX has its own separate `-super` config or shares the Orin Nano one.
