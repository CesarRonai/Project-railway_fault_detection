🚆 Railway Track Fault Detection

📌 Project Overview

Railway infrastructure is critical for transportation systems worldwide, and ensuring the integrity of railway tracks is essential for safety and efficiency. This project leverages Deep Learning techniques to automate the detection of faults in railway tracks using image classification. The model is deployed via an API and a Streamlit dashboard, making it a robust and user-friendly solution for real-world applications.

🎯 Objectives

Develop a Deep Learning model to classify railway track conditions (Defective vs. Non-Defective).

Implement Grad-CAM for explainability and advanced error analysis.

Deploy the trained model using a Flask API.

Create an interactive Streamlit dashboard for real-time image classification.

🛠 Technologies Used

Python 3.11

TensorFlow / Keras (Deep Learning)

OpenCV (Image Processing)

Matplotlib & Seaborn (Visualization)

Flask (API Deployment)

Streamlit (Dashboard)

Grad-CAM (Explainability)

📂 Dataset

O conjunto de dados utilizado neste projeto está disponível no Kaggle:

🔗 [Railway Track Fault Detection Updated](COLOQUE_AQUI_O_LINK_DO_KAGGLE)

Estrutura do Dataset:

Railway Track Fault Detection Updated/
│── Train/
│   ├── Defective/
│   ├── Non-Defective/
│── Validation/
│   ├── Defective/
│   ├── Non-Defective/
│── Test/
│   ├── Defective/
│   ├── Non-Defective/

📥 Como Baixar o Dataset

Para utilizar este dataset, você pode baixá-lo diretamente do Kaggle ou utilizar o comando abaixo:

pip install kaggle
kaggle datasets download -d usuario/nome-do-dataset --unzip

🔍 Exploratory Data Analysis (EDA)

Verificamos a estrutura e integridade do dataset.

Checamos imagens corrompidas.

Visualizamos amostras das categorias Defective e Non-Defective.

Analisamos a distribuição das imagens entre treino, validação e teste.

🧠 Model Development

O modelo foi construído utilizando Transfer Learning com a arquitetura VGG16:

Pretrained VGG16 model (com pesos do ImageNet) foi usado como feature extractor.

Camadas totalmente conectadas customizadas foram adicionadas para classificação binária.

Otimização com Adam e função de perda Binary Cross-Entropy.

Early Stopping foi implementado para evitar overfitting.

Final Model Performance:

Training Accuracy: 72.08%

Validation Accuracy: 76.27%

🖼 Explainability with Grad-CAM

Para melhorar a interpretabilidade do modelo, utilizamos Grad-CAM, que destaca as áreas das imagens que mais influenciaram a decisão do modelo. Isso ajuda a entender melhor como o modelo identifica falhas nos trilhos.

🌐 Deployment

1️⃣ Flask API

Uma Flask API foi criada para permitir previsões em tempo real.

Rodando a API:

python app.py

Testando a API:

curl -X POST -F "file=@path\_to\_image.jpg" [http://127.0.0.1:5000/predict](http://127.0.0.1:5000/predict)

2️⃣ Streamlit Dashboard

Criamos um dashboard interativo com Streamlit para permitir que usuários carreguem imagens de trilhos ferroviários e recebam previsões instantâneas.

Rodando o Dashboard:

streamlit run dashboard.py

🚀 How to Use

1️⃣ Clone o Repositório

git clone [https://github.com/CesarRonai/railway-fault-detection.git](https://github.com/CesarRonai/railway-fault-detection.git)
cd railway-fault-detection

2️⃣ Instale as Dependências

pip install -r requirements.txt

3️⃣ Execute a API ou o Dashboard

API: python app.py

Dashboard: streamlit run dashboard.py

📌 Future Enhancements

Data Augmentation para melhorar a generalização do modelo.

Integração com IoT para monitoramento em tempo real dos trilhos.

Aplicativo Web/Mobile para ampliar acessibilidade.

📜 License

Este projeto está licenciado sob a MIT License.

👨‍💻 Author

Cesar Ronai

🔗 GitHub

📧 Contact: cesar.ronai\@hotmail.com

🚆 Garantindo a segurança ferroviária com IA para detecção de falhas!
