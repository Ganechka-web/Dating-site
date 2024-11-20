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
    path('<int:pk>/<str:username>/',
         views.DatingUserDatailView.as_view(),
         name='user_detail')
]