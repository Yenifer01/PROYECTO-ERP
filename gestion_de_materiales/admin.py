
from django.contrib import admin
from .models import *
from .tables import *
from .views import*
from .forms import*

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['codigo_material', 'descripcion', 'tipo_material', 'unidad_medida', 'precio_estandar', 'peso_bruto','centro','grupo_compras','organizacion_compras','almacen', 'fecha_creacion','estado']
    search_fields = ['descripcion', 'tipo_material']
    list_filter = ['tipo_material', 'estado']

    