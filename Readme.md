# 🚄 Railway Fault Detection - Detecting Railway Track Failures with Deep Learning

🔍 **A Data Science and Deep Learning project to identify railway track failures using Convolutional Neural Networks (CNNs).**  

---

## 📌 Project Overview  
Railway infrastructure maintenance is essential to ensure transportation safety and efficiency. This project applies **Deep Learning** to detect failures in railway tracks using images, enabling faster and more accurate fault identification.  

📊 The model was trained on the **Railway Track Fault Detection Updated** dataset, leveraging **Convolutional Neural Networks (CNNs)** to classify the images.  

---

## 🗂️ Dataset Used  
The project utilizes the **Railway Track Fault Detection Updated** dataset, which includes images of railway tracks with and without defects. The dataset structure consists of:  

- **Images of normal railway tracks**  
- **Images of defective railway tracks**  
- **Annotations describing different types of faults**  

The dataset was **preprocessed**, including **normalization, data augmentation, and class balancing** to improve model performance.  

---

## 🚀 Methodology  
The project follows a **Deep Learning-based approach**, using CNN models with the following key steps:  

1️⃣ **Exploratory Data Analysis (EDA)**  
2️⃣ **Image Preprocessing** (Normalization, Data Augmentation)  
3️⃣ **Training CNN Models** (ResNet, VGG16, MobileNet)  
4️⃣ **Explainability with Grad-CAM** (Visualizing model attention regions)  
5️⃣ **Error Analysis & Hyperparameter Tuning**  
6️⃣ **Deployment via Flask API & Streamlit Dashboard**  

---

## 🛠️ Technologies Used  

| Technology | Description |
|------------|-------------|
| Python 🐍 | Primary programming language |
| TensorFlow/Keras 🤖 | Deep Learning framework |
| OpenCV 📸 | Image processing |
| Pandas 🐼 | Data manipulation |
| Matplotlib/Seaborn 📊 | Data visualization |
| Flask 🌐 | API for real-time predictions |
| Streamlit 📈 | Interactive dashboard |
| Git & GitHub 🛠️ | Version control & repository |

---

## 📦 How to Run the Project  

### 📌 1️⃣ Clone the Repository  
```bash
git clone https://github.com/CesarRonai/Project-railway_fault_detection.git
cd Project-railway_fault_detection
