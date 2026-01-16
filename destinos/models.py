from django.db import models

class Destino(models.Model):
    TIPO_CHOICES = [
        ('natural', 'Atracción Natural'),
        ('cultural', 'Sitio Cultural'),
        ('historico', 'Sitio Histórico'),
        ('gastronomico', 'Gastronomía'),
    ]
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=300)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    imagen = models.ImageField(upload_to='destinos/', null=True, blank=True)
    horario = models.CharField(max_length=100)
    precio_aprox = models.DecimalField(max_digits=10, decimal_places=2)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre