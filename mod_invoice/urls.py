from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'factura', views.FacturaViewSet)
router.register(r'detallesfac', views.DetallesFacturaHabitacionViewSet)
router.register(r'metodospago', views.MetodosPagoHabitacionViewSet)

urlpatterns = [
     path('', include(router.urls)),
     
]

