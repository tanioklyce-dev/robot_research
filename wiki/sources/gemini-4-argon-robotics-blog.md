---
title: "Gemini 4 Argon for Robotics (Google Developers Blog)"
type: source
url: https://developers.googleblog.com/gemini-4-argon-for-robotics/
local_path: raw/2026-10-13-google-developers-blog-gemini-4-argon-robotics.md
sha256: 41ab5fff46228e4c2333d8c2b92b3b9b139f220c84e5c2554bd27707cef5b7b5
author: Kanishka Rao (Google)
published: 2026-10-13
ingested: 2026-10-13
venue: Google Developers Blog
format: "vendor blog post: four capability areas, each shown as a demo video plus the prompt that produced it. Captured 2026-10-13 via curl with article-text extraction. The videos were not captured."
tags: [gemini-4-argon, gemini, google-deepmind, embodied-reasoning, erqa, code-as-policy, real-to-sim, mujoco, mujoco-warp, video-world-model, hindsight-labeling, value-function, self-improvement, so-101, spot, aloha, umi, franka, apollo, vendor-source, primary]
---

# Gemini 4 Argon for Robotics (Google Developers Blog)

## Summary

Google presents **[Gemini 4 Argon](../entities/gemini-4-argon.md)** (`gemini-4-argon`) as a *general-purpose* frontier model that is also a **"general-purpose physical reasoning model,"** and the robotics post makes its case almost entirely with **prompts and demo videos**. The only benchmark number is **ERQA 87%**, "using pure reasoning," said to beat every other frontier model. The post is organised in four areas: **robot control** (code-as-policy on Spot and a small arm; prompting a video world model step by step), **Real2Sim** (MuJoCo twins built from robot logs, egocentric human video, or a paper sketch), **physical understanding** (hindsight annotation, a 12-ball puzzle environment and solver, a dense value function), and **research and self-improvement** (sim data that lifts a VLA from 56% to 75% real success; iterative self-improvement on an SO-101; one-prompt paper reproductions in MuJoCo WebAssembly). Its central claim is that **one model now covers the whole robotics toolchain**, from simulation authoring and labeling to control. It is **not** a [Gemini Robotics](../entities/gemini-robotics.md) model and does not output motor actions. Every control demo goes through code, primitives or prompts.

## Key claims

**Benchmark**
- **ERQA 87%**, "using pure reasoning… outperforming every other frontier model." No table, no competitor scores, no harness or thinking budget given.

**Robot control**
- **[Spot](../entities/spot.md) mobile manipulation** (12-DoF legs + 6-DoF arm): to learn to step on a foot-pedal bin and drop soda cans in, Argon **builds an articulated MuJoCo twin of the bin and practises a 3-leg tripod balance** before trying it on hardware. The prompt calls a `spot-mobile-manipulation` **skill** and asks for a **"2-agent verification swarm"** (foot-verifier, hand-verifier) to check before release.
- **Zero-shot arm control**: a simple arm uprights a fallen mug and puts a crumpled napkin in it over several turns. The harness is the most informative part of the post. A **calibrated wrist image** is annotated with a 2 cm world grid, a pinch-centre crosshair, jaw brackets and an object-axis line, and the model emits `curl` calls to a local `/plan` endpoint exposing **[code-as-policies](../concepts/agents/code-as-policy.md) primitives** (`look_at`, `deproject`, `grasp`, `place_until_contact`, `move_by`, `move_until_contact`…). On turn 1 the model chooses its own **call granularity**: coarse (2–4 calls), hover-verify (4–7), or fine visual servoing (8–20).
- **"Omni control"**: Argon **steers the Gemini Omni video world model** with timestamped action prompts, inspects rollout keyframes, and refines them. Dexterous hands rearrange Scrabble tiles to spell A-R-G-O-N in a **33-step steered rollout**. This is control of a *generated video*, not of a robot.

