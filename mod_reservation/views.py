from .models import Reserva,huespedxreserva,habitacionxreserva
from rest_framework import viewsets
from .serializer import ReservaSerializer,HuespedxReservaSerializer, HabitacionxReservaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


class HuespedxReservaViewSet(viewsets.ModelViewSet):
    queryset = huespedxreserva.objects.all()
    serializer_class = HuespedxReservaSerializer

class HabitacionxReservaViewSet(viewsets.ModelViewSet):
    queryset = habitacionxreserva.objects.all()
    serializer_class = HabitacionxReservaSerializer


