# Generated by Django 3.1 on 2020-08-28 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductosApp', '0005_remove_producto_precio_de_compra'),
        ('StockApp', '0002_auto_20200828_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductosApp.categoriaproducto'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='nombre_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductosApp.producto'),
        ),
    ]
