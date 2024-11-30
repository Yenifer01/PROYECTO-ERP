
from django.urls import path
from .views import *

urlpatterns = [
    path('solicitud/', SolicitudPedidoListCreateView.as_view(), name='solicitud-list-create'),
    path('solicitud/<int:pk>/', SolicitudPedidoDetailView.as_view(), name='solicitud-detail'),

]
