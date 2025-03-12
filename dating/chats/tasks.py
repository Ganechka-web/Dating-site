from celery import shared_task

from chats.services.messages import create_message
from chats.services.chats import create_chat


@shared_task(ignore_result=True)
def process_chat(cur_user_id: int, second_user_id: int) -> None:
    create_chat(cur_user_id, second_user_id)


@shared_task(ignore_result=True)
def process_message(user_id: int, chat_id: int, content: str) -> None:
    create_message(user_id, chat_id, content)
