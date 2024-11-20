from django.urls import reverse
from django.views.generic.base import TemplateResponseMixin
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, \
    get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View

from .forms import DatingUserCreationForm, \
                    DatingUserLoginForm


DatingUser = get_user_model()


class DatingUserRegistrationView(View, TemplateResponseMixin):
    template_name = 'accounts/registration/register.html'

    def get(self, reguest):
        form = DatingUserCreationForm()

        return self.render_to_response({'form': form})

    def post(self, request):
        form = DatingUserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data['password1'])
            new_user.save()

            return redirect('login')

        return self.render_to_response({'form': form})


class DatingUserLoginView(View, TemplateResponseMixin):
    template_name = 'accounts/registration/login.html'

    def get(self, request):
        form = DatingUserLoginForm()

        return self.render_to_response({'form': form})

    def post(self, request):
        form = DatingUserLoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            current_user = authenticate(request,
                                        username=cd['username'],
                                        password=cd['password'])
            if current_user:
                login(request, current_user)

                return redirect('user_detail',
                                current_user.id,
                                current_user.username)

            else:
                form.add_error('password',
                               'Your username or password didn`t match')

        return self.render_to_response({'form': form})


class DatingUserLogoutView(View):
    def post(self, request):
        logout(request)

        return redirect('login')


class DatingUserDatailView(DetailView):
    template_name = 'accounts/dating_user/profile.html'
    model = DatingUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'profile'

        return context
