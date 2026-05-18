# AI/ML Internship — Day 6 (Raritone)

## Overview

Day 6 focuses on improving the practical implementation of AI-based systems by enhancing body measurement accuracy, testing pose detection across different inputs, researching cloth segmentation techniques, creating a recommendation dataset, and integrating AI outputs with backend APIs.

---

## Tasks Completed

### Task 1 — Improve Body Measurement Accuracy

- Implemented body measurement calculation using pose landmarks  
- Calculated distances between key points (e.g., shoulders)  
- Improved measurement estimation using MediaPipe  
- Displayed real-time measurements using OpenCV  

---

### Task 2 — Test Pose Detection on Images and Videos

- Tested pose detection on static images  
- Tested pose detection on video recordings  
- Compared performance across inputs  
- Observed differences in accuracy and tracking  

---

### Task 3 — Research Cloth Segmentation AI

- Studied segmentation techniques (semantic and instance segmentation)  
- Explored deep learning models such as U-Net and Mask R-CNN  
- Understood pixel-level classification of clothing regions  
- Analyzed segmentation workflow  

---

### Task 4 — Create Basic Recommendation Dataset

- Created a simple dataset mapping body size to outfit suggestions  
- Structured dataset in tabular format  
- Used dataset for basic recommendation logic  
- Prepared data for future AI model training  

---

### Task 5 — Integration with Backend APIs

- Implemented Flask API for backend integration  
- Created endpoint to return AI predictions  
- Sent responses in JSON format  
- Simulated real-world AI deployment  

---

## Technologies Used

- Python  
- OpenCV  
- MediaPipe  
- Flask  
- Pandas  
- Artificial Intelligence  
- Computer Vision  
- Machine Learning  

---

## How to Run

1. Activate environment:


mp-final\Scripts\activate


2. Run Task 1 (Measurement):


python practice_code/day6_task1.py


3. Run API:


python practice_code/api.py


4. Open browser:


http://127.0.0.1:5000/predict


---

## Output

- Real-time body measurement detection  
- Pose detection results on images and videos  
- Dataset-based outfit recommendations  
- API response in JSON format  

---

## Project Structure


Raritone/
│
├── day6/
│ ├── README.md
│ ├── task1_measurement
│ ├── task2_pose_testing
│ ├── task3_segmentation
│ ├── task4_dataset
│ ├── task5_api
│
├── practice_code/
│ ├── day6_task1.py
│ ├── api.py


---

## Learning Outcomes

- Improved understanding of pose-based measurement  
- Knowledge of segmentation techniques  
- Experience in dataset creation  
- Understanding of API integration  
- Exposure to real-world AI workflows  

---

## Conclusion

Day 6 focused on transitioning AI models from experimental setups to real-world applications. The tasks improved accuracy, robustness, and system integration, providing a strong foundation for deploying AI solutions in practical scenarios.
