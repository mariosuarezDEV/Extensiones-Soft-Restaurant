from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    ChequesSerializer,
    CheqdetSerializer,
    ChequespagosSerializer,
    FoliosfacturadosSerializer,
    FacturasSerializer,
    TempchequesSerializer,
)
from .models import (
    Cheques,
    Cheqdet,
    Chequespagos,
    Productos,
    Productosdetalle,
    Foliosfacturados,
    Facturas,
    Tempcheques,
)
import random
from datetime import timedelta, datetime, date
from django.utils import timezone
from rest_framework import status
from .scripts import get_sustituno


@api_view(["GET"])
def listar_ventas(request):
    # Obtener fecha del query param
    fecha = request.query_params.get("fecha", None)
    if not fecha:
        return Response({"error": "Fecha no proporcionada, prueba con: ?fecha=2026-12-31"}, status=400)

    # Obtener de la base de datos
    cheques = Cheques.objects.filter(fecha__date=fecha)
    serializer = ChequesSerializer(cheques, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def auditoria(request, folio: int):
    # Query de los modelos
    venta = Cheques.objects.get(numcheque=folio)
    cheqdet = Cheqdet.objects.filter(foliodet=venta.folio)
    chequespagos = Chequespagos.objects.filter(folio=venta.folio)
    # Buscar si el folio ya fue facturado en foliosfacturados
    folios_facturados = Foliosfacturados.objects.filter(folio=venta.folio).first()
    factura = (
        Facturas.objects.get(idfactura=folios_facturados.idfactura)
        if folios_facturados
        else None
    )
    # Serializar los datos
    venta_serializer = ChequesSerializer(venta)
    cheqdet_serializer = CheqdetSerializer(cheqdet, many=True)
    pagos_serializer = ChequespagosSerializer(chequespagos, many=True)
    factura_serializer = FacturasSerializer(factura) if factura else None
    # Combinar los datos
    data = {
        "Venta": venta_serializer.data,
        "Consumo": cheqdet_serializer.data,
        "Pago": pagos_serializer.data,
        "Factura": factura_serializer.data if factura_serializer else None,
    }

    return Response(data)

@api_view(["GET"])
def detalle_venta(request, folio: int):
    # Query de los modelos
    venta = Cheques.objects.get(folio=folio)
    cheqdet = Cheqdet.objects.filter(foliodet=venta.folio)
    chequespagos = Chequespagos.objects.filter(folio=venta.folio)
    # Buscar si el folio ya fue facturado en foliosfacturados
    folios_facturados = Foliosfacturados.objects.filter(folio=venta.folio).first()
    factura = (
        Facturas.objects.get(idfactura=folios_facturados.idfactura)
        if folios_facturados
        else None
    )
    # Serializar los datos
    venta_serializer = ChequesSerializer(venta)
    cheqdet_serializer = CheqdetSerializer(cheqdet, many=True)
    pagos_serializer = ChequespagosSerializer(chequespagos, many=True)
    factura_serializer = FacturasSerializer(factura) if factura else None
    # Combinar los datos
    data = {
        "Venta": venta_serializer.data,
        "Consumo": cheqdet_serializer.data,
        "Pago": pagos_serializer.data,
        "Factura": factura_serializer.data if factura_serializer else None,
    }

    return Response(data)


@api_view(["POST"])
def ajuste_folio(request, folio: int):
    # TODO - Obtener el cheque, chequedet y chequespagos
    cheque = Cheques.objects.filter(folio=folio)

    producto_info, cantidad = get_sustituno()
    """
    producto_info -> id, precio, preciosinimpuestos, categoria (otros, bebidas)
    cantidad -> int
    """

    fecha = cheque.first().fecha if cheque.exists() else None
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
        subtotal=producto_info['preciosinimpuestos'] * cantidad,
        subtotalsinimpuestos= None, # En la BD es nullable, se puede dejar como None
        total=producto_info['precio'] * cantidad,
        totalconpropina=producto_info['precio'] * cantidad,
        totalimpuesto1=(producto_info['precio'] * cantidad) - (producto_info['preciosinimpuestos'] * cantidad),
        cargo=0,
        totalconcargo=producto_info['precio'] * cantidad,
        totalconpropinacargo=producto_info['precio'] * cantidad,
        descuentoimporte=0,
        efectivo=producto_info['precio'] * cantidad,
        tarjeta=0,
        vales=0,
        otros=0,
        propina=0,
        propinatarjeta=0,
        totalsindescuento=producto_info['preciosinimpuestos'] * cantidad,
        totalalimentos=0,
        totalbebidas= producto_info['preciosinimpuestos'] * cantidad if producto_info['categoria'] == 'bebidas' else 0,
        totalotros=producto_info['preciosinimpuestos'] * cantidad if producto_info['categoria'] == 'otros' else 0,
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
        totalbebidassindescuentos= producto_info['preciosinimpuestos'] * cantidad if producto_info['categoria'] == 'bebidas' else 0,
        totalotrossindescuentos=producto_info['preciosinimpuestos'] * cantidad if producto_info['categoria'] == 'otros' else 0,
        descuentocriterio=0,
        subtotalcondescuento=producto_info['preciosinimpuestos'] * cantidad,
        totalimpuestod1=producto_info['preciosinimpuestos'] * cantidad,
        totalsindescuentoimp=0.00,
    )

    movimientos = Cheqdet.objects.filter(foliodet=folio)
    primer_movimiento = movimientos.first()
    movimientos.exclude(movimiento=primer_movimiento.movimiento).delete()

    Cheqdet.objects.filter(foliodet=folio).update(
        movimiento=1,
        cantidad=cantidad,
        idproducto=producto_info['id'],
        descuento=0,
        precio=producto_info['precio'],
        impuesto1= producto_info['impuesto'],
        preciosinimpuestos=producto_info['preciosinimpuestos'],
        comentario="",
        usuariodescuento="",
        comentariodescuento="",
        idtipodescuento=0,
        idproductocompuesto="",
        productocompuestoprincipal=False,
        preciocatalogo=producto_info['precio'],
        idcortesia="",
    )

    Chequespagos.objects.filter(folio=folio).update(
        importe=producto_info['precio'] * cantidad, propina=0, tipodecambio=1
    )

    return Response(
        {"Mensaje": f"Folio: {folio} ajustado por: {producto_info['id']} - ${producto_info['precio'] * cantidad} - #{cantidad}"}, status=status.HTTP_200_OK
    )


@api_view(["GET"])
def listar_tempcheques(request):
    # obtener fecha actual del servidor
    fecha = timezone.now().date()
    print(fecha)
    tempcheques = Tempcheques.objects.filter(fecha__date=fecha)
    serializer = TempchequesSerializer(tempcheques, many=True)
    return Response(serializer.data)
