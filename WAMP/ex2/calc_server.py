import asyncio  # Import the asyncio library for asynchronous programming
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner  # Import the necessary classes from autobahn.asyncio.wamp for implementing the WebSocket Application Messaging Protocol (WAMP) in asyncio

class CalculatorComponent(ApplicationSession):  # Define a class named CalculatorComponent that inherits from ApplicationSession

    async def onJoin(self, details):  # Define an asynchronous function called onJoin that is executed when the client joins the WAMP session
        print("Server is ready")  # Print a message to the console indicating that the server is ready

        # Register the basic arithmetic functions
        await self.register(self.add, 'com.example.add')  # Register the add method of the CalculatorComponent class as a remote procedure with the name 'com.example.add' using the register method of the session object self
        print("Registered addition function")  # Print a message to the console indicating that the add method has been registered
        await self.register(self.subtract, 'com.example.subtract')  # Register the subtract method of the CalculatorComponent class as a remote procedure with the name 'com.example.subtract' using the register method of the session object self
        print("Registered subtraction function")  # Print a message to the console indicating that the subtract method has been registered
        await self.register(self.multiply, 'com.example.multiply')  # Register the multiply method of the CalculatorComponent class as a remote procedure with the name 'com.example.multiply' using the register method of the session object self
        print("Registered multiplication function")  # Print a message to the console indicating that the multiply method has been registered
        await self.register(self.divide, 'com.example.divide')  # Register the divide method of the CalculatorComponent class as a remote procedure with the name 'com.example.divide' using the register method of the session object self
        print("Registered division function")  # Print a message to the console indicating that the divide method has been registered

    def add(self, a, b):  # Define a method called add that takes two arguments, a and b
        result = a + b  # Add the values of a and b and assign the result to the variable result
        print(f"Adding: {a} + {b} = {result}")  # Print a message to the console showing the addition operation and its result
        return result  # Return the result of the addition operation

    def subtract(self, a, b):  # Define a method called subtract that takes two arguments, a and b
        result = a - b  # Subtract the value of b from the value of a and assign the result to the variable result
        print(f"Subtracting: {a} - {b} = {result}")  # Print a message to the console showing the subtraction operation and its result
        return result  # Return the result of the subtraction operation

    def multiply(self, a, b):  # Define a method called multiply that takes two arguments, a and b
        result = a * b  # Multiply the values of a and b and assign the result to the variable result
        print(f"Multiplying: {a} * {b} = {result}")  # Print a message to the console showing the multiplication operation and its result
        return result  # Return the result of the multiplication operation

    def divide(self, a, b):  # Define a method called divide that takes two arguments, a and b
        result = a / b  # Divide the value of a by the value of b and assign the result to the variable result
