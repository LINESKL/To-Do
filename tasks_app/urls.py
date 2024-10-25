
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('inbox/', views.task_inbox, name='task_inbox'),
    path('today/', views.task_today, name='task_today'),
    path('upcoming/', views.task_upcoming, name='task_upcoming'),
    path('completed/', views.completed_tasks, name='completed_tasks'),
]
