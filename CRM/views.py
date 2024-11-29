from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Cliente, ActividadCliente, Venta
from .serializers import ClienteSerializer, ActividadClienteSerializer, VentaSerializer

# Vistas para Cliente
class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Vistas para ActividadCliente
class ActividadClienteListCreateView(generics.ListCreateAPIView):
    queryset = ActividadCliente.objects.all()
    serializer_class = ActividadClienteSerializer

class ActividadClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActividadCliente.objects.all()
    serializer_class = ActividadClienteSerializer

# Vistas para Venta
class VentaListCreateView(generics.ListCreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class VentaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
