---
title: "Hugging Face TRL — SFT Trainer documentation"
type: source
url: https://huggingface.co/docs/trl/en/sft_trainer
project_url: https://github.com/huggingface/trl
author: Younes Belkada (initial contributor) + Hugging Face TRL maintainers
affiliation: Hugging Face
published: continuously updated; current docs reflect TRL v1.4.0 (as of 2026-05)
ingested: 2026-05-14
created: 2026-05-14
updated: 2026-05-14
license: Apache 2.0 (TRL library)
tags: [trl, sft, supervised-fine-tuning, hugging-face, llm, vlm, peft, lora, liger-kernel, unsloth, alignment, library-docs]
---

> [!note] Ingest depth
> Source-page metadata + key features gathered from a WebFetch of the current TRL SFT Trainer documentation page. This ingest captures the docs' published feature surface as of TRL v1.4.0 (May 2026); upstream behavior may evolve.

## Summary

**TRL SFT Trainer** — Hugging Face's de-facto **Supervised Fine-Tuning** trainer, distributed as part of the [TRL](https://github.com/huggingface/trl) (Transformer Reinforcement Learning) library. Initially contributed by **Younes Belkada**, now maintained by the Hugging Face TRL team. The trainer is a thin wrapper over Hugging Face Transformers' `Trainer` class that handles SFT-specific concerns: dataset format dispatch (standard / conversational / prompt-completion), tokenization + chat-template application, loss masking (assistant-only / completion-only), and PEFT/LoRA integration.

**Default API** is one-line:

```python
from trl import SFTTrainer
from datasets import load_dataset

trainer = SFTTrainer(
    model="Qwen/Qwen3-0.6B",
    train_dataset=load_dataset("trl-lib/Capybara", split="train"),
)
trainer.train()
```

**Loss:** token-level cross-entropy on the target sequence — `L_SFT(θ) = −Σ_t log p_θ(y_t | y_{<t})`. Padding ignored via `ignore_index = −100`. A label-shift right-by-one yields next-token targets from the input sequence.

## Why it matters to this wiki

