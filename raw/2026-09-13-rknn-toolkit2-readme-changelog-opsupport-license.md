<!-- airockchip/rknn-toolkit2 @ master, captured 2026-09-13. Bundle: README.md, CHANGELOG.md, doc/RKNNToolKit2_OP_Support-2.3.2.md, LICENSE -->

===== README.md =====
# Description
  RKNN software stack can help users to quickly deploy AI models to Rockchip chips. The overall framework is as follows:
    <center class="half">
        <div style="background-color:#ffffff;">
        <img src="res/framework.png" title="RKNN"/>
    </center>

  In order to use RKNPU, users need to first run the RKNN-Toolkit2 tool on the computer, convert the trained model into an RKNN format model, and then inference on the development board using the RKNN C API or Python API.

- RKNN-Toolkit2 is a software development kit for users to perform model conversion, inference and performance evaluation on PC and Rockchip NPU platforms.

- RKNN-Toolkit-Lite2 provides Python programming interfaces for Rockchip NPU platform to help users deploy RKNN models and accelerate the implementation of AI applications.

- RKNN Runtime provides C/C++ programming interfaces for Rockchip NPU platform to help users deploy RKNN models and accelerate the implementation of AI applications.

- RKNPU kernel driver is responsible for interacting with NPU hardware. It has been open source and can be found in the Rockchip kernel code.

# Support Platform
  - RK3588 Series
  - RK3576 Series
  - RK3566/RK3568 Series
  - RK3562 Series
  - RV1103/RV1106
  - RV1103B/RV1106B
  - RV1126B
  - RK2118


Note:

​      **For RK1808/RV1109/RV1126/RK3399Pro, please refer to :**

​          https://github.com/airockchip/rknn-toolkit

​          https://github.com/airockchip/rknpu

​          https://github.com/airockchip/RK3399Pro_npu


