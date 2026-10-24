---
title: NVIDIA RTX Spark
type: entity
subtype: product
created: 2026-10-24
updated: 2026-10-24
sources: 2
tags: [nvidia, rtx-spark, n1x, grace, blackwell, windows-on-arm, unified-memory, local-ai, agents, isaac-sim]
---

# NVIDIA RTX Spark

**RTX Spark** — NVIDIA's **Windows 11 on Arm** PC platform, sold as OEM slim laptops and compact desktops. It is built on the **RTX Spark Superchip (N1X)**: up to a 20-core Grace CPU plus a 6,144-core Blackwell RTX GPU on up to 128 GB of unified LPDDR5X ([product page](../sources/nvidia-rtx-spark-product-page.md)). It is the Windows sibling of [DGX Spark](dgx-spark.md); the headline numbers are identical, but the chip identity is not stated.

## Specs ([product page](../sources/nvidia-rtx-spark-product-page.md))

| | Laptop | Desktop |
|---|---|---|
| GPU | 6,144 or 5,120 Blackwell RTX cores | 6,144 cores |
| CPU | 20- or 18-core Grace | 20-core Grace |
| Memory | up to 128 / 64 GB unified LPDDR5X | up to 128 GB |
| TDP | 45–80 W | 140 W |
| AI | up to 1 PF FP4 | — |

Named OEM laptops: ASUS ProArt P16, Dell XPS 16, HP OmniBook Ultra 16, Lenovo Pro 9n, Microsoft Surface Laptop Ultra, MSI Prestige N16 Flip AI. Prices and bandwidth are not published.

## Role in robotics workflows

NVIDIA's [Microduck tutorial](../sources/nvidia-microduck-ai-agents-sim-blog.md) (2026-10-23) casts RTX Spark as the **local development hub**:
- It runs [Hermes Agent](hermes-agent.md) + [Nemotron](nemotron.md) 3.5 Bolt for planning.
- Policy validation runs in [Isaac Sim](nvidia-isaac-sim.md).
- Training goes to a cloud RTX PRO 6000 running [Isaac Lab](nvidia-isaac-lab.md).

> [!warning] Isaac Sim runs under x86 emulation
> NVIDIA's own install instruction is to *"download the Windows x86 binaries (runnable out of the box via Windows x86 emulation on Arm)"* ([blog](../sources/nvidia-microduck-ai-agents-sim-blog.md)). As of 2026-10, there is no native Arm-Windows Isaac Sim. Compare [DGX Spark](dgx-spark.md), which runs Linux (DGX OS) on the same class of silicon.

## How it differs from DGX Spark
- **OS**: Windows 11 (RTX Spark) vs Linux / DGX OS (DGX Spark). For ROS 2, Isaac Lab and most robot tooling, the Linux box remains the native path.
- **Form**: laptops and small desktops with consumer RTX features (DLSS, Reflex, Studio drivers) vs a networked desk cube with ConnectX-7 pairing.
- **Same pitch for agents**: both are marketed as always-on local agent hosts.

## Related
- [DGX Spark](dgx-spark.md) — the Linux sibling
- [NVIDIA](nvidia.md)
- [On-device and on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md)

## Mentioned in
- [NVIDIA RTX Spark — product page](../sources/nvidia-rtx-spark-product-page.md)
- [Using AI agents to teach Microduck to walk in simulation](../sources/nvidia-microduck-ai-agents-sim-blog.md) — local planning and validation hub; Isaac Sim under x86 emulation.

## Open questions
- Is N1X the same die as GB10? What is its memory bandwidth?
- How large is the emulation penalty for Isaac Sim on Arm Windows? Is a native build planned?
