---
title: Stretch as the de-facto assistive-robotics platform
type: synthesis
created: 2026-05-09
updated: 2026-05-09
tags: [stretch, hello-robot, assistive-robotics, research-platform, mobile-manipulation, eup, hcrlab]
---

Why has [Hello Robot](../entities/hello-robot.md)'s [Stretch](../entities/stretch.md) become the default platform for in-home and assistive-robotics research? It is not the most capable platform, the most expressive form factor, or the most autonomous. It is the platform every wiki-relevant in-home deployment, OVMM-class benchmark, and assistive demonstration converged on between 2023 and 2026. This synthesis explains the convergence by enumerating what Stretch got right — concretely, by what the wiki's source pages cite when they pick Stretch.

> [!note] TL;DR
> Stretch wins the assistive-robotics platform race because the alternatives don't satisfy the *intersection* of: (a) priced for academic labs (~$20–25k vs PR2's $400k or Kinova-arm-only's $50k), (b) safe enough for shared space with disabled users, (c) mobile-manipulator form factor (not arm-only, not full humanoid), (d) supported software (ROS 2 + Python + open-source LLM agent + a documented MuJoCo wrapper), and (e) live commercial vendor that ships EUP-tooled SE2 hardware. No other platform satisfies all five.

---

## The convergence in numbers

Sources in this wiki using Stretch as their primary platform:

- **OK-Robot** — 10 NYC homes; 58.5% pick-and-drop success ([OK-Robot project page](../sources/ok-robot-project-page.md)).
- **Robot Utility Models** — 25 evaluation homes across NYC, Jersey City, Pittsburgh; 90% with mLLM retry ([RUM paper](../sources/robot-utility-models-paper.md)).
- **HomeRobot / OVMM** — 20% real-world baseline; the benchmark Stretch was *built around* ([OVMM](../sources/ovmm-homerobot.md)).
- **HCR Lab Henry Evans deployments** — three summers, expanding task set ([Maya Cakmak Research](../sources/maya-cakmak-research.md)).
- **Yang et al. 2025 — Sense of Agency** — Stretch 3 used in survey illustrations ([Yang 2025](../sources/yang2025-sense-of-agency.md)).
- **Murray et al. 2024 — Grasping in Clutter (IVFP)** — Stretch RE1 in industrial warehouse ([Murray 2024](../sources/murray2024-grasping-clutter-ivfp.md)).
- **stretch_ai LLM agent** — Hello Robot's own open-source stack ([Stretch AI docs](../sources/stretch-ai-llm-agent-docs.md)).
- **Hello Robot Stretch documentation** — full vendor support ([Stretch docs](../sources/hello-robot-stretch-docs.md)).
- **IEEE Spectrum coverage** — public-facing assistive narrative ([IEEE Spectrum, 2023](../sources/ieee-spectrum-stretch-assistive.md)).

The de-facto status is not a research community fashion — it is the platform every published assistive-or-real-home result in this wiki actually deployed on.

---

## Why Stretch and not something else

### What Stretch beats

| Alternative | Why it loses for assistive R&D |
|---|---|
| **PR2 / older research mobile manipulators** | $400k+ ([IEEE Spectrum](../sources/ieee-spectrum-stretch-assistive.md)); requires multiple people to move; out of academic budget; no longer commercially supported. |
| **Arm-only platforms (Kinova JACO, Franka Panda, xArm 7)** | No mobility — limits tasks to whatever's reachable from a fixed mount. Useful for feeding ([Nanavati 2025](../sources/nanavati2025-feeding-out-of-lab.md) uses JACO) but cannot do fetch tasks. Franka Panda is research-grade arm but ~$30k arm-only with no chassis. |
| **Boston Dynamics Spot / quadrupeds** | Designed for inspection and locomotion, not manipulation. No assistive deployments in the wiki. |
| **Humanoids ([1X NEO](../entities/1x-neo.md), [Unitree G1](../entities/unitree-g1.md), [Apptronik Apollo](../entities/apptronik-apollo.md), [Figure 02](../entities/figure.md))** | Form-factor right; safety, cost, software, and openness wrong (as of 2026). NEO requires a $200 deposit, ships unknown date; G1 is the cheapest at ~$16k but lacks the tooling Stretch ships; Apollo and Figure are closed development. No long in-home assistive deployment exists for any humanoid in this wiki. |
| **[TurtleBot 4](../entities/turtlebot.md)** | Mobile base only — no manipulator. Educational platform; not an assistive device. |
| **Educational kits ([ROSOrin Pro](../entities/rosorin-pro.md), [myAGV](../entities/myagv.md), [myBuddy 280](../entities/mybuddy-280.md))** | Hobbyist-grade hardware; no published in-home assistive deployment; arms not safe near humans without careful setup. |
| **[Reachy 2](../entities/reachy.md) — Pollen Robotics** | Open-source bimanual mobile manipulator with the right values, but ROS 2 + 7 DOF/arm at premium price. No assistive in-home deployments in the wiki yet. The closest plausible Stretch competitor architecturally. |

### What Stretch ships

The features the wiki's sources actually cite when they pick Stretch:

1. **Price.** $20k for Stretch 3 ([IEEE Spectrum](../sources/ieee-spectrum-stretch-assistive.md)). Within an academic lab's discretionary equipment budget. ~17× cheaper than [educational tier](robot-platforms-comparison.md) on the relevant axis vs PR2.
2. **Form factor.** Single telescoping arm + mobile base + ~2 kg payload at face/table/floor reach. Sufficient for the assistive task set Henry Evans actually does ([Maya Cakmak Research](../sources/maya-cakmak-research.md)) — face wiping, scratching, lotion, card games, fetching. Not strong enough for body-transfer or dressing — see [Underserved PAR domains](underserved-par-domains.md).
3. **Inherent safety properties.** Light arm; low payload; the wiki's IEEE Spectrum description emphasizes Henry could safely use it without specialized supervision. No reported injuries across three summers of Henry Evans deployment. Compare with a dynamically-walking humanoid in the same situation.
4. **Software stack.** ROS 2 + Python via [stretch_body](../entities/stretch.md) and the open-source [stretch_ai](../entities/stretch-ai.md) including an LLM agent supporting Qwen2.5, Gemma, and GPT-4o-mini ([Stretch AI LLM Agent docs](../sources/stretch-ai-llm-agent-docs.md)). Vendor-supported, not lab-bespoke.
5. **Simulation.** "Stretch Mujoco" wrapper for [MuJoCo](../entities/mujoco.md) (low priority but exists per [TBD list](../index.md)) plus [Gazebo](../sources/hello-robot-stretch-docs.md). Not Isaac-Sim integrated, but enough for sim-to-real workflows.
6. **Vendor with assistive DNA.** [Charlie Kemp](../sources/ieee-spectrum-stretch-assistive.md) (Georgia Tech, Robots for Humanity) and Aaron Edsinger (ex-MIT/Meka) build the company. Vy Nguyen, an occupational therapist, on staff. Not a side market — the assistive use case is core to the company's positioning.
7. **EUP-tooled commercial variant.** [Maya Cakmak](../entities/maya-cakmak.md)'s lab transferred their end-user-programming tooling to the **Stretch SE2** commercial variant ([Maya Cakmak Research](../sources/maya-cakmak-research.md), [HCR Lab Publications](../sources/hcrlab-publications.md)). Other commercial robots ship without an EUP layer; Stretch ships with one.
8. **Published baselines and dataset assets.** RUM's open dataset (~5,500 trajectories across 5 tasks); OK-Robot code; OVMM benchmark — all on Stretch. Picking Stretch means picking a platform with comparable baselines, not green-field engineering.

The features make Stretch the *only* platform where you can trade between research and assistive workflows without rebuilding the stack.

---

## What Stretch does not solve

The convergence on Stretch does not mean Stretch is sufficient. Hard limits the wiki has documented:

- **Payload and contact.** ~2 kg lift; cannot manipulate the user's body; cannot do dressing, bathing, or transfer. These are exactly the [underserved PAR domains](underserved-par-domains.md) that need different hardware (compliant arms, soft robotics, specialized end-effectors).
- **Single arm.** Bimanual tasks (folding, two-handed object manipulation) are out of scope. Reachy 2's bimanual form is closer to what bimanual assistive tasks need.
- **No stairs.** Mobile base on flat surfaces only ([IEEE Spectrum](../sources/ieee-spectrum-stretch-assistive.md)).
- **Manual setup.** "Requires significant technical setup" per IEEE Spectrum. Even with Hello Robot's documentation, deployment is not plug-and-play — a real barrier to broad household deployment.
- **Action-space mismatch with broader VLA / world-model corpus.** Stretch's relative 6D end-effector + gripper action space does not match the typical Franka-arm action spaces in [V-JEPA 2](../entities/v-jepa-2.md), [DINO-WM](../entities/dino-wm.md), [JEPA-WMs](../entities/jepa-wms.md). Pretrained checkpoints don't transfer directly. RUM's dataset is the unique published exception ([LeWM-on-Stretch feasibility](lewm-on-stretch-feasibility.md)).

