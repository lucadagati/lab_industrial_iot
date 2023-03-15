from flask import Flask, jsonify  # Import the Flask class from the flask module, and the jsonify function

app = Flask(__name__)  # Create a Flask object named app
weather_data = {  # Create a dictionary containing simulated weather data
    "temperature": 23.5,  # The current temperature in Celsius
    "humidity": 40.0  # The current relative humidity as a percentage
}

@app.route('/weather', methods=['GET'])  # Define a route decorator for the "/weather" endpoint with the GET method
def get_weather_data():  # Define a function called get_weather_data that handles GET requests to the "/weather" endpoint
    return jsonify(weather_data)  # Return a JSON response containing the weather data as a dictionary

if __name__ == '__main__':  # Check if the script is being run directly
    app.run(host='0.0.0.0', port=5000)  # Start the Flask web server on all network interfaces at port 5000
