from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import SolicitudPedido
from .serializers import SolicitudPedidoSerializer
from django.db.models import Prefetch

class SolicitudPedidoListCreateView(generics.ListCreateAPIView):
    queryset = SolicitudPedido.objects.prefetch_related('material')  # Optimización con prefetch_related
    serializer_class = SolicitudPedidoSerializer

    def perform_create(self, serializer):
        # Validación de datos antes de guardar, por ejemplo, verificar que haya materiales seleccionados
        materiales = self.request.data.get('material')
        if not materiales:
            raise ValidationError("Debe seleccionar al menos un material.")
        
        # Guardar la solicitud de pedido
        serializer.save()

    def get_queryset(self):
        # Personalización de la queryset si es necesario
        # Si hay algún filtro en la URL o parámetros, los puedes manejar aquí
        return self.queryset


class SolicitudPedidoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SolicitudPedido.objects.prefetch_related('material')  # Optimización con prefetch_related
    serializer_class = SolicitudPedidoSerializer

    def perform_update(self, serializer):
        # Acción personalizada antes de actualizar
        materiales = self.request.data.get('material')
        if materiales:
            # Validar si los materiales son correctos antes de actualizar
            # Aquí podrías agregar lógica para verificar la validez de los materiales
            pass

        # Guardar la solicitud de pedido actualizada
        serializer.save()

    def perform_destroy(self, instance):
        # Acción personalizada antes de eliminar
        # Verificar si la solicitud tiene materiales asociados
        if instance.material.all():
            raise ValidationError("No se puede eliminar la solicitud de pedido porque tiene materiales asociados.")
        
        # Eliminar la solicitud
        instance.delete(), 