from django.db import models

class huesped(models.Model):
    IDHUESPED =  models.AutoField(primary_key=True)
    NRODOCUMENTO = models.CharField(max_length=10, primary_key=True)
    NOMBRE = models.CharField(max_length=70)
    APELLIDO = models.CharField(max_length=70)
    EMAIL = models.EmailField(unique=True)
    TELEFONO = models.CharField(max_length=15)

    def __str__(self):
        return (f'{self.NRODOCUMENTO} || {self.NOMBRE} || {self.APELLIDO}  ')