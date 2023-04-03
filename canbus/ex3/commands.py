import can
import time
import random
import getch

bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

# Continuously send CAN messages with ID 0x123 and varying speed values
speed = 0
while True:
    char = getch.getch()
    if char == 'a':
        speed += 1
    elif char == 'z':
        speed -= 1
    elif char not in ['a', 'z']:
        speed += random.randint(-5, 5)

    if speed > 170:
        speed = 170
    elif speed < 0:
        speed = 0
    message = can.Message(arbitration_id=0x123, data=[speed])
    bus.send(message)
    time.sleep(0.01)  # Wait 10 ms before sending the next message
