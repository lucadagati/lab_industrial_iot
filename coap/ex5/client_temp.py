import asyncio
from aiocoap import Context, Message, Code

async def main():
    context = await Context.create_client_context()

    request = Message(code=Code.GET, uri="coap://127.0.0.1:5683/temperature")
    response = await context.request(request).response
    print("Initial temperature:", response.payload.decode('utf-8'))

    request.opt.observe = 0  # Add the "Observe" option
    observation = context.request(request)

    async for response in observation.observation:
        print("Updated temperature:", response.payload.decode('utf-8'))

if __name__ == "__main__":
    asyncio.run(main())
