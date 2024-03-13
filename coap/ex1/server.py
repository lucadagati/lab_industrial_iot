import asyncio
import logging
from aiocoap import resource, Context, Message
from aiocoap.numbers.codes import Code

# Configure logging level
logging.basicConfig(level=logging.INFO)

class MyResource(resource.Resource):
    def __init__(self):
        super().__init__()

    async def render_post(self, request):
        try:
            payload = request.payload
            # Log the received message and payload in various formats
            logging.info(f'Message received: {request}\n')
            logging.info(f'Payload (bytes): {payload}')
            logging.info(f'Payload (string): {payload.decode("utf-8")}')
            logging.info(f'Payload (hexadecimal): {payload.hex()}')
            logging.info(f'Payload (binary): {"".join(format(byte, "08b") for byte in payload)}\n')

            # Create a response message with a CHANGED status code
            response = Message(code=Code.CHANGED)
            return response
        except Exception as e:
            # Log any errors encountered during request processing
            logging.error(f"Error processing the request: {e}")
            return Message(code=Code.INTERNAL_SERVER_ERROR)

async def main():
    # Create a CoAP server context and start listening
    root = resource.Site()
    root.add_resource(('input',), MyResource())

    context = await Context.create_server_context(root)
    logging.info("CoAP server listening")

    # Keep the server running for an hour
    await asyncio.sleep(3600)

if __name__ == "__main__":
    # Run the main function using asyncio's event loop
    asyncio.run(main())
