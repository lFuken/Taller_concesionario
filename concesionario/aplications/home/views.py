from django.shortcuts import render
from django.urls import reverse_lazy
from aplications.clientes.models import Cliente
from aplications.coches_vendidos.models import Coche
from aplications.revisiones.models import Revision

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView

class ClientesCreateView(CreateView):
    template_name = "home/home.html"
    model = Cliente
    fields = ['nombre_cliente','apellido_cliente', 'direccion_cliente','poblacion', 'codigo_postal', 'provincia','telefono','fecha_nacimiento']

class ListarClienteListView(ListView):
    cl= Cliente.objects.prefetch_related()
    queryset=cl
    fields=('__all__')
    template_name = "home/listar.html"
    context_object_name = 'cliente'    

class ListarCocheListView(ListView):
    cl= Coche.objects.prefetch_related()
    queryset=cl
    fields=('__all__')
    template_name = "home/lista_cliente.html"
    context_object_name = 'listar'

class ListarRevicionListView(ListView):
    Rv= Revision.objects.prefetch_related()
    queryset=Rv
    fields=('__all__')
    template_name = "home/lista_reviciones.html"
    context_object_name = 'revicion'  

class ClienteUpdateView(UpdateView):
    template_name = "home/actualizar_cliente.html"
    model = Cliente
    fields = ('__all__')
    success_url = reverse_lazy('home_app:Cli_up')
  