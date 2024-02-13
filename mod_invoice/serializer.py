from rest_framework import serializers
from .models import Factura,DetallesFactura,MetodoPago

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = "__all__"

class DetallesFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallesFactura
        fields = "__all__"

class MetodosPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = "__all__"

