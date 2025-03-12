from django.contrib.auth import get_user_model

from chats.models import Chat


DatingUser = get_user_model()


def create_chat(cur_user_id: int, member_id: int) -> None:
    current_user = DatingUser.objects.get(id=cur_user_id)
    second_user = DatingUser.objects.get(id=member_id)

    # all members ids set from user`s chats to exclude duplicates
    members_ids_for_cur_user = {
        id 
        for chat in Chat.objects.filter(members__in=[current_user.id])
        for id in chat.members.values_list('id', flat=True)
    }

    if second_user.id not in members_ids_for_cur_user:
        new_chat = Chat.objects.create()
        new_chat.members.add(current_user, second_user)
    