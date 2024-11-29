# Generated by Django 4.2 on 2024-11-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('codigo_material', models.AutoField(primary_key=True, serialize=False, verbose_name='Código del Material')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripción')),
                ('tipo_material', models.CharField(choices=[('FERT', 'Producto Terminado'), ('MP', 'Materia Prima'), ('HALB', 'Productos Semi-Elaborados'), ('VERP', 'Material de Empaque'), ('ERSA', 'Piezas de Repuesto')], max_length=25, verbose_name='Tipo de Material')),
                ('unidad_medida', models.CharField(max_length=20, verbose_name='Unidad de Medida')),
                ('precio_estandar', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Estándar')),
                ('peso_bruto', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Peso Bruto')),
                ('centro', models.CharField(choices=[('1000', '1000'), ('1001', '1001'), ('1002', '1002')], max_length=4, verbose_name='Centro')),
                ('grupo_compras', models.CharField(choices=[('001', '001'), ('002', '002'), ('003', '003')], max_length=3, verbose_name='GCp')),
                ('organizacion_compras', models.CharField(choices=[('0001', '0001'), ('0002', '0002'), ('0003', '0003')], max_length=4, verbose_name='OrgC')),
                ('almacen', models.CharField(choices=[('A01', 'A01'), ('A02', 'A01')], max_length=3, verbose_name='Almacén')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiales',
                'ordering': ['descripcion'],
            },
        ),
    ]