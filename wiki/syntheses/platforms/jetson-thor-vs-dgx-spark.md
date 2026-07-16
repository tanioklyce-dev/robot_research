---
title: Jetson Thor vs DGX Spark — the train-on-Spark, deploy-on-Thor split
type: synthesis
created: 2026-05-16
updated: 2026-05-16
tags: [jetson-thor, dgx-spark, nvidia, physical-ai, training-vs-deployment, isaac-sim, isaac-lab]
---

# Jetson Thor vs DGX Spark — train on Spark, deploy on Thor

NVIDIA's two new Blackwell-generation **personal-scale** AI hardware products — [Jetson Thor](../../entities/jetson-thor.md) (Aug 2025) and [DGX Spark](../../entities/dgx-spark.md) — look superficially similar (Blackwell GPU, 128 GB LPDDR5X at 273 GB/s, ARM CPU, sub-$5k). They are **not** substitutes. They are the two halves of the same physical-AI workflow: **train and simulate on Spark; deploy and infer on Thor**.

> [!warning] The 128 GB match holds only for the Thor **T5000**
> This whole comparison assumes "Thor" = the **128 GB T5000** — the SKU that mirrors Spark's memory. As of **2026-07-15** NVIDIA expanded the Thor family downward ([T3000/T2000 blog](../../sources/nvidia-jetson-thor-t3000-t2000-blog.md)): **T3000 = 32 GB, T2000 = 16 GB** (GA Q1 2027). On those tiers the "a model that fits on Spark fits on Thor" oracle **breaks** — a 3B VLA that trains comfortably in Spark's 128 GB may not deploy on a 16 GB T2000 without aggressive quantization. The train-on-Spark/deploy-on-Thor split still holds; the *memory-parity convenience* is a T5000-only property.

## TL;DR — answer to "can Thor run what Spark runs?"

| Capability | Jetson Thor | DGX Spark |
|---|---|---|
| **AI training** (small / quantized fine-tune, LoRA, edge adaptation) | ✅ Possible | ✅ Designed for it (up to 70B) |
| **AI inference** (VLA / VLM / LLM serving) | ✅ Designed for it | ✅ Up to 200B / 405B paired |
| **Isaac Sim** (full RTX viewport) | ❌ **No** — no RT cores | ✅ Yes |
| **Isaac Sim headless** (still RTX renderer) | ❌ **No** — RT cores required even headless | ✅ Yes |
| **Isaac Lab** RL training | ❌ No (Isaac Sim dependency) | ✅ Yes |
| **Isaac ROS** GEMs | ✅ Yes (Isaac ROS 4.0 for Thor) | ✅ Yes |
| **NVIDIA Holoscan** | ✅ Yes (latency-critical sensor) | ✅ Yes |
| **GR00T / VLA fine-tuning** | Possible at small scale | ✅ Primary use case |
| **GR00T / VLA inference & deploy** | ✅ Primary use case | Possible but not the form factor |
| **CUDA-X / NIM containers** | ✅ Most (ARM64 + JetPack 7) | ✅ Yes |
| **Omniverse RTX viewports / NuRec** | ❌ No (RT cores) | ✅ Yes |
| **Multi-box clustering** | ❌ No | ✅ Two-box via ConnectX-7 |
| **On-robot mounting** | ✅ Designed for it | ❌ Desktop cube + 240 W PSU |

## Why they look alike

Both ship in the same Blackwell + 128 GB + 273 GB/s + ARM64 + ~$4k bracket. Numbers that match almost exactly:

| Spec | Thor T5000 | DGX Spark |
|---|---|---|
| Memory | 128 GB LPDDR5X | 128 GB LPDDR5X **unified** |
| Memory bandwidth | 273 GB/s | 273 GB/s |
| Memory bus | 256-bit | 256-bit |
| GPU generation | Blackwell, 5th-gen Tensor | Blackwell, 5th-gen Tensor |
| FP4 sparse | 2,070 TFLOPS | 1,000 TFLOPS |

Same generation, identical memory tier, similar AI throughput class. So why are they not substitutes?

## Why they aren't substitutes — the three structural differences

### 1. RT cores (the categorical one)

**DGX Spark's Blackwell GPU has 4th-gen RT cores. Thor's does not** ([DGX Spark Hardware Overview](../../sources/nvidia-dgx-spark-hardware-overview.md), [Isaac Sim and Isaac Lab on Jetson AGX Thor](../../sources/rs-designspark-isaac-sim-on-thor.md)).

This is the **gating capability** for Isaac Sim, Isaac Lab, Omniverse RTX viewports, and NuRec. Critically, **headless mode does not help** — the RTX rendering pipeline requires RT cores even when no display is attached. RS DesignSpark's vendor explainer is explicit:

> "Jetson Thor and other Jetson SoCs do not incorporate dedicated raytracing hardware. ... Isaac Sim is not supported on Jetson Thor or other Jetson devices."

This is a **deliberate** product decision, not an oversight. Every prior Jetson (Xavier, Orin, Thor) has omitted RT cores; RT cores are reserved for workstation / data-centre Blackwell parts. NVIDIA's prescribed workflow ([RS DesignSpark](../../sources/rs-designspark-isaac-sim-on-thor.md)):

- **Train** on RTX workstation or DGX Spark (with RT cores).
- **Deploy** trained policy on Thor.
- **HIL-validate** trained policy on Thor against real sensors / actuators.

