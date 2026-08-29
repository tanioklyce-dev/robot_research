---
title: "Jetson module ladder — performance and power, Orin Nano 4 GB → AGX Thor T5000"
type: synthesis
created: 2026-07-26
updated: 2026-08-17
tags: [jetson, jetson-orin-nano, orin-nx, agx-orin, jetson-thor, nvpmodel, power-modes, perf-per-watt, edge-ai, hardware, reference, platforms]
---

# Jetson module ladder — performance and power

A hardware-neutral reference for **every Jetson SKU the wiki tracks**, from the 7 W Orin Nano 4 GB to the 130 W AGX Thor T5000 — specs, price, `nvpmodel` power modes, perf-per-watt, and the measured workload numbers that exist. Assembled entirely from wiki sources; nothing here is new external research.

Two existing pages cover *slices* of this and remain the place to go for a decision:
- [Onboard compute for XLeRobot](jetson-onboard-compute-xlerobot.md) — the same ladder narrowed to one SKU per tier and framed by a 288 Wh battery budget.
- [GR00T inference on Jetson](gr00t-inference-on-jetson.md) — measured VLA throughput per tier.

This page is the **superset table** underneath both: all SKUs, both `nvpmodel` chapters merged, and an explicit list of what the wiki doesn't know.

> [!warning] Cross-generation numbers are not comparable
> The Orin ladder quotes **INT8 TOPS (sparse)**; Thor quotes **FP4 TFLOPS (sparse)**. These are different units at different precisions — "2070 vs 275" is not a 7.5× ratio in any single metric. NVIDIA's own relative anchors are **7.5× AI compute and 3.5× energy efficiency vs AGX Orin** ([Thor product page](../../sources/nvidia-jetson-thor-product-page.md)); the wiki has no independent verification of either.

## 1. The full ladder

| Module | Arch | GPU | CPU | Memory | Bandwidth | AI perf | Power | Price (wiki-recorded) | SDK |
|---|---|---|---|---|---|---|---|---|---|
| **Orin Nano 4 GB** | Ampere | 512-core / 16 TC | 6× A78AE | 4 GB 64-bit LPDDR5 | 51 GB/s | 34 TOPS | 7 / 10 / 25 W | — | JetPack 7.2+ ¹ |
| **Orin Nano 8 GB** | Ampere | 1024-core / 32 TC | 6× A78AE | 8 GB 128-bit LPDDR5 | 102 GB/s | 67 TOPS | 7 / 15 / 25 W | **~$249** dev kit | JetPack 7.2+ ¹ |
| **Orin NX 8 GB** | Ampere | 1024-core / 32 TC **+ 1 DLA** ⁴ | 6× A78AE | 8 GB 128-bit LPDDR5 | 102.4 GB/s | 117 TOPS | 10–25 W (40 W Super) | — | JetPack 7.2+ ¹ |
| **Orin NX 16 GB** | Ampere | 1024-core / 32 TC **+ 2 DLA** ⁴ | 8× A78AE | 16 GB 128-bit LPDDR5 | 102.4 GB/s | 157 TOPS | 10–40 W | **~$600** module | JetPack 7.2+ ¹ |
| **AGX Orin 32 GB** | Ampere | 1792-core / 56 TC **+ 2 DLA** | 8× A78AE | 32 GB 256-bit LPDDR5 | 204.8 GB/s | 200 → **241 TOPS** (MAXN_SUPER, JP7.2) | 15–60 W | — | JetPack 7.2+ ¹ |
| **AGX Orin 64 GB** | Ampere | 2048-core / 64 TC **+ 2 DLA** | 12× A78AE | 64 GB 256-bit LPDDR5 | 204.8 GB/s | 275 TOPS | 15–60 W (≤75 W MAXN per some listings) | **~$1,999** dev kit | JetPack 7.2+ ¹ |
| **AGX Thor T4000** | **Blackwell** | 1536-core / 5th-gen TC | 12× Neoverse-V3AE | 64 GB 256-bit LPDDR5X | 273 GB/s | **1200 FP4 TFLOPS** | 40–70 W (**90 W TDP**) | — | **JetPack 7** |
| **AGX Thor T5000** | **Blackwell** | 2560-core / 5th-gen TC | 14× Neoverse-V3AE | 128 GB 256-bit LPDDR5X | 273 GB/s | **2070 FP4 TFLOPS** | 40–130 W (**130 W TDP**) | **$3,499** dev kit | **JetPack 7** |

