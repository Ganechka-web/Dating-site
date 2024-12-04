from django import template
from django.contrib.auth import get_user_model


DatingUser = get_user_model()

register = template.Library()


@register.filter
def get_other_user(chat, current_user) -> DatingUser:
    return chat.members.exclude(id=current_user.id) \
                       .first()