### 2. Form factor and thermal envelope

- **Thor**: SoM that bolts onto a robot's mainboard, 40–130 W envelope, optimised for fanless / ruggedized integration.
- **Spark**: 6-inch desktop cube, 240 W external PSU, 1.2 kg — needs a power outlet and sits on your desk.

This isn't a software gap — it's a physical one. **You cannot put a DGX Spark on a 1X or Boston Dynamics humanoid**, and you wouldn't try.

### 3. Networking and clustering

- **Spark**: ConnectX-7 Smart NIC + 10 GbE + Wi-Fi 7. Two boxes pair for **405B-parameter** model inference.
- **Thor**: Embedded I/O for cameras / lidars / IMUs. No ConnectX. No multi-Thor clustering for distributed model serving.

Spark is built for **off-robot AI workflows** (cluster two, push trained checkpoints to your own S3, run JupyterLab). Thor is built for **on-robot AI workflows** (one node, sensor-tight latency budget, no network dependency).

## The headline-FP4 inversion (and what it actually means)

Thor's headline FP4-sparse rating is **~2× Spark's** (2,070 vs 1,000 TFLOPS). At first glance Thor looks faster.

Why this isn't the whole story:
- The 2× ratio is for **FP4-sparse-tensor** math specifically — i.e. heavily quantized inference. It's the precision Thor is built for, because quantized VLAs are what you deploy on a robot.
- Spark has **2.4× more CUDA cores** (6,144 vs 2,560), more CPU cores, and the renderer hardware. It wins on **anything that isn't FP4-sparse-tensor-dominated**: RL environment stepping, rendering, dataset preprocessing, full-precision training math.
- Spark's **unified memory** lets you fine-tune models that don't fit on consumer GPUs without quantization tricks. Thor's memory is the same capacity but the workflow ergonomics are very different.

In short: **Thor wins the on-robot inference shootout per watt; Spark wins the developer-workflow shootout per workstation.**

## What this means for the user's question

**"Can Jetson Thor run AI training programs?"**
Yes for **fine-tuning** and **edge adaptation** of small/quantized models. No for **pretraining** large models — that's not the form factor, the thermal envelope, or the clustering model. Practically: if you're doing GR00T fine-tunes for your robot, do them on [DGX Spark](../../entities/dgx-spark.md) or on [NVIDIA Brev](../../entities/nvidia-brev.md) and push checkpoints to Thor.

**"Can Jetson Thor run Isaac Sim?"**
**No.** Thor's GPU lacks RT cores, which Isaac Sim's renderer requires even in headless mode. This is the single most important constraint to internalize. The Jetson family architecturally is not — and as far as anyone has signalled, will not become — an Isaac Sim host.

**"Can Jetson Thor run other apps that run on DGX Spark?"**
Most CUDA-X / NIM / inference / Isaac ROS workloads, **yes**. RT-core-gated workloads (Isaac Sim, Isaac Lab, Omniverse RTX, NuRec), **no**. Multi-box clustered model serving, **no**.

## Recommended buying decision tree

```
Do you need to put compute on a robot? ─┬─ yes → Jetson Thor (or AGX Orin if budget-tight)
                                        │
Do you need to render with RTX / run    ├─ yes → DGX Spark (or RTX workstation)
Isaac Sim or Isaac Lab?                 │
                                        │
Do you need to fine-tune > 30B-param    ├─ yes → DGX Spark (single) or two paired
models locally?                         │       (cluster); else rent on Brev / cloud
                                        │
Do you only need to fine-tune small/    └─ Brev / RTX workstation / Spark — all fine
quantized VLAs?
```

For most wiki-tracked robot projects (Stretch 3, ROSOrin Pro, XLeRobot, SO-101), the bill of materials looks like: **Spark on the desk + Thor (or Orin) on the robot**, or equivalently: **Brev for cloud fine-tunes + Thor (or Orin) on the robot**. The hackathon-grade pipeline — [GR00T N1.5 fine-tuned on Brev, deployed on Thor](../../sources/seeed-embodied-ai-hackathon-2025-recap.md) — is the canonical example.

## References
- [NVIDIA Jetson Thor product page](../../sources/nvidia-jetson-thor-product-page.md) — official Thor specs (T5000 + T4000).
- [NVIDIA Blackwell-Powered Jetson Thor Now Available — Newsroom](../../sources/nvidia-jetson-thor-launch-newsroom.md) — 2025-08-25 launch + $3,499 + 12 partner adopters + Jensen quote.
- [NVIDIA DGX Spark Hardware Overview](../../sources/nvidia-dgx-spark-hardware-overview.md) — GB10 SoC, RT cores, unified memory.
- [Isaac Sim and Isaac Lab on NVIDIA Jetson AGX Thor — RS DesignSpark](../../sources/rs-designspark-isaac-sim-on-thor.md) — the authoritative explainer on why Isaac Sim cannot run on Thor.
- [Jetson Thor entity page](../../entities/jetson-thor.md), [DGX Spark entity page](../../entities/dgx-spark.md).

## Related syntheses
- [Robot platforms comparison](robot-platforms-comparison.md) — the broader robot-platform landscape this compute split slots into.
- [Humanoid platforms survey](humanoid-platforms-survey.md) — for which humanoids ship with which on-robot compute.
