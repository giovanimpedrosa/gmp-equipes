from django.urls import path
from . import views

app_name = 'teste'

urlpatterns = [
    path('', views.edicao, name='edicao'),
    path('validate/', views.validate_input, name='validate_input'),
    path('process_data/', views.process_data, name='process_data'),
    path('number_input/', views.number_input_view, name='number_input'),
    
] 