¹ **Corrected 2026-08-16.** These rows read *"JetPack 6"* until today. **JetPack 7.2 (Jetson Linux r39.2, **2026-06-02**) extends JetPack 7 to the entire Orin family** (Ubuntu 24.04 / kernel 6.8 / **CUDA 13.2.1** / TensorRT 10.16.2), unifying the toolchain with Thor; **7.2.1** followed 2026-08-12. Consequences: the Orin Nano dev kit **no longer has an SD-card image** (unified ISO from USB installs to microSD or NVMe); **Isaac ROS is listed "Coming soon"** on 7.2, which gates ROS robots on JetPack 6; and **AGX Orin 32 GB gains Super Mode (MAXN_SUPER), 200 → 241 TOPS**. Primary source: [JetPack 7.2 / Jetson Linux 39.2](../../sources/nvidia-jetpack-7-2-release.md).

Sources: module ladder from the [Seeed selection guide](../../sources/seeed-jetson-selection-guide.md) (cross-checked against NVIDIA-official); Thor SKU specs from the [Thor product page](../../sources/nvidia-jetson-thor-product-page.md); TDPs from the [Thor power-modes chapter](../../sources/nvidia-jetson-thor-platform-power-performance.md); prices from [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) / [XLeRobot onboard-compute](jetson-onboard-compute-xlerobot.md) / the [Thor launch newsroom](../../sources/nvidia-jetson-thor-launch-newsroom.md).

> [!note] Orin AI-perf figures are the **Super** numbers
> [!warning] ⁴ **Corrected 2026-08-28, confirmed 2026-08-29 — the 8 GB has 1 DLA, not 2, and the headline TOPS is mostly DLA anyway.**
> This table read "+2 DLA" for **both** Orin NX SKUs. NVIDIA's per-SKU DLA INT8 row is **80 TOPS (16 GB) vs 40 TOPS (8 GB)**, and a colspan-aware read of the DL-accelerator row confirms it: **2× NVDLA v2 through the Orin NX 16 GB, 1× on the 8 GB**. (The 2026-08-28 note hedged this as unresolved on the strength of a mis-parsed table; it is resolved.) All Orin NX and AGX Orin modules also carry **1× PVA v2**. See [Jetson Orin NX](../../entities/jetson-orin-nx.md) and [Jetson AGX Orin](../../entities/jetson-agx-orin.md).
>
> More consequential for every number below: **157 = 77 (GPU tensor cores) + 80 (DLA)**, both **SPARSE INT8**. A stock PyTorch/TensorRT-on-GPU pipeline — every VLA in this wiki — does not touch the DLAs, and without 2:4 structured sparsity the GPU delivers **38 dense INT8 TOPS**, about **24% of the headline**. The TOPS/W column below is therefore **GPU+DLA+sparse throughout**; it is fine for ranking modules against each other (they are all quoted the same way) and **wrong as an estimate of what one workload will see**.
>
> **The same arithmetic runs up the AGX tier**, where the DLA share is 37–46%: AGX Orin 64 GB is **170 GPU + 105 DLA = 275**; Industrial **156 + 92 = 248**; AGX Orin 32 GB **108 + 92 = 200** — so **46% of the 32 GB's headline is DLA**, and its dense-GPU figure (54 TOPS) is 27% of the number on the box. See [Jetson AGX Orin](../../entities/jetson-agx-orin.md).

> 34 / 67 / 117 / 157 TOPS require a module flashed with a `-super` config and JetPack 6.2+. Standard-flash values are materially lower — the wiki records **Orin NX 16 GB at 100 TOPS standard vs 157 Super** ([XLeRobot onboard-compute](jetson-onboard-compute-xlerobot.md)). Standard-flash figures for the other Orin SKUs are not recorded in the wiki. See §3 on the flash-time lock-in.

> [!warning] Added 2026-08-17 — Super Mode is also a *carrier* decision, not only a flash-time one
> Seeed's own flash guide for the **J401** carrier (the board under the reComputer J4012, this wiki's Orin NX recommendation) says: **"if you are using an Orin NX 16GB/8GB module, do not enable MAXN SUPER mode. The cooling capacity of the reComputer J401 carrier board is insufficient to support it"** ([Seeed flash guide](../../sources/seeed-j401-flash-jetpack.md)). Seeed separately markets the **reComputer Super J4012 at 157 TOPS in Super MAXN**. Same silicon, two sanctioned ceilings — the variable is the carrier's cooling. **So the 157 TOPS row above is only reachable on a carrier that can dissipate it**, and every TOPS/W figure below inherits that condition. Which Seeed SKUs qualify is not documented in one place; the Robotics J30/40 (quoted elsewhere at 157 TOPS / 40 W / 60 °C) has no primary in the wiki yet.

