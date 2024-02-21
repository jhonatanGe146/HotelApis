# Generated by Django 5.0.2 on 2024-02-21 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mod_inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='estado_habitacion',
            fields=[
                ('IDESTADOHABITACION', models.AutoField(primary_key=True, serialize=False)),
                ('TIPO_ESTADO', models.CharField(max_length=20)),
                ('DESCRIPCION', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_habitacion',
            fields=[
                ('IDTIPOHABITACION', models.AutoField(primary_key=True, serialize=False)),
                ('TIPO_HABITACION', models.CharField(max_length=30)),
                ('DESCRIPCION', models.TextField(max_length=200)),
                ('PRECIOXNOCHE', models.FloatField()),
                ('CANTIDAD_ADULTOS', models.IntegerField()),
                ('CANTIDAD_NINOS', models.IntegerField()),
                ('FOTO', models.ImageField(upload_to='fotos_tipoHab')),
            ],
        ),
        migrations.CreateModel(
            name='habitacion',
            fields=[
                ('NROHABITACION', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('ESTADO_HABITACION_IDESTADOHABITACION', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mod_room.estado_habitacion')),
                ('TIPO_HABITACION_IDTIPOHABITACION', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_room.tipo_habitacion')),
            ],
        ),
        migrations.CreateModel(
            name='inventario_habitacion',
            fields=[
                ('ID_INVENTARIO_HABITACION', models.AutoField(primary_key=True, serialize=False)),
                ('HABITACION_NROHABITACION', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_room.habitacion')),
                ('INVENTARIO_IDINVENTARIO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_inventory.inventario')),
            ],
        ),
    ]