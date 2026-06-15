---
title: "Wolfe — Understanding and Using Supervised Fine-Tuning (SFT) for Language Models (Deep Learning Focus Substack, Sep 2023)"
type: source
url: https://cameronrwolfe.substack.com/p/understanding-and-using-supervised
author: Cameron R. Wolfe, Ph.D.
affiliation: Deep (Learning) Focus Substack newsletter; Wolfe is Director of AI at Rebuy and ex-Alegion ML lead
published: 2023-09-11
ingested: 2026-05-14
tags: [sft, supervised-fine-tuning, llm, alignment, rlhf, lima, instruction-tuning, alpaca, vicuna, llama2, falcon, wolfe, blog, pedagogical]
---

> [!note] Ingest depth
> Source-page metadata + key claims gathered from a WebFetch of the article. This ingest is **summary-level** — it captures the article's main pedagogical structure and the model/dataset zoo it surveys, not a verbatim reproduction.

## Summary

**"Understanding and Using Supervised Fine-Tuning (SFT) for Language Models"** — Cameron R. Wolfe, Ph.D., *Deep (Learning) Focus* Substack newsletter, **2023-09-11**. A long-form pedagogical guide to **Supervised Fine-Tuning (SFT)** — the post-pretraining stage where an LLM is fine-tuned on a curated dataset of *(prompt, high-quality response)* pairs to teach behavioral patterns (instruction-following, chat format, tone) while preserving the general capabilities acquired during pretraining.

Wolfe places SFT inside the three-stage modern LLM alignment recipe:

```
Pretraining (raw web text, next-token prediction)
   ↓
SFT (curated demonstrations, next-token prediction)
   ↓
RLHF / DPO (preference data, reward modeling + policy optimization)
```

**Central claims:**

- **SFT uses the same objective as pretraining** (next-token negative-log-likelihood) — the difference is the *data* (curated demonstrations vs. raw web).
- **SFT is computationally inexpensive** relative to pretraining — fits on a single multi-GPU node for ≤13B models, often fits on a single GPU with PEFT/LoRA.
- **Data quality dominates quantity.** The article highlights **LIMA** (Meta AI, May 2023) — "Less Is More for Alignment" — which achieved competitive instruction-following with **only 1,000 carefully-curated examples**. The result reshapes the field's expectations.
- **SFT alone is insufficient for state-of-the-art.** Wolfe argues RLHF / preference tuning still provides substantial gains beyond SFT, but SFT is the necessary first step and the most data-efficient leverage point.
- **Open-source landscape (Sep 2023).** Surveys the LLaMA-2 / Falcon / MPT base models and the Alpaca / Vicuna / Orca / LIMA / WizardLM SFT recipes built on top.

## Why it matters to this wiki

