import asyncio
from aiocoap import resource, Context, Message
from aiocoap.numbers.codes import Code

class MyResource(resource.Resource):
    def __init__(self):
        super().__init__()

    async def render_post(self, request):
        # Stampa il messaggio ricevuto
        print(f'Messaggio ricevuto: {request}\n')

        # Stampa il payload in diversi formati
        payload = request.payload
        print(f'Payload (bytes): {payload}')
        print(f'Payload (stringa): {payload.decode("utf-8")}')
        print(f'Payload (esadecimale): {payload.hex()}')
        print(f'Payload (binario): {"".join(format(byte, "08b") for byte in payload)}\n')

        response = Message(code=Code.CHANGED)
        return response

async def main():
    # Crea una risorsa e aggiungila al contesto
    root = resource.Site()
    root.add_resource(('input',), MyResource())

    # Crea il contesto del server CoAP e avvialo
    context = await Context.create_server_context(root)
    print("Server CoAP in ascolto")
    await asyncio.sleep(3600)  # Tieni il server attivo per un'ora

if __name__ == "__main__":
    asyncio.run(main())
