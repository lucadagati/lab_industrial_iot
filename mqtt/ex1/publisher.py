import time
import random
from paho.mqtt import client as mqtt_client

broker = "mqtt.eclipseprojects.io"  # MQTT broker address
port = 1883  # MQTT broker port
topic = "demo/temperature"  # MQTT topic to publish to

def on_connect(client, userdata, flags, rc):
    """
    Callback function called when the client is connected to the broker.
    If the connection is successful, it subscribes to the topic.
    """
    if rc == 0:
        print("Connected to MQTT broker!")
    else:
        print(f"Failed to connect, return code {rc}")

def main():
    """
    Main function that publishes temperature values to the MQTT broker.
    """
    client = mqtt_client.Client("publisher")  # Create a client instance
    client.on_connect = on_connect  # Set the callback function for connection
    client.connect(broker, port)  # Connect to the broker

    client.loop_start()  # Start the MQTT client loop

    while True:
        temperature = round(random.uniform(20, 30), 2)  # Generate a random temperature value
        client.publish(topic, f"Temperature: {temperature} °C")  # Publish the temperature value to the topic
        print(f"Published: {temperature} °C")  # Print the published temperature value
        time.sleep(5)  # Wait for 5 seconds before publishing the next temperature value

    client.loop_stop()  # Stop the MQTT client loop

if __name__ == "__main__":
    main()
