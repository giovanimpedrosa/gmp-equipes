from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('update-theme/', views.update_theme, name='update_theme'),
] 