# Generated by Django 4.2 on 2024-11-30 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion_de_materiales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudPedido',
            fields=[
                ('id_solicitud', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_solicitud', models.CharField(editable=False, max_length=30)),
                ('tipo_solicitud', models.CharField(choices=[('RV', 'Contrato Marco'), ('NB', 'Pedido Estándar')], max_length=10)),
                ('solicitante', models.CharField(max_length=50, verbose_name='Solicitante')),
                ('fecha_entrega', models.DateField(verbose_name='Fecha de Entrega')),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Solicitud')),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('aceptada', 'Aceptada'), ('cancelada', 'Cancelada')], default='pendiente', max_length=10)),
            ],
            options={
                'verbose_name': 'Solicitud de Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='SolicitudPedidoMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_de_materiales.material')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes_de_pedidos.solicitudpedido')),
            ],
            options={
                'verbose_name': 'Material de Solicitud',
                'verbose_name_plural': 'Materiales de Solicitud',
            },
        ),
        migrations.AddField(
            model_name='solicitudpedido',
            name='materiales',
            field=models.ManyToManyField(related_name='solicitudes_pedido', through='solicitudes_de_pedidos.SolicitudPedidoMaterial', to='gestion_de_materiales.material'),
        ),
    ]
