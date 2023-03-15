import time
from paho.mqtt import client as mqtt_client  # Import the MQTT client library
from mqtt_utils import print_mqtt_message  # Import the helper function for printing MQTT messages
from json_utils import decode_json_message  # Import the function for decoding JSON messages
from binary_utils import binary_representation  # Import the function for getting the binary representation of bytes

broker = "mqtt.eclipseprojects.io"  # Set the MQTT broker address
port = 1883  # Set the MQTT broker port number
topic = "demo/temperature"  # Set the topic to subscribe to


def on_connect(client, userdata, flags, rc):
    # This function is called when the client connects to the broker
    if rc == 0:
        print("Connected to MQTT broker!")
        # Subscribe to the topic
        client.subscribe(topic)
    else:
        print(f"Failed to connect, return code {rc}")


def on_message(client, userdata, msg):
    # This function is called when a new message is received
    print("Received:")
    # Print the message structure for debugging purposes
    print_mqtt_message(msg.topic, msg.payload, msg.qos)
    # Print the JSON message for debugging purposes
    print("JSON message:")
    print(decode_json_message(msg.payload))
    # Print the binary representation of the message for debugging purposes
    print("Binary representation:")
    print(binary_representation(msg.payload))


def main():
    # Create a new MQTT client instance
    client = mqtt_client.Client("subscriber")
    # Set the callback functions for when the client connects to the broker and when a new message is received
    client.on_connect = on_connect
    client.on_message = on_message
    # Connect the client to the broker
    client.connect(broker, port)

    # Start the MQTT client loop, which will continue running forever
    client.loop_forever()


if __name__ == "__main__":
    # Call the main function if this file is run as the main program
    main()
