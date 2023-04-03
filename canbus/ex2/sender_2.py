import can
import time

def input_can_parameters():
    channel = input("Enter the CAN channel (e.g., vcan0): ")
    message_id = int(input("Enter the message ID (e.g., 0x123): "), 16)
    message_string = input("Enter the message string to send: ")
    return channel, message_id, message_string

def send_custom_can_messages(channel, message_id, message_string):
    bus = can.interface.Bus(channel=channel, bustype='socketcan')
    data = bytearray(message_string, 'utf-8')
    
    if len(data) > 8:
        print("Warning: CAN messages are limited to 8 bytes. Truncating the message.")
        data = data[:8]

    message = can.Message(arbitration_id=message_id, data=data, is_extended_id=False)

    while True:
        try:
            bus.send(message)
            print(f"Message sent: {message}")
            time.sleep(1)
        except can.CanError:
            print("Error sending message")

if __name__ == "__main__":
    channel, message_id, message_string = input_can_parameters()
    send_custom_can_messages(channel, message_id, message_string)
