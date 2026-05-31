---
title: "cubff (paradigms-of-intelligence/cubff) — GitHub"
type: source
url: https://github.com/paradigms-of-intelligence/cubff
local_path: raw/cubff-github-readme.md
author: Google Paradigms of Intelligence Team
published: 2024
ingested: 2026-05-31
format: github
license: Apache-2.0
tags: [artificial-life, alife, self-replication, emergence, brainfuck, bff, forth, subleq, cuda, agent-based-model, paradigms-of-intelligence, code]
---

## Summary

**cubff** is the official code release behind ["Computational Life" (Agüera y Arcas et al., 2024)](computational-life-self-replicating-programs-paper.md): "a (optionally) CUDA-based implementation of a self-modifying soup of programs which show emergence of self-replicators." Most experiments in the paper were run with it. It's the runnable substrate for the paper's central result — drop random, non-self-replicating programs into a shared-tape soup, concatenate + execute random pairs, and **self-replicators reliably emerge with no fitness function**.

> [!note] Name disambiguation
> The paper's substrate is called **"BFF"** (an extended Brainfuck where programs share one read/write tape). It is implemented in **this** repo (`cubff`), *not* in the similarly-named `apankrat/bff` (an unrelated standalone Brainfuck interpreter).

## Key claims

- **Purpose.** CUDA-or-CPU simulation of a self-modifying program soup demonstrating spontaneous emergence of self-replicators; the experimental engine for the [Computational Life paper](computational-life-self-replicating-programs-paper.md).
- **Substrates selectable via `--lang`:**
  - **BFF / Brainfuck variants** — `bff_noheads`, `bff8`, `bff_perm`, `bff_selfmove`.
  - **Forth** — stack-based variants.
  - **SUBLEQ** and **RSUBLEQ4** — the one-instruction-set substrates that serve as the paper's *counterexample* (spontaneous emergence not observed).
- **Build.** Deps: `build-essential` + `libbrotli-dev` (Debian/Ubuntu) or `base-devel` + `brotli` (Arch). Build with `make` (CUDA) or `make CUDA=0` (CPU-only). Run e.g. `bin/main --lang bff_noheads`. **Python bindings** via `cubff.py`.
- **Repo (at capture):** Apache-2.0; ~200 stars / 48 forks; C++ 38.9% / Python 25.5% / HTML 17.8% / CUDA 16.2%; CI via GitHub Actions.

## Entities mentioned
- [Blaise Agüera y Arcas](../entities/blaise-aguera-y-arcas.md) — leads the Google Paradigms of Intelligence Team that authored the paper + this code.

## Concepts touched
- [Artificial life and the emergence of self-replication](../concepts/alife/artificial-life-and-self-replication.md) — this is the runnable engine for that concept's anchor result.
- [Flocking and boids](../concepts/alife/flocking-and-boids.md) — sibling "emergence from simple local interaction" model, different substrate (continuous steering vs. self-modifying code).

## Open questions
- The README lists more BFF variants (`bff8`, `bff_perm`, `bff_selfmove`) than the paper foregrounds — which variant maps to which paper figure isn't captured here.
- Reproduction cost / runtime for the headline emergence experiments on CPU-only vs. CUDA is not documented in this capture (cf. the wiki's interest in single-GPU reproducibility for [LeWM](leworldmodel-paper.md)).
