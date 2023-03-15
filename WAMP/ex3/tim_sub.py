import asyncio  # Import the asyncio library for asynchronous programming
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner  # Import the necessary classes from autobahn.asyncio.wamp for implementing the WebSocket Application Messaging Protocol (WAMP) in asyncio

class TimeSubscriber(ApplicationSession):  # Define a class named TimeSubscriber that inherits from ApplicationSession

    async def onJoin(self, details):  # Define an asynchronous function called onJoin that is executed when the client joins the WAMP session
        await self.subscribe(self.on_time_update, 'com.example.time')  # Subscribe to the 'com.example.time' topic on the WAMP server using the subscribe method of the session object self and the on_time_update method as the callback function

    async def on_time_update(self, time):  # Define an asynchronous function called on_time_update that takes a single argument called time
        print(f"Received: Time: {time}")  # Print a message to the console indicating that the time has been received

if __name__ == "__main__":  # Check if the script is being run directly
    runner = ApplicationRunner(url="ws://localhost:8880/ws", realm="realm1")  # Create an ApplicationRunner object to connect to the WAMP server at ws://localhost:8880/ws using the realm "realm1"
    runner.run(TimeSubscriber)  # Run the TimeSubscriber class using the ApplicationRunner object
