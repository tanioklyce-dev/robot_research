---
title: CAI (Cybersecurity AI)
type: entity
subtype: software
created: 2026-11-08
updated: 2026-11-08
sources: 3
tags: [cai, alias-robotics, robot-security, llm-agent, penetration-testing]
---

**CAI (Cybersecurity AI)** — open-source LLM-agent framework for security testing, from [Alias Robotics](alias-robotics.md).

## On a robot

Alias ran CAI on a [Unitree G1](unitree-g1.md)'s onboard RK3588. It enumerated reachable network endpoints, attempted broker logins and produced an attack-surface matrix. Certificate-authenticated access was prepared but withheld, so no exploitation was carried out ([paper](../sources/cai-humanoid-robots-attack-vectors-paper.md)).

## On consumer robots

With a human operator in the loop, CAI was used to assess a lawnmower, an exoskeleton and a window cleaner, and the authors report 38 vulnerabilities in about 7 hours ([paper](../sources/cai-hacking-consumer-robots-paper.md)). Durations were not controlled, and the LLM used is not named.

## Related

- [Alias Robotics](alias-robotics.md) · [Robot security](../concepts/robotics/robot-security.md)

## Mentioned in

- [Cybersecurity AI: Humanoid Robots as Attack Vectors](../sources/cai-humanoid-robots-attack-vectors-paper.md)
- [Cybersecurity AI: Hacking Consumer Robots in the AI Era](../sources/cai-hacking-consumer-robots-paper.md)
- [Alias Robotics research record](../sources/alias-robotics-research-page.md)
