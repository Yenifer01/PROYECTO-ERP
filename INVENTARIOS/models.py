# from django.db import models

# # Create your models here.

# class Producto(models.Model):
#     id_producto = models.AutoField(primary_key=True)
#     codigo = models.CharField(max_length=50, unique=True)
#     nombre = models.CharField(max_length=255)
#     descripcion = models.TextField(blank=True, null=True)
#     precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
#     cantidad_disponible = models.IntegerField()
#     estado = models.BooleanField(default=True)  

#     def __str__(self):
#         return self.nombre
    
#     class Meta:
#         verbose_name_plural = "Productos"


# class MovimientoInventario(models.Model):
#     id_movimiento = models.AutoField(primary_key=True)
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     tipo = models.CharField(max_length=50, choices=[('Entrada', 'Entrada'), ('Salida', 'Salida')])
#     cantidad = models.IntegerField()
#     fecha = models.DateTimeField(auto_now_add=True)
#     estado = models.BooleanField(default=True)  

#     def __str__(self):
#         return f"Movimiento de {self.producto.nombre} - {self.tipo}"
    
#     class Meta:
#         verbose_name_plural = "Movimientos de Inventario"