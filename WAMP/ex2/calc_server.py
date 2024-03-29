import asyncio  # Import the asyncio library for asynchronous programming
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner  # Import the necessary classes from autobahn.asyncio.wamp for implementing the WebSocket Application Messaging Protocol (WAMP) in asyncio

class CalculatorComponent(ApplicationSession):  # Define a class named CalculatorComponent that inherits from ApplicationSession

    async def onJoin(self, details):  # Define an asynchronous function called onJoin that is executed when the client joins the WAMP session
        print("Server is ready")  # Print a message to the console indicating that the server is ready

        # Register the basic arithmetic functions
        await self.register(self.add, 'com.example.add')  # Register the add function with the remote procedure 'com.example.add' on the WAMP server using the register method of the session object self
        print("Registered addition function")  # Print a message to the console indicating that the addition function has been registered
        await self.register(self.subtract, 'com.example.subtract')  # Register the subtract function with the remote procedure 'com.example.subtract' on the WAMP server using the register method of the session object self
        print("Registered subtraction function")  # Print a message to the console indicating that the subtraction function has been registered
        await self.register(self.multiply, 'com.example.multiply')  # Register the multiply function with the remote procedure 'com.example.multiply' on the WAMP server using the register method of the session object self
        print("Registered multiplication function")  # Print a message to the console indicating that the multiplication function has been registered
        await self.register(self.divide, 'com.example.divide')  # Register the divide function with the remote procedure 'com.example.divide' on the WAMP server using the register method of the session object self
        print("Registered division function")  # Print a message to the console indicating that the division function has been registered

    def add(self, a, b):  # Define a function called add that takes two arguments a and b
        result = a + b  # Add the values of a and b and assign the result to the variable result
        print(f"Adding: {a} + {b} = {result}")  # Print a message to the console indicating that the addition operation is being performed and showing the result
        return result  # Return the result of the addition operation

    def subtract(self, a, b):  # Define a function called subtract that takes two arguments a and b
        result = a - b  # Subtract the value of b from a and assign the result to the variable result
        print(f"Subtracting: {a} - {b} = {result}")  # Print a message to the console indicating that the subtraction operation is being performed and showing the result
        return result  # Return the result of the subtraction operation

    def multiply(self, a, b):  # Define a function called multiply that takes two arguments a and b
        result = a * b  # Multiply the values of a and b and assign the result to the variable result
        print(f"Multiplying: {a} * {b} = {result}")  # Print a message to the console indicating that the multiplication operation is being performed and showing the result
        return result  # Return the result of the multiplication operation
    def divide(self, a, b):  # Define a function called divide that takes two arguments a and b
    result = a / b  # Divide the value of a by b and assign the result to the variable result
    print(f"Dividing: {a} / {b} = {result}")  # Print a message to the console indicating that the division operation is being performed and showing the result
    return result  # Return the result of the division operation

if __name__ == "__main__":  # Check if the script is being run directly
    runner = ApplicationRunner(url="ws://localhost:8880/ws", realm="realm1")  # Create an ApplicationRunner object to connect to the WAMP server at ws://localhost:8880/ws using the realm "realm1"
    runner.run(CalculatorComponent)  # Run the CalculatorComponent class using the ApplicationRunner object
