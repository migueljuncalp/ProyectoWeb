from django.db import models

class Cliente (models.Model):
    nombre_cliente = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length = 70)
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    def __str__(self):
        return self.nombre_cliente
     

