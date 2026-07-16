---
title: Jetson Thor
type: entity
subtype: product
created: 2026-05-16
updated: 2026-07-15
sources: 17
tags: [jetson, thor, nvidia, blackwell, edge-ai, robotics-compute, physical-ai, jetpack-7, nvfp4, mig, t3000, t2000, igx]
---

# Jetson Thor

NVIDIA's **Blackwell-generation flagship edge-AI module** for on-robot compute — the successor to AGX Orin / Orin NX / [Jetson Orin Nano](jetson-orin-nano.md) in the Jetson product line. Positioned as "the brain for general robotics": designed for on-board VLA inference, multi-policy generative-AI execution, and sensor-side perception. **Launched 2025-08-25** ([NVIDIA Newsroom](../sources/nvidia-jetson-thor-launch-newsroom.md)).

## One-line definition
On-robot Blackwell SoC + 128 GB unified memory for running large VLAs at the edge — not a workstation, not a substitute for [DGX Spark](dgx-spark.md).

## Variants

Two production module SKUs plus an AGX-style Developer Kit ([Jetson Thor product page](../sources/nvidia-jetson-thor-product-page.md)):

### Jetson T5000 (flagship)
| Spec | Value |
|---|---|
| GPU | 2560-core Blackwell with 5th-gen Tensor Cores |
| CPU | 14-core ARM Neoverse-V3AE 64-bit |
| Memory | 128 GB, 256-bit LPDDR5X |
| Memory bandwidth | 273 GB/s |
| AI performance | 2070 TFLOPS (FP4 sparse), 1035 TOPS (FP8) |
| Power | 40 W – 130 W |

### Jetson T4000
| Spec | Value |
|---|---|
| GPU | 1536-core Blackwell |
| CPU | 12-core ARM Neoverse-V3AE 64-bit |
| Memory | 64 GB, 256-bit LPDDR5X |
| Memory bandwidth | 273 GB/s |
| AI performance | 1200 TFLOPS (FP4 sparse) |
| Power | 40 W – 70 W |

### Lower tiers — T3000 / T2000 / IGX T3000 (announced 2026-07-15)

NVIDIA extended the family *downward* with three smaller-memory, lower-power SKUs ([T3000/T2000 blog](../sources/nvidia-jetson-thor-t3000-t2000-blog.md)), so the Jetson line now advertises **"70 TOPS to 2,000 teraflops"** end to end. **Emulation** later July 2026 (JetPack 7.2.1); **GA Q1 2027**; pricing undisclosed.

| SKU | AI compute | Memory | CPU | Notes |
|---|---|---|---|---|
| **Jetson T3000** | 865 TFLOPS (FP4) | **32 GB** LPDDR5X, 273 GB/s | 8-core Neoverse Arm | 25 GbE; **~50% smaller / lower power than T5000**; "inference comparable to T5000 for multimodal workloads" |
| **IGX T3000** | = T3000 | 32 GB | — | **Integrated functional safety**; runs **NVIDIA Halos for Robotics** full-stack safety system |
| **Jetson T2000** | 400 TFLOPS (FP4) | **16 GB** | — | Entry-level Thor architecture |

> [!warning] The "Thor = 128 GB" assumption only holds for T5000
> The wiki's [train-on-Spark / deploy-on-Thor](../syntheses/platforms/jetson-thor-vs-dgx-spark.md) framing rests on Thor and [DGX Spark](dgx-spark.md) sharing **128 GB**. That is true **only of the T5000/T4000** (128/64 GB). **T3000 = 32 GB, T2000 = 16 GB** — the smaller tiers are *not* memory-matched to Spark, and 16 GB is the floor the wiki already flags for 3B-VLA deployment (cf. Orin NX 16 GB). Match the tier to the model: T5000 for concurrent multi-VLA, T2000/T3000 for a single quantized policy.

> [!note] Lower-power tiers vs. the mobile-robot power budget
> T3000 ("~50% lower power than T5000") and the entry T2000 are exactly what the [XLeRobot + Thor power budget](../syntheses/projects/xlerobot-thor-power-budget.md) problem needed — [Cutting the Cord](../sources/cutting-the-cord-untethered-xlerobot.md) judged the T5000's **40–130 W** to *exceed* a 288 Wh mobile-robot budget. Actual T2000/T3000 wattage isn't quantified in the announcement yet, so this is promise, not a validated fit.

