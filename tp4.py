import asyncio
import websockets


async def hello(websocket, path):
    receivedMessage=await websocket.recv()
    print("Message received "+ receivedMessage)
    messageToSend = "Hi client"
    await websocket.send(messageToSend)

start_server = websockets.serve(hello, "localhost", 12345)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()