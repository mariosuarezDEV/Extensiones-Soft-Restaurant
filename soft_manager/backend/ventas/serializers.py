from rest_framework import serializers

from .models import Cheques


class ChequesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheques
        fields = ["folio", "numcheque", "fecha", "cierre", "mesa", "facturado", "total", "efectivo", "tarjeta", "otros"]
