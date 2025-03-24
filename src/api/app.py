from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

MODELO_PATH = '../../models/modelo_ridge.pkl'

modelo_completo = joblib.load(MODELO_PATH)
model = modelo_completo['modelo']
scaler = modelo_completo['scaler']

FEATURES = [
    'area', 
    'area_per_bathroom', 
    'bathrooms', 
    'area_per_bedroom', 
    'airconditioning',
    'parking',
    'stories',
    'prefarea'
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("Requisição recebida")
        data = request.get_json()
        print("JSON recebido:", data)

        input_data = pd.DataFrame([data])
        print("DataFrame montado")

        if scaler is not None:
            print("Aplicando scaler")
            input_data[['area_per_bedroom', 'area_per_bathroom']] = scaler.transform(
                input_data[['area_per_bedroom', 'area_per_bathroom']]
            )

        print("Fazendo predição")
        prediction = model.predict(input_data[FEATURES])[0]
        print("Predição realizada com sucesso")

        return jsonify({
            "status": "sucesso",
            "modelo_usado": MODELO_PATH.split('/')[-1],
            "preco_previsto": round(prediction, 2),
            "moeda": "R$",
            "mensagem": "Preço previsto com base nas características fornecidas."
        })

    except Exception as e:
        print("Erro ocorrido:", e)
        return jsonify({
            "status": "erro",
            "mensagem": "Erro ao processar a previsão.",
            "detalhes": str(e)
        }), 500


@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "status": "ok",
        "mensagem": "API de Previsão de Imóveis está ativa!",
        "modelo_em_uso": MODELO_PATH.split('/')[-1],
        "exemplo_requisicao": {
            "area": 5000,
            "area_per_bathroom": 2500,
            "bathrooms": 2,
            "area_per_bedroom": 1666.67,
            "airconditioning": 1,
            "parking": 1,
            "stories": 2,
            "prefarea": 1
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