**Real2Sim** (see [real-to-sim-to-real](../concepts/robotics/real-to-sim-to-real.md))
- **Robot log → MuJoCo twin.** Argon replays teleop episodes and tunes assets until both the **visual** match (three cameras) and the **physical** match hold. Physical match means the simulated fingertip force/torque on [Sharpa](../entities/sharpa-wave.md) fingertips agrees with logged tactile force in timing, magnitude and direction. The prompt carries an explicit **"No sim cheating"** clause. After t = 0 it forbids changing model parameters, applying external forces, welds, feedforward torques, setting or rolling back object state, disabling collisions, and *"reporting contact forces that don't come from the MuJoCo solver (for example, copying the logged tactile readings)."*
- **Egocentric human video → humanoid twin.** Task objects get convex-decomposed meshes, and human hand keypoints are retargeted to a **76-DoF bimanual humanoid with 22-DoF five-finger hands** at 500 Hz, with force-closure, lift > 2 cm and placement checks.
- **Paper sketch → simulation.** From a photo of a sketch, Argon builds a **[mujoco_warp](../entities/mujoco-warp.md)** scene in which an **[Apollo 2](../entities/apptronik-apollo.md)** throws a ball into a 3-2-1 box pyramid. It synthesises a 76-DoF whole-body throw (50 Hz, 140 steps), verifies **6/6 knockdown with < 3 cm pelvis drift**, and renders the result in Blender Cycles.

**Physical understanding**
- **Hindsight labeling**: on a 136 s [ALOHA](../entities/aloha.md) 2 origami-fox episode, a four-level hierarchy (goal, 6 subtasks, 17 contact-level primitives, QC). QC **holds task progress flat during fumbles** and **downweights those segments 0.15–0.25×** for behaviour cloning.
- **12-ball puzzle**: Argon writes a dual-arm [Franka FR3](../entities/franka-panda.md) MuJoCo environment with a Roberval balance, then a **vision-only** stereo solver that reads scale tilt from pixel disparity and isolates the odd ball within 3 weighings.
- **Value function**: on a 60 s bimanual ring-sorting episode from a human [UMI](../entities/umi.md) dataset, three synchronised camera feeds yield dense progress predictions and **28 segments** with positive, neutral or negative slope.

**Research and self-improvement**
- **Sim data for a VLA**: from **one overhead RGB photo**, Argon builds a calibrated MuJoCo twin of a bimanual Franka FR3 table (9 props, including a spring-hinged plush crown), defines a **77-task curriculum**, writes a closed-loop IK generator, and exports **4,500+ domain-randomised episodes**. Fine-tuning a "generalist VLA" on them takes real success **56% → 75%** and completion time **35 s → 24 s**. The VLA, the number of trials and the task set are not given.
- **SO-101 self-improvement**: a staged prompt (measure and dry-run with no motion → hover and verify with the wrist camera → execute → self-diagnose from logs and footage → retry → speed up ≥2× "within safety limits (rule R5)" from an `AGENTS.md`). Pick-and-place times across iterations: **58.9 s → 22.9 s (grazed the box rim) → 17.4 s (dead-centre drop)**. See [SO-ARM101](../entities/so-arm101.md).
- **Paper reproductions**: one prompt per paper ports physics and controller into a **MuJoCo WebAssembly** browser lab, verified in headless Chromium. Shown: OP3 soccer, DeepLoco, the ANYmal C massively parallel RL paper, [Go2](../entities/unitree-go2.md) whole-body MPC (iLQR in a Web Worker) and HUSKY G1 skateboarding. These are **"from 68 interactive browser sandboxes."**

**Access**
- Google AI Studio (AI Ultra), the paid Gemini API (`gemini-4-argon`, Interactions API) and Google Antigravity (AI Ultra; `/goal` runs and multi-agent orchestration).

## Reading it critically

