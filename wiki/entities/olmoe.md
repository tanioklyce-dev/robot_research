---
title: OLMoE (Open Mixture-of-Experts LM)
type: entity
subtype: llm
created: 2026-07-24
updated: 2026-07-24
sources: 4
tags: [olmoe, mixture-of-experts, open-source-llm, language-model, ai2, sparse-moe]
---

# OLMoE (Open Mixture-of-Experts LM)

**OLMoE** is the **[Mixture-of-Experts](../concepts/learning/mixture-of-experts.md)**
member of the [Allen Institute for AI](ai2.md)'s fully-open
[OLMo](olmo.md) family: a **sparse MoE** language model with **7B total parameters
but ~1B active per token** ([Muennighoff et al. 2024](../sources/olmoe-paper.md)).
It gives ~1B-dense inference cost at well-above-1B quality, and it is the backbone
of Molmo's **MolmoE-1B** variant.

## Key facts

- **OLMoE-1B-7B:** 7B total / **1B active**; **64 experts per layer, top-8**
  activated (fine-grained experts); pretrained on **5T tokens**; + an Instruct
  variant.
- **Beats its weight class:** outperforms models with similar active params and
  even larger ones — **Llama2-13B-Chat**, **DeepSeekMoE-16B**.
- **Fully open:** weights + data + code + logs (Apache 2.0 / ODC-BY) — same
  open-everything stance as [OLMo](olmo.md).
- **Doubles as an MoE cookbook:** its ablations (granular experts, dropless
  routing, shared-experts-ineffective, upcycling-limited) are the wiki's clearest
  open [MoE](../concepts/learning/mixture-of-experts.md) design reference.

## Why it matters in this wiki

OLMoE is the **open, inspectable MoE** — the counterpart to the dense
[OLMo](olmo.md) from the same lab, so the two together isolate "what does sparsity
buy?" It's also a [Molmo](molmo.md) backbone (MolmoE-1B), extending the open
VLM/VLA stack to the sparse regime.

## Related

- [OLMo](olmo.md) — the dense sibling family.
- [Mixture-of-Experts](../concepts/learning/mixture-of-experts.md) — the concept OLMoE instantiates openly.
- [Molmo](molmo.md) — MolmoE-1B uses OLMoE as backbone.
- [Ai2](ai2.md) — the lab.

## Mentioned in

- [OLMoE paper (Muennighoff et al. 2024)](../sources/olmoe-paper.md) — the primary source.
- [Molmo and PixMo paper (Deitke et al. 2024)](../sources/molmo-pixmo-paper.md) — OLMoE as the MolmoE-1B backbone.
