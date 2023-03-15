from flask import Flask, request  # Import the Flask class from the flask module, and the request function
from flask_restful import Resource, Api  # Import the Resource and Api classes from the flask_restful module

app = Flask(__name__)  # Create a Flask object named app
api = Api(app)  # Create an Api object using the Flask app

devices = {  # Define a dictionary containing information about different devices
    "bulb": {
        "status": "off",  # The current status of the bulb (on/off)
        "brightness": 100  # The current brightness of the bulb as a percentage
    },
    "thermostat": {
        "temperature": 22,  # The current temperature setpoint in Celsius
        "mode": "cool"  # The current operating mode (cool/heat/off)
    },
    "door_lock": {
        "status": "locked"  # The current status of the door lock (locked/unlocked)
    }
}

class DeviceController(Resource):  # Define a class called DeviceController that inherits from the Resource class

    def get(self, device_name):  # Define a method called get that handles GET requests
        if device_name in devices:  # Check if the requested device is in the dictionary
            return devices[device_name]  # If so, return its information as a dictionary
        else:
            return {"error": "Device not found"}, 404  # Otherwise, return an error message and a 404 status code

    def put(self, device_name):  # Define a method called put that handles PUT requests
        if device_name in devices:  # Check if the requested device is in the dictionary
            devices[device_name].update(request.get_json())  # Update the device information with the data from the request body
            return devices[device_name]  # Return the updated device information as a dictionary
        else:
            return {"error": "Device not found"}, 404  # Otherwise, return an error message and a 404 status code

api.add_resource(DeviceController, '/devices/<string:device_name>')  # Add the DeviceController class to the API, with the endpoint /devices/<device_name>

if __name__ == '__main__':  # Check if the script is being run directly
    app.run(host='0.0.0.0', port=5000)  # Start the Flask web server on all network interfaces at port 5000
