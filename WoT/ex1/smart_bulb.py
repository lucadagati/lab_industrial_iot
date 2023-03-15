class SmartBulb:  # Define a class named SmartBulb

    def __init__(self, status=False, brightness=100):  # Define a constructor method that takes two optional arguments: status (default value is False) and brightness (default value is 100)
        self.status = status  # Assign the value of status to the instance variable self.status
        self.brightness = brightness  # Assign the value of brightness to the instance variable self.brightness

    def turn_on(self):  # Define a method called turn_on that takes no arguments
        self.status = True  # Set the value of self.status to True

    def turn_off(self):  # Define a method called turn_off that takes no arguments
        self.status = False  # Set the value of self.status to False

    def set_brightness(self, brightness):  # Define a method called set_brightness that takes a single argument called brightness
        self.brightness = max(0, min(brightness, 100))  # Set the value of self.brightness to brightness, ensuring that it is between 0 and 100

    def get_state(self):  # Define a method called get_state that takes no arguments
        return {  # Return a dictionary containing the current status and brightness of the bulb
            "status": "on" if self.status else "off",  # If self.status is True, set the value of "status" to "on", otherwise set it to "off"
            "brightness": self.brightness,  # Set the value of "brightness" to self.brightness
        }
