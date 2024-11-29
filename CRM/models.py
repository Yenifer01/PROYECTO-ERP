from django.db import models

# Create your models here.

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)  

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Clientes"

class ActividadCliente(models.Model):
    id_interaccion = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50, choices=[('Llamada', 'Llamada'), ('Email', 'Email'), ('Reunión', 'Reunión')])
    descripcion = models.TextField()
    estado = models.BooleanField(default=True) 

    def __str__(self):
        return f"Interacción con {self.cliente.nombre} - {self.tipo}"
    
    class Meta:
        verbose_name_plural = "Interacciones de Clientes"

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True) 

    def __str__(self):
        return f"Venta a {self.cliente.nombre} - {self.producto}"
    
    class Meta:
        verbose_name_plural = "Ventas"

