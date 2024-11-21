from django.urls import path

from . import views


urlpatterns = [
    path('register/',
         views.DatingUserRegistrationView.as_view(),
         name='registration'),
    path('login/',
         views.DatingUserLoginView.as_view(),
         name='login'),
    path('logout/',
         views.DatingUserLogoutView.as_view(),
         name='logout'),
    path('<int:pk>/profile/',
         views.DatingUserDatailView.as_view(),
         name='user_detail'),
    path('update-interests/',
         views.DatingUserUpdateInterestsView.as_view(),
         name='update_user_interests')
]