import time
from paho.mqtt import client as mqtt_client
from mqtt_utils import print_mqtt_message  # Import the helper function

broker = "mqtt.eclipseprojects.io"
port = 1883
topic = "demo/temperature"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker!")
        client.subscribe(topic)
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    print("Received:")
    print_mqtt_message(msg.topic, msg.payload, msg.qos)  # Print the message structure


def main():
    client = mqtt_client.Client("subscriber")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)

    client.loop_forever()

if __name__ == "__main__":
    main()
