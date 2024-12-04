from django.urls import re_path

from . import consumers


ws_urlpatterns = [
    re_path('ws/chats/(?P<chat_id>[^/]+)/$',
            consumers.ChatConsumer.as_asgi())
]