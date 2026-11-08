---
title: HOBOT S7 Pro
type: entity
subtype: robot
created: 2026-11-08
updated: 2026-11-08
sources: 1
tags: [hobot, window-cleaner, consumer-robot, robot-security]
---

**HOBOT S7 Pro** — Bluetooth-connected window-cleaning robot that attaches to glass by suction.

## Security

An Alias Robotics assessment reported 17 vulnerabilities, including Bluetooth access with no pairing or authentication and firmware writes without signature checks. The authors warn that an attacker in Bluetooth range could disable suction while the robot is on a window ([paper](../sources/cai-hacking-consumer-robots-paper.md)). Patch status is not stated.

## Related

- [Robot security](../concepts/robotics/robot-security.md) · [Household robots compared](../syntheses/platforms/household-robots-comparison.md)

## Mentioned in

- [Cybersecurity AI: Hacking Consumer Robots in the AI Era](../sources/cai-hacking-consumer-robots-paper.md)
