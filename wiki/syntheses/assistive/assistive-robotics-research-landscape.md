---
title: Assistive robotics — R&D landscape and JEPA applicability
type: synthesis
created: 2026-05-09
updated: 2026-07-09
tags: [assistive-robotics, jepa, research-landscape, independent-researcher]
---

Synthesized from: [Assistive robotics](../../concepts/robotics/assistive-robotics.md), [OK-Robot](../../entities/ok-robot.md), [Robot Utility Models](../../entities/robot-utility-models.md), [Stretch](../../entities/stretch.md), [JEPA task capabilities](../world-models/jepa-task-capabilities.md), [V-JEPA 2](../../entities/v-jepa-2.md).

---

## The reliability gap is the central problem

The headline numbers from the wiki and the [Stanford HAI AI Index 2026](../../sources/stanford-hai-ai-index-2026.md):

- **OK-Robot**: 58.5% success across 10 real NYC homes — zero-shot, no prior mapping, open-vocabulary pick-and-drop. State of the art for a household mobile manipulation system as of early 2024.
- **BEHAVIOR-1K 2025 Challenge** (1,000 household tasks from surveys of what people actually want robots to help with): top team full task success rate **12.4%**; Q-score (partial credit) ~26%.
- **RLBench** (controlled simulation, short-horizon): EquAct reaches **89.4%** — the ceiling in simulation.

A deployable assistive robot needs 99%+ reliability for a user who cannot recover from failures themselves. The 12.4% BEHAVIOR-1K number — from realistic household environments with long-horizon tasks — is the most honest current baseline. The gap between 12.4% and 99%+ frames everything else.

---

## Seven blocking problems

### 1. Reliability gap (58.5% → 99%+)
Current open-vocabulary pick-and-place fails roughly 4 times in 10. For [Henry Evans](../../sources/ieee-spectrum-stretch-assistive.md) or any user with severe motor impairment, a dropped item, a knocked-over glass, or a failed grasp is not a recoverable nuisance — it may end the session. Reliability must compound across multi-step tasks, so a 90%-per-step rate gives ~35% success on a 10-step task.

### 2. Manipulation in clutter
OK-Robot's failures concentrated in cluttered scenes. Occlusion, contact-rich grasping, and close object proximity all degrade performance. The manipulation benchmark ecosystem ([RoboCasa365](../../sources/robocasa365-paper.md), [ManiSkill-HAB](../../sources/maniskill-hab-paper.md)) is pushing toward harder household scenarios, but real home clutter exceeds what any benchmark has captured.

### 3. Long-horizon execution
Assistive tasks are rarely single grasps. "Get my medication, open the bottle, put two pills on the tray" is a 10+ step sequence where each failure mode propagates. [Robot Utility Models](../../entities/robot-utility-models.md) (RUM) show strong generalization on individual skills; long-horizon chaining remains an open problem not yet addressed by the RUM/DINO-WM family.

### 4. Safe contact with humans
Assistive manipulation — helping someone dress, passing an object, adjusting a support device — requires physical contact near or with users who cannot easily recoil. Standard manipulation benchmarks assume no human in the workspace. The [Virginia Tech Assistive Robotics Lab](../../sources/virginia-tech-assistive-robotics-lab.md) (Prof. Alan Asbeck) and the [RELab tenoexo](../../sources/relab-ethz-tenoexo.md) (ETH Zurich; <150g, 5N/finger) work in this space. Collaborative robotics (ISO/TS 15066, force-torque sensing) is mature for industrial settings but not for human-intimate home scenarios.

### 5. Per-user personalization
A robot calibrated for one user's reach envelope, grip strength, preferred object positions, and communication style is not calibrated for the next. No current system adapts to the individual without significant engineering effort. RUM's key insight — diversity beats quantity in training data ([25 demos × 40 environments beats 200 × 5](../../entities/robot-utility-models.md)) — suggests generalization is achievable, but "generalize to new environments" ≠ "adapt to a specific person."

### 6. Accessible human-robot interaction for low-motor users
For users with ALS, high-cervical spinal cord injury, or progressive motor disorders, standard HRI (voice, touchscreen, joystick) may not be accessible. Gaze tracking, switch scanning, EMG, and BCI inputs are niche and fragmented. No end-to-end stack exists that goes from a low-bandwidth user signal all the way through task-level robot control robustly.

### 7. Data scarcity in assistive contexts
General manipulation datasets (DROID: 350 hr / 76k trajectories) exist but are not collected in assistive contexts, with assistive-relevant objects, or with the goal of serving users with disabilities. Collecting assistive-specific demonstration data requires ethical review, accessible recruiting, and patience — barriers that purely academic robot-learning groups often don't navigate.

