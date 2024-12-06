from django.contrib.auth import get_user_model

from celery import shared_task

from .models import Chat, Message


DatingUser = get_user_model()


@shared_task(ignore_result=True)
def save_message(user_id, chat_id, content):
    user = DatingUser.objects.get(id=user_id)
    chat = Chat.objects.get(id=chat_id)
    Message.objects.create(
        content=content,
        sender=user,
        chat=chat)
