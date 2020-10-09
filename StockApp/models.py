from django.db import models
from ProductosApp.models import categoriaProducto,Producto

# Create your models here.
class Stock (models.Model):

	nombre_producto = models.ForeignKey( 
        Producto,on_delete=models.CASCADE,blank=False
    )
	categoria = models.ForeignKey( 
        categoriaProducto,on_delete=models.CASCADE,blank=False,
    )
	precio_de_compra=models.DecimalField(default=0,max_digits=7,decimal_places=2, blank=False)
	cantidad = models.PositiveIntegerField(default='0', blank=False, null=True)
	fecha_stock = models.DateField(auto_now_add=False, auto_now=True)
	export_to_CSV = models.BooleanField(default=False)

	def __str__(self):
		return str(self.nombre_producto) + ' (' + str(self.cantidad) + ')'