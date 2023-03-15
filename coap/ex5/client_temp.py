import asyncio
from aiocoap import Context, Message, Code

async def main():
    context = await Context.create_client_context()  # Create a CoAP client context

    request = Message(code=Code.GET, uri="coap://127.0.0.1:5683/temperature")  # Create a CoAP GET request to retrieve the temperature resource
    response = await context.request(request).response  # Send the request and wait for the response
    print("Initial temperature:", response.payload.decode('utf-8'))  # Print the initial temperature

    request.opt.observe = 0  # Add the "Observe" option to the request
    observation = context.request(request)  # Send the observation request to the server

    async for response in observation.observation:  # Start listening for updates
        print("Updated temperature:", response.payload.decode('utf-8'))  # Print the updated temperature

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine
