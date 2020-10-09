from django.db import models
from ProductosApp.models import Producto

# Create your models here.
class Stock (models.Model):

	nombre_producto = models.ForeignKey(Producto,null=True ,blank=True ,on_delete=models.CASCADE)

	precio_de_compra=models.DecimalField(default=0,max_digits=7,decimal_places=2, blank=False)
	cantidad = models.PositiveIntegerField(default='0', blank=False, null=True)
	fecha_stock = models.DateField(auto_now_add=False, auto_now=True)
	export_to_CSV = models.BooleanField(default=False)

