import asyncio  # Import the asyncio module
from aiocoap import Context, Message, Code  # Import the Context, Message, and Code classes from the aiocoap module
from coap_utils import print_coap_header  # Import the print_coap_header helper function

async def main():  # Define an asynchronous function called main
    # Create a CoAP context and set the client address
    context = await Context.create_client_context()

    # Create a CoAP GET request
    request = Message(code=Code.GET, uri="coap://127.0.0.1:5683/hello")

    # Send the request and wait for the response
    response = await context.request(request).response

    print_coap_header(response)  # Print the response header using the helper function

    # Print the response
    print("Response code:", response.code)
    print("Payload:", response.payload.decode('utf-8'))

if __name__ == "__main__":  # Check if the script is being run directly
    asyncio.run(main())  # Run the main function using the asyncio event loop
