---
title: "A Drosophila computational brain model reveals sensorimotor processing (Shiu et al. 2024)"
type: source
subtype: paper
created: 2026-05-08
updated: 2026-05-08
url: https://doi.org/10.1038/s41586-024-07763-9
pmcid: PMC11446845
author: Shiu, Sterne, Spiller, Franconville, Sandoval, Zhou, Simha, Kang, Yu, Kim, Dorkenwald, Matsliah, Schlegel, Yu, McKellar, Sterling, Costa, Eichler, Bates, Eckstein, Funke, Jefferis, Murthy, Bidaye, Hampel, Seeds, Scott
published: 2024-10-02
ingested: 2026-05-08
journal: "Nature 634(8032):210–219"
code: https://github.com/philshiu/Drosophila_brain_model
data: https://edmond.mpdl.mpg.de/dataset.xhtml?persistentId=doi:10.17617/3.CZODIW
license: MIT (code)
tags: [drosophila, flywire, connectome, leaky-integrate-and-fire, brian2, sensorimotor, brain-simulation, biological-ai]
---

## Summary

Open-access *Nature* paper (published 2 October 2024) introducing a **leaky integrate-and-fire (LIF) computational model of the entire adult *Drosophila* central brain** built directly on the [FlyWire](../entities/flywire.md) connectome. 127,400 proofread neurons; ~50M synaptic connections. The model is calibrated by a single free parameter (synaptic weight `Wsyn = 0.275 mV`) and reproduces sensorimotor responses for taste-driven proboscis extension and antennal mechanosensory grooming circuits, matching ~91% of 164 empirical predictions tested optogenetically. The released code (MIT-licensed, [philshiu/Drosophila_brain_model](https://github.com/philshiu/Drosophila_brain_model)) is what powers the "fly brain on a laptop" claim from the [Berkeley News article](berkeley-fly-brain-news.md). Lead author **Philip K. Shiu** (UC Berkeley → Eon Systems); senior author **Kristin Scott** (UC Berkeley).

## Thesis

A single, anatomically constrained LIF model — wiring straight from the connectome, neurotransmitter polarity straight from EM-predicted transmitter identity — predicts which neurons are activated by specified sensory inputs and which downstream neurons drive observable behaviour, *without any training, fitting, or learning*. The connectome alone, plus simple spike dynamics, already captures first-order sensorimotor transformations.

## Key claims

### Model construction
- **Scale.** 127,400 neurons (FlyWire materialization v.630), all chemical synapses with predicted neurotransmitter identity. No gap junctions (not visible in EM). No neuropeptides. No plasticity.
- **Dynamics.** Leaky integrate-and-fire. Resting potential −52 mV; firing threshold −45 mV; refractory period 2.2 ms.
- **Polarity from EM transmitter prediction.** GABAergic + glutamatergic → inhibitory; cholinergic, dopaminergic, octopaminergic, serotonergic → excitatory. (Glutamate-as-inhibitory tested for sensitivity; flipping it to excitatory bumps false-positive rate from 1% → 16%.)
- **Single free parameter** `Wsyn = 0.275 mV`, calibrated to give plausible behavioural firing rates. ±30% perturbation leaves predictions 85–88% accurate.

### Software & runtime
- **Implemented in [Brian 2](https://briansimulator.org/)** — a Python-based spiking-neural-network simulator. The repo's `environment.yml` pins Brian 2 and the FlyWire connectivity tables (parquet, materializations 630 + 783).
- **Runtime.** ~5 minutes per 1,000 ms simulated trial on a standard CPU; configurable thread count. The "runs on a laptop" framing in [Berkeley News](berkeley-fly-brain-news.md) is correct in this sense — the model is not GPU-bound.
- **Repository contents.** `model.py` (core), `utils.py` (helpers), `example.ipynb` (tutorial), `figures.ipynb` (paper figure regeneration), connectivity parquet files, completeness CSVs. Raw model output (multi-GB) hosted externally on Edmond (Max Planck data archive).

### Validation
- **Feeding circuit (suboesophageal zone).** Activating sugar-sensing GRNs in the model predicts neurons known to drive feeding initiation; 91% of 164 predictions held up against optogenetic activation/silencing experiments and calcium imaging on the real fly. Specifically:
  - 10 of 11 cell types upstream of MN9 (proboscis extension motor neuron) tested cleanly positive in optogenetics.
  - Sugar and water pathways predicted to share ~250 common downstream neurons.
  - Bitter and **Ir94e** GRNs predicted to inhibit proboscis extension. Ir94e's aversive function was *novel* — confirmed in vivo, prior literature treated Ir94e as a salt/courtship sensor.
- **Grooming circuit (antennal mechanosensory and motor center).** JON activation in the model identifies the known aBN1/aBN2 interneurons + aDN1/aDN2 descending neurons in the antennal grooming circuit. The model also correctly predicts that JO-F neurons fail to activate aBN1 *despite* anatomical connectivity — confirmed by calcium imaging.

## Reproducibility status

- **Code:** [github.com/philshiu/Drosophila_brain_model](https://github.com/philshiu/Drosophila_brain_model) — **MIT licensed**. 47 commits on the main branch; conda-based install via `environment.yml` (full pin in `environment_full.yml`). Brian 2 + C++ codegen recommended for performance.
- **Data:** FlyWire connectivity tables shipped in the repo as parquet (versions 630 and 783). Raw paper-output simulation tensors archived at Edmond, doi `10.17617/3.CZODIW`.
- **Hardware:** standard multi-core CPU; no GPU required.
- **Net assessment.** This is the most reproducible piece of the brain-side stack. Reproduces independently of FlyWire's web tooling (the connectome data is bundled), and the entire pipeline is open-source Python.

## Entities mentioned

- [FlyWire](../entities/flywire.md) — connectome dataset; the wiring is the input.
- [Drosophila melanogaster](../entities/drosophila.md) — model organism.
- [Drosophila brain model](../entities/drosophila-brain-model.md) — the released codebase (MIT, Brian 2).
- [Phil Shiu](../entities/phil-shiu.md) — lead author + code maintainer (UC Berkeley → Eon Systems).
- Kristin Scott — senior author (UC Berkeley).
- Sven Dorkenwald, Mala Murthy — Princeton; FlyWire consortium leads also on this paper.
- Gregory Jefferis, Philipp Schlegel, Marta Costa — MRC LMB / Cambridge; FlyWire annotation leads.

## Concepts touched

- [Connectome](../concepts/connectome.md) — the input substrate.
- [Biomechanical simulation](../concepts/biomechanical-simulation.md) — companion thread; this paper is brain-only.

## Open questions

- **No body, no environment.** The model takes synthetic spike inputs to designated sensory neurons and reads out spike outputs from designated motor neurons. There is no fly body, no MuJoCo coupling, no closed loop. Pairing it with [flybody](../entities/flybody.md) is the obvious next step but is not implemented in this paper or its repo. See [Whole-organism agentic AI](../syntheses/whole-organism-agentic-ai.md).
- **No learning.** All "weights" are connectome-given counts × `Wsyn` × ±polarity. No plasticity, no training. This is intentional — the paper's claim is precisely that the connectome alone is enough — but it limits the model to circuits where intrinsic dynamics and neuromodulation are not load-bearing.
- **Excluded biology.** No gap junctions (EM invisibility), no neuropeptides, no glia, no non-spiking neurons, no morphologically detailed compartments. The authors flag circuits with "extensive basal inhibition" or heavy neuromodulation as poorly predicted; absolute firing rates are not expected to match real recordings.
- **Glutamate uniformly inhibitory** — known oversimplification; in vivo polarity varies by receptor.

## Why it matters here

- **Closes a wiki gap.** This paper was [previously TBD](../syntheses/whole-organism-agentic-ai.md) — only its [Berkeley News writeup](berkeley-fly-brain-news.md) was ingested. Now we have the primary source, the runtime substrate (Brian 2), and the actual reproducibility surface (MIT-licensed Python repo + bundled connectivity data + external simulation archive).
- **First half of the brain-side reproducibility answer.** Combined with [Lappalainen et al. 2024](lappalainen-flyvis-paper.md) (connectome-constrained deep nets), this defines two distinct, both-open-source ways to *use* a connectome — see the two paradigms now documented on [Connectome](../concepts/connectome.md).
