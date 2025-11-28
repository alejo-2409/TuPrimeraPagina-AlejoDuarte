from django.shortcuts import render
from inicio.models import Articulo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from .models import Articulo
from django.urls import reverse_lazy
from .forms import FormularioArticulo


@login_required
def inicio(request):
    return render(request, 'inicio.html')

class ListaArticulo(LoginRequiredMixin, ListView):
    model = Articulo
    template_name = 'listar_articulos.html'
    context_object_name = 'listado_de_articulos'


class CrearArticulo (LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = FormularioArticulo
    template_name = 'crear_articulo.html'
    success_url = reverse_lazy('listar_articulos')

class ActualizarArticulo (LoginRequiredMixin, UpdateView):
    model = Articulo
    form_class = FormularioArticulo
    template_name = 'editar_articulo.html'
    success_url = reverse_lazy ('listar_articulos')

class BorrarArticulo (LoginRequiredMixin, DeleteView):
    model = Articulo
    template_name = 'borrar_articulo.html'
    success_url = reverse_lazy ('listar_articulos')

def about(request):
    return render(request, "inicio/about.html")