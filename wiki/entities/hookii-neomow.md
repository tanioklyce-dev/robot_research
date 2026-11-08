---
title: Hookii Neomow
type: entity
subtype: robot
created: 2026-11-08
updated: 2026-11-08
sources: 1
tags: [hookii, lawnmower, consumer-robot, ros2, robot-security]
---

**Hookii Neomow** — autonomous lawnmower running ROS 2 Humble on Debian, with camera, Livox LiDAR, GPS and a 4G modem.

## Security

An Alias Robotics assessment reported 9 vulnerabilities, including unauthenticated root access and shared fleet credentials giving access to 267 connected robots. GPS was sent unencrypted every 30 seconds ([paper](../sources/cai-hacking-consumer-robots-paper.md)). Patch status is not stated.

## Related

- [Robot security](../concepts/robotics/robot-security.md) · [Household robots compared](../syntheses/platforms/household-robots-comparison.md)

## Mentioned in

- [Cybersecurity AI: Hacking Consumer Robots in the AI Era](../sources/cai-hacking-consumer-robots-paper.md)