### Power modes (`nvpmodel`)
Thor's power is a **software-selectable budget**, not a fixed draw ([Thor Platform Power & Performance, R38.4](../sources/nvidia-jetson-thor-platform-power-performance.md)). **T5000**: Mode 0 **MAXN** (uncapped, throttles at the 130 W TDP), Mode 1 **120 W** (default), Mode 2 **90 W**, Mode 3 **70 W**. **T4000**: Mode 0 MAXN, Mode 1 **70 W** (default); module TDP 90 W. The main trade-off is GPU — sub-120 W modes drop the GPU from **10 → 6 TPC (~−40 % throughput)** while barely touching the CPU. Set with `sudo nvpmodel -m <id>` (persists across reboot/SC7). Decisive for battery robots — see [XLeRobot + Thor power budget](../syntheses/projects/xlerobot-thor-power-budget.md). For a small mobile manipulator, even the 70 W floor is high: [Cutting the Cord (2026)](../sources/cutting-the-cord-untethered-xlerobot.md) judges Thor's **40–130 W to "exceed the power budget"** of a 288 Wh XLeRobot, where a 7–25 W [Orin Nano](jetson-orin-nano.md) is the validated fit — see [Jetson onboard compute for XLeRobot](../syntheses/platforms/jetson-onboard-compute-xlerobot.md).

### Jetson AGX Thor Developer Kit
NVIDIA reference carrier + T5000 module. **$3,499 starting** ([NVIDIA Newsroom](../sources/nvidia-jetson-thor-launch-newsroom.md)). Styled like an RTX Founders Edition; AGX-class connectivity.

