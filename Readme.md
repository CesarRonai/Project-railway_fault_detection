# 🚄 Railway Fault Detection - Detecting Railway Track Failures with Deep Learning

🔍 **A Data Science and Deep Learning project to identify railway track failures using Convolutional Neural Networks (CNNs).**  

---

## 📌 Project Overview
Railway infrastructure maintenance is essential to ensure transportation safety and efficiency. This project applies **Deep Learning** to detect failures in railway tracks using images, enabling faster and more accurate fault identification.

📊 The model was trained on the **Railway Track Fault Detection Updated** dataset, leveraging **Convolutional Neural Networks (CNNs)** to classify the images.

---

## 📋 Table of Contents
1. [Dataset Overview](#dataset-overview)
2. [Methodology](#methodology)
3. [Technologies Used](#technologies-used)
4. [Project Structure](#project-structure)
5. [How to Run the Project](#how-to-run-the-project)
6. [Results & Conclusions](#results--conclusions)
7. [Contributions & Contact](#contributions--contact)

---

## 🗂️ Dataset Overview
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

## 📁 Project Structure
```
Project-railway_fault_detection/
│-- Notebooks/
│   ├── railway_fault_detection.ipynb  # Main Jupyter Notebook
│-- data/
│   ├── railway_images/  # Images of railway tracks
│-- models/
│   ├── model_vgg16_trilhos.h5  # Trained Model
│-- src/
│   ├── train_model.py  # Model training script
│   ├── app.py  # Flask API script
│-- dashboard.py  # Streamlit dashboard
│-- requirements.txt  # Dependencies list
│-- README.md  # Project documentation
```

---

## 📦 How to Run the Project

### 📌 1️⃣ Clone the Repository
```bash
git clone https://github.com/CesarRonai/Project-railway_fault_detection.git
cd Project-railway_fault_detection
```

### 📌 2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate  # Windows
```

### 📌 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 📌 4️⃣ Run the Model
```bash
python src/train_model.py
```

### 📌 5️⃣ Start the Flask API
```bash
python src/app.py
```
Access the API at **http://127.0.0.1:5000**

### 📌 6️⃣ Launch the Streamlit Dashboard
```bash
streamlit run dashboard.py
```

---

## 📊 Results & Conclusions
- The **VGG16 model** achieved the highest accuracy of **97.8%** in fault detection.  
- **Grad-CAM visualization** provided insights into the areas influencing model predictions.  
- **Deployment via Flask API & Streamlit** made the model accessible for external use.  

---

## 📌 Contributions & Contact
Contributions are welcome! Feel free to open a **Pull Request** or reach out for collaborations:

📧 **Email:** cesar.ronai@hotmail.com
🐙 **GitHub:** [CesarRonai](https://github.com/CesarRonai)  

🚀 **Let's revolutionize railway maintenance with AI!** 🚆🔥  

---

### 🔥 **If you liked this project, give it a ⭐ on GitHub!**  

