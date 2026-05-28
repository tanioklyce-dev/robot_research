---
title: "ROS 2 Humble Hawksbill — Official Documentation"
type: source
url: https://docs.ros.org/en/humble/
author: Open Robotics / Open Source Robotics Foundation (community-maintained docs)
published: 2022-05-23 (Humble release; docs continuously updated)
ingested: 2026-05-28
tags: [ros2, ros, humble, hawksbill, lts, middleware, dds, ament, colcon, jazzy, kilted, lyrical, robotics-os]
---

## Summary

The official documentation site for **ROS 2 Humble Hawksbill**, the **LTS distribution most commonly used as the integration target** for robotics software in 2024–2026. Released **May 23, 2022** (World Turtle Day), EOL **May 2027** — the 5-year LTS pattern. It is the ROS 2 version targeted by [ROSOrin Pro](../entities/rosorin-pro.md), [TurtleBot 4](../entities/turtlebot.md), [Stretch](../entities/stretch.md) (Stretch 4 uses ROS 2 Jazzy), [nimiCurtis/so101_ros2](so101-ros2-readthedocs.md), and most production educational kits.

## Key facts about Humble

- **Codename**: Humble Hawksbill (`humble`).
- **Release date**: 2022-05-23 (World Turtle Day, ROS 2's annual release date).
- **EOL**: May 2027.
- **Status**: **Long-term support (LTS)** — the 5-year LTS pattern; non-LTS releases get ~18 months.
- **Target Ubuntu**: 22.04 LTS (Jammy) — paired with the corresponding LTS Ubuntu.
- **Position**: an *older but still supported* distribution; banner directs new users to the latest (Lyrical Luth).

## ROS 2 release timeline (as of May 2026)

| Codename | Released | EOL | LTS? | Release boss |
|---|---|---|---|---|
| **Lyrical Luth** | 2026-05-22 | May 2031 | — (newest; LTS status TBC) | Shane Loretz |
| Kilted Kaiju | 2025-05-23 | December 2026 | non-LTS | Scott K Logan |
| **Jazzy Jalisco** | 2024-05-23 | May 2029 | LTS | Marco A. Gutiérrez |
| **Humble Hawksbill** | 2022-05-23 | May 2027 | **LTS** | Christophe Bédard / Audrow Nash |

Cadence: **new ROS 2 distribution every May 23rd (World Turtle Day)**.

> [!note] Cross-distribution compatibility
> "Nodes are not guaranteed to be able to communicate across distributions." Humble Hawksbill and Jazzy Jalisco are both currently supported LTS distributions and both widely deployed, but a node running on Humble may not interoperate with a node running on Jazzy without explicit testing.

## Documentation structure (top-level)

- **Installation** — multiple OS options (binary, source, Docker).
- **Tutorials** — beginner through advanced progressions.
- **How-To Guides** — practical task-specific guidance.
- **Concepts** — foundational through advanced topics.
- **Contributing** — development and governance.
- **Distributions / Releases** — release history, changelogs, EOL timelines.

## Entities mentioned

- [ROS 2](../entities/ros2.md) — the framework.
- Downstream tooling that pins to specific distributions in this wiki: [ROSOrin Pro](../entities/rosorin-pro.md) (Humble), [Stretch](../entities/stretch.md) (Stretch 4 uses Jazzy), [TurtleBot](../entities/turtlebot.md) (4 = Humble, 3 = older), [so101-ros2](../entities/so101-ros2.md) (Humble), [lerobot-ros](../entities/lerobot-ros.md) (Jazzy only).

## Why this matters for the wiki

ROS 2 is **the integration substrate** for nearly all real-robot software in this wiki — yet it has not had its own entity page despite 20+ entity-page mentions. The Humble/Jazzy split is **operationally load-bearing** for the LeRobot↔ROS 2 bridges:

- [Rosetta](../entities/rosetta.md) — distribution-agnostic (the README does not pin a specific distro).
- [lerobot-ros](../entities/lerobot-ros.md) — **Jazzy only** ("This repo is only tested on Jazzy").
- [so101-ros2](../entities/so101-ros2.md) — **Humble only**.

So a wiki reader asking "which bridge can I use on my Humble-based [ROSOrin Pro](../entities/rosorin-pro.md)?" — the answer depends on this distribution split.

## Open questions

- Lyrical Luth (May 2026, newest) — LTS status not yet stated.
- Per-distro Ubuntu version pinning — not on this landing page; documented per-distro on the individual install pages.
- Bridges between ROS 2 distributions (e.g. `ros2_bridge` / `ros1_bridge`-style tooling for inter-distribution communication) — not surfaced from this landing page.
