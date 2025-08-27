from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ChequesSerializer
from .models import Cheques
from django.core.cache import cache


@api_view(["GET"])
def listar_ventas(request):
    # Obtener fecha del query param
    fecha = request.query_params.get("fecha", None)
    if not fecha:
        return Response({"error": "Fecha no proporcionada"}, status=400)

    # Generar key para el cache
    cache_key = f"ventas_{fecha}"

    # Intentar obtener datos del cache
    cached_data = cache.get(cache_key)
    if cached_data is not None:
        return Response(cached_data)

    # Si no está en cache, obtener de la base de datos
    cheques = Cheques.objects.filter(fecha__date=fecha)
    serializer = ChequesSerializer(cheques, many=True)

    # Guardar en cache por 24 horas (86400 segundos)
    cache.set(cache_key, serializer.data, timeout=86400)

    return Response(serializer.data)
