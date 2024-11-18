from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .forms import DatingUserCreationForm, \
                    DatingUserChangeForm
from .models import DatingUser, Interest


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(DatingUser)
class DatingUserAdmin(UserAdmin):
    add_form = DatingUserCreationForm
    form = DatingUserChangeForm
    model = DatingUser
    list_display = ['username', 'city',
                    'date_birth', 'phone']
