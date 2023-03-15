def binary_representation(data):
    return ' '.join(format(byte, '08b') for byte in data)
