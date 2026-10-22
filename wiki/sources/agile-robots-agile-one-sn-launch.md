---
title: "Agile Robots Launches Agile ONE SN – a Humanoid Reference Platform Built on NVIDIA Isaac GR00T (Agile Robots press release)"
type: source
url: https://www.agile-robots.com/en/news/detail/agile-robots-launches-agile-one-sn/
local_path: raw/2026-10-21-agile-robots-agile-one-sn.txt
sha256: 2aa99d7c1272ba328562809837ec0fe3d5ae2416ef47b0717209c7443fda5320
author: Agile Robots SE (corporate press release)
published: 2026-10-21
ingested: 2026-10-22
venue: Agile Robots newsroom (GTC Berlin launch, with NVIDIA)
format: "corporate press release (~750 words). Product page captured the same day as raw/2026-10-22-agile-one-sn-product-page.txt (spec values recovered from JS counter attributes)."
tags: [agile-robots, agile-one-sn, humanoid, reference-platform, research-humanoid, gr00t, gr00t-1-7, jetson-thor, wuji-hand, dexterous-hands, halos, isaac-sim, isaac-lab, gtc-berlin, europe, germany]
---

# Agile Robots Launches Agile ONE SN (2026-10-21)

## Summary

[Agile Robots](../entities/agile-robots.md) launched **[Agile ONE SN](../entities/agile-one-sn.md)** with NVIDIA at GTC Berlin. It is a **compact R&D humanoid** that ships preconfigured with NVIDIA's [GR00T](../entities/nvidia-groot.md) stack on [Jetson Thor](../entities/jetson-thor.md). The pitch is integration: one system for demonstration capture, simulation, training, evaluation, deployment and real-world testing, instead of separate tools. It becomes the compact reference platform in Agile's humanoid line, next to the full-size industrial [Agile ONE](../entities/agile-one.md), and *"skills and data developed on Agile ONE SN can later be transferred to Agile ONE."* It is due at the **beginning of 2027**. No price is given.

## Key claims

**Hardware** (press release; the product page agrees where it overlaps)
- *"Agile ONE S humanoid body, 1.4 meters / 4.59 feet tall; 43 kilograms / 95 pounds."* Product page: **140 cm, 43 kg, 31 DoF, 3 kg payload per arm**.
- *"31 degrees of freedom … (body)"* plus *"Dual Wuji tactile five-finger hands with 20 degrees of freedom, for a total of 71 degrees of freedom across body and hands."*
- *"Whole-body control with joint torque of up to 140 Nm and a payload of up to 3 kg per arm."*
- **Compute:** Jetson Thor *"for real-time sensor processing and robot inference."* The product page adds an **Intel i3 N305 base computing module**.
- **Sensing:** RGB-D head camera, wrist cameras, 3D LiDAR. The product page puts the LiDAR **at the waist**, with further **RGB-D cameras at the waist and back**.
- Wi-Fi 7, Bluetooth, an emergency stop button *"and other safety features."*

**Software**
- Ships with *"GR00T 1.7 open VLA model, GR00T whole-body control and the open GR00T end-to-end reference workflow."* **URDF and USD assets** are provided for Isaac Sim and Isaac Lab.
- *"Agile Robots is exploring integration with NVIDIA Halos safety platform … including design with NVIDIA IGX Thor, validation, and software."*
- *"Open and modular … Researchers keep full control of their data."*

**Positioning**
- *"with interest from leading institutions such as Stanford University and ETH Zurich"*. "Interest" is not an order.
- Agile describes itself as **3,500+ employees**, founded in Munich in 2018 by DLR researchers, with subsidiaries **BÄR Automation, Franka Robotics, idealworks and Krause Automation**.
- NVIDIA's Deepu Talla is quoted on reducing integration work.

## Reading it critically

> [!warning] Contradiction: weight
> **43 kg** here and on the product page, against **40 kg (88 lb)** in [NVIDIA's release](nvidia-isaac-platform-gtc-berlin-2026.md). The manufacturer's figure is preferred.

> [!note] Halos: "exploring", not "planned"
> NVIDIA's release says *"planned integration"*. Agile's says *"exploring integration"*. The wiki records the weaker commitment as Agile's own.

- **What NVIDIA's release adds:** the hand model name (**WUJI Hand 2**), **1 kHz force control** on the hands, and Thor's 2,070 FP4 TFLOPS / 128 GB. The TFLOPS figure is the sparse number.
- **What only Agile's pages give:** joint torque (140 Nm), the secondary x86 computer, waist and back cameras, connectivity, and the e-stop.
- **Not stated anywhere:** price, battery and runtime, walking speed, the actuator type, and whether the hands come off. Nothing confirms the ONE SN → ONE skill-transfer claim, and the two bodies differ a lot: 140 cm / 43 kg here against 174 cm / 69 kg for Agile ONE, with 20-DoF hands vs 21-DoF.
- **Two AI stacks, not a switch.** Agile ONE launched in November 2025 with its AI *"developed with Google DeepMind"* ([launch](agile-robots-agile-one-launch.md)), and Agile is still listed as a **Gemini Robotics 2 partner** ([DeepMind model page](deepmind-gemini-robotics-model-page.md)). The SN ships on NVIDIA's GR00T. Neither release mentions the other partner. Agile is backing both stacks.

## Entities mentioned
- [Agile Robots](../entities/agile-robots.md) · [Agile ONE SN](../entities/agile-one-sn.md) · [Agile ONE](../entities/agile-one.md) · [NVIDIA](../entities/nvidia.md) · [Isaac GR00T](../entities/nvidia-groot.md) · [Jetson Thor](../entities/jetson-thor.md) · [NVIDIA Halos](../entities/nvidia-halos.md) · [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md) · [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md) · [Google DeepMind](../entities/google-deepmind.md)
- No pages: WUJI Hand 2, Franka Robotics, idealworks, BÄR Automation, Krause Automation.

## Concepts touched
- [Whole-body control](../concepts/robotics/whole-body-control.md)
- [VLA models](../concepts/learning/vla-models.md) — GR00T 1.7 as the shipped default policy.

## Open questions
- **Price**, and whether it is sold or leased to labs.
- **Weight**: 40 or 43 kg, with or without hands?
- **Battery, runtime and walking speed.**
- **How do skills transfer** between a 140 cm and a 174 cm body with different hands, given that GR00T 1.7 uses a relative-EEF action space ([GR00T](../entities/nvidia-groot.md))?
- **Is the DeepMind partnership** behind Agile ONE still active?
