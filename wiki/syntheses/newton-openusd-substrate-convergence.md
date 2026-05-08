---
title: Newton + OpenUSD — the substrate convergence
type: synthesis
created: 2026-05-07
updated: 2026-05-07
tags: [newton, openusd, usdphysics, mjcphysics, physics-engine, isaac-lab, mujoco-playground, linux-foundation, infrastructure, cad]
---

# Newton + OpenUSD — the substrate convergence

A synthesis on a structurally important fact buried in the simulator landscape: the GPU physics engine and the scene-description format underneath the two leading agentic-robotics training stacks are converging on a **vendor-neutral, cross-stack substrate**. **[Newton](../entities/newton-physics-engine.md)** (the physics engine) and **[OpenUSD](../entities/openusd.md)** (the scene format and physics-schema layer) are now plug-compatible into both [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md) and DeepMind's [MuJoCo Playground](../entities/mujoco-playground.md). That is unusual; traditionally each simulator stack ships its own physics engine and scene format, which locks researchers in. This page works through what is converging, why it matters, and what is still uncertain.

> [!note] Updated 2026-05-07 with deeper OpenUSD detail
> The first draft of this synthesis treated OpenUSD as a "scene format" — a useful but narrow framing. Subsequent ingest of the [UsdPhysics whitepaper](../sources/openusd-rigid-body-physics-proposal.md) and the [NVIDIA OpenUSD-for-robotic-simulation blog](../sources/nvidia-openusd-for-robotic-simulation.md) established that OpenUSD ships **formal robotics physics schemas** (articulations, joint drives, collision filtering) and that [DeepMind](../entities/google-deepmind.md) is **authoring** USD schema plugins (`MjcPhysics`), not merely consuming them. Both facts strengthen the convergence argument.

## What is actually converging

