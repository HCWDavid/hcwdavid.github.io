---
layout: default
title: EXACT - A Meta-Learning Framework for Precise Exercise Segmentation in Physical Therapy
---
# EXACT: A Meta-Learning Framework for Precise Exercise Segmentation in Physical Therapy

[![DOI](https://zenodo.org/badge/921933978.svg)](https://doi.org/10.5281/zenodo.14834927)

## Overview

EXACT is a meta-learning framework designed to precisely segment exercises in physical therapy using IMU (Inertial Measurement Unit) sensor data. The framework addresses the critical challenge of automatically identifying exercise boundaries and transitions in continuous sensor data streams, enabling accurate assessment and feedback for remote physical therapy.

## The Challenge

Physical therapy exercises need precise temporal segmentation to:

- Accurately count repetitions
- Assess exercise quality
- Provide timely feedback
- Track patient progress over time

However, traditional supervised learning approaches struggle with:

- **Limited labeled data** for each new patient or exercise type
- **High inter-patient variability** in movement patterns
- **Computational constraints** for real-time on-device processing
- **Need for rapid adaptation** to new exercises without extensive retraining

## Our Solution

EXACT leverages **meta-learning** (learning to learn) to enable few-shot segmentation of exercise data. The framework can quickly adapt to new patients or exercise types with minimal labeled examples while maintaining high segmentation accuracy.

### Key Innovations

1. **Meta-Learning Framework**: Uses Model-Agnostic Meta-Learning (MAML) to learn initialization parameters that can rapidly adapt to new tasks
2. **Temporal Positional Encoding**: Captures temporal dependencies critical for exercise segmentation
3. **Atrous Spatial Pyramid Pooling (ASPP)**: Multi-scale feature extraction for robust segmentation
4. **Dense Labeling Task Sampler**: Specialized episodic sampling for time-series segmentation tasks
5. **Support for Multiple Architectures**: Compatible with U-Net, Transformer, CNN, and custom models

## Technical Architecture

### EXACT-UNet Model

Our best-performing model combines:

- **Temporal and Positional Encoding** for capturing time dependencies
- **ASPP Module** for multi-scale feature extraction
- **U-Net Encoder-Decoder** with skip connections
- **Residual connections** for improved gradient flow

### Meta-Learning Pipeline

```
Support Set (K-shot examples) → Inner Loop Adaptation → Query Set Evaluation
                                      ↓
                              Meta-Optimizer Updates
```

1. **Support Set**: Few labeled examples (e.g., 1-5 samples) from a new task
2. **Inner Loop**: Rapid adaptation using gradient descent
3. **Query Set**: Test on unseen samples from the same task
4. **Meta Update**: Learn better initialization for future adaptation

## Results

EXACT was evaluated on three physical therapy datasets:

- **PhysiQ**: Smartwatch-based shoulder exercises
- **SPAR**: Multi-exercise physical therapy activities
- **MMFIT**: Fitness and rehabilitation exercises

### Performance Metrics

- **Dice Score**: 0.85-0.92 across datasets
- **IoU (Intersection over Union)**: 0.78-0.88
- **ROC-AUC**: 0.90-0.96

**Key Achievement**: EXACT achieves competitive performance with only **1-shot learning** (single example per class), enabling rapid deployment for new patients.

## Code & Resources

- **GitHub Repository**: [AICPS-Lab/EXACT-ICCPS2025](https://github.com/AICPS-Lab/EXACT-ICCPS2025)
- **Docker Image**: `wang584041187/exact:latest`
- **Full Paper**: [Read on ACM Digital Library](https://doi.org/10.1145/3716550.3722027)
- **DOI**: [10.5281/zenodo.14834927](https://doi.org/10.5281/zenodo.14834927)

### Quick Start

```bash
# Pull Docker image
docker pull wang584041187/exact:latest

# Run with GPU
docker run -it --rm --gpus all wang584041187/exact:latest

# Train on PhysiQ dataset
python main_meta_v2.py --dataset physiq --model ex --n_shot 1 --n_epochs 200
```

## Publications

**Wang, Hanchen David**, Bae, Siwoo, Sun, Xutong, Thatigotla, Yashvitha, and Ma, Meiyi. "EXACT: A Meta-Learning Framework for Precise Exercise Segmentation in Physical Therapy." *Proceedings of the ACM/IEEE 16th International Conference on Cyber-Physical Systems (ICCPS)*, 2024.

### Citation

```bibtex
@inproceedings{wang2025exact,
  title={EXACT: A Meta-Learning Framework for Precise Exercise Segmentation in Physical Therapy},
  author={Wang, Hanchen David and Bae, Siwoo and Sun, Xutong and Thatigotla, Yashvitha and Ma, Meiyi},
  booktitle={Proceedings of the ACM/IEEE 16th International Conference on Cyber-Physical Systems (with CPS-IoT Week 2025)},
  pages={1--11},
  year={2025}
}
```

## Technology Stack

- **Framework**: PyTorch
- **Meta-Learning**: MAML/FOMAML
- **Architectures**: U-Net, Transformer, CNN, Custom EX model
- **Logging**: Weights & Biases (WandB)
- **Datasets**: IMU time-series data from smartwatches and wearable sensors

## Supported Models

- **EXACT-UNet**: U-Net with TPE and ASPP (Best Performance)
- **EX**: Custom encoder-decoder with multi-head self-attention
- **Transformer**: Self-attention based temporal model
- **Segmenter**: Transformer-based segmentation model
- **CNN**: Lightweight convolutional baseline

## Impact & Applications

EXACT enables:

- **Personalized Physical Therapy**: Rapid adaptation to individual patient movement patterns
- **Remote Monitoring**: Accurate exercise tracking outside clinical settings
- **Real-time Feedback**: On-device segmentation for immediate coaching
- **Scalable Deployment**: Minimal data requirements for new exercises or patients
- **Clinical Research**: Automated analysis of large-scale therapy data

## Authors

- **Hanchen David Wang** (Corresponding Author) - Vanderbilt University
- Siwoo Bae - Vanderbilt University
- Xutong Sun - Vanderbilt University
- Yashvitha Thatigotla - Vanderbilt University
- Meiyi Ma - Vanderbilt University

## Future Directions

We continue to enhance EXACT through:

- Multi-modal sensor fusion (vision + IMU)
- Continuous learning for long-term patient monitoring
- Integration with therapeutic feedback systems
- Expansion to broader rehabilitation contexts

---

[← Back to Projects](../projects.html)
