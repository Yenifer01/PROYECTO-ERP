from django.contrib import admin

# Register your models here.
from .models import *
from .tables import *
from .views import*
from .forms import*

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id_cliente', 'nombre', 'email', 'telefono', 'fecha_registro', 'estado']
    search_fields = ['nombre', 'email']
    list_filter = ['estado', 'fecha_registro']

@admin.register(ActividadCliente)
class ActividadClienteAdmin(admin.ModelAdmin):
    list_display = ['id_interaccion', 'cliente', 'fecha', 'tipo', 'descripcion', 'estado']
    search_fields = ['cliente__nombre', 'tipo']
    list_filter = ['tipo', 'estado', 'fecha']
    
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['id_venta', 'cliente', 'producto', 'cantidad', 'precio', 'fecha_venta', 'estado']
    search_fields = ['cliente__nombre', 'producto']
    list_filter = ['estado', 'fecha_venta']
