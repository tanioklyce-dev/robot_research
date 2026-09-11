---
source_url: https://unigen-x.github.io/unifolm-wla.github.io/
collected: 2026-09-11
published: 2026-09-11
author: Unitree Robotics
companion_urls:
  - https://github.com/unitreerobotics/unifolm-wla (README, main @ 2026-09-11)
  - https://huggingface.co/unitreerobotics/UnifoLM-ER-1 (model card)
  - https://huggingface.co/unitreerobotics/UnifoLM-ER-Flow (model card)
  - https://huggingface.co/collections/unitreerobotics/unifolm-wla-10
  - https://www.youtube.com/watch?v=GHySQMMrIa4 (launch video)
license: CC BY-NC-SA 4.0 (repo LICENSE and both HF model LICENSE files)
note: Project page is JS-rendered; text below is a tag-stripped capture. Videos, animated diagrams and the interactive benchmark table are not reproduced; the table is taken verbatim from the UnifoLM-ER-1 model card, which carries the same numbers.
---

# UnifoLM-WLA-1.0 — project page (tag-stripped capture)

UnifoLM-WLA-1.0
ER Model
WLA Model
Robot Tests
文
中文
☾
Dark
General-Purpose Humanoid Robot Foundation Model
UnifoLM-WLA-1.0
One Model Drives All, Whole-Body Coordination
Code
Models
Datasets
UnifoLM-WLA-1.0 is Unitree Robotics' comprehensively upgraded, next-generation general-purpose humanoid robot foundation model with 6B parameters. Built on large-scale general multimodal perception and understanding data and interaction-centric world modeling, it substantially advances spatial perception and understanding, achieving leading results across multiple embodied reasoning benchmarks. Trained on approximately 2,500 hours of high-quality real-robot data, a single model coordinates 64 tasks spanning desktop manipulation and whole-body manipulation. It supports two-finger grippers and multiple five-finger dexterous hands, with strong generalization across tasks and end effectors.
6B
VLA parameters
5M+
ER samples
≈2,500h
Robot data
ER Model · Embodied Reasoner
Understand the World,
Connect with Action.
A unified multimodal model brings together embodied reasoning, future dynamic-region prediction, and discrete action learning to jointly strengthen spatial perception, interaction prediction, and action generation, providing a unified vision–language–action representation for subsequent WLA training.
Embodied Reasoning
Across 16 multimodal perception and understanding benchmarks, UnifoLM-ER-1 leads open-source models on seven and delivers overall performance comparable to leading proprietary models. Built on Qwen3-VL-4B, UnifoLM-ER-1 is trained on more than 5 million samples spanning image point prediction, object detection, multi-image reasoning, 2D trajectory prediction, 3D object detection, and multi-image spatial question answering. These data are co-trained with general image–text data, preserving broad vision-language capabilities while substantially improving spatial understanding and reasoning in embodied environments.
Training mix
Point Prediction
Object Detection
Multi-image Reasoning
2D Trajectory
3D Detection
Spatial QA
General VLM Data
 -->
