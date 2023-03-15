import time
import random
from paho.mqtt import client as mqtt_client
from paho.mqtt.client import MQTTMessage  # Import the MQTTMessage class
from mqtt_utils import print_mqtt_message  # Import the helper function


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
        message_str = f"Temperature: {temperature} °C"
        
        client.publish(topic, message_str)  # Publish the message
        print("Published:")
        print_mqtt_message(topic, message_str.encode(), 0)  # Print the message structure

        time.sleep(5)

    client.loop_stop()
if __name__ == "__main__":
    main()

