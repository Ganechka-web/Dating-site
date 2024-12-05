import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.channel_layer.group_add(
            self.scope['url_route']['chat_id'])

        await self.accept()

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.scope['url_route']['chat_id'])

        await self.close(code)

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)

        await self.send(
            text_data=json.dumps(data)
        )