> [!warning] Added 2026-08-17 — the 7 W and 10 W modes have an open crash bug on JetPack 7.2
> [Jetson Linux r39.2 release notes](../../sources/nvidia-jetson-linux-r39-2-release-notes.md), known issue **6236259**: on Orin platforms, reducing EMC below Fmax (~3200 MHz) via `nvpmodel.service` during systemd initialization "can cause system crashes upon reboot," and this is "especially noticeable when a display is connected, regardless of its resolution." The affected modes are exactly the low-power ones this ladder exists to compare — **Orin Nano 8 GB @ 7 W, Orin NX 8/16 GB @ 10 W, AGX Orin 32/64 GB/Industrial @ 15 W** (all dropping EMC 3200 → 2133 MHz). NVIDIA's workaround is to switch to MAXN before rebooting and reapply the desired mode afterwards — awkward to automate on a headless robot, and the notes do not say whether headless operation avoids the bug.

### Announced but not shipping — the lower Thor tiers

NVIDIA extended Thor *downward* in July 2026 ([T3000/T2000 blog](../../sources/nvidia-jetson-thor-t3000-t2000-blog.md)). These are **GA Q1 2027**, emulation-only before that, and **no power figures or prices have been published**:

| Module | AI perf | Memory | CPU | Notes |
|---|---|---|---|---|
| **Jetson T3000** | 865 FP4 TFLOPS | 32 GB LPDDR5X (273 GB/s) | 8-core Neoverse | 25 GbE; ~50 % smaller / lower power than T5000; NVIDIA claims "inference comparable to T5000 for multimodal workloads" |
| **IGX T3000** | = T3000 | 32 GB | — | Adds integrated functional safety + [NVIDIA Halos](../../entities/nvidia-halos.md) for Robotics |
| **Jetson T2000** | 400 FP4 TFLOPS | 16 GB | — | Entry-level Thor architecture |

If the "~50 % lower power than T5000" claim holds, T3000 lands near the AGX Orin power class with Blackwell/JetPack 7 — which would be the first Thor-architecture part that fits a battery robot without software-capping. **Unverified; the blog does not quantify it.**

## 2. Perf per watt

Within the Orin family the units are consistent, so the ratio is meaningful:

| Module | AI perf (Super) | Top sustained power | **TOPS/W** |
|---|---|---|---|
| Orin Nano 4 GB | 34 TOPS | 25 W | **1.4** |
| Orin Nano 8 GB | 67 TOPS | 25 W | **2.7** |
| Orin NX 8 GB | 117 TOPS | 40 W | **2.9** |
| Orin NX 16 GB | 157 TOPS | 40 W | **3.9** |
| AGX Orin 32 GB | 200 → **241** TOPS ² | 60 W | 3.3 → **4.0** ² |
| AGX Orin 64 GB | 275 TOPS | 60 W | **4.6** |
| AGX Thor T4000 | 1200 FP4 TFLOPS | 70 W | *different unit* |
| AGX Thor T5000 | 2070 FP4 TFLOPS | 130 W | *different unit* |

Two things fall out:

- **Efficiency rises monotonically up the Orin ladder except at AGX Orin 32 GB**, which is *less* efficient than the Orin NX 16 GB (3.3 vs 3.9 TOPS/W) because it pays the AGX-class 60 W envelope for only 1.27× the TOPS. The 32 GB AGX buys you **memory and IO**, not efficiency.

