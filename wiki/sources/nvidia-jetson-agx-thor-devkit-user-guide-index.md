---
title: "NVIDIA Jetson AGX Thor Developer Kit — User Guide (landing/index)"
type: source
url: https://docs.nvidia.com/jetson/agx-thor-devkit/user-guide/latest/index.html
local_path: null
author: NVIDIA (official documentation)
affiliations: NVIDIA
published: 2026
ingested: 2026-05-31
format: web-docs
tags: [jetson-thor, agx-thor, devkit, user-guide, index, navigation, quick-start, jetpack, primary-source]
---

## Summary

The **landing/index page of the official AGX Thor Developer Kit User Guide** — a navigation hub, not a content page. It frames the dev kit as "frontline access to the most advanced AI edge platform for physical AI and robotics," **powered by the NVIDIA T5000 SoM**, and links out to the full guide. Ingested mainly as a **map of the doc set**: it tells the wiki which official AGX Thor dev-kit pages exist and which are worth ingesting next. The one already filed in depth is **[Hardware Layout](nvidia-jetson-agx-thor-devkit-hardware-layout.md)**; the carrier-board detail lives in the separate **[Carrier Board Spec](nvidia-jetson-thor-carrier-board-spec.md)**.

## Guide structure (table of contents)

- **Getting Started** → Quick Start Guide
- **Detailed Setup Guides** → BSP Setup · Docker Setup · CUDA Setup · **JetPack SDK Setup**
- **Hardware** → **Hardware Layout** (ingested) · **Supported Hardware**
- **Extra Guides** → Interim Solutions (UEFI compatibility · USB installation · headless setup) · Troubleshooting Guide
- **Resources** → Additional Docs

## Why this matters for the wiki
- **Confirms the canonical doc map** for the AGX Thor dev kit, so future "how do I set up / flash / what's supported" questions route to the right official page rather than forum guesswork.
- **Names the highest-value un-ingested subpages**: **Supported Hardware** (likely the home of the Micro-Fit mating-connector part number — an [open question on the Carrier Board Spec](nvidia-jetson-thor-carrier-board-spec.md)) and **Quick Start / JetPack SDK Setup** (first-boot + flashing flow, JetPack 7 / Jetson Linux 38.2 — see [Jetson Thor entity](../entities/jetson-thor.md)).

## Entities mentioned
- [Jetson Thor](../entities/jetson-thor.md) — T5000 SoM; this is its dev-kit user guide.

## Open questions
- This page has **no kit/box contents, first-boot steps, or version specs** — those are on the Quick Start and JetPack SDK Setup subpages (not yet ingested).
- **Supported Hardware subpage is itself empty** — checked 2026-05-31; it is a one-line redirect to the **Jetson Thor Series Supported Components List, doc DA-12429-001**, a **download-gated PDF** on the [Jetson Download Center](https://developer.nvidia.com/embedded/downloads). That SCL (not the web pages) is the authoritative source for the **exact Micro-Fit mating-connector part**, supported cameras, M.2 modules, and QSFP28 optics. **To ingest it, the PDF must be downloaded into `raw/`** (same flow as the Carrier Board Spec) — WebFetch can't pull the gated download.
