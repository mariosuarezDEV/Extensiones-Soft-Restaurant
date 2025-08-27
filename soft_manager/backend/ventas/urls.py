from django.urls import path, include
from .views import listar_ventas
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path("api/", include(router.urls)),
    path("", listar_ventas, name="listar_ventas"),
]
