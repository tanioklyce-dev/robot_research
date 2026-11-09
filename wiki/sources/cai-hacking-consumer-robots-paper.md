---
title: "Cybersecurity AI: Hacking Consumer Robots in the AI Era (Alias Robotics, Mar 2026)"
type: source
url: https://arxiv.org/abs/2603.08665v2
author: Mayoral-Vilches, Ayucar-Carbajo, Laflamme, Peng, Sanz-Gómez, Balassone, Apa, Gil-Uriarte (Alias Robotics; IOActive)
published: 2026-03-10
ingested: 2026-11-08
tags: [robot-security, cai, consumer-robots, exoskeleton, lawnmower, window-cleaner, ble, mqtt, disclosure, primary-source]
---

# Cybersecurity AI: Hacking Consumer Robots in the AI Era

## Summary

[Alias Robotics](../entities/alias-robotics.md) used its [CAI](../entities/cai-cybersecurity-ai.md) agent, with a human operator in the loop, to assess three consumer robots: a lawnmower, a powered exoskeleton and a window cleaner. It reports **38 vulnerabilities in about 7 hours**, 30 rated Critical or High by the authors. **The basic failures are the important result: consumer robots with no authentication, fleet-wide credentials and unsigned firmware.** The claim that AI lets "anyone" do this is not what the study tested. Read version 2 by URL; no copy is kept in this repository, and credentials and exploit details are deliberately not repeated here.

## Key claims

| Robot | Type | Findings | Time | Worst results reported |
|---|---|---|---|---|
| [Hookii Neomow](../entities/hookii-neomow.md) | Lawnmower, ROS 2 Humble | 9 (4 Critical) | 2.5 h | Unauthenticated root over the debug bridge; shared fleet credentials and a default-credential broker exposing **267 connected robots**; GPS sent unencrypted every 30 seconds |
| [Hypershell X](../entities/hypershell-x.md) | Powered exoskeleton | 12 (all Critical or High) | 1.5 h | Unauthenticated BLE control including motor commands; owner data retrievable through unauthenticated APIs; recovered credentials exposing an estimated 3,300+ support emails |
| [HOBOT S7 Pro](../entities/hobot-s7-pro.md) | Window cleaner | 17 | 3 h | Unauthenticated BLE commands; firmware writes accepted without signature checks; a stated risk of disabling suction while on a window |

- **Protocol.** CAI was given only the product name. Humans oversaw it and intervened when testing reached vendor cloud infrastructure.
- **Disclosure.** The authors "attempted to contact all three manufacturers." Hypershell replied that it "is not pursuing vulnerability disclosure reports or external security research submissions."
- **CVEs.** The authors chose not to request CVE identifiers, arguing the system "primarily serves as a credentialing mechanism."
- **Privacy.** Two of the three robots had what the authors call confirmed GDPR compliance failures. The lawnmower stored 456 MB of 3D property mapping data and has a 4G modem that bypasses home network controls.
- **Limitations stated by the authors.** Three robots is not the market. Two Hypershell findings lack working exploits, including the motor-parameter overflow. One cross-tenant leak was seen once and could not be reproduced.

## Reading it critically

> [!warning] What the study shows versus what it claims
> - **"Automated" is overstated.** The abstract says vulnerabilities were found "in an automated manner." The method has a human operator in the loop, and the operators are robot-security specialists.
> - **"Anyone" was not tested.** No novices took part, so the claim that no robotics expertise is needed is inferred.
> - **The time advantage is weakly measured.** The authors say durations "do not represent controlled measurements." The 33-hour traditional baseline is an estimate. The one real comparison is Hypershell, at 1.5 hours against about 5 for an independent human team, with "similar results."
> - **The model is not named.** The paper does not state which LLM powered CAI, which limits reproduction.
> - **Severity is self-assessed.** The CVSS scores are the authors' own, with no CVE review.
> - **Authorization is not discussed.** The findings include vendor brokers and support mailboxes. The paper mentions intervention at cloud boundaries but does not say whether vendors permitted any of this.
> - **"Reported" versus "attempted."** The paper says both that all vulnerabilities "were reported to manufacturers" and that it "attempted to contact" them. Patch status is not given.
> - **Conflict of interest.** The work is partly funded through Alias's Robot Immune System project, and it concludes that such defences must evolve.
> - **The regional framing is thin.** All three robots come from China or Taiwan, and no comparison group from elsewhere was assessed. Its evidence for a pattern of ignored reports cites the G1 work, yet Unitree [launched a disclosure programme](unitree-vulnerability-record-2026.md) in November 2025, before this paper appeared.

## Entities mentioned

- [Alias Robotics](../entities/alias-robotics.md)
- [CAI](../entities/cai-cybersecurity-ai.md)
- [Hookii Neomow](../entities/hookii-neomow.md)
- [Hypershell X](../entities/hypershell-x.md)
- [HOBOT S7 Pro](../entities/hobot-s7-pro.md)
- [Robot Immune System](../entities/robot-immune-system.md)
- [ROS 2](../entities/ros2.md)

## Concepts touched

- [Robot security](../concepts/robotics/robot-security.md)
- [Assistive robotics](../concepts/robotics/assistive-robotics.md)

## Open questions

- Have any of the 38 been fixed?
- Would a person with no security background get the same results with CAI?
- Does an unauthenticated exoskeleton motor command cause physical harm in practice? The paper shows the commands are exposed, not an injury scenario.
