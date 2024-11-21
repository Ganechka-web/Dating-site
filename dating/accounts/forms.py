from dateutil.relativedelta import relativedelta
from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,\
                                       UserChangeForm
from django.core.exceptions import ValidationError
from django import forms

from .models import Interest


DatingUser = get_user_model()


class DatingUserCreationForm(UserCreationForm):
    class Meta:
        model = DatingUser
        fields = ('username', 'email', 'date_birth',
                  'phone')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] == cd['password2']:
            return cd['password2']
        raise ValidationError('Passwords aren`t the same')

    def clean_date_birth(self):
        cd = self.cleaned_data
        age = relativedelta(datetime.now(),
                            cd['date_birth']).years
        if age > 18:
            return cd['date_birth']
        raise ValidationError('You aren`t old enough to register')


class DatingUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = DatingUser
        fields = ('username', 'city', 'email',
                  'date_birth', 'description',
                  'phone')


class DatingUserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class DatingUserUpdateInterestsForm(forms.ModelForm):
    interests = forms.ModelMultipleChoiceField(
                        queryset=Interest.objects.all())

    class Meta:
        model = DatingUser
        fields = ('interests',)


class DatingUserUpdateAdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = DatingUser
        fields = ('image', 'city', 'gender',
                  'description')
