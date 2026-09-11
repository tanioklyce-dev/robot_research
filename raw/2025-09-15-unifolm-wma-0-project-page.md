---
source_url: https://unigen-x.github.io/unifolm-world-model-action.github.io/
collected: 2026-09-11
published: 2025-09-15
author: Unitree Robotics
companion_urls:
  - https://github.com/unitreerobotics/unifolm-world-model-action (README main @ 2026-09-11; last push 2026-03-18; ~1.1k stars)
  - https://huggingface.co/unitreerobotics/UnifoLM-WMA-0-Dual (model card; -Base is gated)
  - configs/train/config.yaml (verbatim below)
license: CC BY-NC-SA 4.0
note: Bilingual page; Chinese lines dropped from the capture. Videos/GIFs not reproduced. No paper exists.
---

# UnifoLM-WMA-0 project page (tag-stripped, English lines)

UnifoLM-WMA-0: A World-Model-Action(WMA) Framework under UnifoLM Family
🌎 English
UnifoLM-WMA-0: A World-Model-Action (WMA) Framework 
 under UnifoLM Family
      Code
15 Sep 2025
UnifoLM-WMA-0
 is Unitree‘s open-source world-model–action architecture spanning multiple types of robotic embodiments, designed specifically for general-purpose robot learning. Its core component is a world-model capable of understanding the physical interactions between robots and the environments. This world-model provides two key functions: (a) 
Simulation Engine
 – operates as an interactive simulator to generate synthetic data for robot learning; (b) 
Policy Enhancement
 – connects with an action head and, by predicting future interaction processes with the world-model, further optimizes decision-making performance. The deployment on the real robots are shown below: .
UnifoLM-WMA-0
      (Note: The top-right window shows the world model’s prediction of future action videos.)
Fine-tuning the Video Generation Model
: First, we fine-tune the video generation model on the Open-X dataset to adapt its generative capability to robotic operation scenarios. The model takes images and text instructions as input and generates future interactions in video format. The generation results of the fine-tuned model on the test set are as follows:
UnifoLM-WMA-0 Architecture
: We propose a world-model–embedded policy architecture. This framework enables the world model to operate in two modes: (1) 
Decision-Making Mode
: predicts information about future physical interactions to assist the policy in generating actions. (2) 
Simulation Mode
: generates high-fidelity environmental feedback based on robot actions. The complete system architecture and its working flow are shown as follows: 
UnifoLM-WMA-0 Action Controllable Generation
: We trained the model on five 
open-source datasets from Unitree Robotics
. Test results show that, as a simulation engine, the model can achieve interactive controllable generation based on the current image and a certain number of future robot actions. A comparison between the generated results and the original videos is shown below:
◀
▶
UnifoLM-WMA-0 Long-Term Interactive Generation
: The model also has the capability to perform long-term interactive generation for long-horizon tasks. A comparison between the generated results and the original videos is shown below:
        ◀
        ▶

---

# GitHub README — unitreerobotics/unifolm-world-model-action

# UnifoLM-WMA-0: A World-Model-Action (WMA) Framework under UnifoLM Family
<p style="font-size: 1.2em;">
    <a href="https://unigen-x.github.io/unifolm-world-model-action.github.io"><strong>Project Page</strong></a> | 
    <a href="https://huggingface.co/collections/unitreerobotics/unifolm-wma-0-68ca23027310c0ca0f34959c"><strong>Models</strong></a> |
    <a href="https://huggingface.co/unitreerobotics/datasets"><strong>Dataset</strong></a> 
  </p>
<div align="center">
  <p align="right">
    <span> 🌎English </span> | <a href="README_cn.md"> 🇨🇳中文 </a>
  </p>
</div>
<div align="justify">
    <b>UnifoLM-WMA-0</b> is Unitree‘s open-source world-model–action architecture spanning multiple types of robotic embodiments, designed specifically for general-purpose robot learning. Its core component is a world-model capable of understanding the physical interactions between robots and the environments. This world-model provides two key functions: (a) <b>Simulation Engine</b> – operates as an interactive simulator to generate synthetic data for robot learning; (b) <b>Policy Enhancement</b> – connects with an action head and, by predicting future interaction processes with the world-model, further optimizes decision-making performance.
