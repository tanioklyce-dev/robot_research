---
title: "NVIDIA RTX Spark — product page (Windows-on-Arm laptops and small desktops)"
type: source
url: https://www.nvidia.com/en-us/products/rtx-spark/
local_path: raw/2026-10-24-nvidia-rtx-spark-product-page.txt
sha256: ff724454044516f23d4fb2e577f610af1969999fe47f0d75d9c076ff7d4d27cb
author: NVIDIA (marketing product page)
published: 2026-10-24
ingested: 2026-10-24
venue: nvidia.com product page
format: "marketing page with spec table; visible text extracted from HTML. No publication date on the page; `published` is the capture date."
tags: [nvidia, rtx-spark, n1x, grace, blackwell, windows-on-arm, unified-memory, local-ai, agents, laptop, vendor-source]
---

# NVIDIA RTX Spark — product page

Captured as the spec primary for [RTX Spark](../entities/nvidia-rtx-spark.md). The page carries no date, so this is a snapshot of it.

## Summary

**RTX Spark** is NVIDIA's *"new beginning for Windows PCs"*: slim laptops and compact desktops built on the **RTX Spark Superchip**, a Grace CPU plus a Blackwell RTX GPU on unified memory, running **Windows 11**. It is pitched equally at AI development, creative work and gaming. *"CUDA … runs natively on RTX Spark."* Agents are a headline use: *"Compact desktops that run agents around the clock."*

## Key claims

### Spec table (verbatim values)
| | Laptop, top config | Laptop, lower config | Desktop |
|---|---|---|---|
| Chip label | RTX Spark N1X | RTX Spark N1X | RTX Spark N1X |
| GPU | 6,144-core Blackwell RTX | 5,120-core Blackwell RTX | 6,144-core Blackwell RTX |
| CPU | 20-core Grace | 18-core Grace | 20-core Grace |
| Memory | up to 128 GB LPDDR5X unified | up to 64 GB LPDDR5X unified | up to 128 GB LPDDR5X unified |
| TDP | 45–80 W | 45–80 W | **140 W** |
| RT / Tensor cores | 4th gen / 5th gen | 4th gen / 5th gen | 4th gen / 5th gen |

- Headline: *"Up to 1 petaflop FP4 AI performance"*. *"Run models up to 120B parameters with 1M context."*
- Large scenes: *"Up to 128 GB of unified memory handles 3D scenes up to 90 GB."*
- Developer pitch: *"CUDA, TensorRT, and NVFP4 … What you build here runs unchanged on NVIDIA GPUs anywhere."*
- Agents: *"Personal AI agents, right on your PC … Secured by Windows."*
- OEM laptops named: ASUS ProArt P16, Dell XPS 16, HP OmniBook Ultra 16, Lenovo Pro 9n, Microsoft Surface Laptop Ultra, MSI Prestige N16 Flip AI.

### What the page does not say
- No memory bandwidth, prices or ship dates.
- No statement that the chip is GB10, although the top configuration's numbers are identical to [DGX Spark](../entities/dgx-spark.md)'s GB10: 6,144 cores, 20-core Grace, 128 GB, 1 PF FP4.
- Nothing about Linux. Windows 11 is the only OS listed.

## Entities mentioned
- [RTX Spark](../entities/nvidia-rtx-spark.md), [NVIDIA](../entities/nvidia.md), [DGX Spark](../entities/dgx-spark.md) (by comparison)

## Concepts touched
- Local agents on unified-memory desktops; see [On-device and on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md).

## Open questions
- **Is N1X the same die as GB10?** The specs match, but NVIDIA does not say so on this page.
- **Is Isaac Sim native on Arm Windows?** Not as of 2026-10-23: NVIDIA's own [Microduck tutorial](nvidia-microduck-ai-agents-sim-blog.md) installs the **x86 build under Windows-on-Arm emulation**. Emulation overhead on a simulator is unmeasured.
- Memory bandwidth matters most for LLM-agent token rates, and it is unpublished.
