from djongo import models

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    lugar = models.CharField(max_length=200)
    organizador = models.CharField(max_length=100)
    costo = models.CharField(max_length=50)  # Gratuito/Pago
    imagen = models.ImageField(upload_to='eventos/', null=True, blank=True)

    def __str__(self):
        return self.nombre
