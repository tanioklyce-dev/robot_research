---
title: Seeed Studio
type: entity
subtype: organization
created: 2026-05-10
updated: 2026-06-13
sources: 5
tags: [seeed-studio, distributor, open-hardware, shenzhen, lekiwi, raspberry-pi, hackathon, jetson, recomputer]
---

**Seeed Studio** — Shenzhen-based open-hardware distributor and OEM. Long-running in the maker / educational-electronics ecosystem (Grove sensor kits, reTerminal, Wio, XIAO, etc.). In this wiki, Seeed is the **commercial hardware distributor for [LeKiwi](lekiwi.md)** — selling assembled or kit forms through its bazaar, and hosting the de-facto end-user tutorial for LeKiwi at [wiki.seeedstudio.com/lerobot_lekiwi](https://wiki.seeedstudio.com/lerobot_lekiwi/). In 2025 Seeed **escalated from sponsor to co-organizer** of LeRobot-ecosystem events — co-hosting (with NVIDIA and Hugging Face) the [October 2025 Embodied AI Hackathon](../sources/seeed-embodied-ai-hackathon-2025-recap.md) across Shenzhen + Mountain View.

## In this wiki

Seeed plays a **distribution + documentation + event-organizer role** distinct from the design authority ([SIGRobotics-UIUC](sigrobotics-uiuc.md)) and the software framework owner ([Hugging Face](hugging-face.md) / [LeRobot](lerobot.md)). This separation of roles — student lab designs, third-party distributor sells, foundation-tier IL framework runs — is a recurring pattern in the LeRobot ecosystem. Seeed's October 2025 hackathon co-organizer billing alongside NVIDIA is the strongest sign yet of the company's shift from passive distributor to active ecosystem orchestrator.

## reComputer — Jetson carrier products
Seeed is also a major **NVIDIA Jetson** carrier-board vendor: its **reComputer** line wraps bare Jetson modules into robot-ready boxes ([Seeed Jetson selection guide](../sources/seeed-jetson-selection-guide.md)). The mapping: **Mini J3011 → [Orin Nano](jetson-orin-nano.md) 8 GB**; the **J4012 family → Orin NX 16 GB** (J4012B compact, reServer Industrial fanless, Super J4012 +CSI, **Robotics J4012** +GMSL2); **J501 / Robotics J50 → AGX Orin 32/64 GB**; **Thor J601 board → [AGX Thor](jetson-thor.md) 128 GB** (EtherCAT / 4× CAN / 8× GMSL2 / 4× 10 GbE; "brain + cerebellum" humanoid tier). A dedicated **Robotics** line targets robots: **Robotics J30/40** is the *battery-powered* mobile-robot carrier (19–54 V input, CAN + 4× GMSL + I2C-for-IMU, 157 TOPS at 60 °C/40 W) — the off-the-shelf onboard carrier for the [XLeRobot](xlerobot.md) Orin NX pick — while J50 / J601 add AGX-Orin / Thor power for AMRs and humanoids. This makes Seeed the practical "buy-it-as-a-carrier" path for the [Jetson onboard-compute comparison](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) — e.g. the XLeRobot Orin NX 16 GB upgrade is concretely the reComputer J4012.

Seeed also publishes **`jetson-examples`** (Seeed-Projects/jetson-examples), a `reComputer`-based one-command example runner for the Jetson. The wiki ingests its **[nvblox recipe](../sources/seeed-jetson-examples-nvblox.md)** — a `reComputer run nvblox` path to a working [Isaac ROS NVBlox](nvblox.md) 3D-mapping demo (Orin + JetPack 6.x + Docker + [Orbbec Gemini2](orbbec.md)).

## Related

- [LeKiwi](lekiwi.md) — distributed by Seeed
- [SIGRobotics-UIUC](sigrobotics-uiuc.md) — design authority
- [LeRobot](lerobot.md) — software framework
- [Hiwonder](hiwonder.md) — adjacent Chinese educational-robotics vendor

## Mentioned in

- [Seeed Studio LeRobot LeKiwi Wiki](../sources/seeed-lekiwi-wiki.md)
- [LeRobot Worldwide Hackathon 2025 — All Winners](../sources/lerobot-worldwide-hackathon-2025-winners.md) — sponsor.
- [Seeed × NVIDIA × HF Embodied AI Hackathon 2025 Recap](../sources/seeed-embodied-ai-hackathon-2025-recap.md) — co-organizer.
- [Seeed Studio Jetson Product-Line Selection Guide](../sources/seeed-jetson-selection-guide.md) — reComputer Jetson carriers + module comparison.
- [How to Choose the Right NVIDIA Jetson Carrier Board (Liyan Gong)](../sources/seeed-jetson-carrier-board-selection.md) — carrier-board selection methodology (J401 / A603 / A608 / Mini J501).
- [Seeed jetson-examples — nvblox recipe (README)](../sources/seeed-jetson-examples-nvblox.md) — `reComputer run nvblox` Isaac ROS 3D-mapping demo.
