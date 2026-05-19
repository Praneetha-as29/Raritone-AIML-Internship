# AI/ML Internship — Day 7

## Overview

Day 7 focused on developing AI-based Human Body Detection, Measurement Estimation, Position Detection, Angle Analysis, and Outfit Recommendation Systems using MediaPipe, OpenCV, and CSV dataset processing.

---

# Technologies Used

- Python
- OpenCV
- MediaPipe
- Pandas
- NumPy
- Artificial Intelligence
- Computer Vision

---

# Tasks Completed

## 1. Human Body Landmark Detection
- Implemented body landmark detection using MediaPipe
- Generated skeletal visualization
- Performed body posture analysis
- Tracked human body movement

## 2. Position and Angle Detection
- Calculated body angles using landmark coordinates
- Detected standing and tilted posture
- Analysed body orientation
- Performed skeletal tracking

## 3. Fashion Measurement & Outfit Recommendation
- Estimated chest and waist measurements
- Processed clothing dataset using CSV
- Compared body measurements with clothing sizes
- Recommended suitable outfit sizes

---

# Libraries Used

```python
import cv2
import mediapipe as mp
import pandas as pd
import numpy as np
```

---

# How to Run

## Activate Environment

```bash
mp-final\Scripts\activate
```

## Install Libraries

```bash
pip install opencv-python mediapipe pandas numpy
```

## Run Program

```bash
python recommendation_system.py
```

---

# Project Structure

```text
Day7/
│
├── README.md
├── recommendation_system.py
├── fashion_brand_measurements_dataset.csv
├── screenshots/
├── outputs/
├── Day 7 Module-1.pdf
├── Measurements Estimation Task Praneetha.pdf
└── Position and Angle Detection Praneetha.pdf
```

---

# Outputs Generated

- Human landmark detection
- Skeletal tracking
- Body angle analysis
- Position estimation
- Measurement estimation
- Outfit recommendation

---

# Challenges Faced

| Challenge | Impact |
|---|---|
| Poor lighting | Reduced accuracy |
| Fast movement | Tracking instability |
| Side posture | Angle variation |
| Complex background | Detection variation |

---

# Learning Outcomes

- Human pose estimation
- Landmark tracking
- Body measurement estimation
- AI skeletal visualization
- CSV dataset processing
- Outfit recommendation logic
- Computer vision workflows

---

# Conclusion

Day 7 successfully demonstrated AI-based human landmark detection, posture analysis, body measurement estimation, and outfit recommendation using Computer Vision and Artificial Intelligence technologies.
