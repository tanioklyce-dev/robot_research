---
title: "Previewing the Model Hardware Standard"
type: source
url: https://www.anthropic.com/news/model-hardware-standard-research-preview
author: Anthropic (Beneficial Deployments) with Genentech, UW Baker/Pinglay labs, Carnegie Mellon, HHMI Janelia, QuEra Computing, Tetsuwan Scientific
published: 2026-08-27
ingested: 2026-08-30
venue: anthropic.com — Announcements / Beneficial Deployments
format: web article (product announcement + six partner case studies)
tags: [anthropic, claude, mhs, model-hardware-standard, mcp, lab-automation, self-driving-lab, device-drivers, agentic-robotics, hardware-abstraction, quantum-computing, microscopy, liquid-handling, safety, lerobot]
---

## Summary

Anthropic announced a **research preview of the Model Hardware Standard (MHS)** — a shared specification that lets AI agents discover and operate physical instruments through one standardized driver interface instead of per-vendor glue code. MHS began as a collaboration between **Alek Kemeny** (Anthropic Beneficial Deployments) and **Arco Bast**, a postdoc at [HHMI Janelia](../entities/hhmi-janelia.md) who had put an entire microscope rig's state into a shared-memory dictionary so his instruments could talk at memory speed. The claim is bluntly quantitative: integration work that takes **weeks to months** drops to **hours or minutes**, and once devices are on the bus an agent can run experiments unattended overnight. Six partners report early results — [Genentech](../entities/genentech.md), the UW Baker/Pinglay labs, Carnegie Mellon, Janelia, [QuEra Computing](../entities/quera-computing.md), and [Tetsuwan Scientific](../entities/tetsuwan-scientific.md) — plus eight hardware vendors building MHS support. It is **not open source yet**; access is by waitlist, and Anthropic says it wants to build safety evaluations with launch partners first.

For this wiki the announcement matters less as lab-automation news than as **the integration layer every LLM-agent robot stack in here assumes already exists**. [Project Fetch](anthropic-project-fetch-robot-dog.md) measured the largest human-vs-Claude uplift gap precisely at *connecting to unfamiliar hardware and reading its sensors*; MHS is Anthropic building that gap shut as infrastructure. See [agent–hardware abstraction](../concepts/agents/agent-hardware-abstraction.md).

## What MHS actually is

Four mechanisms, per the announcement:

