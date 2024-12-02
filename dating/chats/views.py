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
            Chat.objects.get_or_create(member1=request.user,
                                       member2=member2)
            return JsonResponse({'status': 'ok'})


class ChatsListView(ListView):
    template_name = 'chats/chat/list.html'
    model = Chat

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list,
                                           **kwargs)
        context['section'] = 'chats'

        return context


class ChatDetailConnectView(View, TemplateResponseMixin):
    template_name = 'chats/chat/detail.html'

    def get(self, group_id: str):
        chat = Chat.objects.get(id=group_id)

        self.render_to_response({'section': 'chats',
                                 'chat': chat})