---

## Timeline estimates

| Capability | Realistic horizon | Key blockers |
|---|---|---|
| Pick-and-drop at 80%+ in familiar environments | **1–3 years** | Policy generalization, sim-to-real; active research |
| Open-vocabulary fetch in any home at 90%+ | **3–7 years** | Clutter, failure detection, recovery |
| Long-horizon multi-step ADL sequences | **5–10 years** | Task planning + recovery + replanning |
| Safe physical contact assistance (dressing, transfer) | **10–15 years** | Safe contact, force control, regulatory clearance |
| Per-user adaptation without engineering effort | **5–10 years** | Personalization, RLHF from sparse user signals |
| Accessible low-bandwidth HRI (BCI-to-robot) | **7–20 years** | BCI stability, latency, regulatory |
| Commercial deployment at scale | **10–20 years** | All of the above + cost + liability |

---

## Who is actively working on this

### Strong in the wiki
- **[Lerrel Pinto](../../entities/lerrel-pinto.md) + [Mahi Shafiullah](../../entities/mahi-shafiullah.md) — NYU**: DINO-WM, Robot Utility Models, OK-Robot. The most productive academic group directly advancing toward deployable household manipulation.
- **[Hello Robot](../../entities/hello-robot.md) (Aaron Edsinger, Charlie Kemp)**: [Stretch](../../entities/stretch.md) platform is the de-facto research vehicle for assistive mobile manipulation. Their IEEE Spectrum demo with Henry Evans is the canonical proof-of-concept ([Stretch assistive demo](../../sources/ieee-spectrum-stretch-assistive.md)).
- **ETH Zurich RELab**: [tenoexo](../../sources/relab-ethz-tenoexo.md) — <150g hand orthosis with 5N per finger; clinical trials showing benefit in spinal cord injury patients. Wearable + robotic augmentation track.
- **Virginia Tech Assistive Robotics Lab (Prof. Alan Asbeck)**: exoskeletons, soft robotics, haptics.

### Beyond the wiki
- **[HCR Lab — Maya Cakmak](../../entities/hcrlab.md) (UW Paul G. Allen School)**: the most directly relevant academic group for accessible HRI. Key results: long-term in-home deployments with quadriplegic user Henry Evans (Stretch, summers 2021–2023 — self-feeding, grooming, card games, medical device operation); HRI 2020 finding that people with severe motor impairments do NOT always prefer more autonomous robots (autonomy preference is user/context-specific); [end-user robot programming (EUP)](../../concepts/robotics/end-user-robot-programming.md) tools transferred to commercial Stretch SE2; 2025 RO-MAN paper "Preserving Sense of Agency" ([HCR Lab publications](../../sources/hcrlab-publications.md); [Maya Cakmak research overview](../../sources/maya-cakmak-research.md)).
- **[CMU Quality of Life Technology Center (QoLT)](../../entities/cmu-qolt-center.md)**: NSF Engineering Research Center (CMU + Pitt, 2006 – mid-2010s, ~$30M; now graduated); PerMMA robotic wheelchair + HERB robot; power wheelchair integration; assistive manipulation at the systems level. Historical rather than active — see the entity page for why its wind-down is a relevant data point for this synthesis's timeline pessimism.
- **Georgia Tech Healthcare Robotics Lab (Charlie Kemp, now at Hello Robot; formerly PI there)**: CURI, Henry Evans demos, object handover, robot-assisted dressing.
- **Stanford GRAB Lab (Monroe Kennedy III)**: physical human-robot interaction; compliant manipulation; handover; care robotics.
- **Stanford HAI + CRUSE (Allison Okamura)**: haptics, teleoperation, surgical and care robotics.
- **MIT CSAIL (Daniela Rus, Pulkit Agrawal)**: soft robotics, in-home manipulation, generalizable policies.
- **Microsoft Research**: Project Learned Manipulation; semi-structured home environments.

---

## What an independent researcher can do

### 1. Collect and release assistive-context demonstration data
The data gap is real and tractable. If you have access to Stretch (or any mobile manipulator), collecting 50–100 demonstrations of assistive-relevant tasks — picking objects off the floor, retrieving items from lower shelves, opening medication bottles — in a real home environment is publishable and directly useful. RUM showed that 25 diverse demos generalize better than 200 homogeneous ones; even a small, well-documented dataset fills a gap.

