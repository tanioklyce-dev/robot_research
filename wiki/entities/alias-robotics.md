---
title: Alias Robotics
type: entity
subtype: company
created: 2026-07-15
updated: 2026-11-08
sources: 5
tags: [alias-robotics, robot-security, cybersecurity, ros, ros2, spain, rsf]
---

# Alias Robotics

**Alias Robotics** — a **robot cybersecurity** company (Vitoria-Gasteiz, Spain) focused on securing industrial and service robots and their [ROS 2](ros2.md) middleware. In this wiki it's the maintainer of the open-source **[Robot Security Framework (RSF)](../sources/aliasrobotics-rsf-github.md)** — a standardized four-layer (Physical / Network / Firmware / Application) methodology for security assessments in robotics (GPL-3.0; methodology paper arXiv 1806.04042, 2018).

## Why it matters in this wiki

- The wiki's entry point into **classical robot cybersecurity** (OS / middleware / network / firmware) — the counterpart to its LLM-era [prompt-injection / input-rail](../concepts/agents/llm-agent-architecture.md) and [guardrails](../concepts/safety/ai-guardrails.md) coverage. As robots gain LLM-agent brains on [ROS 2](ros2.md), both threads converge.

## Offerings

Its [robotics page](https://aliasrobotics.com/robotics.php) (read 2026-11-08) lists threat modelling, security assessments and certification support (IEC 62443, ISO 21434, ISO 27001, MISRA C), plus three products: a Secure Data Recorder for forensics, the [Robot Immune System](robot-immune-system.md) endpoint protection ([product page](../sources/alias-robotics-ris-page.md)), and the Alurity testing toolbox. It also argues that CVSS scoring misses robots' interaction with their environments and people.

## Research and disclosure record

By [its own count](../sources/alias-robotics-research-page.md), Alias has published 26+ papers and issued 30+ CVE IDs as a CVE Numbering Authority since 2020, with disclosures against MiR mobile robots, DDS implementations used by ROS 2, Universal Robots and KUKA. It founded the Robot Vulnerability Database.

## Unitree G1 assessment

In September 2025 Alias published a [security assessment of the Unitree G1](../sources/cai-humanoid-robots-attack-vectors-paper.md), running its own [CAI](cai-cybersecurity-ai.md) agent on the robot. Its conclusion favours the kind of product Alias sells, so read the claims separately from the measurements.

## Related

- [Robot Security Framework (RSF)](../sources/aliasrobotics-rsf-github.md) — its open methodology.
- [Robot security](../concepts/robotics/robot-security.md) — the concept it anchors.
- [ROS 2](ros2.md) — its primary assessment target.

## Mentioned in

- [Robot Security Framework (RSF)](../sources/aliasrobotics-rsf-github.md) — primary source.
- [Cybersecurity AI: Humanoid Robots as Attack Vectors](../sources/cai-humanoid-robots-attack-vectors-paper.md) — Unitree G1 assessment.
- [Cybersecurity AI: Hacking Consumer Robots in the AI Era](../sources/cai-hacking-consumer-robots-paper.md) — three consumer robots.
- [Alias Robotics research record](../sources/alias-robotics-research-page.md) — publications and disclosures.
