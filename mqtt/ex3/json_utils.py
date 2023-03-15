import json
import time

def encode_json_message(temperature):
    # Create a dictionary representing the message
    message = {
        'temperature': temperature,
        'timestamp': time.time(),  # Add the current timestamp to the message
    }
    # Convert the dictionary to a JSON-encoded string and encode it as bytes using UTF-8
    encoded_message = json.dumps(message).encode('utf-8')
    # Return the resulting bytes object
    return encoded_message

def decode_json_message(encoded_message):
    # Decode the bytes object as a UTF-8 string and parse it as a JSON object
    decoded_message = json.loads(encoded_message.decode('utf-8'))
    # Return the resulting dictionary
    return decoded_message
