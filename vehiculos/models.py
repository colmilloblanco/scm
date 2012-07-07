# -*- coding: utf-8 *-*
from django.db import models


class PropietarioConductor(models.Model):
    """Contiene los propietarios y conductores"""

    TIPO_PROPIETARIO = (
        ('P', 'PROPIETARIO'),
        ('C', 'CONDUCTOR'),
        ('T', 'CONDUCTOR / PROPIETARIO'),
        )

    TIPO_PERSONA = (
        ('N', 'NATURAL'), 
        ('J', 'JURIDICO'),
    )

    tipo_persona = models.CharField(max_length=1, choices=TIPO_PERSONA)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    movil = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    tipo_propietario = models.CharField(max_length=1, choices=TIPO_PROPIETARIO)
    ruc = models.CharField(max_length=11, null=True, blank=True)
    dni = models.CharField(max_length=8, null=True, blank=True)

    def __unicode__(self):
        documento = ""
        if self.dni:
            documento = self.dni
        else:
            documento = self.ruc

        return "%s - %s" % (self.nombre.upper(), documento)


class LicenciaConducir(models.Model):
    """contiene la licecia (propietarios,conductores)"""
    nro_licencia = models.CharField(max_length=10)
    clase = models.CharField(max_length=3)
    categoria = models.CharField(max_length=3)
    fecha_emision = models.DateField(blank=True, null=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    estado = models.BooleanField()
    propietarioconductor = models.ForeignKey(PropietarioConductor,
                                             blank=True, null=True)

    def __unicode__(self):

        return self.nro_licencia


class Categoria(models.Model):
    """"""
    descripcion = models.CharField(max_length=4, unique=True)

    def __unicode__(self):

        return self.descripcion


class Clase(models.Model):
    """Clase de vehiculos """
    descripcion = models.CharField(max_length=30, unique=True)    

    def __unicode__(self):

        return self.descripcion


class Asociacion(models.Model):
    """Asociacion de vehiculos"""
    nombre = models.CharField(max_length=50, unique=True)
    direccion = models.CharField(max_length=100)

    def __unicode__(self):

        return self.nombre


class Marca(models.Model):
    """Marca de vehiculos"""
    descripcion = models.CharField(max_length=50, unique=True)

    def __unicode__(self):

        return self.descripcion


class Color(models.Model):
    """Colores de vehiculos"""
    descripcion = models.CharField(max_length=50, unique=True)

    def __unicode__(self):

        return self.descripcion


class Modelo(models.Model):
    """Modelos de vehiculos"""
    descripcion = models.CharField(max_length=50, unique=True)

    def __unicode__(self):

        return self.descripcion


class Sede(models.Model):
    """Sede de reqgistros de tarjetas"""
    descripcion = models.CharField(max_length=50, unique=True)

    def __unicode__(self):

        return self.descripcion


class Carroceria(models.Model):
    nombre = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.nombre


class Combustible(models.Model):
    nombre = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.nombre


class Vehiculo(models.Model):
    """Contiene todos los vehiculos"""
    sede = models.ForeignKey(Sede, null=True, blank=True)
    placa_antigua  = models.CharField(max_length=15, null=True,blank=True)
    nro_placa = models.CharField(max_length=15, null=True, blank=True)
    nro_tarjeta = models.CharField(max_length=15, null=True, blank=True)
    year_fabricacion = models.IntegerField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True)
    clase = models.ForeignKey(Clase, null=True, blank=True)
    marca = models.ForeignKey(Marca, null=True, blank=True)
    modelo = models.ForeignKey(Modelo,null=True, blank=True)
    combustible = models.ForeignKey(Combustible, null=True, blank=True)
    carroceria = models.ForeignKey(Carroceria, null=True, blank=True)
    ejes = models.IntegerField(null=True, blank=True)
    color = models.ForeignKey(Color, null=True, blank=True)
    motor = models.CharField(max_length=30, null=True, blank=True)
    serie = models.CharField(max_length=50, unique=True)
    cilindros = models.IntegerField(null=True, blank=True)
    ruedas = models.IntegerField(null=True, blank=True)
    pasajeros = models.IntegerField(null=True, blank=True)
    asientos = models.IntegerField(null=True, blank=True)
    peso_neto = models.IntegerField(null=True, blank=True)
    peso_bruto = models.IntegerField(null=True, blank=True)
    longitud = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    altura = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    ancho = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    carga_util = models.IntegerField(null=True, blank=True)
    estado = models.BooleanField()


    def __unicode__(self):

        placa = ""
        if self.nro_placa:
            placa = self.nro_placa
        else:
            placa = "EN TRAMITE"

        return '(%s) %s' % (placa, self.serie)


class DetalleVehiculo(models.Model):
    """ Contiene la placa actual del vehiculo y su propietario"""
    propietario = models.ForeignKey(PropietarioConductor)
    vehiculo = models.ForeignKey(Vehiculo)
    asociacion = models.ForeignKey(Asociacion, blank=True, null=True)
    estado = models.BooleanField()

    def __unicode__(self):

        return '%s %s' % (self.vehiculo.__str__(), self.propietario.__str__())


class Soat(models.Model):
    """ Contiene soat de Vehiculo"""
    fecha_emision = models.DateField()
    fecha_caducidad = models.DateField()
    estado = models.BooleanField()
    #codigo_soat = models.CharField(max_length=8)
    vehiculo = models.ForeignKey(Vehiculo)

    def __unicode__(self):

        return str(self.estado)


class TarjetaOperatividad(models.Model):
    """Contiene Tarjeta Operatividad de Vehiculos"""

    fecha_expedicion = models.DateField()
    fecha_caducidad = models.DateField()
    estado = models.BooleanField()
    nro_regimen_individual = models.CharField(max_length=20)
    detalle_vehiculo = models.ForeignKey(DetalleVehiculo)
    recibo = models.IntegerField()
