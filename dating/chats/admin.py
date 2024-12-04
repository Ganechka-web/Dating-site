from django.contrib import admin

from .models import Chat, Message


class MessagesInLine(admin.StackedInline):
    model = Message


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [MessagesInLine]