> [!warning] ² JetPack 7.2 inverts this finding, narrowly
> [JetPack 7.2](../../sources/nvidia-jetpack-7-2-release.md) *"adds support for Jetson AGX Orin 32GB Super Mode (MAXN_SUPER) increasing performance from 200 TOPS to 241 TOPS."* At the same 60 W that is **4.0 TOPS/W**, which edges past the Orin NX 16 GB's 3.9 and **removes the dip in the ladder** this bullet was built on.
>
> How much to read into it: **not much, and it does not move the buying advice.** The margin (4.0 vs 3.9) is inside the noise of a metric built from vendor headline TOPS over max-mode wattage, and the *reason* to prefer Orin NX 16 GB for a battery robot was never efficiency alone — it is the **10–40 W envelope, the drop-in carrier compatibility, and the price**, none of which changed. What the bullet can no longer say is that the 32 GB AGX buys memory and IO *at an efficiency penalty*; on 7.2 it does not.
- **Orin NX 16 GB is the efficiency sweet spot of the Ampere ladder** at module level (3.9 TOPS/W) — narrowly, since JP7.2's Super Mode puts AGX Orin 32 GB at ~4.0 (above) — with AGX Orin 64 GB the peak (4.6). Still consistent with the XLeRobot page landing on Orin NX 16 GB as the battery-robot upgrade, which rests on the **power envelope and carrier compatibility**, not on the TOPS/W dip.

> [!warning] These are peak-marketing TOPS over a nominal power budget
> Not measured throughput per measured wall-watt. The [Orin](../../sources/nvidia-jetson-platform-power-performance-orin.md) and [Thor](../../sources/nvidia-jetson-thor-platform-power-performance.md) power chapters both quote **frequencies and core counts, never TOPS per mode** — so per-mode efficiency cannot be derived from wiki sources without assumptions. Both source pages flag this as an open question.

## 3. Unified `nvpmodel` power-mode ladder

The two Developer Guide chapters merged. **Mode IDs are not portable across modules** — ID 1 means 7 W on an Orin Nano 8 GB, 10 W on an Orin NX, 15 W on an AGX Orin, and 120 W on a Thor T5000. Always cross-reference per module.

Runtime switching is identical across the whole line, and persists across reboot and SC7:

```bash
sudo /usr/sbin/nvpmodel -m <mode-id>   # set
sudo /usr/sbin/nvpmodel -q             # query
```

### Orin series ([R36.5 chapter](../../sources/nvidia-jetson-platform-power-performance-orin.md))

**Orin Nano 4 GB**

| Flash | Name | Power | ID | Cores | CPU max | GPU max | Mem max |
|---|---|---|---|---|---|---|---|
| Standard | 10W (default) | 10 W | 0 | 6 | 1510.4 | 624.75 | 2133 |
| Standard | 7W_AI | 7 W | 1 | 4 | 806.4 | 408 | 2133 |
| Standard | 7W_CPU | 7 W | 2 | 4 | 960 | 306 | 2133 |
| Super | 10W | 10 W | 0 | 6 | 1497.6 | 612 | 2133 |
| Super | 25W | 25 W | 1 | 6 | 1728 | 1020 | 3199 |
| Super | MAXN_SUPER | n/a | 2 | 6 | 1728 | 1020 | 3199 |

**Orin Nano 8 GB**

| Flash | Name | Power | ID | Cores | CPU max | GPU max | Mem max |
|---|---|---|---|---|---|---|---|
| Standard | 15W (default) | 15 W | 0 | 6 | 1510.4 | 624.75 | 2133 |
| Standard | 7W | 7 W | 1 | 4 | 960 | 408 | 2133 |
| Super | 15W | 15 W | 0 | 6 | 1497.6 | 612 | 2133 |
| Super | 25W | 25 W | 1 | 6 | 1344 | 918 | 3199 |
| Super | MAXN_SUPER | n/a | 2 | 6 | 1728 | 1020 | 3199 |

**Orin NX 8 GB** (DLA column appears from here up)

| Flash | Name | Power | ID | Cores | CPU max | GPU max | DLA max | Mem max |
|---|---|---|---|---|---|---|---|---|
| Standard | MAXN | n/a | 0 | 6 | 1984 | 765 | 614.4 | 3200 |
| Standard | 10W | 10 W | 1 | 4 | 1190.4 | 612 | 153.6 | 2133 |
| Standard | 15W | 15 W | 2 | 4 | 1420.8 | 612 | 614.4 | 3200 |
| Standard | 20W | 20 W | 3 | 6 | 1497.6 | 408 | 614.4 | 3200 |
| Super | MAXN_SUPER | n/a | 0 | 6 | 1984 | 1173 | 1228.8 | 3200 |
| Super | 40W | 40 W | 4 | 6 | 1984 | 1173 | 1203.2 | 3200 |

**Orin NX 16 GB**

