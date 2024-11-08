from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='list'),
    path('partial/', views.task_list_partial, name='list_partial'),
    path('new/', views.task_create, name='create'),
    path('<int:pk>/', views.task_detail, name='detail'),
    path('<int:pk>/edit/', views.task_update, name='update'),
    path('<int:pk>/delete/', views.task_delete, name='delete'),
    path('<int:pk>/change-status/', views.task_change_status, name='change_status'),
] 