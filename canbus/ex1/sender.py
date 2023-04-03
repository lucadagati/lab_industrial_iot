import can
import time

def send_can_messages(channel, message_id, data):
    bus = can.interface.Bus(channel=channel, bustype='socketcan')
    message = can.Message(arbitration_id=message_id, data=data, is_extended_id=False)

    while True:
        try:
            bus.send(message)
            print(f"Message sent: {message}")
            time.sleep(1)
        except can.CanError:
            print("Error sending message")

if __name__ == "__main__":
    channel = "vcan0"  # Cambia questo con il tuo canale CAN
    message_id = 0x123
    data = [0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88]
    send_can_messages(channel, message_id, data)
