# Capture: https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/
Captured 2026-11-17 via curl; visible text of the page's <article> element. Page metadata: published 2026-10-15, modified 2026-11-09. Images are not included; Figures 1-4 are saved under raw/assets/nemotron-3-5-super-vl/. Key link targets:
  technical report -> https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Super-and-Lightning-Technical-Report.pdf
  usage cookbook -> https://github.com/NVIDIA-NeMo/Nemotron/tree/main/usage-cookbook/Nemotron-3.5-Super-VL
  NIM -> https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/nemotron-3.5-super-vl-120b-a12b
  Hugging Face -> https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4
  Nemotron 3.5 Lightning post -> https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/
  Nemotron 3 Ultra post -> https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/
  Nemotron 3 Nano Omni post -> https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/
  Hermes Bench -> https://portal.nousresearch.com/bench
  LangChain evals -> https://github.com/langchain-ai/deepagents/tree/main/libs/evals
  Dynamo recipes -> https://docs.nvidia.com/dynamo/dev/recipes/nemotron-3-5-super-vl

Agentic AI / Generative AI

English한국어中文

# NVIDIA Nemotron 3.5 Super VL Powers Specialized Agents with Multimodal Reasoning


By Chris Alexiuk and Chintan Patel

Like

Discuss (0)

- L

- T

- F

- R

- E

## AI-Generated Summary

- NVIDIA Nemotron 3.5 Super VL is an open, customizable multimodal model with a 120B-parameter mixture-of-experts architecture that activates 12B parameters per token for agentic workflows.
- The model combines reasoning, instruction following, tool use, and text, image, document, and video understanding in a single model, eliminating the need for separate vision-language models.
- On a single GPU, Nemotron 3.5 Super VL delivers up to 5x higher throughput for agentic tasks compared to other open models in its size category.
- Organizations including Scale AI, Ramp, and AI21 have post-trained the model for specialized workflows, achieving improvements such as 40x lower inference cost, 10x lower latency, and 40% higher accuracy.
- Developers can customize the model using NVIDIA NeMo with supervised fine-tuning, low-rank adaptation, and reinforcement learning on open datasets released on Hugging Face.
- The model uses LiLiCorr speculative decoding, NVFP4 quantization with quantization-aware distillation, multi-token prediction, and context reuse to optimize inference efficiency on platforms including NVIDIA DGX Spark.
### Next Steps
- Read the Nemotron 3.5 technical report for model details.
- Explore the Nemotron 3.5 Super VL usage cookbook on GitHub for customization resources.
- Get started with NVIDIA NIM for optimized deployment.

Powered by NVIDIA Nemotron. AI-generated content may summarize information incompletely. Verify important information. Learn more

Always-on agents are taking on longer, more complex enterprise workflows. A single request can involve reading a document, checking information across sources, following company policy, and calling several tools.

NVIDIA Nemotron 3.5 Super VL is an open, customizable multimodal model for these specialized workflows. Its 120B-parameter mixture-of-experts (MoE) architecture activates 12B parameters per token, balancing model capacity with inference efficiency.

On a single GPU, this model delivers up to 5x higher throughput for agentic tasks compared to other open models in its size category.

Figure 1. Nemotron 3.5 Super VL delivers over 600 TPS on Artificial Analysis Intelligence Index agentic tasks on the Baseten endpoint

The model combines reasoning, instruction following, and tool use with text, image, document, and video understanding. By combining these capabilities into one model, teams can handle text and visual tasks without deploying separate text and vision-language models or passing task context between them.

Developers can post-train Nemotron 3.5 Super VL with NVIDIA NeMo using their own data, tools, policies, and workflows. This post explains how to use that foundation to build specialized enterprise agents and describes the training and inference techniques that power it.

## Why Nemotron 3.5 Super VL for specialized agents?

Agents need to understand both their tasks and operating environments. A customer-service agent must follow company return policies. Research agents connect evidence across sources, while document agents interpret tables, charts, and page layouts.

Nemotron 3.5 Super VL combines reasoning and visual understanding across a range of agent workflows, including:

- Coding: Test and validate code, analyze errors, and recommend fixes.

- Web research: Search across websites, connect information, and verify answers.

- Document intelligence: Extract information from tables, charts, and page layouts to produce summaries and reports.

