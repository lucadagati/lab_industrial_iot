import asyncio  # Import the asyncio library for asynchronous programming
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner  # Import the necessary classes from autobahn.asyncio.wamp for implementing the WebSocket Application Messaging Protocol (WAMP) in asyncio

class SubscriberComponent(ApplicationSession):  # Define a class named SubscriberComponent that inherits from ApplicationSession

    async def onJoin(self, details):  # Define an asynchronous function called onJoin that is executed when the client joins the WAMP session
        def on_temperature_change(temperature):  # Define a function called on_temperature_change that takes a temperature value as input
            print(f"Received: Temperature: {temperature} °C")  # Print a message to the console indicating that a temperature value has been received

        await self.subscribe(on_temperature_change, 'com.example.temperature')  # Subscribe to the 'com.example.temperature' topic using the subscribe method of the session object self and the on_temperature_change function as the callback function

if __name__ == "__main__":  # Check if the script is being run directly
    runner = ApplicationRunner(url="ws://localhost:8880/ws", realm="realm1")  # Create an ApplicationRunner object to connect to the WAMP server at ws://localhost:8880/ws using the realm "realm1"
    runner.run(SubscriberComponent)  # Run the SubscriberComponent class using the ApplicationRunner object
