from django.urls import path, include
from .views import listar_ventas, detalle_venta, ajuste_folio, listar_tempcheques
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path("api/", include(router.urls)),
    path("", listar_ventas, name="listar_ventas"),
    path("<int:folio>", detalle_venta, name="detalle_venta"),
    path("ajuste/<int:folio>", ajuste_folio, name="ajuste_folio"),
    path("actuales/", listar_tempcheques, name="listar_tempcheques"),
]