| Layer | Old state | New state (2026) |
|---|---|---|
| Physics engine | PhysX (Isaac Sim only), MuJoCo (DeepMind only), Bullet, Drake — each silo | [Newton](../entities/newton-physics-engine.md) — pluggable into both Isaac Lab and MuJoCo Playground |
| Scene format | Per-stack URDF / MJCF / proprietary | [OpenUSD](../entities/openusd.md) as a shared scene-description target |
| Physics schema | Per-engine internal | `UsdPhysics` baseline + per-solver USD plugins (`MjcPhysics`, `newton-usd-schemas`) |
| GPU compute kernel | PhysX (CUDA), MJX (JAX), Warp, custom | NVIDIA Warp (Newton's compute kernel) plus MJX continuing |
| CAD ingestion | Per-vendor exporters | OpenUSD Exchange SDK + Omniverse Connectors (SolidWorks, CATIA, AutoCAD, Creo, JT) |
| Governance | Vendor-controlled | Linux Foundation, with [NVIDIA](../entities/nvidia.md) + [Google DeepMind](../entities/google-deepmind.md) + [Disney Research](../entities/disney-research.md) as co-developers |

Two sources establish the cross-stack pluggability directly:

- The [NVIDIA Newton Physics Engine Developer Page](../sources/nvidia-newton-physics-engine-developer-page.md) explicitly states Newton is "designed as a pluggable backend for both [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md) and [MuJoCo Playground](../entities/mujoco-playground.md)."
- The [MuJoCo Playground Paper](../sources/mujoco-playground-paper.md) (DeepMind, RSS 2025) says Playground "optionally backends to [Newton](../entities/newton-physics-engine.md) in 2026."

Both vendors confirm it from their own side. The [NVIDIA OpenUSD-for-robotic-simulation blog](../sources/nvidia-openusd-for-robotic-simulation.md) (Aaron Luk, Pomi Lee, Renato Gasoto, March 2025) is the third source — it confirms Isaac Sim 5.0 / Omniverse Kit 107 runs OpenUSD 24.05 and treats USD as the scene format underneath the entire physics stack.

## OpenUSD as a robotics physics schema, not just a scene format

The [UsdPhysics whitepaper](../sources/openusd-rigid-body-physics-proposal.md) (Apple + NVIDIA + Pixar, v1.0, 2020) establishes that OpenUSD ships **formal robotics physics schemas**, not just scene-description geometry:

- **`PhysicsArticulationRootAPI`** marks the root of an articulated robot and explicitly distinguishes **floating articulations** (mobile / aerial robots) from **fixed articulations** (industrial arms bolted to the floor) — robotics jargon recognized in the open standard.
- **Joint subtypes** (revolute, prismatic, fixed, spherical, distance) and **joint drives** (`stiffness * (targetPosition - p) + damping * (targetVelocity - v)`) cover the motor models robotics needs.
- **Mass / inertia / collision-filtering APIs** complete the rigid-body specification.

This matters for the convergence argument: OpenUSD isn't just a 3D file format that happens to be loaded by multiple simulators. It is a **standardized robotics-physics representation** that both stacks can write and read, with the schema work itself happening in the open. The schema bakes robotics concepts in at the foundation, not as a vendor add-on.

## DeepMind authors USD schema plugins, not just consumes them

The single most consequential update to this synthesis since the first draft: **`MjcPhysics` is a USD schema plugin maintained by [Google DeepMind](../entities/google-deepmind.md)**. It authors MuJoCo-specific solver attributes (integrator type, constraint solver algorithm, tolerance, contact settings) onto USD prims, allowing MuJoCo's solver-specific knowledge to live inside a USD scene.

Equally important: **`newton-usd-schemas`** (Apache 2.0, Linux Foundation governance) defines `NewtonSceneAPI` and is explicitly designed as a **"proving ground"** — physically meaningful parameters generalizable across at least two Newton solvers may eventually be **promoted into upstream `UsdPhysics`**. v0.2.0 was released 2026-05-07 (the day this synthesis was filed); 52 commits and 7 releases indicate active work.

There is also a concrete **`mujoco-usd-converter`** tool living in the `newton-physics` GitHub org. The bridge between MuJoCo's MJCF format and USD is being built **inside the Newton ecosystem** — i.e., the cross-stack bridge is hosted in the cross-vendor governance domain, not by either parent vendor.

The combined picture: **DeepMind ships USD plugins for MuJoCo**, **NVIDIA + DeepMind + Disney govern Newton**, **Newton hosts the MuJoCo→USD converter**, and **Newton's own schemas are designed to feed back into Pixar's UsdPhysics base**. That is not "DeepMind tolerating USD"; it is DeepMind investing engineering in USD as cross-stack infrastructure.

## Why a shared physics substrate is structurally unusual

Physics engines have historically been the stickiest part of a robotics simulator stack. They embed assumptions about contact models, integrator schemes, units, and asset formats that propagate up through the entire training pipeline. Switching engines typically meant rewriting environment definitions, re-tuning rewards, and revalidating sim-to-real transfer. That stickiness has been the core moat for simulator vendors.

Newton breaks the pattern by being designed from the start as a *backend*, not a stack. The compute kernel ([NVIDIA](../entities/nvidia.md) Warp) is the same; the scene format (OpenUSD) is the same; the wrapping framework (Isaac Lab vs. MuJoCo Playground) is what changes. A policy trained against Newton in Isaac Lab can in principle be evaluated against the same Newton in MuJoCo Playground without re-authoring physics. That has not been possible across competing simulator stacks before.

## What Linux Foundation governance buys

The same [developer page](../sources/nvidia-newton-physics-engine-developer-page.md) flags "Linux Foundation governance gives vendor-neutral oversight despite heavy NVIDIA contribution." This matters because:

1. **DeepMind protection.** DeepMind would not invest its researchers' time in shipping MJX → Newton interop if Newton were a single-vendor project NVIDIA could license-flip. Linux Foundation governance creates a credible commitment that the substrate stays open.
2. **Disney's seat.** [Disney Research](../entities/disney-research.md)'s involvement is the puzzle piece — Disney isn't a robotics vendor in the GR00T / Optimus / Pi sense. Its stake is presumably entertainment-grade physics for character animation and theme-park robotics; co-developer status keeps Newton's contact and soft-body models fit for high-fidelity entertainment use, not just industrial manipulation. The cross-pressure widens what Newton has to handle correctly.
3. **Reduced single-vendor moat.** A roboticist betting on Newton today has structural insurance that no one company can pull the rug.

## Why OpenUSD is the other half

OpenUSD handles geometry, scene composition, and asset interchange — and, via `UsdPhysics`, the formal robotics physics schemas described above. Both NVIDIA's Omniverse / Isaac Sim line and DeepMind's MJX-based stack now consume OpenUSD as a scene format and contribute to its physics-schema layer. **Same scene, same physics schema, same Newton runtime, different training framework** is the new shape.

URDF and MJCF are not going away. The [practitioner survey](../sources/source-robotics-urdf-mjcf-usd-comparison.md) establishes that the three formats stratify by use case — URDF for ROS / motion planning, MJCF for MuJoCo RL, USD for large environments and Omniverse-modern simulators — and the [NVIDIA blog](../sources/nvidia-openusd-for-robotic-simulation.md) explicitly lists URDF / MJCF / SDFormat → OpenUSD conceptual mapping as **planned but unshipped** roadmap work. The convergence is happening at the physics-schema layer (`UsdPhysics` + per-solver plugins) and at the multi-asset scene-composition layer, while URDF and MJCF remain the dominant single-robot description formats above them.

## CAD ingestion — the upstream half nobody else addresses

Most of the simulator landscape ignores where assets come from. OpenUSD's third structural advantage is its position as **the target format for CAD-to-simulation pipelines**:

- **NVIDIA's Omniverse Connector ecosystem** ships native connectors for SolidWorks, CATIA, AutoCAD, Creo. The [JT pipeline blog](../sources/nvidia-cad-to-usd-jt-workflows.md) documents the ISO-14306 Jupiter Tessellation case end-to-end: `omni.kit.converter.jt_core` + `omni.services.convert.cad`, built on the **OpenUSD Exchange SDK**, with `omni.scene.optimizer` producing 82% vertex reduction in their example.
- **Okino PolyTrans|CAD+DCC** is a third-party SolidWorks→USD converter (via STEP AP204 / IGES BREP intermediates), giving an option outside the NVIDIA ecosystem.

> [!warning] Joint / kinematic survival through CAD→USD is the open question
> Sources cover geometry, hierarchy, and metadata preservation well. None explicitly addresses how SolidWorks mates → `PhysicsJoint` types is automated. The implication is that for robot-arm import, joint topology is **re-authored** inside USD/Isaac Sim after geometry import, despite Omniverse marketing claims about "eliminating manual URDF authoring." This is a meaningful caveat for any team planning a CAD-only-to-trained-policy pipeline.

The implication for the convergence argument: even if the simulators converge on Newton+USD, the **CAD-to-physics-ready-asset workflow remains lossy** in 2026. That is the single biggest unresolved gap in the substrate story.

## Implications for policy researchers and tool builders

- **Cross-stack policy mobility is on the table.** A research group training in Isaac Lab can plausibly evaluate against MuJoCo Playground (or vice versa) without re-authoring physics or scenes. This was not possible across competing stacks before 2026.
- **Vendor-neutral substrate, vendor-specific framework.** The interesting ML differentiation moves *up the stack* — to environment APIs, learning frameworks ([Isaac Lab](../entities/nvidia-isaac-lab.md) vs Playground vs ManiSkill), and model libraries ([GR00T](../entities/nvidia-groot.md), [VLAs](../concepts/vla-models.md)). The physics layer becomes commoditized infrastructure, like LLVM for compilers or Linux for OSes.
- **The schema-promotion path is the long-term moat-eraser.** Newton's `newton-usd-schemas` is explicitly designed so that cross-solver-meaningful parameters get promoted into upstream `UsdPhysics`. If that pipeline runs, vendor-specific physics customization becomes a *temporary* extension that the standard absorbs over time — the reverse of the historical pattern where vendors hoard extensions.
- **The lock-in moves to assets and tooling.** Whichever stack has better robot models, better scene libraries, and better RL infrastructure wins — but the floor (physics + scene format) is shared.
- **Genesis and other custom-physics simulators are now exceptions.** [Genesis](../entities/genesis.md) uses its own Python-first custom physics; [ManiSkill](../entities/maniskill.md) sits on [SAPIEN](../entities/sapien.md). Both can still win on domain-specific advantages (Genesis's claimed 10–80× speedup, SAPIEN's manipulation-realism), but they now have to justify the *non-Newton* choice.
- **CAD ingestion is the lossy upstream step.** The substrate convergence is real at the simulator layer; CAD-to-USD pipelines preserve geometry well but kinematic-joint authoring is still a manual step. Teams targeting full CAD-to-trained-policy automation should budget for this gap.

## What is still uncertain

> [!warning] Real cross-stack adoption is not yet demonstrated in the wiki
> Both source pages assert pluggability. Neither shows a worked example of a single policy / scene running unchanged across Isaac Lab and MuJoCo Playground via Newton. The architectural promise is in the docs; the empirical demonstration is not yet ingested here.

- **Throughput parity?** No source compares Newton's throughput against MJX or [Genesis](../entities/genesis.md) on the same task. The [MuJoCo Playground Paper](../sources/mujoco-playground-paper.md)'s own open question is whether Playground throughput matches Isaac Lab on identical tasks; with Newton as a shared backend, that question becomes empirically tractable but isn't answered.
- **Will MuJoCo Playground actually default to Newton?** "Optionally backends" is not "primarily backends." MJX continues; Newton is one option. If the JAX ecosystem advantages of MJX outweigh the cross-stack advantages of Newton, DeepMind may keep MJX as the default and Newton as a compatibility layer.
- **Disney's actual contribution depth?** [The Disney Research entity page](../entities/disney-research.md) is a stub. The relationship is real (the developer page lists Disney as a co-developer) but the specific technical contributions Disney makes to Newton are not yet documented in the wiki.
- **Closed engines still ship policies in production.** Tesla Optimus, Pi π0, Skild, and other closed teams use undisclosed in-house simulators. The Newton / OpenUSD convergence is in the *open* research stack; closed industry stacks are not visibly affected.
- **GR00T version drift.** Sources reference both GR00T N1.6 GA ([NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)) and N1.7 Early Access ([Top 10 Physical AI Models 2026](../sources/top-10-physical-ai-models-2026.md)) as the current Newton/Isaac Lab-bundled VLA. This is the same standing inconsistency tracked in the simulator survey; not Newton-specific but worth noting whenever Newton is described in context.
- **CAD mate → `PhysicsJoint` automation.** The biggest *practical* gap. None of the four ingested OpenUSD/CAD sources documents automated SolidWorks-mate-to-USD-joint conversion. If anyone ships this, it changes the robot-design-to-trained-policy timeline meaningfully.
- **Will URDF / MJCF / SDFormat → OpenUSD conceptual mapping ship?** The [NVIDIA blog](../sources/nvidia-openusd-for-robotic-simulation.md) (March 2025) lists this as planned roadmap work. As of 2026-05 it is unclear whether the mapping is now shipped, partially shipped, or still aspirational. Worth a follow-up source on the next ingest.

## Sources used in this synthesis

- [NVIDIA Newton Physics Engine Developer Page](../sources/nvidia-newton-physics-engine-developer-page.md)
- [NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)
- [MuJoCo Playground Paper](../sources/mujoco-playground-paper.md)
- [OpenUSD Rigid Body Physics Proposal](../sources/openusd-rigid-body-physics-proposal.md)
- [Using OpenUSD for Modular and Scalable Robotic Simulation](../sources/nvidia-openusd-for-robotic-simulation.md)
- [Robot Simulation File Formats — URDF vs MJCF vs USD](../sources/source-robotics-urdf-mjcf-usd-comparison.md)
- [Building CAD-to-USD Workflows with NVIDIA Omniverse](../sources/nvidia-cad-to-usd-jt-workflows.md)

## Related

- [OpenUSD](../entities/openusd.md) — entity page covering the format, UsdPhysics schema, and per-solver extensions.
- [Newton physics engine](../entities/newton-physics-engine.md) — entity page.
- [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md) / [MuJoCo Playground](../entities/mujoco-playground.md) — the two stacks converging on Newton.
- [Simulators for agentic robotics — 2026 landscape](simulators-for-agentic-robotics-2026.md) — surveys the broader simulator field; this page zooms into one structural insight from it.
