import time
from paho.mqtt import client as mqtt_client

broker = "mqtt.eclipseprojects.io"  # Set the broker address
port = 1883  # Set the broker port
topic = "demo/temperature"  # Set the topic to subscribe to

def on_connect(client, userdata, flags, rc):
    # Define a callback function to handle connection events
    if rc == 0:
        print("Connected to MQTT broker!")
        client.subscribe(topic)  # Subscribe to the topic
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    # Define a callback function to handle incoming messages
    print(f"Received: {msg.payload.decode()}")

def main():
    client = mqtt_client.Client("subscriber")  # Create a new MQTT client instance
    client.on_connect = on_connect  # Set the on_connect callback function
    client.on_message = on_message  # Set the on_message callback function
    client.connect(broker, port)  # Connect to the MQTT broker

    client.loop_forever()  # Start the MQTT client loop

if __name__ == "__main__":
    main()  # Call the main function to start the MQTT client
