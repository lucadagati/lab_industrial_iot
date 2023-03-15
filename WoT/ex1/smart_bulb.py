class SmartBulb:
    def __init__(self, status=False, brightness=100):
        self.status = status
        self.brightness = brightness

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def set_brightness(self, brightness):
        self.brightness = max(0, min(brightness, 100))

    def get_state(self):
        return {
            "status": "on" if self.status else "off",
            "brightness": self.brightness,
        }
