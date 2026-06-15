---
title: "autoresearch — Karpathy's agent-driven LLM training research repo (GitHub repo, 2026-03)"
type: source
url: https://github.com/karpathy/autoresearch
author: Andrej Karpathy
affiliation: independent / formerly OpenAI & Tesla
published: 2026-03-06 (initial commit)
ingested: 2026-05-14
tags: [karpathy, autoresearch, llm-agent, agent-research, nanochat, github, reference-implementation, claude-code, codex]
github_stats: 81K stars, 11.8K forks (May 2026)
---

> [!note] Ingest depth
> Read the README in full (~120 lines). Key external context: Karpathy's two tweets ([1](https://x.com/karpathy/status/2029701092347630069), [2](https://x.com/karpathy/status/2031135152349524125)). Code itself (`train.py`, `prepare.py`, `program.md`) is the actual artifact.

## Summary

**autoresearch** — Karpathy's March 2026 project: **give an AI coding agent a small but real LLM training setup and let it experiment autonomously overnight.** The agent modifies `train.py` (a simplified single-GPU version of [nanochat](karpathy-nanochat.md)'s pipeline), trains for a **fixed 5-minute wall-clock budget**, checks if **val_bpb** (validation bits per byte, vocab-size-invariant) improved, keeps or discards the change, and repeats. You wake up to a log of ~100 experiments and (hopefully) a better model.

**The novel pedagogical claim:** "you're not touching any of the Python files like you normally would as a researcher. Instead, you are programming the `program.md` Markdown files that provide context to the AI agents and set up your autonomous research org." The unit of work shifts from *edit Python* to *edit prompt*.

**Why it matters to this wiki.** Two reasons:

1. **First public, measurable evidence that an AI coding agent can produce real improvements to a frontier ML training pipeline.** Karpathy used autoresearch to drive **two leaderboard improvements on [nanochat](karpathy-nanochat.md)'s GPT-2 speedrun** — rows 5 and 6 of the nanochat leaderboard, dropping wall-clock from 2.02 → 1.80 → 1.65 hours over two rounds ([1.80h commit](https://github.com/karpathy/nanochat/commit/6ed7d1d), [1.65h commit](https://github.com/karpathy/nanochat/commit/a825e63)). This is a wiki-relevant data point: agent-driven research isn't speculative anymore; it's producing leaderboard commits.

2. **A concrete template for "agent + small training pipeline + measurable objective."** The architecture (single-GPU H100, fixed 5-min budget, single Python file the agent edits, single Markdown file the human edits) is small enough to copy. **The [Onchain AI Garage LeWM reproduction](onchain-ai-garage-lewm-reproduction.md)** independently arrives at a similar pattern (Claude Code in WSL + handoff markdown + nightly run), suggesting this is a generalizable workflow for ML-with-an-agent.

## How it works (the README's three files)

```
prepare.py      — fixed constants, one-time data prep, runtime utilities (do not modify)
train.py        — model, optimizer, training loop (the AGENT modifies this)
program.md      — agent instructions (the HUMAN modifies this)
pyproject.toml  — dependencies
```

The agent (Claude Code, Codex, or whatever) is pointed at `program.md` and turned loose with all permissions disabled (sandbox mode). The README's example prompt:

> Hi have a look at program.md and let's kick off a new experiment! let's do the setup first.

`program.md` is "essentially a super lightweight 'skill.'" The agent reads it, picks a candidate change to `train.py`, runs the 5-minute training experiment, evaluates val_bpb, and decides whether to keep the change or revert. The cycle repeats indefinitely.

## Design choices (from the README)

1. **Single file to modify.** Agent only touches `train.py`. Scope is bounded; diffs are reviewable.
2. **Fixed 5-minute time budget per experiment.**
   - Makes experiments **directly comparable** regardless of what the agent changes (model size, batch size, architecture).
   - Means **~12 experiments/hour, ~100 experiments overnight**.
   - Means autoresearch finds the most compute-optimal model **for your specific platform** in that budget.
   - Downside: your results aren't directly comparable to other people's autoresearch results on different hardware.
3. **Self-contained.** No external dependencies beyond PyTorch. No distributed training, no complex configs. One GPU, one file, one metric.
4. **The metric is `val_bpb`** (validation bits per byte). Vocab-size-invariant, so architectural changes that touch tokenization or vocab are fairly compared.

## What it produces (the leaderboard evidence)

The nanochat README's GPT-2 speedrun leaderboard rows 5 and 6 are autoresearch-driven:

| Row | Time | val_bpb | CORE | Description | Date |
|---|---|---|---|---|---|
| 4 | 2.02 h | 0.71854 | 0.2571 | NVIDIA ClimbMix dataset (human) | Mar 4 2026 |
| **5** | **1.80 h** | **0.71808** | **0.2690** | **autoresearch round 1** | **Mar 9 2026** |
| **6** | **1.65 h** | **0.71800** | **0.2626** | **autoresearch round 2** | **Mar 14 2026** |

