---
title: Tetsuwan Scientific
type: entity
subtype: company
created: 2026-08-30
updated: 2026-08-30
sources: 1
tags: [tetsuwan, researchos, lab-automation, self-driving-lab, mhs, qpcr, compiler]
---

**Tetsuwan Scientific** — building an **automated biology lab available to researchers and agents via an API**, on top of its own automation platform **ResearchOS**. An [MHS](model-hardware-standard.md) preview partner ([Previewing the Model Hardware Standard](../sources/anthropic-model-hardware-standard-preview.md)).

## The thesis

Labs have had pipetting, sealing, shaking and labware-moving machines since the 1960s, yet most biology is still done by hand — because biology experiments are **dynamic**: sample count, plate format, condition count, dilution depth, incubation times and timepoints all change between runs. Translating one configuration into an automated workflow takes an automation engineer **weeks or months**, so automation only pays off at high-throughput-screening scale. Everything else stays manual, with the error and reproducibility cost that implies.

## ResearchOS + MHS

- **ResearchOS** turns natural-language protocols into a script in Tetsuwan's experiment syntax (with Claude's help), which a **custom compiler** lowers into automation code.
- **MHS is the layer beneath** — the orchestration bus over a heterogeneous fleet of pipetting robots, arms and automated labware "that all use different languages and all have their quirks."
- **Hardware-independent protocols.** A protocol says "spin down at 15,000 × rpm for five minutes" without naming a centrifuge; ResearchOS queries the network via MHS for a compatible machine, learns its driver interface, and has Claude convert the specified force into that machine's parameters (dividing by rotor radius, for one that only accepts rotor speed). The protocol author never learns which machine ran.
- **Cross-device error recovery.** A camera watching each transfer feeds a computer-vision check for bubbles and foam. In one run the camera found bubbles in master mix held by a robotic arm — which the arm alone could not fix — so ResearchOS **scanned the network for MHS devices that could**, and Claude proposed (over Slack) a brief low-speed centrifuge spin, then issued the commands. This is the wiki's cleanest example of **recovery by discovery** rather than by pre-programmed exception handling.

## Compiler improvement as a closed-loop experiment

Claude used MHS to run an optimization on Tetsuwan's own compiler heuristics: compile a qPCR protocol into realistic worklists, enumerate the transfer types the compiler can emit, run them on a robot under varying conditions, measure accuracy and precision with a tracer dye, then pull the plate-reader data back through MHS, analyze it, and propose tweaks to the transfer-precision model.

- **9,143 dispenses**, **300 unique transfer types** (liquid × tip × volume × dispense count × over-aspiration), **1,508 measured conditions**, four liquid types.
- On held-out experiments the refined model predicted multi-dispense precision **~12% more accurately than the manufacturer's technical specification**, winning **31 of 45 runs** (sign-test p ≈ 0.001); **~17%** on the most-replicated data.

> [!note] Worth noticing
> This is a lab-automation company using an agent to beat **its instrument vendor's own published spec** on that instrument's behavior, and folding the result into a compiler's cost model — the automation equivalent of learning a better actuator model than the datasheet gives. Compare [actuator fidelity in sim-to-real](../concepts/learning/actuator-fidelity-sim2real.md).

## Application: San Pedro Creek

A citizen-science qPCR project in Pacifica, California, characterizing fecal contamination sources. Human-associated *Bacteroides* markers (**HF183**, **BacH**) amplified clearly; no other host-specific markers were detectable, corroborating the San Pedro Creek Watershed Coalition's finding that humans are the primary contributor. Presented as preliminary.

## Related

- [Model Hardware Standard](model-hardware-standard.md)
- [Laboratory automation and self-driving labs](../concepts/robotics/laboratory-automation.md)
- [Code as policy](../concepts/agents/code-as-policy.md) — ResearchOS is a compiler-backed variant: language in, machine code out.

## Mentioned in

- [Previewing the Model Hardware Standard](../sources/anthropic-model-hardware-standard-preview.md)
