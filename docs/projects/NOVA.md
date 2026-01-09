---
layout: default
title: NOVA - Multi-Modal Video Annotation System
---
# NOVA: Multi-Modal Video Annotation System

<div style="margin-bottom: 20px; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white; text-align: center;">
  <a href="../nova/index.html" target="_blank" style="color: white; text-decoration: none; font-size: 1.2em; font-weight: 600;">
    🚀 Launch NOVA Tool →
  </a>
</div>

## Overview

NOVA (Nursing Operational View of Actions) is a web-based video annotation framework designed for multi-modal data analysis. Version 0.2 implements a synchronized playback system for multiple high-fidelity video streams with integrated data overlays, supporting gaze tracking, heatmaps, and IMU sensor visualization.

## Key Features

### Multi-Modal Synchronization
- **Multiple Video Streams**: Load and synchronize multiple video files simultaneously
- **Data Overlays**: Overlay gaze tracking, heatmaps, and IMU data directly on video
- **Time-Synchronized Playback**: Frame-accurate synchronization across all modalities

### Annotation System
- **Layer-Based Annotations**: Organize annotations into customizable layers
- **Keyboard Shortcuts**: Rapid annotation with keyboard-driven workflow
- **Export Support**: Export annotations in standard formats

### Data Support
- **Gaze Tracking**: Native support for Tobii Pro Glasses 3 data
- **IMU Visualization**: 5-second rolling window waveform display
- **Gzip Support**: Direct client-side decompression of .gz files

## Technical Architecture

### Client-Side Processing
NOVA is a fully client-side application requiring no server infrastructure:

- **Pure JavaScript**: No frameworks, maximum compatibility
- **Local File Processing**: Videos and data stay on your machine
- **Responsive Design**: Adaptive layout for various screen sizes

### Canvas Overlay System
The overlay system uses a four-tier canvas sizing strategy:

1. **Base Layer**: Video element with `object-fit: contain`
2. **Overlay Canvas**: Positioned absolutely over video area
3. **Letterbox Detection**: Automatic calculation of video display bounds
4. **Coordinate Mapping**: Accurate translation from data coordinates to display pixels

## Use Cases

NOVA is designed for:

- **Nursing Education Research**: Analyze student performance during simulations
- **Eye-Tracking Studies**: Visualize gaze patterns over procedural videos
- **Behavioral Analysis**: Annotate and categorize actions in video recordings
- **Multi-Sensor Integration**: Combine video with IMU and physiological data

## Quick Start

1. **Open NOVA**: Click the launch button above or navigate to the tool
2. **Add Video**: Click "Add Data" and select your video file(s)
3. **Add Overlays**: Load gaze or IMU data files
4. **Annotate**: Select annotation types and use keyboard shortcuts (S/E) to mark segments
5. **Export**: Save your annotations for analysis

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Space` | Play/Pause |
| `←` / `→` | Previous/Next Frame |
| `S` | Start Annotation |
| `E` | End Annotation |

## Supported Formats

### Video
- MP4, WebM, MOV, AVI

### Data Files
- CSV, TSV (gaze coordinates)
- JSON Lines (Tobii Pro Glasses 3)
- Gzip compressed files (.gz)

## Technology Stack

- **Frontend**: Vanilla JavaScript, CSS3
- **Decompression**: Pako for .gz support
- **Fonts**: Inter (Google Fonts)
- **No Dependencies**: Fully self-contained

## Future Development

Planned enhancements include:

- Additional sensor modality support
- Collaborative annotation features
- Machine learning-assisted annotation suggestions
- Extended export formats

## Authors

- **Hanchen David Wang** - Vanderbilt University

---

[← Back to Projects](../projects.html)
