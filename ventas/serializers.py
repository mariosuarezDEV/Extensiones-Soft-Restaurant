from rest_framework import serializers

# Modelos
from .models import Cheques


class ChequesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheques
        fields = "__all__"
