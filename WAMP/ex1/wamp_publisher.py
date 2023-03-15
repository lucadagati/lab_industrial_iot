import asyncio
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from wamp_utils import random_temperature

class PublisherComponent(ApplicationSession):
    async def onJoin(self, details):
        while True:
            temperature = random_temperature()
            self.publish('com.example.temperature', temperature)  # Removed 'await'
            print(f"Published: Temperature: {temperature} °C")
            await asyncio.sleep(5)


if __name__ == "__main__":
    runner = ApplicationRunner(url="ws://localhost:8880/ws", realm="realm1")
    runner.run(PublisherComponent)
