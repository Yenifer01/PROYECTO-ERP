from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import SolicitudPedido, SolicitudPedidoMaterial, Material

class SolicitudPedidoMaterialInline(admin.TabularInline):
    model = SolicitudPedidoMaterial
    extra = 1  
    fields = ('material', 'cantidad')
    raw_id_fields = ('material',)


@admin.register(SolicitudPedido)
class SolicitudPedidoAdmin(admin.ModelAdmin):
    inlines = [SolicitudPedidoMaterialInline]
    list_display = [
        'codigo_solicitud', 'tipo_solicitud', 'mostrar_materiales', 'cantidad',
        'unidad_medida', 'centro', 'almacen', 'GCp',
        'precio_estandar', 'precio_total', 'OrgC',
        'fecha_solicitud', 'fecha_entrega', 'estado'
    ]
    search_fields = ['codigo_solicitud', 'tipo_solicitud']
    
    def mostrar_materiales(self, obj):
        materiales = obj.materiales.all()
        return ", ".join([str(material.codigo_material) for material in materiales])
    mostrar_materiales.short_description = 'Materiales'

    def cantidad(self, obj):
        return ", ".join([str(item.cantidad) for item in obj.solicitudpedidomaterial_set.all()])
    cantidad.short_description = 'Cantidades'

    def save_model(self, request, obj, form, change):
        if SolicitudPedido.objects.filter(codigo_solicitud=obj.codigo_solicitud).exclude(pk=obj.pk).exists():
            self.message_user(
                request,
                'No se insertó la solicitud porque ya existe una solicitud con el mismo código.',
                level='error'
            )
        else:
            super().save_model(request, obj, form, change)
  
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('materiales') 
        return queryset