import asyncio
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

class CalculatorClient(ApplicationSession):
    async def onJoin(self, details):
        print("Client is ready")

        # Call the remote arithmetic functions
        a, b = 10, 5

        result_add = await self.call('com.example.add', a, b)
        print(f"{a} + {b} = {result_add}")

        result_subtract = await self.call('com.example.subtract', a, b)
        print(f"{a} - {b} = {result_subtract}")

        result_multiply = await self.call('com.example.multiply', a, b)
        print(f"{a} * {b} = {result_multiply}")

        result_divide = await self.call('com.example.divide', a, b)
        print(f"{a} / {b} = {result_divide}")

if __name__ == "__main__":
    runner = ApplicationRunner(url="ws://localhost:8880/ws", realm="realm1")
    runner.run(CalculatorClient)
