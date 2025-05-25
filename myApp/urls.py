from django.urls import path
from . import views


urlpatterns = [
    path('', views.TaskList.as_view()),
    path('edit/<int:pk>/', views.TaskDetail.as_view()),
]