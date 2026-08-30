---
title: Genentech
type: entity
subtype: company
created: 2026-08-30
updated: 2026-08-30
sources: 1
tags: [genentech, biotech, drug-discovery, lab-automation, mhs, liquid-handling]
---

**Genentech** — biotechnology company (Roche group), founded on the recombinant-DNA work that produced somatostatin in *E. coli* in 1977 and recombinant human insulin, FDA-approved in 1982 as the first genetically engineered therapeutic. In this wiki it appears as an [MHS](model-hardware-standard.md) preview partner, and as the source of the **clearest documented account of where a frontier model's physical reasoning runs out** ([Previewing the Model Hardware Standard](../sources/anthropic-model-hardware-standard-preview.md)).

## MHS proof-of-concept: the BCA protein assay

Three instruments — a **liquid handler**, a **robotic arm**, and a **microplate reader** — with Claude orchestrating over MHS and acting as the communication hub, in standard 96-well plates. Their stated bottleneck: setting up such automated systems is manual and takes **weeks or months**, capping how many scientific ideas get tested.

**Autonomous parameter optimization.** Given the standard protocol as a baseline, Claude ran the steps but chose **one generic flow rate for both aqueous and viscous liquids**, foaming the BSA and corrupting transfers. Asked to optimize against an expert's ground-truth transfer performed in the same plate — minimizing RMSE, measured by dyed-liquid trials read on the plate reader — it converged on:

- **water ≈ 140 µL/s** (0.016 RMSE)
- **viscous BSA ≈ 10 µL/s** (0.181 RMSE)

Genentech's automation experts confirmed both as reasonable for that setup. Ordinarily this optimization requires a specialist to write custom programming logic for every parameter set.

**Error recovery.** Claude recovered on its own from tip-pickup failures and fluid-detection errors — "a capability that current scientific instruments mostly lack."

## The failure that is worth more than the success

On runtime errors caused by bubbles during mixing, Claude's default was to **retry in the same well with different parameters**, which agitated the fluid and produced more bubbles. It did not know the failure was physical. Once told the error code meant real bubbles, and that the fix was a **clean well plus fewer mixing cycles**, it held that context for the rest of the run — and the lesson was codified into reusable liquid-handling [skills](../concepts/agents/agent-skills.md) that let it pick sensible defaults by liquid type.

Bubbles are a good illustration of why this is not a software bug class: aspirating 40 µL of a foamy reagent transfers less than 40 µL of liquid, liquid-level sensors throw hardware errors on foam, and bubbles distort the optical readout that *is* the experiment.

> [!note] Why this belongs in a robotics wiki
> This is the same deficit that shows up in [Project Fetch](../sources/anthropic-project-fetch-robot-dog.md) (Claude could not close the loop on ball retrieval) and in [How Claude Performs on Robotics Tasks](../sources/anthropic-how-claude-performs-on-robotics-tasks.md) (an LLM supervising a trained policy does *worse* in-distribution). A model whose world knowledge is textual mis-attributes physical failures to the software layer it can see. See [spatial intelligence](../concepts/world-models/spatial-intelligence.md).

## Stated direction

End-to-end autonomous workflows in drug discovery labs: scientists set high-level biological intent; agents generate hardware instructions, execute, run closed-loop analysis, and deliver screening data. Requires MHS on centrifuges, incubators, analytical instruments and sensors; a harness tuned for live, sensitive cells; and custom models doing round-the-clock adaptive optimization.

Contributors named: Anupriya Tripathi, Matthew Bucci, Justin Nicola, Corinne Gullekson.

## Related

- [Model Hardware Standard](model-hardware-standard.md)
- [Laboratory automation and self-driving labs](../concepts/robotics/laboratory-automation.md)
- [Agent skills](../concepts/agents/agent-skills.md)

## Mentioned in

- [Previewing the Model Hardware Standard](../sources/anthropic-model-hardware-standard-preview.md)
