---
title: "Karpathy — Software 3.0 and the history of the Transformer (TreeHacks keynote + Stanford CS25 lecture, re-uploaded compilation)"
type: source
url: https://www.youtube.com/watch?v=EsQ_bmXKA4A
author: Andrej Karpathy (speaker); uploaded by the third-party channel TechXOps
venue: "Stanford (hackathon keynote + CS25 guest lecture), early 2023; this compilation re-uploaded 2026-08-19"
published: 2026-08-19 (re-upload); underlying talks early 2023
ingested: 2026-08-30
format: video (68 min 30 s), auto-generated captions
tags: [karpathy, software-2.0, software-3.0, data-engine, transformer, attention, history, prompting, in-context-learning, message-passing, secondary-source, compilation]
---

> [!warning] Provenance — this is a third-party compilation, not a primary upload
> The channel is **TechXOps**, not Karpathy. The 68½-minute video is a **stitch of at least two separate 2023 Karpathy appearances**, cut together without on-screen attribution:
>
> | Span | Content | Identification |
> |---|---|---|
> | 00:00–~22:19 | "Software 1.0 / 2.0 / 3.0", prompting, "the hottest new programming language is English"; ends with applause and a host's thank-you | A **hackathon keynote at Stanford**. He says he *"came back to OpenAI as of 1 week ago"* (he rejoined in Feb 2023) and refers to Bing Sydney as having "taken over the internet over the last few days" — dating it to **mid-February 2023**. Consistent with TreeHacks 2023, though the event is never named on the audio. |
> | ~22:19–~24:29 | Scratchpad / external memory / domain-specific models / mixture of experts | A **spliced fragment**, cutting in mid-sentence. Source not identifiable from audio alone. |
> | ~24:21–1:08:28 | *"I live very nearby, so I got the invites to come to class… I want to talk about transformers"* — transformer history and mechanics, with student Q&A | A **Stanford CS25 (Transformers United) guest lecture**. |
>
> **Consequence for the wiki:** cite this page for **Karpathy's framing and the Bahdanau anecdote**, which appear nowhere else here. Do **not** cite it for any claim about the underlying papers — [NPLM](bengio2003-neural-probabilistic-language-model.md), [seq2seq](sutskever2014-sequence-to-sequence-learning.md), [Bahdanau](bahdanau2014-neural-machine-translation-align-translate.md) and [Vaswani](attention-is-all-you-need.md) are all ingested as primaries, and one of his paraphrases is already wrong (see *Corrections* below). The original uploads should replace this page if located.

> [!note] Ingest depth
> Auto-generated English captions pulled with `yt-dlp` and de-duplicated into a 2,325-line timestamped transcript; read in full. Slides are not visible in the transcript, so figure content is inferred from narration. **Auto-captions garble proper nouns** — corrections noted inline.

## Summary

Two talks that turn out to be halves of one argument. The first is Karpathy's **Software 1.0 / 2.0 / 3.0** taxonomy: programming has moved from *designing the algorithm* (70 years) to *designing the dataset* (neural networks, the "data engine") to *designing the prompt*. The second is a historical walk through **where the Transformer came from** — the same 2003 → 2013 → 2014 → 2017 lineage this wiki has just ingested as primaries — plus his own framing of attention as **data-dependent message passing on a directed graph**.

Its unique value here is a **piece of oral history**: Karpathy emailed [Dzmitry Bahdanau](../entities/dzmitry-bahdanau.md) asking where soft attention came from, and reads the reply on stage.

## Part 1 — Software 1.0 / 2.0 / 3.0

| Paradigm | You design… | Artifact |
|---|---|---|
| **Software 1.0** | the algorithm | source code, ~70 years, "unchanged on a high level" |
| **Software 2.0** | the **dataset** | neural network **weights** — "you can't write it by hand; it comes out of the optimization" |
| **Software 3.0** | the **prompt** | a conditioned LLM |

He is explicit that these **layer rather than replace**: "you actually still need a ton of 1.0 code to compile your software 2.0."

### The data engine (~05:26) — the part that matters most to this wiki

Described as "about 5 years of my life at Tesla":

```
dataset → train a net → deploy → telemetry & monitoring
   ↑                                      ↓
   └── label ←── collect the data the network finds troubling
              (some to test sets, some back into training)
```

