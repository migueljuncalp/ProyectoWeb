"""" Creamos un urls para la AppWeb, lo llammos desde urls del proyecto"""

from django.urls import path
from StockApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("stock",views.list_stock,name="listStock"),
    path('addToStock', views.add_items, name='addToStock'),
    
    ]

###PAra poder ver imagenes desde admin
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)