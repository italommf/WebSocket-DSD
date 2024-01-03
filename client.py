import asyncio
import websockets

async def client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            message = input("Client - Fulanilson: ")
            await websocket.send(message)

            response = await websocket.recv()
            print(f"Resposta do servidor: {response}")

asyncio.get_event_loop().run_until_complete(client())