Benchmark results
Model
Open Source
Spatial Understanding
Multimodal Understanding
RoboVQA
Ego-Plan2
RefSpatial-
Bench
Where2Place
Pixmo-Point
BLINK
CV-Bench
EmbSpatial
RoboSpatial
SAT
VSI-Bench
VSR
ERQA
RealWorld
QA
MME
MMMU_VAL
UnifoLM-ER-1-4B
Yes
62.4
55.1
61.7
82.0
73.8
93.4
†
88.6
88.9
73.1
76.0
54.2
88.1
50.0
69.8
2223.3
54.7
RoboBrain2.0-7B
*
Yes
30.0
33.23
42.2
63.6
54.7
83.9
85.7
76.3
54.2
75.3
36.1
84.0
/
69.4
2057.4
44.4
Robix-7B
*
No
63.6
/
/
41.9
29.5
87.6
86.5
77.4
/
71.1
44.6
83.3
42.5
70.7
2332.8
/
Pelican-7B
*
Yes
31.8
33.7
22.3
57.3
20.4
/
79.4
73.2
57.5
52.0
52.8
82.2
39.8
69.3
2141.9
51.1
Cosmos-R1-7B
*
Yes
38.8
26.0
5.6
2.9
8.2
/
76.7
68.9
42.4
82.7
25.4
82.4
/
67.6
2157.4
37.4
Cosmos3-Super-64B
*
Yes
/
/
57.0
71.0
/
90.3
†
88.0
/
70.0
/
60.9
/
51.2
/
/
/
Qwen3-VL-4B
*
Yes
47.7
40.7
46.6
63.0
48.3
85.0
†
85.1
79.6
61.7
68.7
59.3
81.6
41.3
71.0
2325.2
57.8
Qwen3-VL-8B
*
Yes
43.3
49.7
54.2
61.9
51.0
73.8
†
86.2
78.5
66.9
67.3
59.4
83.2
45.8
70.6
2412.5
62.3
Embodied-R1-3B
*
Yes
51.8
26.5
39.7
69.5
49.4
78.5
†
82.7
67.4
47.4
76.3
26.6
/
35.2
/
/
/
Embodied-R1.5-8B
*
Yes
61.0
53.8
54.2
74.0
64.8
83.0
†
86.9
78.1
69.7
74.7
56.1
/
46.0
/
/
/
Molmo2-ER-4B
*
Yes
/
/
52.5
54.0
/
85.7
†
87.8
78.8
/
78.0
74.5
/
46.8
/
/
/
Hy-Embodied-VLM-1.0
30B-A3B
*
Yes
/
49.6
53.4
65.0
64.6
87.3
†
89.7
82.7
69.4
78.0
/
/
60.8
/
/
/
MiMo-Emb-7B
*
Yes
62.0
43.0
48.0
63.6
42.35
81.3
88.2
76.2
61.7
78.6
48.5
79.0
46.7
66.3
2320.8
26.4
Thinker-4B
*
Yes
62.7
63.7
61.0
72.0
57.4
84.6
86.3
80.2
70.8
72.7
65.4
81.5
/
71.9
2323.4
46.2
GenieReasoner-3B
*
No
/
/
/
/
/
74.8
83.9
70.7
/
/
/
/
/
/
/
/
 -->
Wall-OSS-0.5-3B
*
Yes
/
/
/
15.0
/
/
/
/
/
/
/
/
33
44
/
/
Lumo-1-Stage1-7B
*
No
/
/
51.0
69.1
/
82.4
86.4
75.6
62.6
74.7
/
/
/
/
/
/
Gemini-ER 2
‡
No
/
/
35.4
/
/
90.6
†
90.4
81.4
51.1
/
/
/
71.0
/
/
/
Gemini-ER 1.5
‡
No
/
/
41.8
48.0
/
/
83.6
73.4
57.7
62.0
39.9
/
47.0
/
/
/
Gemini 2.5 Pro
‡
No
/
/
33.6
37.0
/
88.6
†
85.9
78.0
71.3
74.7
51.1
/
56.0
/
/
/
Gemini 2.5 Flash
‡
No
/
/
41.2
48.0
/
80.3
†
85.5
76.2
73.4
73.3
45.3
/
47.5
/
/
/
Gemini 3.1 Pro
‡
No
/
/
70.0
61.0
/
86.1
†
88.6
/
65.1
/
47.5
/
65.2
/
/
/
GPT-5.6-sol
‡
No
/
/
58.3
51.1
/
85.6
†
85.2
80.7
66.8
21.3
/
/
64.8
/
/
/
GPT-6-Astra
‡
No
/
/
79.6
69.0
/
90.4
†
87.3
83.3
73.4
31.3
/
/
77.7
/
/
/
Results are sourced from the models' official technical reports or publicly available papers.
Results were obtained through tests using the models' official APIs.
BLINK scores are averaged over the Relative Depth and Spatial Relation subtasks only; all reported results were obtained in our own testing.
Dynamic Region Prediction
We use optical flow to extract dynamic regions that capture future scene changes, then train a VQ-VAE to encode them into fixed-length sequences of discrete tokens. Conditioned on the current image and a task description or action, the VLM directly predicts mask tokens for future dynamic regions, focusing on interaction subjects and the scene changes they induce to enable interaction-centric world modeling.
LIVE PIPELINE
01 / OPTICAL-FLOW SUPERVISION
IMAGE_t0
IMAGE_t1
ESTIMATE
Optical
Flow
OPTICAL FLOW
DYNAMIC MASK
DISCRETIZE
VQ-VAE
Task
OR
Action
IMAGE_t0 + CONDITION
VLM
02 / FUTURE CHANGE PREDICTION
08
21
37
04
19
42
11
26
FUTURE MASK TOKENS
Clean table
01
Fold towel
02
Packaging phone
03
Place plates
04
Discrete Action Learning
We partition the unified action space into three components: end-effector (EEF) poses, end-effector joints, and lower-body joints. A separate residual vector quantization (RVQ) model is trained for each component to discretize action sequences. Building on UnifoLM-ER-1, we introduce discrete action tokens and mask tokens for future dynamic regions, jointly aligning visual, language, and action representations within a single VLM to obtain the UnifoLM-ER-Flow model.
LIVE ENCODING
CONTINUOUS MOTION
VECTOR QUANTIZATION
DISCRETE TOKENS
EEF trajectory
RVQ
<EEF_START>
18
42
07
31
56
<EEF_END>
Gripper / dexterous hand
RVQ
<HAND_START>
04
29
51
16
38
<HAND_END>
Lower-body motion
RVQ
<LOWER_START>
27
11
44
03
22
<LOWER_END>
Temporal alignment
Shared timesteps · Synchronously fed into VLM
WLA Model
Multi-Source Data,
One Model.
UnifoLM-WLA-1.0 builds on the UnifoLM-ER-Flow multimodal backbone and incorporates an MMDiT action expert. It is trained on approximately 2,500 hours of high-quality real-robot data—including the 
Unitree Open Datasets
, 
BitRobot-HIW-500
—covering diverse robot embodiments and operational scenarios. Through a unified action space, it enables cross-embodiment prior transfer and jointly models perception and understanding, interaction prediction, and action generation, balancing embodied manipulation capabilities with general multimodal perception and reasoning.
Training Setup
真机数据、具身推理数据与通用 VLM 数据共同构成训练配方。所有机器人、任务和末端执行器共享同一套模型参数。
 -->
 -->
