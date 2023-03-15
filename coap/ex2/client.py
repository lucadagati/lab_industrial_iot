import asyncio
from aiocoap import Context, Message, Code
from coap_utils import print_coap_header  # Import the helper function

async def main():

    # Create a CoAP context and set the client address
    context = await Context.create_client_context()

    # Create a CoAP GET request
    request = Message(code=Code.GET, uri="coap://127.0.0.1:5683/hello")

    # Send the request and wait for the response
    response = await context.request(request).response

    print_coap_header(response)  # Print the response header

    # Print the response
    print("Response code:", response.code)
    print("Payload:", response.payload.decode('utf-8'))

if __name__ == "__main__":
    asyncio.run(main())
