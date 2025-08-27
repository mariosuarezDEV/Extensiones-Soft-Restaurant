from django.urls import path, include
from .views import listar_ventas, detalle_venta
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path("api/", include(router.urls)),
    path("", listar_ventas, name="listar_ventas"),
    path("<int:folio>", detalle_venta, name="detalle_venta"),
]
