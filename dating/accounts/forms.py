from django.contrib.auth.forms import UserCreationForm,\
                                       UserChangeForm

from .models import DatingUser


class DatingUserCreationForm(UserCreationForm):
    class Meta:
        model = DatingUser
        fields = ('username', 'email', 'date_birth',
                  'phone')


class DatingUserChangeForm(UserChangeForm):
    class Meta:
        model = DatingUser
        fields = ('username', 'city', 'email',
                  'date_birth', 'description',
                  'phone')


