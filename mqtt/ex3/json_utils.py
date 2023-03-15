import json
import time

def encode_json_message(temperature):
    message = {
        'temperature': temperature,
        'timestamp': time.time(),
    }
    return json.dumps(message).encode('utf-8')

def decode_json_message(encoded_message):
    return json.loads(encoded_message.decode('utf-8'))
