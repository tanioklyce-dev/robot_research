---
title: NVIDIA Jetson AGX Orin
type: entity
subtype: hardware
created: 2026-08-29
updated: 2026-08-29
sources: 9
tags: [jetson, jetson-agx-orin, nvidia, edge-ai, onboard-compute, ampere, dla, pva, nvpmodel, super-mode, robotics, vla]
---

**Product page:** [developer.nvidia.com/embedded/jetson-agx-orin](https://developer.nvidia.com/embedded/jetson-agx-orin) · **Form factor:** 100 × 87 mm, **699-pin Molex Mirror Mezz** connector, integrated thermal transfer plate

**NVIDIA Jetson AGX Orin** — the top of the Ampere-generation Jetson ladder, above the [Orin NX](jetson-orin-nx.md) and below the Blackwell-generation [Thor](jetson-thor.md). Three module SKUs — **64 GB**, **32 GB**, and **Industrial** — plus a Developer Kit. What the AGX tier actually buys over the Orin NX is **memory and IO**: a 256-bit LPDDR5 bus at **204.8 GB/s** (2× the Orin NX's width), up to 64 GB, 16 CSI lanes, 10 GbE, and 2× CAN. It pays for that with a **15–60 W** envelope and a different carrier.

In this wiki it is the tier where **3B-class VLAs actually fit** — the [module ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md)'s central finding is that the practical break in the Orin range is **memory, not TOPS**.

## Specifications

From NVIDIA's module comparison table (retrieved 2026-08-29):

| | **AGX Orin 64 GB** | **AGX Orin 32 GB** | **AGX Orin Industrial** |
|---|---|---|---|
| AI performance | **275 TOPS** | **200 → 241 TOPS** ¹ | **248 TOPS** |
| GPU | 2048-core Ampere, 64 tensor cores | **1792-core, 56 TC** | 2048-core, 64 TC |
| GPU max clock | 1.3 GHz | 1.3 GHz | 1.2 GHz |
| CPU | **12-core** A78AE, 3 MB L2 + 6 MB L3 | **8-core** A78AE, 2 MB L2 + 4 MB L3 | 12-core A78AE |
| CPU max clock | 2.2 GHz | 2.2 GHz | 2.0 GHz |
| DLA | **2× NVDLA v2** @ 1.6 GHz | 2× NVDLA v2 @ 1.4 GHz | 2× NVDLA v2 @ 1.4 GHz |
| Vision accelerator | 1× PVA v2 | 1× PVA v2 | 1× PVA v2 |
| Memory | **64 GB** 256-bit LPDDR5, **204.8 GB/s** | 32 GB 256-bit LPDDR5, 204.8 GB/s | 64 GB 256-bit LPDDR5 **+ ECC** |
| Storage | **64 GB eMMC 5.1** on module | 64 GB eMMC 5.1 | 64 GB eMMC 5.1 |
| Camera | up to **6 cameras** (16 virtual), **16 lanes** MIPI CSI-2 D-PHY 2.1 (40 Gbps) / C-PHY 2.0 (164 Gbps) | *same* | *same* |
| PCIe | up to 2× x8 + 1× x4 + 2× x1, **Gen4** | *same* | *same* |
| Networking | 1× GbE + **1× 10 GbE** | *same* | *same* |
| Other I/O | 4× UART, 3× SPI, 4× I2S, 8× I2C, **2× CAN**, PWM, DMIC/DSPK, GPIO | *same* | *same* |
| Power | **15–60 W** | 15–60 W | **15–75 W** |
| Mechanical | 100 × 87 mm, 699-pin Molex Mirror Mezz | *same* | *same* |
| Price | **~$1,999** dev kit | not recorded in this wiki | not recorded |

¹ **200 TOPS at launch; 241 with Super Mode**, added for the 32 GB by [JetPack 7.2](../sources/nvidia-jetpack-7-2-release.md): *"adds support for Jetson AGX Orin 32GB Super Mode (MAXN_SUPER) increasing performance from 200 TOPS to 241 TOPS."*

> [!note] NVIDIA's own two tables disagree on the 32 GB
> The summary comparison table now lists the 32 GB at **241 TOPS**; the detailed performance-breakdown table on the same page still reads **200 SPARSE INT8 TOPS**. The reconciliation is Super Mode — the summary has absorbed the JP7.2 figure and the breakdown has not been updated. Quote 200 for a pre-7.2 module, 241 for a Super-Mode one, and say which.

### How the headline TOPS decomposes

Same arithmetic as the [Orin NX](jetson-orin-nx.md), and it matters just as much here:

| | GPU tensor cores | DLA | Total | **DLA share** |
|---|---|---|---|---|
| AGX Orin 64 GB | 170 sparse / **85 dense** | 105 sparse / 52.5 dense | **275** | 38% |
| AGX Orin Industrial | 156 sparse / 78 dense | 92 sparse / 46 dense | **248** | 37% |
| AGX Orin 32 GB | 108 sparse / **54 dense** | 92 sparse / 46 dense | **200** | **46%** |

All INT8. Also: GPU CUDA-core FP32 is **5.3 TFLOPS** (64 GB), 4.8 (Industrial), 3.8 (32 GB); tensor-core FP16 is 85 sparse / 43 dense TFLOPS (64 GB).

> [!warning] A stock VLA sees the dense GPU column, not the headline
> Between a third and nearly half of every AGX Orin headline figure is **DLA** — fixed-function accelerators a PyTorch/TensorRT-on-GPU pipeline does not touch unless you explicitly compile for them. And the headline is **sparse** (2:4 structured); without it the GPU tensor cores give **85 dense INT8 TOPS** on the 64 GB and **54** on the 32 GB. The 32 GB is the worst offender: **46% of its 200 TOPS is DLA**, so its dense-GPU figure (54) is **27% of the number on the box**.


## RT cores — present, and absent from every spec table

*Added 2026-08-29 ([Orin module datasheets](../sources/nvidia-jetson-orin-module-datasheets.md)).*

**NVIDIA's Jetson product-comparison page — the table the specs above come from — never mentions RT cores.** The datasheet does, in language identical across the AGX Orin and Orin NX documents:

> "**The RTcore unit assists Ray Tracing by accelerating Bounding Volume Hierarchy (BVH) traversal and intersection of scene geometry** during Ray Tracing… **Each TPC includes two SMs, a Polymorph Engine, two Texture Units, and a Ray Tracing core (RTcore).**"

An **RT core** is fixed-function silicon for the two operations that dominate ray tracing: walking the BVH acceleration tree (pointer-chasing with divergent branches — the worst case for a SIMT machine) and ray–triangle intersection. It is a third core type alongside CUDA and tensor cores, reached through DXR / Vulkan Ray Tracing / OptiX rather than programmed directly.

**On this module: 1 RT core per TPC** — so **8 on the 64 GB** (2 GPC | 8 TPC) and **7 on the 32 GB** (2 GPC | 7 TPC), per the datasheet's own config line. Note the density: Orin is **one RT core per TPC, i.e. per two SMs**, where desktop Ampere is one per SM — half the ratio, on a far smaller GPU. An RTX 4090 has 128.

> [!note] Why this matters, and why it mostly doesn't
> Ray casting is a **geometric query**, not inherently graphics: it is also how simulated lidar and radar work ([Isaac Sim](nvidia-isaac-sim.md)'s RTX lidar is ray-traced), and how visibility and some collision queries are posed. So RT cores matter on the **simulation** side of sim-to-real — the workstation — far more than on the robot. With 7–8 units and an unclear API path on Tegra, they are **not a reason to choose a Jetson**. The reason to record them is epistemic: **absence from a spec table is not absence from the silicon**, and these tables are the wiki's main source for this whole tier.

## nvpmodel power modes

**AGX Orin 32 GB** — no Standard/Super flash split; MAXN is the default mode ([Platform Power and Performance](../sources/nvidia-jetson-platform-power-performance-orin.md)):

| Name | Power | ID | Cores | CPU max | GPU max | DLA max | Mem max |
|---|---|---|---|---|---|---|---|
| MAXN (default) | n/a | 0 | 8 | 2188.8 | 930.75 | 1408 | 3200 |
| 15W | 15 W | 1 | 4 | 1113.6 | 408 | 614.4 | 2133 |
| 30W | 30 W | 2 | 8 | 1728 | 612 | 1369.6 | 3200 |
| 40W | 40 W | 3 | 8 | 1497.6 | 816 | 1228.8 | 3200 |

> [!note] Mode IDs are not portable across modules
> ID 1 means 7 W on an Orin Nano 8 GB, 10 W on an [Orin NX](jetson-orin-nx.md), **15 W on an AGX Orin**, and 120 W on a Thor T5000. Always cross-reference per module.

## Measured VLA performance — the only Orin actually benchmarked

**GR00T N1.6-3B**, end-to-end camera→action, batch 1 ([TensorRT deployment docs](../sources/isaac-gr00t-tensorrt-deployment-docs.md)):

| Platform | PyTorch eager | Official TensorRT |
|---|---|---|
| **AGX Orin 64 GB** | 300 ms (**3.3 Hz**) | **173 ms (5.8 Hz)** |
| AGX Thor (for scale) | 117 ms (8.6 Hz) | 92 ms (10.9 Hz) |

This is the wiki's **only measured VLA latency on any Orin module** — NVIDIA's table tests AGX Orin and Thor only, and [Orin NX and Orin Nano are not benchmarked at all](../syntheses/platforms/jetson-module-ladder-power-performance.md). Every Orin NX VLA figure in this wiki is extrapolated from this row.

**5.8 Hz is the number to hold onto**: a 3B VLA on the biggest Ampere Jetson, fully optimised, runs at under 6 Hz. Against the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) that is squarely in the planner tier, not the servo tier — it needs action chunking or a fast policy underneath it.

## Where it sits in the ladder

- **vs [Orin NX 16 GB](jetson-orin-nx.md)**: the AGX buys **memory and IO** — 2× the memory-bus width (204.8 vs 102.4 GB/s), up to 4× the RAM, 16 vs 8 CSI lanes, 10 GbE, 2× CAN, on-module eMMC. It costs a 15–60 W envelope (vs 10–40 W), ~$2k (vs ~$600), more weight and cooling, and **a different carrier** — the Orin NX is pin-compatible with the Orin Nano's, the AGX is not.
- **Efficiency**: 64 GB is the **peak of the Ampere ladder at 4.6 TOPS/W**. The 32 GB was the ladder's one dip — 3.3 TOPS/W, *below* the Orin NX 16 GB's 3.9, because it paid the AGX 60 W envelope for only 1.27× the TOPS. **JetPack 7.2's Super Mode removes that dip** (241 TOPS / 60 W ≈ 4.0). The margin over the NX is inside the noise of a metric built from headline TOPS over max wattage, and it does not move any buying advice ([module ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md)).
- **vs [Thor](jetson-thor.md)**: a generation and a power class up — Blackwell, 128 GB, 2070 FP4 TFLOPS, 40–130 W, $3,499 dev kit, and NVIDIA's [GR00T](nvidia-groot.md) deploy target.

> [!note] The practical break in the Orin ladder is memory, not TOPS
> [GR00T](nvidia-groot.md)-3B's stated **16 GB inference floor** equals an [Orin NX 16 GB](jetson-orin-nx.md)'s *entire shared* RAM. So 3B-class VLAs realistically mean **AGX Orin 64 GB or Thor**, with Orin Nano excluded outright and Orin NX sitting exactly on the floor (~2–3 Hz extrapolated; the [GR00T-on-Jetson page](../syntheses/platforms/gr00t-inference-on-jetson.md) recommends off-board serving there instead). **AGX Orin 64 GB is the smallest module in this wiki that runs a 3B VLA with headroom.**

## Deployment notes

> [!warning] The 15 W mode has an open reboot-crash bug
> [Jetson Linux r39.2 release notes](../sources/nvidia-jetson-linux-r39-2-release-notes.md), known issue **6236259**: dropping EMC below Fmax via `nvpmodel.service` during systemd init *"can cause system crashes upon reboot,"* especially with a display attached. Affected modes include **AGX Orin 32/64 GB/Industrial at 15 W**. Workaround: switch to MAXN before rebooting, reapply after. Whether headless operation is exempt is **not stated**.

> [!warning] Isaac ROS has no current line on Orin
> Isaac ROS **4.x** supports only Thor, x86_64 and DGX Spark — **no Orin appears in the supported-platform table** ([release notes and platforms](../sources/isaac-ros-release-notes-and-platforms.md)). The last Orin-supporting line is **3.2** (Dec 2024) on JetPack 6.1–6.2 / ROS 2 Humble. Stay on JetPack 6.2 with a frozen 3.2, or move to [JetPack 7.2](../sources/nvidia-jetpack-7-2-release.md) and have none. 4.x is a **ROS 2 Jazzy** line — a distro migration, not an upgrade.

JetPack 7.2 (Jetson Linux r39.2, 2026-06-02) extended JetPack 7 to the whole Orin family on Ubuntu 24.04 / kernel 6.8 / CUDA 13.2.1 / TensorRT 10.16.2, unifying the toolchain with Thor; 7.2.1 followed 2026-08-12.

## Related

- [Jetson Orin NX](jetson-orin-nx.md) — the tier below; the battery-robot pick.
- [Jetson Orin Nano](jetson-orin-nano.md) — entry tier.
- [Jetson Thor](jetson-thor.md) — the Blackwell generation above.
- [Jetson module ladder — power and performance](../syntheses/platforms/jetson-module-ladder-power-performance.md) — the full cross-module comparison.
- [GR00T inference on Jetson](../syntheses/platforms/gr00t-inference-on-jetson.md) · [VLA deployability landscape](../syntheses/platforms/vla-deployability-landscape.md) · [The control-rate ladder](../syntheses/platforms/control-rate-ladder.md)
- [Onboard compute for XLeRobot](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) — where AGX Orin is judged "usually more than needed" for a tabletop bimanual robot.

## Mentioned in

- [NVIDIA Jetson Orin module datasheets (DS-10662 / DS-10712)](../sources/nvidia-jetson-orin-module-datasheets.md) — the RT-core / TPC architecture, and the dense-INT8 totals.
- [Jetson Linux Developer Guide — Platform Power and Performance (Orin)](../sources/nvidia-jetson-platform-power-performance-orin.md) — nvpmodel tables.
- [JetPack 7.2 with Jetson Linux 39.2](../sources/nvidia-jetpack-7-2-release.md) — Super Mode for the 32 GB; JetPack 7 across the Orin family.
- [Jetson Linux r39.2 release notes](../sources/nvidia-jetson-linux-r39-2-release-notes.md) — the 15 W crash bug.
- [Isaac ROS release notes and platforms](../sources/isaac-ros-release-notes-and-platforms.md) — no Orin on 4.x.
- [Isaac GR00T TensorRT deployment docs](../sources/isaac-gr00t-tensorrt-deployment-docs.md) — the 173 ms / 5.8 Hz measurement.
- [Seeed Jetson selection guide](../sources/seeed-jetson-selection-guide.md) — module ladder cross-check.
- [NVIDIA Jetson AI Lab — LeRobot](../sources/nvidia-jetson-ai-lab-lerobot.md) — AGX Orin as a containerized LeRobot target.

## Open questions

- **Prices for the 32 GB and Industrial modules** — not recorded anywhere in this wiki; only the 64 GB dev kit (~$1,999) is.
- **What is the 64 GB's actual MAXN ceiling?** The ladder notes "≤75 W MAXN per some listings" against NVIDIA's stated 15–60 W. The Industrial is officially 15–75 W. Unresolved.
- **No 32 GB VLA benchmark.** The GR00T measurement is 64 GB only; the 32 GB has a *smaller GPU* (1792 vs 2048 cores) as well as less RAM, so it cannot be interpolated from the 64 GB row.
- **Does DLA offload help a VLA?** Between 37% and 46% of every AGX Orin headline is DLA, unused by any VLA stack here. Compiling a vision encoder to DLA to free GPU for the action head is untested anywhere in this wiki — and on the 32 GB, where DLA is 46% of the total, the upside is largest. Same open question as on the [Orin NX](jetson-orin-nx.md).
- **Safety Cluster Engine** reads "-" for every SKU including Industrial on NVIDIA's table, which is surprising for an industrial part. Not chased.
