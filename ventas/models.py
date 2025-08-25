from django.db import models


# Modelo de empresa
class Empresas(models.Model):
    idempresa = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    razonsocial = models.CharField(max_length=200, blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    sucursal = models.CharField(max_length=250, blank=True, null=True)
    rfc = models.CharField(max_length=150, blank=True, null=True)
    curp = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=150, blank=True, null=True)
    giro = models.CharField(max_length=200, blank=True, null=True)
    contacto = models.CharField(max_length=200, blank=True, null=True)
    fax = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    fechacompra = models.DateTimeField(blank=True, null=True)
    distribuidor = models.CharField(max_length=250, blank=True, null=True)
    numerofactura = models.CharField(max_length=100, blank=True, null=True)
    numerodecontrol = models.CharField(max_length=200, blank=True, null=True)
    contrasenacontrol = models.CharField(max_length=150, blank=True, null=True)
    idhardware = models.CharField(max_length=150, blank=True, null=True)
    licenciaprincipal = models.CharField(max_length=150, blank=True, null=True)
    licenciamonederoelectronico = models.CharField(
        max_length=150, blank=True, null=True
    )
    licenciamonitorproduccion = models.CharField(max_length=150, blank=True, null=True)
    licenciasrmovil = models.CharField(max_length=150, blank=True, null=True)
    licenciamanttoventas = models.CharField(max_length=150, blank=True, null=True)
    licenciapagoenlinea = models.CharField(max_length=150, blank=True, null=True)
    licenciahuelladigital = models.CharField(max_length=150, blank=True, null=True)
    licenciabillar = models.CharField(max_length=150, blank=True, null=True)
    franquicia = models.BooleanField(blank=True, null=True)
    web = models.CharField(max_length=200, blank=True, null=True)
    ciudad = models.CharField(max_length=150, blank=True, null=True)
    estado = models.CharField(max_length=150, blank=True, null=True)
    pais = models.CharField(max_length=150, blank=True, null=True)
    ciudadsucursal = models.CharField(max_length=150, blank=True, null=True)
    estadosucursal = models.CharField(max_length=150, blank=True, null=True)
    passwordempresa = models.CharField(max_length=15, blank=True, null=True)
    escedis = models.BooleanField(blank=True, null=True)
    idproveedor = models.CharField(max_length=15, blank=True, null=True)
    escorporativo = models.BooleanField(blank=True, null=True)
    codigopostal = models.CharField(max_length=100, blank=True, null=True)
    ventapedidocedis = models.BooleanField(blank=True, null=True)
    descuentocedis = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    idtipoempresa = models.ForeignKey(
        "Tipoempresa",
        models.DO_NOTHING,
        db_column="idtipoempresa",
        blank=True,
        null=True,
    )
    idregionempresa = models.ForeignKey(
        "Regionempresa",
        models.DO_NOTHING,
        db_column="idregionempresa",
        blank=True,
        null=True,
    )
    idestado = models.ForeignKey(
        "Estados", models.DO_NOTHING, db_column="idestado", blank=True, null=True
    )
    idpais = models.ForeignKey(
        "Paises", models.DO_NOTHING, db_column="idpais", blank=True, null=True
    )
    claveunicaempresa = models.CharField(max_length=50, blank=True, null=True)
    regimen = models.CharField(max_length=100, blank=True, null=True)
    idempresahub = models.CharField(max_length=50, blank=True, null=True)
    logohub = models.BinaryField(blank=True, null=True)
    logoempresa = models.TextField()
    logoempresaext = models.CharField(max_length=10)
    prefijoempresa = models.CharField(max_length=3)
    a86ed5f9d02ec5b3 = models.CharField(max_length=250, blank=True, null=True)
    idplaza = models.CharField(max_length=15, blank=True, null=True)
    idcompania = models.CharField(max_length=15, blank=True, null=True)
    idubicacionempresa = models.CharField(max_length=15, blank=True, null=True)
    idzonaempresa = models.CharField(max_length=15, blank=True, null=True)
    asientos = models.IntegerField(blank=True, null=True)
    metroscuadrados = models.DecimalField(
        max_digits=12, decimal_places=3, blank=True, null=True
    )
    fechaapertura = models.CharField(max_length=10, blank=True, null=True)
    fechacierre = models.CharField(max_length=10, blank=True, null=True)
    fechamodificado = models.CharField(max_length=10, blank=True, null=True)
    imagen_logo_menu = models.TextField(blank=True, null=True)
    imagen_portada_menu = models.TextField(blank=True, null=True)
    eslogan = models.CharField(max_length=300)
    nombre_menu = models.CharField(max_length=300)
    codigopostalsucursal = models.CharField(max_length=100)
    idregimen_sat = models.CharField(
        db_column="idregimen_SAT", max_length=50
    )  # Field name made lowercase.
    uid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "empresas"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return f"Empresa {self.nombre} con id {self.id}"


