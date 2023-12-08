from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Reserva(models.Model):
    nombre = models.CharField(max_length=80)
    telefono = models.CharField(max_length=15)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    cantidad_personas = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(15)])
    correo_electronico = models.EmailField()
    estado = models.CharField(max_length=20, choices=[
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ])
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
