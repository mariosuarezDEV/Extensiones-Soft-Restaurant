from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ChequesViewSet

router = DefaultRouter()
router.register(r"cheques", ChequesViewSet, basename="cheques")

urlpatterns = [
    path("api/", include(router.urls))
]
