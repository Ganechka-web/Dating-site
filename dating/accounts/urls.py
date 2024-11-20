from django.urls import path

from . import views


urlpatterns = [
    path('register/',
         views.DatingUserRegistrationView.as_view(),
         name='registration'),
    path('login/',
         views.DatingUserLoginView.as_view(),
         name='login'),
    # path('logout/',
    #      views,
    #      name='logout')
]