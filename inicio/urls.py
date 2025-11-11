from django.urls import path
from inicio.views import listar_articulo, crear_articulo
urlpatterns = [
    path('crear-articulo/<tipo>/<marca>', crear_articulo),
    path('listado-articulos', listar_articulo)
]