# Generated by Django 3.1 on 2020-08-25 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_clientes', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=70)),
            ],
        ),
    ]