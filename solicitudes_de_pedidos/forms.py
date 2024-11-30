from datetime import timezone
from django import forms
from .models import SolicitudPedido, Material

class SolicitudPedidoForm(forms.ModelForm):
    materiales = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,  
        label="Materiales"
    )

    class Meta:
        model = SolicitudPedido
        fields = '__all__'

    def clean_codigo_solicitud(self):
      
        return self.cleaned_data.get('codigo_solicitud')

    def clean_fecha_entrega(self):
        fecha_entrega = self.cleaned_data.get('fecha_entrega')
    
        if fecha_entrega and fecha_entrega < timezone.now().date():  
            raise forms.ValidationError("La fecha de entrega no puede ser en el pasado.")
        
        return fecha_entrega

    def clean_estado(self):
        estado = self.cleaned_data.get('estado')
        
        if estado not in ['pendiente', 'aceptada', 'cancelada']:
            raise forms.ValidationError("Estado inválido. El estado debe ser pendiente, aceptada o cancelada.")
        
        return estado

    def clean_materiales(self):
        materiales = self.cleaned_data.get('materiales')
        if not materiales:
            raise forms.ValidationError("Debe seleccionar al menos un material.")
        
        if len(materiales) != len(set(materiales)):
            raise forms.ValidationError("No puede seleccionar materiales duplicados.")
        
        return materiales
