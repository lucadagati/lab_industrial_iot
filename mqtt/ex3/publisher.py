import time
import random
from paho.mqtt import client as mqtt_client
from mqtt_utils import print_mqtt_message
from json_utils import encode_json_message
from binary_utils import binary_representation

broker = "mqtt.eclipseprojects.io"
port = 1883
topic = "demo/temperature"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker!")
    else:
        print(f"Failed to connect, return code {rc}")

def main():
    client = mqtt_client.Client("publisher")
    client.on_connect = on_connect
    client.connect(broker, port)

    client.loop_start()

    while True:
        temperature = round(random.uniform(20, 30), 2)
        message_bytes = encode_json_message(temperature)  # Encode the JSON message
        
        client.publish(topic, message_bytes)  # Publish the message
        print("Published:")
        print_mqtt_message(topic, message_bytes, 0)  # Print the message structure
        print("Binary representation:")
        print(binary_representation(message_bytes))  # Print the binary representation

        time.sleep(5)

    client.loop_stop()

    client.loop_stop()
if __name__ == "__main__":
    main()