- **The wiki tracks ~10 VLA / robot-learning sources that rely on SFT-style fine-tuning** — [π0](pi-zero-paper.md), [OpenVLA] (not yet ingested as its own page but mentioned across [vla-models concept](../concepts/learning/vla-models.md) and [Curriculum Module 9](../syntheses/curriculum/curriculum-09-vla.md)), [GR00T](../entities/nvidia-groot.md), [Helix](helix-blog.md), [Gemini Robotics](bostondynamics-spot-gemini-robotics.md), [Robot Utility Models](robot-utility-models-paper.md). All of these inherit the *LLM-trained-on-demonstrations* recipe Wolfe describes. The article is the cleanest non-paper pedagogical entry point for **what SFT is and why it's the necessary first step before robot-action RLHF**.
- **Pairs with [HuggingFace TRL SFT Trainer docs](huggingface-trl-sft-trainer.md)** — Wolfe's article is the *theory + survey*; the TRL docs are the *runnable code*. Both are now in the wiki.
- **Pre-read for any wiki-level discussion of LLM alignment**, complementing [Claude's Constitution](claudes-constitution.md) on the values-and-policy side. Wolfe's piece is about the *mechanics* of getting an LLM to behave; the Constitution is about *what behavior* you're aiming for.
- **The LIMA "data quality > quantity" finding** is directly relevant to the wiki's robot-learning Tier 3 discussion of dataset curation ([Robot Utility Models](robot-utility-models-paper.md): "data diversity > data quantity"). The two slogans are different ("quality" vs "diversity") but rhyme — both reject the "scale at all costs" framing.

## Key claims (per WebFetch summary)

- **SFT definition:** Curate a dataset of high-quality LLM outputs; fine-tune the base model on those examples via standard next-token cross-entropy. Token-level NLL: `L_SFT(θ) = −Σ_t log p_θ(y_t | y_{<t})`. (See [HuggingFace TRL SFT Trainer](huggingface-trl-sft-trainer.md) for the computational form.)
- **Three-stage alignment:** Pretraining → SFT → RLHF (or DPO / KTO / GRPO).
- **LIMA (Meta, 2023):** 1,000 examples sufficient for competitive instruction-following. Reframes the field's expectations away from "more data = better SFT."
- **Open-source models surveyed:** LLaMA-2 (Meta), Falcon (TII), MPT (MosaicML).
- **SFT recipes surveyed:** Alpaca (Stanford, 52K Davinci-003-generated examples), Vicuna (LMSYS, ShareGPT data), Orca (Microsoft, GPT-4 reasoning traces), LIMA (1K curated), WizardLM (instruction-evolution).
- **Public SFT datasets surveyed:** Dolly15K (Databricks), Baize (UCSD), Ultrachat.

## Entities mentioned

- **Cameron R. Wolfe** — author; ex-ML lead at Alegion, currently Director of AI at Rebuy; PhD from Rice University. Not yet a wiki entity.
- **LIMA / LLaMA-2 / Falcon / MPT / Alpaca / Vicuna / Orca / WizardLM** — all SFT-relevant model lineages. None yet have wiki entity pages; **LLaMA-2** in particular is the substrate for [OpenVLA](../concepts/learning/vla-models.md) and several other VLA models tracked here, so an entity stub is worth considering.
- **Hugging Face TRL library** — see [HF TRL SFT Trainer source page](huggingface-trl-sft-trainer.md).

## Concepts touched

- **Supervised Fine-Tuning (SFT)** — the central topic. Not yet a wiki concept page.
- **Instruction tuning** — the most common SFT use case; what turns a *base* LLM into an *instruct/chat* LLM.
- **RLHF / preference tuning** — the second alignment stage; covered briefly in Wolfe's piece. Relevant to [Claude's Constitution](claudes-constitution.md)'s training-process discussion.
- **PEFT / LoRA / adapters** — covered as the parameter-efficient SFT path; the standard way to SFT a 7B+ model on a single consumer GPU.
- **VLA fine-tuning** — not in Wolfe's article (which is LLM-only), but the SFT methodology is what every VLA paper inherits.

## Curriculum hookup

Most natural placement is in [Curriculum Module 9 — Vision-Language-Action models](../syntheses/curriculum/curriculum-09-vla.md) as a **recommended-reading** pointer: "VLAs are vision-language models fine-tuned on robot-action demonstrations, i.e., VLAs *are* SFT applied to a multi-modal model with robot actions in the output space." Wolfe's piece is the cleanest pedagogical entry for the LLM-side of that pattern.

Also potentially relevant to [Curriculum Module 6 — Imitation learning and behavior cloning](../syntheses/curriculum/curriculum-06-imitation-learning.md) — BC is structurally identical to SFT (supervised regression on demonstrations), just with continuous actions instead of discrete tokens.

## Position in the LLM-alignment landscape

```
Pretraining:
  GPT-3 / LLaMA / Falcon / MPT / DeepSeek / Qwen
SFT (Wolfe's topic):
  Alpaca, Vicuna, Orca, LIMA, WizardLM, Dolly
RLHF / preference tuning:
  InstructGPT, Claude, GPT-4, Llama-Chat
DPO / KTO / GRPO / iterative DPO:
  Zephyr, Tulu, NeMo-Aligner
Robot-action SFT (this wiki):
  OpenVLA, π0, π0.5, GR00T, Helix, Gemini Robotics
```

Wolfe's article is the canonical mid-2023 snapshot of the SFT band of this stack.

## Open questions / TBD

- **A `concepts/sft.md` page** — would unify Wolfe + the TRL trainer docs + the VLA-line papers' fine-tuning sections. Defer until a third SFT-flavored source surfaces.
- **Wolfe's follow-up articles** — *Deep (Learning) Focus* has many subsequent pieces on RLHF, DPO, mixture-of-experts, etc. The wiki could pick up specific follow-ups if a particular topic comes up.
- **LIMA paper** (Zhou et al., Meta AI, 2023, arxiv 2305.11206) — the headline reference in Wolfe's piece; not in `raw/`. Candidate ingest if the data-curation-for-SFT thread accumulates.
- **DPO (Rafailov et al. 2023)** — the post-Wolfe successor to RLHF that has largely replaced PPO-RLHF in 2024–2026. Wolfe's article predates the DPO line by ~3 months; worth flagging for a follow-up "DPO and friends" ingest.
- **A wiki entity stub for LLaMA-2 / Meta-Llama lineage** — would let multiple VLA-line ingests attach cleanly. Defer.
