from djongo import models

class Servicio(models.Model):
    CATEGORIA_CHOICES = [
        ('hotel', 'Hotel'),
        ('restaurante', 'Restaurante'),
        ('tour', 'Tour Guiado'),
        ('transporte', 'Transporte'),
    ]
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=300)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    precio_rango = models.CharField(max_length=100)
    calificacion = models.FloatField(default=0)
    imagen = models.ImageField(upload_to='servicios/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"
