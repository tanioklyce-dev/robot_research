---
title: Robot Immune System (RIS)
type: entity
subtype: software
created: 2026-11-08
updated: 2026-11-08
sources: 3
tags: [ris, alias-robotics, endpoint-protection, robot-security]
---

**Robot Immune System (RIS)** — [Alias Robotics](alias-robotics.md)' endpoint-protection software, installed on the robot itself.

## What the vendor says

Firewall, hardening, logging, visualization and an adaptive AI module, listed for Universal Robots, KUKA, MiR, UVD Robots, Enabled Robotics and ROS. Stated overhead is 80 MB RAM and at most 100 µs of added latency. The vendor says it meets IEC 62443-4-2 component requirements ([product page](../sources/alias-robotics-ris-page.md)). No independent evaluation was found.

## Scope

The product page lists no humanoid or home robot, and its ROS 2 support is shown as Dashing, "Coming soon." Nothing reviewed here shows that it can protect the consumer robots in Alias's [own study](../sources/cai-hacking-consumer-robots-paper.md).

## Adaptive or static

The vendor page describes RIS as adaptive. Alias's 2026 paper calls its approach "static, rule-based" and not designed for AI-powered attacks ([paper](../sources/cai-hacking-consumer-robots-paper.md)).

## Related

- [Alias Robotics](alias-robotics.md) · [Robot security](../concepts/robotics/robot-security.md) · [CAI](cai-cybersecurity-ai.md)

## Mentioned in

- [Alias Robotics — RIS product page](../sources/alias-robotics-ris-page.md)
- [Cybersecurity AI: Hacking Consumer Robots in the AI Era](../sources/cai-hacking-consumer-robots-paper.md)
- [Alias Robotics research record](../sources/alias-robotics-research-page.md)
