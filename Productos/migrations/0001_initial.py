# Generated by Django 2.1.3 on 2018-11-26 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_Cat', models.AutoField(primary_key=True, serialize=False)),
                ('catNombre', models.CharField(default='Nombre_Default', max_length=30)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('catStatus', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_Prod', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=30)),
                ('Descripcion', models.CharField(max_length=70)),
                ('Precio', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('Existencias', models.IntegerField(default=0)),
                ('Status', models.BooleanField(default=True)),
                ('CatId', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Productos.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_Venta', models.AutoField(primary_key=True, serialize=False)),
                ('Precio', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('Nombre', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Productos.Producto')),
            ],
        ),
    ]
