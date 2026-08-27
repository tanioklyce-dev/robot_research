---
title: Seeed Studio
type: entity
subtype: organization
created: 2026-05-10
updated: 2026-08-27
sources: 10
tags: [seeed-studio, distributor, open-hardware, shenzhen, lekiwi, raspberry-pi, hackathon, jetson, recomputer, rebot-arm, nvidia-dli]
---

**Seeed Studio** — Shenzhen-based open-hardware distributor and OEM. Long-running in the maker / educational-electronics ecosystem (Grove sensor kits, reTerminal, Wio, XIAO, etc.). In this wiki, Seeed is the **commercial hardware distributor for [LeKiwi](lekiwi.md)** — selling assembled or kit forms through its bazaar, and hosting the de-facto end-user tutorial for LeKiwi at [wiki.seeedstudio.com/lerobot_lekiwi](https://wiki.seeedstudio.com/lerobot_lekiwi/). In 2025 Seeed **escalated from sponsor to co-organizer** of LeRobot-ecosystem events — co-hosting (with NVIDIA and Hugging Face) the [October 2025 Embodied AI Hackathon](../sources/seeed-embodied-ai-hackathon-2025-recap.md) across Shenzhen + Mountain View.

## In this wiki

Seeed plays a **distribution + documentation + event-organizer role** distinct from the design authority ([SIGRobotics-UIUC](sigrobotics-uiuc.md)) and the software framework owner ([Hugging Face](hugging-face.md) / [LeRobot](lerobot.md)). This separation of roles — student lab designs, third-party distributor sells, foundation-tier IL framework runs — is a recurring pattern in the LeRobot ecosystem. Seeed's October 2025 hackathon co-organizer billing alongside NVIDIA is the strongest sign yet of the company's shift from passive distributor to active ecosystem orchestrator.

## reBot Arm — Seeed as an original-design robot vendor

As of 2026, Seeed is no longer only distributing other people's designs. The **[reBot Arm B601](rebot-arm-b601.md)** is Seeed's own **6+1-DOF CAN-bus manipulator** ($1,499 bare, $7,057 bundled with a [Jetson AGX Thor](jetson-thor.md) devkit), sold in two actuator variants — [Damiao](damiao.md) DM and [Robstride](robstride.md) RS — alongside the matching **[Star Arm 102](star-arm-102.md)** leader arm ($200) for teleoperation ([product page](../sources/seeed-rebot-arm-b601-dm-thor-bundle.md)). It is marketed as *"truly 100% open-source"* in both hardware and software (BOM, drawings, SDK, algorithms on GitHub) and sits in a price band the wiki previously had no entry in: an order of magnitude above the [FeeTech](feetech.md)-servo hobby arms Seeed also sells, an order of magnitude below research manipulators.

The more interesting move is the **content** attached to it. Seeed co-developed a free **19-module [NVIDIA Deep Learning Institute course](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md)** that carries the arm end to end through [LeRobot](lerobot.md) teleop collection → [Isaac Sim](nvidia-isaac-sim.md) → [Cosmos 3](nvidia-cosmos.md) Transfer augmentation → [GR00T 1.7](nvidia-groot.md) fine-tuning → seven-engine TensorRT deployment on Jetson — and promises *"a series of completely free courses"* as an ongoing deliverable. Combined with the 2025 hackathon co-organizer role, the trajectory is legible: **distributor → sponsor → co-organizer → curriculum author and first-party hardware designer.** Seeed is buying developer mindshare in the LeRobot/GR00T ecosystem with content, and using its own arm as the reference platform.

## reComputer — Jetson carrier products
Seeed is also a major **NVIDIA Jetson** carrier-board vendor: its **reComputer** line wraps bare Jetson modules into robot-ready boxes ([Seeed Jetson selection guide](../sources/seeed-jetson-selection-guide.md)). The mapping: **Mini J3011 → [Orin Nano](jetson-orin-nano.md) 8 GB**; the **J4012 family → Orin NX 16 GB** (J4012B compact, reServer Industrial fanless, Super J4012 +CSI, **Robotics J4012** +GMSL2); **J501 / Robotics J50 → AGX Orin 32/64 GB**; **Thor J601 board → [AGX Thor](jetson-thor.md) 128 GB** (EtherCAT / 4× CAN / 8× GMSL2 / 4× 10 GbE; "brain + cerebellum" humanoid tier). A dedicated **Robotics** line targets robots: **Robotics J30/40** is the *battery-powered* mobile-robot carrier (19–54 V input, CAN + 4× GMSL + I2C-for-IMU, 157 TOPS at 60 °C/40 W) — the off-the-shelf onboard carrier for the [XLeRobot](xlerobot.md) Orin NX pick — while J50 / J601 add AGX-Orin / Thor power for AMRs and humanoids. This makes Seeed the practical "buy-it-as-a-carrier" path for the [Jetson onboard-compute comparison](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) — e.g. the XLeRobot Orin NX 16 GB upgrade is concretely the reComputer J4012.

> [!warning] Not every Seeed Orin NX carrier can cool Super Mode
> Seeed's J401 flash guide states: **"if you are using an Orin NX 16GB/8GB module, do not enable MAXN SUPER mode. The cooling capacity of the reComputer J401 carrier board is insufficient to support it"** ([Seeed flash guide](../sources/seeed-j401-flash-jetpack.md)) — while the **Super J4012** is marketed at **157 TOPS in Super MAXN**. The 157 TOPS quoted for the Robotics J30/40 above is likewise a Super-Mode figure and comes from the [selection guide](../sources/seeed-jetson-selection-guide.md), not from a thermal spec. **Confirm Super-Mode support per carrier SKU before quoting Orin NX peak TOPS in a build.**

**BSP status (2026-08-17):** Seeed ships a **JetPack 7.2.0 / Jetson Linux 39.2.0** prebuilt image for **Orin NX 16 GB on J401**, dated **2026-06-18** — about two and a half weeks behind NVIDIA's 2026-06-01 release. It installs via `l4t_initrd_flash.sh` from an `mfi_*` tarball to NVMe, not via NVIDIA's unified ISO. Seeed's device selector still presents **R36.4.3 (JetPack 6.2)** as the default for the Super J4012.

Seeed also publishes **[`jetson-examples`](jetson-examples.md)** (Seeed-Projects/jetson-examples), a `reComputer`-based one-command example runner for the Jetson (MIT; ~37 recipes spanning LLM/VLM serving, detection/depth/pose, image+audio generation, and robotics — built on top of [jetson-containers](jetson-containers.md)). See the [repo source page](../sources/seeed-jetson-examples.md) for the full catalog; the wiki also deep-dives its **[nvblox recipe](../sources/seeed-jetson-examples-nvblox.md)** — a `reComputer run nvblox` path to a working [Isaac ROS NVBlox](nvblox.md) 3D-mapping demo (Orin + JetPack 6.x + Docker + [Orbbec Gemini2](orbbec.md)).

## Related

- [reBot Arm B601](rebot-arm-b601.md) — Seeed's own robot arm
- [Star Arm 102](star-arm-102.md) — the matching leader arm
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
- [reBot Arm B601-DM Bundle with Jetson Thor](../sources/seeed-rebot-arm-b601-dm-thor-bundle.md) — Seeed's own arm; specs, bundle pricing, accessory ladder.
- [A Sim-to-Real VLA Pipeline with Seeed reBot Arm and NVIDIA Isaac](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) — the 19-module DLI course Seeed co-developed with NVIDIA.
- [Seeed jetson-examples (repo + reComputer runner)](../sources/seeed-jetson-examples.md) — one-command Jetson AI recipe catalog (MIT).
- [Seeed jetson-examples — nvblox recipe (README)](../sources/seeed-jetson-examples-nvblox.md) — `reComputer run nvblox` Isaac ROS 3D-mapping demo.
- [Seeed — flash JetPack OS to J401 carrier board](../sources/seeed-j401-flash-jetpack.md) — the JetPack 7.2 image for Orin NX (`mfi_recomputer-orin-nx-16g-j401-7.2.0-39.2.0-2026-06-18`), host-OS matrix, and the **"do not enable MAXN SUPER on J401"** cooling warning.
