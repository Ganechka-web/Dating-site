from django import forms

from .models import Message


class CreateChatForm(forms.Form):
    member2_id = forms.IntegerField(widget=forms.HiddenInput())


class SaveMessageForm(forms.ModelForm):
    chat_id = forms.UUIDField(widget=forms.HiddenInput())

    class Meta:
        model = Message
        fields = ('content',)
