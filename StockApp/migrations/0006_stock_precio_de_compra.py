# Generated by Django 3.1 on 2020-08-29 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockApp', '0005_auto_20200829_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='precio_de_compra',
            field=models.FloatField(default=0),
        ),
    ]