import json

from django.utils import timezone

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.chat_group_name = f'channel_for_chat_{chat_id}'
        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name)

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        current_user = self.scope['user']
        sent = timezone.now()

        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user_id': current_user.id,
                'user_username': current_user.username,
                'sent': sent.isoformat()
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))