- Cybersecurity: Identify security vulnerabilities and triage threats to prioritize remediation.

- Video understanding: Extract information for search, content review, and incident analysis.

Within a system of models, Nemotron 3.5 Super VL handles specialized, multistep work that needs reasoning, tool use, and text and visual understanding together. Smaller models, such as NVIDIA Nemotron 3.5 Lightning, handle high-volume text tasks, while frontier models such as NVIDIA Nemotron 3 Ultra tackle complex planning and orchestration.

## Customize Nemotron 3.5 Super VL for domain data, tools, and policies

Specialized agents must learn how an organization works. Domain terminology, tool interfaces, operating procedures, and policy requirements shape how agents complete tasks successfully.

Organizations in industries ranging from cybersecurity and finance to healthcare are post-training Nemotron 3.5 Super VL to outperform frontier models in accuracy and efficiency across their production workflows. For example:

- Scale AI, an AI data and technology provider, post-trained Nemotron 3.5 Super VL for automated vendor credit processing at Skydance Corporation, a media and entertainment company. Inference cost for this workload will decrease by 40x and latency by 5x.

- Ramp, a financial operations platform provider, is converting receipt images into structured JSON containing merchant information, dates, and payment data. Ramp expects up to 50% higher throughput and 10x lower latency.

- AI21 and Alice post-trained Nemotron 3.5 Super VL for threat intelligence and vulnerability analysis, improving accuracy by 41%.

Figure 2. Post-trained Nemotron 3.5 Super VL achieves leading performance for specialized tasks across industries

Teams can use NVIDIA NeMo open libraries to post-train models to meet these requirements. Developers can use NVIDIA NeMo AutoModel for supervised fine-tuning (SFT) and low-rank adaptation (LoRA) to teach domain-specific behavior. Reinforcement learning (RL) improves performance in agentic environments that reflect organizational workflows.

Alongside Nemotron 3.5 Super VL, NVIDIA is releasing open datasets on Hugging Face. These include agentic tool-use and conversational data, finance reasoning and tool-calling datasets, instruction-following and chat data, long-context transduction and translation data, fairness data, and 40 vision-language datasets. These datasets can supplement proprietary data for SFT and RL.

For multimodal data, start with NeMo Data Designer resources for chart question answering and long-document understanding. Explore NVIDIA NeMo RL and NVIDIA NeMo Gym for RL and environment-based evaluation.

Organizations can adapt and deploy the model’s open weights in supported local, data center, or cloud environments to meet their infrastructure and data requirements. For customization resources, see the Nemotron 3.5 Super VL usage cookbook on GitHub.

## Combine text and visual understanding in one workflow

Nemotron 3.5 Super VL combines text, image, document, and video understanding with reasoning and instruction following to answer questions across these inputs.

Its visual training covers charts, tables, optical character recognition (OCR), multipage documents, and video understanding. A two-stage SFT pipeline trains the language and vision components, combining visual evidence with reasoning, chat, safety, long-context data, and agent trajectories.

For document intelligence, the same model can interpret a chart, connect it with a table elsewhere in a document, and summarize both. Developers can tailor the workflow to their own documents and evaluation criteria.

Diverse training data generated with NeMo Data Designer helped the model better understand complex charts. On CharXiv, a chart-reasoning benchmark, the model scored 80.8%, compared with 63% for Nemotron 3 Nano Omni. With Python code interpretation, it reached 84%. For the approach and lessons learned, read the chart-understanding deep dive and the open-source chart question-answering pipeline.

This model was built with support and expertise from Nemotron Coalition organizations. For instance, high-quality datasets from Perplexity helped improve and streamline the model’s mid-training. Environments from Prime Intellect enabled building better teacher models.

Nemotron 3.5 Super VL is also one of the top open models on the OCRBench v2 leaderboard.

## Accuracy and efficiency across agent tasks

Evaluations of Nemotron 3.5 Super VL span Hermes, LangChain, OpenClaw, OpenCode, Pi, Codex, and Claude. In addition to coding tasks, agent harness providers use their own evaluations to test a wide range of agent tasks. On Hermes Bench and LangChain behavioral evaluations, Nemotron 3.5 Super VL scores higher than Nemotron 3 Ultra.

