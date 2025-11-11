from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Articulo



def crear_articulo(request, tipo, marca):

    articulo = Articulo (tipo=tipo, marca=marca)
    articulo.save()

    return render(request,'crear_articulo.html', {'objeto_guardado': articulo})

def listar_articulo(request):
    articulos = Articulo.objects.all()
    return render(request,'listar_articulos.html', {'listado_de_articulos': articulos})