≈ 2,500h
Multi-embodiment robot data
Co-training
Robot + general VLM data
Fully shared
One set of model weights
 -->
 -->
LIVE GRAPH
Language prediction
place
the
plates
on
the
rack
Discrete actions
8
29
63
118
Continuous actions
-1.7
1.25
3.14
1.42
UnifoLM-ER-Flow
Stop Gradient
Action Expert
MMDiT flow decoder
Gate
MLP
Scale & Shift
Norm
Gate
Gate
MLP
Scale & Shift
Norm
Gate
Self-Attention
q
q
k
k
v
v
RoPE
QK-Norm
q
k
v
Linear
Scale & Shift
Norm
RoPE
QK-Norm
q
k
v
Linear
Scale & Shift
Norm
Linear
Embodiment Embed
VLM Hidden State
Noise Actions
MLP
t
Image encoder
Prompt
State
Noise Actions
Real-robot tests · Unitree G1
One Model Driven,
Multiple Tasks, Multiple End-effectors.
A single UnifoLM-WLA-1.0 model supports both tabletop and whole-body manipulation, demonstrating smooth task execution across diverse real-robot evaluations. The videos below showcase real-robot evaluation results.
10 Whole-Body Manipulation Tasks
10 tasks
 -->
Scroll to explore
←
→
54 Table-top Manipulation Tasks
54 tasks
 -->
Scroll to explore
←
→
UnifoLM-WLA-1.0
General-Purpose Humanoid Robot Foundation Model

---

# GitHub README — unitreerobotics/unifolm-wla (main, 2026-09-11)

# UnifoLM-WLA-1.0
<div align="right"><a href="README.md"><kbd>English</kbd></a> | <a href="README_zh.md"><kbd>简体中文</kbd></a></div>
<div align="center">

