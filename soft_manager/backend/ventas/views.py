from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    ChequesSerializer,
    CheqdetSerializer,
    ChequespagosSerializer,
    FoliosfacturadosSerializer,
    FacturasSerializer,
)
from .models import (
    Cheques,
    Cheqdet,
    Chequespagos,
    Productos,
    Productosdetalle,
    Foliosfacturados,
    Facturas,
)
import random
from datetime import timedelta
from rest_framework import status


@api_view(["GET"])
def listar_ventas(request):
    # Obtener fecha del query param
    fecha = request.query_params.get("fecha", None)
    if not fecha:
        return Response({"error": "Fecha no proporcionada"}, status=400)

    # Obtener de la base de datos
    cheques = Cheques.objects.filter(fecha__date=fecha)
    serializer = ChequesSerializer(cheques, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def detalle_venta(request, folio: int):
    # Query de los modelos
    venta = Cheques.objects.get(folio=folio)
    cheqdet = Cheqdet.objects.filter(foliodet=folio)
    chequespagos = Chequespagos.objects.filter(folio=folio)
    # Buscar si el folio ya fue facturado en foliosfacturados
    folio_facturado = Foliosfacturados.objects.filter(folio=folio).first()
    if folio_facturado:
        factura_encontrada = Facturas.objects.get(idfactura=folio_facturado.idfactura)
        print("Factura encontrada:", factura_encontrada)

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

    return Response(data)


@api_view(["POST"])
def ajuste_folio(request, folio: int):
    # TODO - Obtener el cheque, chequedet y chequespagos
    cheque = Cheques.objects.filter(folio=folio)

    # Definir productos
    productos: dict[str, str] = {
        "cafe": "V-034003",
        "pan": "042035",
    }

    # Escoger producto al azar
    prod_key = random.choice(list(productos.keys()))
    cantidad = 1

    # TODO - Obtener información del producto en productos y productodetalle
    producto_info = Productos.objects.get(idproducto=productos[prod_key])
    producto_detalle = Productosdetalle.objects.get(idproducto=producto_info.idproducto)

    fecha = cheque.first().fecha if cheque.exists() else None
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

    Cheqdet.objects.filter(foliodet=folio).update(
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
    Chequespagos.objects.filter(folio=folio).update(
        importe=producto_detalle.precio * cantidad, propina=0, tipodecambio=1
    )

    # TODO - Mostrar la información
    return Response(
        {"Mensaje": "Venta ajustada correctamente"}, status=status.HTTP_200_OK
    )
