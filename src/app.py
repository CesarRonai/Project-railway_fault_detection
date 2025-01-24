from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Carregar o modelo treinado
import h5py
with h5py.File("modelo_vgg16_trilhos.h5", "r") as f:
    model = tf.keras.models.load_model(f)
  # Substituir pelo caminho correto

# Definir as classes do modelo
CLASSES = ["Non Defective", "Defective"]

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "Nenhuma imagem enviada"}), 400

    file = request.files["file"]
    img = Image.open(file).resize((224, 224))
    
    # Converter imagem para array
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)
    
    # Fazer previsão
    prediction = model.predict(img_array)[0][0]
    result = CLASSES[1] if prediction > 0.5 else CLASSES[0]

    return jsonify({"prediction": result, "confidence": float(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