| Flash | Name | Power | ID | Cores | CPU max | GPU max | DLA max | Mem max |
|---|---|---|---|---|---|---|---|---|
| Standard | MAXN | n/a | 0 | 8 | 1984 | 918 | 614.4 | 3200 |
| Standard | 10W | 10 W | 1 | 4 | 1190.4 | 612 | 153.6 | 2133 |
| Standard | 15W | 15 W | 2 | 4 | 1420.8 | 612 | 614.4 | 3200 |
| Standard | 25W | 25 W | 3 | 8 | 1497.6 | 408 | 614.4 | 3200 |
| Super | MAXN_SUPER | n/a | 0 | 8 | 1984 | 1173 | 1228.8 | 3200 |
| Super | 40W | 40 W | 4 | 8 | 1497.6 | 1173 | 908.8 | 3200 |

**AGX Orin 32 GB** (no Standard/Super split — MAXN is the default mode)

| Name | Power | ID | Cores | CPU max | GPU max | DLA max | Mem max |
|---|---|---|---|---|---|---|---|
| MAXN (default) | n/a | 0 | 8 | 2188.8 | 930.75 | 1408 | 3200 |
| 15W | 15 W | 1 | 4 | 1113.6 | 408 | 614.4 | 2133 |
| 30W | 30 W | 2 | 8 | 1728 | 612 | 1369.6 | 3200 |
| 40W | 40 W | 3 | 8 | 1497.6 | 816 | 1228.8 | 3200 |

**AGX Orin 64 GB**

| Name | Power | ID | Cores | CPU max | GPU max | DLA max | Mem max |
|---|---|---|---|---|---|---|---|
| MAXN (default) | n/a | 0 | 12 | 2201.6 | 1301 | 1600 | 3200 |
| 15W | 15 W | 1 | 4 | 1113.6 | 408 | 614.4 | 2133 |
| 30W | 30 W | 2 | 8 | 1728 | 612 | 1369.6 | 3200 |
| 50W | 50 W | 3 | 12 | 1497.6 | 816 | 1369.6 | 3200 |

### Thor series ([R38.4 chapter](../../sources/nvidia-jetson-thor-platform-power-performance.md))

**T5000** — GPU is reported as **TPC / FBP** rather than clock-only:

| Name | Budget | ID | Cores | CPU max | GPU (TPC/FBP) | GPU max | Mem max |
|---|---|---|---|---|---|---|---|
| MAXN (throttles @ 130 W TDP) | uncapped | 0 | 14 | 2601 | 10 / 4 | 1386 | 4266 |
| 120W (default) | 120 W | 1 | 14 | 2601 | 10 / 4 | 1386 | 4266 |
| 90W | 90 W | 2 | 14 | 2601 | **6 / 3** | 1530 | 4266 |
| 70W | 70 W | 3 | **12** | **1998** | **6 / 3** | 1530 | 4266 |

**T4000**

| Name | Budget | ID | Cores | CPU max | GPU (TPC/FBP) | GPU max | Mem max |
|---|---|---|---|---|---|---|---|
| MAXN (90 W TDP) | uncapped | 0 | 12 | 2601 | 6 / 3 | 1530 | 4266 |
| 70W (default) | 70 W | 1 | 12 | 1998 | 6 / 3 | 1530 | 4266 |

### The three structural differences between the Orin and Thor mode systems

1. **Super Mode is locked at flash time; Thor's budgets are not.** An Orin flashed with `jetson-orin-nano-devkit.conf` **physically cannot** enter 25 W / MAXN_SUPER — you must reflash with the `-super` (or `-super-maxn`) config. Thor has no equivalent gate: all four T5000 budgets are available from any flash. **On Orin, "which power modes do I have" is a decision you make at flash time.**
2. **Orin degrades by clock; Thor degrades by GPU partition.** Every Orin low-power mode works by dropping CPU cores and clocks. Thor's sub-120 W modes instead **power-gate the GPU from 10 → 6 TPC (~−40 % GPU throughput)** while nudging the clock *up* (1386 → 1530 MHz). Practical consequence: on Thor, CPU/perception/control work is nearly free at 90 W and only modestly slower at 70 W, while **GPU-bound VLA inference takes roughly a 40 % hit at any sub-120 W mode**.
3. **Thor adds a second, independent ceiling.** nvpmodel budgets are **module** power. The Thor dev kit's carrier separately enforces a **168 W total-system cap** (INA238-monitored, protecting the 140 W adapter) that applies regardless of nvpmodel mode. Orin has no analogous documented system-level cap in the wiki.

