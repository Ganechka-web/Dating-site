from django.views.generic.base import View, TemplateResponseMixin
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from .forms import CreateChatForm
from .models import Chat


DatingUser = get_user_model()


class CreateChatView(View):
    def post(self, request):
        form = CreateChatForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            member2 = DatingUser.objects.get(id=cd['member2_id'])
            try:
                Chat.objects.get(members__in=[request.user, member2])
            except Chat.DoesNotExist:
                new_chat = Chat.objects.create()
                new_chat.members.add(request.user, member2)

            return JsonResponse({'status': 'ok'})


class ChatsListView(ListView):
    template_name = 'chats/chat/list.html'
    context_object_name = 'chats'
    model = Chat

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list,
                                           **kwargs)
        context['section'] = 'chats'

        return context

    def get_queryset(self):
        return self.model.objects.filter


class ChatConnectDetailView(View, TemplateResponseMixin):
    template_name = 'chats/chat/detail.html'

    def get(self, request, chat_id: str):
        chat = Chat.objects.get(id=chat_id)

        return self.render_to_response({'section': 'chats',
                                        'chat': chat})
