import django_tables2 as tables
from .models import*


class MaterialTable(tables.Table):
    class Meta: 
        model = Material

