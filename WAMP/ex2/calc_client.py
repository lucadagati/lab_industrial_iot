import asyncio  # Import the asyncio library for asynchronous programming
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner  # Import the necessary classes from autobahn.asyncio.wamp for implementing the WebSocket Application Messaging Protocol (WAMP) in asyncio

class CalculatorClient(ApplicationSession):  # Define a class named CalculatorClient that inherits from ApplicationSession

    async def onJoin(self, details):  # Define an asynchronous function called onJoin that is executed when the client joins the WAMP session
        print("Client is ready")  # Print a message to the console indicating that the client is ready

        # Call the remote arithmetic functions
        a, b = 10, 5  # Assign the values 10 and 5 to the variables a and b, respectively

        result_add = await self.call('com.example.add', a, b)  # Call the remote procedure 'com.example.add' on the WAMP server with the arguments a and b using the call method of the session object self, and assign the result to the variable result_add
        print(f"{a} + {b} = {result_add}")  # Print a message to the console showing the addition result

        result_subtract = await self.call('com.example.subtract', a, b)  # Call the remote procedure 'com.example.subtract' on the WAMP server with the arguments a and b using the call method of the session object self, and assign the result to the variable result_subtract
        print(f"{a} - {b} = {result_subtract}")  # Print a message to the console showing the subtraction result

        result_multiply = await self.call('com.example.multiply', a, b)  # Call the remote procedure 'com.example.multiply' on the WAMP server with the arguments a and b using the call method of the session object self, and assign the result to the variable result_multiply
        print(f"{a} * {b} = {result_multiply}")  # Print a message to the console showing the multiplication result

        result_divide = await self.call('com.example.divide', a, b)  # Call the remote procedure 'com.example.divide' on the WAMP server with the arguments a and b using the call method of the session object self, and assign the result to the variable result_divide
        print(f"{a} / {b} = {result_divide}")  # Print a message to the console showing the division result

if __name__ == "__main__":  # Check if the script is being run directly
    runner = ApplicationRunner(url="ws://localhost:8880/ws", realm="realm1")  # Create an ApplicationRunner object to connect to the WAMP server at ws://localhost:8880/ws using the realm "realm1"
    runner.run(CalculatorClient)  # Run the CalculatorClient class using the ApplicationRunner object
