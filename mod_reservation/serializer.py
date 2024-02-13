from rest_framework import serializers
from .models import Reserva,huespedxreserva,habitacionxreserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = "__all__"

class HuespedxReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = huespedxreserva
        fields = "__all__"

class HabitacionxReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = habitacionxreserva
        fields = "__all__"