import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        await self.close(code)

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)

        await self.send(
            text_data=json.dumps(data)
        )


