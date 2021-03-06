from django.contrib import admin
from django.urls import path

from.import views

app_name = "home_app"

urlpatterns = [
    path('home/', views.ClientesCreateView.as_view()),
    path('listar/', views.ListarClienteListView.as_view()),
    path('lista_cliente/', views.ListarCocheListView.as_view()),
    path('lista_reviciones/', views.ListarRevicionListView.as_view()),
    path('success/', views.successView.as_view(), name='Cli_up'),
    path('actualizar_cliente/<pk>/', views.ClienteUpdateView.as_view(),),
]