> [!note] Why this belongs in a robotics wiki
> This loop is the reference design behind every data-collection programme the wiki tracks — [Figure's Index](../entities/figure-index.md), [DROID](../entities/droid.md), the whole [crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md) thread. The load-bearing step is the one that is hardest to copy: **"collect more data that the network finds troubling."** The engine only works if deployment telemetry can *identify* failures and route them back.
>
> That is precisely the step a crowdsourced or teleop-harvested robot corpus does not have. Scraping more hours of human video is the *volume* half of the data engine with the *targeting* half missing — and targeting is what made it work at Tesla. Worth holding against any claim in this wiki that a large robot dataset constitutes a data engine; mostly they are datasets.

### Prompting as programming (~07:00–19:45)

Worked examples, all from early 2023: few-shot Q&A conditioning from the GPT-3 paper; chain-of-thought ("let's think step by step," **17% → 78.7%**, and the stronger "let's work this out in a step by step way to be sure we have the right answer" at **82%**); "Building a virtual machine inside ChatGPT" (a hallucinated filesystem that stays self-consistent across `touch` / `echo` / `ls` / `cat`, and a `ping bbc.com` returning a **fabricated IP with plausible 24.9 ms latency**); a smart-home assistant specified entirely in English that emits JSON commands; an app whose **entire backend is an LLM** mutating JSON state.

His framing: earlier nets were "a special purpose computer designed for a specific task"; a GPT is "a **general purpose computer**, reconfigurable at runtime to run natural language programs." And, on why prompt phrasing matters so much: the model "is imitating the average answer it can find on the internet," so you must "narrow in on the slice of the prediction that you want."

> [!note] Dated in a useful way
> Much of Part 1 is a period piece — "prompt engineer" as a novel job title, Sydney's leaked prompt as current events, `text-davinci` era behaviour. The *taxonomy* aged well and the *tactics* did not, and having both in one artifact is a good calibration exercise on how fast this layer moves. See [chain-of-thought](../concepts/learning/chain-of-thought.md).

## Part 2 — Where the Transformer came from

### Architectural convergence (~30:37)

A vivid account of pre-2012 computer vision: papers spending "three pages describing a zoo, a kitchen sink of different feature descriptors" — sparse SIFT histograms, SSIMs, color histograms, textons, tiny images, geometry-specific histograms — all extracted, concatenated, and fed to an SVM. "You're collecting code from everywhere and running it and it was a total nightmare. On top of that, it also didn't work." Misclassifications were shrugged off; "today you would be looking for a bug."

Worse, each subfield had **its own vocabulary** — an NLP paper was unreadable to a vision person. Then two convergences:

1. **2012 (AlexNet)** — scale a large net on a large dataset and it works; the *toolkit* becomes shared across vision, NLP, speech, translation, RL.
2. **2017 (Transformer)** — the *architecture itself* converges. "You can just copy-paste this architecture and use it everywhere. What's changing is the details of the data and the chunking of the data and how you feed them."

He offers a speculation, flagged as such: the cortex is "very homogeneous and uniform" across auditory, visual and everything else, so maybe the convergence is toward "some kind of a uniform powerful learning algorithm."

### The lineage he walks

**2003 → 2014 seq2seq → the encoder bottleneck → 2014 attention → 2017 Transformer.** Every step is now a primary source page in this wiki; see [From n-grams to attention](../syntheses/sequence-models/language-model-to-transformer-lineage.md).

His statement of the bottleneck (~35:56) is the crisp one: "this entire English sentence that we are trying to condition on is packed into a single vector that goes from the encoder to the decoder… this is just too much information to potentially retain in a single vector, and that didn't seem correct."

### The Bahdanau email (~37:42) — the reason to keep this page

Karpathy emailed the first author of [*Neural Machine Translation by Jointly Learning to Align and Translate*](bahdanau2014-neural-machine-translation-align-translate.md) asking where soft attention came from, and got back "this like massive email." The excerpt he reads:

- Bahdanau was looking for a way to avoid the encoder–decoder bottleneck, and had earlier ideas "about cursors that traverse the sequences" that **did not work out**.
- Then: *"one day I had this thought that it would be nice to enable the decoder RNN to learn to search where to put the cursor in the source sequence. This was certainly inspired by translation exercises that learning English in my middle school involved. Your gaze shifts back and forth between source and target sequence as you translate."*
- *"I expressed the soft search as softmax and then weighted averaging of the [hidden] states… to my great excitement this worked from the very first try."*
- **The name "attention" was Yoshua Bengio's**, added on one of the final passes over the paper. The mechanism's working name was **RNNsearch** — which is exactly what the models are called in [the paper's Table 1](bahdanau2014-neural-machine-translation-align-translate.md). Karpathy: "maybe *Attention Is All You Need* would have been called RNNsearch."

Three things worth extracting. The mechanism came from **introspection on a human procedure** (a non-native speaker's gaze shifting during translation homework) rather than from theory. It **worked on the first try**, which is rare enough to be worth recording. And the [naming](../entities/yoshua-bengio.md) was a late editorial choice by the senior author — the same person who, eleven years earlier, was senior author of [the paper that created the embedding table](bengio2003-neural-probabilistic-language-model.md).

### Why the Transformer stuck (~43:37)

Karpathy's three-property argument — it simultaneously optimizes properties that usually trade off:

1. **Expressive** in the forward pass — can implement interesting functions, possibly including meta-learning.
2. **Optimizable** — residual connections, layer norms.
3. **Efficient** — "if you look at the computational graph, [it] is a shallow, wide network, which is perfect to take advantage of the parallelism of GPUs… designed very deliberately to run efficiently on GPUs," reasoning "backwards from the constraints of the hardware."

He calls the paper "a mix of multiple things at the same time… combined in a very unique way" that "achieved a very good local minimum in the architecture space" — against the usual incremental single-change paper.

**What has and has not survived**, as of the talk: the **4× MLP expansion factor** stuck; the layer-norm reshuffle to **pre-norm** is "the only thing to my knowledge that stuck" as a change; positional encodings moved to **rotary and relative** schemes. Otherwise "the GPTs and everything else that you're seeing today is basically the 2017 architecture." This corroborates the [attention source page](attention-is-all-you-need.md)'s pre-norm and RoPE notes from an independent direction.

### Attention as message passing (~44:50)

The framing that makes this lecture worth watching even given the primaries. A Transformer interleaves two phases:

- **Communication** — multi-head attention: *data-dependent message passing on a directed graph.*
- **Computation** — the MLP, applied to each node independently.

Forget translation. You have a directed graph; each node stores a vector and emits three linear projections of it:

| Projection | Reading |
|---|---|
| **Query** | "what are the things that I'm looking for" |
| **Key** | "what are the things that I have" |
| **Value** | "what I will communicate" |

Each node broadcasts its key; the receiving node dot-products its query against them to get affinities, softmaxes to a distribution, and takes a **weighted sum of values** as its update. "This happens in every head in parallel, and then in every layer in series, with different weights each time."

The architecture variants then become **graph connectivity**: encoder tokens are **fully connected**; decoder tokens are causally masked, giving "this triangular structure of the directed graph," plus full connection to the encoder's top-layer states for cross-attention.

### Transformers eat every modality (~24:39)

ViT ("you take an image and you chop it up into little squares… which is kind of ridiculous"), Whisper ("a copy-paste transformer" over mel-spectrogram slices), **Decision Transformer** ("take your states, actions, and reward… and you just pretend it's a language"), AlphaFold.

The **Tesla sensor-fusion argument** is the most directly transferable part:

> With a ConvNet, if you have radar, map information, vehicle type, or audio to add — "how do you feed information into a ConvNet? Where do you feed it in? Do you concatenate it? Do you add it? At what stage?" With a transformer: "you take whatever you want, you chop it up into pieces, and you feed it in with the set of what you had before, and you let the self-attention figure out how it should communicate. And that actually frankly works."

Each modality gets a **learned modality-embedding token** — "these radar tokens are reflected different in the representation, and it's learnable by gradient descent" — which is [distributed representations](../concepts/learning/distributed-representations.md) again, with sensors as the alphabet, and is structurally the same trick as [soft-prompt cross-embodiment conditioning](../concepts/learning/soft-prompt-cross-embodiment.md). His summary: attention "frees neural nets from this version of Euclidean space… in attention, everything is just sets."

### [Inductive bias](../concepts/learning/inductive-bias.md) versus data scale (~29:19)

Asked about positional encodings: "if you have enough data, usually trying to mess with it is a bad thing… trying to enter knowledge when you have enough knowledge in the data set itself is not usually productive. If you have infinite data then you actually want to encode less and less. If you have very little data then actually you do want to encode some biases, and maybe convolutions are a good idea because you have this bias coming from the filters."

Independent restatement of the [ViT paper](vit-paper.md)'s central claim, and directly relevant to the wiki's recurring small-robot-dataset problem: **at robot-data scale, inductive bias is probably still worth paying for.**

### In-context learning (~41:20)

On GPT-3: "I would have said something like *Transformers are capable of in-context learning*, or meta-learning. That's what makes them really special." He distinguishes the **outer loop** (SGD over weights) from the **inner loop** (learning in the activations while reading the prompt), and gestures at the argument that a residual stack structurally resembles iterated gradient updates — "forward pass, backward pass, and update… well, that looks like a resnet. Transformer is a resnet." Flagged by him as "much more hand-wavy."

## Corrections to the talk

> [!warning] Karpathy's NPLM paraphrase is wrong on a detail
> At ~34:57 he describes [Bengio et al. 2003](bengio2003-neural-probabilistic-language-model.md) as taking "three words and predicted the probability that you should put the fourth word in a sequence." The paper's models use **`n` = 5 on Brown (four words of context) and `n` = 6 on AP News (five words)**; `n = 3` appears only as the MLP7/MLP8 ablation. The point he is making is unaffected, but the wiki cites the primary for that claim.

**Caption garbles** (auto-generated captions mangle proper nouns):
- *"Osindero and colleagues"* (~32:39) for the 2012 scaling result — this is **Krizhevsky, Sutskever & Hinton (AlexNet)**.
- *"Dmitri"* / *"Dimitri"* for **Dzmitry Bahdanau**; *"min GPT"* for **minGPT**; *"P-Tron"* for **perceptron**; *"metal learning"* for **meta-learning**.
- *"the raw operator"* (~42:52), a paper said to implement ridge regression on top of it — **not identifiable from the captions**; likely a garble, and deliberately not guessed at here.

## Entities mentioned

- **[Andrej Karpathy](../entities/andrej-karpathy.md)** — speaker.
- **[Dzmitry Bahdanau](../entities/dzmitry-bahdanau.md)** — the email correspondent; the origin story of attention.
- **[Yoshua Bengio](../entities/yoshua-bengio.md)** — named as the person who chose the word "attention."
- **[Ilya Sutskever](../entities/ilya-sutskever.md)** — via the seq2seq segment (and, uncredited in the captions, AlexNet).
- Riley Goodside — named as "one of the first" staff prompt engineers, then at Scale.
- OpenAI, Tesla, Microsoft (Bing Sydney), Stanford.

## Concepts touched

- **Software 2.0 / the data engine** — bears on [crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md).
- **[Chain-of-thought](../concepts/learning/chain-of-thought.md)** — the 17% → 78.7% → 82% prompt sequence.
- **[Distributed representations](../concepts/learning/distributed-representations.md)** — learned modality tokens for sensor fusion.
- **[Soft-prompt cross-embodiment conditioning](../concepts/learning/soft-prompt-cross-embodiment.md)** — same trick, robot embodiments as the alphabet.
- **[VLA models](../concepts/learning/vla-models.md)** — "chop everything up and throw it in the set" is the design argument underneath multimodal robot trunks.
- **[Inductive bias](../concepts/learning/inductive-bias.md)** — the data-scale heuristic, and "in attention, everything is just sets."
- **In-context learning**, **attention as message passing**.

## Curriculum hookup

Best companion viewing for **[Module 3](../syntheses/curriculum/curriculum-03-attention-and-transformers.md)**. The **message-passing framing** (§44:50) is a genuinely different presentation from the module's matrix-algebra one and is worth watching *after* the equations — Q/K/V as "what I'm looking for / what I have / what I'll communicate" is the fastest route to intuition for anyone who has met graph neural networks.

## Open questions / TBD

- **Locate and ingest the two originals**, replacing this compilation. The CS25 lecture in particular is on Stanford's own channel.
- **Whether "the data engine needs a failure-targeting signal" is stated anywhere citable** — it is the load-bearing critique of robot data-scaling claims in this wiki, and currently rests on one narrated Tesla anecdote.
- **AlexNet, GPT-3, Decision Transformer, ViT-as-Whisper** — of these only [ViT](vit-paper.md) is ingested. Decision Transformer is the most wiki-relevant gap (RL as sequence modelling).
