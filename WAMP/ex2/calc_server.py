import asyncio
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

class CalculatorComponent(ApplicationSession):
    async def onJoin(self, details):
        print("Server is ready")

        # Register the basic arithmetic functions
        await self.register(self.add, 'com.example.add')
        print("Registered addition function")
        await self.register(self.subtract, 'com.example.subtract')
        print("Registered subtraction function")
        await self.register(self.multiply, 'com.example.multiply')
        print("Registered multiplication function")
        await self.register(self.divide, 'com.example.divide')
        print("Registered division function")

    def add(self, a, b):
        result = a + b
        print(f"Adding: {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        print(f"Subtracting: {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        print(f"Multiplying: {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        result = a / b
        print(f"Dividing: {a} / {b} = {result}")
        return result

if __name__ == "__main__":
    runner = ApplicationRunner(url="ws://localhost:8880/ws", realm="realm1")
    runner.run(CalculatorComponent)
