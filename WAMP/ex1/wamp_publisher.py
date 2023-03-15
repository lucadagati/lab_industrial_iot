import asyncio  # Import the asyncio library for asynchronous programming
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner  # Import the necessary classes from autobahn.asyncio.wamp for implementing the WebSocket Application Messaging Protocol (WAMP) in asyncio
from wamp_utils import random_temperature  # Import the random_temperature function from wamp_utils for generating random temperature values

class PublisherComponent(ApplicationSession):  # Define a class named PublisherComponent that inherits from ApplicationSession

    async def onJoin(self, details):  # Define an asynchronous function called onJoin that is executed when the client joins the WAMP session
        while True:  # Enter an infinite loop
            temperature = random_temperature()  # Generate a random temperature value using the random_temperature function
            self.publish('com.example.temperature', temperature)  # Publish the temperature value to the WAMP server using the publish method of the session object self
            print(f"Published: Temperature: {temperature} °C")  # Print a message to the console indicating that the temperature value has been published
            await asyncio.sleep(5)  # Wait for 5 seconds before repeating the loop

if __name__ == "__main__":  # Check if the script is being run directly
    runner = ApplicationRunner(url="ws://localhost:8880/ws", realm="realm1")  # Create an ApplicationRunner object to connect to the WAMP server at ws://localhost:8880/ws using the realm "realm1"
    runner.run(PublisherComponent)  # Run the PublisherComponent class using the ApplicationRunner object
