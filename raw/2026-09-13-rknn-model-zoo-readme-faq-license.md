<!-- airockchip/rknn_model_zoo @ main, captured 2026-09-13. Bundle: README.md, FAQ.md, examples/yolov8/README.md, LICENSE -->

===== README.md =====
[简体中文](README_CN.md) | [English](README.md)



# RKNN Model Zoo

## Description

`RKNN Model Zoo` is developed based on the RKNPU SDK toolchain and provides deployment examples for current mainstream algorithms. Include the process of `exporting the RKNN model` and using `Python API` and `CAPI` to infer the RKNN model.

- Support `RK3562`, `RK3566`, `RK3568`, `RK3576`, `RK3588` , `RV1126B`  platforms. 
- Limited support `RV1103`, `RV1106` 
- Support  `RV1109`, `RV1126`, `RK1808` platforms.



## Dependency library installation

`RKNN Model Zoo` relies on `RKNN-Toolkit2` for model conversion. The Android compilation tool chain is required when compiling the Android demo, and the Linux compilation tool chain is required when compiling the Linux demo. For the installation of these dependencies, please refer to the `Quick Start` documentation at https://github.com/airockchip/rknn-toolkit2/tree/master/doc.

- Please note that the Android compilation tool chain recommends using `version r18 or r19`. Using other versions may encounter the problem of Cdemo compilation failure.
- Please note that the Linux compilation tool chain recommends using `gcc-linaro-6.3.1(aarch64)/gcc-arm-8.3(armhf)/armhf-uclibcgnueabihf(armhf for RV1106/RV1103 series)`. Using other versions may encounter the problem of Cdemo compilation failure. For detailed compilation guide, please refer to [Compilation_Environment_Setup_Guide.md](./docs/Compilation_Environment_Setup_Guide.md)


## Model support

In addition to exporting the model from the corresponding respository, the models file are available on https://console.zbox.filez.com/l/8ufwtG (key: rknn). 

