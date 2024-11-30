from django.db import models
from gestion_de_materiales.models import Material

class SolicitudPedido(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    codigo_solicitud = models.CharField(max_length=30, editable=False)
    tipo_solicitud = models.CharField(
        max_length=10,
        choices=[('RV', 'Contrato Marco'), ('NB', 'Pedido Estándar')]
    )
    solicitante = models.CharField(max_length=50, verbose_name="Solicitante")
    fecha_entrega = models.DateField(verbose_name="Fecha de Entrega")
    fecha_solicitud = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Solicitud")
    estado = models.CharField(
        max_length=10,
        choices=[('pendiente', 'Pendiente'), ('aceptada', 'Aceptada'), ('cancelada', 'Cancelada')],
        default='pendiente'
    )

    materiales = models.ManyToManyField(
        Material,
        through='SolicitudPedidoMaterial',
        related_name='solicitudes_pedido'
    )
    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs) 
        if not self.codigo_solicitud:
            prefijo = "001000"
            self.codigo_solicitud = f"{prefijo}{self.id_solicitud}"
        super().save(*args, **kwargs)

    def codigo_material(self):
        return ', '.join([material.codigo_material for material in self.materiales.all()])

    def descripcion_material(self):
        return ', '.join([material.descripcion for material in self.materiales.all()])

    def unidad_medida(self):
        return ', '.join([material.unidad_medida for material in self.materiales.all()])

    def centro(self):
        return ', '.join([material.centro for material in self.materiales.all()])

    def almacen(self):
        return ', '.join([material.almacen for material in self.materiales.all()])

    def GCp(self):
        return ', '.join([material.grupo_compras for material in self.materiales.all()])

    def precio_estandar(self):
        return sum([material.precio_estandar for material in self.materiales.all()])

    def OrgC(self):
        return ', '.join([material.organizacion_compras for material in self.materiales.all()])

    def precio_total(self):
        total = 0
   
        for material_solicitud in self.solicitudpedidomaterial_set.all():

            total += material_solicitud.cantidad * material_solicitud.material.precio_estandar
        return total

    def __str__(self):
        return f"Solicitud {self.id_solicitud} - {self.codigo_solicitud}"

    class Meta:
        verbose_name = "Solicitud de Pedido"
        verbose_name_plural = "Pedidos"

class SolicitudPedidoMaterial(models.Model):
    solicitud = models.ForeignKey(SolicitudPedido, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name="Cantidad")

    def __str__(self):
        return f"{self.material} - Cantidad: {self.cantidad}"

    class Meta:
        verbose_name = "Material de Solicitud"
        verbose_name_plural = "Materiales de Solicitud"