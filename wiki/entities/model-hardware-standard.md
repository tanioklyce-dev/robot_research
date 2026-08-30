---
title: Model Hardware Standard (MHS)
type: entity
subtype: standard
created: 2026-08-30
updated: 2026-08-30
sources: 1
tags: [mhs, anthropic, standard, device-drivers, hardware-abstraction, mcp, lab-automation, agentic-robotics]
---

**Model Hardware Standard (MHS)** — [Anthropic](anthropic.md)'s specification for letting AI agents discover and operate physical instruments through one standardized driver interface, announced as a waitlisted **research preview on 2026-08-27** ([Previewing the Model Hardware Standard](../sources/anthropic-model-hardware-standard-preview.md)). Model-agnostic; reachable over standard protocols including [MCP](../concepts/agents/llm-agent-architecture.md#mcp--model-context-protocol). **Not yet open source.**

If MCP is "one interface between a model and software services," MHS is the same move for **devices**: instruments become discoverable, self-describing endpoints instead of a per-vendor integration project. See [agent–hardware abstraction](../concepts/agents/agent-hardware-abstraction.md) for the pattern and the other stacks converging on it.

## Origin

A collaboration between **Alek Kemeny** (Anthropic, Beneficial Deployments team) and **Arco Bast**, a postdoctoral scientist at [HHMI Janelia](hhmi-janelia.md). Bast ran deep two-photon brain imaging on a rig of lasers, motorized focusers and multi-vendor cameras with no common interface, and built **a shared-memory dictionary holding the whole rig's state** so the instruments could communicate at memory speed. Kemeny and Bast integrated AI models into that interface; **Bast's microscope was the first rig to run on MHS**.

## Architecture

- **Standardized driver** over a minimal primitive set — `read` (e.g. "get temperature") and `write` (e.g. "set temperature") — that any programmable device can implement, plus **discovery in a standard format** so devices and agents find each other across networks with no bespoke translator.
- **Natural-language tags.** The driver carries prose fields for what code cannot express — the weight of a robot arm, say — written by the user or by an agent that interviews them about the rig. MHS compiles these into a **device reference file**: what it can measure, what can be adjusted, **and what safety limits will be enforced**. The explicit target is knowledge that today lives in paper manuals or as tacit expertise.
- **States and procedures.** Each instrument is normalized into a manifest of states (conditions it can be in) and procedures (operations it can perform), so the model sees one interface regardless of what runs underneath — at CMU that was a directory-watcher job scheduler, a Windows ActiveX/COM script interface, and a plate reader with **no API at all, driven through its GUI**.
- **Three control surfaces** — MCP, a CLI, and code files (APIs) — enabling multi-device orchestration from a single line of code.
- **Shared state dictionary in shared memory** — Janelia's original contribution; any attached process, in any language, reads the same documented structure. This is what makes analysis and visualization code reusable *per data type* rather than *per device*.

## What it is claimed to buy

Integration cost that **stops scaling with device count**. Reported reductions: CMU **weeks → 8 hours** for a four-instrument workcell across three computers; UW **6 instruments in under a week**, drivers included; Janelia **multi-day → a few minutes** to add a camera, and 7 sequenced program launches → **one dashboard click**.

Downstream of that: unattended overnight operation, cross-device error recovery (a camera sees bubbles, the network is queried for a centrifuge that can fix them), and **hardware-independent protocols** — "spin at 15,000 × rpm" resolved at runtime to whatever compatible machine is on the network, with the parameter conversion done by the model.

## The pattern worth naming: explore, then compile

Anthropic's own description of Claude on a laser — adjust, observe through a camera, repeat, then **"package what it learned into code files, writing a deterministic script"** so the whole alignment runs as one command. [QuEra](quera-computing.md)'s relock controller is the same shape at production scale: an overnight agent loop whose deliverable is **an agent-free, fully inspectable script**. [Genentech](genentech.md)'s bubble lesson became a reusable liquid-handling [skill](../concepts/agents/agent-skills.md).

