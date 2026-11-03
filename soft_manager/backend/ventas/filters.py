import django_filters
from django_filters import rest_framework as filters
from .models import Cheques

class ChequesFilter(filters.FilterSet):
    fecha = django_filters.DateFilter(field_name='fecha', lookup_expr='date')
    class Meta:
        model = Cheques
        fields = ['folio', 'numcheque', 'fecha', 'cierre', 'mesa', 'facturado', 'total', 'efectivo', 'tarjeta', 'otros']