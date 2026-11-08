---
title: "Cybersecurity AI: Humanoid Robots as Attack Vectors (Mayoral-Vilches, Makris, Finisterre, Sep 2025)"
type: source
url: https://arxiv.org/abs/2509.14139v3
secondary_url: https://arxiv.org/abs/2509.14139v2
author: Víctor Mayoral-Vilches (Alias Robotics), Andreas Makris (thinkAwesome! GmbH), Kevin Finisterre
published: 2025-09-23
ingested: 2026-11-08
tags: [robot-security, unipwn, ble, unitree-g1, alias-robotics, cai, telemetry, privacy, reverse-engineering, primary-source]
---

# Cybersecurity AI: Humanoid Robots as Attack Vectors

## Summary

A security assessment of the [Unitree G1](../entities/unitree-g1.md) by [Alias Robotics](../entities/alias-robotics.md). Version 3 adds independent research by Andreas Makris and Kevin Finisterre on a Bluetooth root-access flaw. The paper also reverse-engineers the encryption protecting the robot's configuration, captures telemetry the robot sends to external servers, and runs Alias's own [CAI](../entities/cai-cybersecurity-ai.md) agent on the robot. **The strongest findings are the Bluetooth flaw, fleet-wide static keys, unencrypted local middleware and unannounced outbound telemetry.** The surveillance and offensive-weapon framing goes well beyond what was measured.

> [!note] Key material omitted
> The paper publishes recovered encryption keys and an injection pattern. This page deliberately does not repeat keys, IVs, cipher constants or exploit strings, and no copy of the PDF is kept in this repository. This page records version 3. The assessment dates from September 2025 and does not state a firmware version, so **current patch status is unknown**.

## Key claims

**Bluetooth provisioning (§2.2, new in v3).**

- The Wi-Fi setup protocol over BLE does not sanitize its input, which allows command injection through the credential fields.
- BLE traffic uses AES-CFB with a static key and IV hardcoded across the fleet.
- Anyone within Bluetooth range can gain root on G1, H1 and R1, and the paper says this is "also applicable to Go2 and B2." It says the flaw "persists across firmware versions," and access can be made persistent.
- The exploitation work is credited to Makris and Finisterre (UniPwn).

**Encryption (§3).**

- Unitree's "FMX" scheme protects configuration files with two layers. The outer layer is Blowfish-ECB with a static 128-bit key recovered from the `master_service` binary, reused across multiple G1 units, so one device exposes the fleet.
- The inner layer is a linear congruential generator using glibc `rand()` parameters. Its seed derivation is only partly understood. The authors call this layer "partially broken."

**Platform (§2).**

- RK3588, 8 GB RAM, 32 GB eMMC, Linux 5.10 with RT patches. Runs ROS 2 Foxy, which the paper's figure marks as end-of-life since May 2023, and CycloneDDS 0.10.2.
- `master_service`, 9.2 MB, supervises 26 daemons.
- Exposed debug connectors, unpopulated JTAG pads and accessible UART.
- DDS/RTPS traffic is unencrypted on the local network. TLS certificate verification is disabled in the shipped WebRTC client and in the `chat_go` WebSocket.

**Telemetry (§4).**

- Within 5 seconds of startup, the robot opens MQTT over TLS on port 17883 to 43.175.228.18 and 43.175.229.18, with automatic reconnection.
- A single 10-minute capture on 9 September 2025 showed JSON frames of 4.5–4.6 KB every 300 seconds. They held battery data, IMU orientation, per-joint torque and temperature, service inventories, and CPU, memory and disk metrics.
- `chat_go` also holds a WebSocket to 8.222.78.102:6080.
- Audio, video and LiDAR run on local DDS topics, where anyone on that network segment can listen.

**Agent test (§5.2).** CAI, run on the RK3588, enumerated reachable endpoints, attempted broker logins (anonymous access was rejected, and certificate-authenticated sessions were "prepped but withheld" for ethical reasons), and produced an attack-surface matrix.

**Disclosure.** "Findings reported to manufacturer prior to publication."

## Reading it critically

> [!warning] What was measured versus what is claimed
> - **Off-robot audio and video were not shown.** The abstract says the robot exfiltrates "multi-sensor" telemetry, and the case study lists audio, video and spatial channels. But the authors write that their "limited telemetry inspection didn't allow us to confirm this." The captured payload is robot health and state data. Audio and video were observed on the **local** network, and the case for covert recording off-site is an inference from the software's capabilities.
> - **The throughput figures do not fit the payload.** 4.6 KB every 300 seconds is about 123 bit/s, yet the paper reports 1.03 Mbps and 0.39 Mbps on those connections, roughly 8,400 times more for the first. Either much more traffic was present than the decoded frames, or a figure is wrong. The paper does not explain it.
> - **Thin sample.** The telemetry claim rests on one 10-minute capture, which would contain about two reporting intervals.
> - **"Autonomous exploitation" was not carried out.** CAI did reconnaissance and planning, and the authenticated attempt was withheld. Lateral movement in "air-gapped facilities" is asserted, not tested.
> - **Legal claims are arguments.** The GDPR and CCPA statements are not supported by a legal analysis of who the data controller is or what Unitree's terms disclose.
> - **Conflict of interest.** The lead author's company makes CAI and [sells robot security services and endpoint protection](https://aliasrobotics.com/robotics.php), and the paper concludes that CAI-style defences are needed.
> - **The Bluetooth finding stands apart.** It is specific, attributed to independent researchers, and needs no inference about intent. It is the claim to act on first.

**Internal tension.** The conclusion calls this "the most sophisticated security implementation observed in commercial robotics," and the same paper reports a fleet-wide static key and disabled certificate checks. Both can be true if the industry baseline is very low.

## Edition history

- **[v3](https://arxiv.org/abs/2509.14139v3) (23 September 2025), used here.** Adds Makris and Finisterre as co-authors, the Bluetooth provisioning finding (now five critical findings rather than four), and BLE as an initial-access route. It also cites the full report, [arXiv 2509.14096](https://arxiv.org/abs/2509.14096), which is not ingested here.
- **[v2](https://arxiv.org/abs/2509.14139v2) (19 September 2025).** Single author, without the Bluetooth finding. The telemetry and CAI sections are carried into v3 substantively unchanged.
- Both editions are referenced by URL only.

The practical disclosure is [UniPwn](https://www.ieee-ras.org/news/exploit-allows-for-takeover-of-fleets-of-unitree-robots/).

## Entities mentioned

- [Unitree G1](../entities/unitree-g1.md)
- [Unitree](../entities/unitree.md)
- [Alias Robotics](../entities/alias-robotics.md)
- [CAI](../entities/cai-cybersecurity-ai.md)
- [Rockchip RK3588](../entities/rockchip-rk3588.md)
- [ROS 2](../entities/ros2.md)

## Concepts touched

- [Robot security](../concepts/robotics/robot-security.md)

## Open questions

- Which of these findings survive on current G1 firmware?
- What fills the gap between 4.6 KB frames and a 1.03 Mbps connection? A longer, decoded capture would settle whether anything beyond health data leaves the robot.
- Unitree's response is not recorded here.