- **The companion runnable artifact to [Wolfe's SFT theory survey](wolfe-sft-blog.md).** Wolfe explains *what* SFT is and why it works; this page is *how to actually run an SFT job* in 2026.
- **VLM support out of the box** — relevant to every VLA in the wiki. The docs explicitly cover training Qwen2.5-VL with `SFTTrainer(model="Qwen/Qwen2.5-VL-3B-Instruct", ...)` on the LLaVA-Instruct-Mix dataset. Most VLA fine-tuning recipes ([OpenVLA](../concepts/vla-models.md), [Helix](helix-blog.md), [π0](pi-zero-paper.md) variants, [GR00T](../entities/nvidia-groot.md)) build on this exact pattern, often via a fork.
- **PEFT / LoRA integration** is first-class — `peft_config=LoraConfig()` is the one-line LoRA setup. Critical for fine-tuning 7B+ VLAs on a single consumer GPU, which is the canonical [SIGRobotics-UIUC](../entities/sigrobotics-uiuc.md) / [XLeRobot](../entities/xlerobot.md) / hackathon workflow.
- **Liger Kernel + Unsloth integrations** — Liger Kernel (Triton kernels, 20% throughput / 60% memory) and Unsloth (2× faster, 70% less VRAM) are both supported via flags. These are the standard "fits on a 24 GB consumer card" optimization paths.
- **Tool-calling SFT support** — relevant to the wiki's [LLM agent architecture concept](../concepts/llm-agent-architecture.md) and to the [stretch-ai LLM-agent docs](stretch-ai-llm-agent-docs.md) thread, where the robot's LLM controller calls tools that map to robot capabilities.

## Key feature surface (per docs)

### Dataset format dispatch

`SFTTrainer` accepts four dataset shapes (any of these works without preprocessing):

```python
# Standard language modeling
{"text": "The sky is blue."}

# Conversational language modeling
{"messages": [{"role": "user", "content": "What color is the sky?"},
              {"role": "assistant", "content": "It is blue."}]}

# Standard prompt-completion
{"prompt": "The sky is", "completion": " blue."}

# Conversational prompt-completion
{"prompt": [{"role": "user", "content": "What color is the sky?"}],
 "completion": [{"role": "assistant", "content": "It is blue."}]}
```

For conversational data, the trainer auto-applies the model's chat template. For prompt-completion, loss is computed on the completion only by default (`completion_only_loss=True`).

### Loss masking modes

- **`completion_only_loss=True`** (default for prompt-completion): mask the prompt, train only on the completion. Standard for instruction-tuning recipes.
- **`assistant_only_loss=True`** (conversational): mask user + system turns, train only on the assistant turn. Requires the chat template to include `{% generation %}…{% endgeneration %}` markers (TRL auto-patches for Qwen3 and similar known families).
- Both can be combined for prompt-completion-conversational data.

### Loss variants

- **`loss_type="nll"`** (default): the standard token-level cross-entropy.
- **`loss_type="chunked_nll"`**: memory-efficient variant — `lm_head` projection skips ignored-label tokens, cross-entropy processed in chunks; peak activation memory no longer scales with `vocab_size × seq_len`.
- **`loss_type="dft"`** (Dynamic Fine-Tuning, [arxiv 2508.05629](https://huggingface.co/papers/2508.05629)) — RL-style reward-rectified objective for improved generalization. Newer alternative to plain SFT loss.

### Configuration

`SFTConfig` overrides several Transformers `TrainingArguments` defaults: `logging_steps=10` (vs 500), `gradient_checkpointing=True` (vs False), `bf16=True` (vs `fp16=False`), `learning_rate=2e-5` (vs `5e-5`). Tuned for the typical "fine-tune a 7B model on a single 8×H100 node" recipe.

### Performance / scaling integrations

- **PEFT / LoRA** — `peft_config=LoraConfig()` argument; standard parameter-efficient fine-tuning. Recommended `learning_rate=1e-4` for adapters.
- **Packing** — `packing=True` packs multiple short examples into a single sequence; reduces padding waste, improves throughput.
- **Liger Kernel** — Triton kernels, 20%+ throughput, 60% memory; works with FlashAttention + PyTorch FSDP + DeepSpeed.
- **Unsloth** — fork-style framework for fine-tuning + RL; 2× faster, 70% less VRAM. Compatible with TRL's API.
- **RapidFire AI** — multi-config experimentation engine; runs several SFT configs in parallel on a single GPU.

### VLM (Vision-Language Model) support

```python
trainer = SFTTrainer(
    model="Qwen/Qwen2.5-VL-3B-Instruct",
    args=SFTConfig(max_length=None),  # IMPORTANT: don't truncate, you'll cut image tokens
    train_dataset=load_dataset("trl-lib/llava-instruct-mix", split="train"),
)
trainer.train()
```

The key gotcha called out in the docs: `max_length=None` (never truncate) is mandatory for VLM training, otherwise image tokens get cut and training errors out.

### Tool calling

`SFTTrainer` accepts tool-calling datasets with `tool_calls` / `tool`-role messages and a `tools` column of JSON schemas. Pattern mirrors OpenAI / Anthropic tool-use APIs.

### Logged metrics

Standard: `global_step`, `epoch`, `num_tokens`, `loss`, `entropy`, `mean_token_accuracy`, `learning_rate`, `grad_norm`.

## Entities mentioned

- **[Hugging Face](../entities/hugging-face.md)** — already a wiki entity (4 sources). TRL is one of its alignment-stack libraries (alongside `transformers`, `datasets`, `peft`, `accelerate`).
- **Younes Belkada** — initial TRL/SFT contributor. Not yet a wiki entity.
- **Qwen / Alibaba** — Qwen3 is the default example model in the docs. Not yet a wiki entity.
- **Unsloth (Daniel Han & Michael Han, 2023+)** — fine-tuning framework; integrated with TRL. Not yet a wiki entity.
- **Liger Kernel (LinkedIn, 2024)** — open-source Triton kernels for LLM training. Not yet a wiki entity.
- **RapidFire AI** — experimentation engine. Not yet a wiki entity.

## Concepts touched

- **[SFT (Supervised Fine-Tuning)](wolfe-sft-blog.md)** — Wolfe's theory page is the natural pairing.
- **PEFT / LoRA / adapters** — parameter-efficient fine-tuning. Standard practice in 2026 for any model > 3B params on consumer hardware.
- **Chat templates** — the data-formatting layer that turns conversational data into tokenizable strings with role markers.
- **Vision-language fine-tuning** — the VLM-SFT path is the LLM-side of every VLA recipe.
- **Tool calling** — relevant to [LLM agent architecture](../concepts/llm-agent-architecture.md).

## Curriculum hookup

Strong recommended-reading entry for [Curriculum Module 9 — Vision-Language-Action models](../syntheses/curriculum-09-vla.md), specifically at the "how is a VLA actually trained?" section. The TRL SFTTrainer is what every wiki-tracked VLA's training pipeline either is built on directly or is a fork of.

Also relevant to [Curriculum Module 14 — Capstone](../syntheses/curriculum-14-capstone.md) for the "training a small LLM / VLM end-to-end" path; pairs naturally with [karpathy/nanochat](karpathy-nanochat.md) (which builds the SFT trainer from scratch as one of its stages).

## Position in the Hugging Face alignment stack

```
transformers           — base model architecture + tokenizers + Trainer class
datasets               — data loading + processing
accelerate             — distributed training + mixed precision + FSDP/DeepSpeed
peft                   — LoRA / IA3 / prefix-tuning / etc.
trl                    — RL / preference / SFT training (SFTTrainer lives here)
  ├── SFTTrainer       — SFT (this source page)
  ├── DPOTrainer       — Direct Preference Optimization
  ├── PPOTrainer       — PPO-style RLHF
  ├── GRPOTrainer      — Group-Relative Policy Optimization (DeepSeek-style)
  ├── KTOTrainer       — Kahneman-Tversky Optimization
  └── ORPOTrainer      — Odds-Ratio Preference Optimization
smol-course            — pedagogical companion repo; Chapter 1 covers SFTTrainer
```

The wider TRL family covers the post-SFT stages too — the wiki's natural follow-up ingests for the alignment thread would be DPOTrainer and GRPOTrainer pages.

## Open questions / TBD

- **The TRL `trl/` source code itself** — the library is short enough that a guided code-walk of `trl/trainer/sft_trainer.py` would make a useful pedagogical artifact (analogous to the karpathy/nanoGPT walkthrough). Logged.
- **Hugging Face `smol-course`** — a pedagogical companion repo, Chapter 1 = SFT, Chapter 2 = preference alignment, etc. Worth a follow-up evaluation pass for the curriculum.
- **DPO / GRPO trainer pages** — strong candidates for follow-up ingests once the wiki picks up a preference-tuning / RLHF source.
- **A `concepts/sft.md` page** — would unify Wolfe + this trainer doc + VLA-line papers' fine-tuning sections (already flagged in [wolfe-sft-blog.md](wolfe-sft-blog.md)).
- **The DFT loss paper (arxiv 2508.05629)** referenced in the docs — alternative SFT loss that "rectifies the reward signal." Logged for possible ingest if the SFT-improvements thread accumulates.
