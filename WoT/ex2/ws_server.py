from flask import Flask, jsonify

app = Flask(__name__)

# Simulated weather data
weather_data = {
    "temperature": 23.5,
    "humidity": 40.0
}

@app.route('/weather', methods=['GET'])
def get_weather_data():
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
