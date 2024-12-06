import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy

DatingUser = get_user_model()


class Chat(models.Model):
    objects = models.Manager()

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    members = models.ManyToManyField(DatingUser,
                                     related_name='chats')
    # member1 = models.ForeignKey(DatingUser,
    #                             related_name='member1_groups',
    #                             null=True,
    #                             on_delete=models.SET_NULL)
    # member2 = models.ForeignKey(DatingUser,
    #                             related_name='member2_groups',
    #                             null=True,
    #                             on_delete=models.SET_NULL)

    def __str__(self):
        return f'Chat {self.id}'

    def get_absolute_url(self):
        return reverse_lazy('chat_detail', args=[self.id])


class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(DatingUser,
                               related_name='+',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)
    sent = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat,
                             related_name='messages',
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True)
