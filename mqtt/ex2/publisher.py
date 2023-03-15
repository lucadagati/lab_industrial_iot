import time
import random
from paho.mqtt import client as mqtt_client  # Import the MQTT client library
from paho.mqtt.client import MQTTMessage  # Import the MQTTMessage class
from mqtt_utils import print_mqtt_message  # Import the helper function for printing MQTT messages


broker = "mqtt.eclipseprojects.io"  # Set the MQTT broker address
port = 1883  # Set the MQTT broker port number
topic = "demo/temperature"  # Set the topic to publish to


def on_connect(client, userdata, flags, rc):
    # This function is called when the client connects to the broker
    if rc == 0:
        print("Connected to MQTT broker!")
    else:
        print(f"Failed to connect, return code {rc}")


def main():
    # Create a new MQTT client instance
    client = mqtt_client.Client("publisher")
    # Set the callback function for when the client connects to the broker
    client.on_connect = on_connect
    # Connect the client to the broker
    client.connect(broker, port)

    # Start the MQTT client loop in a new thread
    client.loop_start()

    while True:
        # Generate a random temperature between 20 and 30 degrees Celsius
        temperature = round(random.uniform(20, 30), 2)
        # Format the temperature as a string with a degree symbol
        message_str = f"Temperature: {temperature} °C"
        
        # Publish the message to the MQTT broker
        client.publish(topic, message_str)
        print("Published:")
        # Print the message structure for debugging purposes
        print_mqtt_message(topic, message_str.encode(), 0)

        # Wait for 5 seconds before publishing the next message
        time.sleep(5)

    # Stop the MQTT client loop when the program exits the loop
    client.loop_stop()


if __name__ == "__main__":
    # Call the main function if this file is run as the main program
    main()