| Model | Hermes Bench | LangChain Evals
| Nemotron 3 Ultra | 56.33% | 84.3%
| Nemotron 3.5 Super VL | 63.44% | 87.05%
Table 1. Nemotron 3.5 Super VL scores higher than Nemotron 3 Ultra on Hermes Bench and LangChain evaluations

For always-on agents, efficiency determines how much work a deployment can complete. Throughput, token usage, tool calls, and the steps needed to reach a correct result all affect task completion time.

Figure 3. Nemotron 3.5 Super VL uses higher throughput and token efficiency to deliver 4x faster task completion

This model was also optimized to run locally on NVIDIA DGX Spark. An independent evaluation by EXO Labs placed Nemotron 3.5 Super VL on the Pareto frontier for accuracy and task completion time.

Figure 4. Nemotron 3.5 Super VL balances accuracy and speed for agent tasks on DGX Spark

## Nemotron 3.5 Super VL under the hood

The model builds on a strong foundation and uses a hybrid architecture, speculative decoding, context reuse, and mixed precision to reduce inference work across repeated agent calls.

### Building a strong base model

Nemotron 3.5 Super VL was distilled from Nemotron 3 Ultra. Ultra’s coding capabilities, combined with the SkewReverse loss used during distillation, helped improve coding accuracy.

During post-training, multi-teacher on-policy distillation (MOPD) combines guidance from specialized teachers across text and vision. The model generates responses, and the teachers score them for video reasoning and tracking, vision tool use, and alignment.

Additional training on examples of agent actions, code repositories, and software engineering tasks improved the model’s performance on agent tasks. Nemotron 3.5 Super VL outperforms Nemotron 3 Super on SWE-bench and Terminal-Bench across multiple evaluation setups.

Continued pretraining with high-quality natural and synthetic data improved Indic-language capabilities and contributed to higher overall scores after post-training. This stage added 10B Indic tokens, drawn from a 12-language subset of Nemotron-pretraining-Indic-v1 and natural Indic text.

NVIDIA is releasing the full dataset, which contains about 2.8T tokens across 22 Indian languages and was developed with IIT Madras and its AI4Bharat lab. The following results are based on the post-trained Nemotron 3.5 Super VL.

Figure 5. Nemotron 3.5 Super VL delivers leading accuracy on Indic benchmarks, thanks to specialized Indic data

Developers can use NeMo to build on this foundation and customize Nemotron 3.5 Super VL for their applications, adapting its reasoning and agentic capabilities to their data, tools, and workflows.

### LiLiCorr: An open speculative decoding technique

LiLiCorr improves parallel speculative decoding by jointly evaluating token candidates across an entire draft, capturing dependencies that independent token predictions miss. A lightweight network computes compatibility scores in a single pass to produce more coherent drafts, leaving only a low-cost, sequential final selection step.

On DGX Spark, LiLiCorr is the recommended drafter for low-latency inference with Nemotron 3.5 Super VL. It delivers up to 2.3x faster token generation than decoding without speculation.

### NVFP4 and mixed precision

The model uses NVIDIA Model Optimizer for post-training quantization and quantization-aware distillation (QAD). The NVFP4 recipe uses 4-bit weights and activations on the NVIDIA Blackwell architecture. The same checkpoint runs on non-Blackwell platforms with 4-bit weights and 16-bit activations. Precision is selected separately for sensitive components.

NVFP4 makes the model smaller, and QAD helps it retain its accuracy at lower precision. During QAD, the quantized model learns to match the outputs of the original BF16 model, which closes the accuracy gap that quantization introduces. QAD also supports storing the key-value (KV) cache in NVFP4 instead of FP8 while still meeting accuracy targets. Because QAD happens during training, it adds no inference overhead.

### Multi-token prediction

Multi-token prediction (MTP) gives Nemotron 3.5 Super VL an internal drafter that proposes several tokens for the main model to verify in one forward pass. Accepting multiple tokens at once reduces the number of compute-intensive verification steps needed to generate a response.

A dedicated MTP-boosting training phase further aligned the drafter with the final model.

### Context reuse across agent turns

Agents repeatedly pass system instructions, tool definitions, and conversation history back to the model. Prefix caching reuses computation from those shared inputs.

The model’s serving optimizations preserve both attention caches and Mamba recurrent states. Additional Mamba checkpoints reduce the replay needed to recover inputs for speculative decoding, while internal checkpointing avoids extra model passes during prompt processing.