[Project Page](https://unigen-x.github.io/unifolm-wla.github.io/) | [Models](https://huggingface.co/collections/unitreerobotics/unifolm-wla-10) | [Datasets](https://huggingface.co/collections/unitreerobotics/unifolm-wla-10)

<p align="center">
  <a href="https://www.youtube.com/watch?v=GHySQMMrIa4">
    <img src="assets/unifolm-wla-en-cover.png" alt="UnifoLM-WLA-1.0 video" width="800">
  </a>
</p>

</div>

UnifoLM-WLA-1.0 is Unitree Robotics' comprehensively upgraded, next-generation general-purpose humanoid robot foundation model with 6B parameters. Built on large-scale general multimodal perception and understanding data and interaction-centric world modeling, it substantially advances spatial perception and understanding, achieving leading results across multiple embodied reasoning benchmarks. Trained on approximately 2,500 hours of high-quality real-robot data, a single model coordinates 64 tasks spanning desktop manipulation and whole-body manipulation. It supports two-finger grippers and multiple five-finger dexterous hands, with strong generalization across tasks and end effectors.

## 🔥 News

- Sep 11, 2026: 🚀 we released the model weights of [UnifoLM-ER-1](https://huggingface.co/unitreerobotics/UnifoLM-ER-1)
- Sep 11, 2026: 🚀 we released the model weights of [UnifoLM-ER-Flow](https://huggingface.co/unitreerobotics/UnifoLM-ER-Flow)

## 📑 Open-Source Plan

- **Code**
  - [ ] Post-Train Code
- **Models**
  - [x] [**UnifoLM-ER-1**](https://huggingface.co/unitreerobotics/UnifoLM-ER-1)
  - [x] [**UnifoLM-ER-Flow**](https://huggingface.co/unitreerobotics/UnifoLM-ER-Flow)
  - [ ] UnifoLM-WLA-1.0
- **Datasets**
  - [x] [**UniBot-V1 Challenge Dataset**](https://huggingface.co/collections/unitreerobotics/unibot-v1-challenge)
  - [ ] Unitree-WBT-Dataset
  - [ ] Unitree-Manipulation-Dataset


---

# Hugging Face model card — unitreerobotics/UnifoLM-ER-1

# UnifoLM-ER-1-4B

[Project Page](https://unigen-x.github.io/unifolm-wla.github.io/)

Across 16 multimodal perception and understanding benchmarks, UnifoLM-ER-1 leads open-source models on seven and delivers overall performance comparable to leading proprietary models. Built on Qwen3-VL-4B, UnifoLM-ER-1 is trained on more than 5 million samples spanning image point prediction, object detection, multi-image reasoning, 2D trajectory prediction, 3D object detection, and multi-image spatial question answering. These data are co-trained with general image-text data, preserving broad vision-language capabilities while substantially improving spatial understanding and reasoning in embodied environments.

## Benchmark Results

| Model | Open Source | RoboVQA | Ego-Plan2 | RefSpatial-Bench | Where2Place | Pixmo-Point | BLINK | CV-Bench | EmbSpatial | RoboSpatial | SAT | VSI-Bench | VSR | ERQA | RealWorldQA | MME | MMMU_VAL |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **UnifoLM-ER-1-4B** | Yes | 62.4 | 55.1 | **61.7** | **82.0** | **73.8** | **93.4<sup>†</sup>** | 88.6 | **88.9** | **73.1** | 76.0 | 54.2 | **88.1** | 50.0 | 69.8 | 2223.3 | 54.7 |
| RoboBrain2.0-7B<sup>*</sup> | Yes | 30.0 | 33.23 | 42.2 | 63.6 | 54.7 | 83.9 | 85.7 | 76.3 | 54.2 | 75.3 | 36.1 | 84.0 | — | 69.4 | 2057.4 | 44.4 |
| Robix-7B<sup>*</sup> | No | **63.6** | — | — | 41.9 | 29.5 | 87.6 | 86.5 | 77.4 | — | 71.1 | 44.6 | 83.3 | 42.5 | 70.7 | 2332.8 | — |
| Pelican-7B<sup>*</sup> | Yes | 31.8 | 33.7 | 22.3 | 57.3 | 20.4 | — | 79.4 | 73.2 | 57.5 | 52.0 | 52.8 | 82.2 | 39.8 | 69.3 | 2141.9 | 51.1 |
| Cosmos-R1-7B<sup>*</sup> | Yes | 38.8 | 26.0 | 5.6 | 2.9 | 8.2 | — | 76.7 | 68.9 | 42.4 | **82.7** | 25.4 | 82.4 | — | 67.6 | 2157.4 | 37.4 |
| Cosmos3-Super-64B<sup>*</sup> | Yes | — | — | 57.0 | 71.0 | — | 90.3<sup>†</sup> | 88.0 | — | 70.0 | — | 60.9 | — | 51.2 | — | — | — |
| Qwen3-VL-4B<sup>*</sup> | Yes | 47.7 | 40.7 | 46.6 | 63.0 | 48.3 | 85.0<sup>†</sup> | 85.1 | 79.6 | 61.7 | 68.7 | 59.3 | 81.6 | 41.3 | 71.0 | 2325.2 | 57.8 |
| Qwen3-VL-8B<sup>*</sup> | Yes | 43.3 | 49.7 | 54.2 | 61.9 | 51.0 | 73.8<sup>†</sup> | 86.2 | 78.5 | 66.9 | 67.3 | 59.4 | 83.2 | 45.8 | 70.6 | **2412.5** | **62.3** |
| Embodied-R1-3B<sup>*</sup> | Yes | 51.8 | 26.5 | 39.7 | 69.5 | 49.4 | 78.5<sup>†</sup> | 82.7 | 67.4 | 47.4 | 76.3 | 26.6 | — | 35.2 | — | — | — |
| Embodied-R1.5-8B<sup>*</sup> | Yes | 61.0 | 53.8 | 54.2 | 74.0 | 64.8 | 83.0<sup>†</sup> | 86.9 | 78.1 | 69.7 | 74.7 | 56.1 | — | 46.0 | — | — | — |
| Molmo2-ER-4B<sup>*</sup> | Yes | — | — | 52.5 | 54.0 | — | 85.7<sup>†</sup> | 87.8 | 78.8 | — | 78.0 | **74.5** | — | 46.8 | — | — | — |
| Hy-Embodied-VLM-1.0-30B-A3B<sup>*</sup> | Yes | — | 49.6 | 53.4 | 65.0 | 64.6 | 87.3<sup>†</sup> | **89.7** | 82.7 | 69.4 | 78.0 | — | — | **60.8** | — | — | — |
| MiMo-Emb-7B<sup>*</sup> | Yes | 62.0 | 43.0 | 48.0 | 63.6 | 42.35 | 81.3 | 88.2 | 76.2 | 61.7 | 78.6 | 48.5 | 79.0 | 46.7 | 66.3 | 2320.8 | 26.4 |
| Thinker-4B<sup>*</sup> | Yes | 62.7 | **63.7** | 61.0 | 72.0 | 57.4 | 84.6 | 86.3 | 80.2 | 70.8 | 72.7 | 65.4 | 81.5 | — | **71.9** | 2323.4 | 46.2 |
| Wall-OSS-0.5-3B<sup>*</sup> | Yes | — | — | — | 15.0 | — | — | — | — | — | — | — | — | 33 | 44 | — | — |
| Lumo-1-Stage1-7B<sup>*</sup> | No | — | — | 51.0 | 69.1 | — | 82.4 | 86.4 | 75.6 | 62.6 | 74.7 | — | — | — | — | — | — |
| Gemini-ER 2<sup>‡</sup> | No | — | — | 35.4 | — | — | 90.6<sup>†</sup> | **90.4** | 81.4 | 51.1 | — | — | — | 71.0 | — | — | — |
| Gemini-ER 1.5<sup>‡</sup> | No | — | — | 41.8 | 48.0 | — | — | 83.6 | 73.4 | 57.7 | 62.0 | 39.9 | — | 47.0 | — | — | — |
| Gemini 2.5 Pro<sup>‡</sup> | No | — | — | 33.6 | 37.0 | — | 88.6<sup>†</sup> | 85.9 | 78.0 | 71.3 | 74.7 | 51.1 | — | 56.0 | — | — | — |
| Gemini 2.5 Flash<sup>‡</sup> | No | — | — | 41.2 | 48.0 | — | 80.3<sup>†</sup> | 85.5 | 76.2 | 73.4 | 73.3 | 45.3 | — | 47.5 | — | — | — |
| Gemini 3.1 Pro<sup>‡</sup> | No | — | — | 70.0 | 61.0 | — | 86.1<sup>†</sup> | 88.6 | — | 65.1 | — | 47.5 | — | 65.2 | — | — | — |
| GPT-5.6-sol<sup>‡</sup> | No | — | — | 58.3 | 51.1 | — | 85.6<sup>†</sup> | 85.2 | 80.7 | 66.8 | 21.3 | — | — | 64.8 | — | — | — |
| GPT-6-Astra<sup>‡</sup> | No | — | — | **79.6** | 69.0 | — | 90.4<sup>†</sup> | 87.3 | 83.3 | **73.4** | 31.3 | — | — | **77.7** | — | — | — |

<sup>*</sup> Results are sourced from the models' official technical reports or publicly available papers.

<sup>‡</sup> Results were obtained through tests using the models' official APIs.

<sup>†</sup> BLINK scores are averaged over the Relative Depth and Spatial Relation subtasks only; all reported results were obtained in our own testing.

## Citation

```yaml
@misc{unifolm-er-1,
  author       = {Unitree},
  title        = {UnifoLM-WLA-1.0: One Model Driven, Whole-Body Coordination},
  year         = {2026},
}
```


---

# Hugging Face model card — unitreerobotics/UnifoLM-ER-Flow

# UnifoLM-ER-Flow

[Project Page](https://unigen-x.github.io/unifolm-wla.github.io/)

UnifoLM-ER-Flow extends UnifoLM-ER-1 with interaction-centric world modeling and discrete action learning. It jointly aligns visual observations, language conditions, predicted future dynamic regions, and robot actions within a single vision-language model.

## Dynamic Region Prediction

We use optical flow to extract dynamic regions that capture future scene changes, then train a VQ-VAE to encode them into fixed-length sequences of discrete tokens. Conditioned on the current image and a task description or action, the VLM directly predicts mask tokens for future dynamic regions, focusing on interaction subjects and the scene changes they induce to enable interaction-centric world modeling.

![Dynamic region prediction pipeline](assets/dynamic-region-prediction-pipeline.png)


### Demonstrations

<table>
  <tr>
    <td width="50%" align="center">
      <video src="assets/videos/flow-demo-web-2x/clean_table.mp4" controls muted loop playsinline width="100%"></video>
      <br><strong>01 · Clean table</strong>
    </td>
    <td width="50%" align="center">
      <video src="assets/videos/flow-demo-web-2x/fold_towel.mp4" controls muted loop playsinline width="100%"></video>
      <br><strong>02 · Fold towel</strong>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <video src="assets/videos/flow-demo-web-2x/install_phone.mp4" controls muted loop playsinline width="100%"></video>
      <br><strong>03 · Packaging phone</strong>
    </td>
    <td width="50%" align="center">
      <video src="assets/videos/flow-demo-web-2x/place_plates.mp4" controls muted loop playsinline width="100%"></video>
      <br><strong>04 · Place plates</strong>
    </td>
  </tr>
</table>

## Discrete Action Learning

We partition the unified action space into three components: end-effector (EEF) poses, end-effector joints, and lower-body joints. A separate residual vector quantization (RVQ) model is trained for each component to discretize action sequences. Building on UnifoLM-ER-1, we introduce discrete action tokens and mask tokens for future dynamic regions, jointly aligning visual, language, and action representations within a single VLM to obtain the UnifoLM-ER-Flow model.

### Action Encoding Pipeline

Each continuous motion component is encoded independently with its own RVQ model. The resulting token sequences share the same timesteps and are synchronously fed into the VLM.

![Discrete action learning pipeline](assets/discrete-action-learning-pipeline.png)

### Unified Training Signals

| Signal | Representation | Role |
|---|---|---|
| Visual observations | Image tokens | Describe the current environment |
| Task or action condition | Language or action tokens | Specify the intended interaction |
| Future dynamic regions | Mask tokens | Represent interaction-induced scene changes |
| EEF poses | Discrete EEF tokens | Encode end-effector trajectories |
| End-effector joints | Discrete hand tokens | Encode gripper or dexterous-hand motion |
| Lower-body joints | Discrete lower-body tokens | Encode whole-body coordination |

Together, these signals connect spatial understanding, future-change prediction, and action representation in a unified multimodal model.