### 2. Replicate and extend OK-Robot in higher-clutter scenarios
[OK-Robot](../../entities/ok-robot.md)'s code is public. Replicating it on a Stretch in a real messy home, characterizing failure modes in cluttered scenes, and publishing the failure taxonomy is a concrete contribution. The original evaluation (10 cleaned NYC homes) understates real-world difficulty.

### 3. Build an accessible HRI interface layer
Take a robot system (Stretch + OK-Robot / RUM) and add a non-standard input modality: gaze tracking, switch scanning, or EMG. Evaluate task completion rate vs. standard voice/touch input. This is a systems integration contribution that requires no novel ML but produces real data on whether current robot systems are actually accessible to the users they claim to serve.

### 4. Document unmet needs with potential users
Structured interviews or participatory design sessions with users with motor impairments, their caregivers, and occupational therapists — identifying which ADL tasks matter most, which current robot behaviors are frustrating, and what failure modes are acceptable vs. unacceptable. This kind of needs-assessment work is chronically underdone in the robotics literature and directly informs which problems to prioritize.

---

## Would JEPA help?

### Where JEPA offers clear gains

**Data efficiency via broad pretraining.** JEPA's core advantage — learning compressed, structured world representations from large video datasets without behavioral supervision — is directly relevant to the assistive-robotics data scarcity problem. A model pretrained on internet home videos may generalize to novel household objects faster than a behavioral cloning model trained only on robot demonstrations. [V-JEPA 2](../../entities/v-jepa-2.md) demonstrated zero-shot Franka manipulation after video-only pretraining.

**Image-goal planning.** [DINO-WM](../../entities/dino-wm.md) (NYU + FAIR — the same NYU group behind OK-Robot and RUM) uses a JEPA-style frozen DINOv2 feature extractor + learned predictor for zero-shot model-predictive control from an image goal. This is directly applicable to "fetch this item" assistive tasks: specify goal as an image, roll out candidate trajectories in latent space, execute the best one. No reward engineering required.

**Action anticipation.** The JEPA family's strongest empirical result is action anticipation on Ego4D / Epic-Kitchens (SOTA at time of filing). For assistive robotics, anticipating a user's next intended action from their body language or gaze — before they have to explicitly command the robot — is a meaningful HRI upgrade. [JEPA task capabilities](../world-models/jepa-task-capabilities.md) documents this capability.

**Per-user world model adaptation.** A JEPA world model can in principle be fine-tuned on a small corpus of videos of a specific user in their specific home, building a personalized internal model of their environment and behavior. This is speculative but mechanistically plausible, and more data-efficient than fine-tuning a behavioral cloning policy.

### Where JEPA does not yet help

**Contact-rich manipulation.** JEPA models predict in the latent space of visual observations. They do not currently model contact forces, tool compliance, or the tactile feedback required for opening bottles, folding fabric, or physical-contact assistance. The [JEPA task capabilities](../world-models/jepa-task-capabilities.md) survey shows JEPA is weakest here relative to other approaches.

**Long-horizon task planning.** JEPA predictors are trained on short video clips (1–16 seconds). Composing predictions across a 10+ step assistive task — plan, execute, recover from failure, re-plan — is not demonstrated in the current literature. This is an open research problem for world models generally, not just JEPA.

**Language grounding for user commands.** Current JEPA models are vision-only or vision+state. A user saying "get my blue mug from the counter but not the one with the chip" requires language understanding that VLA architectures handle more naturally than pure JEPA models. Hybrid VLA+JEPA approaches ([VLA-JEPA](../../entities/vla-jepa.md)) are emerging but not mature.

### Bottom line

JEPA is a plausible accelerant for two of the seven blocking problems: **data efficiency** (problem 7) and **per-user personalization** (problem 5), and potentially useful for **long-horizon planning** via learned world models (problem 3). It does not directly address **reliability in clutter**, **safe human contact**, or **accessible HRI**. An independent researcher could meaningfully contribute by applying DINO-WM (the JEPA-family model closest to deployment) to assistive-relevant tasks — it is open-source, runs on a workstation GPU, and the NYU group's codebase integrates directly with Stretch.

---

## Related pages
- [Assistive robotics](../../concepts/robotics/assistive-robotics.md)
- [OK-Robot](../../entities/ok-robot.md)
- [Robot Utility Models](../../entities/robot-utility-models.md)
- [Stretch](../../entities/stretch.md)
- [JEPA task capabilities](../world-models/jepa-task-capabilities.md)
- [V-JEPA 2](../../entities/v-jepa-2.md)
- [DINO-WM](../../entities/dino-wm.md)
- [VLA-JEPA](../../entities/vla-jepa.md)