</div>

## 🦾 Real-Robot Demonstrations
| <img src="assets/gifs/real_z1_stackbox.gif" style="border:none;box-shadow:none;margin:0;padding:0;" /> | <img src="assets/gifs/real_dual_stackbox.gif" style="border:none;box-shadow:none;margin:0;padding:0;" /> |
|:---:|:---:|
| <img src="assets/gifs/real_cleanup_pencils.gif" style="border:none;box-shadow:none;margin:0;padding:0;" /> | <img src="assets/gifs/real_g1_pack_camera.gif" style="border:none;box-shadow:none;margin:0;padding:0;" /> |

**Note: the top-right window shows the world model’s pretion of future action videos.**

## 🔥 News

* Sep 22, 2025: 🚀 We released the deployment code for assisting experiments with [Unitree](https://www.unitree.com/) robots.
* Sep 15, 2025: 🚀 We released the training and inference code along with the model weights of [**UnifoLM-WMA-0**](https://huggingface.co/collections/unitreerobotics/unifolm-wma-0-68ca23027310c0ca0f34959c).

## 📑 Opensource Plan
- [x] Training 
- [x] Inference
- [x] Checkpoints
- [x] Deployment

## ⚙️  Installation
```
conda create -n unifolm-wma python==3.10.18
conda activate unifolm-wma

conda install pinocchio=3.2.0 -c conda-forge -y
conda install ffmpeg=7.1.1 -c conda-forge

git clone --recurse-submodules https://github.com/unitreerobotics/unifolm-world-model-action.git

# If you already downloaded the repo:
cd unifolm-world-model-action
git submodule update --init --recursive

pip install -e .

cd external/dlimp
pip install -e .
```
## 🧰 Model Checkpoints
| Model | Description | Link|
|---------|-------|------|
|$\text{UnifoLM-WMA-0}_{Base}$| Fine-tuned on [Open-X](https://robotics-transformer-x.github.io/) dataset. | [HuggingFace](https://huggingface.co/unitreerobotics/UnifoLM-WMA-0-Base)|
|$\text{UnifoLM-WMA-0}_{Dual}$| Fine-tuned on five [Unitree opensource dataset](https://huggingface.co/collections/unitreerobotics/g1-dex1-datasets-68bae98bf0a26d617f9983ab) in both decision-making and simulation modes. | [HuggingFace](https://huggingface.co/unitreerobotics/UnifoLM-WMA-0-Dual)|

## 🛢️ Dataset
In our experiments, we consider the following five opensource dataset:
| Dataset | Robot | Link |
|---------|-------|------|
|Z1_StackBox| [Unitree Z1](https://www.unitree.com/z1)|[Huggingface](https://huggingface.co/datasets/unitreerobotics/Z1_StackBox_Dataset/tree/v2.1)|
|Z1_DualArm_StackBox|[Unitree Z1](https://www.unitree.com/z1)|[Huggingface](https://huggingface.co/datasets/unitreerobotics/Z1_Dual_Dex1_StackBox_Dataset/tree/v2.1)|
|Z1_DualArm_StackBox_V2|[Unitree Z1](https://www.unitree.com/z1)|[Huggingface](https://huggingface.co/datasets/unitreerobotics/Z1_Dual_Dex1_StackBox_Dataset_V2/tree/v2.1)|
|Z1_DualArm_Cleanup_Pencils|[Unitree Z1](https://www.unitree.com/z1)|[Huggingface](https://huggingface.co/datasets/unitreerobotics/Z1_Dual_Dex1_CleanupPencils_Dataset/tree/v2.1)|
|G1_Pack_Camera|[Unitree G1](https://www.unitree.com/g1)|[Huggingface](https://huggingface.co/datasets/unitreerobotics/G1_Dex1_MountCameraRedGripper_Dataset/tree/v2.1)|

#### Extra available dataset
This dataset is collected using the Unitree G1 robot with a 7-DOF dexterous arm, covering a variety of table-top manipulation tasks in both single-arm and dual-arm settings. It is suitable for training video generation models, world models, and other downstream applications. Each episode lasts approximately 30 seconds. Available image resolutions: 256×256 and 128×128.

| Dataset | Robot | Link |
|---------|-------|------|
|G1_Dex1_DiverseManip_DualArm_256x256|[Unitree G1](https://www.unitree.com/g1)|[Huggingface](https://huggingface.co/datasets/unitreerobotics/G1_Dex1_DiverseManip_DualArm_256x256)|
|G1_Dex1_DiverseManip_DualArm_128x128|[Unitree G1](https://www.unitree.com/g1)|[Huggingface](https://huggingface.co/datasets/unitreerobotics/G1_Dex1_DiverseManip_DualArm_128x128)|
|G1_Dex1_DiverseManip_SingleArm_256x256|[Unitree G1](https://www.unitree.com/g1)|[Huggingface](https://huggingface.co/datasets/unitreerobotics/G1_Dex1_DiverseManip_SingleArm_256x256)|
|G1_Dex1_DiverseManip_SingleArm_128x128|[Unitree G1](https://www.unitree.com/g1)|[Huggingface](https://huggingface.co/datasets/unitreerobotics/G1_Dex1_DiverseManip_SingleArm_128x128)|
<br>

To train on your own dataset, first to have the data following the [Huggingface LeRobot V2.1](https://github.com/huggingface/lerobot) dataset format. Assume the dataset’s source directory structure is as follows:
```
source_dir/
    ├── dataset1_name
    ├── dataset2_name
    ├── dataset3_name
    └── ...
```
Then, convert a dataset to the required format using the command below:
```python
cd prepare_data
python prepare_training_data.py \
    --source_dir /path/to/your/source_dir \
    --target_dir /path/to/save/the/converted/data \
    --dataset_name "dataset1_name" \
    --robot_name "a tag of the robot in the dataset" # e.g, Unitree Z1 Robot Arm or Unitree G1 Robot with Gripper.
```
The resulting data structure (Note: model training only supports input from the main-view camera. If the dataset includes multiple views, remove the corresponding values from the ```data_dir``` column in the CSV file.
```
target_dir/
    ├── videos
    │     ├──dataset1_name
    │     │   ├──camera_view_dir
    │     │       ├── 0.mp4
    │     │       ├── 1.mp4
    │     │       └── ...
    │     └── ...
    ├── transitions
    │    ├── dataset1_name
    │        ├── meta_data
    │        ├── 0.h5
    │        ├── 1.h5
    │        └── ...
    └──  dataset1_name.csv
```
## 🚴‍♂️ Training
A. Our training strategy is outlined as follows:
- **Step 1**: Fine-tune a video generation model as the world model using the [Open-X](https://robotics-transformer-x.github.io/) dataset;
- **Step 2**: Post-train $\text{UnifoLM-WMA}$ in decision-making mode on the downstream task dataset;
  <div align="left">
      <img src="assets/pngs/dm_mode.png" width="600">
  </div>
- **Step 3**: Post-train $\text{UnifoLM-WMA}$ in simulation mode on the downstream task dataset.
  <div align="left">
      <img src="assets/pngs/sim_mode.png" width="600">
  </div>
**Note**: If you only require $\text{UnifoLM-WMA}$ to operate in a single mode, you may skip the corresponding step.

B. To conduct training on a single or multiple datasets, please follow the steps below:
- **Step 1**: The maximum DoF is assumed to be 16, if you have more than 16 DoF, update ```agent_state_dim``` and ```agent_action_dim``` in [configs/train/config.yaml](https://github.com/unitreerobotics/unifolm-wma/blob/working/configs/train/config.yaml) ;
- **Step 2**: Set up the input shapes for each modality in [configs/train/meta.json](https://github.com/unitreerobotics/unitree-world-model/blob/main/configs/train/meta.json);
- **Step 3**: Configure the training parameters in [configs/train/config.yaml](https://github.com/unitreerobotics/unitree-world-model/blob/main/configs/train/config.yaml). For the ```pretrained_checkpoint```, we recommend using the checkpoint " $\text{UnifoLM-WMA-0}_{Base}$ " fine-tuned on the [Open-X](https://robotics-transformer-x.github.io/) dataset;
  ```yaml
  model:
      pretrained_checkpoint: /path/to/pretrained/checkpoint;
      ...
      decision_making_only: True # Train the world model only in decision-making mode. If False, jointly train it in both decision-making and simulation modes.
      ...
  data:
      ...
      train:
          ...
          data_dir: /path/to/training/dataset/directory
      dataset_and_weights: # list the name of each dataset below and make sure the summation of weights is 1.0
          dataset1_name: 0.2
          dataset2_name: 0.2
          dataset3_name: 0.2
          dataset4_name: 0.2
          dataset5_name: 0.2
  ```
- **Step 4**: Setup ```experiment_name```, ```save_root``` variables in [scripts/train.sh](https://github.com/unitreerobotics/unitree-world-model/blob/main/scripts/train.sh);
- **Step 5**: Launch the training with the command:
```
bash scripts/train.sh
```
## 🌏 Inference under Interactive Simulation Mode
To run the world model in an interactive simulation mode, follow these steps:
- **Step 1**: (Skip this step if you just would like to test using the examples we provided) Prepare your own prompt following the format used in the [examples/world_model_interaction_prompts](https://github.com/unitreerobotics/unitree-world-model/tree/main/examples/world_model_interaction_prompts):
  ```
  world_model_interaction_prompts/
    ├── images
    │    ├── dataset1_name
    │    │       ├── 0.png     # Image prompt
    │    │       └── ...
    │    └── ...
    ├── transitions
    │    ├── dataset1_name
    │    │       ├── meta_data # Used for normalization
    │    │       ├── 0.h       # Robot state and action data; in interaction mode,
    │    │       │             # only used to retrieve the robot state corresponding 
    │    │       │             # to the image prompt
    │    │       └── ...
    │    └── ...
    ├──  dataset1_name.csv     # File for loading image prompts, text instruction and corresponding robot states
    └── ...
  ```
- **Step 2**: Specify the correct paths for ```pretrained_checkpoint```(e.g, $\text{UnifoLM-WMA-0}_{Dual}$) and ```data_dir``` in [configs/inference/world_model_interaction.yaml](https://github.com/unitreerobotics/unitree-world-model/blob/main/configs/inference/world_model_interaction.yaml) 
- **Step 3**: Set the paths for ```checkpoint```, ```res_dir``` and ```prompt_dir``` in [scripts/run_world_model_interaction.sh](https://github.com/unitreerobotics/unitree-world-model/blob/main/scripts/run_world_model_interaction.sh), and specify all the dataset's name in ```datasets=(...)```. Then, launch the inference with the command:
    ```
    bash scripts/run_world_model_interaction.sh
    ```

## 🧠 Inference and Deployment under Decision-Making Mode

In this setup, inference is performed on a server, while a robot client gathers observations from the real-robot and sends them to the server to query actions. The process unfolds through the following steps:

### Server Setup:
- **Step-1**: Specify ```ckpt```, ```res_dir```, ```datasets``` in [scripts/run_real_eval_server.sh](https://github.com/unitreerobotics/unifolm-world-model-action/blob/main/scripts/run_real_eval_server.sh);
- **Step-2**: Configure ```data_dir``` and ```dataset_and_weights``` in [config/inference/world_model_decision_making.yaml](https://github.com/unitreerobotics/unifolm-world-model-action/blob/f12b4782652ca00452941d851b17446e4ee7124a/configs/inference/world_model_decision_making.yaml#L225);
- **Step-3**: Launch the server:
```
conda activate unifolm-wma
cd unifolm-world-model-action
bash scripts/run_real_eval_server.sh
```

### Client Setup
- **Step-1**: Follow the instructions in [unitree_deploy/README.md](https://github.com/unitreerobotics/unifolm-world-model-action/blob/main/unitree_deploy/README.md) to create the ```unitree_deploy``` conda environment, install the required packages, launch the controllers or services on the real-robot.
- **Step-2**: Open a new terminal and establish a tunnel connection from the client to the server:
```
ssh user_name@remote_server_IP -CNg -L 8000:127.0.0.1:8000
```
- **Step-3**: Run the ```unitree_deploy/robot_client.py``` script to start inference:
```
cd unitree_deploy
python scripts/robot_client.py --robot_type "g1_dex1" --action_horizon 16 --exe_steps 16 --observation_horizon 2 --language_instruction "pack black camera into box" --output_dir ./results --control_freq 15
```

## 📝 Codebase Architecture
Here's a high-level overview of the project's code structure and core components:
```
unitree-world-model/
    ├── assets                      # Media assets such as GIFs, images, and demo videos
    ├── configs                     # Configuration files for training and inference
    │    ├── inference
    │    └──  train
    ├── examples                    # Example inputs and prompts for running inference
    ├── external                    # External packages
    ├── prepare_data                # Scripts for dataset preprocessing and format conversion
    ├── scripts                     # Main scripts for training, evaluation, and deployment
    ├── src
    │    ├──unitree_worldmodel      # Core Python package for the Unitree world model
    │    │      ├── data            # Dataset loading, transformations, and dataloaders
    │    │      ├── models          # Model architectures and backbone definitions
    │    │      ├── modules         # Custom model modules and components
    │    │      └──  utils          # Utility functions and common helpers
    └── unitree_deploy              # Deployment code
```

## 🙏 Acknowledgement
Lots of code are inherited from [DynamiCrafter](https://github.com/Doubiiu/DynamiCrafter), [Diffusion Policy](https://github.com/real-stanford/diffusion_policy), [ACT](https://github.com/MarkFzp/act-plus-plus) and [HPT](https://github.com/liruiw/HPT).

## 📝 Citation
```
@misc{unifolm-wma-0,
  author       = {Unitree},
  title        = {UnifoLM-WMA-0: A World-Model-Action (WMA) Framework under UnifoLM Family},
  year         = {2025},
}
```


---

# configs/train/config.yaml

```yaml
model:
  pretrained_checkpoint: /path/to/pretrained/checkpoint
  base_learning_rate: 1.0e-05
  scale_lr: False
  target: unifolm_wma.models.ddpms.LatentVisualDiffusion
  params:
    rescale_betas_zero_snr: True
    parameterization: "v"
    linear_start: 0.00085
    linear_end: 0.012
    num_timesteps_cond: 1
    log_every_t: 200
    timesteps: 1000
    first_stage_key: video
    cond_stage_key: instruction
    cond_stage_trainable: False
    image_proj_model_trainable: True
    conditioning_key: hybrid
    image_size: [40, 64]
    channels: 4
    scale_by_std: False
    scale_factor: 0.18215
    use_ema: False
    uncond_prob: 0.05
    uncond_type: 'empty_seq'
    rand_cond_frame: false
    use_dynamic_rescale: true
    base_scale: 0.7
    fps_condition_type: 'fps'
    perframe_ae: True
    freeze_embedder: True
    n_obs_steps_imagen: 2
    n_obs_steps_acting: 2
    agent_state_dim: 16
    agent_action_dim: 16
    decision_making_only: True

    ###################### DP Related 
    input_pertub: 0.1
    lr_scheduler: cosine
    lr_warmup_steps: 2000
    num_epochs: 60000
    gradient_accumulate_every: 1
    use_scheduler: True
    dp_use_ema: True

    dp_ema_config:
      target: unifolm_wma.models.diffusion_head.ema_model.EMAModel
      params:
        update_after_step: 0
        inv_gamma: 1.0
        power: 0.75
        min_value: 0.0
        max_value: 0.9999

    noise_scheduler_config:
      target: diffusers.DDIMScheduler
      params:
        num_train_timesteps: 1000
        beta_start: 0.0001
        beta_end: 0.02
        beta_schedule: squaredcos_cap_v2
        clip_sample: True
        set_alpha_to_one: True
        steps_offset: 0
        prediction_type: epsilon

    dp_optimizer_config:
      target: torch.optim.AdamW
      params:
        lr: 1.0e-4
        betas: [0.95, 0.999]
        eps: 1.0e-8
        weight_decay: 1.0e-6

    wma_config:
      target: unifolm_wma.modules.networks.wma_model.WMAModel
      params:
        in_channels: 8
        out_channels: 4
        model_channels: 320
        attention_resolutions:
        - 4
        - 2
        - 1
        num_res_blocks: 2
        channel_mult:
        - 1
        - 2
        - 4
        - 4
        dropout: 0.1
        num_head_channels: 64
        transformer_depth: 1
        context_dim: 1024
        use_linear: true
        use_checkpoint: True
        temporal_conv: True
        temporal_attention: True
        temporal_selfatt_only: True
        use_relative_position: False
        use_causal_attention: False
        temporal_length: 16
        addition_attention: True
        image_cross_attention: True
        default_fs: 10
        fs_condition: True
        cross_attention_scale_learnable: False
        n_obs_steps: ${model.params.n_obs_steps_imagen}
        num_stem_token: 16
        base_model_gen_only: False

        unet_head_config:
          target: unifolm_wma.models.diffusion_head.conditional_unet1d.ConditionalUnet1D
          params:
            input_dim: ${model.params.agent_action_dim} 
            n_obs_steps: ${model.params.n_obs_steps_acting}
            diffusion_step_embed_dim: 128
            down_dims: [256, 512, 1024, 2048]
            kernel_size: 5
            n_groups: 8
            cond_predict_scale: True
            num_head_channels: ${model.params.wma_config.params.num_head_channels}
            horizon: ${model.params.wma_config.params.temporal_length}
            use_linear_attn: ${model.params.wma_config.params.use_linear}
            use_linear_act_proj: True
            act_proj_dim: 32
            cond_cross_attention: False
            context_dims: []
            image_size: ${model.params.image_size}
            imagen_cond_gradient: True
            last_frame_only: False
            use_imagen_mid_only: False
            use_z_only: False

            obs_encoder_config:
              target: unifolm_wma.models.diffusion_head.vision.multi_image_obs_encoder.MultiImageObsEncoder
              params:
                rgb_model_config:
                  target: unifolm_wma.models.diffusion_head.vision.model_getter.get_resnet
                  params:
                    name: resnet18
                    weights: null
                resize_shape: null
                crop_shape: null
                random_crop: False
                use_group_norm: True
                share_rgb_model: False
                imagenet_norm: True
                use_spatial_softmax: True
                spatial_softmax_kp: 128

        ###################### Action Tokenization
        stem_process_config:
          target: unifolm_wma.modules.encoders.condition.SATokenProjector
          params:
            dim: 1024
            depth: 1
            dim_head: 64
            heads: 16
            num_queries: ${model.params.wma_config.params.num_stem_token}
            output_dim: 1024
            ff_mult: 4
            chunk_size: ${model.params.wma_config.params.temporal_length}

    first_stage_config:
      target: unifolm_wma.models.autoencoder.AutoencoderKL
      params:
        embed_dim: 4
        monitor: val/rec_loss
        ddconfig:
          double_z: True
          z_channels: 4
          resolution: 256
          in_channels: 3
          out_ch: 3
          ch: 128
          ch_mult:
          - 1
          - 2
          - 4
          - 4
          num_res_blocks: 2
          attn_resolutions: []
          dropout: 0.0
        lossconfig:
          target: torch.nn.Identity

    cond_stage_config:
      target: unifolm_wma.modules.encoders.condition.FrozenOpenCLIPEmbedder
      params:
        freeze: True
        layer: "penultimate"

    img_cond_stage_config:
      target: unifolm_wma.modules.encoders.condition.FrozenOpenCLIPImageEmbedderV2
      params:
        freeze: true

    image_proj_stage_config:
      target: unifolm_wma.modules.encoders.resampler.Resampler
      params:
        dim: 1024
        depth: 4
        dim_head: 64
        heads: 12
        num_queries: 16
        embedding_dim: 1280
        output_dim: 1024
        ff_mult: 4
        video_length: ${model.params.wma_config.params.temporal_length}

  normalization_config:
    input_shapes:
      observation.state: ${model.params.wma_config.params.unet_head_config.params.input_dim}
    input_normalization_modes:
      observation.state: 'min_max'
    output_shapes:
      action: ${model.params.wma_config.params.unet_head_config.params.input_dim}
    output_normalization_modes:
      action: 'min_max'

data:
  target: unifolm_wma.utils.data.DataModuleFromConfig
  params:
    batch_size: 8
    num_workers: 12
    wrap: False
    train:
      target: unifolm_wma.data.wma_data.WMAData
      params:
        data_dir: '/path/to/training/dataset/directory'
        video_length: ${model.params.wma_config.params.temporal_length}
        frame_stride: 2
        load_raw_resolution: True
        resolution: [320, 512]
        spatial_transform: resize_center_crop
        crop_resolution: [320, 512]
        random_fs: False
        cond_robot_label_prob: 0.0
        normalization_mode: 'min_max'
        individual_normalization: True
        n_obs_steps: ${model.params.n_obs_steps_imagen}
        max_action_dim: ${model.params.agent_action_dim}
        max_state_dim: ${model.params.agent_state_dim}
    dataset_and_weights: 
      unitree_z1_stackbox: 0.2
      unitree_z1_dual_arm_stackbox: 0.2
      unitree_z1_dual_arm_stackbox_v2: 0.2
      unitree_z1_dual_arm_cleanup_pencils: 0.2
      unitree_g1_pack_camera: 0.2

lightning:
  precision: 16
  trainer:
    benchmark: True
    accumulate_grad_batches: 2
    max_steps: 300000
    log_every_n_steps: 50
    val_check_interval: 1.0
    gradient_clip_algorithm: 'norm'
    gradient_clip_val: 0.5
    enable_model_summary: False
  callbacks:
    model_checkpoint:
      target: pytorch_lightning.callbacks.ModelCheckpoint
      params:
        every_n_train_steps: 1000
        filename: "{epoch}-{step}"
        save_weights_only: True
    metrics_over_trainsteps_checkpoint:
      target: pytorch_lightning.callbacks.ModelCheckpoint
      params:
        filename: '{epoch}-{step}'
        save_weights_only: True
        every_n_train_steps: 10000
    batch_logger:
      target: unifolm_wma.utils.callbacks.ImageLogger
      params:
        batch_frequency: 20000
        to_local: False
        max_images: 8
        log_images_kwargs:
          ddim_steps: 16
          unconditional_guidance_scale: 1.0
          timestep_spacing: uniform_trailing
          guidance_rescale: 0.7

```

---

# Hugging Face model card — unitreerobotics/UnifoLM-WMA-0-Dual

---
tags:
- robotics
---

# UnifoLM-WMA-0: A World-Model-Action (WMA) Framework under UnifoLM Family
<p style="font-size: 1.2em;">
    <a href="https://unigen-x.github.io/unifolm-world-model-action.github.io"><strong>Project Page</strong></a> | 
    <a href="https://github.com/unitreerobotics/unifolm-world-model-action"><strong>Code</strong></a> |
    <a href="https://huggingface.co/unitreerobotics/datasets"><strong>Dataset</strong></a> 
  </p>
<div align="center">
  <div align="justify">
    <b>UnifoLM-WMA-0</b> is Unitree‘s first open-source world-model–action architecture spanning multiple types of robotic embodiments, designed specifically for general-purpose robot learning. Its core component is a world-model capable of understanding the physical interactions between robots and the environments. This world-model provides two key functions: (a) <b>Simulation Engine</b> – operates as an interactive simulator to generate synthetic data for robot learning; (b) <b>Policy Enhancement</b> – connects with an action head and, by predicting future interaction processes with the world-model, further optimizes decision-making performance.
  </div>
</div>

## 🦾 Real Robot Deployment
| <img src="assets/real_z1_stackbox.gif" style="border:none;box-shadow:none;margin:0;padding:0;" /> | <img src="assets/real_dual_stackbox.gif" style="border:none;box-shadow:none;margin:0;padding:0;" /> |
|:---:|:---:|
| <img src="assets/real_cleanup_pencils.gif" style="border:none;box-shadow:none;margin:0;padding:0;" /> | <img src="assets/real_g1_pack_camera.gif" style="border:none;box-shadow:none;margin:0;padding:0;" /> |

**Note: the top-right window shows the world model’s prediction of future environmental changes.**

## License
The model is released under the CC BY-NC-SA 4.0 license as found in the [LICENSE](https://huggingface.co/unitreerobotics/UnifoLM-WMA-0/blob/main/LICENSE). You are responsible for ensuring that your use of Unitree AI Models complies with all applicable laws.

## Model Architecture
![Demo](assets/world_model_interaction.gif)

## Citation
```
@misc{unifolm-wma-0,
  author = {Unitree},
  title  = {UnifoLM-WMA-0: A World-Model-Action (WMA) Framework under UnifoLM Family},
  year   = {2025},
}
```
