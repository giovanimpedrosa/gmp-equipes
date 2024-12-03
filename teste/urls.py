from django.urls import path
from . import views

app_name = 'teste'

urlpatterns = [
    path('', views.edicao, name='edicao'),
    path('validate/', views.validate_input, name='validate_input'),
    path('validate_number/', views.validate_number, name='validate_number'),
    path('input-form/', views.input_form, name='input_form'),  
    path('validate_text/', views.validate_text, name='validate_text'),
    path('validate_email/', views.validate_email, name='validate_email'),
    path('validate_password/', views.validate_password, name='validate_password'),
    path('validate_date/', views.validate_date, name='validate_date'),
    path('validate_number/', views.validate_number, name='validate_number'),
    path('validate_textarea/', views.validate_textarea, name='validate_textarea'),
    path('validate_checkbox/', views.validate_checkbox, name='validate_checkbox'),
    path('validate_select/', views.validate_select, name='validate_select'),

    
] 