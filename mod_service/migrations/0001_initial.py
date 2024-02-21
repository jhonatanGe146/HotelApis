# Generated by Django 5.0.2 on 2024-02-21 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tipo_servicio',
            fields=[
                ('IDTIPOSERVICIO', models.AutoField(primary_key=True, serialize=False)),
                ('TIPO_SERVICIO', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('IDPRODUCTO', models.AutoField(primary_key=True, serialize=False)),
                ('NOMBRE_PRODUCTO', models.CharField(max_length=45)),
                ('VALOR', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TIPO_SERVICIO_IDTIPOSERVICIO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_service.tipo_servicio')),
            ],
        ),
    ]