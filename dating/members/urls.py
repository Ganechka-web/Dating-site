from django.urls import path

from . import views


app_name = 'members'

urlpatterns = [
    path('', views.MembersListView.as_view(),
         name='members_list')
]