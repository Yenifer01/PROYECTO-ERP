from django.urls import path
from .views import *

urlpatterns = [
    # Rutas para Cliente
    path('clientes/', ClienteListCreateView.as_view(), name='Lista-Cliente-Create'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='Cliente-Detalle'),

    # Rutas para ActividadCliente
    path('actividades/', ActividadClienteListCreateView.as_view(), name='Lista-Actividad-Create'),
    path('actividades/<int:pk>/', ActividadClienteDetailView.as_view(), name='Actividad-Detalle'),

    # Rutas para Venta
    path('ventas/', VentaListCreateView.as_view(), name='Lista-Venta-Create'),
    path('ventas/<int:pk>/', VentaDetailView.as_view(), name='Venta-Detalle'),
]