---

## Implications for someone choosing a platform

Decision framing for an independent researcher or small lab:

| If your goal is | Pick |
|---|---|
| **Real-home in-home study** | Stretch. Six deployments in the wiki use it; one used JACO (feeding-only). |
| **Open-vocabulary fetch / pick-and-place research** | Stretch. RUM dataset + OK-Robot code + OVMM benchmark all on Stretch. |
| **Assistive deployment with quadriplegic / low-motor user** | Stretch + EUP-tooled SE2 variant. Closest published precedent to Henry Evans. |
| **Feeding-specific work** | Kinova JACO + custom F/T fork ([Nanavati 2025](../sources/nanavati2025-feeding-out-of-lab.md)) — the published feeding system. |
| **Bimanual or fine-manipulation tabletop** | Reachy 2 (open) or Franka Panda dual-arm. Stretch is single-arm. |
| **Body-contact assistance (dressing, transfer)** | None of the above are sufficient. Different hardware class entirely (compliant arms, soft robotics — see [Underserved PAR domains](underserved-par-domains.md)).
| **Cheap educational JEPA experiments** | [ROSOrin Pro](../entities/rosorin-pro.md) ([feasibility analysis](lewm-on-rosorin-pro-feasibility.md)). Limits are real but acceptable for pedagogy.
| **JEPA on a real research-grade robot** | Stretch + RUM dataset ([LeWM-on-Stretch feasibility](lewm-on-stretch-feasibility.md)). |

---

## Open questions

- **When does Reachy 2 catch up?** Reachy 2 has the right values (open source, ROS 2, French academic-friendly vendor) but no in-home assistive deployments yet ([Reachy 2 source](../sources/pollen-robotics-reachy.md)). Plausibly the next-platform candidate if Hello Robot stalls.
- **When does an affordable humanoid (G1, NEO) get a credible assistive demonstration?** Currently no humanoid has a long-deployment in-home assistive case in the wiki. The form factor is right; the maturity isn't yet.
- **Will Hello Robot ship a Stretch 4?** Generation cadence has been 2018 → RE1 → RE2 → 3. Stretch 4 should be in pipeline. The wiki has no source on its specs or timeline.

---

## Sources used in this synthesis

- [Stretch entity](../entities/stretch.md) and [Hello Robot entity](../entities/hello-robot.md).
- [IEEE Spectrum — Stretch assistive robot (2023)](../sources/ieee-spectrum-stretch-assistive.md).
- [HomeRobot / OVMM](../sources/ovmm-homerobot.md).
- [OK-Robot project page](../sources/ok-robot-project-page.md).
- [Robot Utility Models Paper](../sources/robot-utility-models-paper.md).
- [Hello Robot Stretch Documentation](../sources/hello-robot-stretch-docs.md).
- [Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md).
- [Maya Cakmak — Research Overview](../sources/maya-cakmak-research.md).
- [HCR Lab Publications](../sources/hcrlab-publications.md).
- [Sense of Agency (Yang et al. 2025)](../sources/yang2025-sense-of-agency.md).
- [Grasping in Clutter IVFP (Murray et al. 2024)](../sources/murray2024-grasping-clutter-ivfp.md).
- [Feeding System Out-of-lab (Nanavati et al. 2025)](../sources/nanavati2025-feeding-out-of-lab.md).

## Related

- [Long-term in-home robot deployments](long-term-in-home-robot-deployments.md) — what the in-home deployment record actually shows.
- [Levels of autonomy in assistive robotics](levels-of-autonomy-in-assistive-robotics.md) — the design pattern that runs on top of Stretch.
- [Robot platforms — comparison](robot-platforms-comparison.md) — at-a-glance comparison of every platform in the wiki.
- [Household robot decision — Stretch vs Unitree G1](household-robot-decision-stretch-vs-g1.md) — adjacent buying-decision context.
- [LeWM on Stretch — feasibility analysis](lewm-on-stretch-feasibility.md) — Stretch as a research substrate for JEPA work.
- [DINO-WM on Stretch — concrete experiment plan](dino-wm-on-stretch-experiment.md) — concrete next-experiment plan on this platform.
