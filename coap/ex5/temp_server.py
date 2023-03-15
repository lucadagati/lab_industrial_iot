import asyncio
import random
from aiocoap import resource, Context, Message, Code

class TemperatureResource(resource.ObservableResource):
    def __init__(self):
        super().__init__()

        # Set the initial temperature to 20 °C
        self.temperature = 20

    async def update_temperature(self):
        # Loop forever, updating the temperature every 5 seconds
        while True:
            # Update the temperature by a random amount
            self.temperature += random.uniform(-0.5, 0.5)

            # Notify observers that the resource state has been updated
            self.updated_state()

            # Wait for 5 seconds before updating again
            await asyncio.sleep(5)

    async def render_get(self, request):
        # Create a CoAP response with the current temperature
        response = Message(code=Code.CONTENT)
        response.payload = f"Temperature: {self.temperature:.2f} °C".encode('utf-8')
        return response

async def main():
    # Create a CoAP server with the TemperatureResource
    root = resource.Site()
    temperature_resource = TemperatureResource()
    root.add_resource(('temperature',), temperature_resource)

    # Create a CoAP context and listen on a specific address and port
    context = await Context.create_server_context(root, bind=('127.0.0.1', 5683))
    print("CoAP server started on 127.0.0.1:5683")

    # Start the temperature update task
    asyncio.create_task(temperature_resource.update_temperature())

    # Wait for 1 hour before exiting
    await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
