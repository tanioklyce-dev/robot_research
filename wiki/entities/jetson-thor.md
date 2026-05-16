---
title: Jetson Thor
type: entity
subtype: product
created: 2026-05-16
updated: 2026-05-16
sources: 4
tags: [jetson, thor, nvidia, blackwell, edge-ai, robotics-compute, physical-ai]
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

### Jetson AGX Thor Developer Kit
NVIDIA reference carrier + T5000 module. **$3,499 starting** ([NVIDIA Newsroom](../sources/nvidia-jetson-thor-launch-newsroom.md)). Styled like an RTX Founders Edition; AGX-class connectivity.

## Versus AGX Orin (headline)
**7.5× more AI compute, 3.5× better energy efficiency** ([Jetson Thor product page](../sources/nvidia-jetson-thor-product-page.md)).

## Software stack

- **OS / BSP**: Jetson Linux R37.x line ("for Thor"); ARM64 Ubuntu.
- **SDK**: **[JetPack 7.0](jetpack.md)** — Thor's launch SDK, paired with CUDA 13-class libraries, TensorRT, DeepStream, VPI.
- **Robotics stack**: NVIDIA Isaac platform — **Isaac ROS 4.0** (Thor-compatible release), [Isaac GR00T](nvidia-groot.md) deploy target, NVIDIA Holoscan, NVIDIA Metropolis.
- **Containers**: NIM microservices for VLM / VLA / perception models packaged for the JetPack 7 runtime.

## What Thor can and cannot do

> [!warning] No RT cores
> Thor's Blackwell GPU **does not include dedicated ray-tracing cores**. This is the same architectural choice as every prior Jetson — RT cores are reserved for workstation / data-centre Blackwell parts ([Isaac Sim and Isaac Lab on Thor](../sources/rs-designspark-isaac-sim-on-thor.md)).

| Workload | On Thor? | Notes |
|---|---|---|
| VLA / VLM **inference** (GR00T N1.5/N1.6/N1.7, π0, OpenVLA-class) | ✅ Yes | The headline use case. 128 GB + 2,070 FP4 TFLOPS lets multiple models run concurrently. |
| ROS 2 perception, sensor fusion, control loops | ✅ Yes | Isaac ROS 4.0 ships GEMs tuned for Thor. |
| **On-device fine-tuning** of small / quantized VLAs | ✅ Possible | 128 GB memory enables it; not the primary design target. |
| **Isaac Sim** (full or headless) | ❌ No | RT cores required even headless. Train on [DGX Spark](dgx-spark.md) or RTX workstation, deploy here. |
| **Isaac Lab** RL training | ❌ No | Inherits Isaac Sim's RT-core dependency. |
| Omniverse RTX viewports / NuRec | ❌ No | RT-core gated. |
| LLM **pretraining** of large models | ❌ No | Not the form factor or thermal envelope. |
| Multi-box **clustered** training | ❌ No | Thor lacks DGX Spark's ConnectX-7 pairing. |

## Named adopters

From the [NVIDIA Newsroom launch release](../sources/nvidia-jetson-thor-launch-newsroom.md): **Agility Robotics, Amazon Robotics, [Boston Dynamics](boston-dynamics.md), Caterpillar, Figure, Hexagon, Medtronic, Meta, 1X, John Deere, OpenAI, Physical Intelligence**.

In the wiki's own observed deployments, the U.S.-side **SIGRobotics-UIUC matcha-bot** at the October 2025 Seeed × NVIDIA × HF hackathon ran [GR00T N1.5](nvidia-groot.md) on Jetson Thor (fine-tuned upstream via [NVIDIA Brev](nvidia-brev.md)) ([Seeed Embodied AI Hackathon 2025 Recap](../sources/seeed-embodied-ai-hackathon-2025-recap.md)) — the earliest hackathon-scale Thor deployment the wiki tracks.

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
- Real measured throughput for GR00T N1.5 / N1.7 EA on Thor (latency, concurrent-model count, power).
- JetPack 7.x update cadence vs the JetPack 6.x line maintained for Orin.
- Whether subsequent Jetson generations will add RT cores or whether NVIDIA's strategy is permanent: simulate-off-Jetson, deploy-on-Jetson.

## Mentioned in
- [Jetson Thor vs DGX Spark](../syntheses/platforms/jetson-thor-vs-dgx-spark.md)
- [NVIDIA Jetson Thor product page](../sources/nvidia-jetson-thor-product-page.md)
- [NVIDIA Blackwell-Powered Jetson Thor Now Available — Newsroom](../sources/nvidia-jetson-thor-launch-newsroom.md)
- [Isaac Sim and Isaac Lab on NVIDIA Jetson AGX Thor — RS DesignSpark](../sources/rs-designspark-isaac-sim-on-thor.md)
- [Seeed Embodied AI Hackathon 2025 Recap](../sources/seeed-embodied-ai-hackathon-2025-recap.md) — winning-bot deployment target.
