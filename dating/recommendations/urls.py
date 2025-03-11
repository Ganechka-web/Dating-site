from django.urls import path

from . import views


app_name = 'recommendations'

urlpatterns = [
    path('create/', views.create_recommendation, name='create'),
    path('', views.RecommendationsListView.as_view(), name='list'),
    path('<int:pk>/', views.RecommendationsDetailView.as_view(),
         name='detail')
]