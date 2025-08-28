from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ChequesSerializer, CheqdetSerializer, ChequespagosSerializer
from .models import Cheques, Cheqdet, Chequespagos, Productos, Productosdetalle
from django.core.cache import cache
import random
from datetime import timedelta


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


@api_view(["GET"])
def detalle_venta(request, folio: int):
    # Generar key para el cache
    cache_key = f"detalle_venta_{folio}"

    # Intentar obtener datos del cache
    cached_data = cache.get(cache_key)
    if cached_data is not None:
        return Response(cached_data)

    # Query de los modelos
    venta = Cheques.objects.get(folio=folio)
    cheqdet = Cheqdet.objects.filter(foliodet=folio)
    chequespagos = Chequespagos.objects.filter(folio=folio)

    # Serializar los datos
    venta_serializer = ChequesSerializer(venta)
    cheqdet_serializer = CheqdetSerializer(cheqdet, many=True)
    pagos_serializer = ChequespagosSerializer(chequespagos, many=True)
    # Combinar los datos
    data = {
        "Venta": venta_serializer.data,
        "Consumo": cheqdet_serializer.data,
        "Pago": pagos_serializer.data,
    }

    # Guardar en cache por 24 horas (86400 segundos)
    cache.set(cache_key, data, timeout=86400)

    return Response(data)


@api_view(["POST"])
def ajuste_folio(request, folio: int):
    # TODO - Obtener el cheque, chequedet y chequespagos
    cheque = Cheques.objects.get(folio=folio)

    # Definir productos
    productos: dict[str, str] = {
        "cafe": "V-034003",
        "pan": "042035",
    }

    # Escoger producto al azar
    prod_key = random.choice(list(productos.keys()))

    # TODO - Obtener información del producto en productos y productodetalle
    producto_info = Productos.objects.get(idproducto=productos[prod_key])
    producto_detalle = Productosdetalle.objects.filter(idproducto=productos[prod_key])

    fecha = cheque.first().fecha if cheque.exists() else None
    cantidad = 1
    # TODO - Actualizar información
    cheque.update(
        cierre=fecha + timedelta(minutes=3),
        mesa="P/LL",
        nopersonas=1,
        cambio=0,
        descuento=0,
        cambiorepartidor=0,
        usuariodescuento="",
        idtipodescuento=0,
        propinapagada=0,
        propinafoliomovtocaja=0,
        propinaincluida=0,
        propinamanual=0,
        totalarticulos=cantidad,
        subtotal=producto_detalle.preciosinimpuestos * cantidad,
        subtotalsinimpuestos=producto_detalle.preciosinimpuestos * cantidad,
        total=producto_detalle.precio * cantidad,
        totalconpropina=producto_detalle.precio * cantidad,
        totalimpuesto1=producto_detalle.precio * cantidad,
        cargo=0,
        totalconcargo=producto_detalle.precio * cantidad,
        totalconpropinacargo=producto_detalle.precio * cantidad,
        descuentoimporte=0,
        efectivo=producto_detalle.precio * cantidad,
        tarjeta=0,
        vales=0,
        otros=0,
        propina=0,
        propinatarjeta=0,
        totalsindescuento=producto_detalle.precio * cantidad,
        totalalimentos=0,
        totalbebidas=0,
        totalotros=producto_detalle.precio * cantidad,
        totaldescuentos=0,
        totaldescuentoalimentos=0,
        totaldescuentobebidas=0,
        totaldescuentootros=0,
        totalcortesias=0,
        totalcortesiaalimentos=0,
        totalcortesiabebidas=0,
        totalcortesiaotros=0,
        totaldescuentoycortesia=0,
        totalalimentossindescuentos=0,
        totalbebidassindescuentos=0,
        totalotrossindescuentos=producto_detalle.precio * cantidad,
        descuentocriterio=0,
        subtotalcondescuento=producto_detalle.precio * cantidad,
        totalimpuestod1=producto_detalle.precio * cantidad,
        totalsindescuentoimp=producto_detalle.precio * cantidad,
    )

    # TODO - Cambiar la información en los detalles de la venta
    movimientos = Cheqdet.objects.filter(foliodet=folio)
    primer_movimiento = movimientos.first()
    movimientos.exclude(movimiento=primer_movimiento.movimiento).delete()

    chequedet = Cheqdet.objects.filter(foliodet=folio).update(
        movimiento=1,
        cantidad=cantidad,
        idproducto=producto_info.idproducto,
        descuento=0,
        precio=producto_detalle.precio,
        impuesto1=producto_detalle.impuesto1,
        preciosinimpuestos=producto_detalle.preciosinimpuestos,
        comentario="",
        usuariodescuento="",
        comentariodescuento="",
        idtipodescuento=0,
        idproductocompuesto="",
        productocompuestoprincipal=False,
        preciocatalogo=producto_detalle.precio,
        idcortesia="",
    )

    # TODO - Cambiar las formas de pago
    chequespagos = Chequespagos.objects.filter(folio=folio).update(
        importe=producto_detalle.precio * cantidad, propina=0, tipodecambio=1
    )

    # TODO - Serializar solo para prueba
    cheque_serializer = ChequesSerializer(cheque)
    chequedet_serializer = CheqdetSerializer(chequedet, many=True)
    chequespagos_serializer = ChequespagosSerializer(chequespagos, many=True)

    # TODO - Mostrar la información
    return Response(
        {
            "cheque": cheque_serializer.data,
            "chequedet": chequedet_serializer.data,
            "chequespagos": chequespagos_serializer.data,
        }
    )