| Category | Name | Dtype | Model Download Link | Support platform |
| --- | --- | --- | --- | --- |
| Classification | [mobilenet](https://github.com/onnx/models/tree/8e893eb39b131f6d3970be6ebd525327d3df34ea/vision/classification/mobilenet/model/mobilenetv2-12.onnx) | FP16/INT8 | [mobilenetv2-12.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/mobilenet/mobilenetv2-12.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RV1103\|RV1106<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Classification | [resnet](https://github.com/onnx/models/tree/8e893eb39b131f6d3970be6ebd525327d3df34ea/vision/classification/resnet/model/resnet50-v2-7.onnx) | FP16/INT8 | [resnet50-v2-7.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/resnet/resnet50-v2-7.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Object Detection | [yolov5](https://github.com/airockchip/yolov5) | FP16/INT8 | [./yolov5s_relu.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov5/yolov5s_relu.onnx)<br/>[./yolov5n.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov5/yolov5n.onnx)<br/>[./yolov5s.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov5/yolov5s.onnx)<br/>[./yolov5m.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov5/yolov5m.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RV1103\|RV1106<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Object Detection | [yolov6](https://github.com/airockchip/yolov6) | FP16/INT8 | [./yolov6n.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov6/yolov6n.onnx)<br/>[./yolov6s.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov6/yolov6s.onnx)<br/>[./yolov6m.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov6/yolov6m.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Object Detection | [yolov7](https://github.com/airockchip/yolov7) | FP16/INT8 | [./yolov7-tiny.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov7/yolov7-tiny.onnx)<br/>[./yolov7.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov7/yolov7.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Object Detection | [yolov8](https://github.com/airockchip/ultralytics_yolov8) | FP16/INT8 | [./yolov8n.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov8/yolov8n.onnx)<br/>[./yolov8s.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov8/yolov8s.onnx)<br/>[./yolov8m.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov8/yolov8m.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Object Detection | [yolov8_obb](https://github.com/airockchip/ultralytics_yolov8) | INT8 | [./yolov8n-obb.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov8_obb/yolov8n-obb.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Object Detection | [yolov10](https://github.com/THU-MIG/yolov10) | FP16/INT8 | [./yolov10n.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov10/yolov10n.onnx)<br/>[./yolov10s.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov10/yolov10s.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RV1103\|RV1106<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Object Detection | [yolo11](https://github.com/airockchip/ultralytics_yolo11) | FP16/INT8 | [./yolo11n.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolo11/yolo11n.onnx)<br/>[./yolo11s.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolo11/yolo11s.onnx)<br/>[./yolo11m.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolo11/yolo11m.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RV1103\|RV1106<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Object Detection | [yolox](https://github.com/airockchip/YOLOX) | FP16/INT8 | [./yolox_s.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolox/yolox_s.onnx)<br/>[./yolox_m.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolox/yolox_m.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Object Detection | [ppyoloe](https://github.com/PaddlePaddle/PaddleDetection/blob/release/2.6/configs/ppyoloe) | FP16/INT8 | [./ppyoloe_s.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/ppyoloe/ppyoloe_s.onnx)<br/>[./ppyoloe_m.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/ppyoloe/ppyoloe_m.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Object Detection | [yolo_world](https://github.com/AILab-CVC/YOLO-World) | FP16/INT8 | [./yolo_world_v2s.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolo_world/yolo_world_v2s.onnx)<br/>[./clip_text.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolo_world/clip_text.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/> |
| Body Pose | [yolov8_pose](https://github.com/airockchip/ultralytics_yolov8) | INT8 | [./yolov8n-pose.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov8_pose/yolov8n-pose.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/> |
| Image Segmentation | deeplabv3 | FP16/INT8 | [./deeplab-v3-plus-mobilenet-v2.pb](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/deeplabv3/deeplab-v3-plus-mobilenet-v2.pb) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Image Segmentation | [yolov5_seg](https://github.com/airockchip/yolov5) | FP16/INT8 | [./yolov5n-seg.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov5_seg/yolov5n-seg.onnx)<br/>[./yolov5s-seg.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov5_seg/yolov5s-seg.onnx)<br/>[./yolov5m-seg.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov5_seg/yolov5m-seg.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Image Segmentation | [yolov8_seg](https://github.com/airockchip/ultralytics_yolov8) | FP16/INT8 | [./yolov8n-seg.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov8_seg/yolov8n-seg.onnx)<br/>[./yolov8s-seg.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov8_seg/yolov8s-seg.onnx)<br/>[./yolov8m-seg.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov8_seg/yolov8m-seg.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Image Segmentation | [ppseg](https://github.com/PaddlePaddle/PaddleSeg/tree/release/2.8) | FP16/INT8 | [pp_liteseg_cityscapes.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/ppseg/pp_liteseg_cityscapes.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Image Segmentation | [mobilesam](https://github.com/ChaoningZhang/MobileSAM) | FP16 | [mobilesam_encoder_tiny.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/mobilesam/mobilesam_encoder_tiny.onnx)<br />[mobilesam_decoder.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/mobilesam/mobilesam_decoder.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B |
| Face Key Points | [RetinaFace](https://github.com/biubug6/Pytorch_Retinaface) | INT8 | [RetinaFace_mobile320.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/RetinaFace/RetinaFace_mobile320.onnx)<br/>[RetinaFace_resnet50_320.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/RetinaFace/RetinaFace_resnet50_320.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Car Plate Recognition | [LPRNet](https://github.com/sirius-ai/LPRNet_Pytorch/) | FP16/INT8 | [./lprnet.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/LPRNet/lprnet.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RV1103\|RV1106<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Text Detection | [PPOCR-Det](https://github.com/PaddlePaddle/PaddleOCR/tree/release/2.7) | FP16/INT8 | [../ppocrv4_det.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/PPOCR/ppocrv4_det.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Text Recognition | [PPOCR-Rec](https://github.com/PaddlePaddle/PaddleOCR/tree/release/2.7) | FP16 | [../ppocrv4_rec.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/PPOCR/ppocrv4_rec.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Neural Machine Translation | [lite_transformer](https://github.com/airockchip/lite-transformer) | FP16 | [lite-transformer-encoder-16.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/lite_transformer/lite-transformer-encoder-16.onnx)<br/>[lite-transformer-decoder-16.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/lite_transformer/lite-transformer-decoder-16.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/>RK1808\|RK3399PRO<br/>RV1109\|RV1126 |
| Image-Text Matching | [clip](https://huggingface.co/openai/clip-vit-base-patch32) | FP16 | [./clip_images.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/clip/clip_images.onnx)<br/>[./clip_text.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/clip/clip_text.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/> |
| Speech Recognition | [wav2vec2](https://github.com/facebookresearch/fairseq/tree/main/examples/wav2vec#wav2vec-20) | FP16 | [wav2vec2_base_960h_20s.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/wav2vec2/wav2vec2_base_960h_20s.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B |
| Speech Recognition | [whisper](https://github.com/openai/whisper) | FP16 | [whisper_encoder_base_20s.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/whisper/whisper_encoder_base_20s.onnx)<br/>[whisper_decoder_base_20s.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/whisper/whisper_decoder_base_20s.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/> |
| Speech Recognition | [zipformer](https://huggingface.co/csukuangfj/k2fsa-zipformer-bilingual-zh-en-t) | FP16 | [encoder-epoch-99-avg-1.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/zipformer/encoder-epoch-99-avg-1.onnx)<br/>[decoder-epoch-99-avg-1.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/zipformer/decoder-epoch-99-avg-1.onnx)<br/>[joiner-epoch-99-avg-1.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/zipformer/joiner-epoch-99-avg-1.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/> |
| Speech Classification | [yamnet](https://www.tensorflow.org/hub/tutorials/yamnet) | FP16 | [yamnet_3s.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yamnet/yamnet_3s.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B |
| Text to Speech | [mms_tts](https://huggingface.co/facebook/mms-tts-eng) | FP16 | [mms_tts_eng_encoder_200.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/mms_tts/mms_tts_eng_encoder_200.onnx)<br/>[mms_tts_eng_decoder_200.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/mms_tts/mms_tts_eng_decoder_200.onnx) | RK3562\|RK3566\|RK3568\|RK3576\|RK3588\|RV1126B<br/> |




## Model performance benchmark(FPS)

| demo             | model_name                          | inputs_shape&nbsp;&nbsp;&nbsp;&nbsp; | dtype | RK3566<br />RK3568 | RK3562         | RK3588<br />@single_core | RK3576<br />@single_core | RV1109     | RV1126     | RK1808     |
| ---------------- | ----------------------------------- | ------------------------------------ | ----- | ------------------ | -------------- | ------------------------ | ------------------------ | ---------- | ---------- | ---------- |
| mobilenet        | mobilenetv2-12                      | [1, 3, 224, 224]        | INT8     | 180.7                 | 281.3     | 450.7          | 467.0     | 212.9      | 322.3      | 170.3      |
| resnet           | resnet50-v2-7                       | [1, 3, 224, 224]        | INT8     | 37.9                  | 54.9      | 110.1          | 99.0      | 24.4       | 36.2       | 37.1       |
| yolov5           | yolov5s_relu                        | [1, 3, 640, 640]        | INT8     | 25.5                  | 33.2      | 66.1           | 65.0      | 20.2       | 29.2       | 37.2       |
|                  | yolov5n                             | [1, 3, 640, 640]        | INT8     | 39.7                  | 47.4      | 82.5           | 112.7     | 36.3       | 53.2       | 61.2       |
|                  | yolov5s                             | [1, 3, 640, 640]        | INT8     | 19.3                  | 23.6      | 48.4           | 57.5      | 13.6       | 20.0       | 28.2       |
|                  | yolov5m                             | [1, 3, 640, 640]        | INT8     | 8.6                   | 10.8      | 20.9           | 23.7      | 5.8        | 8.5        | 13.3       |
| yolov6           | yolov6n                             | [1, 3, 640, 640]        | INT8     | 48.8                  | 56.4      | 106.4          | 109.1     | 37.8       | 56.8       | 66.8       |
|                  | yolov6s                             | [1, 3, 640, 640]        | INT8     | 15.2                  | 17.3      | 36.4           | 35.0      | 10.8       | 16.3       | 24.1       |
|                  | yolov6m                             | [1, 3, 640, 640]        | INT8     | 7.2                   | 8.6       | 17.8           | 17.4      | 5.6        | 8.3        | 11.5       |
| yolov7           | yolov7-tiny                         | [1, 3, 640, 640]        | INT8     | 27.9                  | 36.5      | 72.7           | 74.8      | 15.4       | 22.4       | 37.2       |
|                  | yolov7                              | [1, 3, 640, 640]        | INT8     | 4.6                   | 5.9       | 11.4           | 13.0      | 3.3        | 4.8        | 7.4        |
| yolov8           | yolov8n                             | [1, 3, 640, 640]        | INT8     | 34.0                  | 40.9      | 73.5           | 90.2      | 24.0       | 35.4       | 42.3       |
|                  | yolov8s                             | [1, 3, 640, 640]        | INT8     | 15.1                  | 18.4      | 38.0           | 40.8      | 8.9        | 13.1       | 19.1       |
|                  | yolov8m                             | [1, 3, 640, 640]        | INT8     | 6.5                   | 8.2       | 16.2           | 16.7      | 3.9        | 5.8        | 9.1        |
| yolov8_obb       | yolov8n-obb                         | [1, 3, 640, 640]        | INT8     | 33.9                  | 41.3      | 74.0           | 90.2      | 25.1       | 37.3       | 42.8       |
| yolov10          | yolov10n                            | [1, 3, 640, 640]        | INT8     | 20.7                  | 34.1      | 61.2           | 80.2      | /          | /          | /          |
|                  | yolov10s                            | [1, 3, 640, 640]        | INT8     | 10.3                  | 16.9      | 33.8           | 39.9      | /          | /          | /          |
| yolo11           | yolo11n                             | [1, 3, 640, 640]        | INT8     | 20.6                  | 34.0      | 60.0           | 77.9      | 11.7       | 17.0       | 17.6       |
|                  | yolo11s                             | [1, 3, 640, 640]        | INT8     | 10.2                  | 16.7      | 33.0           | 38.2      | 5.0        | 7.3        | 8.4        |
|                  | yolo11m                             | [1, 3, 640, 640]        | INT8     | 4.6                   | 6.5       | 12.7           | 14.6      | 2.8        | 4.0        | 5.1        |
| yolox            | yolox_s                             | [1, 3, 640, 640]        | INT8     | 15.2                  | 18.3      | 37.1           | 41.5      | 10.6       | 15.7       | 23.0       |
|                  | yolox_m                             | [1, 3, 640, 640]        | INT8     | 6.6                   | 8.2       | 16.0           | 17.6      | 4.6        | 6.8        | 10.7       |
| ppyoloe          | ppyoloe_s                           | [1, 3, 640, 640]        | INT8     | 17.1                   | 20.0      | 32.5           | 41.3      | 11.2       | 16.4       | 21.1       |
|                  | ppyoloe_m                           | [1, 3, 640, 640]        | INT8     | 7.8                   | 9.2       | 15.8           | 17.8      | 5.2        | 7.7        | 9.4        |
| yolo_world       | yolo_world_v2s                      | [1, 3, 640, 640]        | INT8     | 7.4                   | 9.6       | 22.1           | 22.3      | /          | /          | /          |
|                  | clip_text                           | [1, 20]                 | FP16     | 29.8                  | 67.4      | 95.8           | 63.5      | /          | /          | /          |
| yolov8_pose      | yolov8n-pose                        | [1, 3, 640, 640]        | INT8     | 22.6                  | 31.0      | 55.9           | 66.8      | /          | /          | /          |
| deeplabv3        | deeplab-v3-plus-mobilenet-v2        | [1, 513, 513, 1]        | INT8     | 10.9                  | 21.4      | 34.0           | 39.4      | 10.1       | 13.0       | 4.4        |
| yolov5_seg       | yolov5n-seg                         | [1, 3, 640, 640]        | INT8     | 32.2                  | 38.5      | 69.3           | 88.3      | 28.6       | 42.2       | 49.6       |
|                  | yolov5s-seg                         | [1, 3, 640, 640]        | INT8     | 15.0                  | 18.1      | 36.8           | 41.6      | 9.6        | 14.0       | 22.5       |
|                  | yolov5m-seg                         | [1, 3, 640, 640]        | INT8     | 6.8                   | 8.4       | 16.4           | 18.0      | 4.7        | 6.8        | 10.8       |
| yolov8_seg       | yolov8n-seg                         | [1, 3, 640, 640]        | INT8     | 27.8                  | 33.0      | 60.8           | 71.1      | 18.6       | 27.6       | 32.9       |
|                  | yolov8s-seg                         | [1, 3, 640, 640]        | INT8     | 11.7                  | 14.1      | 28.9           | 30.8      | 6.6        | 9.8        | 14.6       |
|                  | yolov8m-seg                         | [1, 3, 640, 640]        | INT8     | 5.2                   | 6.4       | 12.6           | 12.7      | 3.1        | 4.6        | 6.9        |
| ppseg            | ppseg_lite_1024x512                 | [1, 3, 512, 512]        | INT8     | 5.9                   | 13.9      | 35.7           | 33.6      | 18.4       | 27.1       | 20.9       |
| mobilesam        | mobilesam_encoder_tiny              | [1, 3, 448, 448]        | FP16     | 1.0                   | 6.6       | 10.0           | 11.9      | /          | /          | /          |
|                  | mobilesam_decoder                   | [1, 1, 112, 112]        | FP16     | 24.3                  | 69.6      | 116.4          | 108.6     | /          | /          | /          |
| RetinaFace       | RetinaFace_mobile320                | [1, 3, 320, 320]        | INT8     | 156.4                 | 300.8     | 227.2          | 470.5     | 144.8      | 212.5      | 198.5      |
|                  | RetinaFace_resnet50_320             | [1, 3, 320, 320]        | INT8     | 18.7                  | 26.9      | 49.2           | 56.6      | 14.6       | 20.8       | 24.6       |
| LPRNet           | lprnet                              | [1, 3, 24, 94]          | FP16     | 143.2                 | 420.6     | 586.4          | 647.8     | 30.6(INT8) | 47.6(INT8) | 30.1(INT8) |
| PPOCR-Det        | ppocrv4_det                         | [1, 3, 480, 480]        | INT8     | 22.1                  | 28.0      | 50.7           | 64.3      | 11.0       | 16.1       | 14.2       |
| PPOCR-Rec        | ppocrv4_rec                         | [1, 3, 48, 320]         | FP16     | 19.5                  | 54.3      | 73.9           | 96.8      | 1.0        | 1.6        | 6.7        |
| lite_transformer | lite-transformer-encoder-16         | embedding-256, token-16 | FP16     | 337.5                 | 725.8     | 867.6          | 784.1     | 22.7       | 35.4       | 98.3       |
|                  | lite-transformer-decoder-16         | embedding-256, token-16 | FP16     | 142.5                 | 252.0     | 343.8          | 272.3     | 48.0       | 65.8       | 109.9      |
| clip             | clip_images                         | [1, 3, 224, 224]        | FP16     | 2.3                   | 3.4       | 6.5            | 6.7       | /          | /          | /          |
|                  | clip_text                           | [1, 20]                 | FP16     | 29.7                  | 66.6      | 96.0           | 63.7      | /          | /          | /          |
| wav2vec2         | wav2vec2_base_960h_20s              | 20s audio               | FP16     | RTF <br>0.817   | RTF <br>0.323   | RTF <br>0.133  | RTF <br>0.073  | /        | /        | /         |
| whisper          | whisper_base_20s                    | 20s audio               | FP16     | RTF <br>1.178   | RTF <br>0.420   | RTF <br>0.215  | RTF <br>0.218  | /        | /        | /         |
| zipformer        | zipformer-bilingual-zh-en-t         | streaming audio         | FP16     | RTF <br>0.196   | RTF <br>0.116   | RTF <br>0.065  | RTF <br>0.082  | /        | /        | /         |
| yamnet           | yamnet_3s                           | 3s audio                | FP16     | RTF <br>0.013   | RTF <br>0.008   | RTF <br>0.004  | RTF <br>0.005  | /        | /        | /         |
| mms_tts          | mms_tts_eng_200                     | token-200               | FP16     | RTF <br>0.311   | RTF <br>0.138   | RTF <br>0.069  | RTF <br>0.069  | /        | /        | /         |

- This performance data are collected based on the maximum NPU frequency of each platform.
- This performance data calculate the time-consuming of model inference. Does not include the time-consuming of pre-processing and post-processing if not specified.
- `/` means currently not support.



## Compile Demo

For Linux develop board:

```sh
./build-linux.sh -t <target> -a <arch> -d <build_demo_name> [-b <build_type>] [-m]
    -t : target (rk356x/rk3576/rk3588/rv1106/rv1126b/rv1126/rk1808)
    -a : arch (aarch64/armhf)
    -d : demo name
    -b : build_type(Debug/Release)
    -m : enable address sanitizer, build_type need set to Debug
Note: 'rk356x' represents rk3562/rk3566/rk3568, 'rv1106' represents rv1103/rv1106, 'rv1126' represents rv1109/rv1126，'rv1126b' is different from 'rv1126'.

# Here is an example for compiling yolov5 demo for 64-bit Linux RK3566.
./build-linux.sh -t rk356x -a aarch64 -d yolov5
```

For Android development board:

```sh
# For Android develop boards, it's require to set path for Android NDK compilation tool path according to the user environment
export ANDROID_NDK_PATH=~/opts/ndk/android-ndk-r18b
./build-android.sh -t <target> -a <arch> -d <build_demo_name> [-b <build_type>] [-m]
    -t : target (rk356x/rk3576/rk3588)
    -a : arch (arm64-v8a/armeabi-v7a)
    -d : demo name
    -b : build_type (Debug/Release)
    -m : enable address sanitizer, build_type need set to Debug

# Here is an example for compiling yolov5 demo for 64-bit Android RK3566.
./build-android.sh -t rk356x -a arm64-v8a -d yolov5
```



## Release Notes

| Version | Description                                                  |
| ------- | ------------------------------------------------------------ |
| 2.3.2   | Add support for `RV1126B`. |
| 2.3.0   | New demos released, including yolo11, zipformer, mms_tts, etc. |
| 2.2.0   | New demo wav2vec, mobilesam release. Update demo guide about exporting model. |
| 2.1.0   | New demo release, including yolov8_pose, yolov8_obb, yolov10, yolo_world, clip, whisper, yamnet<br>`RK1808`, `RV1109`, `RV1126` platform support of these demo will be added in next version. |
| 2.0.0   | Add support for `RK3576`.<br />Add support for `RK1808`,  `RV1109`, `RV1126`. |
| 1.6.0   | New demo release, including object detection, image segmentation, OCR, car plate detection&recognition etc.<br />Full support for `RK3566`, `RK3568`, `RK3588`, `RK3562` platforms.<br />Limited support for `RV1103`, `RV1106` platforms. |
| 1.5.0   | Yolo detection demo release.                                 |



## Environment dependencies

All demos in `RKNN Model Zoo` are verified based on the latest RKNPU SDK. If using a lower version for verification, the inference performance and inference results may be wrong.

| Version | RKNPU2 SDK | RKNPU1 SDK |
| ------- | ---------- | ---------- |
| 2.3.2   | >=2.3.2    | >=1.7.5    |
| 2.3.0   | >=2.3.0    | >=1.7.5    |
| 2.2.0   | >=2.2.0    | >=1.7.5    |
| 2.1.0   | >=2.1.0    | >=1.7.5    |
| 2.0.0   | >=2.0.0    | >=1.7.5    |
| 1.6.0   | >=1.6.0    | -          |
| 1.5.0   | >=1.5.0    | >=1.7.3    |



## RKNPU Resource

- RKNPU2 SDK: https://github.com/airockchip/rknn-toolkit2
- RKNPU1 SDK: https://github.com/airockchip/rknn-toolkit



## License

[Apache License 2.0](./LICENSE)


===== FAQ.md =====
- [1. Common Issue](#1-common-issue)
  - [1.1 How to upgrade RKNPU’s related dependent libraries](#11-how-to-upgrade-rknpus-related-dependent-libraries)
  - [1.2 Result differs via platform](#12-result-differs-via-platform)
  - [1.3 The demo result not correct](#13-the-demo-result-not-correct)
  - [1.4 The demo ran correctly, but when I replaced it with my own model, it ran wrong.](#14-the-demo-ran-correctly-but-when-i-replaced-it-with-my-own-model-it-ran-wrong)
  - [1.5 Model inference performance does not meet reference performance](#15-model-inference-performance-does-not-meet-reference-performance)
  - [1.6 How to solve the accuracy problem after model quantization](#16-how-to-solve-the-accuracy-problem-after-model-quantization)
  - [1.7 Is there a board-side python demo](#17-is-there-a-board-side-python-demo)
  - [1.8 Why are there no demos for other models? Is it because they are not supported](#18-why-are-there-no-demos-for-other-models-is-it-because-they-are-not-supported)
  - [1.9 Is there a LLM model demo?](#19-is-there-a-llm-model-demo)
  - [1.10 Why RV1103 and RV1106 can run fewer demos](#110-why-rv1103-and-rv1106-can-run-fewer-demos)
  - [1.11 Segmentation fault error will occur when opencv and jpeg libraries are used together](#111-segmentation-fault-error-will-occur-when-opencv-and-jpeg-libraries-are-used-together)
  - [1.12 Failed during compilation or prompted that some dependent libraries could not be found during runtime](#112-failed-during-compilation-or-prompted-that-some-dependent-libraries-could-not-be-found-during-runtime)
- [2. RGA](#2-rga)
- [3. YOLO](#3-yolo)
  - [3.1 Class confidence exceeds 1](#31-class-confidence-exceeds-1)
  - [3.2 So many boxes in the inference results and fill the entire picture](#32-so-many-boxes-in-the-inference-results-and-fill-the-entire-picture)
  - [3.3 The box's position and confidence are correct, but size not match well(yolov5, yolov7)](#33-the-boxs-position-and-confidence-are-correct-but-size-not-match-wellyolov5-yolov7)
  - [3.4 MAP accuracy is lower than official results](#34-map-accuracy-is-lower-than-official-results)
  - [3.5 Can NPU run YOLO without modifying the model structure?](#35-can-npu-run-yolo-without-modifying-the-model-structure)



## 1. Common Issue

### 1.1 How to upgrade RKNPU’s related dependent libraries

|              | RKNPU1                                                       | RKNPU2                                                       |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Platform     | RV1109<br />RV1126<br />RK1808<br />RK3399pro                | RV1103<br />RV1106<br />RV1126B<br />RK3562<br />RK3566<br />RK3568<br />RK3588<br />RK3576 |
| Driver       | Upgrade by replace .ko file                                  | Upgrade by burning new firmware                              |
| Runtime      | Refer to the [documentation](https://github.com/airockchip/rknpu/blob/master/README.md) and replace **librknn_runtime.so** and its related dependency files to upgrade.<br /><br />(PC-to-board debugging function requires updating the **rknn_server** file described in the document) | Refer to [Document](https://github.com/airockchip/rknn-toolkit2/blob/master/doc/rknn_server_proxy.md), replace the **librknnrt.so** file to upgrade<br />(RV1103/RV1106 use the cropped version runtime, the corresponding file name is **librknnmrt.so**)<br /><br />(PC-to-board debugging function requires updating the **rknn_server** file described in the document) |
| RKNN-Toolkit | Refer to the [documentation](https://github.com/airockchip/rknn-toolkit/blob/master/README.md) to install the new python whl file for upgrade | Refer to the [documentation](https://github.com/airockchip/rknn-toolkit2/blob/master/doc/02_Rockchip_RKNPU_User_Guide_RKNN_SDK_V2.2.0_EN.pdf) **Chapter 2.1** to install the new python whl file for upgrade |

- Please note that due to differences in specifications of development boards, firmware is usually incompatible with each other. Please contact the source of purchase to obtain new firmware and burning methods.



### 1.2 Result differs via platform

Affected by the NPU generation, it is normal for the inference results to be slightly different. If the difference is significant, please submit an issue for feedback.



### 1.3 The demo result not correct

Please check whether the versions of the **driver**, runtime.so, and **RKNN-Toolkit** meet the version requirements listed in the [Document](README.md).



### 1.4 The demo ran correctly, but when I replaced it with my own model, it ran wrong.

Please check whether the requirements of the demo document are followed when exporting the model. For example, follow the [document](./examples/yolov5/README.md) and using https://github.com/airockchip/yolov5 to export onnx model.



### 1.5 Model inference performance does not meet reference performance

The following factors may cause differences in inference performance:

- The inference performance of **python api** may be weaker, please test the inference performance based on **C api**.

- The inference performance data of rknn model zoo does **not include pre-processing and post-processing**. It only counts the time-consuming of **rknn.run**, which is different from the time-consuming of the complete demo. The time-consuming of these other operations is related to usage scenarios and system resource occupancy.
- Whether the board has been **fixed frequency and reached the maximum frequency** set by [scaling_frequency.sh](./scaling_frequency.sh). Some firmware may limit the maximum frequency of the CPU/NPU/DDR, resulting in reduced inference performance.
- Whether there are other applications occupying **CPU/NPU and bandwidth resources**, which will cause the inference performance to be lower.
- For chips with both big and small core CPUs (currently RK3588, RK3576), please refer to [document](https://github.com/airockchip/rknn-toolkit2/blob/master/doc/02_Rockchip_RKNPU_User_Guide_RKNN_SDK_V2.2.0_EN.pdf) Chapter 5.3.3, **bind the big CPU core for testing**.



### 1.6 How to solve the accuracy problem after model quantization

Please refer to the [userguide document](https://github.com/airockchip/rknn-toolkit2/blob/master/doc/02_Rockchip_RKNPU_User_Guide_RKNN_SDK_V2.2.0_EN.pdf) to confirm whether the quantization function is used correctly.

If the **model structural** characteristics and **weight distribution** cause int8 quantization to lose accuracy, please consider using **hybrid quantization** or **QAT quantization**.



### 1.7 Is there a board-side python demo

Install **RKNN-Toolkit-lite** on the board end and use the python inference script corresponding to the demo to implement python inference on the board. For RKNPU1 devices, refer to [RKNN-Toolkit-lite](https://github.com/airockchip/rknn-toolkit/tree/master/rknn-toolkit-lite). For RKNPU2 devices, refer to [RKNN-Toolkit-lite2](https://github.com/airockchip/rknn-toolkit2/tree/master/rknn-toolkit-lite2).

(Some examples currently lack python demo. In addition, it is recommended that users who care about performance use the C interface for deployment)



### 1.8 Why are there no demos for other models? Is it because they are not supported

Actually most of the models are supported. Limited by the development period, consideration for the needs of most developers, we have selected models with higher practicality as demo examples. If you have better model recommendations, please feel free to submit an issue or contact us.



### 1.9 Is there a LLM model demo?

Not provided now. Support for the transformer model is still being gradually optimized, and we also hope to provide large model demos for developers to refer to and use as soon as possible.



### 1.10 Why RV1103 and RV1106 can run fewer demos

Due to the memory size limit of **RV1103** and **RV1106**, the **memory** usage of many larger models exceeds the board limit, so corresponding demos are not provided now.

### 1.11 Segmentation fault error will occur when opencv and jpeg libraries are used together

This is because the jpeg library included in opencv conflicts with jpeg_turbo library in rknn_model_zoo/3rdparty. The solution can be:  
1.Recompile an opencv library without jpeg library  
2.If you only want to use opencv to read or save jpg images, you can specify the '-j' parameter in ./build-linux.sh or ./build-android.sh to disable jpeg_turbo library  

### 1.12 Failed during compilation or prompted that some dependent libraries could not be found during runtime
This is because the cross compiler currently used is different from the default cross compiler used by rknn_model_zoo. Please follow the instructions in the [Compilation_Environment_Setup_Guide.md](./docs/Compilation_Environment_Setup_Guide.md) document to recompile using the corresponding compiler (Note: Remember to delete the old build directory)

## 2. RGA

For RGA related issues, please refer to [RGA documentation](https://github.com/airockchip/librga/blob/main/docs/Rockchip_FAQ_RGA_EN.md).




## 3. YOLO

### 3.1 Class confidence exceeds 1

The **post-processing code** of the YOLO should matches with the model structure, otherwise an exception will occur. The post-process used by the current YOLO demo requires that the **category confidence output** of the model is **generated by sigmoid op**. The sigmoid op adjusts the confidence of (-∞, ∞) to the confidence of (0, 1). The lack of this sigmoid op will cause the category confidence greater than 1, as shown below:

![yolov5_without_sigmoid_out](asset/yolov5_without_sigmoid_out.png)

When encountering such problems, please refer to the instructions of the demo document to export the model.



### 3.2 So many boxes in the inference results and fill the entire picture

![yolo_too_much_box](asset/yolo_too_much_box.png)

As shown above, there are two possibilities:

- Same as the 3.1 section. Missing sigmoid op at the tail of the model may cause this problem.
- **Box threshold** value set too small and the **NMS threshold** value set too large in demo.



### 3.3 The box's position and confidence are correct, but size not match well(yolov5, yolov7)

This problem is usually caused by **anchor mismatch**. When exporting the model, please pay attention to whether the printed anchor information is inconsistent with the default anchor configuration in the demo.



### 3.4 MAP accuracy is lower than official results

There are two main reasons:

- The official map test uses **dynamic shape model**, while rknn model zoo uses a **fixed shape model** for simplicity and ease of use, and the map test results will be lower than the dynamic shape model.
- The RKNN model will also suffer some accuracy loss after **quantization** is turned on.

- If the user tries to use the C interface to test the map results on the board, please note that the way to read the image will affect the test results. For example, the map results are different when testing based on **cv2** and **stbi**.



### 3.5 Can NPU run YOLO without modifying the model structure?

**Yes, but not recommended.**

If the model structure changes, the post-processing code corresponding to python demo and Cdemo needs to be adjusted.

In addition, the adjustment method of the model structure was based on accuracy and performance considerations. Maintaining the original model structure may lead to **poor quantification accuracy** and **worse inference performance**.


===== examples/yolov8/README.md =====
# yolov8

## Table of contents

- [1. Description](#1-description)
- [2. Current Support Platform](#2-current-support-platform)
- [3. Pretrained Model](#3-pretrained-model)
- [4. Convert to RKNN](#4-convert-to-rknn)
- [5. Python Demo](#5-python-demo)
- [6. Android Demo](#6-android-demo)
  - [6.1 Compile and Build](#61-compile-and-build)
  - [6.2 Push demo files to device](#62-push-demo-files-to-device)
  - [6.3 Run demo](#63-run-demo)
- [7. Linux Demo](#7-linux-demo)
  - [7.1 Compile and Build](#71-compile-and-build)
  - [7.2 Push demo files to device](#72-push-demo-files-to-device)
  - [7.3 Run demo](#73-run-demo)
- [8. Expected Results](#8-expected-results)



## 1. Description

The model used in this example comes from the following open source projects:  

https://github.com/airockchip/ultralytics_yolov8



## 2. Current Support Platform

RK3562, RK3566, RK3568, RK3576, RK3588, RV1126B, RV1109, RV1126, RK1808, RK3399PRO


## 3. Pretrained Model

Download link: 

[./yolov8n.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov8/yolov8n.onnx)<br />[./yolov8s.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov8/yolov8s.onnx)<br />[./yolov8m.onnx](https://ftrg.zbox.filez.com/v2/delivery/data/95f00b0fc900458ba134f8b180b3f7a1/examples/yolov8/yolov8m.onnx)

Download with shell command:

```
cd model
./download_model.sh
```

**Note**: The model provided here is an optimized model, which is different from the official original model. Take yolov8n.onnx as an example to show the difference between them.
1. The comparison of their output information is as follows. The left is the official original model, and the right is the optimized model. As shown in the figure, the original one output is divided into three groups. For example, in the set of outputs ([1,64,80,80],[1,80,80,80],[1,1,80,80]), [1,64,80,80] is the coordinate of the box, [1,80,80,80] is the confidence of the box corresponding to the 80 categories, and [1,1,80,80] is the sum of the confidence of the 80 categories.

<div align=center>
  <img src="./model_comparison/yolov8_output_comparison.jpg" alt="Image">
</div>

2. Taking the the set of outputs ([1,64,80,80],[1,80,80,80],[1,1,80,80]) as an example, we remove the subgraphs behind the two convolution nodes in the model, keep the outputs of these two convolutions ([1,64,80,80],[1,80,80,80]), and add a reducesum+clip branch for calculating the sum of the confidence of the 80 categories ([1,1,80,80]).

<div align=center>
  <img src="./model_comparison/yolov8_graph_comparison.jpg" alt="Image">
</div>


## 4. Convert to RKNN

*Usage:*

```shell
cd python
python convert.py <onnx_model> <TARGET_PLATFORM> <dtype(optional)> <output_rknn_path(optional)>

# such as: 
python convert.py ../model/yolov8n.onnx rk3588
# output model will be saved as ../model/yolov8.rknn
```

*Description:*

- `<onnx_model>`: Specify ONNX model path.
- `<TARGET_PLATFORM>`: Specify NPU platform name. Such as 'rk3588'.
- `<dtype>(optional)`: Specify as `i8`, `u8` or `fp`. `i8`/`u8` for doing quantization, `fp` for no quantization. Default is `i8`.
- `<output_rknn_path>(optional)`: Specify save path for the RKNN model, default save in the same directory as ONNX model with name `yolov8.rknn`



## 5. Python Demo

*Usage:*

```shell
cd python
# Inference with PyTorch model or ONNX model
python yolov8.py --model_path <pt_model/onnx_model> --img_show

# Inference with RKNN model
python yolov8.py --model_path <rknn_model> --target <TARGET_PLATFORM> --img_show
```

*Description:*

- `<TARGET_PLATFORM>`: Specify NPU platform name. Such as 'rk3588'.

- `<pt_model / onnx_model / rknn_model>`: Specify the model path.



## 6. Android Demo

**Note: RK1808, RV1109, RV1126 does not support Android.**

#### 6.1 Compile and Build

Please refer to the [Compilation_Environment_Setup_Guide](../../docs/Compilation_Environment_Setup_Guide.md#android-platform) document to setup a cross-compilation environment and complete the compilation of C/C++ Demo.  
**Note: Please replace the model name with `yolov8`.**

#### 6.2 Push demo files to device

With device connected via USB port, push demo files to devices:

```shell
adb root
adb remount
adb push install/<TARGET_PLATFORM>_android_<ARCH>/rknn_yolov8_demo/ /data/
```

#### 6.3 Run demo

```sh
adb shell
cd /data/rknn_yolov8_demo

export LD_LIBRARY_PATH=./lib
./rknn_yolov8_demo model/yolov8.rknn model/bus.jpg
```

- After running, the result was saved as `out.png`. To check the result on host PC, pull back result referring to the following command: 

  ```sh
  adb pull /data/rknn_yolov8_demo/out.png
  ```

- Output result refer [Expected Results](#8-expected-results).



## 7. Linux Demo

#### 7.1 Compile and Build

Please refer to the [Compilation_Environment_Setup_Guide](../../docs/Compilation_Environment_Setup_Guide.md#linux-platform) document to setup a cross-compilation environment and complete the compilation of C/C++ Demo.
**Note: Please replace the model name with `yolov8`.**

#### 7.2 Push demo files to device

- If device connected via USB port, push demo files to devices:

```shell
adb push install/<TARGET_PLATFORM>_linux_<ARCH>/rknn_yolov8_demo/ /userdata/
```

- For other boards, use `scp` or other approaches to push all files under `install/<TARGET_PLATFORM>_linux_<ARCH>/rknn_yolov8_demo/` to `userdata`.

#### 7.3 Run demo

```sh
adb shell
cd /userdata/rknn_yolov8_demo

export LD_LIBRARY_PATH=./lib
./rknn_yolov8_demo model/yolov8.rknn model/bus.jpg
```

- After running, the result was saved as `out.png`. To check the result on host PC, pull back result referring to the following command: 

  ```
  adb pull /userdata/rknn_yolov8_demo/out.png
  ```

- Output result refer [Expected Results](#8-expected-results).



## 8. Expected Results

This example will print the labels and corresponding scores of the test image detect results, as follows:

```
person @ (211 241 283 507) 0.873
person @ (109 235 225 536) 0.866
person @ (476 222 560 521) 0.863
bus @ (99 136 550 456) 0.859
person @ (80 326 116 513) 0.311
```

<img src="result.png">

- Note: Different platforms, different versions of tools and drivers may have slightly different results.

===== LICENSE =====
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
