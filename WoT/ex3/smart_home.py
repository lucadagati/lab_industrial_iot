from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

devices = {
    "bulb": {
        "status": "off",
        "brightness": 100
    },
    "thermostat": {
        "temperature": 22,
        "mode": "cool"
    },
    "door_lock": {
        "status": "locked"
    }
}

class DeviceController(Resource):
    def get(self, device_name):
        if device_name in devices:
            return devices[device_name]
        else:
            return {"error": "Device not found"}, 404

    def put(self, device_name):
        if device_name in devices:
            devices[device_name].update(request.get_json())
            return devices[device_name]
        else:
            return {"error": "Device not found"}, 404

api.add_resource(DeviceController, '/devices/<string:device_name>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
