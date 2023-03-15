from flask import Flask, jsonify, request
from smart_bulb import SmartBulb

app = Flask(__name__)
bulb = SmartBulb()

@app.route("/bulb", methods=["GET"])
def get_bulb_state():
    return jsonify(bulb.get_state())

@app.route("/bulb", methods=["PUT"])
def update_bulb_state():
    data = request.json
    if "status" in data:
        if data["status"] == "on":
            bulb.turn_on()
        elif data["status"] == "off":
            bulb.turn_off()

    if "brightness" in data:
        bulb.set_brightness(data["brightness"])

    return jsonify(bulb.get_state())

if __name__ == "__main__":
    app.run()
