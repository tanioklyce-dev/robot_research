---
title: QuEra Computing
type: entity
subtype: company
created: 2026-08-30
updated: 2026-08-30
sources: 1
tags: [quera, quantum-computing, neutral-atom, mhs, agentic-control, laser-stabilization]
---

**QuEra Computing** — builds quantum computers using **neutral atoms**, where nearly all control, operation and readout of the atomic qubits happens through the controlled interaction of lasers with atoms. In this wiki QuEra appears as the [MHS](model-hardware-standard.md) preview partner that produced its **strongest quantitative result**: an agent-developed laser relock controller ([Previewing the Model Hardware Standard](../sources/anthropic-model-hardware-standard-preview.md)).

## Why the problem is hard

A titanium-sapphire laser must hold its frequency to roughly **one part in 10¹²** — QuEra's analogy is measuring the Earth–Moon distance to the width of a human hair. Temperature, vibration or a pressure change (someone opening the lab door) can break the "lock," and a long error-corrected computation dies with it. Human recovery takes **5–10 minutes** and requires an expert reading several instruments at once; in university labs the skill is handed down between graduate students, and at 2 a.m. someone drives in. QuEra's framing: at fleet scale that is untenable.

## Result 1 — relock controller

| | Success rate | Time per attempt |
|---|---|---|
| Human expert at the bench | — | 5–10 min |
| Bespoke script (4 engineers, several months) | **58%** | ~150 s |
| Claude via MHS, blind test over **700 trials** | **99.3%** (695/700) | 0.9–5.4 s typical, 10–14 s worst |

The **method** is the transferable part: four roles, each a fresh Claude instance — hypothesize an improvement, write it into the script, run it against the **live laser** and log every step, read the logbook and choose the next change — cycling hundreds of times unattended overnight. Development-run convergence was ~6 s at 96%; the 99.3% is the later blind test with no agent involved.

**Why it beat the prior script.** The bespoke script reproduced the human procedure step for step, so it inherited the human flaw: a linear sequence cannot absorb a disturbance that undoes an already-completed step, and must restart. Claude rewrote it as a **decision tree** that reads the instruments and touches only the one or two controls the observed disturbance implicates. A human must check every control to be *sure*; Claude found the shortcut by inducing disturbances repeatedly until the pattern was legible — an advantage of iteration speed, not of insight.

**The deliverable is a deterministic, fully inspectable script that runs in production without an agent** — the *explore, then compile* pattern described on [MHS](model-hardware-standard.md) and [code as policy](../concepts/agents/code-as-policy.md).

## Result 2 — PID tuning, and a heuristic caught failing

12 interdependent servo parameters set lock quality. A specialist tunes against the servo's reported **RMS error**, because capturing an oscilloscope trace and running an FFT after every change is impractical by hand. Claude did precisely that, hundreds of times overnight.

- **15.7 mV** (the specialist's standing tune) → **1.55 mV**, over **363 experiments and 16 unattended hours**.
- Independent verification on a **phase-noise analyzer**, against a blind from-scratch retune by the same specialist: the two matched across the band **except at a ~220 kHz resonance, where the manual tune left roughly 1000× more noise** — exactly the error the RMS heuristic permits.
- The check that matters operationally: over a **19-hour run Claude's PIDs never lost lock**, while the expert-tuned PIDs unlocked **~1.6 times an hour**.

Unlike the relock controller, this workflow **keeps the agent in the loop**, because the parameters drift with temperature and pressure.

> [!note] The general lesson
> The specialist's heuristic was not wrong — it is usually right, and cheap. Claude's advantage was **not having to trust it**: it could measure the true objective after every change, at a rate no human can sustain. That is the same argument as [ASPIRE](aspire.md)'s and [Karpathy's autoresearch](../sources/karpathy-autoresearch.md)'s, arriving from instrumentation rather than from code.

## Limitations QuEra reports

- Claude's understanding of the rig was **programmatic rather than physical**: when something went wrong with the hardware itself, it could not troubleshoot.
- **Over-caution** — experiments sometimes paused overnight waiting for human confirmation on actions Claude deemed slightly risky. QuEra's judgment: preferable to the alternative.
- Substantial context engineering was required to get correct behavior.

## What's next (stated)

Deploy relock recovery on live quantum processors, package the tuning workflow as a standalone tool, and extend the approach to other precise, fragile subsystems — "a fleet of machines that increasingly look after themselves."

## Related

- [Model Hardware Standard](model-hardware-standard.md) — the interface used.
- [Code as policy](../concepts/agents/code-as-policy.md) — agent explores, deterministic script ships.
- [Anthropic](anthropic.md)

## Mentioned in

- [Previewing the Model Hardware Standard](../sources/anthropic-model-hardware-standard-preview.md)
