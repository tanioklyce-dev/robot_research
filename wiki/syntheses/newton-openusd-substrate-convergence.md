---
title: Newton + OpenUSD — the substrate convergence
type: synthesis
created: 2026-05-07
updated: 2026-05-07
tags: [newton, openusd, physics-engine, isaac-lab, mujoco-playground, linux-foundation, infrastructure]
---

# Newton + OpenUSD — the substrate convergence

A short synthesis on a structurally important fact buried in the simulator landscape: the GPU physics engine and the scene-description format underneath the two leading agentic-robotics training stacks are converging on a **vendor-neutral, cross-stack substrate**. Specifically, **[[newton-physics-engine|Newton]]** (the physics engine) and **OpenUSD** (the scene format) are now plug-compatible into both [[nvidia-isaac-lab|NVIDIA Isaac Lab]] and DeepMind's [[mujoco-playground|MuJoCo Playground]]. That is unusual; traditionally each simulator stack ships its own physics engine and scene format, which locks researchers in. This page works through what is converging, why it matters, and what is still uncertain.

## What is actually converging

| Layer | Old state | New state (2026) |
|---|---|---|
| Physics engine | PhysX (Isaac Sim only), MuJoCo (DeepMind only), Bullet, Drake — each silo | [[newton-physics-engine|Newton]] — pluggable into both Isaac Lab and MuJoCo Playground |
| Scene format | Per-stack URDF / MJCF / proprietary | OpenUSD as a shared scene-description target |
| GPU compute kernel | PhysX (CUDA), MJX (JAX), Warp, custom | NVIDIA Warp (Newton's compute kernel) plus MJX continuing |
| Governance | Vendor-controlled | Linux Foundation, with [[nvidia|NVIDIA]] + [[google-deepmind|Google DeepMind]] + [[disney-research|Disney Research]] as co-developers |

Two sources establish the cross-stack pluggability directly:

- The [[nvidia-newton-physics-engine-developer-page|NVIDIA Newton Physics Engine Developer Page]] explicitly states Newton is "designed as a pluggable backend for both [[nvidia-isaac-lab|NVIDIA Isaac Lab]] and [[mujoco-playground|MuJoCo Playground]]."
- The [[mujoco-playground-paper|MuJoCo Playground Paper]] (DeepMind, RSS 2025) says Playground "optionally backends to [[newton-physics-engine|Newton]] in 2026."

Both vendors confirm it from their own side.

## Why a shared physics substrate is structurally unusual

Physics engines have historically been the stickiest part of a robotics simulator stack. They embed assumptions about contact models, integrator schemes, units, and asset formats that propagate up through the entire training pipeline. Switching engines typically meant rewriting environment definitions, re-tuning rewards, and revalidating sim-to-real transfer. That stickiness has been the core moat for simulator vendors.

Newton breaks the pattern by being designed from the start as a *backend*, not a stack. The compute kernel ([[nvidia|NVIDIA]] Warp) is the same; the scene format (OpenUSD) is the same; the wrapping framework (Isaac Lab vs. MuJoCo Playground) is what changes. A policy trained against Newton in Isaac Lab can in principle be evaluated against the same Newton in MuJoCo Playground without re-authoring physics. That has not been possible across competing simulator stacks before.

## What Linux Foundation governance buys

The same [[nvidia-newton-physics-engine-developer-page|developer page]] flags "Linux Foundation governance gives vendor-neutral oversight despite heavy NVIDIA contribution." This matters because:

1. **DeepMind protection.** DeepMind would not invest its researchers' time in shipping MJX → Newton interop if Newton were a single-vendor project NVIDIA could license-flip. Linux Foundation governance creates a credible commitment that the substrate stays open.
2. **Disney's seat.** [[disney-research|Disney Research]]'s involvement is the puzzle piece — Disney isn't a robotics vendor in the GR00T / Optimus / Pi sense. Its stake is presumably entertainment-grade physics for character animation and theme-park robotics; co-developer status keeps Newton's contact and soft-body models fit for high-fidelity entertainment use, not just industrial manipulation. The cross-pressure widens what Newton has to handle correctly.
3. **Reduced single-vendor moat.** A roboticist betting on Newton today has structural insurance that no one company can pull the rug.

## Why OpenUSD is the other half

Newton handles dynamics; OpenUSD (the Universal Scene Description format originated by Pixar) handles geometry, scene composition, and asset interchange. Both NVIDIA's Omniverse / Isaac Sim line and DeepMind's MJX-based stack now consume OpenUSD as a scene format. **Same scene, same physics, different training framework** is the new shape.

URDF and MJCF are not going away — they are still the dominant robot-description formats today — but for the multi-asset, multi-robot, scene-composition problems that VLA training demands, OpenUSD is the format both stacks are converging on.

## Implications for policy researchers and tool builders

- **Cross-stack policy mobility is on the table.** A research group training in Isaac Lab can plausibly evaluate against MuJoCo Playground (or vice versa) without re-authoring physics or scenes. This was not possible across competing stacks before 2026.
- **Vendor-neutral substrate, vendor-specific framework.** The interesting ML differentiation moves *up the stack* — to environment APIs, learning frameworks ([[nvidia-isaac-lab|Isaac Lab]] vs Playground vs ManiSkill), and model libraries ([[nvidia-groot|GR00T]], [[vla-models|VLAs]]). The physics layer becomes commoditized infrastructure, like LLVM for compilers or Linux for OSes.
- **The lock-in moves to assets and tooling.** Whichever stack has better robot models, better scene libraries, and better RL infrastructure wins — but the floor (physics + scene format) is shared.
- **Genesis and other custom-physics simulators are now exceptions.** [[genesis|Genesis]] uses its own Python-first custom physics; [[maniskill|ManiSkill]] sits on [[sapien|SAPIEN]]. Both can still win on domain-specific advantages (Genesis's claimed 10–80× speedup, SAPIEN's manipulation-realism), but they now have to justify the *non-Newton* choice.

## What is still uncertain

> [!warning] Real cross-stack adoption is not yet demonstrated in the wiki
> Both source pages assert pluggability. Neither shows a worked example of a single policy / scene running unchanged across Isaac Lab and MuJoCo Playground via Newton. The architectural promise is in the docs; the empirical demonstration is not yet ingested here.

- **Throughput parity?** No source compares Newton's throughput against MJX or [[genesis|Genesis]] on the same task. The [[mujoco-playground-paper|MuJoCo Playground Paper]]'s own open question is whether Playground throughput matches Isaac Lab on identical tasks; with Newton as a shared backend, that question becomes empirically tractable but isn't answered.
- **Will MuJoCo Playground actually default to Newton?** "Optionally backends" is not "primarily backends." MJX continues; Newton is one option. If the JAX ecosystem advantages of MJX outweigh the cross-stack advantages of Newton, DeepMind may keep MJX as the default and Newton as a compatibility layer.
- **Disney's actual contribution depth?** [[disney-research|The Disney Research entity page]] is a stub. The relationship is real (the developer page lists Disney as a co-developer) but the specific technical contributions Disney makes to Newton are not yet documented in the wiki.
- **Closed engines still ship policies in production.** Tesla Optimus, Pi π0, Skild, and other closed teams use undisclosed in-house simulators. The Newton / OpenUSD convergence is in the *open* research stack; closed industry stacks are not visibly affected.
- **GR00T version drift.** Sources reference both GR00T N1.6 GA ([[nvidia-newton-contact-rich-manipulation-blog|NVIDIA Newton Contact-Rich Manipulation Blog]]) and N1.7 Early Access ([[top-10-physical-ai-models-2026|Top 10 Physical AI Models 2026]]) as the current Newton/Isaac Lab-bundled VLA. This is the same standing inconsistency tracked in the simulator survey; not Newton-specific but worth noting whenever Newton is described in context.

## Sources used in this synthesis

- [[nvidia-newton-physics-engine-developer-page|NVIDIA Newton Physics Engine Developer Page]]
- [[nvidia-newton-contact-rich-manipulation-blog|NVIDIA Newton Contact-Rich Manipulation Blog]]
- [[mujoco-playground-paper|MuJoCo Playground Paper]]

## Related

- [[newton-physics-engine|Newton physics engine]] — entity page.
- [[nvidia-isaac-lab|NVIDIA Isaac Lab]] / [[mujoco-playground|MuJoCo Playground]] — the two stacks converging on Newton.
- [[simulators-for-agentic-robotics-2026|Simulators for agentic robotics — 2026 landscape]] — surveys the broader simulator field; this page zooms into one structural insight from it.
