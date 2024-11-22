from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .forms import DatingUserCreationForm, \
                    DatingUserChangeForm
from .models import DatingUser, Interest


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {
        'slug': ['name']
    }


@admin.register(DatingUser)
class DatingUserAdmin(UserAdmin):
    custom_fieldsets = ((
        'Additional information', {'fields': (
            'image', 'city', 'date_birth',
            'phone', 'description'
        )}
    ),)
    add_form = DatingUserCreationForm
    form = DatingUserChangeForm
    model = DatingUser
    list_display = ['username', 'city',
                    'date_birth', 'phone']
    fieldsets = UserAdmin.fieldsets + custom_fieldsets
