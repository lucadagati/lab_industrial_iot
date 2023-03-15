import asyncio  # Import the asyncio module
from aiocoap import resource, Context, Message  # Import the resource, Context, and Message classes from the aiocoap module
from aiocoap.numbers.codes import Code  # Import the Code class from the aiocoap.numbers.codes module

class MyResource(resource.Resource):  # Define a class called MyResource that inherits from the Resource class
    def __init__(self):
        super().__init__()

    async def render_post(self, request):  # Define a method called render_post that handles POST requests
        # Print the received message
        print(f'Messaggio ricevuto: {request}\n')

        # Print the payload in various formats
        payload = request.payload
        print(f'Payload (bytes): {payload}')
        print(f'Payload (stringa): {payload.decode("utf-8")}')
        print(f'Payload (esadecimale): {payload.hex()}')
        print(f'Payload (binario): {"".join(format(byte, "08b") for byte in payload)}\n')

        response = Message(code=Code.CHANGED)  # Create a response message with a CHANGED code
        return response  # Return the response message

async def main():  # Define an asynchronous function called main
    # Create a resource and add it to the context
    root = resource.Site()
    root.add_resource(('input',), MyResource())

    # Create a CoAP server context and start it
    context = await Context.create_server_context(root)
    print("Server CoAP in ascolto")
    await asyncio.sleep(3600)  # Keep the server running for one hour

if __name__ == "__main__":  # Check if the script is being run directly
    asyncio.run(main())  # Run the main function using the asyncio event loop
