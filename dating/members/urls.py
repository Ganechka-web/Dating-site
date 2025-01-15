from django.urls import path

from . import views


app_name = 'members'

urlpatterns = [
    path('', views.MembersListView.as_view(),
         name='members_list'),
    path('<int:pk>/<str:username>/',
         views.MemberDetailView.as_view(),
         name='member_detail')
]