**Power input** (primary source: [Carrier Board Spec SP-12533-001 v1.2](../sources/nvidia-jetson-thor-carrier-board-spec.md)): main input **`VCC_SRC` = 9–28 V**, max **5 A over USB-C, 15 A over Micro-Fit 3.0** (Table 6-2), with a **~168 W enforced cap** ([Jetson Linux dev guide](https://docs.nvidia.com/jetson/archives/r38.2/DeveloperGuide/SD/PlatformPowerAndPerformance/JetsonThor.html)). The **bundled power adapter is USB-C** (28 V / 5 A = 140 W); the **Micro-Fit 3.0 (J83, 3.0 mm-pitch 2×2 header**, board part `2147561041` per a [forum thread](https://forums.developer.nvidia.com/t/what-is-the-correct-male-microfit-connector-for-the-jetson-agx-thor-developer-kit/347250)) is the **alternative** input — its advantage is **higher current (15 A vs 5 A) and a latching connector**, so it can carry the full 168 W where USB-C's 140 W falls ~28 W short. A **CYPD8225 PD controller arbitrates first-come-first-serve** — if both inputs are connected only the first is used; **they don't sum.** **For battery operation NVIDIA officially says to use the bundled PSU only** — off-label otherwise. The input is a *different rail* than the 12 V used by most low-cost arm/base platforms — see the [XLeRobot + Thor power budget](../syntheses/projects/xlerobot-thor-power-budget.md) for battery chemistry, the 28 V ceiling trap, and wiring.

**IO / board layout** (primary source: [AGX Thor Dev Kit — Hardware Layout](../sources/nvidia-jetson-agx-thor-devkit-hardware-layout.md)):
- **Power**: Micro-Fit **9–28 V DC, up to 8 A** (confirmed from official docs). The **two USB-C ports are PD Sink 140 W** — i.e. USB-C input is hard-capped **28 W below the 168 W power ceiling**, so full-load operation needs the 28 V brick / Micro-Fit, not USB-C.
- **USB**: 2× USB-A **USB 3.2 Gen 2 (10 Gbps)**; 2× USB-C (USB 3.2 Gen 1, 5 Gbps; port *5a* also does Force-Recovery); debug USB-C behind the lid.
- **Networking**: **5 GbE (RJ45)** + a **QSFP28 cage, 4× 25 Gbps** (100 Gb-class) — unusually high bandwidth for an edge module; relevant to CSI-over-Ethernet / distributed compute.
- **Display**: DisplayPort + HDMI.
- **Storage / wireless**: **M.2 Key M (J103)** PCIe ×4 + I2C, NVMe SSD preinstalled (1 TB); **M.2 Key E (J505)** PCIe ×1 + USB 2.0 + I2S + UART, **Wi-Fi/BT module preinstalled**.
- **Robotics IO**: **CAN header (J47)** — 2× CAN (26-pin, 1.27 mm); **Automation Header (J42)** — Power/Reset/Force-Recovery/Sleep/Overcurrent-Throttle/Auto-Power-ON (12-pin 2×6; tie pin 5↔6 for boot-on-power); fan header (12 V/1.5 A); audio panel header (J511); RTC backup-battery connector (J13).
- **Module connector**: 699-pin (11×65) board-to-board. Operating temp 0–35 °C.
- **Buttons**: Power, Force Recovery, Reset, white status LED. Recovery = hold Force-Recovery, tap Reset, release.

> [!note] No 40-pin GPIO header, no MIPI-CSI camera connectors
> Unlike the Orin generation, the AGX Thor Dev Kit carrier board has **neither a 40-pin expansion header nor onboard CSI camera connectors** ([Carrier Board Spec](../sources/nvidia-jetson-thor-carrier-board-spec.md)). Sensors/peripherals move to **Ethernet (5 GbE / QSFP28 4×25 Gbps, i.e. CSI-over-Ethernet via Holoscan Sensor Bridge), USB, and CAN.** A real porting constraint for Orin-era robot wiring harnesses.

## Versus AGX Orin (headline)
**7.5× more AI compute, 3.5× better energy efficiency** ([Jetson Thor product page](../sources/nvidia-jetson-thor-product-page.md)).

## Software stack

- **OS / BSP**: **[Jetson Linux 38.2](jetson-linux.md)** — Linux kernel **6.8**, **Ubuntu 24.04 LTS** rootfs, SBSA-aligned ([JetPack 7 software-stack reference](../sources/nvidia-jetpack-7-thor-whitepaper.md)).
- **SDK**: **[JetPack 7.0](jetpack.md)** — Thor's launch SDK. **CUDA 13 / cuDNN 9.12 / TensorRT 10.13**, with **MIG**, an **NVIDIA-optimized preemptible real-time kernel**, and **CSI-over-Ethernet (CoE)** via Holoscan Sensor Bridge.
- **Quantization formats**: **NVFP4** (Blackwell 4-bit float), **FP8**, **W4A16**.
- **Robotics stack**: NVIDIA Isaac platform — **Isaac ROS 4.0** (Thor-compatible release), [Isaac GR00T](nvidia-groot.md) deploy target, NVIDIA Holoscan, NVIDIA Metropolis.
- **Containers**: NIM microservices for VLM / VLA / perception models packaged for the JetPack 7 runtime.
- **AI-serving frameworks** documented in the JetPack 7 release: **vLLM**, **SGLang**, **MLC**, **llama.cpp**, **Ollama**, **Hugging Face Transformers**.
- **Edge foundation models / agents** ([T3000/T2000 blog](../sources/nvidia-jetson-thor-t3000-t2000-blog.md), 2026-07): **[Cosmos 3](nvidia-cosmos.md) Edge** (4B embodied FM, "post-train for a specific embodiment in ~a day") delivered to the Thor lineup; **Nemotron** open models; **NemoClaw** agentic-orchestration blueprints; and **Jetson Agent Skills** — on-device agents that automate memory optimization / config / deployment (case studies report **up to 15 GB** memory reduction).

### Post-launch generative-AI throughput (single-Thor, Sept 2025)

Numbers from the [JetPack 7 software-stack reference](../sources/nvidia-jetpack-7-thor-whitepaper.md) — a **7×** improvement over Thor's August launch on the same silicon, driven by NVFP4 + speculative decoding:

| Model | Sept 2025 tok/s | + EAGLE-3 speculative decoding |
|---|---|---|
| Llama 3.3 70B | 41.5 | **88.62** |
| DeepSeek R1 70B | 40.29 | — |
| Llama 3.3 W4A16 | — | **16.19** (2.5× uplift) |

## What Thor can and cannot do

> [!warning] No RT cores
> Thor's Blackwell GPU **does not include dedicated ray-tracing cores**. This is the same architectural choice as every prior Jetson — RT cores are reserved for workstation / data-centre Blackwell parts ([Isaac Sim and Isaac Lab on Thor](../sources/rs-designspark-isaac-sim-on-thor.md)).

| Workload | On Thor? | Notes |
|---|---|---|
| VLA / VLM **inference** (GR00T N1.5/N1.6/N1.7, π0, OpenVLA-class) | ✅ Yes | The headline use case. 128 GB + 2,070 FP4 TFLOPS lets multiple models run concurrently. Measured: GR00T N1.6 **10.9 Hz** official TensorRT, **22–24 Hz** community-optimized — see below. |
| ROS 2 perception, sensor fusion, control loops | ✅ Yes | Isaac ROS 4.0 ships GEMs tuned for Thor. |
| **On-device fine-tuning** of small / quantized VLAs | ✅ Possible | 128 GB memory enables it; not the primary design target. |
| **Isaac Sim** (full or headless) | ❌ No | RT cores required even headless. Train on [DGX Spark](dgx-spark.md) or RTX workstation, deploy here. |
| **Isaac Lab** RL training | ❌ No | Inherits Isaac Sim's RT-core dependency. |
| Omniverse RTX viewports / NuRec | ❌ No | RT-core gated. |
| LLM **pretraining** of large models | ❌ No | Not the form factor or thermal envelope. |
| Multi-box **clustered** training | ❌ No | Thor lacks DGX Spark's ConnectX-7 pairing. |

### Measured VLA inference (GR00T / π0.5)

First real numbers (previously an open question on this page). End-to-end, batch 1:

| Model | Path | Latency | Rate | Source |
|---|---|---|---|---|
| GR00T N1.6-3B | PyTorch eager | 117 ms | 8.6 Hz | [Isaac GR00T TensorRT docs](../sources/isaac-gr00t-tensorrt-deployment-docs.md) |
| GR00T N1.6-3B | Official TensorRT (DiT head only, BF16) | 92 ms | **10.9 Hz** | [Isaac GR00T TensorRT docs](../sources/isaac-gr00t-tensorrt-deployment-docs.md) |
| GR00T N1.6 | Community hand-written CUDA kernels | 41–45 ms | **22–24 Hz** | [NVIDIA forums (May 2026)](../sources/nvidia-forum-thor-realtime-vla-inference.md) |
| π0.5 | Community hand-written CUDA kernels | 44 ms | 23 Hz | [NVIDIA forums (May 2026)](../sources/nvidia-forum-thor-realtime-vla-inference.md) |

Thor's official TensorRT speedup (1.27×) is the weakest in NVIDIA's own table (desktop GPUs get 1.73–2.14×) and no NVFP4/FP8 GR00T path exists yet — i.e. the official engine is under-tuned for Blackwell-on-Jetson and the community ~23 Hz is the better estimate of Thor's current ceiling. No N1.7-specific numbers published yet (horizon-40 action head may cost more). Cross-platform comparison: [GR00T inference on Jetson](../syntheses/platforms/gr00t-inference-on-jetson.md) (AGX Orin 64 GB manages 5.8 Hz TensorRT; Orin NX 16 GB unbenchmarked and below the 16 GB+ memory floor).

## Named adopters

From the [NVIDIA Newsroom launch release](../sources/nvidia-jetson-thor-launch-newsroom.md): **Agility Robotics, Amazon Robotics, [Boston Dynamics](boston-dynamics.md), Caterpillar, Figure, Hexagon, Medtronic, Meta, 1X, John Deere, OpenAI, Physical Intelligence**. The [T3000/T2000 expansion blog](../sources/nvidia-jetson-thor-t3000-t2000-blog.md) adds **FANUC, Hitachi, Techman Robot, UBTech, Agile Robots, GROOVE X (LOVOT), SandStar, NoTraffic** plus the carrier/edge ecosystem (ADLINK, Advantech, AAEON, Aetina, Auvidea, AVerMedia, [Seeed Studio](seeed-studio.md), Antmicro, RidgeRun).

In the wiki's own observed deployments, the U.S.-side **SIGRobotics-UIUC matcha-bot** at the October 2025 Seeed × NVIDIA × HF hackathon ran [GR00T N1.5](nvidia-groot.md) on Jetson Thor (fine-tuned upstream via [NVIDIA Brev](nvidia-brev.md)) ([Seeed Embodied AI Hackathon 2025 Recap](../sources/seeed-embodied-ai-hackathon-2025-recap.md)) — the earliest hackathon-scale Thor deployment the wiki tracks.

As of the July 2026 NVIDIA↔HF partnership, Thor is also the announced VLA-deployment brain for **[Reachy 2](reachy.md)**, LeRobot's open-source humanoid ([NVIDIA + HF partnership blog](../sources/nvidia-hf-lerobot-open-robotics-blog.md)) — detail TBD.

## Position in the NVIDIA AI hardware lineup

- **Thor** — on-robot brain (deploy + inference; sensor-side).
- **[DGX Spark](dgx-spark.md)** — developer-desk personal supercomputer (train, simulate, fine-tune up to 70B; inference up to 200B on one box, 405B paired).
- **RTX workstation (4090 / 5090 / 6000 Ada)** — the consumer-priced training-and-simulation path; gives you the RT cores Thor lacks.
- **DGX-class data centre (H100, B100, B200)** — pretraining and large-scale fine-tuning.

See [Jetson Thor vs DGX Spark](../syntheses/platforms/jetson-thor-vs-dgx-spark.md) for the train-vs-deploy decision tree.

## Related
- [JetPack SDK](jetpack.md), [Jetson Linux](jetson-linux.md) — software stack.
- [Jetson Orin Nano](jetson-orin-nano.md) — the wiki's prior-generation Jetson reference.
- [NVIDIA Isaac Sim](nvidia-isaac-sim.md), [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — workstation-side counterparts.
- [NVIDIA GR00T](nvidia-groot.md) — primary VLA family deployed on Thor.
- [NVIDIA Brev](nvidia-brev.md) — common cloud step for fine-tuning before deploying to Thor.
- [NVIDIA DGX Spark](dgx-spark.md) — paired training-side hardware.

## Open questions
- T5000 / T4000 module pricing through distribution.
- ~~Real measured throughput for GR00T on Thor (latency)~~ — answered 2026-07-08 (N1.6: 10.9 Hz official TRT / 22–24 Hz community; see above). Still open: **N1.7-specific** latency, concurrent-model count, and power draw during inference.
- JetPack 7.1 timeline (referenced in NVIDIA developer forums; not yet released).
- Per-MIG-instance performance envelope — JetPack 7 primary sources publish single-Thor numbers only.
- Whether subsequent Jetson generations will add RT cores or whether NVIDIA's strategy is permanent: simulate-off-Jetson, deploy-on-Jetson.

## Mentioned in
- [Jetson Thor vs DGX Spark](../syntheses/platforms/jetson-thor-vs-dgx-spark.md)
- [NVIDIA Jetson Thor product page](../sources/nvidia-jetson-thor-product-page.md)
- [NVIDIA Blackwell-Powered Jetson Thor Now Available — Newsroom](../sources/nvidia-jetson-thor-launch-newsroom.md)
- [Isaac Sim and Isaac Lab on NVIDIA Jetson AGX Thor — RS DesignSpark](../sources/rs-designspark-isaac-sim-on-thor.md)
- [Seeed Embodied AI Hackathon 2025 Recap](../sources/seeed-embodied-ai-hackathon-2025-recap.md) — winning-bot deployment target.
- [JetPack 7.0 for Jetson Thor software-stack reference](../sources/nvidia-jetpack-7-thor-whitepaper.md) — primary source for the JetPack 7 / Jetson Linux 38.2 contents + post-launch 7× generative-AI throughput.
- [AGX Thor Dev Kit — Hardware Layout (User Guide)](../sources/nvidia-jetson-agx-thor-devkit-hardware-layout.md) — primary source for dev-kit IO: Micro-Fit 9–28 V/8 A, USB-C PD Sink 140 W, QSFP28 4×25 Gbps, M.2 Key M 1 TB NVMe, buttons.
- [Jetson Thor Module Carrier Board Spec (SP-12533-001 v1.2)](../sources/nvidia-jetson-thor-carrier-board-spec.md) — authoritative carrier-board spec: USB-C 5 A / Micro-Fit 15 A current split, bundled adapter is USB-C, first-come-first-serve PD, M.2 Key E + CAN + Automation Header + RTC, **no 40-pin / no CSI**.
- [AGX Thor Dev Kit — User Guide (landing/index)](../sources/nvidia-jetson-agx-thor-devkit-user-guide-index.md) — doc-set map: Quick Start, BSP/Docker/CUDA/JetPack SDK setup, Hardware Layout, Supported Hardware, Interim Solutions, Troubleshooting.
- [Jetson Linux Developer Guide — Platform Power and Performance (Jetson Thor, R38.4)](../sources/nvidia-jetson-thor-platform-power-performance.md) — primary source for the T5000/T4000 nvpmodel power modes (70/90/120 W + MAXN), per-mode CPU/GPU caps, and the 168 W system cap vs module TDP distinction.
- [Cutting the Cord (Shaw et al., 2026)](../sources/cutting-the-cord-untethered-xlerobot.md) — frames Thor's 40–130 W as exceeding a low-cost mobile manipulator's power budget (Orin Nano is the fit).
- [Isaac GR00T docs — TensorRT optimization](../sources/isaac-gr00t-tensorrt-deployment-docs.md) — first official GR00T-on-Thor latency (92 ms / 10.9 Hz TensorRT, N1.6).
- [NVIDIA forums — real-time VLA inference on Thor & RTX](../sources/nvidia-forum-thor-realtime-vla-inference.md) — community 22–24 Hz GR00T N1.6 / 23 Hz π0.5 on Thor via custom CUDA kernels.
- [NVIDIA + HF LeRobot partnership blog](../sources/nvidia-hf-lerobot-open-robotics-blog.md) — Thor + Reachy 2 integration for open-humanoid VLA deployment.
