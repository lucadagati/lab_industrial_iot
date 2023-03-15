import asyncio
import random
from aiocoap import resource, Context, Message, Code

class TemperatureResource(resource.ObservableResource):
    def __init__(self):
        super().__init__()

        self.temperature = 20

    async def update_temperature(self):
        while True:
            self.temperature += random.uniform(-0.5, 0.5)
            self.updated_state()
            await asyncio.sleep(5)

    async def render_get(self, request):
        response = Message(code=Code.CONTENT)
        response.payload = f"Temperature: {self.temperature:.2f} °C".encode('utf-8')
        return response

async def main():
    root = resource.Site()
    temperature_resource = TemperatureResource()
    root.add_resource(('temperature',), temperature_resource)

    context = await Context.create_server_context(root, bind=('127.0.0.1', 5683))
    print("CoAP server started on 127.0.0.1:5683")

    asyncio.create_task(temperature_resource.update_temperature())
    await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
