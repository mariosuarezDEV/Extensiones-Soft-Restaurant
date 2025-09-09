from rest_framework import serializers

from .models import Cheques, Cheqdet, Chequespagos, Facturas, Foliosfacturados


class ChequesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheques
        fields = [
            "folio",
            "numcheque",
            "fecha",
            "salidarepartidor",
            "cierre",
            "mesa",
            "nopersonas",
            "cambio",
            "descuento",
            "facturado",
            "cambiorepartidor",
            "usuariodescuento",
            "idtipodescuento",
            "propinapagada",
            "propinafoliomovtocaja",
            "propinaincluida",
            "propinamanual",
            "totalarticulos",
            "subtotal",
            "subtotalsinimpuestos",
            "total",
            "totalconpropina",
            "totalimpuesto1",
            "cargo",
            "totalconcargo",
            "totalconpropinacargo",
            "descuentoimporte",
            "efectivo",
            "tarjeta",
            "vales",
            "otros",
            "propina",
            "propinatarjeta",
            "totalsindescuento",
            "totalalimentos",
            "totalbebidas",
            "totalotros",
            "totaldescuentos",
            "totaldescuentoalimentos",
            "totaldescuentobebidas",
            "totaldescuentootros",
            "totalcortesias",
            "totalcortesiaalimentos",
            "totalcortesiabebidas",
            "totalcortesiaotros",
            "totaldescuentoycortesia",
            "totalalimentossindescuentos",
            "totalbebidassindescuentos",
            "totalotrossindescuentos",
            "descuentocriterio",
            "subtotalcondescuento",
            "totalimpuestod1",
            "totalcondonativo",
            "totalconpropinacargodonativo",
            "subtotal_ec",
            "total_ec",
            "totalconpropinacargo_ec",
            "totalsindescuentoimp",
        ]


class CheqdetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheqdet
        fields = [
            "foliodet",
            "movimiento",
            "cantidad",
            "idproducto",
            "descuento",
            "precio",
            "impuesto1",
            "preciosinimpuestos",
            "comentario",
            "usuariodescuento",
            "comentariodescuento",
            "idtipodescuento",
            "idproductocompuesto",
            "productocompuestoprincipal",
            "preciocatalogo",
            "idcortesia",
        ]


class ChequespagosSerializer(serializers.ModelSerializer):
    forma_pago = serializers.CharField(source="idformadepago", read_only=True)

    class Meta:
        model = Chequespagos
        fields = [
            "folio",
            "importe",
            "forma_pago",
            "idformadepago",
            "propina",
            "tipodecambio",
        ]


class FacturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facturas
        fields = ["idfactura", "serie", "folio", "fecha", "nota"]


class FoliosfacturadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foliosfacturados
        fields = "__all__"
