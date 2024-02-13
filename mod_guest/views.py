from .models import Huesped
from rest_framework import viewsets
from .serializer import HuespedSerializer

class HuespedViewSet(viewsets.ModelViewSet):
    queryset = Huesped.objects.all()
    serializer_class = HuespedSerializer


