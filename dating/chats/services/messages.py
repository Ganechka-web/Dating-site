from django.contrib.auth import get_user_model

from chats.models import Chat, Message


DatingUser = get_user_model()


def create_message(user_id: int, chat_id: int, content: str) -> None:
    user = DatingUser.objects.get(id=user_id)
    chat = Chat.objects.get(id=chat_id)
    Message.objects.create(
        content=content,
        sender=user,
        chat=chat)
