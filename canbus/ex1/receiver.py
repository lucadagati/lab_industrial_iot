import can

def receive_can_messages(channel):
    bus = can.interface.Bus(channel=channel, bustype='socketcan')

    while True:
        message = bus.recv()
        print(f"Message received: {message}")

if __name__ == "__main__":
    channel = "vcan0"  # Cambia questo con il tuo canale CAN
    receive_can_messages(channel)
