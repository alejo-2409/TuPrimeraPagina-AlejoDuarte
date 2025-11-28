from django.urls import path
from inicio.views import inicio,about, CrearArticulo, ListaArticulo, BorrarArticulo, ActualizarArticulo
urlpatterns = [
    path('', inicio, name ='inicio'),
    path('articulos/', ListaArticulo.as_view(), name ='listar_articulos'),
    path('articulos/crear/', CrearArticulo.as_view(), name = 'crear_articulo'),
    path('articulos/editar/<int:pk>/', ActualizarArticulo.as_view(), name = 'actualizar_articulo'),
    path('articulos/borrar/<int:pk>/', BorrarArticulo.as_view(), name = 'borrar_articulo'),
    path('about/', about, name='about'),


]   