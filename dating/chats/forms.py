from django import forms


class CreateChatForm(forms.Form):
    member2_id = forms.IntegerField(widget=forms.HiddenInput())
