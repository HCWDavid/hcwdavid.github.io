# Learning with Preserving (LwP)

## Overview

**Learning with Preserving (LwP)** is a novel continual learning framework designed to address catastrophic forgetting in continual multitask learning (CMTL) scenarios. Unlike traditional approaches that focus on preserving task-specific outputs, LwP fundamentally shifts the paradigm by maintaining the geometric structure of learned representations through **Dynamic Weighted Distance Preservation (DWDP)**.

### The Problem

In real-world applications like autonomous driving and medical imaging, AI systems must continuously learn new tasks using shared input streams without forgetting previously acquired knowledge. For example, after learning to detect traffic signs, a model must later learn to classify traffic lights using the same camera feed. This scenario presents unique challenges:

- **Catastrophic Forgetting**: Neural networks tend to forget previously learned tasks when adapting to new ones
- **Task Interference**: Learning fragmented, task-specific features that conflict with one another
- **Privacy Constraints**: Many domains (healthcare, finance) cannot store historical data for replay

### The Solution

LwP introduces a fundamentally different approach by:

1. **Preserving Representation Structure**: Instead of focusing only on task outputs, LwP maintains the geometric relationships between learned representations
2. **Dynamic Weighted Distance Preservation (DWDP)**: A novel loss function that prevents representation drift by regularizing pairwise distances in the latent space
3. **Privacy-Preserving Design**: No replay buffer required, making it suitable for sensitive applications
4. **Robust to Distribution Shifts**: Demonstrated superior performance when data distributions change over time

## Technical Architecture

### Core Components

LwP consists of three main architectural components:

1. **Shared Encoder**: Feature extraction backbone (ResNet, ViT, etc.) that learns generalizable representations
2. **Task-Specific Predictors**: Separate classification heads for each learned task
3. **Preservation Mechanism**: Frozen copies of previous models for computing DWDP loss

### Dynamic Weighted Distance Preservation (DWDP) Loss

The key innovation is the DWDP loss function, which maintains the geometric structure of the representation space:

$$
\mathcal{L}_{\text{DWDP}} = \frac{1}{N^2} \sum_{i,j} m_{ij} \cdot (d(z_i, z_j) - d(z'_i, z'_j))^2
$$

Where:

- $z, z'$ are current and past representations
- $d(\cdot, \cdot)$ is a distance metric (L2, RBF, Cosine, or RKD)
- $m_{ij}$ is a dynamic mask based on label similarity

**Dynamic Weighting**: The mask $m_{ij}$ is crucial - it equals 1 for same-class pairs and 0 for different-class pairs, preventing conflicts between preservation and classification objectives.

### Total Loss Function

The complete LwP objective combines three components:

$$
\mathcal{L}_{\text{total}} = \lambda_{\text{new}} \mathcal{L}_{\text{current}} + \lambda_{\text{old}} \mathcal{L}_{\text{distillation}} + \lambda_{\text{dwdp}} \mathcal{L}_{\text{DWDP}}
$$

- **Current Task Loss**: Supervised learning on the new task
- **Distillation Loss**: Preserves performance on previous tasks via pseudolabels
- **DWDP Loss**: Maintains geometric structure of representations

### Supported Distance Metrics

LwP supports multiple distance metrics for different representation spaces:

- **L2 (Euclidean)**: $||z_i - z_j||_2$ - Standard distance measure
- **RBF Kernel**: $\exp(-||z_i - z_j||_2^2)$ - Non-linear similarity
- **Cosine Similarity**: $\langle z_i, z_j \rangle / (||z_i||_2 ||z_j||_2)$ - Angle-based
- **RKD**: Relational Knowledge Distillation - Preserves relative distances

## Experimental Results

### Benchmark Performance

LwP was evaluated on four diverse datasets spanning image and time-series domains:

| Dataset            | Type                 | Tasks | LwP Accuracy      | Best Baseline | Improvement |
| ------------------ | -------------------- | ----- | ----------------- | ------------- | ----------- |
| **CelebA**   | Face Attributes      | 10    | **85.064%** | 70.921% (DVC) | +14.1%      |
| **FairFace** | Demographics         | 7     | **69.432%** | 65.340% (DVC) | +4.1%       |
| **BDD100K**  | Autonomous Driving   | 4     | **77.227%** | 72.5% (FDR)   | +4.7%       |
| **PhysiQ**   | Exercise Recognition | 3     | **67.388%** | 64.220% (OBC) | +3.2%       |

### Key Findings

1. **Only Method to Exceed Single-Task Learning**: LwP is the only continual learning method that surpasses the performance of training each task independently, suggesting it benefits from positive knowledge transfer
2. **Superior Backward Transfer**: Across all benchmarks, LwP demonstrates the best Backward Transfer (BWT) scores, indicating minimal forgetting of previous tasks
3. **Robustness to Distribution Shifts**: In non-stationary environments (weather shifts, time-of-day changes), LwP maintains significant advantages over baselines
4. **Modality-Agnostic**: Consistent performance across both image-based tasks (CelebA, FairFace, BDD100K) and time-series data (PhysiQ from IMU sensors)

### Ablation Studies

Comprehensive ablation studies demonstrate:

