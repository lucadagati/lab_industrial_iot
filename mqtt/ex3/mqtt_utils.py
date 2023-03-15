def print_mqtt_message(topic, payload, qos):
    print("MQTT Message:")
    print(f"  Topic: {topic}")
    print(f"  QoS: {qos}")
    print(f"  Payload: {payload.decode()}")
