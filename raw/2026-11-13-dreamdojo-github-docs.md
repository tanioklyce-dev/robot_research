<!-- NVIDIA/DreamDojo docs/*.md at commit 02f119b (2026-03-21), fetched 2026-11-13 -->

<!-- ===== docs/SETUP.md ===== -->
# Setup

### Environment

The current code is tested with NVIDIA H100 80GB. We use [uv](https://docs.astral.sh/uv/) to manage the environment. We provide a bash script for quick installation.

```
bash install.sh
```

### Dataset

In this release, we provide the GR-1 post-training dataset along with evaluation sets as example datasets for training and inference. The datasets can be downloaded from [Hugging Face](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-GR00T-Teleop-GR1) and can be placed in or linked to the `datasets` directory.

---

=> Next: [[Latent Action Model Training](https://github.com/NVIDIA/DreamDojo/blob/main/docs/LAM.md)]
<!-- ===== docs/LAM.md ===== -->
# Latent Action Model Training

The provided configuration only includes the GR-1 post-training dataset as an example. You can add new datasets by adding folders to `dataset_paths` by yourselves. The code will recursively search the folder and add any detected MP4 videos to the training set.

Using the following bash script to launch latent action training (suppose you are training on 1 node with 8 GPUs).

```
cd external/lam_project
bash train.sh
```

A multi-node training script example is provided at `external/lam_project/launch.sh`. Add the index of the YAML file to specify the configuration to use.

```
bash launch.sh 0
```

> [!NOTE]
> Our latent action model weights can be found at [Hugging Face](https://huggingface.co/nvidia/DreamDojo). To set the path to your own checkpoint for proxy action extraction, check `https://github.com/NVIDIA/DreamDojo/blob/main/cosmos_predict2/_src/predict2/models/text2world_model_rectified_flow.py`.

---

<= Previous: [[Setup](https://github.com/NVIDIA/DreamDojo/blob/main/docs/SETUP.md)]

=> Next: [[DreamDojo Pretraining](https://github.com/NVIDIA/DreamDojo/blob/main/docs/PRETRAIN.md)]
<!-- ===== docs/PRETRAIN.md ===== -->
# DreamDojo Pretraining

We provide a launching script for DreamDojo pretraining (suppose you are training on 1 node with 8 GPUs).

1. Make sure you have set the correct paths in `launch.sh`.
2. Replace the `ckpt_path` in `cosmos_predict2/_src/predict2/models/text2world_model_rectified_flow.py` to the actual latent action model path.
3. Launch DreamDojo pretraining.
    
    ```
    bash launch.sh dreamdojo_2b_480_640_pretrain
    ```

> [!NOTE]
> The pretrained DreamDojo checkpoints (2B and 14B) can be found at [Hugging Face](https://huggingface.co/nvidia/DreamDojo).

---

<= Previous: [[Latent Action Model Training](https://github.com/NVIDIA/DreamDojo/blob/main/docs/LAM.md)]

=> Next: [[DreamDojo Post-Training](https://github.com/NVIDIA/DreamDojo/blob/main/docs/POSTTRAIN.md)]
<!-- ===== docs/POSTTRAIN.md ===== -->
# DreamDojo Post-Training

The training configurations are managed by yaml under `configs`. To launch post-training:

1. Follow the same setup as the pretraining.
2. Change `load_path` in `cosmos_predict2/experiments/base/action.py` to the pretrained checkpoint and specify its training step. To use our pretrained model, set `load_path` to `checkpoints/DreamDojo/2B_pretrain/iter_000140000/` or `checkpoints/DreamDojo/14B_pretrain/iter_000140000/`.
3. (Optional) Disable the extraction of latent actions on the fly, as it will be reset to zero.
4. Send the desired experiment config (e.g., `dreamdojo_2b_480_640_gr1` to use `2b_480_640_gr1.yaml`).
    
    ```
    bash launch.sh dreamdojo_2b_480_640_gr1
    bash launch.sh dreamdojo_2b_480_640_g1
    bash launch.sh dreamdojo_2b_480_640_agibot
    bash launch.sh dreamdojo_2b_480_640_yam
    ```

For simplicity of implementation, we set the dimension of the first action projection layer to 384. This will slightly increase computational requirements but makes checkpoint resuming easier. You can also reduce it to the dimension actually used by the model after post-training. Our dimension assignment follows this rule:
- [0, 29): Fourier GR-1
- [29, 58): Retargeted GR-1 actions from Manus gloves
- [58, 101): Unitree G1
- [101, 147): Bimanual YAM
- [147, 169): AgiBot
- [169, 220): Reserved for other usages
- [220, 352): MANO actions
- [352, 384): Latent actions

> [!NOTE]
> The post-trained DreamDojo checkpoints for G1, GR-1, AgiBot, and YAM (2B and 14B) can be found at [Hugging Face](https://huggingface.co/nvidia/DreamDojo).

---

<= Previous: [[DreamDojo Pretraining](https://github.com/NVIDIA/DreamDojo/blob/main/docs/PRETRAIN.md)]

=> Next: [[DreamDojo Distillation](https://github.com/NVIDIA/DreamDojo/blob/main/docs/DISTILL.md)]
<!-- ===== docs/DISTILL.md ===== -->
# Distillation

The distillation pipeline converts a post-trained DreamDojo teacher model into a fast, causal student model capable of long-horizon autoregressive generation at 10 FPS. The pipeline consists of three stages:

1. **Teacher Generation** — Generate multi-step denoising targets from the teacher model.
2. **Warmup** — Train the causal student architecture to match the teacher's outputs.
3. **Self-Forcing** — Finetune the student with its own autoregressive predictions to reduce error accumulation.

After distillation, you can run offline inference to generate videos from a dataset of action sequences, or real-time inference for interactive teleoperation.

## Teacher Generation

Generate denoising targets from the teacher model at few-step noise levels. This pre-computes the supervision for warmup training.

```bash
bash launch_teacher_gen.sh
```

## Warmup Training

Train the causal student network to match the teacher's denoising outputs. This initializes the student before self-forcing.

```bash
bash launch_warmup.sh
```

The warmup experiment configs are defined in `cosmos_predict2/_src/predict2/interactive/configs/experiment/exp_action_warmup.py`.

## Self-Forcing Distillation

Finetune the student model with its own autoregressive rollouts to improve long-horizon stability, using the teacher model to provide the score during DMD distillation.

```bash
bash launch_self_forcing.sh
```

The self-forcing experiment configs are defined in `cosmos_predict2/_src/predict2/interactive/configs/experiment/exp_action_self_forcing.py`.

## Inference

Generate videos conditioned on pre-recorded action sequences via:

```bash
bash launch_student_inference.sh
```

Key arguments:
- `--experiment`: Self-forcing experiment config name, which should match the one used during distillation.
- `--ckpt_path`: Path to the distilled checkpoint.
- `--input_json`: Path to a JSON file containing evaluation entries (each entry specifies a video path, actions, and metadata).

### Real-Time Teleoperation

Run the distilled model interactively with live action inputs (e.g., teleoperation):

```bash
bash launch_student_inference_teleop.sh
```

Key arguments:
- `--ckpt_path`: Path to the distilled checkpoint.
- `--input_frame`: Path to the initial conditioning frame (PNG image).
- `--action_source`: Action input source (`file` for pre-recorded, or other sources for live input).
- `--action_file`: Path to a `.npy` file containing actions (when using `file` source).
- `--max_latent_frames`: Maximum number of latent frames to generate.
- `--fps`: Target generation framerate (default: 10.0).
- `--save_output`: Path to save the generated video (e.g., `output.mp4`).

---

<= Previous: [[DreamDojo Post-Training](https://github.com/NVIDIA/DreamDojo/blob/main/docs/POSTTRAIN.md)]

=> Next: [[Evaluation](https://github.com/NVIDIA/DreamDojo/blob/main/docs/EVAL.md)]

<!-- ===== docs/EVAL.md ===== -->
# Evaluation

When/After adapting to the target robot action space through post-training, you can keep tracking the performance of the checkpoints at a specified interval.

```
bash eval.sh
```

Important arguments:

- `--checkpoints-dir`: Path to the saved checkpoints.
- `--experiment`: Configuration name.
- `--save-dir`: Path to save the generated videos.
- `--num-frames`: Length of the ground truth video, including the first condition frame.
- `--num-samples`: Number of the samples to evaluate on.
- `--dataset-path`: Path to the evaluation datasets. You can also concatenate multiple evaluation sets here by spliting them with commas.
- `--data-split`: Which subset for evaluation. (`full`: sample from 100%; `train`: the first 95% of each concatenated eval set; `test`: the last 5% of each concatenated eval set).
- `--deterministic-uniform-sampling`: If enabled, sample from the concatenated datasets uniformly instead of by their lengths.
- `--checkpoint-interval`: Interval of the checkpoints to evaluate.
- `--infinite`: Continuously check for new checkpoints at the desired interval to track performance during training.

To reproduce our evaluation samples:

- In-lab Eval:
  ```
  --num-frames 49 \
  --num-samples 100 \
  --dataset-path "datasets/PhysicalAI-Robotics-GR00T-Teleop-GR1/In-lab_Eval/gr1_unified.pnp_handover_plate_robot,datasets/PhysicalAI-Robotics-GR00T-Teleop-GR1/In-lab_Eval/gr1_unified.pnp_cucumber_robot,datasets/PhysicalAI-Robotics-GR00T-Teleop-GR1/In-lab_Eval/gr1_unified.pnp_corn_robot,datasets/PhysicalAI-Robotics-GR00T-Teleop-GR1/In-lab_Eval/gr1_unified.pnp_dragonfruit_robot,datasets/PhysicalAI-Robotics-GR00T-Teleop-GR1/In-lab_Eval/gr1_unified.pour_items_into_basket_robot,datasets/PhysicalAI-Robotics-GR00T-Teleop-GR1/In-lab_Eval/gr1_unified.right_to_left_handover_corn_robot,datasets/PhysicalAI-Robotics-GR00T-Teleop-GR1/In-lab_Eval/gr1_unified.mug_robot,datasets/PhysicalAI-Robotics-GR00T-Teleop-GR1/In-lab_Eval/gr1_unified.fold_cloth_long_robot,datasets/PhysicalAI-Robotics-GR00T-Teleop-GR1/In-lab_Eval/gr1_unified.fold_cloth_robot,datasets/PhysicalAI-Robotics-GR00T-Teleop-GR1/In-lab_Eval/gr1_unified.color_puzzles_robot" \
  --data-split full \
  --deterministic-uniform-sampling \
  ```
- EgoDex Eval:
  ```
  --num-frames 49 \
  --num-samples 100 \
  --dataset-path "datasets/PhysicalAI-Robotics-GR00T-Teleop-GR1/EgoDex_Eval" \
  --data-split full \
  --deterministic-uniform-sampling \
  ```
- DreamDojo-HV Eval:
  ```
  --num-frames 49 \
  --num-samples 100 \
  --dataset-path "datasets/PhysicalAI-Robotics-GR00T-Teleop-GR1/DreamDojo-HV_Eval" \
  --data-split full \
  --deterministic-uniform-sampling \
  ```

---

<= Previous: [[DreamDojo Post-Training](https://github.com/NVIDIA/DreamDojo/blob/main/docs/POSTTRAIN.md)]

=> Next: [[Trouble Shooting](https://github.com/NVIDIA/DreamDojo/blob/main/docs/ISSUES.md)]
<!-- ===== docs/ISSUES.md ===== -->
# Troubleshooting

We will continue to improve this repository. If you encounter any issues, please feel free to let us know!

Make sure you have exported the following variables in the training script. Missing these may cause unstable training performance.

```
export TORCH_NCCL_ENABLE_MONITORING=0
export TORCH_NCCL_HEARTBEAT_TIMEOUT_SEC=1800
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export FI_EFA_USE_DEVICE_RDMA=1
export RDMAV_FORK_SAFE=1
export TORCH_DIST_INIT_BARRIER=1
```

---

<= Previous: [[Evaluation](https://github.com/NVIDIA/DreamDojo/blob/main/docs/EVAL.md)]