Shared across both: **MAXN/MAXN_SUPER is explicitly not recommended for sustained heavy workloads** on either family (Orin: use the `-maxn` flash variant's conservative thermal settings; Thor: MAXN "does not guarantee the best performance" because it hardware-throttles at TDP). Orin additionally documents an **OC3 hardware throttle to 87.5 %** of CPU and GPU on instantaneous power excursions.

## 4. Measured workload throughput

The only *measured* per-tier numbers the wiki holds. Note how sparse this is relative to the spec tables above.

**GR00T N1.6-3B**, end-to-end camera→action, batch 1 ([TensorRT deployment docs](../../sources/isaac-gr00t-tensorrt-deployment-docs.md); community numbers from the [NVIDIA forum thread](../../sources/nvidia-forum-thor-realtime-vla-inference.md)):

| Platform | PyTorch eager | Official TensorRT | Community custom-CUDA |
|---|---|---|---|
| **AGX Thor** | 117 ms (8.6 Hz) | **92 ms (10.9 Hz)** | **41–45 ms (22–24 Hz)** |
| **AGX Orin 64 GB** | 300 ms (3.3 Hz) | **173 ms (5.8 Hz)** | — |
| Orin NX / Orin Nano | *not benchmarked* | *not benchmarked* | — |
| RTX 5090 (reference) | 58 ms (17.3 Hz) | 31 ms (32.1 Hz) | 12.5–13 ms (76–80 Hz) |

**Small policies on Orin Nano 8 GB**, FP16, end-to-end ([Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md)):

| Model | Latency | Max replan |
|---|---|---|
| ACT | 36 ms | **27.8 Hz** |
| Diffusion Policy | 540 ms | 1.8 Hz |
| SmolVLA (450 M) | 714 ms | 1.4 Hz |

> [!note] Which VLAs have *no* number on this ladder
> The wiki tracks far more VLAs than have ever been benchmarked on a Jetson. The [VLA deployability landscape](vla-deployability-landscape.md) scores nine of them on a latency axis, but that axis is largely **datacenter** latency — e.g. [MolmoAct2](../../entities/molmoact2.md)'s headline **55.8 Hz is a single H100**, not edge silicon. Only GR00T (AGX Orin + Thor) and the small policies (Orin Nano) appear in the tables above; π0.5 appears only via the unreplicated [community Thor result](../../sources/nvidia-forum-thor-realtime-vla-inference.md). **A VLA's "deployable" score and its on-Jetson rate are separate claims, and for most models the wiki has only the first.**
>
> Where a 4 B-class VLA would even fit is a memory question before it's a throughput one: GR00T-3B's stated **16 GB inference floor** already equals an Orin NX 16 GB's *entire shared* RAM, so anything in that class realistically means **AGX Orin 64 GB or Thor** — with Orin Nano (8 GB) excluded outright. *That placement is inference from the memory floors in §1 and §4, not a measurement.*

Reading across the two tables: **the ladder's practical break is memory, not TOPS.** Orin Nano runs ACT-class policies at real-time and 3 B VLAs not at all; AGX Orin 64 GB runs a 3 B VLA at ~6 Hz; Thor runs it at 11–23 Hz with room for concurrent models. Orin NX 16 GB sits exactly on GR00T's stated 16 GB inference floor — the [GR00T-on-Jetson page](gr00t-inference-on-jetson.md) extrapolates ~2–3 Hz there and recommends off-board serving instead. **That extrapolation is the wiki's inference, not a measurement.**

## 5. Platform breaks between Orin and Thor

Beyond watts and TOPS, the Ampere→Blackwell jump changes the *platform*, and several of these are regressions for robot builders:

| | Orin (all SKUs) | Thor (T5000/T4000) |
|---|---|---|
| SDK | JetPack 6.x — Jetson Linux 36.5, Ubuntu 22.04, kernel 5.15, CUDA 12.6, TensorRT 10.3 | **JetPack 7.0** — Jetson Linux 38.2, Ubuntu 24.04, kernel 6.8, CUDA 13, TensorRT 10.13 |
| RT cores | present | **absent → [Isaac Sim / Isaac Lab cannot run on Thor](../../sources/rs-designspark-isaac-sim-on-thor.md)**, even headless |
| Camera | MIPI-CSI connectors on carriers | **No MIPI-CSI connectors and no 40-pin GPIO header** on the reference carrier — sensors move to Ethernet / USB / CAN, or CSI-over-Ethernet via Holoscan Sensor Bridge |
| GPU partitioning | — | **MIG** (new on Jetson) — e.g. a VLM in one instance, a VLA in another |
| Real-time kernel | custom build | ships in JetPack 7 |
| System architecture | bespoke embedded | **SBSA-aligned**, server-class ARM |

Sources: [JetPack 7 reference](../../sources/nvidia-jetpack-7-thor-whitepaper.md), [JetPack 6.2.2 release](../../sources/nvidia-jetpack-6-2-2-release.md), [Thor carrier-board spec](../../sources/nvidia-jetson-thor-carrier-board-spec.md), [RS DesignSpark on Isaac Sim](../../sources/rs-designspark-isaac-sim-on-thor.md).

The camera and GPIO removals are the ones that bite an existing Orin design hardest — a CSI-camera robot does not port to Thor by swapping the module.

## 6. What the wiki does not have

Stated plainly so this page isn't mistaken for complete:

- **TOPS per power mode — for any module.** Both Developer Guide chapters give frequencies and core counts only. Every efficiency number in §2 is peak-spec ÷ nominal-budget, not throughput ÷ measured draw.
- **Measured wall-power under load.** No page records actual watts drawn by any module running a real VLA. The [XLeRobot power budget](../projects/xlerobot-thor-power-budget.md) reasons from nvpmodel *caps*, not measurements.
- **Orin NX and Orin Nano VLA latency.** NVIDIA's GR00T table tests only AGX Orin and Thor; the Orin Nano numbers come from a third-party paper on small policies. There is no like-for-like model benchmarked across all six Orin SKUs.
- **Thor T4000 measured anything.** All Thor numbers in §4 are T5000. Also unresolved: T4000's **90 W TDP exceeds its 70 W top nvpmodel budget** — whether a higher budget exists on non-dev-kit carriers is an open question on the [source page](../../sources/nvidia-jetson-thor-platform-power-performance.md).
- **T3000 / T2000 power and price.** Not published; GA Q1 2027.
- **Prices for Orin Nano 4 GB, Orin NX 8 GB, AGX Orin 32 GB / Industrial.** Not recorded anywhere in the wiki.
- **Does DLA offload help a VLA?** If half the Orin NX headline is DLA and no VLA stack uses it, can a vision encoder be compiled to DLA to free the GPU for the action head? Untested here, and cheap on hardware this fleet owns. See [Jetson Orin NX](../../entities/jetson-orin-nx.md).
- **Standard-flash TOPS** for Orin SKUs other than the NX 16 GB (100 standard / 157 Super).
- **Thor's default nvpmodel mode.** The source ingest was ambiguous between MAXN and the 120 W budget; the wiki treats "120 W (Mode 1)" as provisional.

Both Developer Guide chapters were ingested via WebFetch summarization and their own pages carry a verify-before-hardware-planning caveat. **Treat every clock value in §3 as needing confirmation against the live NVIDIA doc before you design against it.**

## Related

- [Onboard compute for XLeRobot](jetson-onboard-compute-xlerobot.md) — the buying decision, power-budget-first.
- [GR00T inference on Jetson](gr00t-inference-on-jetson.md) — VLA throughput per tier.
- [Jetson Thor vs DGX Spark](jetson-thor-vs-dgx-spark.md) — train-on-Spark / deploy-on-Thor, and the RT-core constraint.
- [Hailo NPU vs Jetson](hailo-npu-vs-jetson-xlerobot.md) — the non-CUDA alternative that isn't on this ladder.
- [XLeRobot + AGX Thor power budget](../projects/xlerobot-thor-power-budget.md) — what software-capping Thor buys on a 288 Wh pack.
- [Seeed Jetson selection guide](../../sources/seeed-jetson-selection-guide.md) / [carrier-board selection](../../sources/seeed-jetson-carrier-board-selection.md) — module → buyable carrier.
- Entities: [Jetson Orin Nano](../../entities/jetson-orin-nano.md), [Jetson Thor](../../entities/jetson-thor.md), [JetPack](../../entities/jetpack.md), [Jetson Linux](../../entities/jetson-linux.md), [NVIDIA](../../entities/nvidia.md).
