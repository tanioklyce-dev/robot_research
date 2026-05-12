---
title: "Possible Principles Underlying the Transformations of Sensory Messages (H. B. Barlow, 1961)"
type: source
url: https://www.researchgate.net/publication/259201023_Possible_Principles_Underlying_the_Transformation_of_Sensory_Messages
local_path: raw/Barlow-SensoryCommunication-1961.pdf
author: Horace B. Barlow
affiliation: Physiological Laboratory, Cambridge University
published: 1961 (chapter 13 in *Sensory Communication*, ed. W. A. Rosenblith, MIT Press)
ingested: 2026-05-12
created: 2026-05-12
updated: 2026-05-12
tags: [barlow, neuroscience, redundancy-reduction, factorial-code, sensory-coding, information-theory, foundational, historical]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/Barlow-SensoryCommunication-1961.pdf`, 18 pages, pages 217–234 of the source book *Sensory Communication*). Full read; this is a position paper / theoretical-neuroscience essay, not a technical paper, so the depth is moderate — about as much summary as the original author put into his own concluding paragraph plus the redundancy-reduction section, which is the part everything downstream cites.

## Summary

**Horace Barlow's 1961 chapter** — the **foundational reference for the "redundancy reduction" principle** in sensory neuroscience. Asks: what *operation* do sensory relays perform? Birds fly; their wings are for flying. What are sensory neurons *for*?

Barlow proposes three (non-exclusive) hypotheses:

1. **Password hypothesis** — sensory relays detect specific key stimuli of behavioral significance (e.g. frog retina detecting bug-shaped moving spots).
2. **Filter / control hypothesis** — sensory relays act as adaptive filters whose pass-characteristics are modulated by downstream cognitive needs.
3. **Redundancy-reduction hypothesis** — sensory relays **recode highly redundant sensory inputs into a factorial code** (statistically independent components), extracting high-relative-entropy signals from low-entropy raw input.

The third hypothesis gets ~75% of the chapter and is **the only one that has propagated forward as a continuing organizing principle** in 60+ years of computational vision and SSL research.

**Why this matters to the wiki.** This is the **eponymous reference** for [Barlow Twins (Zbontar et al. 2021)](barlow-twins-paper.md): Zbontar, Jing, Misra, LeCun, and Deny named their SSL method after Horace Barlow because their cross-correlation-identity loss is the neural-network analogue of Barlow's redundancy-reduction principle. The full causal chain into modern JEPA literature:

```
Barlow 1961: "factorial code" / redundancy reduction
   ↓ (60 years of vision neuroscience + computational SSL)
Barlow Twins 2021: cross-correlation → I
   ↓ (decomposed into separate terms)
VICReg 2022: variance + covariance + invariance
   ↓ (LeCun cites VICReg by name)
LeCun 2022 — Path Towards AMI: regularized SSL as JEPA training paradigm
   ↓
