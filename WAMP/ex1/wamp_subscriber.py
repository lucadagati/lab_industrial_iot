import asyncio
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

class SubscriberComponent(ApplicationSession):
    async def onJoin(self, details):
        def on_temperature_change(temperature):
            print(f"Received: Temperature: {temperature} °C")

        await self.subscribe(on_temperature_change, 'com.example.temperature')

if __name__ == "__main__":
    runner = ApplicationRunner(url="ws://localhost:8880/ws", realm="realm1")
    runner.run(SubscriberComponent)
