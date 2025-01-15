from django.urls import path, include

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
    path('<int:pk>/<str:username>/profile/',
         views.DatingUserDetailView.as_view(),
         name='user_detail'),
    path('update-interests/',
         views.DatingUserUpdateInterestsView.as_view(),
         name='update_user_interests'),
    path('add-additional-info/',
         views.DatingUserUpdateAdditionalInfoView.as_view(),
         name='add_additional_user_info'),
    path('', include('django.contrib.auth.urls'))
]