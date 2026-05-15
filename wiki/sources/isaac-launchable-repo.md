---
title: Isaac Launchable (isaac-sim/isaac-launchable)
type: source
url: https://github.com/isaac-sim/isaac-launchable
launchable_url: https://brev.nvidia.com/launchable/deploy?launchableID=env-35JP2ywERLgqtD0b0MIeK1HnF46
launchable_id: env-35JP2ywERLgqtD0b0MIeK1HnF46
author: NVIDIA Isaac Sim team
published: ongoing (v1.2.1 — 2026-01-29)
ingested: 2026-05-14
tags: [nvidia, isaac-sim, isaac-lab, brev, launchable, simulation, devtools, cost-management]
---

## Summary
NVIDIA's official "try Isaac Sim and Isaac Lab in a browser" environment, packaged as a [NVIDIA Brev](../entities/nvidia-brev.md) [Launchable](nvidia-brev-docs.md#launchables). One click on the Deploy link provisions a GPU instance running three containers — VS Code, [Isaac Sim](../entities/nvidia-isaac-sim.md) 5.1, and [Isaac Lab](../entities/nvidia-isaac-lab.md) 2.3 — plus an Omniverse Kit App Streaming client based on the `web-viewer-sample` project. The user gets two browser tabs (VS Code + streamed Sim UI) with no local install. 150★ on GitHub; latest release v1.2.1 (2026-01-29).

> [!note] Version drift
> The Launchable ships **Isaac Sim 5.1 / Isaac Lab 2.3**, *not* the GTC-2026 Isaac Sim 6.0 / Isaac Lab 3.0 / Newton-1.0-GA stack the [NVIDIA entity page](../entities/nvidia.md) currently tracks. Useful as a learning environment, but not the latest.

## Key claims
- **Stack**: VS Code container + Isaac Sim 5.1 + Isaac Lab 2.3 + Kit App Streaming client.
- **Browser-first**: access through "Secure Links" with NVIDIA-account auth; one tab is VS Code, another is the streamed Sim viewer.
- **GPU requirement**: "GPUs with RT cores are required for Kit App Streaming." Rules out the [Brev catalog's](nvidia-brev-docs.md) cheapest tier (T4 / V100 / P4) — needs at minimum L40 / L40S / A10G / RTX 6000 Ada–class.
- **Cloud**: AWS tested and default; explicitly incompatible with Crusoe instances.
- **Single viewer instance only** — known limitation.
- **Audience**: explicitly "learning purposes only; not for production use."
- **Tutorials it's intended for**: Showroom Demos, "Train Your First Robot With Isaac Lab", "Train Your Second Robot With Isaac Lab" (NVIDIA Learning Path), Isaac Lab Walkthrough.
- **Repo composition**: 47.7% Dockerfile, 47.0% Shell, 5.3% Just (Justfile-driven build automation, `docker-compose.yml`, setup scripts).
- **License**: NVIDIA Isaac Sim Additional Software and Materials License Agreement (not OSS).

## Cost notes (specific to this Launchable)
The repo's own guidance: instances are "pay-by-the-hour"; "stop instances when not in use" — stopped instances incur only storage charges. This restates the [general Brev cost model](nvidia-brev-docs.md#instance-lifecycle-and-billing).

What makes this particular Launchable a cost-discipline trap:
- **No T4 escape hatch.** RT-core requirement means the cheapest dev tier is unavailable; you're paying L40-class rates from minute one.
- **Multi-container, browser-first.** Easy to leave the browser tab open and forget the GPU is metered. The streamed Sim viewer feels like a website, but the meter is running in AWS.
- **"Learning environment" framing invites long-tail use.** People work through tutorials over days/weeks — exactly the scenario where `brev stop` hygiene matters most.

Recommended pattern: complete a tutorial session → `brev stop <name>`. For multi-day breaks, `brev delete` (after pushing any work to git), then redeploy from the Launchable URL — the whole point of a Launchable is one-click reproducibility.

## Entities mentioned
- [NVIDIA](../entities/nvidia.md)
- [NVIDIA Brev](../entities/nvidia-brev.md)
- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md)
- [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md)

## Concepts touched
- Browser-delivered GPU dev environments (Launchables-as-tutorial-distribution)
- Pixel streaming for 3D simulator UIs (Omniverse Kit App Streaming, RT-core dependency)

## Open questions
- What does the Launchable actually cost per hour at the AWS default? (Not in repo or docs; visible only on the Launchable card at deploy time.)
- Does the Launchable expose the `Newton physics engine` backend, or is it stuck on PhysX at Isaac Lab 2.3?
- When will the Launchable bump to Isaac Sim 6.0 / Isaac Lab 3.0?
- Is there a way to use the Kit App Streaming client against a smaller (L4 / A10G) RT-core GPU to save cost, or is L40-class effectively the floor?
