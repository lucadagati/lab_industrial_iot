import asyncio
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

class TimeSubscriber(ApplicationSession):
    async def onJoin(self, details):
        await self.subscribe(self.on_time_update, 'com.example.time')

    async def on_time_update(self, time):
        print(f"Received: Time: {time}")

if __name__ == "__main__":
    runner = ApplicationRunner(url="ws://localhost:8880/ws", realm="realm1")
    runner.run(TimeSubscriber)
