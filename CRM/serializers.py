
from rest_framework import serializers
from .models import Cliente, ActividadCliente, Venta

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        exclude = ('estado',)

class ActividadClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActividadCliente
        exclude = ('estado',)

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        exclude = ('estado',)