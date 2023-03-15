import asyncio  # Import the asyncio library for asynchronous programming
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner  # Import the necessary classes from autobahn.asyncio.wamp for implementing the WebSocket Application Messaging Protocol (WAMP) in asyncio
from datetime import datetime  # Import the datetime module for working with dates and times

class TimePublisher(ApplicationSession):  # Define a class named TimePublisher that inherits from ApplicationSession

    async def onJoin(self, details):  # Define an asynchronous function called onJoin that is executed when the client joins the WAMP session
        while True:  # Create an infinite loop
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get the current date and time in the format 'YYYY-MM-DD HH:MM:SS' using the strftime method of the datetime object returned by the now function of the datetime module, and assign it to the variable current_time
            self.publish('com.example.time', current_time)  # Publish the current time to the 'com.example.time' topic on the WAMP server using the publish method of the session object self
            print(f"Published: Time: {current_time}")  # Print a message to the console indicating that the time has been published
            await asyncio.sleep(1)  # Pause the loop for 1 second before continuing

if __name__ == "__main__":  # Check if the script is being run directly
    runner = ApplicationRunner(url="ws://localhost:8880/ws", realm="realm1")  # Create an ApplicationRunner object to connect to the WAMP server at ws://localhost:8880/ws using the realm "realm1"
    runner.run(TimePublisher)  # Run the TimePublisher class using the ApplicationRunner object
