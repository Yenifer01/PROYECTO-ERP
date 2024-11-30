# from django.db import models
# from INVENTARIOS.models import*

# # Create your models here.
# class Proveedor(models.Model):
#     id_proveedor = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=255)
#     email = models.EmailField(blank=True, null=True)
#     telefono = models.CharField(max_length=20, blank=True, null=True)
#     direccion = models.TextField(blank=True, null=True)
#     fecha_registro = models.DateTimeField(auto_now_add=True)
#     estado = models.BooleanField(default=True) 

#     def __str__(self):
#         return self.nombre
    
#     class Meta:
#         verbose_name_plural = "Proveedores"

# class OrdenCompra(models.Model):
#     id_orden_compra = models.AutoField(primary_key=True)
#     proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
#     fecha_orden = models.DateTimeField(auto_now_add=True)
#     estado = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('Completada', 'Completada')])
#     total = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Orden de Compra {self.id_orden_compra} - {self.proveedor.nombre}"
    
#     class Meta:
#         verbose_name_plural = "Órdenes de Compra"

   
# class DetalleCompra(models.Model):
#     id_detalle_compra = models.AutoField(primary_key=True)
#     orden = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE)
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     cantidad = models.IntegerField()
#     precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Detalle de compra {self.producto.nombre} - {self.cantidad}"
    
#     class Meta:
#         verbose_name_plural = "Detalles de Compras"

