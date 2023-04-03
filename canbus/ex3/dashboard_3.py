import can
import time
import math
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QProgressBar, QLabel
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtCore import Qt, QTimer

class Tachometer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the tachometer
        self.tachometer = QProgressBar(self)
        self.tachometer.setOrientation(Qt.Vertical)
        self.tachometer.setRange(0, 170)
        self.tachometer.setValue(0)

        # Set up the speed label
        self.speed_label = QLabel('Speed: 0 km/h', self)
        self.speed_label.setAlignment(Qt.AlignCenter)

        # Set up the layout
        grid = QGridLayout()
        grid.addWidget(self.tachometer, 0, 0)
        grid.addWidget(self.speed_label, 1, 0)
        self.setLayout(grid)

        # Initialize the CAN bus
        self.bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

        # Start the timer to read CAN messages
        self.timer = QTimer()
        self.timer.timeout.connect(self.readCAN)
        self.timer.start(10) # Read every 10ms

    def readCAN(self):
        # Read the most recent CAN message and update the tachometer and speed label
        message = self.bus.recv()
        if message.arbitration_id == 0x123:
            speed = message.data[0]
            self.tachometer.setValue(speed)
            self.speed_label.setText(f'Speed: {speed} km/h')

    def closeEvent(self, event):
        # Stop the timer and close the CAN bus on exit
        self.timer.stop()
        self.bus.shutdown()

class TachometerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.tachometer = Tachometer()
        self.initUI()

    def initUI(self):
        # Set up the layout
        grid = QGridLayout()
        grid.addWidget(self.tachometer, 0, 0)
        self.setLayout(grid)

        # Set up the window
        self.setWindowTitle('Tachometer Widget')
        self.setGeometry(100, 100, 200, 400)
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    window = TachometerWidget()
    app.exec_()
