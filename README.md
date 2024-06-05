# U-KAN Makes Strong Backbone for Medical Image Segmentation and Generation

:pushpin: This is an official PyTorch implementation of **U-KAN Makes Strong Backbone for Medical Image Segmentation and Generation**

<p align="center">
  <img src="./assets/logo_1.png" alt="" width="120" height="120">
</p>

> [**U-KAN Makes Strong Backbone for Medical Image Segmentation and Generation**](https://arxiv.org)<br>
> [Chenxin Li](https://xggnet.github.io/)\*, [Xinyu Liu](https://xinyuliu-jeffrey.github.io/)\*, [Wuyang Li](https://wymancv.github.io/wuyang.github.io/)\*, [Cheng Wang](https://scholar.google.com/citations?user=AM7gvyUAAAAJ&hl=en)\*, [Hengyu Liu](), [Yixuan Yuan](https://www.ee.cuhk.edu.hk/~yxyuan/people/people.htm)<sup>✉</sup><br>The Chinese Univerisity of Hong Kong

We explore the untapped potential of KANs in improving backbones for vision tasks. We investigate, modify and re-design the established U-Net pipeline by integrating the dedicated KAN layers on the tokenized intermediate representation, termed U-KAN. Rigorous medical image segmentation benchmarks verify the superiority of U-KAN by higher accuracy even with less computation cost. We further delved into the potential of U-KAN as an alternative U-Net noise predictor in diffusion models, demonstrating its applicability in generating task-oriented model architectures. These endeavours unveil valuable insights and sheds light on the prospect that with U-KAN, you can make strong backbone for medical image segmentation and generation.

<div align="center">
    <img width="100%" alt="UKAN overview" src="assets/framework-1.png"/>
</div>

## 📰News

**[2024.6]** Code and paper of U-KAN are released!

## 💡Key Features
- The first effort to incorporate the advantage of emerging KAN to improve established U-Net pipeline to be more **accurate, efficient and interpretable**.
- A Segmentation U-KAN with **tokenized KAN block to effectively steer the KAN operators** to be compatible with the exiting convolution-based designs.
- A Diffusion U-KAN as an **improved noise predictor** demonstrates its potential in backboning generative tasks and broader vision settings.

## 🛠Setup

```bash
git clone https://github.com/CUHK-AIM-Group/U-KAN.git
cd U-KAN
conda create -n ukan python=3.10
conda activate ukan
cd Seg_UKAN && pip install -r requirements.txt
```

**Tips A**: We test the framework using pytorch=1.13.0, and the CUDA compile version=11.6. Other versions should be also fine but not totally ensured.


## 📚Data Preparation
**BUSI**:  The dataset can be found [here](https://www.kaggle.com/datasets/aryashah2k/breast-ultrasound-images-dataset). 

**GLAS**:  The dataset can be found [here](https://websignon.warwick.ac.uk/origin/slogin?shire=https%3A%2F%2Fwarwick.ac.uk%2Fsitebuilder2%2Fshire-read&providerId=urn%3Awarwick.ac.uk%3Asitebuilder2%3Aread%3Aservice&target=https%3A%2F%2Fwarwick.ac.uk%2Ffac%2Fcross_fac%2Ftia%2Fdata%2Fglascontest&status=notloggedin). 
<!-- You can directly use the [processed GLAS data]() without further data processing. -->
**CVC-ClinicDB**:  The dataset can be found [here](https://www.dropbox.com/s/p5qe9eotetjnbmq/CVC-ClinicDB.rar?e=3&dl=0). 
<!-- You can directly use the [processed CVC-ClinicDB data]() without further data processing. -->

We also provide all the [pre-processed dataset](https://mycuhk-my.sharepoint.com/:f:/g/personal/1155206760_link_cuhk_edu_hk/ErDlT-t0WoBNlKhBlbYfReYB-iviSCmkNRb1GqZ90oYjJA?e=hrPNWD) without requiring any further data processing. You can directly download and put them into the data dir.



The resulted file structure is as follows.
```
Seg_UKAN
├── inputs
│   ├── busi
│     ├── images
│           ├── malignant (1).png
|           ├── ...
|     ├── masks
│        ├── 0
│           ├── malignant (1)_mask.png
|           ├── ...
│   ├── GLAS
│     ├── images
│           ├── 0.png
|           ├── ...
|     ├── masks
│        ├── 0
│           ├── 0.png
|           ├── ...
│   ├── CVC-ClinicDB
│     ├── images
│           ├── 0.png
|           ├── ...
|     ├── masks
│        ├── 0
│           ├── 0.png
|           ├── ...
```

## 🔖Evaluating Segmentation U-KAN

You can directly evaluate U-KAN from the checkpoint model. Here is an example for quick usage for using our **pre-trained models** in [Segmentation Model Zoo](#segmentation-model-zoo):
1. Download the pre-trained weights and put them to ```{args.output_dir}/{args.name}/model.pth```
2. Run the following scripts to 
```bash
cd Seg_UKAN
python val.py --name ${dataset}_UKAN --output_dir [YOUR_OUTPUT_DIR] 
```

## ⏳Training Segmentation U-KAN

You can simply train U-KAN on a single GPU by specifing the dataset name ```--dataset``` and input size ```--input_size```.
```bash
cd Seg_UKAN
python train.py --arch UKAN --dataset ${dataset} --input_w ${input_size} --input_h ${input_size} --name ${dataset}_UKAN  --data_dir [YOUR_DATA_DIR]
```
For example, train U-KAN with the resolution of 256x256 with a single GPU on the BUSI dataset in the ```inputs``` dir:
```bash
cd Seg_UKAN
python train.py --arch UKAN --dataset busi --input_w 256 --input_h 256 --name busi_UKAN  --data_dir ./inputs
```
Please see Seg_UKAN/scripts.sh for more details.

## 🎪Segmentation Model Zoo

Here is an overview of performance&checkpoints.
|Method| Dataset | IoU | F1  | Checkpoints |
|-----|------|-----|-----|-----|
|Seg U-KAN| BUSI | -- | --| [Link]()|
|Seg U-KAN| GLAS | -- | --| [Link]()|
|Seg U-KAN| CVC | -- | --| [Link]()|

## 🎇Medical Image Generation with Diffusion U-KAN


## 🎪Diffusion Model Zoo

Here is an overview of performance&checkpoints.
|Method| Dataset | FID | IS  | Checkpoints |
|-----|------|-----|-----|-----|
|Diffusion U-KAN| BUSI | -- | --| [Link]()|
|Diffusion U-KAN| GLAS | -- | --| [Link]()|
|Diffusion U-KAN| CVC | -- | --| [Link]()|


## 🛒TODO List
- [X] Release code for Seg U-KAN
- [X] Release code for Diffusion U-KAN
- [X] Upload the pretrained checkpoints.


## 🎈Acknowledgements
Greatly appreciate the tremendous effort for the following projects!
- [CKAN](https://github.com/AntonioTepsich/Convolutional-KANs)


## 📜Citation
If you find this work helpful for your project,please consider citing the following paper:
```
@article{li2024endora,
  author    = {Chenxin Li and Xinyu Liu and Wuyang Li and Cheng Wang and Hengyu Liu and Yixuan Yuan},
  title     = {U-KAN Makes Strong Backbone for Medical
Image Segmentation and Generation},
  journal   = {arXiv preprint},
  year      = {2024}
}
```