from rest_framework import viewsets
from .serializers import ChequesSerializer
from .models import Cheques
from .filters import ChequesFilter

class ChequesViewSet(viewsets.ModelViewSet):
    queryset = Cheques.objects.all().order_by('-fecha')
    serializer_class = ChequesSerializer
    filterset_class = ChequesFilter