def binary_representation(data):
    # Convert each byte in the input data to its binary representation and join them with spaces
    binary_str = ' '.join(format(byte, '08b') for byte in data)
    # Return the resulting string
    return binary_str
