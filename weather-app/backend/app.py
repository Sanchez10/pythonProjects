from flask import Flask, request, jsonify
import requests
import os
from flask_cors import CORS  # Importa o Flask-CORS

app = Flask(__name__)
CORS(app)  # Ativa o CORS para todas as rotas

@app.route("/api/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Parâmetro 'city' é obrigatório"}), 400

    api_key = os.getenv("OPEN_WEATHER_API_KEY", "02bedfc68309e6d0563c51fbfa750e8e")
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"

    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        data = response.json()
        return jsonify({
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        })
    except requests.exceptions.RequestException:
        return jsonify({"error": "Erro ao acessar a API"}), 500

if __name__ == "__main__":
    app.run(debug=True)
