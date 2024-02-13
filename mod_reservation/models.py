from django.db import models
from mod_user.models import persona
from mod_guest.models import huesped
from mod_room.models import habitacion

# Create your models here.
class reserva(models.Model):
    IDRESERVA = models.AutoField(primary_key=True)
    FECHA_RESERVACION = models.DateField(null=False)
    FECHA_ENTRADA = models.DateField(null=False)
    HORA_ENTRADA = models.TimeField(null=True)
    FECHA_SALIDA = models.DateField(null=False)
    HORA_SALIDA = models.TimeField(null=True)
    PRECIO_CALCULADO= models.DecimalField(max_digits=10, decimal_places=2, null=False)
    CANTIDAD_ADULTOS = models.IntegerField()
    CANTIDAD_NINOS = models.IntegerField()
    PERSONA_NRODOCUMENTO = models.ForeignKey(persona, on_delete=models.CASCADE)
  
    def __str__(self):
      return self.PERSONA_NRODOCUMENTO.NOMBRE  
    
class huesped_reserva(models.Model):
    ID_HUESPED_RESERVA = models.AutoField(primary_key=True)
    HUESPED_IDHUESPED = models.ForeignKey(
        huesped, 
        on_delete=models.CASCADE,
        )
    RESERVA_IDRESERVA = models.ForeignKey(
        reserva, 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return (f'{self.HUESPED_IDHUESPED} --> {self.RESERVA_IDRESERVA}')
  
class habitacion_reserva(models.Model):
    ID_HABITACION_RESERVA = models.AutoField(primary_key=True)
    HABITACION_NROHABITACION = models.ForeignKey(
        habitacion, 
        on_delete=models.CASCADE,
        )
    RESERVA_IDRESERVA = models.ForeignKey(
        reserva, 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return (f'{self.HABITACION_NROHABITACION} --> {self.RESERVA_IDRESERVA}')