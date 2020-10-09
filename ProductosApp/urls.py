"""" Creamos un urls para la AppWeb, lo llammos desde urls del proyecto"""

from django.urls import path
from ProductosApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("categorias",views.mostrar_categorias, name="categorias"),
    path("categoriaForm",views.categoria_add, name="categoriaForm"),
    path("categoriaEdit/<id_categoria>",views.categoria_edit, name="categoriaEditar"),
    path("categoriaDelete/<id_categoria>",views.categoria_delete, name="categoriaDelete"),

    path("productos",views.mostrar_productos, name="productos"),
    path("productoForm",views.producto_add, name="productoForm"),
    path("productoEdit/<id_producto>",views.producto_edit, name="productoEditar"),
    path("productoDelete/<id_producto>",views.producto_delete, name="productoDelete"),

]
