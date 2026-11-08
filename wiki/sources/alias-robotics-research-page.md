---
title: Alias Robotics — research, CVE and disclosure record
type: source
url: https://aliasrobotics.com/research-security.php#papers
local_path: raw/2026-11-08-alias-robotics-research-page.md
sha256: b9d1a2151b922067f842445cea37250ada066fbad8b9b2158b114eec995a490a
author: Alias Robotics
published: Unknown (retrieved 2026-11-08)
ingested: 2026-11-08
tags: [alias-robotics, robot-security, cve, disclosure, cai, primary-source]
---

# Alias Robotics — research, CVE and disclosure record

## Summary

The company's own catalogue of its publications and vulnerability disclosures, read on 2026-11-08. It is useful as a map of robot-security work, and particularly for its history of disclosures against industrial robots and ROS 2 middleware. **All counts are self-reported, and none of the listed papers except the [G1 assessment](cai-humanoid-robots-attack-vectors-paper.md), the [consumer-robot study](cai-hacking-consumer-robots-paper.md) and [RSF](aliasrobotics-rsf-github.md) has been reviewed in this wiki.**

## Key claims

- **Output.** 26+ publications and 30+ CVE IDs issued as a CVE Numbering Authority since February 2020. The page says that status is unique to it for robots and robotic components.
- **Disclosure policy.** 90 days, inspired by Google Project Zero.
- **MiR mobile robots.** 11 CVE IDs and CISA advisory ICSA-21-280-02, including hardcoded credentials, unauthenticated ROS APIs and a default safety-PLC password described as an E-stop bypass.
- **DDS and ROS 2.** 13 CVE IDs across six DDS vendors, CISA advisory ICSA-21-315-02, with Trend Micro, ADLINK and TXOne. CycloneDDS is among those affected.
- **Universal Robots.** 80+ flaws filed in the Robot Vulnerability Database (RVD), 76% rated High or Critical, plus the Akerbeltz ransomware proof of concept. The page says the 90-day window ended without vendor patches.
- **KUKA.** Coordinated disclosure mediated by Germany's BSI and Spain's INCIBE.
- **Funding.** The EIC-funded RIS project lists total cost €3,571,250 and EU contribution €2,499,875.

**Robotics papers listed:** RSF, Robot Vulnerability Scoring System, RVD, Robotics CTF, Aztarna, Robot Hazards, Akerbeltz, DevSecOps in Robotics, Red teaming ROS in industry, alurity, Securing robots in OT environments, Robot Teardown, Robot Cybersecurity review, SROS2, and the book *Cybersecurity in Robotics*.

**Cybersecurity-AI papers listed:** CAI, PentestGPT, CAIBench, CAI Fluency, The Dangerous Gap Between Automation and Autonomy, Hacking the AI Hackers via Prompt Injection, and further 2025–26 work on CTFs, cyber ranges, the CAI dataset and the CT0 model.

> [!warning] Contradiction — the page's summary of the consumer-robot study
> The page calls these the "first fully autonomous" AI-driven robot-security disclosures. [The paper](cai-hacking-consumer-robots-paper.md) describes a human operator in the loop. The page also credits the exoskeleton with "covert telemetry, dual-layer encryption flaws," which are the [Unitree G1](cai-humanoid-robots-attack-vectors-paper.md) findings, not the Hypershell ones. Use the paper.

## Entities mentioned

- [Alias Robotics](../entities/alias-robotics.md)
- [CAI](../entities/cai-cybersecurity-ai.md)
- [Robot Immune System](../entities/robot-immune-system.md)
- [ROS 2](../entities/ros2.md)

## Concepts touched

- [Robot security](../concepts/robotics/robot-security.md)

## Open questions

- RVSS, RVD and Akerbeltz have no page here. RVSS matters if the wiki wants a way of scoring robot vulnerabilities that accounts for physical harm.
- Were the MiR and DDS flaws fixed in current products?
