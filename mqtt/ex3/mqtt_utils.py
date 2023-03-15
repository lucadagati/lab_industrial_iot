def print_mqtt_message(topic, payload, qos):
    # Print a message header
    print("MQTT Message:")
    # Print the topic of the message
    print(f"  Topic: {topic}")
    # Print the quality of service (QoS) level of the message
    print(f"  QoS: {qos}")
    # Print the payload of the message, decoded from bytes to a string
    print(f"  Payload: {payload.decode()}")