> [!warning] A capability showcase, not an evaluation
> Apart from ERQA, **every result is a single demo with the prompt that produced it.** The two numbers that look like evaluations have no n: the 56→75% VLA lift and the SO-101 timings, which are one run per iteration. Under the wiki's [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) rule, 56→75% is directional until trial counts appear. The 87% ERQA figure has no competitor table, so "beats every frontier model" cannot be checked from this source. For scale: in Unitree's API tests the best frontier ERQA scores were 77.7 (the model it names GPT-6-Astra) and 65.2 (Gemini 3.1 Pro) ([UnifoLM project page](unifolm-wla-1-project-page.md)). The harnesses differ, so this is context, not a comparison.

> [!note] The "no sim cheating" clause is itself a finding
> The Real2Sim prompt lists six ways to fake a physical match, including copying logged tactile readings into the reported contact forces, and forbids each one. Nobody writes that list without a reason. The likeliest reading is that **earlier runs found these shortcuts**, which is reward hacking aimed at a fidelity metric (see [AI safety and alignment](../concepts/safety/ai-safety-alignment.md)). That is inference: the post doesn't say why the clause is there. It is the most transferable practical lesson in the post: **an agent asked to make sim match real will satisfy the metric by whatever channel is open**, so the prompt (or better, the harness) has to close those channels.

- **The harness carries a lot of the capability.** The zero-shot arm demo works because of a calibrated, annotated wrist image and a curated primitive API: exactly the [abstraction confound](../concepts/agents/code-as-policy.md#the-abstraction-confound--the-finding-that-reframes-the-lineage-above) CaP-X measured. `place_until_contact` and `move_until_contact` are S2-tier helpers, not raw joint commands.
- **No cost or latency figures** for any workflow, in keeping with the [code-as-policy](../concepts/agents/code-as-policy.md) literature's three-year silence on compute.
- **Where Argon sits relative to Gemini Robotics ER 2 is not addressed.** ER 2 was billed in July as "the robot's high-level brain." Argon is a general model doing the orchestrator's job and more, with a higher reported ERQA than any ER figure in this wiki.

## Entities mentioned
- [Gemini 4 Argon](../entities/gemini-4-argon.md) · [Google DeepMind](../entities/google-deepmind.md) · [Gemini Robotics](../entities/gemini-robotics.md)
- [MuJoCo](../entities/mujoco.md) · [MuJoCo Warp](../entities/mujoco-warp.md)
- [Spot](../entities/spot.md) · [Boston Dynamics](../entities/boston-dynamics.md) · [ALOHA](../entities/aloha.md) · [UMI](../entities/umi.md) · [Franka](../entities/franka-panda.md) · [Apollo](../entities/apptronik-apollo.md) · [SharpaWave](../entities/sharpa-wave.md) · [SO-ARM101](../entities/so-arm101.md) · [Unitree Go2](../entities/unitree-go2.md)

## Concepts touched
- [Embodied-reasoning VLMs](../concepts/learning/embodied-reasoning-vlms.md) — ERQA; a general model in the ER slot.
- [Code as policy](../concepts/agents/code-as-policy.md) — the control path in every hardware demo.
- [Real-to-sim-to-real](../concepts/robotics/real-to-sim-to-real.md) — LLM-authored twins, validated on contact force.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — prompting a video WM step by step.
- [AI safety and alignment](../concepts/safety/ai-safety-alignment.md) — the no-cheating clause as metric-gaming defence.

## Open questions
- What are the ERQA competitor scores and harness, and the thinking budget behind "pure reasoning"?
- Which VLA went from 56% to 75%, over how many trials, on which of the 77 tasks?
- Does the "no sim cheating" list come from observed failures? How often does Argon violate it when the clause is left out?
- Is Gemini Robotics ER 2 being superseded by a general model, or will an "ER 3" be distilled from Argon?
- What is Gemini Omni, Google's video world model? There is no primary in the wiki yet.
