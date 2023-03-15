from flask import Flask, jsonify, request  # Import the Flask class from the flask module, and the jsonify and request functions
from smart_bulb import SmartBulb  # Import the SmartBulb class from the smart_bulb module

app = Flask(__name__)  # Create a Flask object named app
bulb = SmartBulb()  # Create an instance of the SmartBulb class named bulb

@app.route("/bulb", methods=["GET"])  # Define a route decorator for the "/bulb" endpoint with the GET method
def get_bulb_state():  # Define a function called get_bulb_state that handles GET requests to the "/bulb" endpoint
    return jsonify(bulb.get_state())  # Return a JSON response containing the current state of the bulb as a dictionary

@app.route("/bulb", methods=["PUT"])  # Define a route decorator for the "/bulb" endpoint with the PUT method
def update_bulb_state():  # Define a function called update_bulb_state that handles PUT requests to the "/bulb" endpoint
    data = request.json  # Get the JSON data from the request body

    if "status" in data:  # Check if the "status" key is in the JSON data
        if data["status"] == "on":  # Check if the value of "status" is "on"
            bulb.turn_on()  # Turn on the bulb
        elif data["status"] == "off":  # Check if the value of "status" is "off"
            bulb.turn_off()  # Turn off the bulb

    if "brightness" in data:  # Check if the "brightness" key is in the JSON data
        bulb.set_brightness(data["brightness"])  # Set the brightness of the bulb to the value of "brightness" in the JSON data

    return jsonify(bulb.get_state())  # Return a JSON response containing the updated state of the bulb as a dictionary

if __name__ == "__main__":  # Check if the script is being run directly
    app.run()  # Start the Flask web server
