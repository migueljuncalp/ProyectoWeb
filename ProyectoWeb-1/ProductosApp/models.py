from django.db import models

class categoriaProducto(models.Model):
    categoria = models.CharField(max_length=30)
    pass
    class Meta:
        verbose_name = 'categoriaProducto'
        verbose_name_plural = 'categoriaProductos'
    def __str__(self):
        return self.categoria
        


class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    precio_sin_iva = models.FloatField()
    precio_iva = models.FloatField()
    categoriaProducto = models.ForeignKey( 
        categoriaProducto,on_delete=models.CASCADE,
    )
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    def __str__(self):
        return self.nombre_producto
     
