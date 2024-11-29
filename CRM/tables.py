
import django_tables2 as tables
from .models import*


class ClienteTable(tables.Table):
    class Meta: 
        model = Cliente

class ActividadClienteTable(tables.Table):
    class Meta: 
        model = ActividadCliente

class VentaTable(tables.Table):
    class Meta: 
        model = Venta