from django.urls import path
from . import views

app_name = 'tipo_projeto'

urlpatterns = [
    path('', views.TipoProjetoListView.as_view(), name='list'),
    path('create/', views.TipoProjetoCreateView.as_view(), name='create'),
    path('<int:pk>/', views.TipoProjetoDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.TipoProjetoUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.TipoProjetoDeleteView.as_view(), name='delete'),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    path('select/<int:pk>/', views.select_tipo_projeto, name='select'),
] 