That's an **18% wall-clock improvement on a state-of-the-art-internal pretraining recipe**, driven by an agent over ~5 days of clock time (which includes presumably many overnight experiment batches). The reduction is large by leaderboard standards — autoresearch rounds 1 + 2 produced more wall-clock improvement than the four prior human-driven entries combined (3.04 → 2.91 → 2.76 → 2.02 → 1.80 → 1.65).

## Platform support and forks

Officially: a single NVIDIA GPU (H100 tested). Karpathy explicitly declines to add CPU/MPS support in the main repo to keep it small, but points to community forks:

- **autoresearch-macos** (miolini): MacOS
- **autoresearch-mlx** (trevin-creator): MacOS (MLX backend)
- **autoresearch-win-rtx** (jsegov): Windows
- **andyluo7/autoresearch**: AMD

For smaller hardware the README recommends: TinyStories dataset (lower entropy), smaller `vocab_size`, lower `MAX_SEQ_LEN`, lower `DEPTH` (default 8 → 4), `WINDOW_PATTERN="L"` (skip banded attention), lower `TOTAL_BATCH_SIZE`.

## Curriculum / concept hookups

- **[LLM-agent architecture concept](../concepts/agents/llm-agent-architecture.md)** — autoresearch is a *non-robotics* worked example of an LLM-emits-actions agent pattern: instead of `find()`/`pickup()`/`place()` tool calls, the actions are `edit train.py`, `run experiment`, `compare metric`, `commit or revert`. Same control-flow pattern, applied to ML research.
- **[Curriculum Module 3 — Sequence models, attention, transformers](../syntheses/curriculum/curriculum-03-attention-and-transformers.md)** — natural place to introduce autoresearch as "the modern-2026 extension of the nanoGPT/nanochat reading path: an agent iterating on the training loop."
- **[Curriculum Module 14 — Capstone](../syntheses/curriculum/curriculum-14-capstone.md)** — the capstone's Phase A reproduces LeWM PushT + writes an experiment-design memo. autoresearch is the methodological cousin: a tight loop of "candidate change → 5-min experiment → keep or revert." Worth flagging as prior art for the experiment-design pattern.

## The framing claim

From the README's opening (in-character flavor text):

> "One day, frontier AI research used to be done by meat computers in between eating, sleeping, having other fun, and synchronizing once in a while using sound wave interconnect in the ritual of 'group meeting'. That era is long gone. Research is now entirely the domain of autonomous swarms of AI agents running across compute cluster megastructures in the skies. The agents claim that we are now in the 10,205th generation of the code base, in any case no one could tell if that's right or wrong as the 'code' is now a self-modifying binary that has grown beyond human comprehension. This repo is the story of how it all began. — @karpathy, March 2026"

This is satirical-but-pointed. The real product claim is more modest: a small but real LLM training setup + an agent loop produces measurable improvements on a leaderboard the author maintains. The wiki should treat the **leaderboard result as the load-bearing claim** and the framing as positioning.

## Entities mentioned

- **[Andrej Karpathy](../entities/andrej-karpathy.md)** — author.
- **[Anthropic](../entities/anthropic.md)** (via Claude Code) and **OpenAI** (via Codex) — the example agents the README names. Either works as the autoresearch driver.

## Concepts touched

- **LLM-agent architecture** — autoresearch is the most distilled "agent + tool + measurable metric" example in the wiki.
- **Compute-optimal model training** — the `--depth` dial + fixed 5-min budget makes this the search problem the agent is solving.
- **Coding-agent-driven research** — the pattern (plan in markdown → execute in code → measure → iterate) is the same one the [Onchain AI Garage LeWM reproduction](onchain-ai-garage-lewm-reproduction.md) independently arrives at.

## Related sources

- [karpathy/nanochat](karpathy-nanochat.md) — the parent project; autoresearch is "a simplified single-GPU implementation of nanochat."
- [karpathy/nanoGPT](karpathy-nanogpt.md) — predecessor in the same lineage.
- [karpathy/micrograd](karpathy-micrograd.md) — same author, autograd-from-scratch.
- [Onchain AI Garage — LeWM reproduction](onchain-ai-garage-lewm-reproduction.md) — independent application of "agent + tight training loop + measurable objective" to a different ML research target.

## Open questions / TBD

- **What did the agent actually do in rounds 1 and 2?** The leaderboard rows link to specific commits in the nanochat repo (`6ed7d1d`, `a825e63`); reading those diffs would tell us what kind of changes the agent found. A wiki synthesis could quantify "what fraction of the improvement was hyperparameter tuning vs architecture changes vs optimizer tweaks."
- **How does the agent's $/improvement compare to a human researcher's?** Karpathy hasn't published this comparison directly. With 12 experiments/hour @ ~$3/GPU-hr, autoresearch is ~$0.25/experiment. A human-driven experiment with cluster setup, eval, etc., is probably ~$5–50/experiment. The ratio is interesting.
- **What does the `program.md` look like for a more sophisticated research org?** The README hints at this but doesn't develop it. If autoresearch becomes a category, the `program.md`-design problem is the new "feature engineering."
