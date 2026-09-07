---
title: The NVIDIA robot-AI stack — what is owned, what is contested, and where the lock actually binds
type: synthesis
created: 2026-09-07
updated: 2026-09-07
tags: [nvidia, vertical-integration, jetson, cuda, isaac-ros, cosmos, groot, halos, lerobot, hugging-face, hailo, newton, evaluation, platform-risk]
---

# The NVIDIA robot-AI stack

The [Hugging Face acquisition](../../sources/nvidia-hugging-face-acquisition.md) prompted this page, but the acquisition is not the finding. The finding is that **this wiki has been documenting a single vertically-integrated stack one entity page at a time for a year without ever drawing it**, and that when you do draw it, three things show up that no individual page contains: **where the lock actually binds** (not where it looks like it binds), **what erosion looks like when it happens** (there is already a documented instance), and **a structural pattern in which NVIDIA supplies both the artifact and the instrument that measures it** — at three separate layers.

## The stack, from this wiki's own pages

| Layer | NVIDIA holding | Credible independent alternative |
|---|---|---|
| **Edge silicon** | [Jetson Thor](../../entities/jetson-thor.md) / IGX, [Orin family](../../entities/jetson-orin-nx.md), [DGX Spark](../../entities/dgx-spark.md) | [Hailo](../../entities/hailo.md) NPUs — **for perception, not policy** (see below) |
| **Edge OS / runtime** | JetPack, [Jetson Linux](../../entities/jetson-linux.md) | generic Ubuntu on x86 / ARM |
| **GPU middleware** | [Isaac ROS](../../entities/isaac-ros.md) (GEMs) on [ROS 2](../../entities/ros2.md) | ROS 2 itself is independent; the acceleration is not |
| **Agent runtime / security** | [OpenShell](../../entities/nvidia-openshell.md), [NeMo Guardrails](../../entities/nemo-guardrails.md) | generic containers; [MCP](../../entities/ros2-mcp-server.md) tooling |
| **Simulation** | [Isaac Sim](../../entities/nvidia-isaac-sim.md) / [Isaac Lab](../../entities/nvidia-isaac-lab.md) / [Isaac Gym](../../entities/isaac-gym.md) | **strong** — [MuJoCo](../../entities/mujoco.md), [Genesis](../../entities/genesis.md), [Drake](../../entities/drake.md), [robosuite](../../entities/robosuite.md), [ManiSkill](../../entities/maniskill.md) |
| **Physics substrate** | **[Newton](../../entities/newton-physics-engine.md)** — but see the counter-case below | Newton *is* the shared one |
| **World models** | [Cosmos](../../entities/nvidia-cosmos.md) (Cosmos 3 omni-model) | [FLUX 3](../../entities/flux-3.md), V-JEPA / [LeJEPA](../../entities/leworldmodel.md) line |
| **Robot foundation models** | [GR00T](../../entities/nvidia-groot.md) ([GEAR](../../entities/nvidia-gear.md)) | [π0 / π0.5](../../entities/physical-intelligence.md), [GEN-1.5](../../entities/gen-1-5.md), [S1](../../entities/skild-ai.md), [SmolVLA](../../entities/smolvla.md) |
| **AV models** | [Alpamayo](../../entities/alpamayo.md) | — (outside this wiki's scope) |
| **Certified safety** | [Halos](../../entities/nvidia-halos.md) + ANAB-accredited inspection lab | none in this wiki |
| **Evaluation** | [RoboLab](../../entities/nvidia-robolab.md) | [RoboArena](../../entities/roboarena.md), LIBERO, SIMPLER |
| **Cloud / fine-tuning** | [Brev](../../entities/nvidia-brev.md), DGX | [the rental landscape](nvidia-gpu-rental-landscape.md) |
| **Model distribution** | **[Hugging Face](../../entities/hugging-face.md), [LeRobot](../../entities/lerobot.md), [SmolVLA](../../entities/smolvla.md)** — pending, H1 2027 | **none this wiki knows of** |

Twelve layers. Before the acquisition, NVIDIA held a position in eleven.

## Where the lock actually binds — and it is not the layer you would guess

The instinct is that the acquisition is the lock, because distribution is the newest and largest piece. **That is not what this wiki's own evidence says.** The binding constraint was identified months earlier, in a page written about a $180 accessory:

> **An NPU runs *compiled models*, not your code.** A [Hailo](../../entities/hailo.md) NPU executes models you have compiled to HEF ahead of time, on an x86 host, via Hailo's Dataflow Compiler. A Jetson runs **arbitrary CUDA/PyTorch** — you `pip install lerobot` and your ACT / Diffusion Policy / SmolVLA / π0.5 checkpoint runs unchanged.
> — [Hailo NPU vs Jetson for XLeRobot](hailo-npu-vs-jetson-xlerobot.md)

That page's verdict, reached without any reference to platform strategy: **Hailo can carry perception and agent reasoning; the manipulation policy still wants CUDA.** Three compute jobs, and CUDA is load-bearing for exactly one of them — the one LeRobot exists to run.

> [!note] The lock is CUDA-at-the-policy-layer, and the acquisition sits directly on top of it
> Every layer above silicon is substitutable at some cost, and the wiki has instances: MuJoCo and Genesis for Isaac Sim, π0 and GEN-1.5 for GR00T, RoboArena for RoboLab, plain ROS 2 for Isaac ROS. **What has no substitute in this wiki is "run an arbitrary PyTorch policy checkpoint, onboard, reactively."**
>
> So the acquisition's significance is not that distribution is now owned. It is that **the distribution layer for open policy weights now sits on top of the one layer with a genuine lock**, and the same company owns both ends. That is a different and more specific claim than "NVIDIA is vertically integrated."

## What erosion looks like — and it has already happened once

The [neutrality commitments](../../sources/nvidia-hugging-face-acquisition.md) — *"NVIDIA compute will not be required,"* multi-accelerator support, *"support other silicon vendors"* — are specific, are in an SEC filing, and are under **Item 8.01, a voluntary disclosure**. The question is what a breach would even look like, since no one expects an announcement.

**The wiki already documented the answer, in NVIDIA's own middleware, a month before the acquisition:**

> **Correction 2026-08-17 — Isaac ROS 4.x dropped Jetson Orin entirely.** Per the supported-platform table, the *only* combinations NVIDIA tests and supports are **Jetson Thor (T5000/T4000) on JetPack 7.1**, **x86_64 on Ubuntu 24.04**, and **DGX Spark**. No Orin appears — not under JetPack 6, not under JetPack 7.
> — [Isaac ROS](../../entities/isaac-ros.md)

No decision was announced. A support table stopped listing a platform, and the wiki's own page had to be corrected because it had described the product from an older recipe that no longer held.

> [!warning] The precedent is stronger than a hypothetical because it was applied to NVIDIA's own hardware
> Orin is not a competitor's chip. It is NVIDIA's previous generation, and it was dropped from NVIDIA's ROS acceleration layer without ceremony. If support narrowing happens *impersonally* — driven by test-matrix cost, not strategy — then it will happen to a third-party accelerator at least as readily.
>
> **So the thing to watch for in LeRobot is not a policy change. It is a support table, a CI matrix, and a set of features that quietly assume CUDA.** That is checkable, and it is why the [Hailo comparison](hailo-npu-vs-jetson-xlerobot.md) needs a **before-and-after** rather than a one-off re-run: the "before" has to be captured while it is still true.

## The counter-case: Newton, which NVIDIA declined to own

A page arguing pure enclosure would be wrong, and the clearest counter-evidence is the physics layer.

**[Newton](../../entities/newton-physics-engine.md)** is co-developed by NVIDIA, **Google DeepMind** and **Disney Research**, and managed under the **Linux Foundation** — built on NVIDIA Warp and [OpenUSD](../simulators/newton-openusd-substrate-convergence.md). NVIDIA had the position to own the GPU physics layer outright and instead put it in a foundation with two competitors on the masthead.

Two readings, and the wiki should hold both:

- **Genuine standard-setting.** The value of a physics substrate is in adoption; a foundation is how you get adoption from parties who would not adopt a vendor's engine.
- **Substrate control is sufficient control.** Newton runs on **NVIDIA Warp** and speaks **OpenUSD**. If you own the compute abstraction and the scene format, foundation governance of the layer between them costs little. The wiki's [OpenUSD-across-simulators](../simulators/openusd-support-across-simulators.md) and [substrate-convergence](../simulators/newton-openusd-substrate-convergence.md) pages are the material for judging which reading is right, and they do not settle it.

Either way: **the enclosure is not uniform, and a page that claimed otherwise would be contradicted by NVIDIA's own most-open project.**

## The pattern no single page contains: the vendor supplies the instrument

This is the synthesis's actual finding, and it is not about market share.

**At three separate layers, NVIDIA supplies both the artifact and the thing that measures it:**

| Layer | The artifact | The instrument |
|---|---|---|
| **Safety certification** | [Halos](../../entities/nvidia-halos.md) — the certified safety stack | the **Halos AI Systems Inspection Lab**, ANAB-accredited, described by its own lead as *"an **independent organization within NVIDIA**"* whose inspection certificate a notified body then relies on |
| **Standards** | Halos, designed to IEC 61508 / ISO 13849 | **[Riccardo Mariani](../../entities/riccardo-mariani.md)**, NVIDIA's head of industry safety, **convenes ISO/IEC JTC 1/SC 42/JWG 4** and is project leader of **TR 5469** and **TS 22440** — the standard AI functional safety will be certified against |
| **Policy evaluation** | [GR00T](../../entities/nvidia-groot.md), Cosmos policies | **[RoboLab](../../entities/nvidia-robolab.md)** (NVIDIA SRL) — whose methodology is a substantial part of this wiki's [robot policy evaluation](../../concepts/robotics/robot-policy-evaluation.md) page, including the failure-mode taxonomy and the sample-size argument |

None of these is an accusation, and two of them are defensible on their own terms: functional-safety standards have always been written by the people who ship the systems, and RoboLab's methodology is *good* — this wiki adopted it because it is the best available, and has said so.

> [!warning] But it should be visible, because it changes how citations here should be read
> When this wiki says a learned policy's success rate is untrustworthy below ~1,030 rollouts, it is applying **NVIDIA's** methodology. When it says Halos is the closest artifact to conformity evidence, the accreditation chain runs **through NVIDIA**. When it says TS 22440 is the most consequential unread document in the standards thread, the convenor **works for NVIDIA**. And Cosmos-Predict2 is the backbone of [mimic-video](../../sources/mimic-video-paper.md), one of the two strongest independent robot results the wiki holds.
>
> **The measuring instruments and the measured artifacts have the same author more often than any individual page reveals.** That is the thing worth carrying out of this page.

## What this changes about reading the rest of the wiki

Three practical consequences, stated as reading instructions rather than alarm:

1. **"Independent" needs checking at the layer, not the product.** [mimic-video](../../sources/mimic-video-paper.md) is a European lab's paper, published, adversarially framed against VLAs — and it runs on **Cosmos-Predict2**. Independence of *authorship* is not independence of *substrate*.
2. **Benchmarks and safety claims inherit their author.** See the table above. This does not invalidate them; it means the wiki should name the author when it cites the instrument, which it now mostly does not.
3. **The switching-cost ranking is the useful map, not the ownership list.** Simulation: cheap to leave. World models and robot FMs: real alternatives exist. **Onboard policy execution: no substitute in this wiki.** Distribution: no substitute *at all* — which is new as of this transaction, and is the honest reason the acquisition matters.

## Watch items

- **Re-run [Hailo vs Jetson on XLeRobot](hailo-npu-vs-jetson-xlerobot.md) before and after close (H1 2027).** The wiki's own instrument for *"support other silicon vendors."*
- **Watch LeRobot's support table and CI matrix**, not its announcements. The [Isaac ROS / Orin](../../entities/isaac-ros.md) precedent is the template.
- **Watch LeRobot governance** — an open project with outside contributors moving inside a vendor shipping a competing robot foundation model.
- **Watch the regulatory review.** Close is conditioned on approvals; whether neutrality becomes a *remedy* rather than a *promise* is the difference between binding and reputational.
- **Watch whether a second distribution layer appears.** The wiki has no page on alternatives to the Hub and, until now, no reason to want one.

## Sources used in this synthesis

- [NVIDIA to acquire Hugging Face](../../sources/nvidia-hugging-face-acquisition.md) — the transaction and the neutrality commitments.
- [Hailo NPU vs Jetson for XLeRobot](hailo-npu-vs-jetson-xlerobot.md) — the CUDA-at-the-policy-layer finding, arrived at independently.
- [Isaac ROS](../../entities/isaac-ros.md) + [release notes and platforms](../../sources/isaac-ros-release-notes-and-platforms.md) — the documented erosion precedent.
- [NVIDIA Halos](../../entities/nvidia-halos.md), [Industrial AI Podcast #352](../../sources/industrial-ai-podcast-nvidia-safety-strategy.md), [Riccardo Mariani](../../entities/riccardo-mariani.md) — the safety and standards half of the instrument pattern.
- [RoboLab](../../entities/nvidia-robolab.md) + [robot policy evaluation](../../concepts/robotics/robot-policy-evaluation.md) — the evaluation half.
- [Newton](../../entities/newton-physics-engine.md), [OpenUSD across simulators](../simulators/openusd-support-across-simulators.md), [substrate convergence](../simulators/newton-openusd-substrate-convergence.md) — the counter-case.
- [Cosmos](../../entities/nvidia-cosmos.md), [GR00T](../../entities/nvidia-groot.md), [GEAR](../../entities/nvidia-gear.md), [Jetson Thor](../../entities/jetson-thor.md), [OpenShell](../../entities/nvidia-openshell.md), [Brev](../../entities/nvidia-brev.md) — the layer inventory.

## Related

- [VLA deployability landscape](vla-deployability-landscape.md) · [Jetson onboard compute for XLeRobot](jetson-onboard-compute-xlerobot.md) · [Open-source robot AI projects](open-source-robot-ai-projects.md) — the pages most exposed to a change in platform neutrality.
- [Robot safety standards](../../concepts/robotics/robot-safety-standards.md) — where the standards-authorship half lands.
- [Simulators for agentic robotics 2026](../simulators/simulators-for-agentic-robotics-2026.md) — the layer with the healthiest competition.