1. **A standardized driver** exposing a small primitive set — `read` ("get temperature") and `write` ("set temperature") — that any programmable device can implement, plus **network discovery in a standard format** so agents and devices find each other without a bespoke translator in between.
2. **Natural-language tags in the driver.** The driver carries fields the user (or an agent interviewing the user about their rig) fills in prose — the things not discernible from code, e.g. *the weight of a robot arm*, which matters for manipulating it safely. From these, MHS **auto-generates a reference file**: what the device can measure, what can be adjusted, and **what safety limits will be enforced**. Anthropic's framing: this information "has been stored in paper manuals, on a user's computer, or as tacit knowledge."
3. **Three control surfaces** — [MCP](../concepts/agents/llm-agent-architecture.md#mcp--model-context-protocol), a CLI, and code files (APIs) — which together allow orchestration across multiple devices from a single line of code. MHS is **model-agnostic**; any harness can reach it over standard protocols.
4. **A shared state dictionary in shared memory** (Janelia's contribution) — every device's variables, controls and sensor values in one documented, cross-language structure that any attached process can read.

Each instrument is normalized into a manifest of **states** (conditions the system can be in) and **procedures** (operations it can perform), so a model works from one interface regardless of what is underneath.

## Key claims

### The integration-cost claim, measured four ways

| Partner | Before | With MHS |
|---|---|---|
| **CMU** — liquid handler + plate reader + arm + cameras across 3 computers | "multiple weeks" for a vendor-built setup | **8 hours**, raw equipment → completed dilution curve including one autonomous rerun |
| **UW (Zihao Song)** — 6 instruments | earlier automation attempts: weeks evaluating platforms, chasing vendor support, writing glue code, "finally giving up" | **under a week**, including writing the drivers |
| **Janelia (Virginie Ruetten)** — adding a beam camera to a 7-program microscope rig | "a multi-day project" | **a few minutes**; experiment start goes from 7 programs launched in a fixed order to one dashboard click |
| **Genentech** — BCA assay across liquid handler, arm, plate reader | setup "weeks or even months" | (no integration time given; reports the assay ran) |

Ruetten states the underlying property directly: **"the cost of hardware integration stops scaling with the number of devices."**

### QuEra: the strongest result in the piece

QuEra builds neutral-atom quantum computers whose titanium-sapphire lasers must hold frequency to ~1 part in 10¹². When a laser loses "lock," a human expert takes **5–10 minutes** to recover it; at 2 a.m. in a university lab, someone drives in.

- **The prior art was already automated.** A team of four (laser engineer, software engineer, algorithms specialist, tester) spent **several months** on a bespoke relock script: **58% success, ~150 s per attempt**. It reproduced the human procedure step for step, and inherited its flaw — a linear sequence cannot absorb a disturbance that undoes an already-completed step, so it restarts.
- **The agent loop.** Four roles, each a fresh Claude instance: propose a hypothesis → write it into the script → run against the **live laser** and log every step → read the logbook and decide what to change. Hundreds of unattended passes overnight. By morning: **~6 s, 96%** (development run).
- **Blind test: 700 trials, 695 recoveries — 99.3%.** Hardest disturbances 10–14 s; simple ones 0.9–5.4 s. Setup time for the whole exercise fell from "a day or two" the first time to "a few hours."
- **What changed structurally:** Claude rewrote the linear sequence as a **decision tree** — read the instruments, build if-then conditions from what they show, touch only the one or two controls the observed disturbance implicates. A human must check every control to be sure; Claude found the shortcut by running disturbances repeatedly until the pattern was clear.
- **The end product is a deterministic, fully inspectable script that runs in production with no agent in the loop.**
- **PID tuning, a second and different result.** 12 interdependent servo parameters. A specialist tunes against the RMS error the servo reports, because capturing an oscilloscope trace and running an FFT after every change is impractical for a human. Claude did exactly that — hundreds of times over a night. **15.7 mV (the specialist's standing tune) → 1.55 mV over 363 experiments and 16 unattended hours.** Independent check on a phase-noise analyzer against a fresh blind retune by the same specialist: the two matched across the band **except at a ~220 kHz resonance, where the manual tune left roughly 1000× more noise** — the exact failure mode of the RMS heuristic. Over a 19-hour run, Claude's PIDs **never lost lock**; the expert's unlocked **~1.6 times an hour**. This workflow keeps the agent in the loop; the relock controller does not.

### CMU: autonomous rerun, and safety interlocks that were actually tested

- Stack: Analytik Jena CyBio FeliX liquid handler, Thermo Varioskan LUX plate reader, Thermo Spinnaker arm, monitoring cameras — across **three computers with fundamentally incompatible interfaces**: a directory-watcher scheduler (drop an XML job file, get two files back), a Windows **ActiveX/COM** scripting interface with no modern SDK, and a plate reader with **no programmatic interface at all, only a GUI** that MHS drives the way a person would.
- Driver-writing was itself partly agentic: methods for the COM interface were worked out "from vendor documentation or from a **Claude Opus 4.8** agent exploring the interface to write a functional driver."
- **Six fault conditions were artificially induced** — missing plate, rotated plate, reader busy, disconnected camera, unreachable device, active emergency stop. **The system blocked all six before any device moved.**
- **Autonomous experimental judgment:** the agent ran a serial dilution to 200 µg/mL, judged the fit unusable (**R² < 0.9**, from saturation at the top of the range), discarded the plate, and reran at **100 µg/mL** — **R² > 0.98**, with no human input at any point. Roughly **3× faster** than the prior workflow. Drivers will be released publicly.

### Genentech: where the model's physical reasoning ran out

- Task: the **BCA protein assay**, across a liquid handler, a robotic arm and a plate reader, in 96-well plates, with Claude as orchestrator.
- Given the standard protocol, Claude executed the steps but chose **one generic flow rate for both aqueous and viscous liquids**, foaming the BSA and ruining transfer accuracy. Asked to optimize against an expert's ground-truth transfer in the same plate (minimizing RMSE), it converged on **~140 µL/s for water (0.016 RMSE)** and **10 µL/s for BSA (0.181 RMSE)** — parameters their automation experts confirmed were reasonable.
- It **recovered on its own from tip-pickup and fluid-detection errors**, which Genentech notes current instruments mostly cannot do.
- **The failure is the interesting part.** On bubble-induced runtime errors, Claude's default was to *retry in the same well with different parameters*, which agitated the fluid and made more bubbles. It had to be told that the error code meant **physical** bubbles, and that the fix was a clean well and fewer mixing cycles. Once told, it held that context for the rest of the run, and the lesson was codified into reusable **liquid-handling [skills](../concepts/agents/agent-skills.md)**.

> [!note] The named limitation
> Anthropic's own framing: *"As a large language model, Claude learns about the physical world through text and images, meaning its spatial and physical reasoning have limitations that still require expert oversight."* QuEra reports the same shape — "if something went wrong with the physical hardware, Claude didn't know how to troubleshoot, as its understanding of the rig was **programmatic rather than physical**."

### UW Baker/Pinglay labs: the academic-budget case

- Economics that motivate the work: designing a protein like PETase can cost **~$0.01**; testing one candidate at the bench costs **~$100 and a week of labor**, against 1,000 candidates per round.
- Three demos: a **remote dashboard** for all instruments; an **agent-supervised qPCR** that watches the amplification curve, asks whether to stop before the plateau distorts the library, and on "stop" halts and advances the instrument to a 4 °C hold; and a **plate handoff between a liquid handler and an open-source [LeRobot](../entities/lerobot.md)-based robotic arm** instrumented with MHS. Claude Code triggered the arm ~10 s after the dispense-complete signal; across repeated tests the two instruments **never collided**.
- The honest caveats are the author's own: these are proofs of concept, complex protocols will need significant optimization, and **running an agent continuously over long monitoring windows has compute costs that must be weighed against researcher time saved**.
- Figure 1 of that section frames the argument the whole announcement rests on — traditional academic lab (flexible, labor-intensive, AI limited to human–AI exchange) vs automated lab (scheduled, near-autonomous, expensive and inflexible) vs **MHS lab (scheduled *and* flexible, AI-native so agents participate in the experiment)**.

### Tetsuwan Scientific: MHS under an existing automation platform

- Tetsuwan's **ResearchOS** compiles natural-language protocols into automation code via a custom compiler; MHS sits underneath as the orchestration layer over a heterogeneous fleet.
- **Hardware-independent protocols**: a protocol says "spin at 15,000 × rpm for five minutes"; ResearchOS queries the network via MHS for a compatible centrifuge, learns its driver interface, and has Claude convert the specified force into whatever that machine accepts (dividing by rotor radius, for a machine that only takes rotor speed). The protocol author never learns which centrifuge ran.
- **Cross-device error recovery**: a camera detected bubbles in master mix held by a robotic arm; the arm alone could do nothing, so ResearchOS **scanned the network for MHS devices that could help**, and Claude proposed (over Slack) moving the tube to a centrifuge for a brief low-speed spin — then issued the commands.
- **Compiler improvement via closed-loop experiment**: 9,143 dispenses, 300 unique transfer types, 1,508 measured conditions, four liquid types. The refined precision model beat **the manufacturer's own technical specification by ~12%** on held-out experiments (31 of 45 runs, sign-test p ≈ 0.001), ~17% on the most-replicated data.
- Application: qPCR profiling of fecal contamination in **San Pedro Creek**, Pacifica CA, corroborating the watershed coalition's finding that humans are the primary contributor (HF183/BacH human markers detected; no other host-specific markers).

### Janelia: agentic microscopy

- Ruetten's rig — femtosecond lasers, galvo mirrors, photomultipliers, two translation stages — spans **MATLAB, Python and C#** with no shared interface, and previously required **launching seven programs in a fixed order**, where a wrong order could cost the session.
- With one shared state dictionary, **analysis and visualization code is written once per data type rather than once per device**; she built a modular online-analysis framework (slot → reusable transforms → slot or disk) and reused a spectral transform written for camera-derived heart activity on neural activity from a different device in a different language.
- **Agentic acquisition**: a deterministic acquisition↔analysis loop with the agent entering at decision points (what region to image, what analysis to run). Because **MHS enforces device-level safety limits**, she does not have to worry about the agent using excess laser power and bleaching the sample. Result so far: **it found an oscillatory cell population a fixed setting would have missed**, meaning fewer repeat runs and fewer animals per usable recording.
- Two other Janelia projects: **Arco Bast** (Spruston lab) — deep two-photon imaging of dendrites in navigating mice; **his rig was the first to run on MHS**, and Claude aligns beams, tunes optics and checks itself against the sensors, turning a half-day of manual setup into one step. **Magdalena Schneider and Hari Shroff** — agentic control of a light-sheet microscope, Claude deciding in real time how to image developing *C. elegans* embryos and how to trade off competing imaging parameters.

### The exploratory→deterministic pattern, stated by Anthropic

> "we observed Claude make an adjustment to a laser, observe the results through a camera to assess how its adjustment moved the laser beam, and repeat the process… Claude then packaged what it learned into code files, writing a deterministic script that let it align the laser without having to reason at each step, so the whole process could run as a single command."

The same shape appears in QuEra's relock controller (an agent loop whose deliverable is an agent-free script) and in Genentech's codified liquid-handling skills. See [code as policy](../concepts/agents/code-as-policy.md) — this is *explore online, compile to a deterministic artifact*, which is also the answer MHS gives to the [control-rate](../syntheses/platforms/control-rate-ladder.md) problem: "when the agent needs to execute long-running tasks or operate devices faster than its online reasoning would allow, it can chain together driver commands… in code files."

## Vendors and adopters

Building MHS support into their equipment or platforms:

- **Amazon Web Services** — via **Strands Robots**, its library for connecting AI agents to physical devices; a private pre-release package is provided to preview participants.
- **Automata** — MHS in **LINQ**, for intelligent error handling in autonomous labs.
- **Danaher** — exploring MHS for smart instruments and autonomous labs.
- **Doosan Robotics** — testing MHS with robotic arms, incl. automated QA and multi-robot task coordination.
- **MBF Bioscience** — an MHS driver for **ScanImage**, the software running laser-scanning microscopes in hundreds of neuroscience labs.
- **QIAGEN** — proof-of-concept on **QIAsymphony Connect** nucleic-acid purification: agents helping troubleshoot, guiding operators through recovery, improving uptime.
- **Tecan** — MHS support for **Fluent** liquid handlers.
- **Universal Robots** — early access; plans support in its robotics platform.
- **[Hugging Face](../entities/hugging-face.md)** — adding MHS support **in [LeRobot](../entities/lerobot.md)**.
- **[Raspberry Pi](../entities/raspberry-pi-5.md)** — enabling MHS across a number of products after successful tests with their **Camera MHS Driver**.

## Safety posture

- MHS **auto-generates the enforced safety limits** into the device reference file, so limits are a property of the driver rather than of the prompt. Janelia's laser-power case and CMU's six blocked fault conditions are the two concrete demonstrations.
- CMU plans more checks, responsiveness monitoring, and **protocols for when human approval is required for high-risk decisions**.
- QuEra observed the opposite failure mode from the one usually feared: **Claude stopped to wait for human confirmation before anything it deemed slightly risky, so experiments sometimes paused overnight waiting for approval.** Their comment — "an overly cautious agent is preferable to one that is not cautious enough."
- Anthropic says it is **developing a physical safety roadmap** to extend its safeguards policy and enforcement against misuse of AI in the physical world, will build additional safety evaluations with launch partners during the preview, and will publish preview findings as deployment guidance when MHS is open-sourced.

## Stated limitations

- Physical/spatial reasoning is weak; expert oversight still required (Genentech bubbles, QuEra hardware troubleshooting).
- **MHS does not work with hardware that has no programming interface** — Anthropic is working with those manufacturers to add drivers. (CMU's GUI-only plate reader shows the current workaround: drive the GUI, with nothing to check against but the screen.)
- QuEra: the team "needed to provide a ton of context to Claude about what they wanted from the experiment and how Claude should carry it out."
- Not open source; waitlisted research preview.

## Entities mentioned

- [Anthropic](../entities/anthropic.md) — author; Beneficial Deployments team
- [Model Hardware Standard](../entities/model-hardware-standard.md) — the standard itself
- [HHMI Janelia Research Campus](../entities/hhmi-janelia.md) — co-origin; three MHS projects
- [Genentech](../entities/genentech.md), [QuEra Computing](../entities/quera-computing.md), [Tetsuwan Scientific](../entities/tetsuwan-scientific.md)
- [Hugging Face](../entities/hugging-face.md) / [LeRobot](../entities/lerobot.md) — MHS support planned; the UW arm is a LeRobot-based open-source arm
- [Raspberry Pi 5](../entities/raspberry-pi-5.md) — Raspberry Pi's Camera MHS Driver
- Not yet given pages: AWS (Strands Robots), Automata, Danaher, Doosan Robotics, MBF Bioscience, QIAGEN, Tecan, Universal Robots, Carnegie Mellon (Kangas/Kingsford labs), UW Baker & Pinglay labs

## Concepts touched

- [Agent–hardware abstraction](../concepts/agents/agent-hardware-abstraction.md) — the interface-standard layer MHS instantiates
- [Laboratory automation and self-driving labs](../concepts/robotics/laboratory-automation.md)
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — MCP as one of three control surfaces
- [Code as policy](../concepts/agents/code-as-policy.md) — explore online, compile to a deterministic script
- [Agent skills](../concepts/agents/agent-skills.md) — Genentech's codified liquid-handling skills
- [AI guardrails](../concepts/safety/ai-guardrails.md) / [Guardrails for robot agents](../syntheses/agents/guardrails-for-robot-agents.md) — a shipped execution rail with world-state preconditions
- [Runtime failure detection](../concepts/robotics/runtime-failure-detection.md) — camera-based pipetting-error detection; autonomous recovery
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md), [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) — why the agent compiles itself out of the fast loop
- [AI uplift studies](../concepts/safety/ai-uplift.md) — [Project Fetch](anthropic-project-fetch-robot-dog.md)'s measured gap was hardware integration; MHS is the infrastructure answer

## Open questions

- **Is MHS a competitor to, or a layer under, [ROS 2](../entities/ros2.md)?** The announcement never mentions ROS. Its `read`/`write` primitives plus network discovery plus a typed states/procedures manifest describe much of what a ROS 2 interface already provides — and the wiki already has two ROS↔MCP bridges ([ros2-mcp-server](../entities/ros2-mcp-server.md), [AgenticROS](../entities/agenticros.md)) that arrived at capability manifests independently. Whether MHS drivers wrap ROS nodes, replace them, or ignore that world is unstated.
- **What is the actual safety-limit mechanism?** "Safety limits will be enforced" is asserted; whether enforcement lives in the driver process, the device firmware, or a policy check on the call is not described. CMU's six blocked conditions are the only evidence, and they are preconditions on device state, not on semantic intent — nothing here addresses `pick(knife)`-class problems.
- **Do the natural-language tags create a prompt-injection surface?** Device metadata written in prose by users (or by an agent interviewing users) is untrusted text that lands in the planner's context and is auto-compiled into the reference file the agent trusts to operate hardware. Not discussed.
- **Nobody reports a failure rate for MHS itself** — only for the workflows on top of it. The 99.3% is a relock controller's number, not the bus's.
- **The compute cost is raised once and never quantified** (UW). An agent supervising a 19-hour run is a different economic object from an overnight optimization that terminates in a script.
- **How much of the QuEra result is MHS versus the four-role agent loop?** The loop is a general recipe (cf. [ASPIRE](aspire-paper.md), [Karpathy's autoresearch](karpathy-autoresearch.md)); MHS supplied the instrument access. The counterfactual — same loop, bespoke API — is not run.
- **Open-source date and governance are unannounced**, as is whether the specification will be vendor-neutral in the way MCP became.
