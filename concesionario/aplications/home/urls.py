from django.contrib import admin
from django.urls import path

from.import views

urlpatterns = [
    path('home/', views.ClientesCreateView.as_view()),
    path('listar/', views.ListarClienteListView.as_view()),
    path('lista_cliente/', views.ListarCocheListView.as_view()),
    path('lista_reviciones/', views.ListarRevicionListView.as_view()),
]