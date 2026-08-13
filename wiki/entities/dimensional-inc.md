---
title: Dimensional Inc.
type: entity
subtype: company
created: 2026-08-13
updated: 2026-08-13
sources: 3
tags: [dimensional, dimos, agentic-robotics, startup, open-source, apache-2-0, teleoperation]
---

**Dimensional Inc.** — the company behind [DimOS](dimos.md), an Apache-2.0 agentic robotics operating system. Sites: [dimensional.org](https://dimensional.org) (homepage), [docs.dimensionalos.com](https://docs.dimensionalos.com) (docs), [teleop.dimensionalos.com](https://teleop.dimensionalos.com) (hosted teleoperation). GitHub org: [`dimensionalOS`](https://github.com/dimensionalOS). Discord community.

## What is established

Everything below is verifiable from the [DimOS repository](../sources/dimos-github.md):

- **Apache-2.0 license, "Copyright 2025 Dimensional Inc."** — a permissive open-core posture, matching [LeRobot](lerobot.md) / [SO-ARM](so-arm101.md) / [Rosetta](rosetta.md) rather than the copyleft route [Vulcan Robotics](vulcan-robotics.md) took for hardware.
- **~12+ contributors**, led by `spomichter` (284 commits), `paul-nechifor` (211), `leshy` (139), with a long tail including `Dreamsorcerer`, `jeff-hykin`, `ruthwikdasyam`, `mustafab0`, `TomCC7`, `aclauer`.
- **Repository active daily**; 3,874 stars / 788 forks at ingest; created October 2024.
- **A hosted commercial surface exists**: **dimTELE**, WebRTC teleoperation brokered through Dimensional's servers with per-account API keys. This is the one clearly non-self-hostable component in an otherwise Apache-2.0 stack, and the most legible business model in the project.
- **[`openFT-sensor`](openft-sensor.md)** — a separate open 6-axis force/torque sensor in the same org ([ingested](../sources/openft-sensor-github.md)): Hall-effect magnetic-displacement sensing, Gerbers + JLCPCB-ready BOM + drivers + calibration guide. More completely published than most open hardware in this wiki and **less maintained** — 2 stars, created and last pushed the same day, **no LICENSE file**.

## What is not established

> [!warning] Company facts here are thin and should not be filled in from social media
> Founder, funding, headcount, and location are **not documented by any source ingested into this wiki**. A web search surfaced claims circulating on X — an NYSE listing, a national-security designation, a Shenzhen residency program offering robots and LLM credits — none of which are corroborated by a primary source and none of which are recorded here as fact. `spomichter` is the repository's top committer by a wide margin and is publicly associated with the project, which is the strongest attribution the ingested evidence supports.
>
> This is the same evidentiary posture the wiki takes on [Waddle Labs](waddle-labs.md) and [Vulcan Robotics](vulcan-robotics.md): document the artifact, hedge the company.

## Positioning

Dimensional's pitch is **the SDK standard for generalist robotics** — *"integrating with the majority of robot manufacturers,"* Python-native, ROS-optional, agent-first. In this wiki's terms that puts it in a three-way space:

- Against **[ROS 2](ros2.md)** on developer experience (pip install, no colcon, typed Python modules) while speaking ROS 2 as one of five transports.
- Against **[Waddle Labs](waddle-labs.md)** on the same "agent above the robot" thesis, with a public 3.8k-star repository rather than a position piece.
- Alongside **[LeRobot](lerobot.md)** rather than against it — `dimos dataprep` exports to LeRobot v3.0, so the imitation-learning pipeline terminates in Hugging Face's format rather than a proprietary one.

The open-core shape is worth naming: **give away the middleware and the agent layer, sell the hosted connectivity**. Compare [Vulcan Robotics](vulcan-robotics.md)'s rented-inference plan — two 2026 startups, both open-sourcing the hard engineering and monetizing the service the robot cannot provide itself.

## Related

- [DimOS](dimos.md) — the product
- [Waddle Labs](waddle-labs.md) — nearest thesis competitor
- [Vulcan Robotics](vulcan-robotics.md) — forks DimOS as `dimos-vulcan`; a parallel open-source-plus-hosted-service model
- [Hello Robot](hello-robot.md), [Hugging Face](hugging-face.md) — the wiki's other company/framework pairs

## Mentioned in

- [DimOS GitHub repository](../sources/dimos-github.md)
