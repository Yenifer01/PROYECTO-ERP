import django_tables2 as tables
from .models import SolicitudPedido

class SolicitudPedidoTable(tables.Table):
    materiales_detalles = tables.Column(
        accessor='material.all', 
        verbose_name='Materiales'
    )

    def render_materiales_detalles(self, record):
        materiales = record.material.all()  
        if not materiales:
            return "No hay materiales asociados"
        return ', '.join([f'{material.codigo_material} ({material.descripcion})' for material in materiales])

    class Meta:
        model = SolicitudPedido
        fields = ('codigo_solicitud', 'tipo_solicitud', 'materiales_detalles', 'cantidad', 'fecha_entrega', 'fecha_solicitud', 'estado')
