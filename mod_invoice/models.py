from django.db import models
from mod_user.models import persona
from mod_service.models import productos


class detalles_factura(models.Model):
    IDDETALLESFACTURA = models.AutoField(primary_key=True)
    CANTIDAD = models.IntegerField()
    
    
    def __str__(self):
        return str(self.fecha_emision)

class metodo_pago(models.Model):
    IDMETODOPAGO = models.AutoField(primary_key=True)
    METODO = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.METODO

class factura(models.Model):
    id_metodoPago = models.ForeignKey(metodo_pago, on_delete=models.CASCADE)
    id_detalleFactura = models.ForeignKey(detalles_factura, on_delete=models.CASCADE)
    numero_documento = models.ForeignKey(persona, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_metodoPago)