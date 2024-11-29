from django import forms
from .models import Cliente, ActividadCliente, Venta

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Cliente.objects.filter(email=email).exclude(id_cliente=self.instance.id_cliente).exists():
            raise forms.ValidationError("Ya existe un cliente registrado con este correo electrónico.")
        return email

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError("El nombre no puede estar vacío.")
        return nombre
    

class ActividadClienteForm(forms.ModelForm):
    class Meta:
        model = ActividadCliente
        fields = '__all__'

    def clean_tipo(self):
        tipo = self.cleaned_data.get('tipo')
        if tipo not in ['Llamada', 'Email', 'Reunión']:
            raise forms.ValidationError("Tipo de interacción no válido.")
        return tipo

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if len(descripcion) < 10:
            raise forms.ValidationError("La descripción debe tener al menos 10 caracteres.")
        return descripcion


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad <= 0:
            raise forms.ValidationError("La cantidad debe ser mayor a cero.")
        return cantidad

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor a cero.")
        return precio
