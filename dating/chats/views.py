from django.views.decorators.http import require_POST
from django.views.generic.base import View, TemplateResponseMixin
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.db.models import Q

from .forms import CreateChatForm, SaveMessageForm
from .models import Chat
from .tasks import save_message


DatingUser = get_user_model()


class CreateChatView(View):
    def post(self, request):
        form = CreateChatForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            member2 = DatingUser.objects.get(id=cd['member2_id'])
            chats_members_ids_for_cur_user = [
                member.id
                for chat in Chat.objects.filter(members__in=[request.user.id])
                for member in chat.members.exclude(id=request.user.id)
            ]

            if member2.id not in chats_members_ids_for_cur_user:
                new_chat = Chat.objects.create()
                new_chat.members.add(request.user, member2)

            return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'error'})


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
        return self.model.objects.filter(members__in=[self.request.user])


class ChatConnectDetailView(View, TemplateResponseMixin):
    template_name = 'chats/chat/detail.html'

    def get(self, request, chat_id: str, *args, **kwargs):
        chat = Chat.objects.get(id=chat_id)

        return self.render_to_response({'section': 'chats',
                                        'chat': chat})


@require_POST
def message_save(request) -> JsonResponse:
    form = SaveMessageForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data

        save_message.delay(request.user.id,
                           cd['chat_id'],
                           cd['content'])

        return JsonResponse({'status': 'saved'})
    return JsonResponse({'status': 'error'})
