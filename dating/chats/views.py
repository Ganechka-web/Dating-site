from django.views.decorators.http import require_POST
from django.views.generic.base import View, TemplateResponseMixin
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from .forms import CreateChatForm, SaveMessageForm
from .models import Chat
from .tasks import process_chat, process_message


DatingUser = get_user_model()


class CreateChatView(View):
    """Received form from js, sets off celery task"""
    def post(self, request):
        form = CreateChatForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            process_chat.delay(cur_user_id=request.user.id,
                               second_user_id=cd['member2_id'])

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
    """
    Receives json data with message info and
    sets off celery task
    """
    form = SaveMessageForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data

        process_message.delay(request.user.id,
                              cd['chat_id'],
                              cd['content'])

        return JsonResponse({'status': 'saved'})
    return JsonResponse({'status': 'error'})
