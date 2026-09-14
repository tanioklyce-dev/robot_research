<!-- airockchip/rknn-llm @ main, captured 2026-09-13. Bundle: README.md, benchmark.md, CHANGELOG.md, LICENSE -->

===== README.md =====
# Description

  RKLLM software stack can help users to quickly deploy AI models to Rockchip chips. The overall framework is as follows:
    <center class="half">
        <div style="background-color:#ffffff;">
        <img src="res/framework.jpg" title="RKLLM"/>
    </center>

  In order to use RKNPU, users need to first run the RKLLM-Toolkit tool on the computer, convert the trained model into an RKLLM format model, and then inference on the development board using the RKLLM C API.

- RKLLM-Toolkit is a software development kit for users to perform model conversionand quantization on PC.

- RKLLM Runtime provides C/C++ programming interfaces for Rockchip NPU platform to help users deploy RKLLM models and accelerate the implementation of LLM applications.

- RKNPU kernel driver is responsible for interacting with NPU hardware. It has been open source and can be found in the Rockchip kernel code.

# Support Platform

- RK3588 Series
- RK3576 Series
- RK3562 Series
- RV1126B Series

# Support Models

- [x] [LLAMA models](https://huggingface.co/meta-llama) 
- [x] [TinyLLAMA models](https://huggingface.co/TinyLlama) 
- [x] [Qwen2/Qwen2.5/Qwen3/Qwen3.5](https://huggingface.co/Qwen)
- [x] [Phi2/Phi3](https://huggingface.co/microsoft)
- [x] [ChatGLM3-6B](https://huggingface.co/THUDM/chatglm3-6b/tree/103caa40027ebfd8450289ca2f278eac4ff26405)
- [x] [Gemma2/Gemma3/Gemma3n/Gemma4](https://huggingface.co/google)
- [x] [InternLM2 models](https://huggingface.co/collections/internlm/internlm2-65b0ce04970888799707893c)
- [x] [MiniCPM3/MiniCPM4](https://huggingface.co/openbmb)
- [x] [TeleChat2](https://huggingface.co/Tele-AI)
- [x] [Qwen2-VL/Qwen3-VL](https://huggingface.co/Qwen)
- [x] [MiniCPM-V-2_6](https://huggingface.co/openbmb/MiniCPM-V-2_6)
- [x] [DeepSeek-R1-Distill](https://huggingface.co/collections/deepseek-ai/deepseek-r1-678e1e131c0169c0bc89728d)
- [x] [Janus-Pro-1B](https://huggingface.co/deepseek-ai/Janus-Pro-1B)
- [x] [InternVL2-1B/InternVL3-1B](https://huggingface.co/OpenGVLab)
- [x] [SmolVLM/SmolLM3](https://huggingface.co/HuggingFaceTB)
- [x] [RWKV7](https://huggingface.co/fla-hub)
- [x] [DeepSeekOCR](https://huggingface.co/deepseek-ai/DeepSeek-OCR)

# Quickstart

The easiest way to try it yourself is to download our multimodal vision model example, this demo runs entirely on your local device using **RKNN** (for vision) and **RKLLM** (for language). you can use your own images and ask questions about them. with **RKLLM**, all processing happens locally on your device-your data never leaves it.

1. Download the pre-converted models and the demo executable (located in the `quickstart` directory) from the following [rkllm_model_zoo](https://console.box.lenovo.com/l/l0tXb8), use the fetch code: `rkllm`.

2.  Open a terminal and push the demo and model files to your local device:

```bash
adb push ./demo_Linux_aarch64 /data
adb push model.rkllm /data/demo_Linux_aarch64
adb push model.rknn /data/demo_Linux_aarch64
```

3. Enter the demo directory and set up environment variables:

```bash
adb shell
cd /data/demo_Linux_aarch64
export LD_LIBRARY_PATH=./lib
```

4. Run the demo

```bash
Usage: ./demo image_path encoder_model_path llm_model_path max_new_tokens max_context_len rknn_core_num platform [img_start] [img_end] [img_content]

# for Qwen2.5-VL
./demo demo.jpg ./qwen2_5_vl_3b_vision_rk3588.rknn ./qwen2.5-vl-3b-w8a8_level1_rk3588.rkllm 2048 4096 3 rk3588 "<|vision_start|>" "<|vision_end|>" "<|image_pad|>"

# for Qwen3-VL
./demo demo.jpg ./qwen3-vl-2b_vision_rk3588.rknn ./qwen3-vl-2b-instruct_w8a8_rk3588.rkllm 2048 4096 3 rk3588 "<|vision_start|>" "<|vision_end|>" "<|image_pad|>"

# for Qwen3.5
./demo demo.jpg ./Qwen3.5-0.8B_vision_rk3588.rknn ./Qwen3.5-0.8B_w8a8_rk3588.rkllm 2048 4096 3 rk3588 "<|vision_start|>" "<|vision_end|>" "<|image_pad|>"

# for InternVL3
./demo demo.jpg ./internvl3-1b_vision_fp16_rk3588.rknn ./internvl3-1b_w8a8_rk3588.rkllm 2048 4096 3 rk3588 "<img>" "</img>" "<IMG_CONTEXT>"

# for DeepSeekOCR
./demo demo.jpg ./deepseekocr_vision_rk3588.rknn ./deepseekocr_w8a8_rk3588.rkllm 2048 4096 3 rk3588 "" "" "<｜▁pad▁｜>"
```

   `[img_start]`, `[img_end]`, and `[img_content]` need to be checked in the model’s configuration file.

   For example, in **InternVL3**, you can find them in `modeling_internvl_chat.py` as shown below:

   ```
   def chat(self, tokenizer, pixel_values, question, generation_config, history=None, return_history=False,
            num_patches_list=None, IMG_START_TOKEN='<img>', IMG_END_TOKEN='</img>', IMG_CONTEXT_TOKEN='<IMG_CONTEXT>',
            verbose=False):
   ```

# Model Performance

1.  [Benchmark](https://github.com/airockchip/rknn-llm/tree/main/benchmark.md) results of common LLMs.

# **Performance Testing Methods**

1. Run the frequency-setting script from the `scripts` directory on the target platform.
2. Execute `export RKLLM_LOG_LEVEL=1` on the device to log model inference performance and memory usage.
3. Use the `eval_perf_watch_cpu.sh` script to measure CPU utilization.
4. Use the `eval_perf_watch_npu.sh` script to measure NPU utilization.

# Download

1. You can download the **latest package** from [RKLLM_SDK](https://console.zbox.filez.com/l/RJJDmB), fetch code: rkllm
2. You can download the **converted rkllm model**  from [rkllm_model_zoo](https://console.box.lenovo.com/l/l0tXb8), fetch code: rkllm

# Examples

1. Multimodal deployment demo:   [multimodal_model_demo](https://github.com/airockchip/rknn-llm/tree/main/examples/multimodal_model_demo)
2. API usage demo:  [rkllm_api_demo](https://github.com/airockchip/rknn-llm/tree/main/examples/rkllm_api_demo)
3. API server demo:  [rkllm_server_demo](https://github.com/airockchip/rknn-llm/tree/main/examples/rkllm_server_demo)

# Note

- The supported Python versions are:

  - Python 3.9
  - Python 3.10
  - Python 3.11
  - Python 3.12

**Note: Before installing package in a Python 3.12 environment, please run the command:**

```
export BUILD_CUDA_EXT=0
```
- On some platforms, you may encounter an error indicating that **libomp.so** cannot be found. To resolve this, locate the library in the corresponding cross-compilation toolchain and place it in the board's lib directory, at the same level as librkllmrt.so.
- RWKV model conversion only supports Python 3.12. Please use `requirements_rwkv7.txt` to set up the pip environment.
- Latest version: [ <u>v1.3.0](https://github.com/airockchip/rknn-llm/releases/tag/release-v1.3.0)</u>

# RKNN Toolkit2

If you want to deploy additional AI model, we have introduced a SDK called RKNN-Toolkit2. For details, please refer to:

https://github.com/airockchip/rknn-toolkit2

# CHANGELOG

## v1.3.0

- Added support for Qwen3.5, Gemma4, and SmolLM3 models.
- Optimized the multimodal input interface and cache reuse strategy.
- Added support for multiple EOS token IDs and introduced the ignore_eos_token parameter.
- Optimized performance on 32-bit systems.
- Added support for tokenizer and embedding callbacks.
- Improved long-context decoding performance for certain models on the RK3576 platform.
- Optimized the quantization method for embedding input data.
- Fixed memory usage statistics issues on the RV1126B platform.
- Fixed numerical overflow issues during inference for certain models on the RK3588 platform.
- Improved  rkllm_server_demo compatibility with OpenAI API interfaces.
- Added support for overriding max_new_tokens and sampling parameters in RKLLMInferParam

for older version, please refer [CHANGELOG](CHANGELOG.md)
===== benchmark.md =====
# Model Performance Benchmark

- This performance data were collected based on the maximum CPU and NPU frequencies of each platform. 
- The script for setting the frequencies is located in the scripts directory.
- All models should be converted with `optimization_level` set to 0 to enable optimized runtime performance.

### RK3588

| Model       | Model Size | Dtype | Seqlen | New_tokens | TTFT(ms) | Tokens/s | memory(MB) |
| :---------- | :--------: | :---: | :----: | :--------: | :------: | :------: | :--------: |
| Qwen2       |    0.5B    | w8a8  |  128   |     64     |  145.90  |  41.58   |   669.56   |
| MiniCPM4    |    0.5B    | w8a8  |  128   |     64     |  135.29  |  45.34   |   534.82   |
| Qwen3       |    0.6B    | w8a8  |  128   |     64     |  199.09  |  32.91   |   791.11   |
| TinyLLAMA   |    1.1B    | w8a8  |  128   |     64     |  243.93  |  24.43   |  1093.66   |
| Qwen2.5     |    1.5B    | w8a8  |  128   |     64     |  378.31  |  16.69   |  1689.21   |
| RWKV7       |    1.5B    | w8a8  |  128   |     64     |  634.34  |  13.82   |  1486.19   |
| InternLM2   |    1.8B    | w8a8  |  128   |     64     |  380.14  |  15.45   |  1775.56   |
| Gemma2      |     2B     | w8a8  |  128   |     64     |  598.41  |  10.37   |  2779.22   |
| Gemma3n     |     2B     | w8a8  |  128   |     64     | 1124.51  |   9.91   |  2702.59   |
| TeleChat2   |     3B     | w8a8  |  128   |     64     |  618.48  |  10.18   |  2788.39   |
| Phi3        |    3.8B    | w8a8  |  128   |     64     | 1017.28  |   7.45   |  3758.34   |
| MiniCPM3    |     4B     | w8a8  |  128   |     64     | 1408.49  |   5.94   |  4384.02   |
| ChatGLM3    |     6B     | w8a8  |  128   |     64     | 1352.94  |   4.98   |  5985.99   |
| Qwen3-VL    |     2B     | w8a8  |  128   |     64     |  383.62  |  14.98   |  1868.98   |
| DeepSeekOCR | 3B(A570M)  | w8a8  |  128   |     64     |  701.21  |  31.60   |  3066.66   |
| Qwen3.5     |    0.8B    | w8a8  |  128   |     64     |  587.74  |  27.05   |  1039.66   |
|             |     2B     | w8a8  |  128   |     64     |  776.95  |  13.59   |  2121.91   |
|             |     4B     | w8a8  |  128   |     64     | 2068.88  |   6.22   |  4575.78   |
| Gemma4      |    E2B     | w8a8  |  128   |     64     |  599.06  |  11.12   |  2498.70   |

### RK3576

| Model       | Model Size |   Dtype    | Seqlen | New_tokens | TTFT(ms) | Tokens/s | memory(MB) |
| :---------- | :--------: | :--------: | :----: | :--------: | :------: | :------: | :--------: |
| Qwen2       |    0.5B    |   w4a16    |  128   |     64     |  342.37  |  32.56   |   443.44   |
|             |    0.5B    | w4a16_g128 |  128   |     64     |  361.78  |  30.33   |   463.23   |
|             |    0.5B    |    w8a8    |  128   |     64     |  344.27  |  21.73   |   678.43   |
| MiniCPM4    |    0.5B    |   w4a16    |  128   |     64     |  330.80  |  34.57   |   334.68   |
|             |    0.5B    | w4a16_g128 |  128   |     64     |  359.16  |  32.66   |   374.36   |
|             |    0.5B    |    w8a8    |  128   |     64     |  321.12  |  23.28   |   541.17   |
| Qwen3       |    0.6B    |   w4a16    |  128   |     64     |  468.61  |  24.85   |   512.71   |
|             |    0.6B    | w4a16_g128 |  128   |     64     |  506.41  |  23.48   |   545.35   |
|             |    0.6B    |    w8a8    |  128   |     64     |  461.54  |  17.17   |   796.26   |
| TinyLLAMA   |    1.1B    |   w4a16    |  128   |     64     |  543.68  |  19.71   |   601.09   |
|             |    1.1B    | w4a16_g128 |  128   |     64     |  672.61  |  18.08   |   690.76   |
|             |    1.1B    |    w8a8    |  128   |     64     |  534.13  |  12.18   |  1092.87   |
| RWKV7       |    1.5B    |   w4a16    |  128   |     64     | 1572.09  |  10.18   |   835.34   |
|             |    1.5B    | w4a16_g128 |  128   |     64     | 1733.08  |   9.49   |   925.54   |
|             |    1.5B    |    w8a8    |  128   |     64     | 1534.47  |   7.05   |  1494.13   |
| InternLM2   |    1.8B    |   w4a16    |  128   |     64     |  765.92  |  13.55   |   975.04   |
|             |    1.8B    | w4a16_g128 |  128   |     64     |  986.14  |  12.05   |  1070.44   |
|             |    1.8B    |    w8a8    |  128   |     64     |  750.31  |   7.86   |  1782.05   |
| Gemma2      |     2B     |   w4a16    |  128   |     64     |  997.92  |   9.14   |  1542.14   |
|             |     2B     | w4a16_g128 |  128   |     64     | 1312.15  |   8.27   |  1629.59   |
|             |     2B     |    w8a8    |  128   |     64     |  956.77  |   5.24   |  2784.78   |
| Gemma-3n    |     2B     |   w4a16    |  128   |     64     | 3260.05  |   7.78   |  1577.52   |
|             |     2B     |    w8a8    |  128   |     64     | 2995.26  |   4.90   |  2715.83   |
| TeleChat2   |     3B     |   w4a16    |  128   |     64     | 1153.96  |   8.97   |  1525.80   |
|             |     3B     | w4a16_g128 |  128   |     64     | 1408.37  |   8.14   |  1644.32   |
|             |     3B     |    w8a8    |  128   |     64     | 1029.04  |   5.12   |  2794.56   |
| Phi3        |    3.8B    |   w4a16    |  128   |     64     | 1829.12  |   6.58   |  1995.78   |
|             |    3.8B    | w4a16_g128 |  128   |     64     | 2253.14  |   6.06   |  2151.47   |
|             |    3.8B    |    w8a8    |  128   |     64     | 1615.97  |   3.74   |  3767.28   |
| MiniCPM3    |     4B     |   w4a16    |  128   |     64     | 2536.68  |   4.87   |  2380.24   |
|             |     4B     | w4a16_g128 |  128   |     64     | 3117.53  |   4.46   |  2660.66   |
|             |     4B     |    w8a8    |  128   |     64     | 2539.92  |   3.01   |  4410.50   |
| ChatGLM3    |     6B     |   w4a16    |  128   |     64     | 2166.69  |   4.63   |  3023.39   |
|             |     6B     | w4a16_g128 |  128   |     64     | 2966.85  |   4.14   |  3253.12   |
|             |     6B     |    w8a8    |  128   |     64     | 1948.12  |   2.48   |  5967.63   |
| Qwen3-VL    |     2B     |   w4a16    |  128   |     64     |  802.94  |  12.68   |  1058.56   |
|             |     2B     | w4a16_g128 |  128   |     64     |  983.20  |  11.42   |  1146.77   |
|             |     2B     |    w8a8    |  128   |     64     |  785.79  |   7.62   |  1876.62   |
| DeepSeekOCR | 3B(A570M)  |   w4a16    |  128   |     64     | 1034.97  |  24.38   |  1790.30   |
|             | 3B(A570M)  |    w8a8    |  128   |     64     | 1242.78  |  17.26   |  3109.59   |
| Qwen3.5     |    0.8B    |   w4a16    |  128   |     64     | 1369.31  |  18.79   |   689.50   |
|             |    0.8B    | w4a16_g128 |  128   |     64     | 1392.09  |  17.88   |   687.38   |
|             |    0.8B    |    w8a8    |  128   |     64     | 1342.54  |  13.18   |  1047.08   |
| Qwen3.5     |     2B     |   w4a16    |  128   |     64     | 1661.01  |  11.03   |  1236.12   |
|             |     2B     | w4a16_g128 |  128   |     64     | 1852.42  |  10.10   |  1280.15   |
|             |     2B     |    w8a8    |  128   |     64     | 1678.11  |   6.73   |  2131.55   |
| Qwen3.5     |     4B     |   w4a16    |  128   |     64     | 3976.41  |   5.02   |  2420.34   |
|             |     4B     | w4a16_g128 |  128   |     64     | 4476.37  |   4.60   |  2564.89   |
|             |     4B     |    w8a8    |  128   |     64     | 3906.19  |   3.03   |  4591.72   |
| Gemma4      |    E2B     |   w4a16    |  128   |     64     | 1219.25  |   9.23   |  1463.42   |
|             |    E2B     | w4a16_g128 |  128   |     64     | 1445.36  |   8.27   |  1564.91   |
|             |    E2B     |    w8a8    |  128   |     64     | 1166.94  |   5.56   |  2548.73   |

### RK3562

| Model    | Model Size | Dtype | Seqlen | New_tokens | TTFT(ms) | Tokens/s | memory(MB) |
| :------- | :--------: | :---: | :----: | :--------: | :------: | :------: | :--------: |
| Qwen2    |    0.5B    | w8a8  |  128   |     64     |  640.65  |  13.56   |   647.63   |
| MiniCPM4 |    0.5B    | w8a8  |  128   |     64     |  676.77  |  10.07   |   511.48   |
| Qwen3    |    0.6B    | w8a8  |  128   |     64     |  881.86  |  10.94   |   773.44   |
| Qwen3.5  |    0.8B    | w8a8  |  128   |     64     | 3750.55  |   7.69   |  1020.72   |

### RV1126B

| Model    | Model Size |   Dtype    | Seqlen | New_tokens | TTFT(ms) | Tokens/s | memory(MB) |
| :------- | :--------: | :--------: | :----: | :--------: | :------: | :------: | :--------: |
| Qwen2    |    0.5B    |   w4a16    |  128   |     64     |  656.86  |  20.91   |   410.82   |
|          |    0.5B    | w4a16_g128 |  128   |     64     |  687.00  |  17.69   |   391.32   |
|          |    0.5B    |    w8a8    |  128   |     64     |  651.31  |  13.63   |   646.17   |
| MiniCPM4 |    0.5B    |   w4a16    |  128   |     64     |  680.03  |  23.24   |   302.85   |
|          |    0.5B    | w4a16_g128 |  128   |     64     |  693.41  |  19.24   |   301.88   |
|          |    0.5B    |    w8a8    |  128   |     64     |  665.94  |  15.16   |   509.6    |
| Qwen3    |    0.6B    |   w4a16    |  128   |     64     |  956.32  |  15.04   |   488.64   |
|          |    0.6B    | w4a16_g128 |  128   |     64     | 1017.06  |  12.53   |   473.77   |
|          |    0.6B    |    w8a8    |  128   |     64     |  944.30  |  10.22   |   773.11   |
| Qwen3.5  |    0.8B    |   w4a16    |  128   |     64     | 4359.89  |  10.18   |   659.16   |
|          |    0.8B    | w4a16_g128 |  128   |     64     | 4560.21  |   9.07   |   616.98   |
|          |    0.8B    |    w8a8    |  128   |     64     | 4392.52  |   7.23   |  1017.12   |

### Multimodal

| model                 |        Stage         |  RK3588(w8a8)  | RK3576(w4a16)  |
| :-------------------- | :------------------: | :------------: | :------------: |
| Qwen2-VL-2B           | img-encoder(392*392) |     3.28s      |     3.55s      |
|                       |   Prefill(len=196)   |    632.6ms     |    1234.9ms    |
|                       |        Decode        | 16.6 tokens/s  | 14.57 tokens/s |
| Qwen2.5-VL-3B         | img-encoder(392*392) |     2.93s      |     2.87s      |
|                       |   Prefill(len=196)   |     1120ms     |     2130ms     |
|                       |        Decode        | 8.66 tokens/s  | 7.87 tokens/s  |
| MiniCPM-V-2_6         | img-encoder(448*448) |     3.27s      |      2.4s      |
|                       |   Prefill(len=64)    |     826ms      |     1230ms     |
|                       |        Decode        | 4.18 tokens/s  | 3.85 tokens/s  |
| SmolVLM-256M          | Img-encoder(512*512) |     842ms      |     768ms      |
|                       |   Prefill(len=128)   |     77.3ms     |     180ms      |
|                       |        Decode        |  78 tokens/s   | 57.73tokens/s  |
| Qwen3-VL-2B           | img-encoder(448*448) |     2.08s      |     1.61s      |
|                       |   Prefill(len=196)   |     649ms      |     1587ms     |
|                       |        Decode        | 14.91 tokens/s | 10.36 tokens/s |
| DeepSeekOCR-3B(A570M) | Img-encoder(448*448) |     2.09s      |     2.27s      |
|                       |   Prefill(len=128)   |     696ms      |     1010ms     |
|                       |        Decode        | 31.8 tokens/s  | 22.3 tokens/s  |
| Qwen3.5-0.8B          | Img-encoder(448*448) |     690ms      |     815ms      |
|                       |   Prefill(len=216)   |     1.56s      |      3.4s      |
|                       |        Decode        |  27 tokens/s   | 15.4 tokens/s  |

- The img-encoder runs inference on RKNN with FP16, tested using all NPU cores.
===== CHANGELOG.md =====
# CHANGELOG
## v1.3.0

- Added support for Qwen3.5, Gemma4, and SmolLM3 models.
- Optimized the multimodal input interface and cache reuse strategy.
- Added support for multiple EOS token IDs and introduced the ignore_eos_token parameter.
- Optimized performance on 32-bit systems.
- Added support for tokenizer and embedding callbacks.
- Improved long-context decoding performance for certain models on the RK3576 platform.
- Optimized the quantization method for embedding input data.
- Fixed memory usage statistics issues on the RV1126B platform.
- Fixed numerical overflow issues during inference for certain models on the RK3588 platform.
- Improved  rkllm_server_demo compatibility with OpenAI API interfaces.
- Added support for overriding max_new_tokens and sampling parameters in RKLLMInferParam

## v1.2.3

- Added support for InternVL3.5, DeepSeekOCR, and Qwen3-VL models
- Added automatic cache reuse for embedding input
- Added embedding input support for the Gemma3n model
- Added support for loading chat template from an external file

## v1.2.2

- Added support for Gemma3n and InternVL3 models
- Supported for multi-instance inference
- Supported for LongRoPE
- Fixed issues with asynchronous inference interfaces
- Fixed chat template parsing issues
- Optimized inference performance
- Optimized  multimodal vision model demo

## v1.2.1

- Added support for RWKV7, Qwen3, and MiniCPM4 models
- Added support for the RV1126B platform
- Enabled function calling capability
- Enabled cross-attention inference
- Optimize the callback function to support pausing inference
- Supported multi-batch inference
- Optimized KV cache clearing interface
- Improved chat template parsing with support for thinking mode selection
- Server demo updated to support OpenAI-compatible format
- Added return of model inference performance statistics
- Supported mrope multimodal position encoding
- A new quantization optimization algorithm has been added to improve quantization accuracy

## v1.2.0

- Supports custom model conversion.
- Supports chat_template configuration.
- Enables multi-turn dialogue interactions.
- Implements automatic prompt cache reuse for improved inference efficiency.
- Expands maximum context length to 16K.
- Supports embedding flash storage to reduce memory usage.
- Introduces the GRQ Int4 quantization algorithm.
- Supports GPTQ-Int8 model conversion.
- Compatible with the RK3562 platform.
- Added support for visual multimodal models such as InternVL2, Janus, and Qwen2.5-VL.
- Supports CPU core configuration.
- Added support for Gemma3
- Added support for Python 3.9/3.11/3.12

## v1.1.0
- Support group-wise quantization (w4a16 group sizes of 32/64/128, w8a8 group sizes of 128/256/512).
- Support joint inference with LoRA model loading
- Support storage and preloading of prompt cache.
- Support gguf model conversion (currently only support q4_0 and fp16).
- Optimize initialization, prefill, and decode time.
- Support four input types: prompt, embedding, token, and multimodal.
- Add PC-based simulation accuracy testing and inference interface support for rkllm-toolkit.
- Add gdq algorithm to improve 4-bit quantization accuracy.
- Add mixed quantization algorithm, supporting a combination of grouped and non-grouped quantization based on specified ratios.
- Add support for models such as Llama3, Gemma2, and MiniCPM3.
- Resolve catastrophic forgetting issue when the number of tokens exceeds max_context.

## v1.0.1
 - Optimize model conversion memory occupation
 - Optimize inference memory occupation
 - Increase prefill speed
 - Reduce initialization time
 - Improve quantization accuracy
 - Add support for Gemma, ChatGLM3, MiniCPM, InternLM2, and Phi-3
 - Add Server invocation
 - Add inference interruption interface
 - Add logprob and token_id to the return value

## v1.0.0
 - Support the conversion and deployment of LLM models on RK3588/RK3576 platforms
 - Compatible with Hugging Face model architectures
 - Currently support the models Llama, Qwen, Qwen2, and Phi-2
 - Support quantization with w8a8 and w4a16 precision
===== LICENSE =====
Copyright (c) Rockchip Electronics Co., Ltd.
All rights reserved.

// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
// 1. Redistributions of source code must retain the above copyright notice,
// this list of conditions and the following disclaimer.
//
// 2. Redistributions in binary form must reproduce the above copyright notice,
// this list of conditions and the following disclaimer in the documentation
// and/or other materials provided with the distribution.
//
// 3. Neither the name of the copyright holder nor the names of its contributors
// may be used to endorse or promote products derived from this software without
// specific prior written permission.
//
// 4. This Software may contain some Open Source Software. You may not redistribute 
// and/or modify such Open Source Software except in compliance with the applicable 
// Open Source License.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
// ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
// LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
// CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
// CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
// ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
// POSSIBILITY OF SUCH DAMAGE.

The following Open Source Software have been modified by Rockchip Electronics Co., Ltd. 
----------------------------------------------------------------------------------------
1. ggml  master
Copyright (c) 2023-2025 The ggml authors
All rights reserved.
Licensed under the terms of the MIT License

2. llama.cpp  master
Copyright (c) 2023-2025 The ggml authors
All rights reserved.
Licensed under the terms of the MIT License 

The terms of the MIT License:
--------------------------------------------------------------------
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.