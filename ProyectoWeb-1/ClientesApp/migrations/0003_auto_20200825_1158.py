# Generated by Django 3.1 on 2020-08-25 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClientesApp', '0002_auto_20200825_1155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='nombre_clientes',
            new_name='nombre_cliente',
        ),
    ]