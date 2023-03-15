import asyncio  # Import the asyncio module
from aiocoap import resource, Context, Message, Code  # Import the Context, Message, and Code classes from the aiocoap module
from coap_utils import print_coap_header  # Import the print_coap_header helper function

class HelloWorldResource(resource.Resource):
    async def render_get(self, request):
        print_coap_header(request)  # Print the request header using the helper function

        # Create a CoAP response
        response = Message(code=Code.CONTENT)
        response.payload = b"Hello, CoAP!"
        return response

async def main():  # Define an asynchronous function called main
    # Create a CoAP server with the HelloWorldResource
    root = resource.Site()
    root.add_resource(('hello',), HelloWorldResource())

    # Create a CoAP context and listen on a specific address and port
    context = await Context.create_server_context(root, bind=('127.0.0.1', 5683))
    print("CoAP server started on 127.0.0.1:5683")
    await asyncio.sleep(3600)  # Keep the server running for 1 hour

if __name__ == "__main__":  # Check if the script is being run directly
    asyncio.run(main())  # Run the main function using the asyncio event loop