## Simplify production deployment with NVIDIA NIM and NVIDIA Dynamo

NVIDIA NIM packages models with optimized inference engines, validated configurations, and standard APIs for cloud and data center deployment. NIM receives ongoing security, feature, and performance updates. Enterprise support is available through NVIDIA AI Enterprise. Get started with NIM.

NVIDIA Dynamo supports distributed inference optimizations to increase throughput and reduce latency, including KV-cache-aware routing, KV cache management, and disaggregated serving.

On 16 NVIDIA B200 GPUs at 50 tokens per second per user, KV-aware routing with session affinity and KV cache offload serves up to 8x as many users while reducing first-token latency by 85%. Get started with the Dynamo deployment recipes.

Figure 6. NVIDIA Dynamo serves 8x as many users and reduces first-token latency by 85% at the same per-user token rate

## Get started with Nemotron 3.5 Super VL

Build specialized agents with multimodal reasoning and tool use. Customize the model for specialized workflows, then deploy it in a supported environment.

The release includes base, post-trained, and NVFP4-quantized checkpoints with training recipes, data, and reinforcement-learning environments.

See the Nemotron 3.5 technical report for model details and Hugging Face or ModelScope for deployment instructions. For hosted model access, see OpenRouter.

## Partner ecosystem

Partners support customization and deployment of Nemotron 3.5 Super VL for domain-specific workflows.

View partners:

Post-training

- AfterQuery

- AgileRL

- AI21

- Alice

- Applied Compute

- Baseten

- Bespoke Labs

- Databricks

- distil labs

- Fastino Labs

- Fireworks AI

- Handshake

- Mercor

- Mindbeam

- ms-swift

- Multiverse Computing

- Prime Intellect

- Reasonable

- River AI

- Scale AI

- Thinking Machines Lab (Tinker)

- TNG

- Trajectory

Inference software

- Actual Computer

- Canonical

- Exo

- LM Studio

- Ollama

- SGLang

- Unsloth

- vLLM

Harnesses and agent frameworks

- Aible

- Cline

- Hermes Agent

- Kilo Code

- LangChain

- LM Studio Bionic

- OpenClaw

- OpenCode

- OpenHands

- Pi

Cloud platforms

- Amazon SageMaker JumpStart

- Google Cloud Gemini Enterprise Agent Platform

- Microsoft Foundry

- OCI Enterprise AI

Global systems integrators

- HCLTech

- Infosys

- Tata Consultancy Services

- Thoughtworks

Hardware and infrastructure

- Dell

- HPE Services

- Red Hat

AI natives

- APMIC

- Cognition

- Daily

- Domyn

- Dream

- Eon

- Factory AI

- H Company

- Harvey

- Inflection AI

- Navan

- NextLM

- NYB.AI

- Orca Security

- Perplexity

- Ramp

- Terray

- Two Delta

- Versos

Hosted inference service providers

- Baseten

- Bitdeer AI

- BLACKBOX.AI

- CoreWeave

- Crusoe

- DeepInfra

- DigitalOcean

- fal.ai

- Fireworks AI

- FriendliAI

- GMI Cloud

- Lambda

- Modal

- Nebius

- Nscale

- Together AI

Discuss (0)

Like

## Tags

Agentic AI / Generative AI | Developer Tools & Techniques | General | NeMo | Nemotron | NIM | Intermediate Technical | Deep dive | AI Agent | featured | NVFP4

##
About the Authors

About Chris Alexiuk

Chris Alexiuk is a deep learning developer advocate at NVIDIA, working on creating technical assets that help developers use the incredible suite of AI tools available at NVIDIA. Chris comes from a machine learning and data science background, and he is obsessed with everything and anything about large language models.

View all posts by Chris Alexiuk

About Chintan Patel

Chintan Patel is a senior product manager at NVIDIA focused on bringing GPU-accelerated solutions to the HPC community. He leads the management and offering of the HPC application containers on the NVIDIA GPU Cloud registry. Prior to NVIDIA, he held product management, marketing and engineering positions at Micrel, Inc. He holds an MBA from Santa Clara University and a bachelor's degree in electrical engineering and computer science from UC Berkeley.

View all posts by Chintan Patel

