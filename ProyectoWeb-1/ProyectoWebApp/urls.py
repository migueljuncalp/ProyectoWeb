


"""" Creamos un urls para la AppWeb, lo llammos desde urls del proyecto"""

from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.Home,name="home"),
    path("factura",views.Factura,name="factura"),
    path("inicio",views.Home,name="productos"),
    path("contabilidad",views.Contabilidad,name="contabilidad"),
    path("clientes",views.Clientes,name="clientes"),

]

###PAra poder ver imagenes desde admin
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)