PLDM 2025 / LeJEPA 2025 / LeWM 2026 — JEPA world models
```

**One paper. Two neuroscience-inspired ideas. Sixty-five years of compounding influence.**

## Abstract / source-citation context (verbatim, from the chapter's summary)

> "Most space is given to discussion of the third hypothesis, that reduction of redundancy is an important principle guiding the organization of sensory messages and is carried out at relays in the sensory pathways. Some simplifying assumptions about the information-carrying variables of nerve messages are made, followed by a statement of the hypothesis and an explanation of the terms used. Examples of recoding are described to illustrate its consequences, and predictions (which might be experimentally testable) and speculations (for entertainment only) are made."

> "To strip the redundancy from the preceding pages, what I have said is this: it is foolish to investigate sensory mechanisms blindly — one must also look at the ways in which animals make use of their senses."

## The three hypotheses

### 1. Password hypothesis (Section "Password Hypothesis")
Sensory relays contain detectors for behaviorally significant patterns. Examples Barlow cites:
- **Frog retina** (Lettvin, Maturana, McCulloch, Pitts 1959 — "What the frog's eye tells the frog's brain") — bug detectors.
- Cutaneous stimuli that elicit flexion/withdrawal in the spinal cat.

This hypothesis is what we today call **feature detection** — a hard-wired template for a behaviorally relevant pattern. Barlow notes that this is the simplest hypothesis and probably right for "the early relays" (early sensory stages) but not for the higher-level recoding observed in cortex.

### 2. Filter / control hypothesis (Section "Pass-characteristics Hypothesis")
Sensory relays are filters whose characteristics are **modulated by other parts of the nervous system**. Examples:
- Adaptation in the retina (cat retinal organization varies with state of light adaptation).
- Attention (sensory transmission gated by central state).

Barlow notes this hypothesis is "the fashionable one" of his time and gestures at it before moving on. Today's analogue: **attention mechanisms, top-down predictive coding, contextual gating**.

### 3. Redundancy-reduction hypothesis (Section "Redundancy-Reducing Hypothesis" — the main contribution)

> "Sensory relays try to ensure that what they pass on really is news."

The editorial analogy: an editor rejects redundant content. The information-theoretic restatement (in Shannon's language, which Barlow had recently encountered): **sensory relays recode redundant input signals into a factorial code with statistically independent components, maximizing information transmitted per signal**.

Why redundancy reduction is the central operation:
- Raw sensory input is **enormously redundant** — adjacent retinal cells receive correlated input from the world's statistical structure (smoothness, repeated objects, etc.). A factorial code with the same dimensionality could carry far more information per bit.
- An animal's behavior depends on **detecting changes / events / decisions**, which corresponds to high-entropy events in a non-redundant code.
- The nervous system's bottleneck is fiber count + average firing rate. Redundancy reduction makes maximal use of fixed-capacity channels.

Barlow's **simplifying assumptions** for the math:
1. Sensory pathways treated as noiseless.
2. Discrete-time, binary (impulse / no-impulse) signaling.
3. Channel capacity bounded by `F` (fibers) × `R` (time slots per second) × `I` (avg impulses per fiber per second).

Predictions Barlow makes (Section "Examples of Recoding"):
- Off-center / on-center retinal ganglion cells decorrelate spatial input.
- Lateral inhibition implements local decorrelation.
- Adaptation to repeated stimuli implements temporal decorrelation.
- "Cells should fire most when stimuli depart from expected statistics."

> [!note] Barlow's prediction is exactly modern predictive coding
> The 1961 prediction that "cells should fire most when stimuli depart from expected statistics" is what Rao & Ballard's 1999 predictive-coding model formalized — and what JEPA in 2022 instantiates at the level of learned representations: predict the next embedding; train on residual.

## What this paper grounds

The redundancy-reduction principle propagates forward through three distinct strands:

1. **Vision neuroscience**: lateral inhibition, retinal ganglion-cell types, sparse coding (Olshausen & Field 1996), efficient-coding hypothesis (Atick & Redlich, 1990s), independent-component analysis (Bell & Sejnowski 1995). See Barlow's own 2001 review *"Redundancy reduction revisited"* for a 40-year retrospective.
2. **Self-supervised representation learning**: Barlow Twins (2021) names itself after this paper; VICReg (2022) decomposes the same principle into variance + covariance; SIGReg (LeJEPA 2025) replaces both with a single isotropic-Gaussian regularizer that achieves the same information-maximization goal.
3. **Energy-based models / JEPA**: LeCun's 2022 [Path Towards AMI](lecun2022-path-towards-ami.md) makes redundancy reduction (via VICReg-class regularizers) the core anti-collapse mechanism for JEPA training.

## Entities mentioned

- **Horace B. Barlow** — sole author. Cambridge physiologist, foundational figure in computational vision neuroscience. Eponymous source for [Barlow Twins](barlow-twins-paper.md). Not yet a separate entity page in this wiki — *worth creating if other Barlow-line references accumulate.*

## Concepts touched

- **Redundancy reduction / factorial code** — the foundational concept. Worth a dedicated concept page; currently scattered across [Barlow Twins](barlow-twins-paper.md), [VICReg](vicreg-paper.md), [LeJEPA](lejepa-paper.md), and [Welch Labs explainer](welchlabs-lecun-1b-bet-against-llms.md).
- **Predictive coding (prefigured)** — Barlow's "cells should fire when stimuli depart from expected statistics" is the conceptual core that Rao & Ballard formalized in 1999.
- **Information bottleneck (prefigured)** — Tishby's 2000 information-bottleneck principle is the IT-language descendant of Barlow's redundancy-reduction-with-fixed-capacity story. [Barlow Twins](barlow-twins-paper.md) explicitly derives its loss from the IB principle.

## Why ingest a 64-year-old neuroscience chapter into a robotics wiki

Two reasons:

1. **Eponymous reference.** Every Barlow Twins / VICReg / SIGReg paper traces lineage back to this document. The wiki had implicit references to "Barlow's redundancy-reduction principle" in multiple source pages with no resolving citation — now it does.
2. **It's still the cleanest statement of the principle.** The mid-2020s SSL literature has reinvented redundancy reduction with neural networks; the 1961 statement (a factorial code is the optimal recoding of a redundant high-capacity signal under fixed-capacity downstream constraints) remains the simplest articulation. New SSL methods that drift from "decorrelate features" toward arbitrary anti-collapse heuristics can be measured against this principle to check whether they're still doing the same thing or something different.

## Open questions / TBD

- **Horace Barlow entity page**: warranted if the wiki picks up more Barlow-line references (sparse coding, ICA, efficient-coding hypothesis, Atick & Redlich). Currently just one citation chain into modern SSL.
- **"Redundancy reduction" concept page**: would consolidate the through-line from Barlow 1961 → Barlow Twins → VICReg → SIGReg → DINOv3-Gram-anchoring. Would also clarify which 2020s methods are still doing redundancy reduction (VICReg, LeJEPA) vs. something different (BYOL/SimSiam — implicit, asymmetric; DINO/iBOT — clustering-into-prototypes).
- Barlow's **2001 review** *"Redundancy reduction revisited"* (Network: Computation in Neural Systems) is not in the wiki — would update the bridge from 1961 to the 2010s SSL revival.
- Atick & Redlich's **efficient-coding hypothesis** (early 1990s) and Olshausen & Field's **sparse coding** (1996) are intermediate steps in the Barlow → Barlow-Twins chain — both currently absent from the wiki.
