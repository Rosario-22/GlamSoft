from django.db import models

class Turno(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    servicio = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.nombre_cliente} - {self.servicio} ({self.fecha} {self.hora})"


# Create your models here.
