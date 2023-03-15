import time
import random
from paho.mqtt import client as mqtt_client

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
        client.publish(topic, f"Temperature: {temperature} °C")
        print(f"Published: {temperature} °C")
        time.sleep(5)

    client.loop_stop()

if __name__ == "__main__":
    main()
