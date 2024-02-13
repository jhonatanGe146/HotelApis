from .models import Factura,DetallesFactura,MetodoPago
from rest_framework import viewsets
from .serializer import FacturaSerializer,DetallesFacturaSerializer,MetodosPagoSerializer

# Create your views here.
class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer


class DetallesFacturaHabitacionViewSet(viewsets.ModelViewSet):
    queryset = DetallesFactura.objects.all()
    serializer_class = DetallesFacturaSerializer

class MetodosPagoHabitacionViewSet(viewsets.ModelViewSet):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodosPagoSerializer
