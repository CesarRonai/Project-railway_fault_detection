import streamlit as st
import requests
from PIL import Image
import io

# Configuração do título
st.title("🚆 Detecção de Falhas em Trilhos Ferroviários")

# Upload de imagem
uploaded_file = st.file_uploader("Envie uma imagem de trilho para análise", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Imagem enviada", use_column_width=True)

    # Converter imagem para bytes
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="JPEG")
    img_bytes = img_bytes.getvalue()

    # Enviar imagem para a API Flask
    response = requests.post("http://127.0.0.1:5000/predict", files={"file": img_bytes})

    # Exibir resultado
    if response.status_code == 200:
        prediction = response.json()
        st.write(f"**Resultado:** {prediction['prediction']}")
        st.write(f"**Confiança:** {prediction['confidence']:.2f}")
    else:
        st.write("Erro ao processar a imagem.")
