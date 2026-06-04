# 🩺 PCOS Detection Using Deep Learning and Explainable AI

## Overview

Polycystic Ovary Syndrome (PCOS) is one of the most common hormonal disorders affecting women worldwide. Early detection is crucial for timely treatment and prevention of long-term health complications.

This project presents a Deep Learning-based web application that detects PCOS from ovarian ultrasound images and provides interpretable predictions using Explainable AI (XAI) techniques. The system achieved an impressive accuracy of **99.79%**, making it a powerful tool for assisting medical diagnosis.

---

## Problem Statement

PCOS diagnosis often requires extensive clinical examination and expert interpretation of ultrasound scans. Manual analysis can be time-consuming and subjective.

The objective of this project is to:

* Automatically detect PCOS from ultrasound images.
* Assist healthcare professionals in diagnosis.
* Improve accessibility to preliminary screening tools.
* Enhance model transparency using Explainable AI techniques.

---

## Features

- PCOS Detection from Ultrasound Images

- Deep Learning-Based Classification

- Explainable AI (XAI) Visualization

- User-Friendly Web Interface
  
---

## Tech Stack

### Machine Learning & Deep Learning

* Python
* TensorFlow
* Keras
* NumPy
* Pandas

### Computer Vision

* OpenCV

### Frontend

* HTML
* CSS
* JavaScript

### Data Visualization

* Matplotlib

---

## Dataset

The model was trained using ovarian ultrasound images from Kaggle categorized into:

* PCOS Positive Cases
* Non-PCOS Cases

The dataset underwent preprocessing and augmentation to improve model robustness and generalization.

---

## Methodology

### 1. Data Collection

Collection of ovarian ultrasound images.

### 2. Data Preprocessing

* Image resizing
* Noise reduction
* Normalization
* Data augmentation

### 3. Model Training

Multiple DL models were trained to classify ultrasound images into PCOS and Non-PCOS categories.

### 4. Explainable AI Integration

Explainable AI techniques were applied to visualize the regions of the ultrasound image influencing model predictions, improving transparency and trustworthiness.

### 5. Web Application Development

A responsive web application was developed to allow users to upload ultrasound images and obtain predictions instantly.

---

## Model Performance

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 99.79% |
| Precision | High   |
| Recall    | High   |
| F1 Score  | High   |

### Overall Accuracy

**99.79%**

---

## Project Workflow

1. Ultrasound Image Upload
2. Image Preprocessing
3. Deep Learning Inference
4. Explainable AI Analysis
5. Prediction Generation
6. Result Visualization

---

## Screenshots

Add screenshots of the application:

### Home Page

```md
(<img width="1915" height="932" alt="image" src="https://github.com/user-attachments/assets/d66553f6-cd2b-422d-84b9-f994e57fbecb" />)
*Screenshot of home page*
```

### Upload Interface

```md
(<img width="1907" height="929" alt="image" src="https://github.com/user-attachments/assets/fb2504c1-c13c-4bc2-b6d9-d9ffa62f87a2" />)
*Screenshot of upload page*
```

### Prediction Result

```md
(<img width="1859" height="927" alt="image" src="https://github.com/user-attachments/assets/5a494b5b-973e-41b3-b63f-52ec9692cb92" />)
*Screenshot of prediction*
```

### Explainable AI Visualization

```md
(<img width="705" height="772" alt="image" src="https://github.com/user-attachments/assets/a0cc6073-5948-47eb-a4d9-981d8c3f9d93" />)
*Comparison with XAI visualization*
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/jahnavinischal/PCOS-detection-using-DL.git
cd PCOS-detection-using-DL
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## Future Enhancements

* Integrate clinical reports along with ultrasound images to aid in more accurate detection
* Real-time data integration
* Mobile application and website support
* Advanced Explainable AI visualizations
* Clinical decision support features
