import asyncio
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from datetime import datetime

class TimePublisher(ApplicationSession):
    async def onJoin(self, details):
        while True:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.publish('com.example.time', current_time)
            print(f"Published: Time: {current_time}")
            await asyncio.sleep(1)

if __name__ == "__main__":
    runner = ApplicationRunner(url="ws://localhost:8880/ws", realm="realm1")
    runner.run(TimePublisher)