This is [code as policy](../concepts/agents/code-as-policy.md), and it is also MHS's answer to the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md): the agent reasons at exploration speed and then removes itself from the fast loop.

## Safety properties

- Safety limits are **generated into the device reference file** from the driver, not asserted in a prompt. Janelia relies on this for laser power (an over-power command would bleach the sample).
- CMU **induced six fault conditions** — missing plate, rotated plate, reader busy, disconnected camera, unreachable device, active e-stop — and **all six were blocked before any device moved**. This is the wiki's first ingested example of an [execution rail](../syntheses/agents/guardrails-for-robot-agents.md) that checks **world state**, not just tool names.
- Anthropic reports a **physical safety roadmap** in development, safety evaluations to be built with preview partners, and a commitment to publish preview findings as deployment guidance at open-source time.
- Observed failure mode was **over-caution**: QuEra's experiments sometimes paused overnight while Claude waited for approval on actions it judged slightly risky.

## Limitations (as stated)

- **Requires a programmable interface.** Devices without one are out of scope; Anthropic is working with those manufacturers.
- **Physical and spatial reasoning remains the binding constraint on the model, not the bus.** Genentech had to teach Claude that a bubble error was physical rather than a software fault; QuEra reports Claude's understanding of the rig was "programmatic rather than physical" and it could not troubleshoot hardware.
- Heavy context engineering still required (QuEra: "a ton of context").
- Closed preview; no published open-source date or governance model.

## Ecosystem

Vendors building support: **Amazon Web Services** (Strands Robots), **Automata** (LINQ), **Danaher**, **Doosan Robotics**, **MBF Bioscience** (a driver for **ScanImage**, used in hundreds of neuroscience labs), **QIAGEN** (QIAsymphony Connect), **Tecan** (Fluent), **Universal Robots**, **[Hugging Face](hugging-face.md)** (in **[LeRobot](lerobot.md)**), and **Raspberry Pi** (following tests of a Camera MHS Driver).

Early users: [Genentech](genentech.md), [HHMI Janelia](hhmi-janelia.md), UW Baker/Pinglay labs, Carnegie Mellon, [QuEra Computing](quera-computing.md), [Tetsuwan Scientific](tetsuwan-scientific.md).

## Open questions

- **Relationship to [ROS 2](ros2.md) is unaddressed** — MHS's primitives, discovery and typed manifest overlap substantially with what a ROS 2 interface already provides, and the wiki already holds two independent ROS↔MCP bridges ([ros2-mcp-server](ros2-mcp-server.md), [AgenticROS](agenticros.md)). Wrap, replace, or ignore is unstated.
- **Enforcement location** for safety limits — driver process, firmware, or call-site policy — is not described.
- **Prompt-injection surface**: the natural-language tags are untrusted prose that is compiled into the file the agent trusts to operate hardware. Not discussed in the announcement.
- No reliability number is published **for MHS itself** — only for workflows built on it.

## Related

- [Agent–hardware abstraction](../concepts/agents/agent-hardware-abstraction.md) — the concept page; MHS alongside MCP, ROS↔MCP bridges, Strands Robots, AgenticROS manifests.
- [Laboratory automation and self-driving labs](../concepts/robotics/laboratory-automation.md) — the domain the preview is aimed at.
- [Anthropic](anthropic.md) — and specifically the [Frontier Red Team](frontier-red-team.md)'s [Project Fetch](../sources/anthropic-project-fetch-robot-dog.md), whose largest measured uplift gap was *connecting to unfamiliar hardware and reading its sensors*. MHS is the infrastructure answer to the gap that study identified.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — MHS is a device-side member of the protocol layer with MCP and A2A.

## Mentioned in

- [Previewing the Model Hardware Standard](../sources/anthropic-model-hardware-standard-preview.md)
