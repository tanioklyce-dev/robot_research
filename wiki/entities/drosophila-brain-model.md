---
title: Drosophila brain model (philshiu/Drosophila_brain_model)
type: entity
subtype: code-repository
created: 2026-05-08
updated: 2026-05-10
sources: 3
license: MIT
url: https://github.com/philshiu/Drosophila_brain_model
tags: [fly-brain, leaky-integrate-and-fire, brian2, flywire, drosophila, open-source, mit-license]
---

**`philshiu/Drosophila_brain_model`** — Open-source code release accompanying [Shiu et al. 2024 *Nature*](../sources/shiu-fly-brain-paper.md). Implements a **leaky integrate-and-fire (LIF) dynamical model of the entire adult *Drosophila* central brain**, driven directly by the [FlyWire](flywire.md) connectome. Maintained by **Philip K. Shiu**. **MIT-licensed.**

This is the artifact behind the "fly brain on a laptop" framing in the [Berkeley News writeup](../sources/berkeley-fly-brain-news.md) — simulations run on standard CPU at ~5 minutes per 1,000 ms simulated trial.

## What it is

- **A LIF spiking simulation** of 127,400 FlyWire-proofread neurons with chemical-synapse connectivity from materialization v.630.
- Built on **[Brian 2](https://briansimulator.org/)**, a Python spiking-neural-network simulator.
- A single free parameter `Wsyn = 0.275 mV`; everything else (signs from EM-predicted neurotransmitter, resting potential −52 mV, threshold −45 mV, refractory 2.2 ms) is fixed.
- No training. No learning. The connectome alone, plus simple dynamics, is the model.

## Repository contents

| File | Purpose |
|---|---|
| `model.py` | Core LIF model implementation |
| `utils.py` | Helpers |
| `example.ipynb` | Tutorial notebook |
| `figures.ipynb` | Regenerates the paper's figures |
| `environment.yml` / `environment_full.yml` | Conda envs (full version is fully pinned) |
| `*.parquet` | FlyWire connectivity tables (materializations 630 + 783) |
| Completeness CSVs | Per-cell-type proofreading completeness metrics |

Per the [Shiu source page](../sources/shiu-fly-brain-paper.md), bulk simulation outputs (multi-GB) live externally on the Max Planck **Edmond** archive (`doi:10.17617/3.CZODIW`) rather than in-repo.

## Install + run shape

- **Conda-based.** `conda env create -f environment.yml`, then install Brian 2 with C++ codegen for performance.
- **Configurable threading** via `n_proc`; defaults to all available cores.
- **No GPU required** — runs on standard multi-core CPU.

## Activity / health (as of 2026-05-08)

- 47 commits on the `main` branch.
- Connectivity data shipped in two materializations (630 used in paper; 783 newer).
- No published successor or fork that integrates with body simulators.

## Why it matters here

- **The most reproducible piece of the brain side** of the [whole-organism agentic AI](../syntheses/agents/whole-organism-agentic-ai.md) stack. Code is MIT, the connectivity is bundled, the runtime is laptop-class, and no GPU is needed — so anyone can reproduce the central result.
- **One of two paradigms** for using a connectome computationally — the *mechanistic LIF* path. The companion is connectome-constrained deep learning ([flyvis](flyvis.md)). See [Connectome](../concepts/bio/connectome.md) for the comparison.
- **Brain-only.** Takes synthetic spike inputs to designated sensory neurons; reads spike outputs from designated motor neurons. There is no body, no environment, no closed loop. Pairing with [flybody](flybody.md) is the obvious next step but is not implemented here.

## Related

- [Shiu et al. 2024 — A Drosophila computational brain model](../sources/shiu-fly-brain-paper.md) — the paper.
- [Phil Shiu](phil-shiu.md) — author / maintainer.
- [FlyWire](flywire.md) — input connectome.
- [flyvis](flyvis.md) — sister project (deep-learning paradigm; same domain).
- [flybody](flybody.md) — body-side complement; unintegrated.
- [Connectome](../concepts/bio/connectome.md) — concept.
- [Whole-organism agentic AI](../syntheses/agents/whole-organism-agentic-ai.md) — synthesis.

## Mentioned in

- [Shiu et al. 2024 — A Drosophila computational brain model](../sources/shiu-fly-brain-paper.md)