# Download
- You can also download all packages, docker image, examples, docs and platform-tools from [RKNPU2_SDK](https://console.zbox.filez.com/l/I00fc3), fetch code: rknn
- You can get more examples from [rknn mode zoo](https://github.com/airockchip/rknn_model_zoo)

# Notes
- RKNN-Toolkit2 is not compatible with [RKNN-Toolkit](https://github.com/airockchip/rknn-toolkit)
- The supported Python versions are:
  - Python 3.6
  - Python 3.7
  - Python 3.8
  - Python 3.9
  - Python 3.10
  - Python 3.11
  - Python 3.12
- Latest version:v2.3.2



# RKNN LLM

If you want to deploy LLM (Large Language Model), we have introduced a new SDK called RKNN-LLM. For details, please refer to:

https://github.com/airockchip/rknn-llm



# CHANGELOG

## v2.3.2
- Support for RV1126B platform
- Improved einsum and Norm operations support
- Added automatic mixed precision functionality
- Enhanced graph optimization capabilities
      

 for older version, please refer [CHANGELOG](CHANGELOG.md)

# Feedback and Community Support
- [Redmine](https://redmine.rock-chips.com) (**Feedback recommended, Please consult our sales or FAE for the redmine account**)
- QQ Group Chat: 1025468710 (full, please join group 4)
- QQ Group Chat2: 547021958 (full, please join group 4)
- QQ Group Chat3: 469385426 (full, please join group 4)
- QQ Group Chat4: 958083853
<center class="half">
  <img width="200" height="200"  src="res/QQGroupQRCode.png" title="QQ Group Chat"/>
  <img width="200" height="200"  src="res/QQGroup2QRCode.png" title="QQ Group Chat2"/>
  <img width="200" height="200"  src="res/QQGroup3QRCode.png" title="QQ Group Chat3"/>
  <img width="200" height="200"  src="res/QQGroup4QRCode.png" title="QQ Group Chat4"/>
</center>



===== CHANGELOG.md =====
# CHANGELOG

## v2.3.2

- Support for RV1126B platform

- Improved einsum and Norm operations support

- Added automatic mixed precision functionality

- Enhanced graph optimization capabilities



## v2.3.0

- RKNN-Toolkit2 support ARM64 architecture

- RKNN-Toolkit-Lite2 support installation via pip

- Add support for W4A16 symmetric quantization (RK3576)

- Operator optimization, such as LayerNorm, LSTM, Transpose, MatMul, etc.



## v2.2.0

- Support installation via pip

- Optimize transformer model performance

- Support Python 3.12

- Operator optimization, such as softmax, hardmax, MatMul, etc.



## v2.1.0

- Support RV1103B (Beta)

- Support RK2118 (Beta)

- Support Flash Attention (Only RK3562 and RK3576)

- Improve MatMul API

- Improve support for int32 and int64

- Support more operators and operator fusion

 

## v2.0.0-beta0

 - Support RK3576 (Beta)
 - Support RK2118 (Beta)
 - Support SDPA (Scaled Dot Product Attention) to improve transformer performance
 - Improve custom operators support
 - Improve MatMul API
 - Improve support for Reshape,Transpose,BatchLayernorm,Softmax,Deconv,Matmul,ScatterND etc.
 - Support pytorch 2.1
 - Improve support for QAT models of pytorch and onnx
 - Optimize automatic generation of C++ code



## v1.6.0

 - Support ONNX model of OPSET 12~19
 - Support custom operators (including CPU and GPU)
 - Improve support for dynamic weight convolution, Layernorm, RoiAlign, Softmax, ReduceL2, Gelu, GLU, etc.
 - Added support for python3.7/3.9/3.11
 - Add rknn_convert function
 - Improve transformer support
 - Improve MatMul API, such as increasing the K limit length, RK3588 adding int4 * int4 -> int16 support, etc.
 - Reduce RV1106 rknn_init initialization time, memory consumption, etc.
 - RV1106 adds int16 support for some operators
 - Fixed the problem that the convolution operator of RV1106 platform may make random errors in some cases.
 - Improve user manual
 - Reconstruct the rknn model zoo and add support for multiple models such as detection, segmentation, OCR, and license plate recognition.



## v1.5.2

- Improve dynamic shape support
- Improve matmul api support
- Add GPU back-end implementations for some operators such as matmul
- Improve transformer support
- Reduce rknn_init memory usage
- Optimize rknn_init time-consuming



## v1.5.0

- Support RK3562
- Support more NPU operator fuse, such as Conv-Silu/Conv-Swish/Conv-Hardswish/Conv-sigmoid/Conv-HardSwish/Conv-Gelu ..
- Improve support for  NHWC output layout
- RK3568/RK3588：The maximum input resolution up to 8192
- Improve support for Swish/DataConvert/Softmax/Lstm/LayerNorm/Gather/Transpose/Mul/Maxpool/Sigmoid/Pad
- Improve support for CPU operators (Cast, Sin, Cos, RMSNorm, ScalerND, GRU)
- Limited support for dynamic resolution
- Provide MATMUL API
- Add RV1103/RV1106 rknn_server application as proxy between PC and board
- Add more examples such as rknn_dynamic_shape_input_demo and video demo for yolov5
- Bug fix



## v1.4.0

- Support more NPU operators, such as Reshape、Transpose、MatMul、 Max、Min、exGelu、exSoftmax13、Resize etc.

- Add **Weight Share**  function, reduce memory usage.

- Add **Weight Compression** function, reduce memory and bandwidth usage.(RK3588/RV1103/RV1106)

- RK3588 supports storing weights or feature maps on SRAM, reducing system bandwidth consumption.

- RK3588 adds the function of running a single model on multiple cores at the same time.

- Add new output layout NHWC (C has alignment restrictions) .

- Improve support for non-4D input.

- Add more examples such as rknn_yolov5_android_apk_demo and rknn_internal_mem_reuse_demo.

- Bug fix.



## v1.3.0

- Support RV1103/RV1106（Beta SDK）
- rknn_tensor_attr support w_stride(rename from stride) and h_stride
- Rename rknn_destroy_mem()
- Support more NPU operators, such as Where, Resize, Pad, Reshape, Transpose etc.
- RK3588 support multi-batch multi-core mode
- When RKNN_LOG_LEVEL=4, it supports to display the MACs utilization and bandwidth occupation of each layer.
- Bug fix



## v1.2.0

- Support RK3588
- Support more operators, such as GRU、Swish、LayerNorm etc.
- Reduce memory usage
- Improve zero-copy interface implementation
- Bug fix



## v1.1.0

- Support INT8+FP16 mixed quantization to improve model accuracy
- Support specifying input and output dtype, which can be solidified into the model
- Support multiple inputs of the model with different channel mean/std
- Improve the stability of multi-thread + multi-process runtime
- Support flashing cache for fd pointed to internal tensor memory which are allocated by users
- Improve dumping internal layer results of the model
- Add rknn_server application as proxy between PC and board
- Support more operators, such as HardSigmoid、HardSwish、Gather、ReduceMax、Elu
- Add LSTM support (structure cifg and peephole are not supported, function: layernormal, clip is not supported)
- Bug fix



## v1.0

- Optimize the performance of rknn_inputs_set()
- Add more functions for zero-copy
- Add new OP support, see OP support list document for details.
- Add multi-process support
- Support per-channel quantitative model
- Bug fix



## v0.7

- Optimize the performance of rknn_inputs_set(), especially for models whose input width is 8-byte aligned.

- Add new OP support, see OP support list document for details.

- Bug fix



## v0.6
- Initial version


===== doc/RKNNToolKit2_OP_Support-2.3.2.md =====
# RKNNToolkit2 OPs Support

## ONNX OPs supported by RKNN Toolkit2

According to [ONNX official instructions](https://github.com/microsoft/onnxruntime/blob/master/docs/Versioning.md 'ONNX Version Description'), the corresponding ONNX opset version is 19.
The list of ONNX OPs supported by RKNN Toolkit2 is as follows:
<br>(For more restrictions, please refer to <RKNN_Compiler_Support_Operator_List>)

| **Operators**             | **Remarks**                             |
| ------------------------- | --------------------------------------- |
| Abs                       | Not Supported                           |
| Acos                      | Not Supported                           |
| Acosh                     | Not Supported                           |
| Add                       |                                         |
| And                       |                                         |
| ArgMax                    |                                         |
| ArgMin                    |                                         |
| Asin                      | Not Supported                           |
| Asinh                     | Not Supported                           |
| Atan                      | Not Supported                           |
| Atanh                     | Not Supported                           |
| AveragePool               |                                         |
| BatchNormalization        |                                         |
| Bernoulli                 | Not Supported                           |
| BitShift                  | Not Supported                           |
| BitwiseAnd                | Not Supported                           |
| BitwiseNot                | Not Supported                           |
| BitwiseOr                 | Not Supported                           |
| BitwiseXor                | Not Supported                           |
| BlackmanWindow            | Not Supported                           |
| Cast                      |                                         |
| CastLike                  | Not Supported                           |
| Ceil                      | Not Supported                           |
| Celu                      | Not Supported                           |
| CenterCropPad             | Not Supported                           |
| Clip                      |                                         |
| Col2Im                    | Not Supported                           |
| Compress                  | Not Supported                           |
| Concat                    |                                         |
| ConcatFromSequence        | Not Supported                           |
| Constant                  |                                         |
| ConstantOfShape           |                                         |
| Conv                      |                                         |
| ConvInteger               | Not Supported                           |
| ConvTranspose             |                                         |
| Cos                       |                                         |
| Cosh                      | Not Supported                           |
| CumSum                    | Not Supported                           |
| DeformConv                | Not Supported                           |
| DepthToSpace              |                                         |
| DequantizeLinear          |                                         |
| Det                       | Not Supported                           |
| DFT                       | Not Supported                           |
| Div                       |                                         |
| Dropout                   |                                         |
| DynamicQuantizeLinear     | Not Supported                           |
| Einsum                    | Not Supported                           |
| Elu                       |                                         |
| Equal                     |                                         |
| Erf                       |                                         |
| Exp                       |                                         |
| Expand                    |                                         |
| EyeLike                   | only support constant input             |
| Flatten                   |                                         |
| Floor                     |                                         |
| Gather                    |                                         |
| GatherElements            |                                         |
| GatherND                  | Not Supported                           |
| Gemm                      |                                         |
| GlobalAveragePool         |                                         |
| GlobalLpPool              | Not Supported                           |
| GlobalMaxPool             |                                         |
| Greater                   |                                         |
| GreaterOrEqual            |                                         |
| GridSample                | Not Supported                           |
| GroupNormalization        | Not Supported                           |
| GRU                       | batchsize: 1                            |
| HammingWindow             | Not Supported                           |
| HannWindow                | Not Supported                           |
| Hardmax                   | Not Supported                           |
| HardSigmoid               |                                         |
| HardSwish                 |                                         |
| Identity                  |                                         |
| If                        | only support constant input             |
| InstanceNormalization     |                                         |
| IsInf                     | Not Supported                           |
| IsNaN                     | Not Supported                           |
| LayerNormalization        |                                         |
| LeakyRelu                 |                                         |
| Less                      |                                         |
| LessOrEqual               |                                         |
| Log                       |                                         |
| LogSoftmax                | batchsize: 1                            |
| Loop                      | Not Supported                           |
| LpNormalization           |                                         |
| LpPool                    | Not Supported                           |
| LRN                       |                                         |
| LSTM                      |                                         |
| MatMul                    |                                         |
| MatMulInteger             | Not Supported                           |
| Max                       |                                         |
| MaxPool                   |                                         |
| MaxRoiPool                |                                         |
| MaxUnpool                 |                                         |
| Mean                      | Not Supported                           |
| MeanVarianceNormalization |                                         |
| MelWeightMatrix           | Not Supported                           |
| Min                       |                                         |
| Mish                      |                                         |
| Mod                       |                                         |
| Mul                       |                                         |
| Multinomial               | Not Supported                           |
| Neg                       | Not Supported                           |
| NegativeLogLikelihoodLoss | Not Supported                           |
| NonMaxSuppression         | Not Supported                           |
| NonZero                   | Not Supported                           |
| Not                       | Not Supported                           |
| OneHot                    | Not Supported                           |
| Optional                  | Not Supported                           |
| OptionalGetElement        | Not Supported                           |
| OptionalHasElement        | Not Supported                           |
| Or                        | Not Supported                           |
| Pad                       |                                         |
| Pow                       |                                         |
| PRelu                     |                                         |
| QLinearConv               | Not Supported                           |
| QLinearMatMul             | Not Supported                           |
| QuantizeLinear            |                                         |
| RandomNormal              | Not Supported                           |
| RandomNormalLike          | Not Supported                           |
| RandomUniform             | Not Supported                           |
| RandomUniformLike         | Not Supported                           |
| Range                     | Not Supported                           |
| Reciprocal                | Not Supported                           |
| ReduceL1                  | Not Supported                           |
| ReduceL2                  | Not Supported                           |
| ReduceLogSum              | Not Supported                           |
| ReduceLogSumExp           | Not Supported                           |
| ReduceMax                 |                                         |
| ReduceMean                |                                         |
| ReduceMin                 |                                         |
| ReduceProd                | Not Supported                           |
| ReduceSum                 |                                         |
| ReduceSumSquare           | Not Supported                           |
| Relu                      |                                         |
| Reshape                   |                                         |
| Resize                    | mode: nearest2d/bilinear                |
| ReverseSequence           |                                         |
| RNN                       | Not Supported                           |
| RoiAlign                  | pool type: average<br />batchsize: 1    |
| Round                     | Not Supported                           |
| Scan                      | Not Supported                           |
| ScatterElements           | Not Supported                           |
| ScatterND                 |                                         |
| Selu                      | Not Supported                           |
| SequenceAt                | Not Supported                           |
| SequenceConstruct         | Not Supported                           |
| SequenceEmpty             | Not Supported                           |
| SequenceErase             | Not Supported                           |
| SequenceInsert            | Not Supported                           |
| SequenceLength            | Not Supported                           |
| SequenceMap               | Not Supported                           |
| Shape                     |                                         |
| Shrink                    | Not Supported                           |
| Sigmoid                   |                                         |
| Sign                      | Not Supported                           |
| Sin                       |                                         |
| Sinh                      | Not Supported                           |
| Size                      |                                         |
| Slice                     | batchsize: 1                            |
| Softmax                   | batchsize: 1                            |
| SoftmaxCrossEntropyLoss   | Not Supported                           |
| Softplus                  |                                         |
| Softsign                  | Not Supported                           |
| SpaceToDepth              |                                         |
| Split                     |                                         |
| SplitToSequence           | Not Supported                           |
| Sqrt                      |                                         |
| Squeeze                   |                                         |
| STFT                      | Not Supported                           |
| StringNormalizer          | Not Supported                           |
| Sub                       |                                         |
| Sum                       | Not Supported                           |
| Tan                       | Not Supported                           |
| Tanh                      |                                         |
| TfIdfVectorizer           | Not Supported                           |
| ThresholdedRelu           | Not Supported                           |
| Tile                      | batchsize: 1<br />not support broadcast |
| TopK                      | Not Supported                           |
| Transpose                 |                                         |
| Trilu                     | Not Supported                           |
| Unique                    | Not Supported                           |
| Unsqueeze                 |                                         |
| Where                     |                                         |
| Xor                       | Not Supported                           |

## Pytorch OPs supported by RKNN Toolkit2

The Pytorch version supported by RKNN Toolkit2 is >1.6.0, models generated by other versions may not support.  
The list of Pytorch OPs supported by RKNN Toolkit2 is as follows:

| **Operators**                 | **Remarks**                        |
| ----------------------------- | ---------------------------------- |
| aten::_convolution            | same as onnx Conv                  |
| aten::abs                     | Not supported                      |
| aten::abs_                    | Not supported                      |
| aten::adaptive_avg_pool1d     | Not supported                      |
| aten::adaptive_avg_pool2d     | same as onnx AveragePool           |
| aten::adaptive_max_pool1d     | Not supported                      |
| aten::adaptive_max_pool2d     | same as onnx MaxPool               |
| aten::add                     | same as onnx Add                   |
| aten::add_                    |                                    |
| aten::addmm                   | same as onnx Gemm                  |
| aten::affine_grid_generator   | Not supported                      |
| aten::alpha_dropout           |                                    |
| aten::alpha_dropout_          | Not supported                      |
| aten::arange                  | Not supported                      |
| aten::avg_pool1d              | Not supported                      |
| aten::avg_pool2d              | same as onnx AveragePool           |
| aten::avg_pool3d              | Not supported                      |
| aten::batch_norm              | same as onnx BatchNormalization    |
| aten::bmm                     | same as onnx MatMul                |
| aten::cat                     | same as onnx Concat                |
| aten::celu                    | Not supported                      |
| aten::celu_                   | Not supported                      |
| aten::chunk                   |                                    |
| aten::clamp                   |                                    |
| aten::clamp_                  |                                    |
| aten::clamp_max               | Not supported                      |
| aten::clamp_max_              | Not supported                      |
| aten::clamp_min               |                                    |
| aten::clamp_min_              | Not supported                      |
| aten::clone                   |                                    |
| aten::constant_pad_nd         | same as onnx Pad                   |
| aten::contiguous              |                                    |
| aten::copy                    |                                    |
| aten::cos                     | Not supported                      |
| aten::cos_                    | Not supported                      |
| aten::cumsum                  | Not supported                      |
| aten::detach                  |                                    |
| aten::detach_                 | Not supported                      |
| aten::div                     | same as onnx Div                   |
| aten::div_                    |                                    |
| aten::dropout                 |                                    |
| aten::dropout_                |                                    |
| aten::einsum                  | Not supported                      |
| aten::elu                     | same as onnx Elu                   |
| aten::elu_                    |                                    |
| aten::embedding               | same as onnx Gather                |
| aten::empty                   |                                    |
| aten::eq                      | Not supported                      |
| aten::eq_                     | Not supported                      |
| aten::erf                     | Not supported                      |
| aten::erf_                    | Not supported                      |
| aten::erfc                    | Not supported                      |
| aten::erfc_                   | Not supported                      |
| aten::exp                     |                                    |
| aten::exp_                    |                                    |
| aten::expand                  |                                    |
| aten::expand_as               | Not supported                      |
| aten::expm1                   | Not supported                      |
| aten::expm1_                  | Not supported                      |
| aten::feature_dropout         |                                    |
| aten::feature_dropout_        | Not supported                      |
| aten::flatten                 |                                    |
| aten::flip                    | Not supported                      |
| aten::floor                   | Not supported                      |
| aten::floor_                  | Not supported                      |
| aten::floor_divide            | Not supported                      |
| aten::floor_divide_           | Not supported                      |
| aten::gather                  | Not supported                      |
| aten::ge                      | Not supported                      |
| aten::ge_                     | Not supported                      |
| aten::gelu                    |                                    |
| aten::gelu_                   | Not supported                      |
| aten::grid_sampler            | Not supported                      |
| aten::gru                     |                                    |
| aten::gt                      |                                    |
| aten::gt_                     | Not supported                      |
| aten::hardshrink              | Not supported                      |
| aten::hardshrink_             | Not supported                      |
| aten::hardswish               | same as onnx HardSwish             |
| aten::hardswish_              |                                    |
| aten::hardtanh                |                                    |
| aten::hardtanh_               |                                    |
| aten::index                   | Not supported                      |
| aten::index_put               | Not supported                      |
| aten::index_put_              | Not supported                      |
| aten::instance_norm           | same as onnx InstanceNormalization |
| aten::Int                     |                                    |
| aten::layer_norm              |                                    |
| aten::le                      | Not supported                      |
| aten::le_                     | Not supported                      |
| aten::leaky_relu              | same as onnx LeakyRelu             |
| aten::leaky_relu_             |                                    |
| aten::lerp                    | Not supported                      |
| aten::lerp_                   | Not supported                      |
| aten::log                     | Not supported                      |
| aten::log_                    | Not supported                      |
| aten::log10                   | Not supported                      |
| aten::log10_                  | Not supported                      |
| aten::log1p                   | Not supported                      |
| aten::log1p_                  | Not supported                      |
| aten::log2                    | Not supported                      |
| aten::log2_                   | Not supported                      |
| aten::log_sigmoid             | Not supported                      |
| aten::log_softmax             | Not supported                      |
| aten::linear                  | same as onnx Gemm                  |
| aten::lstm                    | same as onnx LSTM                  |
| aten::lt                      |                                    |
| aten::lt_                     | Not supported                      |
| aten::matmul                  | same as onnx MatMul                |
| aten::max                     |                                    |
| aten::maximum                 |                                    |
| aten::max_                    | Not supported                      |
| aten::max_pool1d              | same as onnx MaxPool               |
| aten::max_pool1d_with_indices |                                    |
| aten::max_pool2d              | same as onnx MaxPool               |
| aten::max_pool2d_with_indices |                                    |
| aten::mean                    | same as onnx ReduceMean            |
| aten::meshgrid                | Not supported                      |
| aten::min                     |                                    |
| aten::minimum                 |                                    |
| aten::min_                    | Not supported                      |
| aten::mish                    |                                    |
| aten::mm                      | same as onnx MatMul                |
| aten::mul                     | same as onnx Mul                   |
| aten::mul_                    |                                    |
| aten::narrow                  | same as onnx Slice                 |
| aten::ne                      |                                    |
| aten::ne_                     | Not supported                      |
| aten::neg                     | Not supported                      |
| aten::neg_                    | Not supported                      |
| aten::new_full                | Not supported                      |
| aten::new_zeros               | Not supported                      |
| aten::nonzero                 | Not supported                      |
| aten::norm                    | Not supported                      |
| aten::ones                    |                                    |
| aten::ones_like               |                                    |
| aten::pad                     | Not supported                      |
| aten::permute                 | same as onnx Transpose             |
| aten::pow                     |                                    |
| aten::pow_                    | Not supported                      |
| aten::prelu                   | same as onnx PRelu                 |
| aten::prelu_                  | Not supported                      |
| aten::prod                    |                                    |
| aten::reciprocal              |                                    |
| aten::reciprocal_             | Not supported                      |
| aten::reflection_pad1d        |                                    |
| aten::reflection_pad2d        |                                    |
| aten::relu                    | same as onnx Relu                  |
| aten::relu6                   | same as onnx Relu                  |
| aten::relu_                   |                                    |
| aten::relu6_                  |                                    |
| aten::repeat                  |                                    |
| aten::reshape                 |                                    |
| aten::reshape_                | Not supported                      |
| torchvision::roi_align        | Not supported                      |
| aten::rsqrt                   | Not supported                      |
| aten::rsqrt_                  | Not supported                      |
| aten::ScalarImplicit          |                                    |
| aten::select                  |                                    |
| aten::selu                    | Not supported                      |
| aten::selu_                   | Not supported                      |
| aten::sigmoid                 | same as onnx Sigmoid               |
| aten::sigmoid_                |                                    |
| aten::silu                    |                                    |
| aten::silu_                   |                                    |
| aten::sin                     | Not supported                      |
| aten::sin_                    | Not supported                      |
| aten::size                    |                                    |
| aten::slice                   | same as onnx Slice                 |
| aten::softmax                 | same as onnx Softmax               |
| aten::softplus                |                                    |
| aten::softshrink              | Not supported                      |
| aten::sort                    | Not supported                      |
| aten::split                   | same as onnx Split                 |
| aten::split_with_sizes        |                                    |
| aten::sqrt                    | Not supported                      |
| aten::sqrt_                   | Not supported                      |
| aten::squeeze                 |                                    |
| aten::squeeze_                | Not supported                      |
| aten::stack                   |                                    |
| aten::sub                     | same as onnx Sub                   |
| aten::sub_                    |                                    |
| aten::sum                     | same as onnx ReduceSum             |
| aten::t                       |                                    |
| aten::t_                      | Not supported                      |
| aten::tanh                    |                                    |
| aten::tanh_                   |                                    |
| aten::threshold               |                                    |
| aten::threshold_              |                                    |
| aten::to                      |                                    |
| aten::topk                    | Not supported                      |
| aten::transpose               |                                    |
| aten::transpose_              |                                    |
| aten::true_divide             | same as onnx Div                   |
| aten::true_divide_            | Not supported                      |
| aten::type_as                 |                                    |
| aten::unfold                  | Not supported                      |
| aten::unsqueeze               |                                    |
| aten::upsample_bilinear2d     |                                    |
| aten::upsample_nearest2d      |                                    |
| aten::view                    |                                    |
| aten::view_                   | Not supported                      |
| aten::view_as                 | Not supported                      |
| aten::view_as_                | Not supported                      |
| aten::where                   |                                    |
| aten::zero_                   | Not supported                      |
| aten::zeros                   |                                    |
| aten::zeros_like              |                                    |




## Caffe OPs supported by RKNN Toolkit2

Caffe protocols RKNN Toolkit2 uses only based on the officially modified protocol of berkeley.
The protocol based on the official revision of berkeley comes from [berkeley caffe](https://github.com/BVLC/caffe/tree/master/src/caffe/proto 'Berkeley Caffe'), commit hash is 21d0608. On this basis RKNN Toolkit2 have added some OPs.  
Based on this protocol, the list of Caffe OPs supported by RKNN Toolkit2 is as follows:

| **Operators**          | **Remarks**                                                                                                   |
| ---------------------- | ------------------------------------------------------------------------------------------------------------- |
| BatchNorm              | same as onnx BatchNormalization                                                                               |
| bn (BatchNorm + Scale) | same as onnx BatchNormalization according to https://github.com/TimoSaemann/caffe-segnet-cudnn5               |
| BNLL                   |                                                                                                               |
| Concat                 | same as onnx Concat                                                                                           |
| Convolution            | same as onnx Conv                                                                                             |
| ConvolutionDepthwise   | kernel height/width: [1, 8]<br />others same as onnx Conv                                                     |
| Crop                   |                                                                                                               |
| Deconvolution          | same as ConvTranspose                                                                                         |
| Dropout                |                                                                                                               |
| Eltwise                |                                                                                                               |
| Flatten                |                                                                                                               |
| HardSigmoid            |                                                                                                               |
| InnerProduct           | same as onnx Gemm                                                                                             |
| LRN                    | same as onnx LRN                                                                                              |
| Lstm                   | same as onnx LSTM according to https://github.com/xmfbit/warpctc-caffe                                        |
| Normalize              |                                                                                                               |
| Permute                | same as onnx Transpose                                                                                        |
| Power                  |                                                                                                               |
| Pooling                | same as onnx pooling                                                                                          |
| PRelu                  | same as onnx PRelu                                                                                            |
| Proposal               | batch: 1                                                                                                      |
| Reduction              | output dims <= 4                                                                                              |
| Relu                   | same as onnx Relu                                                                                             |
| Relu6                  | same as onnx Clip                                                                                             |
| Reorg                  |                                                                                                               |
| Reshape                | same as onnx Reshape                                                                                          |
| Resize                 | bilinear; nearest                                                                                             |
| Reverse                |                                                                                                               |
| ROIPooling             | same as MaxRoiPool according to https://github.com/twmht/caffe-pva-faster-rcnn                                |
| Scale                  | same as onnx Mul                                                                                              |
| Sigmoid                | same as onnx Sigmoid                                                                                          |
| Slice                  | same as onnx Split                                                                                            |
| Softmax                | same as onnx Softmax                                                                                          |
| Split                  | same as onnx Slice                                                                                            |
| TanH                   | same as onnx TanH                                                                                             |
| Tile                   | same as onnx Tile                                                                                             |
| Transpose              | same as onnx Transpose                                                                                        |
| Upsample               | according to https://github.com/SeanQ88/caffe_upsample and https://github.com/TimoSaemann/caffe-segnet-cudnn5 |


## TensorFlow OPs supported by RKNN Toolkit2

The pb files (contain OPs belows) generated by TensorFlow version 1.12 - 1.15 for 1.x and 2.3 - 2.5 for 2.x are supported by RKNN Toolkit2. For more information on TensorFlow version compatibility, please refer to [tensorflow official instructions on OP version](https://www.tensorflow.org/guide/versions 'Tensorflow official instructions on OP version') . 
The list of TensorFlow OPs supported by RKNN Toolkit2 is as follows:

| **Operators**         | **Remarks**                                               |
| --------------------- | --------------------------------------------------------- |
| Add                   | same as onnx Add                                          |
| AvgPool               | same as onnx AveragePool                                  |
| Concat                | same as onnx Concat                                       |
| Conv2D                | same as onnx Conv                                         |
| DepthToSpace          |                                                           |
| DepthwiseConv2d       | kernel height/width: [1, 8]<br />others same as onnx Conv |
| Div                   | same as onnx Div                                          |
| Dropout               |                                                           |
| Flatten               |                                                           |
| LeakyRelu             | same as onnx LeakyRelu                                    |
| Less                  | same as onnx Less                                         |
| LRN                   |                                                           |
| MatMul                |                                                           |
| MaxPool               | same as onnx MaxPool                                      |
| Mean                  | output dims <= 4                                          |
| Pad                   | same as onnx Pad                                          |
| Relu                  | same as onnx Relu                                         |
| Reshape               |                                                           |
| ResizeBilinear        |                                                           |
| ResizeNearestNeighbor |                                                           |
| Sigmoid               |                                                           |
| Slice                 |                                                           |
| Softmax               |                                                           |
| Softplus              | same as onnx Softplus                                     |
| SpaceToDepth          |                                                           |
| Split                 |                                                           |
| Squeeze               |                                                           |
| StridedSlice          |                                                           |
| Tanh                  | same as onnx TanH                                         |
| Transpose             |                                                           |

## Darknet OPs supported by RKNN Toolkit2
The list of Darknet OPs supported by RKNN Toolkit2 is as follows:

| **Operators**           | **Remarks**                                                                                                                                                                   |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| add                     | same as onnx Add                                                                                                                                                              |
| batchnormalize          | same as onnx BatchNormalization                                                                                                                                               |
| concat                  | same as onnx Concat                                                                                                                                                           |
| convolutional           | same as onnx Conv                                                                                                                                                             |
| depthwise_convolutional | kernel height/width: [1, 8]<br />others same as onnx Conv                                                                                                                     |
| fullconnect             |                                                                                                                                                                               |
| leakyrelu               | same as onnx LeakyRelu                                                                                                                                                        |
| mish                    |                                                                                                                                                                               |
| pooling                 | **AveragePool**: same as onnx AveragePool   <br /> **GlobalAveragePool**: same as onnx GlobalAveragePool <br /> **MaxPool/GlobalMaxPool**: same as onnx MaxPool/GlobalMaxPool |
| route                   |                                                                                                                                                                               |
| shortcut                |                                                                                                                                                                               |
| softmax                 |                                                                                                                                                                               |
| upsampling              |                                                                                                                                                                               |
===== LICENSE =====
RKNN SDK License

This License Agreement for RKNN Software Development Kit Package (this “Agreement”) is a legally binding agreement between Rockchip Electronics Co., Ltd. (“Rockchip”) and the person or legal entity You represent (“You”).

DO NOT DOWNLOAD, INSTALL OR USE THE RKNN SOFTWARE DEVELOPMENT KIT PACKAGE (THE “SOFTWARE) UNTIL YOU HAVE CAREFULLY READ AND ACCEPTED THIS AGREEMENT. BY DOWNLOADLING, INSTALLING OR USING THE SOFTWARE, YOU ACKNOWLEDGE THAT YOU HAVE READ AND AGREED TO BE BOUND BY THE TERMS AND CONDITIONS OF THIS AGREEMENT. IF YOU DO NOT AGREE TO ALL OF THE TERMS AND CONDITIONS OF THIS AGREEMENT, CANCEL THE DOWNLOADLING, INSTALLING OR USING OF THE SOFTWARE.

1. License Grant
1.1 Subject to the terms and conditions of this Agreement, Rockchip hereby grants to You a limited, non-exclusive, royalty-free copyright license to use, reproduce, modify, and create derivative works of the Software and redistribute its modifications or derivative works that are made by You solely for the design, development and testing of applications that are compatible with Products (as defined below) of Rockchip or its affiliates.
1.2 Subject to the terms and conditions of this Agreement, You may reproduce and use, on an internal basis only, a reasonable number of copies of the documentation made available by Rockchip in connection with Software (“Documentation”’), solely in support of the license to the Software.
1.3 Except as expressly provided in this Agreement, no other license is granted explicitly, by implication, or otherwise under any intellectual property rights, including patent or copyrights.

2. License Restrictions
2.1 Except as expressively granted in this Agreement or expressively authorized by Rockchip in writing, You may NOT:
(a)decompile, reverse-engineer, dissemble, or attempt to derive any source code from the Software;
(b) remove or obscure any copyright, patent, or trademark statement or notice associated with the Software;
(c) use Third Party Software (as defined below), Open Source Software (as defined below) in any manner other than as permitted in this Agreement.
2.2 The Software may contain Third Party Software that are proprietary to third parties or subjected to separate licenses and restrictions from third parties for any types of usages. The license terms associated with those software apply to Your use of them, and in some instances such software cannot be used or further distributed without a license from the respective owner of such third party software. You shall be solely responsible to obtain, if necessary, a separate and independent license from such owner with respect to any such use. The delivery of the Software does not convey a license, nor imply any rights, to use Third Party Software. 
2.3 The Software may contain Open Source Software that is licensed pursuant to the applicable Open Source Software license agreement(s) (such as BSD, GPL, MIT etc.), which are either identified in the Open Source Software comments in the applicable source code file(s) and/or file header(s). With respect to the Open Source Software, nothing in this Agreement limits any rights under, or grants rights that supersede, the terms of any applicable Open Source Software license agreement(s). You must comply with Open Source Software licenses that may prevail over the terms of this Agreement. In no event may You cause any part of the Software that is not Open Source Software to become Open Source Software. 

3. Updates, Upgrades and Support Services
3.1 Rockchip may, in its sole discretion, release any updates, upgrades, or new versions of the Software and/or Documentation at any time on the website. If You decide to download, intall or use any updates, upgrades, or new versions of the Software and/or Documentation, the terms and conditions of this Agreement will govern such updates, upgrades, or new versions.
3.2 Rockchip is under no obligation to provide any form of technical support for the Software and/or Documentation.

4. Ownership 
Rockchip and/or its licensor(s) retain all rights, titles, and interests in and to the Software and/or Documentation and its updates, upgrades. 

5. No Warranties
YOU EXPRESSLY ACKNOWLEDGE AND AGREE THAT THE USE OF THE SOFTWARE AND DOCUMENTATION IS AT YOUR SOLE RISK. THE SOFTWARE AND DOCUMENTATION IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL ROCKCHIP BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE AND DOCUMENTATION.

6. Indemnifications
You should indemnify, hold harmless, and defend Rockchip from and against any claims, damages, losses, liabilities, obligations, and costs (including attorney fees) associated with an allegation arising out of Your failure to adhere to the terms and conditions of this Agreement.

7. Feedback
If You provide Rockchip with any feedback, suggestions, comments, ideas, reviews, bug reports, or any similar or related information (“Feedback”), You agree that: (a) Rockhip will be able to free use and share such Feedback without Your consent; (b) Rockchip will have no obligation to keep confidentiality to such Feedback. If You do not agree with these terms regarding Feedback, Your sole option is to not submit such specific Feedback to Rockchip.

8. Export Controls
You acknowledge that all hardware, software, source code and technology (collectively, "Products") obtained from Rockchip or its affiliates may be subject to the applicable export control laws and regulations of the U.N., P.R.C., U.S., E.U., and/or other countries, as amended (collectively, the “Export Control and Economic Sanctions Laws and Regulations”). You shall comply with any applicable Export Control and Economic Sanctions Laws and Regulations, when using, exporting, re-exporting, selling, or otherwise disposing of the Products and fulfilling the rights and obligations under this Agreement. You assure that You will not directly or indirectly export, re-export, transfer or release (collectively, "export") any Products to any destination, person, entity or end use prohibited or restricted under Export Control and Economic Sanctions Laws and Regulations in violation of these laws and regulations. You further acknowledge that You are not a person or entity that is listed on any applicable sanctions lists. This section shall survive the termination of this Agreement.

9. Term and Termination
9.1 This Agreement will come into effect on the date You accept this Agreement and shall continue until terminated. This Agreement terminates immediately and automatically, with or without notice, if You fail to comply with any provision hereof. Additionally, Rockchip may at any time terminate this Agreement, either with or without cause, upon notice to You.
9.2 Upon termination of this Agreement, You must delete or destroy all copies of the Software and Documentation in Your possession, and the license and other rights granted to You in this Agreement shall terminate.

10. Governing Law and Jurisdiction
This Agreement will be governed by and construed in accordance with the laws of the People’s Republic of China (“PRC”), without regard to principles of conflict of laws. You agree that any dispute arising out of or in connection with this Agreement will be decided to a court of competent jurisdiction which located in Fuzhou City, PRC.
