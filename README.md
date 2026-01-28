# 🩺 Skin Cancer Detection using Deep Learning (TensorFlow & Keras)

This project implements a **Skin Cancer Detection System** using **Deep Learning**.  
A **Convolutional Neural Network (CNN)** is trained to classify skin lesion images into:

- **Cancer (Malignant)**
- **Non-Cancer (Benign)**

The model is optimized using **Keras Tuner** for hyperparameter tuning and deployed using a **Streamlit web application** for real-time predictions.

---

## 📌 Project Highlights
- Binary image classification (Cancer vs Non-Cancer)
- CNN model built using TensorFlow & Keras
- Hyperparameter tuning using **Keras Tuner**
- Model saved in **`.keras` format**
- Interactive **Streamlit web app**
- Upload image and get instant prediction

---

## 🧠 Technologies & Tools
- Python
- TensorFlow / Keras
- Keras Tuner
- OpenCV
- Streamlit
- NumPy
- Matplotlib

---


---

## 🗂 Dataset Description
The dataset consists of labeled skin lesion images divided into two classes:

- **Cancer (Malignant)**
- **Non-Cancer (Benign)**

### Preprocessing Steps:
- Resize images to **224 × 224**
- Normalize pixel values (0–1)
- Convert images into NumPy arrays
- Split data into training and validation sets

---

## ⚙️ Model Architecture & Training
- Convolutional Neural Network (CNN)
- ReLU activation in hidden layers
- Sigmoid activation in output layer
- Binary Cross-Entropy loss function
- Adam optimizer
- Hyperparameters tuned using **Keras Tuner**
- Best-performing model saved as `final_model.keras`

---

## 📊 Model Output
The model predicts a probability value:
- **> 0.5 → Cancer (Malignant)**
- **≤ 0.5 → Non-Cancer (Benign)**

---

## 🚀 Streamlit Web Application
The Streamlit app allows users to:

1. Upload a skin lesion image (`.jpg`, `.jpeg`, `.png`)
2. Automatically preprocess the image
3. Load the trained `.keras` model
4. Predict the result
5. Display diagnosis:
   - **Cancer Predicted (Malignant)**
   - **No Cancer Predicted (Benign)**

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/skin-cancer-detection.git
cd skin-cancer-detection

