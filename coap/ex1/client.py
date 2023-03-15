import asyncio
from aiocoap import Context, Message
from aiocoap.numbers.codes import Code

async def main():
    # Crea il contesto del client CoAP
    context = await Context.create_client_context()

    while True:
        # Leggi il messaggio dalla tastiera
        messaggio = input("Inserisci un messaggio da inviare al server: ")

        # Prepara la richiesta POST
        request = Message(code=Code.POST, payload=messaggio.encode('utf-8'))
        request.set_request_uri('coap://localhost/input')

        # Invia la richiesta
        await context.request(request).response

if __name__ == "__main__":
    asyncio.run(main())
