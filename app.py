from flask import Flask, jsonify

app = Flask(__name__)

# Mock weather data
WEATHER_DATA = {
    "london": {"city": "London", "temperature": 15, "unit": "C", "condition": "Cloudy"},
    "new york": {"city": "New York", "temperature": 22, "unit": "C", "condition": "Sunny"},
    "tokyo": {"city": "Tokyo", "temperature": 28, "unit": "C", "condition": "Humid"},
    "sydney": {"city": "Sydney", "temperature": 18, "unit": "C", "condition": "Partly Cloudy"},
}


@app.route("/")
def index():
    return jsonify({
        "message": "Welcome to the Weather API",
        "endpoints": {
            "health": "/health",
            "weather": "/weather/<city>",
            "cities": "/cities"
        }
    })


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/cities")
def cities():
    return jsonify({"cities": list(WEATHER_DATA.keys())})


@app.route("/weather/<city>")
def get_weather(city):
    city_lower = city.lower()
    if city_lower in WEATHER_DATA:
        return jsonify(WEATHER_DATA[city_lower])
    return jsonify({"error": f"City '{city}' not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
