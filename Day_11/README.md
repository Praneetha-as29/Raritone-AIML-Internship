## Overview

This project demonstrates a basic 2D Virtual Try-On (VTON) system developed using OpenCV, MediaPipe, NumPy, and image preprocessing techniques. The system detects human body landmarks, removes garment backgrounds, applies TPS-style garment warping, and overlays clothing onto a person's image to simulate a virtual clothing trial.

---

## Technologies Used

- Python
- OpenCV
- MediaPipe Pose
- NumPy
- rembg
- TPS Style Transformation

---

## Project Structure

Day11/
│
├── person.jpg
├── garment.png
├── garment2.png
├── garment4.png
│
├── pose_detection.py
├── vton_demo.py
├── remove_bg.py
├── tps_vton.py
│
├── pose_output.jpg
├── vton_output.jpg
├── tps_vton_output.jpg
│
└── README.md

---

## Workflow

Person Image
↓
Pose Detection
↓
Garment Preprocessing
↓
Background Removal
↓
TPS Style Garment Warping
↓
Transparent Overlay
↓
Virtual Try-On Output

---

## Features

### Pose Detection
- Human body landmark detection using MediaPipe
- Skeleton visualization
- Shoulder coordinate extraction

### Garment Preprocessing
- Background removal using rembg
- Transparent PNG generation
- Image normalization

### TPS Style Garment Warping
- Garment deformation before placement
- Improved garment alignment
- Better visual fitting

### Virtual Try-On
- Garment placement on torso region
- Transparent overlay using alpha blending
- Virtual clothing visualization

---

## Files Description

### pose_detection.py
Detects human body landmarks and visualizes the pose skeleton.

### remove_bg.py
Removes garment background and generates transparent PNG images.

### vton_demo.py
Implements basic garment overlay on a person image.

### tps_vton.py
Applies TPS-style garment warping and generates an improved Virtual Try-On output.

---

## Results

The project successfully performs:

- Human pose detection
- Body landmark extraction
- Shoulder detection
- Background removal
- Transparent garment generation
- TPS-style garment transformation
- Garment warping
- Virtual Try-On generation

Generated Outputs:

- pose_output.jpg
- vton_output.jpg
- tps_vton_output.jpg

---

## Future Improvements

- Human body segmentation
- AI-based garment fitting
- Deep learning Virtual Try-On models
- 3D avatar generation
- Real-time Virtual Try-On systems
- Multi-garment support

---

## Conclusion

A basic 2D Virtual Try-On prototype was successfully developed using OpenCV and MediaPipe. The system combines pose detection, garment preprocessing, TPS-style transformation, and virtual garment placement to simulate digital clothing trials and provides a foundation for future AI-powered fashion technology applications.