- **Dynamic Weighting is Critical**: Disabling dynamic weighting significantly degrades performance
- **Scalability**: Performance improvements maintain across different model sizes (ResNet18/50/101) and input resolutions
- **Distance Metric Selection**: L2 distance performs best overall, with RBF as a strong alternative for non-linear spaces

## Code & Resources

### GitHub Repository

The complete implementation, including training scripts, evaluation tools, and pretrained models, is available at:

**[https://github.com/AICPS-Lab/lwp](https://github.com/AICPS-Lab/lwp)**

### Key Features

- **Comprehensive Framework**: Supports continual learning (CL), multi-task learning (MTL), and hybrid MTL-to-CL training
- **Multiple Baselines**: Implementations of 11 continual learning methods (ER, DER, DERPP, LwF, EWC, SI, GSS, FDR, DVC, OBC)
- **Automatic Dataset Handling**: Built-in support for automatic download and preprocessing
- **Flexible Configuration**: Easy hyperparameter tuning and experiment management
- **Evaluation Tools**: Comprehensive analysis framework with visualization and statistical testing
- **WandB Integration**: Real-time experiment tracking and monitoring

### Quick Start

```bash
# Clone the repository
git clone https://github.com/AICPS-Lab/lwp.git
cd lwp

# Install dependencies
pip install torch torchvision pandas numpy matplotlib seaborn scipy scikit-learn datasets wandb tqdm

# Basic training with LwP on CelebA
python main.py --job cl --model lwp --dataset celeba --num_seed 5

# Hyperparameter tuning
python main.py --job cl --model lwp --dataset celeba \
    --lam_dwdp 0.05 --lam_old 1.0 --dist_method rbf \
    --architecture resnet50 --epochs 30

# Evaluation and analysis
python eval_v2.py --dataset celeba --job cl --model lwp --save_plots
```

### Supported Datasets

- **CelebA**: Face attribute classification (200K+ images, 10 tasks)
- **FairFace**: Demographic attribute classification (7 tasks)
- **BDD100K**: Autonomous driving scene understanding (4 tasks)
- **PhysiQ**: Physiotherapy exercise recognition from IMU sensors (3 tasks)

## Publication

**Learning with Preserving for Continual Multitask Learning**
*Hanchen David Wang\*, Siwoo Bae\*, Zirong Chen, Meiyi Ma*
**AAAI Conference on Artificial Intelligence (AAAI), 2026* *(Accepted - Oral Presentation)*

\*Equal contribution

### Abstract

Artificial intelligence systems in critical fields like autonomous driving and medical imaging must continually learn new tasks using shared input streams. This introduces Continual Multitask Learning (CMTL), where models sequentially learn tasks on an underlying data distribution without forgetting previous abilities. Existing continual learning methods often fail because they learn fragmented, task-specific features that interfere with one another. We introduce Learning with Preserving (LwP), a framework that shifts focus from preserving task outputs to maintaining the geometric structure of the shared representation space. The core innovation is a Dynamically Weighted Distance Preservation (DWDP) loss that prevents representation drift by regularizing pairwise distances between latent representations. This mechanism enables the model to retain implicit knowledge and support diverse tasks without replay buffers, making it suitable for privacy-conscious applications. Extensive evaluations on time-series and image benchmarks demonstrate that LwP consistently outperforms state-of-the-art methods and exceeds single-task learning performance.

### Citation

```bibtex
@inproceedings{wang2026lwp,
  title={Learning with Preserving for Continual Multitask Learning},
  author={Wang, Hanchen David and Bae, Siwoo and Chen, Zirong and Ma, Meiyi},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  year={2026},
  organization={AAAI}
}
```

## Impact & Applications

### Real-World Applications

1. **Autonomous Driving**: Continuously learning to detect new objects (traffic signs → traffic lights → pedestrians → vehicles) without forgetting previous capabilities
2. **Medical Diagnosis**: Adapting to new diagnostic tasks while maintaining performance on existing conditions, crucial for privacy-sensitive healthcare data
3. **Robotics**: Sequential learning of manipulation skills and scene understanding without catastrophic forgetting
4. **Mobile Health**: Exercise recognition systems that adapt to new exercise types while preserving learned patterns

### Technical Contributions

- **Novel Problem Formulation**: Formally defines and analyzes Continual Multitask Learning (CMTL) as distinct from traditional continual learning
- **Theoretical Foundation**: Provides theoretical justification for preserving geometric structure in representation space
- **Privacy-Preserving Design**: No replay buffer requirement makes LwP suitable for sensitive domains (healthcare, finance)
- **Benchmark Establishment**: Comprehensive evaluation framework for CMTL scenarios

### Future Directions

The LwP framework opens several promising research directions:

- **Adaptive Weighting**: Learning task-specific DWDP weights automatically
- **Online Learning**: Extending to online/streaming data scenarios
- **Few-Shot Adaptation**: Combining with meta-learning for rapid task adaptation
- **Lifelong Learning**: Scaling to hundreds or thousands of sequential tasks

---

## Contact

For questions, collaborations, or additional information:

**Hanchen David Wang** (Corresponding Author)
Vanderbilt University
Email: hanchen.wang.1@vanderbilt.edu

**Project Team**:

- Hanchen David Wang* - Vanderbilt University
- Siwoo Bae* - Vanderbilt University
- Zirong Chen - Vanderbilt University
- Meiyi Ma - Vanderbilt University

*Equal contribution
