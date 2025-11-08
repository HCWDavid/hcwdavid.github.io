---
layout: default
title: PhysiQ - Off-Site Quality Assessment of Exercise in Physical Therapy
---

# PhysiQ: Off-Site Quality Assessment of Exercise in Physical Therapy

## Overview

Welcome to PhysiQ — a groundbreaking framework that revolutionizes physical therapy by enabling patients to effectively continue their therapy at home. PhysiQ addresses a critical challenge in physical therapy: providing quality assessment and feedback for exercises performed outside the clinic.

## Video Talk

<div style="position: relative; padding-bottom: 28.125%; height: 0; overflow: hidden; max-width: 50%; margin: 20px auto;">
  <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://www.youtube.com/embed/bV995aebV0M" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## The Problem

Traditional physical therapy relies heavily on in-person supervision to ensure correct exercise execution. However, patients spend most of their recovery time at home, where the lack of expert supervision often leads to inaccuracies in posture and performance. Existing solutions like Human Activity Recognition (HAR) in wearable devices recognize basic activities but don't cater to therapeutic rehabilitation needs. Vision-based tracking systems are cumbersome and not user-friendly for patients with limited mobility.

## Our Solution

PhysiQ uses passive sensory detection through a smartwatch to track and quantitatively measure off-site exercise activity. Our novel multi-task spatiotemporal Siamese Neural Network evaluates exercises based on both absolute and relative quality of performance, providing patients with real-time, explainable feedback to enhance their recovery process.

**Note:** PhysiQ is designed to enhance the PT experience outside the clinic, not to replace physical therapists.

## Key Features

- **Smartwatch-Based Monitoring**: First framework for quantitative exercise measurement using a smartwatch
- **Three Key Metrics**: Identifies and digitalizes range of motion, stability, and repetition
- **Dual Quality Assessment**: Measures both absolute quality and relative quality based on individual PT progress
- **Real-Time Feedback**: Provides explainable feedback with recommendations for improvement
- **High Accuracy**: Achieved 89.67% accuracy in detecting exercise quality levels and 0.949 R-squared correlation in similarity comparison

## Technical Innovation

### Multi-Task Spatiotemporal Siamese Neural Network

The core of PhysiQ is our innovative neural network architecture:

1. **Input Processing**: Two one-repetition exercises (signal and anchor) are fed into the network
2. **Segmentation**: Sliding window segmentation breaks down continuous exercise data into manageable chunks
3. **Encoding**: Spatial and temporal encoding transforms segments into processable format
4. **Attention Mechanism**: Learned weights focus on the most relevant features of exercise data
5. **Similarity Scoring**: Cosine similarity compares exercises to determine relative quality based on individual progress
6. **Classification**: Multi-layer perceptron outputs absolute quality based on range of motion, stability, and repetition

## Research & Evaluation

Our research collected and annotated motion data from 31 participants performing three shoulder exercises:
- Shoulder Abduction
- External Rotation
- Forward Flexion

PhysiQ outperformed baseline methods by 47.67% on average in R-squared across all exercises and metrics. We also conducted user experience studies to understand how user behaviors influence the framework.

## Publications

- **Full Paper**: [Read on ACM Digital Library](https://doi.org/10.1145/3570349)
- **Medium Article**: [PhysiQ: Off-Site Quality Assessment](https://medium.com/ubicomp-iswc-2023/physiq-off-site-quality-assessment-of-exercise-in-physical-therapy-4666f0f9c70d)

*Published in Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT), Volume 6, Issue 4, December 2022*

## Technology Stack

- Deep Learning
- Wearable Sensors (Smartwatch)
- Siamese Neural Networks
- Multi-Task Learning
- Python

## Authors

Hanchen David Wang, Meiyi Ma

## Impact & Future

PhysiQ represents a significant advancement in physical therapy by:
- Empowering patients to take charge of their recovery process
- Providing invaluable data to therapists for personalized therapy plans
- Making physical therapy more accessible for remote rehabilitation

We continue to refine PhysiQ through user feedback, research findings, and technological advancements, working towards revolutionizing physical therapy to ensure optimal patient recovery outcomes.

---

[← Back to Projects](../projects.html)