# Modelo grupos
class Grupos(models.Model):
    idgrupo = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    clasificacion = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    prioridad = models.DecimalField(
        max_digits=4, decimal_places=0, blank=True, null=True
    )
    color = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    colorletra = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    prioridadimpresion = models.DecimalField(
        max_digits=4, decimal_places=0, blank=True, null=True
    )
    cambiacolorcuenta = models.BooleanField(blank=True, null=True)
    colorcuenta = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    colorletracuenta = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    solicitaautorizacion = models.BooleanField(blank=True, null=True)
    imagenmenuelectronico = models.BinaryField(blank=True, null=True)
    extmenu = models.CharField(max_length=5, blank=True, null=True)
    porcentajepropina = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    imagen_menu = models.TextField(blank=True, null=True)
    id_etiqueta = models.CharField(max_length=50)
    workspaceid = models.CharField(
        db_column="WorkspaceId", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    alcohol = models.BooleanField()
    servicecode = models.ForeignKey(
        "Servicecodes",
        models.DO_NOTHING,
        db_column="servicecode",
        blank=True,
        null=True,
    )
    idbo = models.IntegerField(
        db_column="IdBO", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "grupos"
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"

    def __str__(self):
        return f"Grupo {self.descripcion} con id {self.idgrupo}"


# Estados
class Estados(models.Model):
    idestado = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    idpais = models.ForeignKey(
        "Paises", models.DO_NOTHING, db_column="idpais", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "estados"
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __str__(self):
        return f"Estado {self.descripcion} con id {self.idestado}"


# Paises
class Paises(models.Model):
    idpais = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "paises"
        verbose_name = "Pais"
        verbose_name_plural = "Paises"


# Region empresa
class Regionempresa(models.Model):
    idregionempresa = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "regionempresa"
        verbose_name = "Region de la Empresa"
        verbose_name_plural = "Regiones de la Empresa"


# Tipo de empresa
class Tipoempresa(models.Model):
    idtipoempresa = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tipoempresa"
        verbose_name = "Tipo de Empresa"
        verbose_name_plural = "Tipos de Empresas"


# Codigos de servicio
class Servicecodes(models.Model):
    servicecode = models.CharField(primary_key=True, max_length=50)
    descripcion = models.CharField(max_length=200)
    sistema = models.SmallIntegerField()
    tipo = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = "servicecodes"
        verbose_name = "Codigo de Servicio"
        verbose_name_plural = "Codigos de Servicios"


# Uds medida
class Udsmedida(models.Model):
    idunidad = models.CharField(primary_key=True, max_length=50)
    idunidadmedida_sat = models.CharField(
        db_column="idunidadmedida_SAT", max_length=50
    )  # Field name made lowercase.
    workspaceid = models.CharField(
        db_column="WorkspaceId", max_length=36, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "udsmedida"
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medida"


# Cheques
class Cheques(models.Model):  # Importante
    folio = models.BigAutoField(primary_key=True)
    seriefolio = models.CharField(max_length=15, blank=True, null=True)
    numcheque = models.DecimalField(
        max_digits=8, decimal_places=0, blank=True, null=True
    )
    fecha = models.DateTimeField(blank=True, null=True)
    salidarepartidor = models.DateTimeField(blank=True, null=True)
    arriborepartidor = models.DateTimeField(blank=True, null=True)
    cierre = models.DateTimeField(blank=True, null=True)
    mesa = models.CharField(max_length=100, blank=True, null=True)
    nopersonas = models.DecimalField(
        max_digits=3, decimal_places=0, blank=True, null=True
    )
    idmesero = models.CharField(max_length=4, blank=True, null=True)
    pagado = models.BooleanField(blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    impreso = models.BooleanField(blank=True, null=True)
    impresiones = models.DecimalField(
        max_digits=6, decimal_places=0, blank=True, null=True
    )
    cambio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuento = models.DecimalField(
        max_digits=8, decimal_places=4, blank=True, null=True
    )
    reabiertas = models.DecimalField(
        max_digits=4, decimal_places=0, blank=True, null=True
    )
    razoncancelado = models.CharField(max_length=255, blank=True, null=True)
    orden = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    facturado = models.BooleanField(blank=True, null=True)
    idcliente = models.CharField(max_length=15, blank=True, null=True)
    idarearestaurant = models.CharField(max_length=5, blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    tipodeservicio = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    idturno = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    usuariocancelo = models.CharField(max_length=15, blank=True, null=True)
    comentariodescuento = models.CharField(max_length=60, blank=True, null=True)
    estacion = models.CharField(max_length=40, blank=True, null=True)
    cambiorepartidor = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    usuariodescuento = models.CharField(max_length=15, blank=True, null=True)
    fechacancelado = models.DateTimeField(blank=True, null=True)
    idtipodescuento = models.CharField(max_length=5, blank=True, null=True)
    numerotarjeta = models.CharField(max_length=30, blank=True, null=True)
    folionotadeconsumo = models.DecimalField(
        max_digits=8, decimal_places=0, blank=True, null=True
    )
    notadeconsumo = models.BooleanField(blank=True, null=True)
    propinapagada = models.BooleanField(blank=True, null=True)
    propinafoliomovtocaja = models.DecimalField(
        max_digits=8, decimal_places=0, blank=True, null=True
    )
    puntosmonederogenerados = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    propinaincluida = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    tarjetadescuento = models.CharField(max_length=30, blank=True, null=True)
    porcentajefac = models.DecimalField(
        max_digits=11, decimal_places=6, blank=True, null=True
    )
    usuariopago = models.CharField(max_length=15, blank=True, null=True)
    propinamanual = models.BooleanField(blank=True, null=True)
    observaciones = models.CharField(max_length=250, blank=True, null=True)
    idclientedomicilio = models.CharField(max_length=15, blank=True, null=True)
    iddireccion = models.CharField(max_length=15, blank=True, null=True)
    idclientefacturacion = models.CharField(max_length=15, blank=True, null=True)
    telefonousadodomicilio = models.CharField(max_length=50, blank=True, null=True)
    totalarticulos = models.DecimalField(
        max_digits=11, decimal_places=2, blank=True, null=True
    )
    subtotal = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    subtotalsinimpuestos = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalconpropina = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    totalimpuesto1 = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    cargo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    totalconcargo = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    totalconpropinacargo = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    descuentoimporte = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    efectivo = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    tarjeta = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    vales = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    otros = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    propina = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    propinatarjeta = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    campoadicional1 = models.CharField(max_length=250, blank=True, null=True)
    idreservacion = models.CharField(max_length=25, blank=True, null=True)
    idcomisionista = models.CharField(max_length=15, blank=True, null=True)
    importecomision = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    comisionpagada = models.BooleanField(blank=True, null=True)
    fechapagocomision = models.DateTimeField(blank=True, null=True)
    foliopagocomision = models.DecimalField(
        max_digits=8, decimal_places=0, blank=True, null=True
    )
    tipoventarapida = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    callcenter = models.BooleanField(blank=True, null=True)
    idordencompra = models.BigIntegerField(blank=True, null=True)
    totalsindescuento = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    totalalimentos = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    totalbebidas = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    totalotros = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    totaldescuentos = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    totaldescuentoalimentos = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    totaldescuentobebidas = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    totaldescuentootros = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    totalcortesias = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    totalcortesiaalimentos = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    totalcortesiabebidas = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    totalcortesiaotros = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    totaldescuentoycortesia = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    totalalimentossindescuentos = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    totalbebidassindescuentos = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    totalotrossindescuentos = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    descuentocriterio = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    descuentomonedero = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    idmenucomedor = models.CharField(max_length=15, blank=True, null=True)
    subtotalcondescuento = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    comisionpax = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    procesadointerfaz = models.BooleanField(blank=True, null=True)
    domicilioprogramado = models.BooleanField(blank=True, null=True)
    fechadomicilioprogramado = models.DateTimeField(blank=True, null=True)
    enviado = models.BooleanField(blank=True, null=True)
    ncf = models.CharField(max_length=19, blank=True, null=True)
    numerocuenta = models.CharField(max_length=100, blank=True, null=True)
    codigo_unico_af = models.CharField(max_length=30, blank=True, null=True)
    estatushub = models.IntegerField(blank=True, null=True)
    idfoliohub = models.DecimalField(
        max_digits=8, decimal_places=0, blank=True, null=True
    )
    enviadorw = models.BooleanField(
        db_column="EnviadoRW", blank=True, null=True
    )  # Field name made lowercase.
    usuarioapertura = models.CharField(max_length=15)
    titulartarjetamonedero = models.CharField(max_length=100, blank=True, null=True)
    saldoanteriormonedero = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    autorizacionfolio = models.CharField(max_length=50, blank=True, null=True)
    fechalimiteemision = models.DateTimeField(blank=True, null=True)
    totalimpuestod1 = models.DecimalField(max_digits=19, decimal_places=4)
    totalimpuestod2 = models.DecimalField(max_digits=19, decimal_places=4)
    totalimpuestod3 = models.DecimalField(max_digits=19, decimal_places=4)
    idmotivocancela = models.CharField(max_length=200, blank=True, null=True)
    sistema_envio = models.IntegerField()
    idformadepagodescuento = models.CharField(
        db_column="idformadepagoDescuento", max_length=5
    )  # Field name made lowercase.
    titulartarjetamonederodescuento = models.CharField(max_length=100)
    foliotempcheques = models.BigIntegerField(blank=True, null=True)
    c_iddispositivo = models.IntegerField()
    salerestaurantid = models.TextField()
    timemarktoconfirmed = models.DateTimeField(blank=True, null=True)
    timemarktodelivery = models.DateTimeField(blank=True, null=True)
    timemarktodeliveryarrive = models.DateTimeField(blank=True, null=True)
    esalestatus = models.IntegerField()
    statussr = models.IntegerField(db_column="statusSR")  # Field name made lowercase.
    paymentreference = models.CharField(max_length=50)
    deliverycharge = models.DecimalField(
        max_digits=6, decimal_places=5, blank=True, null=True
    )
    comandaimpresa = models.BooleanField(blank=True, null=True)
    foodorder = models.IntegerField()
    cashpaymentwith = models.DecimalField(max_digits=19, decimal_places=4)
    paymentmethod_id = models.IntegerField()
    surveycode = models.CharField(max_length=18)
    intentoenvioaf = models.IntegerField(
        db_column="intentoEnvioAF"
    )  # Field name made lowercase.
    tkc_token = models.CharField(
        db_column="TKC_Token", max_length=50
    )  # Field name made lowercase.
    tkc_transaction = models.CharField(
        db_column="TKC_Transaction", max_length=100
    )  # Field name made lowercase.
    tkc_authorization = models.CharField(
        db_column="TKC_Authorization", max_length=100
    )  # Field name made lowercase.
    tkc_cupon = models.CharField(
        db_column="TKC_Cupon", max_length=100
    )  # Field name made lowercase.
    tkc_expirationdate = models.CharField(
        db_column="TKC_ExpirationDate", max_length=100
    )  # Field name made lowercase.
    tkc_recompensa = models.DecimalField(
        db_column="TKC_Recompensa", max_digits=19, decimal_places=4
    )  # Field name made lowercase.
    campoadicional2 = models.CharField(max_length=250)
    campoadicional3 = models.CharField(max_length=250)
    estrateca_cardnumber = models.CharField(
        db_column="estrateca_CardNumber", max_length=100
    )  # Field name made lowercase.
    estrateca_vouchertext = models.TextField(
        db_column="estrateca_VoucherText"
    )  # Field name made lowercase.
    campoadicional4 = models.CharField(max_length=250)
    campoadicional5 = models.CharField(max_length=250)
    sacoa_cardnumber = models.CharField(
        db_column="sacoa_CardNumber", max_length=100
    )  # Field name made lowercase.
    sacoa_credits = models.DecimalField(max_digits=19, decimal_places=4)
    estrateca_typedisccount = models.CharField(
        db_column="estrateca_TypeDisccount", max_length=50
    )  # Field name made lowercase.
    estrateca_discountcode = models.CharField(
        db_column="estrateca_DiscountCode", max_length=50
    )  # Field name made lowercase.
    estrateca_discountid = models.CharField(
        db_column="estrateca_DiscountID", max_length=50
    )  # Field name made lowercase.
    estrateca_discountamount = models.DecimalField(
        db_column="estrateca_DiscountAmount", max_digits=19, decimal_places=4
    )  # Field name made lowercase.
    desc_imp_original = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    donativo = models.DecimalField(max_digits=19, decimal_places=4)
    totalcondonativo = models.DecimalField(max_digits=19, decimal_places=4)
    totalconpropinacargodonativo = models.DecimalField(max_digits=19, decimal_places=4)
    orderreference = models.CharField(max_length=500)
    appname = models.CharField(max_length=250)
    paymentproviderid = models.CharField(max_length=50)
    paymentprovider = models.CharField(max_length=250)
    changestatussrx = models.BooleanField(
        db_column="ChangeStatusSRX", blank=True, null=True
    )  # Field name made lowercase.
    datedownload = models.DateTimeField(
        db_column="DateDownload", blank=True, null=True
    )  # Field name made lowercase.
    comandaimpresacancelada = models.BooleanField(blank=True, null=True)
    empaquetado = models.DateTimeField(blank=True, null=True)
    status_domicilio = models.IntegerField()
    asignacion = models.DateTimeField(blank=True, null=True)
    enviopagado = models.BooleanField()
    diet_restrictions = models.CharField(max_length=250)
    sl_cupon_descuento = models.CharField(max_length=250)
    sl_tipo_cupon = models.CharField(max_length=50)
    sl_importe_descuento = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    tuki_cardnumber = models.CharField(
        db_column="TUKI_CardNumber", max_length=250
    )  # Field name made lowercase.
    tuki_accumulatedpoints = models.DecimalField(
        db_column="TUKI_AccumulatedPoints",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    tuki_currentpoints = models.DecimalField(
        db_column="TUKI_CurrentPoints",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    sl_num_cupones = models.DecimalField(
        max_digits=16, decimal_places=6, blank=True, null=True
    )
    workspaceid = models.CharField(
        db_column="WorkspaceId", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    sentsync = models.BooleanField(db_column="SentSync")  # Field name made lowercase.
    subtotal_ec = models.BinaryField(blank=True, null=True)
    total_ec = models.BinaryField(blank=True, null=True)
    totalconpropinacargo_ec = models.BinaryField(blank=True, null=True)
    mv_room = models.CharField(max_length=100)
    mv_lastname = models.CharField(max_length=100)
    estado = models.BooleanField(blank=True, null=True)
    totalsindescuentoimp = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "cheques"
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return f"Cheque {self.folio} con fecha {self.fecha} - {self.mesa}"


# Cheqdet
class Cheqdet(models.Model):  # Importante
    foliodet = models.BigIntegerField(blank=True, null=False, primary_key=True)
    movimiento = models.DecimalField(
        max_digits=3, decimal_places=0, blank=True, null=True
    )
    comanda = models.CharField(max_length=8, blank=True, null=True)
    cantidad = models.DecimalField(
        max_digits=14, decimal_places=6, blank=True, null=True
    )
    idproducto = models.ForeignKey(
        "Productos", models.DO_NOTHING, db_column="idproducto", blank=True, null=True
    )
    descuento = models.DecimalField(
        max_digits=8, decimal_places=4, blank=True, null=True
    )
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto1 = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    impuesto2 = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    impuesto3 = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    preciosinimpuestos = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    tiempo = models.CharField(max_length=20, blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    modificador = models.BooleanField(blank=True, null=True)
    mitad = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    comentario = models.CharField(max_length=254, blank=True, null=True)
    idestacion = models.CharField(max_length=40, blank=True, null=True)
    usuariodescuento = models.CharField(max_length=15, blank=True, null=True)
    comentariodescuento = models.CharField(max_length=60, blank=True, null=True)
    idtipodescuento = models.CharField(max_length=5, blank=True, null=True)
    horaproduccion = models.DateTimeField(blank=True, null=True)
    idproductocompuesto = models.CharField(max_length=15, blank=True, null=True)
    productocompuestoprincipal = models.BooleanField(blank=True, null=True)
    preciocatalogo = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    marcar = models.BooleanField(blank=True, null=True)
    idmeseroproducto = models.CharField(max_length=4, blank=True, null=True)
    prioridadproduccion = models.CharField(max_length=1, blank=True, null=True)
    estatuspatin = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    idcortesia = models.CharField(max_length=5, blank=True, null=True)
    numerotarjeta = models.CharField(max_length=16, blank=True, null=True)
    estadomonitor = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    llavemovto = models.CharField(max_length=100, blank=True, null=True)
    horameserofinalizado = models.DateTimeField(blank=True, null=True)
    meserofinalizado = models.CharField(max_length=4, blank=True, null=True)
    sistema_envio = models.IntegerField()
    idturno_cierre = models.BigIntegerField(blank=True, null=True)
    procesado = models.BooleanField(blank=True, null=True)
    promovolumen = models.BooleanField()
    iddispositivo = models.IntegerField()
    productsyncidsr = models.IntegerField()
    subtotalsrx = models.DecimalField(max_digits=7, decimal_places=5)
    totalsrx = models.DecimalField(max_digits=7, decimal_places=5)
    idmovtobillar = models.BigIntegerField()
    idlistaprecio = models.IntegerField(blank=True, null=True)
    tipocambio = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    impuestoimporte3 = models.DecimalField(max_digits=19, decimal_places=4)
    estrateca_discountcode = models.CharField(
        db_column="estrateca_DiscountCode", max_length=50
    )  # Field name made lowercase.
    estrateca_discountid = models.CharField(
        db_column="estrateca_DiscountID", max_length=50
    )  # Field name made lowercase.
    estrateca_discountamount = models.DecimalField(
        db_column="estrateca_DiscountAmount", max_digits=19, decimal_places=4
    )  # Field name made lowercase.
    saledetailid = models.CharField(max_length=250, blank=True, null=True)
    preciosinimpuestos_ec = models.BinaryField(blank=True, null=True)
    precio_ec = models.BinaryField(blank=True, null=True)
    escargoarea = models.BooleanField()
    workspaceid = models.CharField(
        db_column="WorkspaceId", max_length=36, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "cheqdet"
        verbose_name = "Detalle de la venta"
        verbose_name_plural = "Detalles de las ventas"


# Productos
class Productos(models.Model):  # Importante
    idproducto = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    idgrupo = models.ForeignKey(
        Grupos, models.DO_NOTHING, db_column="idgrupo", blank=True, null=True
    )
    nombrecorto = models.CharField(max_length=20, blank=True, null=True)
    plu = models.CharField(max_length=30, blank=True, null=True)
    imagen = models.BinaryField(blank=True, null=True)
    nofacturable = models.BooleanField(blank=True, null=True)
    comentario = models.CharField(max_length=254, blank=True, null=True)
    usarcomedor = models.BooleanField(blank=True, null=True)
    usardomicilio = models.BooleanField(blank=True, null=True)
    usarrapido = models.BooleanField(blank=True, null=True)
    usarcedis = models.BooleanField(blank=True, null=True)
    idinsumospresentaciones = models.CharField(max_length=15, blank=True, null=True)
    imagenmenuelectronico = models.BinaryField(blank=True, null=True)
    descripcionmenuelectronico = models.CharField(max_length=255, blank=True, null=True)
    usarmenuelectronico = models.BooleanField(blank=True, null=True)
    extmenu = models.CharField(max_length=5, blank=True, null=True)
    imagen_menu = models.TextField(blank=True, null=True)
    descripcion_detalle = models.CharField(max_length=300)
    calorias = models.DecimalField(max_digits=18, decimal_places=0)
    visible_menu = models.BooleanField()
    capturar_pendientes = models.BooleanField()
    id_etiqueta = models.CharField(max_length=50)
    id_etiqueta_descripcion = models.CharField(max_length=50)
    idprodserv_sat = models.CharField(
        db_column="idprodserv_SAT", max_length=50
    )  # Field name made lowercase.
    usarvectorplus = models.BooleanField(
        db_column="usarVectorPlus"
    )  # Field name made lowercase.
    workspaceid = models.CharField(
        db_column="WorkspaceId", max_length=36, blank=True, null=True
    )  # Field name made lowercase.
    imagenme_modified = models.BooleanField()
    imagenbackoffice = models.BinaryField(blank=True, null=True)
    monitoreo = models.BooleanField()
    prioridadimpresion = models.DecimalField(
        max_digits=4, decimal_places=0, blank=True, null=True
    )
    idbo = models.IntegerField(
        db_column="IdBO", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "productos"
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.descripcion}"


# Productodetalles
class Productosdetalle(models.Model):  # Importante
    idproducto = models.OneToOneField(
        Productos,
        models.DO_NOTHING,
        db_column="idproducto",
        blank=True,
        null=False,
        primary_key=True,
    )
    idempresa = models.ForeignKey(
        Empresas, models.DO_NOTHING, db_column="idempresa", blank=True, null=True
    )
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impuesto1 = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    impuesto2 = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    impuesto3 = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    preciosinimpuestos = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    bloqueado = models.BooleanField(blank=True, null=True)
    precioabierto = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    canjeablepuntos = models.BooleanField(blank=True, null=True)
    preciopuntos = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    puntoscanje = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    puntosextras = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    lunesinicio = models.CharField(max_length=11, blank=True, null=True)
    lunesfin = models.CharField(max_length=11, blank=True, null=True)
    preciolunes = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    lunesdiasalida = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    martesinicio = models.CharField(max_length=11, blank=True, null=True)
    martesfin = models.CharField(max_length=11, blank=True, null=True)
    preciomartes = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    martesdiasalida = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    miercolesinicio = models.CharField(max_length=11, blank=True, null=True)
    miercolesfin = models.CharField(max_length=11, blank=True, null=True)
    preciomiercoles = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    miercolesdiasalida = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    juevesinicio = models.CharField(max_length=11, blank=True, null=True)
    juevesfin = models.CharField(max_length=11, blank=True, null=True)
    preciojueves = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    juevesdiasalida = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    viernesinicio = models.CharField(max_length=11, blank=True, null=True)
    viernesfin = models.CharField(max_length=11, blank=True, null=True)
    precioviernes = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    viernesdiasalida = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    sabadoinicio = models.CharField(max_length=11, blank=True, null=True)
    sabadofin = models.CharField(max_length=11, blank=True, null=True)
    preciosabado = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    sabadodiasalida = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    domingoinicio = models.CharField(max_length=11, blank=True, null=True)
    domingofin = models.CharField(max_length=11, blank=True, null=True)
    preciodomingo = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    domingodiasalida = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    aplicalunes = models.BooleanField(blank=True, null=True)
    aplicamartes = models.BooleanField(blank=True, null=True)
    aplicamiercoles = models.BooleanField(blank=True, null=True)
    aplicajueves = models.BooleanField(blank=True, null=True)
    aplicaviernes = models.BooleanField(blank=True, null=True)
    aplicasabado = models.BooleanField(blank=True, null=True)
    aplicadomingo = models.BooleanField(blank=True, null=True)
    excentoimpuestos = models.BooleanField(blank=True, null=True)
    secuenciacompuesto = models.BooleanField(blank=True, null=True)
    finalizarsecuenciacompuesto = models.BooleanField(blank=True, null=True)
    heredarmonitormodificadores = models.BooleanField(blank=True, null=True)
    comisionvendedor = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    eliminarfiscal = models.BooleanField(blank=True, null=True)
    enviarproduccionsimodificador = models.BooleanField(blank=True, null=True)
    cargoadicional = models.DecimalField(
        max_digits=5, decimal_places=0, blank=True, null=True
    )
    afectacomensales = models.BooleanField(blank=True, null=True)
    comensalesafectados = models.DecimalField(
        max_digits=2, decimal_places=0, blank=True, null=True
    )
    descargar = models.BooleanField(blank=True, null=True)
    usarmultiplicadorprodcomp = models.BooleanField(blank=True, null=True)
    rentabilidadcedis = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    idarea = models.CharField(max_length=4, blank=True, null=True)
    permitirprodcompenmodif = models.BooleanField(blank=True, null=True)
    politicapuntos = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    favorito = models.BooleanField(blank=True, null=True)
    idunidad = models.ForeignKey(
        "Udsmedida", models.DO_NOTHING, db_column="idunidad", blank=True, null=True
    )
    ocultarmitades = models.BooleanField()
    dev_impuestoimporte3 = models.BooleanField()
    impuestoimporte3 = models.DecimalField(max_digits=19, decimal_places=4)
    usa_imagen_monitor = models.BooleanField()
    rutaimagen = models.TextField(blank=True, null=True)
    comisionprecio = models.DecimalField(max_digits=19, decimal_places=4)
    usa_bascula = models.BooleanField()

    class Meta:
        managed = False
        db_table = "productosdetalle"
        verbose_name = "Detalle de producto"
        verbose_name_plural = "Detalles de productos"


# Forma de pago
class Formasdepago(models.Model):  # Importante
    idformadepago = models.CharField(primary_key=True, max_length=5)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tipodecambio = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    solicitareferencia = models.BooleanField(blank=True, null=True)
    prioridadboton = models.DecimalField(
        max_digits=2, decimal_places=0, blank=True, null=True
    )
    cuentacontableimporte = models.CharField(max_length=5, blank=True, null=True)
    cuentacontablecomision = models.CharField(max_length=5, blank=True, null=True)
    cuentacontableivacomision = models.CharField(max_length=5, blank=True, null=True)
    comision = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    visible = models.BooleanField(blank=True, null=True)
    aceptapropina = models.BooleanField(blank=True, null=True)
    subtipo = models.SmallIntegerField(blank=True, null=True)
    prefijo1 = models.CharField(max_length=3, blank=True, null=True)
    prefijo2 = models.CharField(max_length=3, blank=True, null=True)
    codigodeprefijoconsulta = models.CharField(max_length=10, blank=True, null=True)
    codigodeprefijoacumred = models.CharField(max_length=10, blank=True, null=True)
    generapuntos = models.BooleanField(blank=True, null=True)
    formatoimpresion = models.DecimalField(
        max_digits=2, decimal_places=0, blank=True, null=True
    )
    idfpagofiscal = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    pagoenlinea = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    tipotarjeta = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    imagen = models.BinaryField(blank=True, null=True)
    nofacturable = models.BooleanField(blank=True, null=True)
    comisionreporte1 = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    comisionreporte2 = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    tipotarjetabancaria = models.SmallIntegerField(
        db_column="tipoTarjetaBancaria"
    )  # Field name made lowercase.
    idtipodescuento = models.CharField(max_length=5)
    idformapago_sat = models.CharField(
        db_column="idformapago_SAT", max_length=50
    )  # Field name made lowercase.
    servicecode = models.ForeignKey(
        "Servicecodes",
        models.DO_NOTHING,
        db_column="servicecode",
        blank=True,
        null=True,
    )
    leerbrazalete = models.BooleanField()
    cargohabitacion_eg = models.BooleanField()
    visible_kiosco = models.BooleanField()
    autocapturar = models.BooleanField()
    sumatotal = models.BooleanField()
    equivalencia = models.CharField(max_length=30, blank=True, null=True)
    workspaceid = models.CharField(
        db_column="WorkspaceId", max_length=36, blank=True, null=True
    )  # Field name made lowercase.

    def __str__(self):
        return f"{self.descripcion}"

    class Meta:
        managed = False
        db_table = "formasdepago"
        verbose_name = "Forma de pago"
        verbose_name_plural = "Formas de pago"


# Chequespagos
class Chequespagos(models.Model):  # Importante
    folio = models.BigIntegerField(primary_key=True, blank=True, null=False)
    idformadepago = models.ForeignKey(
        "Formasdepago",
        models.DO_NOTHING,
        db_column="idformadepago",
        blank=True,
        null=True,
    )
    importe = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    propina = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    tipodecambio = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    referencia = models.TextField(blank=True, null=True)
    idturno_cierre = models.BigIntegerField(blank=True, null=True)
    procesado = models.BooleanField(blank=True, null=True)
    sistema_envio = models.IntegerField()
    importe_ec = models.BinaryField(blank=True, null=True)
    propina_ec = models.BinaryField(blank=True, null=True)
    workspaceid = models.CharField(
        db_column="WorkspaceId", max_length=36
    )  # Field name made lowercase.
    cardbrand = models.CharField(
        db_column="cardBrand", max_length=120
    )  # Field name made lowercase.
    importe_cashdro = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    # id = models.BigAutoField()

    class Meta:
        managed = False
        db_table = "chequespagos"
        verbose_name = "Resumen venta"
        verbose_name_plural = "Resumen de ventas"

    def __str__(self):
        return f"Pago {self.folio} con importe {self.importe}"


class Productosdelivery(models.Model):
    idproducto = models.ForeignKey(
        Productos, models.DO_NOTHING, db_column="idproducto", blank=True, null=True
    )
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descripcion = models.CharField(max_length=250)
    nombre = models.CharField(max_length=250)
    idapp = models.IntegerField()
    visiblemenu = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "productosdelivery"


# Estaciones
class Estaciones(models.Model):
    idestacion = models.CharField(primary_key=True, max_length=40)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    serie = models.CharField(max_length=30, blank=True, null=True)
    ip = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=200, blank=True, null=True)
    seriefolio = models.CharField(max_length=15, blank=True, null=True)
    bloqueararearestaurant = models.BooleanField(blank=True, null=True)
    idarearestaurant = models.CharField(max_length=5, blank=True, null=True)
    mostrarcumpleaños = models.BooleanField(blank=True, null=True)
    esconderescritorio = models.BooleanField(blank=True, null=True)
    esconderbarra = models.BooleanField(blank=True, null=True)
    impresoracheques = models.CharField(max_length=50, blank=True, null=True)
    impresoranotas = models.CharField(max_length=50, blank=True, null=True)
    impresorafacturas = models.CharField(max_length=50, blank=True, null=True)
    saltosimpresoracheques = models.IntegerField(blank=True, null=True)
    saltosimpresoranotas = models.IntegerField(blank=True, null=True)
    usacutterimpresoracheques = models.BooleanField(blank=True, null=True)
    usacutterimpresoranotas = models.BooleanField(blank=True, null=True)
    usacajondedinero = models.BooleanField(blank=True, null=True)
    cajonascii = models.CharField(max_length=20, blank=True, null=True)
    cajonpuerto = models.IntegerField(blank=True, null=True)
    cajontipo = models.IntegerField(blank=True, null=True)
    cajontiempo = models.IntegerField(blank=True, null=True)
    cajonimpresora = models.CharField(max_length=50, blank=True, null=True)
    cajontipoconexion = models.IntegerField(blank=True, null=True)
    cajacomandero = models.CharField(max_length=80, blank=True, null=True)
    impventasempezar1 = models.CharField(max_length=3, blank=True, null=True)
    impventasempezar2 = models.CharField(max_length=3, blank=True, null=True)
    impventasempezar3 = models.CharField(max_length=3, blank=True, null=True)
    impventasempezar4 = models.CharField(max_length=3, blank=True, null=True)
    impventasempezar5 = models.CharField(max_length=8, blank=True, null=True)
    impventasfinalizar1 = models.CharField(max_length=3, blank=True, null=True)
    impventasfinalizar2 = models.CharField(max_length=3, blank=True, null=True)
    impventasfinalizar3 = models.CharField(max_length=3, blank=True, null=True)
    impventasfinalizar4 = models.CharField(max_length=3, blank=True, null=True)
    impventasfinalizar5 = models.CharField(max_length=3, blank=True, null=True)
    impnotasempezar1 = models.CharField(max_length=3, blank=True, null=True)
    impnotasempezar2 = models.CharField(max_length=3, blank=True, null=True)
    impnotasempezar3 = models.CharField(max_length=3, blank=True, null=True)
    impnotasempezar4 = models.CharField(max_length=3, blank=True, null=True)
    impnotasempezar5 = models.CharField(max_length=3, blank=True, null=True)
    impnotasfinalizar1 = models.CharField(max_length=3, blank=True, null=True)
    impnotasfinalizar2 = models.CharField(max_length=3, blank=True, null=True)
    impnotasfinalizar3 = models.CharField(max_length=3, blank=True, null=True)
    impnotasfinalizar4 = models.CharField(max_length=3, blank=True, null=True)
    impnotasfinalizar5 = models.CharField(max_length=3, blank=True, null=True)
    impfacempezar1 = models.CharField(max_length=3, blank=True, null=True)
    impfacempezar2 = models.CharField(max_length=3, blank=True, null=True)
    impfacempezar3 = models.CharField(max_length=3, blank=True, null=True)
    impfacempezar4 = models.CharField(max_length=3, blank=True, null=True)
    impfacempezar5 = models.CharField(max_length=3, blank=True, null=True)
    impfacfinalizar1 = models.CharField(max_length=3, blank=True, null=True)
    impfacfinalizar2 = models.CharField(max_length=3, blank=True, null=True)
    impfacfinalizar3 = models.CharField(max_length=3, blank=True, null=True)
    impfacfinalizar4 = models.CharField(max_length=3, blank=True, null=True)
    impfacfinalizar5 = models.CharField(max_length=3, blank=True, null=True)
    idformatofacturafiscal = models.IntegerField(blank=True, null=True)
    idformatofacturapublico = models.IntegerField(blank=True, null=True)
    estacionpocket = models.BooleanField(blank=True, null=True)
    colorbotones = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    colorpantallas = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    colorcuadrosdetexto = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    tipodeimpresionfactura = models.IntegerField(blank=True, null=True)
    seriefacturacion = models.CharField(max_length=15, blank=True, null=True)
    usarturnoestacion = models.IntegerField(blank=True, null=True)
    buscaractualizaciones = models.BooleanField(blank=True, null=True)
    directorioactualizaciones = models.CharField(max_length=150, blank=True, null=True)
    nombrearchivoexportacion = models.CharField(max_length=80, blank=True, null=True)
    directoriorespaldo = models.CharField(max_length=150, blank=True, null=True)
    directoriopoliza = models.CharField(max_length=150, blank=True, null=True)
    directorioexportacion = models.CharField(max_length=150, blank=True, null=True)
    numeroestacion = models.IntegerField(blank=True, null=True)
    nombrepuntodeventa = models.CharField(max_length=40, blank=True, null=True)
    serieimpresoracuentas = models.CharField(max_length=40, blank=True, null=True)
    posnoterminal = models.CharField(max_length=15, blank=True, null=True)
    rutasonido = models.CharField(max_length=150, blank=True, null=True)
    sonidomonitor = models.BooleanField(blank=True, null=True)
    usarbascula = models.BooleanField(blank=True, null=True)
    basculapuerto = models.IntegerField(blank=True, null=True)
    basculabitsegundo = models.CharField(max_length=10, blank=True, null=True)
    basculabitdatos = models.CharField(max_length=10, blank=True, null=True)
    basculaparidad = models.CharField(max_length=10, blank=True, null=True)
    basculabitdeparada = models.CharField(max_length=10, blank=True, null=True)
    facturaslineasencabezado = models.IntegerField(blank=True, null=True)
    facturaslineaspiedepagina = models.IntegerField(blank=True, null=True)
    facturassumarlineascuerpoapie = models.BooleanField(blank=True, null=True)
    autorizacionacceso = models.IntegerField(blank=True, null=True)
    autorizacioneventos = models.IntegerField(blank=True, null=True)
    autorizacioncomandero = models.IntegerField(blank=True, null=True)
    ejecutararchivocierre = models.BooleanField(blank=True, null=True)
    nombrearchivoejecutarcierre = models.CharField(
        max_length=150, blank=True, null=True
    )
    enlacesoftencuestas = models.BooleanField(blank=True, null=True)
    impresorafiscal = models.BooleanField(blank=True, null=True)
    fiscalport = models.IntegerField(blank=True, null=True)
    paridadxsegfiscal = models.IntegerField(blank=True, null=True)
    idcallactivo = models.BooleanField(blank=True, null=True)
    idcallpuerto = models.IntegerField(blank=True, null=True)
    idcallbitsegundo = models.CharField(max_length=10, blank=True, null=True)
    idcallbitdatos = models.CharField(max_length=10, blank=True, null=True)
    idcallparidad = models.CharField(max_length=10, blank=True, null=True)
    idcallbitdeparada = models.CharField(max_length=50, blank=True, null=True)
    paisimpresorafiscal = models.IntegerField(blank=True, null=True)
    visorinstalado = models.BooleanField(blank=True, null=True)
    visorpuerto = models.IntegerField(blank=True, null=True)
    visormensaje = models.BooleanField(blank=True, null=True)
    mensajeespera = models.CharField(max_length=40, blank=True, null=True)
    idcallnorma = models.IntegerField(blank=True, null=True)
    monitorteclaarriba = models.CharField(max_length=5, blank=True, null=True)
    monitorteclafinalizar = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaregresar = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaprimero = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaabajo = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaultimo = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaactualizar = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaadmonanterior = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaadmonsiguiente = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaadmonizquierda = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaadmonderecha = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaadmonactualizar = models.CharField(max_length=5, blank=True, null=True)
    monitorteclaadmonconsultaorden = models.CharField(
        max_length=5, blank=True, null=True
    )
    monitorteclaadmoncerrarconsulta = models.CharField(
        max_length=5, blank=True, null=True
    )
    monitorteclaadmonfinorden = models.CharField(max_length=5, blank=True, null=True)
    intervalosonidoexcedidomonitor = models.DecimalField(
        max_digits=4, decimal_places=1, blank=True, null=True
    )
    monitorimprimircomanda = models.BooleanField(blank=True, null=True)
    monitorimpresoracomandas = models.CharField(max_length=60, blank=True, null=True)
    monitorimpresoraautocutter = models.BooleanField(blank=True, null=True)
    monitoriniciarmodulo = models.IntegerField(blank=True, null=True)
    monitorordenamientoproductos = models.IntegerField(blank=True, null=True)
    tarjetacredito = models.BooleanField(blank=True, null=True)
    tipodispositivo = models.IntegerField(blank=True, null=True)
    pinpadpuertocom = models.CharField(max_length=10, blank=True, null=True)
    pinpadbitsxsegundo = models.CharField(max_length=10, blank=True, null=True)
    pinpadparidad = models.CharField(max_length=1, blank=True, null=True)
    pinpadbitsdeparada = models.CharField(max_length=3, blank=True, null=True)
    pinpadbitsdedatos = models.CharField(max_length=1, blank=True, null=True)
    tipoimpresoracuentas = models.IntegerField(blank=True, null=True)
    tipoimpresoranotas = models.IntegerField(blank=True, null=True)
    fiscalimpcambio = models.IntegerField(blank=True, null=True)
    fiscalimpcantximporte = models.IntegerField(blank=True, null=True)
    sonidomonitortiempoexcedido = models.BooleanField(blank=True, null=True)
    rutasonidotiempoexcedido = models.CharField(max_length=150, blank=True, null=True)
    tipoimpresioncomandamonitor = models.IntegerField(blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    usartipoventarapida = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    actualizarcatalogos = models.BooleanField(blank=True, null=True)
    enviarcomandosdeimpresion = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    comandoantesimprimir1 = models.CharField(max_length=30, blank=True, null=True)
    comandoantesimprimir2 = models.CharField(max_length=30, blank=True, null=True)
    comandoantescopia1 = models.CharField(max_length=30, blank=True, null=True)
    comandoantescopia2 = models.CharField(max_length=30, blank=True, null=True)
    actualizaclientes = models.BooleanField(blank=True, null=True)
    rutatemporal = models.CharField(max_length=255, blank=True, null=True)
    fenombreformatopublico = models.CharField(max_length=50, blank=True, null=True)
    fenombreformatoempresa = models.CharField(max_length=50, blank=True, null=True)
    feimpresoragrafico = models.CharField(max_length=250, blank=True, null=True)
    lectordehuellainstalado = models.IntegerField(blank=True, null=True)
    autorizacioncuentasporcobrar = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    logofiscal = models.DecimalField(
        max_digits=4, decimal_places=0, blank=True, null=True
    )
    densidadlogo = models.DecimalField(
        max_digits=4, decimal_places=0, blank=True, null=True
    )
    idarearestaurantrapido = models.CharField(max_length=5, blank=True, null=True)
    idarearestaurantdomicilio = models.CharField(max_length=5, blank=True, null=True)
    monprodincluirtodas = models.BooleanField(blank=True, null=True)
    impfiscalvalidaitems = models.BooleanField(blank=True, null=True)
    monitorimprimircomandamoduloadmin = models.BooleanField(blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    serieimpresora = models.CharField(max_length=10, blank=True, null=True)
    fecharev = models.CharField(max_length=10, blank=True, null=True)
    rev = models.CharField(max_length=4, blank=True, null=True)
    accesocentral = models.BooleanField(blank=True, null=True)
    usarturnousuario = models.DecimalField(max_digits=1, decimal_places=0)
    solicitarturnocomandero = models.DecimalField(max_digits=1, decimal_places=0)
    usuariocajacomandero = models.CharField(max_length=15)
    actualizarexistencias = models.BooleanField()
    bloquearteclado = models.BooleanField(blank=True, null=True)
    servidoraplicacionessucursal = models.BooleanField(blank=True, null=True)
    servidoraplicaciones = models.BooleanField(blank=True, null=True)
    actualizarcatalogosmovil = models.BooleanField(blank=True, null=True)
    colorbarratitulo = models.DecimalField(max_digits=10, decimal_places=0)
    ejecarchnvacta = models.IntegerField()
    archejecnvacta = models.CharField(max_length=200)
    paramejecnvacta = models.CharField(max_length=200)
    ejecarchreimpresioncta = models.IntegerField()
    archejecreimpresioncta = models.CharField(max_length=200)
    paramejecreimpresioncta = models.CharField(max_length=200)
    ejecarchcancelcta = models.IntegerField()
    archejeccancelcta = models.CharField(max_length=200)
    paramejeccancelcta = models.CharField(max_length=200)
    ejecarchreabrircta = models.IntegerField()
    archejecreabrircta = models.CharField(max_length=200)
    paramejecreabrircta = models.CharField(max_length=200)
    idformatocomedor = models.CharField(max_length=5)
    idformatodomicilio = models.CharField(max_length=5)
    idformatorapido = models.CharField(max_length=5)
    idformatonotadeconsumo = models.CharField(max_length=5)
    idformatomovil = models.CharField(max_length=5)
    copiasticketcomedor = models.DecimalField(max_digits=2, decimal_places=0)
    copiasticketdomicilio = models.DecimalField(max_digits=2, decimal_places=0)
    copiasticketrapido = models.DecimalField(max_digits=2, decimal_places=0)
    copiasnotadeconsumo = models.DecimalField(max_digits=2, decimal_places=0)
    copiasticketmovil = models.DecimalField(max_digits=2, decimal_places=0)
    autorizacionmonedero = models.IntegerField(blank=True, null=True)
    vigianotificar = models.IntegerField()
    archivoejecutarfincierreturno = models.CharField(
        max_length=150, blank=True, null=True
    )
    archivoejecutariniciocierreturno = models.CharField(
        max_length=150, blank=True, null=True
    )
    ejecutarfincierreturno = models.BooleanField(blank=True, null=True)
    ejecutariniciocierreturno = models.BooleanField(blank=True, null=True)
    esperarejecutarfincierreturno = models.BooleanField(blank=True, null=True)
    esperarejecutariniciocierreturno = models.BooleanField(blank=True, null=True)
    autorizacionregistroasistencia = models.IntegerField()
    ejecutararchivoiniciocierreturno = models.BooleanField()
    ejecutararchivofincierreturno = models.BooleanField()
    rutaarchivoiniciocierreturno = models.CharField(
        max_length=150, blank=True, null=True
    )
    rutaarchivofincierreturno = models.CharField(max_length=150, blank=True, null=True)
    ejecarchpagarcta = models.BooleanField()
    archejecpagarcta = models.CharField(max_length=200)
    paramejecpagarcta = models.CharField(max_length=200)
    formato_cfdi_33_persona = models.CharField(max_length=80)
    formato_cfdi_33_empresa = models.CharField(max_length=80)
    formato_cfdi_33_publico = models.CharField(max_length=80)
    abrecajonparacontar = models.IntegerField()
    scaleinputstring = models.CharField(max_length=3)
    tkc_numcaja = models.IntegerField(
        db_column="TKC_NumCaja"
    )  # Field name made lowercase.
    seriecomplementopago = models.CharField(max_length=15, blank=True, null=True)
    habilitapinpad = models.BooleanField()
    ip_pinpad = models.CharField(
        db_column="IP_pinpad", max_length=100
    )  # Field name made lowercase.
    puerto_pinpad = models.CharField(max_length=100)
    seriefactglobal = models.CharField(
        db_column="serieFactGlobal", max_length=15, blank=True, null=True
    )  # Field name made lowercase.
    almacensalida_elabora = models.CharField(max_length=5)
    almacenentrada_elabora = models.CharField(max_length=5)
    ejecarchfactura = models.IntegerField()
    archarchfactura = models.CharField(max_length=150, blank=True, null=True)
    paramarchfactura = models.CharField(max_length=200, blank=True, null=True)
    areatipoventarapida = models.CharField(max_length=5)
    mercadopagoposid = models.CharField(
        db_column="MercadoPagoPosId", max_length=200, blank=True, null=True
    )  # Field name made lowercase.
    usemercadopago = models.BooleanField(
        db_column="UseMercadoPago", blank=True, null=True
    )  # Field name made lowercase.
    idformatokiosco = models.CharField(max_length=5, blank=True, null=True)
    copiasticketkiosco = models.DecimalField(
        max_digits=2, decimal_places=0, blank=True, null=True
    )
    modo_operacion = models.SmallIntegerField()
    ejecarchcancelarfactura = models.IntegerField()
    archcancelarfactura = models.CharField(max_length=150, blank=True, null=True)
    paramarchcancelarfactura = models.CharField(max_length=200, blank=True, null=True)
    posisopen = models.BooleanField(db_column="PosIsOpen")  # Field name made lowercase.
    poslastonline = models.DateTimeField(
        db_column="PosLastOnline"
    )  # Field name made lowercase.
    prefijo_bascula = models.DecimalField(
        max_digits=2, decimal_places=0, blank=True, null=True
    )
    monitorcorte_servidor = models.BooleanField()
    monitorcorte_ejecutando = models.BooleanField()
    sistemamaximizado = models.BooleanField()
    gazebo_eg = models.BooleanField()
    bracelet_enum_payment = models.SmallIntegerField()
    idalmacen = models.CharField(max_length=5, blank=True, null=True)
    only_areas_fastfood = models.BooleanField()
    fastfood_type_mode = models.IntegerField()
    workspaceid = models.CharField(
        db_column="WorkspaceId", max_length=36, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "estaciones"


# Turnos
class Turnos(models.Model):
    idturnointerno = models.BigAutoField(primary_key=True)
    idturno = models.BigIntegerField(blank=True, null=True)
    fondo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    apertura = models.DateTimeField(blank=True, null=True)
    cierre = models.DateTimeField(blank=True, null=True)
    idestacion = models.ForeignKey(
        Estaciones, models.DO_NOTHING, db_column="idestacion", blank=True, null=True
    )
    cajero = models.CharField(max_length=15, blank=True, null=True)
    efectivo = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    tarjeta = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    vales = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    credito = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    procesadoweb = models.BooleanField(blank=True, null=True)
    idempresa = models.CharField(max_length=15, blank=True, null=True)
    enviadoacentral = models.BooleanField(blank=True, null=True)
    fechaenviado = models.DateTimeField(blank=True, null=True)
    usuarioenvio = models.CharField(max_length=30, blank=True, null=True)
    offline = models.BooleanField(blank=True, null=True)
    enviadoaf = models.BooleanField()
    corte_enviado = models.BooleanField()
    eliminartemporalesencierre = models.BooleanField()
    idmesero = models.CharField(max_length=4, blank=True, null=True)
    fondodolares = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    procesado = models.BooleanField()
    workspaceid = models.CharField(
        db_column="WorkspaceId", max_length=36, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "turnos"


class Clientes(models.Model):
    idcliente = models.CharField(primary_key=True, max_length=15)
    nombre = models.TextField(blank=True, null=True)
    direccion = models.CharField(max_length=160, blank=True, null=True)
    codigopostal = models.CharField(max_length=15, blank=True, null=True)
    poblacion = models.CharField(max_length=60, blank=True, null=True)
    estado = models.CharField(max_length=25, blank=True, null=True)
    pais = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    rfc = models.CharField(max_length=15, blank=True, null=True)
    curp = models.CharField(max_length=20, blank=True, null=True)
    cumpleaños = models.DateTimeField(blank=True, null=True)
    limitedecredito = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    limitecreditodiario = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    descuento = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    notas = models.CharField(max_length=254, blank=True, null=True)
    foliofiscal = models.CharField(max_length=15, blank=True, null=True)
    idtipodescuento = models.CharField(max_length=5, blank=True, null=True)
    tipofacturacion = models.IntegerField(blank=True, null=True)
    procesadoweb = models.BooleanField(blank=True, null=True)
    nocobrarimpuestos = models.BooleanField(blank=True, null=True)
    contacto = models.CharField(max_length=250, blank=True, null=True)
    tarjetamonedero = models.CharField(max_length=20, blank=True, null=True)
    telefono1 = models.CharField(max_length=50, blank=True, null=True)
    telefono2 = models.CharField(max_length=50, blank=True, null=True)
    telefono3 = models.CharField(max_length=50, blank=True, null=True)
    telefono4 = models.CharField(max_length=50, blank=True, null=True)
    telefono5 = models.CharField(max_length=50, blank=True, null=True)
    femextipocliente = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    giro = models.CharField(max_length=60, blank=True, null=True)
    tipocredito = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    idtipocliente = models.CharField(max_length=5, blank=True, null=True)
    idtipomenu = models.CharField(max_length=5, blank=True, null=True)
    fotografia = models.BinaryField(blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    retenerimpuesto = models.BooleanField(blank=True, null=True)
    tipocuenta = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    tipoclientencf = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    dinerid = models.CharField(max_length=50, blank=True, null=True)
    descuentoprimeraventacomedoremp = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    idpais_sat = models.CharField(
        db_column="idpais_SAT", max_length=50
    )  # Field name made lowercase.
    contemplarpropina = models.BooleanField()
    oblig_tributarias = models.CharField(max_length=240)
    idregimen_sat = models.CharField(
        db_column="idregimen_SAT", max_length=50
    )  # Field name made lowercase.
    tratamientopersonal = models.CharField(max_length=30)
    status = models.BooleanField()
    dias_vigencia_credito = models.IntegerField()
    primer_nombre = models.CharField(max_length=50)
    otros_nombres = models.CharField(max_length=120)
    apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=120)
    lastchange = models.DateTimeField(
        db_column="LastChange", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "clientes"


class Facturas(models.Model):
    idfactura = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    serie = models.CharField(max_length=15, blank=True, null=True)
    folio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    idcliente = models.ForeignKey(
        Clientes, models.DO_NOTHING, db_column="idcliente", blank=True, null=True
    )
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    cancelada = models.BooleanField(blank=True, null=True)
    subtotal = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    impuesto = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    propina = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    concepto = models.CharField(max_length=180, blank=True, null=True)
    usuariocancelo = models.CharField(max_length=15, blank=True, null=True)
    idturno = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    impresiones = models.DecimalField(
        max_digits=3, decimal_places=0, blank=True, null=True
    )
    codigocontrolbolivia = models.CharField(max_length=30, blank=True, null=True)
    propinafacturada = models.BooleanField(blank=True, null=True)
    idempresa = models.ForeignKey(
        Empresas, models.DO_NOTHING, db_column="idempresa", blank=True, null=True
    )
    femexelectronico = models.BooleanField(blank=True, null=True)
    femextipocliente = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    femexxmlvalido = models.TextField(
        blank=True, null=True
    )  # This field type is a guess.
    femexcadenaoriginal = models.TextField(
        blank=True, null=True
    )  # This field type is a guess.
    femexsello = models.TextField(blank=True, null=True)  # This field type is a guess.
    femexnumcertificado = models.CharField(max_length=50, blank=True, null=True)
    femexanioaprobacion = models.DecimalField(
        max_digits=4, decimal_places=0, blank=True, null=True
    )
    femexnumaprobacion = models.CharField(max_length=30, blank=True, null=True)
    fechacancelacion = models.DateTimeField(blank=True, null=True)
    femexdeclarado = models.BooleanField(blank=True, null=True)
    femexdeclaradocancelado = models.BooleanField(blank=True, null=True)
    femexmodogenerado = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    femexrfc = models.CharField(max_length=20, blank=True, null=True)
    femexcbb = models.BinaryField(blank=True, null=True)
    tipoesquema = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    uidtimbre = models.TextField(blank=True, null=True)  # This field type is a guess.
    timbrenocertificadosat = models.TextField(
        db_column="TimbrenoCertificadoSAT", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    timbrefechatimbrado = models.CharField(
        db_column="TimbreFechaTimbrado", max_length=25, blank=True, null=True
    )  # Field name made lowercase.
    timbresellocfd = models.TextField(
        db_column="TimbreselloCFD", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    timbresellosat = models.TextField(
        db_column="TimbreselloSAT", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    timbrecadenaoriginal = models.TextField(
        db_column="TimbreCadenaOriginal", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    imagencfdi = models.BinaryField(
        db_column="ImagenCFDI", blank=True, null=True
    )  # Field name made lowercase.
    femexretencion1 = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    femexretencion2 = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    femexretencion3 = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    ncf = models.CharField(max_length=19, blank=True, null=True)
    regimen = models.CharField(max_length=100, blank=True, null=True)
    formapago = models.CharField(max_length=200, blank=True, null=True)
    numerocuenta = models.CharField(max_length=140, blank=True, null=True)
    expedidoen = models.CharField(max_length=200, blank=True, null=True)
    idunidad = models.CharField(max_length=200, blank=True, null=True)
    pac_reprocesado = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    pac_enviado = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True
    )
    folios_central = models.BooleanField(blank=True, null=True)
    pac = models.IntegerField()
    acusecancelacion = models.TextField()  # This field type is a guess.
    rifdetallado = models.BooleanField(
        db_column="RIFDetallado"
    )  # Field name made lowercase.
    femexenviado = models.BooleanField()
    impuesto1 = models.DecimalField(max_digits=19, decimal_places=4)
    impuesto2 = models.DecimalField(max_digits=19, decimal_places=4)
    impuesto3 = models.DecimalField(max_digits=19, decimal_places=4)
    numautorizacionbolivia = models.CharField(max_length=30)
    descuento = models.DecimalField(max_digits=19, decimal_places=4)
    complementoine = models.BooleanField()
    tipodecambio = models.DecimalField(max_digits=15, decimal_places=4)
    moneda = models.IntegerField()
    esfoliofiscal = models.BooleanField()
    condicionesdepago = models.CharField(max_length=250)
    leyendadesglosefolios = models.CharField(
        db_column="leyendaDesgloseFolios", max_length=250
    )  # Field name made lowercase.
    ordenleyendadesglosefolios = models.SmallIntegerField(
        db_column="ordenLeyendaDesgloseFolios"
    )  # Field name made lowercase.
    versionfacturacion = models.DecimalField(max_digits=16, decimal_places=6)
    cpcliente_sat = models.CharField(
        db_column="cpcliente_SAT", max_length=15
    )  # Field name made lowercase.
    idusocfdi_sat = models.CharField(
        db_column="idusocfdi_SAT", max_length=50
    )  # Field name made lowercase.
    cfdirelacionado_sat = models.CharField(
        db_column="cfdirelacionado_SAT", max_length=50
    )  # Field name made lowercase.
    idprodserv_sat = models.CharField(
        db_column="idprodserv_SAT", max_length=50
    )  # Field name made lowercase.
    idunidad_sat = models.CharField(
        db_column="idunidad_SAT", max_length=50
    )  # Field name made lowercase.
    idmetodopago_sat = models.CharField(
        db_column="idmetodopago_SAT", max_length=50
    )  # Field name made lowercase.
    idpaiscliente_sat = models.CharField(
        db_column="idpaiscliente_SAT", max_length=50
    )  # Field name made lowercase.
    nombre_emisor = models.CharField(max_length=254)
    idregimen_sat = models.CharField(
        db_column="idregimen_SAT", max_length=50
    )  # Field name made lowercase.
    cpemisor_sat = models.CharField(
        db_column="cpemisor_SAT", max_length=15
    )  # Field name made lowercase.
    factura_agrupada = models.BooleanField()
    des_gt_fechavigencia = models.DateTimeField(
        db_column="Des_GT_fechavigencia"
    )  # Field name made lowercase.
    des_gt_consecutivoinicio = models.DecimalField(
        db_column="Des_GT_consecutivoinicio", max_digits=10, decimal_places=0
    )  # Field name made lowercase.
    des_gt_consecutivofin = models.DecimalField(
        db_column="Des_GT_consecutivofin", max_digits=10, decimal_places=0
    )  # Field name made lowercase.
    des_gt_fechaaprobacion = models.DateTimeField(
        db_column="Des_GT_fechaaprobacion"
    )  # Field name made lowercase.
    pendientecancelacion = models.BooleanField()
    fechaenviopendiente = models.DateTimeField(blank=True, null=True)
    usuarioenviopendiente = models.CharField(max_length=15)
    tipocancelacion = models.SmallIntegerField()
    escancelable = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = "facturas"


class Foliosfacturados(models.Model):
    idfactura = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    folio = models.BigIntegerField(blank=True, null=True)
    porcentajefac = models.DecimalField(
        max_digits=11, decimal_places=6, blank=True, null=True
    )
    idturno_cierre = models.BigIntegerField(blank=True, null=True)
    procesado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "foliosfacturados"
