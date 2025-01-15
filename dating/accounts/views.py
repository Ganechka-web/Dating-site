from dateutil.relativedelta import relativedelta
from datetime import datetime

from django.views.generic.base import TemplateResponseMixin
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, \
                                get_user_model, logout
from django.shortcuts import redirect
from django.views import View

from .forms import (DatingUserCreationForm,
                    DatingUserLoginForm,
                    DatingUserUpdateInterestsForm,
                    DatingUserUpdateAdditionalInfoForm)


DatingUser = get_user_model()


class DatingUserRegistrationView(View, TemplateResponseMixin):
    template_name = 'registration/register.html'

    def get(self, request):
        form = DatingUserCreationForm()

        return self.render_to_response({'form': form})

    def post(self, request):
        form = DatingUserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            user_age = relativedelta(datetime.now(),
                                     form.cleaned_data['date_birth']).years
            if user_age >= 18:
                new_user.age = user_age
                new_user.set_password(
                    form.cleaned_data['password1'])
                new_user.save()

                return redirect('login')
            else:
                form.add_error('date_birth',
                               'You aren`t old enough to register')

        return self.render_to_response({'form': form})


class DatingUserLoginView(View, TemplateResponseMixin):
    template_name = 'registration/login.html'

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


@method_decorator(login_required, name='dispatch')
class DatingUserDetailView(DetailView):
    template_name = 'accounts/dating_user/profile.html'
    model = DatingUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'profile'

        return context


@method_decorator(login_required, name='dispatch')
class DatingUserUpdateInterestsView(View, TemplateResponseMixin):
    template_name = 'accounts/dating_user/interests_form.html'

    def get(self, request):
        form = DatingUserUpdateInterestsForm(instance=request.user)
        choices = form.fields['interests'].choices

        return self.render_to_response({'form': form, 'choices': choices})

    def post(self, request):
        form = DatingUserUpdateInterestsForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('user_detail',
                            request.user.id,
                            request.user.username)
        choices = form.fields['interests'].choices

        return self.render_to_response({'form': form, 'choices': choices})


@method_decorator(login_required, name='dispatch')
class DatingUserUpdateAdditionalInfoView(View, TemplateResponseMixin):
    template_name = 'accounts/dating_user/additional_info_form.html'

    def get(self, request):
        form = DatingUserUpdateAdditionalInfoForm(
                   instance=request.user)

        return self.render_to_response({'form': form})

    def post(self, request):
        form = DatingUserUpdateAdditionalInfoForm(
                   instance=request.user,
                   data=request.POST,
                   files=request.FILES)
        if form.is_valid():
            form.save()

            return redirect('user_detail',
                            request.user.pk,
                            request.user.username)
        return self.render_to_response({'form': form})
