import asyncio
from aiocoap import resource, Context, Message, Code
from coap_utils import print_coap_header  # Import the helper function

class HelloWorldResource(resource.Resource):
    async def render_get(self, request):
        print_coap_header(request)  # Print the request header

        response = Message(code=Code.CONTENT)
        response.payload = b"Hello, CoAP!"
        return response

async def main():
    # Create a CoAP server with the HelloWorldResource
    root = resource.Site()
    root.add_resource(('hello',), HelloWorldResource())

    # Create a CoAP context and listen on a specific address and port
    context = await Context.create_server_context(root, bind=('127.0.0.1', 5683))
    print("CoAP server started on 127.0.0.1:5683")
    await asyncio.sleep(3600)  # Keep the server running for 1 hour

if __name__ == "__main__":
    asyncio.run(main())
