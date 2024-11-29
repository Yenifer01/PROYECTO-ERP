from django.db import models

class Material(models.Model):
    codigo_material = models.AutoField(primary_key=True, verbose_name="Código del Material")
    descripcion = models.CharField(max_length=255, verbose_name="Descripción")

    TIPO_MATERIAL_CHOICES = [
        ('FERT', 'Producto Terminado'),
        ('MP', 'Materia Prima'),
        ('HALB', 'Productos Semi-Elaborados'),
        ('VERP', 'Material de Empaque'),
        ('ERSA', 'Piezas de Repuesto')
    ]
    tipo_material = models.CharField(max_length=25, choices=TIPO_MATERIAL_CHOICES, verbose_name="Tipo de Material")
    unidad_medida = models.CharField(max_length=20, verbose_name="Unidad de Medida")
    precio_estandar = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Estándar")
    peso_bruto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Peso Bruto")
    
    CENTRO_CHOICES = [
        ('1000','1000'),
        ('1001','1001'),
        ('1002','1002'),
    ]
    centro = models.CharField(max_length=4, choices=CENTRO_CHOICES, verbose_name="Centro")

    GRUPO_COMPRAS_CHOICES = [
        ('001','001'),
        ('002','002'),
        ('003','003'),
    ]
    grupo_compras = models.CharField(max_length=3, choices=GRUPO_COMPRAS_CHOICES, verbose_name="GCp")

    ORGANIZACION_COMPRAS_CHOICES = [
        ('0001','0001'),
        ('0002','0002'),
        ('0003','0003'),
    ]
    organizacion_compras = models.CharField(max_length=4, choices=ORGANIZACION_COMPRAS_CHOICES, verbose_name="OrgC")

    ALMACEN_CHOICES = [
        ('A01','A01'),
        ('A02','A01'),
    ]
    almacen = models.CharField(max_length=3, choices=ALMACEN_CHOICES, verbose_name="Almacén")

    def __str__(self):
        return f"{self.codigo_material} - {self.descripcion}"

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"
        ordering = ['descripcion']

    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    estado = models.BooleanField(default=True, verbose_name="Estado")

    