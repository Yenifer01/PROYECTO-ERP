from rest_framework import serializers
from .models import*

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['codigo_material', 'descripcion']  

class SolicitudPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudPedido
        fields = '__all__'

    def create(self, validated_data):

        materiales_data = validated_data.pop('material')
        
        solicitud_pedido = SolicitudPedido.objects.create(**validated_data)
        
        materiales = Material.objects.filter(codigo_material__in=[material['codigo_material'] for material in materiales_data])
        

        solicitud_pedido.material.set(materiales)  
        
        return solicitud_pedido

    def update(self, instance, validated_data):
        materiales_data = validated_data.pop('material')
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
    
        materiales = Material.objects.filter(codigo_material__in=[material['codigo_material'] for material in materiales_data])
    
        instance.material.set(materiales)  
        
        instance.save()
        return instance
    
class SolicitudPedidoMaterialSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()  

    class Meta:
        model = SolicitudPedidoMaterial
        fields = ['material', 'cantidad'] 