import asyncio  # Import the asyncio module
from aiocoap import Context, Message  # Import the Context and Message classes from the aiocoap module
from aiocoap.numbers.codes import Code  # Import the Code class from the aiocoap.numbers.codes module

async def main():  # Define an asynchronous function called main
    # Create a CoAP client context
    context = await Context.create_client_context()

    while True:  # Loop forever
        # Read a message from the keyboard
        messaggio = input("Inserisci un messaggio da inviare al server: ")

        # Prepare a POST request
        request = Message(code=Code.POST, payload=messaggio.encode('utf-8'))
        request.set_request_uri('coap://localhost/input')

        # Send the request and wait for the response
        await context.request(request).response

if __name__ == "__main__":  # Check if the script is being run directly
    asyncio.run(main())  # Run the main function using the asyncio event loop
